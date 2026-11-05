---
id: TC-FA-TAG-E2E-084-replace-satu-tag-non-standard-dengan-dua-tipe-wajib-kosong
title: "Replace: Satu Tag Non-standard dengan Dua Tipe Wajib Kosong Hanya Mendapat Satu Slot"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1483
coverage:
  web: automated
---

# Replace: Satu Tag Non-standard dengan Dua Tipe Wajib Kosong Hanya Mendapat Satu Slot

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Laptop Pro 14 - 36' (AST-0136, Group Plant A, TAG Type Asset Name NFC dan QR) dengan satu Tag RFID Paired `RF-00135` (Non-standard), tanpa Tag NFC maupun QR; Tag NFC `NF-00500` dan Tag QR `QR-00701` Available (stok Global).
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7); entri TAG Log Global (langkah 7).

## Test Steps

### TC-FA-TAG-1483: Replace satu Tag Non-standard dengan dua tipe wajib kosong: hanya satu slot, tipe pertama menurut urutan TAG Type Asset Name

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 36'
3. Verifikasi bagian `Replacement TAG` hanya memuat satu slot `NFC TAG` (tipe pertama menurut urutan TAG Type Asset Name)
4. Verifikasi slot `QR TAG` tidak tampil karena satu Tag di daftar lepas hanya mendapat satu slot
5. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
6. Pindai Tag `NF-00500` dengan reader
7. Klik [Submit]
8. Verifikasi Submit sukses: (baca lewat fixture BE) Tag `NF-00500` Paired pada 'Laptop Pro 14 - 36'
9. Verifikasi (baca lewat fixture BE) aset 'Laptop Pro 14 - 36' tidak punya Tag QR
10. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup di akhir spec. Tag lama `RF-00135` tidak dipindai sesuai data TC.
- Pembagian TC lintas spec: TC-FA-TAG-1478 dan 1479 ada di spec 080.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7); entri TAG Log Global (langkah 7).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Tag RFID `RF-00135` Paired (Non-standard) pada TC-FA-TAG-1483 dipasang di AST-0136, sedangkan TC-FA-TAG-335 memasangnya di AST-0111; satu kode tidak dapat Paired di dua aset sekaligus. Spec mengikuti TC dan fixture BE menyiapkannya per spec.
  - Post Condition TC-FA-TAG-1483 (`RF-00135` Damaged/Missing, `QR-00701` tetap Available) tidak punya langkah observasi di TC dan tidak diasersi.
