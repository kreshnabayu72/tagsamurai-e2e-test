---
id: TC-FA-TAG-E2E-391-replace-tag-berlaporan-terbuka-bertipe-terkunci-plan-dilepas-tanpa-pasangan
title: "Replace: Tag Berlaporan Terbuka Bertipe Terkunci Plan Dilepas Tanpa Pasangan dan Laporan Ditutup"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1508
coverage:
  web: automated
---

# Replace: Tag Berlaporan Terbuka Bertipe Terkunci Plan Dilepas Tanpa Pasangan dan Laporan Ditutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) perubahan plan Client (plan yang hanya mengizinkan Tag RFID dan QR, NFC terkunci) lewat fixture backend atau pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, dan laporan Tag; pembacaan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah plan Client dan menutup laporan Tag.
- Data: aset 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` (laporan terbuka, Report Type Damaged) dan Tag QR `QR-00300` (tanpa laporan) Paired.
- State yang diubah dan pemulihannya: Client berada di plan dengan NFC terkunci sepanjang spec (diatur hook `before`); langkah 7 menutup laporan `NF-00292` dan melepas Tag itu. Hook `after` memulihkan plan awal Client dan data aset walau spec gagal di tengah. Efek yang tidak terpulihkan: entri Changelog `Replace` aset AST-0108 (langkah 7); entri TAG Log Global (langkah 7).
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-1508: Tag berlaporan terbuka bertipe terkunci plan dilepas tanpa pasangan dan laporan ditutup

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Verifikasi row action `Replace TAG` pada baris 'Laptop Pro 14 - 8' Enabled
3. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
4. Verifikasi baris `NF-00292` tercentang dan checkbox Disabled
5. Verifikasi Alert info "This TAG type is not available on your plan." tampil di atas bagian `Replacement TAG`
6. Verifikasi bagian `Replacement TAG` memuat empty state "No replacement needed."
7. Klik [Submit]
8. Verifikasi toast "Success, TAG has been replaced."

## Notes

- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Pembagian TC lintas spec: TC-FA-TAG-1504 sampai 1507 (Tag berlaporan terbuka tercentang dan terkunci) ada di spec 390.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1508 (laporan `NF-00292` ditutup `Replaced`, `NF-00292` dilepas tanpa pasangan dengan New Value Changelog `—`, `QR-00300` tetap Paired) tidak punya langkah observasi di TC dan tidak diasersi.
