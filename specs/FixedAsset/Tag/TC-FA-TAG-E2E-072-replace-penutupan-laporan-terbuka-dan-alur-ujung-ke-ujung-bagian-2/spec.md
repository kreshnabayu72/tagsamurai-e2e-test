---
id: TC-FA-TAG-E2E-072-replace-penutupan-laporan-terbuka-dan-alur-ujung-ke-ujung-bagian-2
title: "Replace: Laporan Terbuka pada Tag yang Dilepas Ditutup Replaced dan Status Tag Reported Dicabut"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-340
  - TC-FA-TAG-1378
coverage:
  web: automated
---

# Replace: Laporan Terbuka pada Tag yang Dilepas Ditutup Replaced dan Status Tag Reported Dicabut

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired dan laporan terbuka (Report Type Damaged), berbadge `Tag Reported` dan dihitung di kartu Reported; aset AST-0020 ('Excavator 20 Ton - 20', Group Plant B) dengan Tag tunggal `RF-00130` dan laporan terbuka Damaged dari Staff Auditor (diatur fixture BE sebelum TC-FA-TAG-1378); Tag RFID `RF-00412` dan `RF-00500` Available.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6, 18); entri TAG Log Global (langkah 6, 18).

## Test Steps

### TC-FA-TAG-340: Replace menutup laporan terbuka pada Tag yang dilepas dan mencabut status Tag Reported

1. Catat angka kartu `Reported` grup Excavator 20 Ton Plant A sebelum aksi
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
5. Pindai Tag `RF-00412` dengan reader
6. Klik [Submit]
7. Verifikasi toast "Success, TAG has been replaced."
8. Verifikasi pada baris 'Excavator 20 Ton - 220' badge `Tag Reported` hilang
9. Verifikasi row action `Decline Report` tidak lagi tersedia untuk aset itu
10. Tutup Popup Detail Assets
11. Verifikasi angka kartu `Reported` pada grup berkurang 1 dari angka yang dicatat

### TC-FA-TAG-1378: Replace menutup laporan terbuka dengan status Replaced

12. Pulihkan lewat fixture BE: Tag tunggal `RF-00130` pada AST-0020 dengan laporan terbuka Damaged dari Staff Auditor, dan Tag `RF-00500` Available
13. Catat angka kartu `Reported` sebelum aksi
14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
15. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 20'
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
17. Pindai Tag `RF-00500` dengan reader
18. Klik [Submit]
19. Verifikasi (baca lewat fixture BE) laporan `RF-00130` berstatus Replaced
20. Verifikasi aset 'Excavator 20 Ton - 20' tidak lagi berstatus `Tag Reported`
21. Tutup Popup Detail Assets
22. Verifikasi kartu `Reported` berkurang satu dari angka yang dicatat

## Notes

- Langkah penghubung (S-03): Pencatatan angka kartu `Reported` adalah langkah baseline tanpa asersi; Popup Detail Assets ditutup sebelum membaca kartu; pemulihan data lewat fixture BE sebelum TC-FA-TAG-1378.
- Pembagian TC lintas spec: TC-FA-TAG-324 sampai 326 ada di spec 071.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6, 18); entri TAG Log Global (langkah 6, 18).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-340 (laporan `RF-00330` ditutup `Replaced`, aset keluar dari Reported, modul Asset tagging) tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-TAG-1378 hanya menyebut Tag lama `RF-00130` tanpa dipindai; spec tidak menambah langkah pindai Tag lama.
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
