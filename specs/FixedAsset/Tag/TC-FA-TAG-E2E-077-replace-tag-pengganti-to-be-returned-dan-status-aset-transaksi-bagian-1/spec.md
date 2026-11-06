---
id: TC-FA-TAG-E2E-077-replace-tag-pengganti-to-be-returned-dan-status-aset-transaksi-bagian-1
title: "Replace: Tag Pengganti To be Returned Diterima bila Return Group Berhak Update dan Ditolak bila Hanya Read atau di Luar Scope (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-345
  - TC-FA-TAG-346
  - TC-FA-TAG-347
coverage:
  web: automated
---

# Replace: Tag Pengganti To be Returned Diterima bila Return Group Berhak Update dan Ditolak bila Hanya Read atau di Luar Scope (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor tambahan (ganti akun lewat langkah eksplisit): Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD`.
- Akun aktor tambahan (ganti akun lewat langkah eksplisit): Manage asset & TAG (Read + Update) dengan Update pada Group Plant A `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired; Tag RFID `RF-00071` To be Returned dengan Return Group 'Disposal Center' yang dipegang Update oleh Total Control; Tag RFID `RF-00072` To be Returned dengan Return Group 'Plant B' yang hanya dipegang Read oleh akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B; Tag RFID `RF-00073` To be Returned dengan Return Group 'Plant C' di luar scope akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7); entri TAG Log Global (langkah 7); entri Event Log To Be Returned (Method `Assigned`) (langkah 7).

## Test Steps

### TC-FA-TAG-345: Tag pengganti To be Returned dengan Return Group berhak Update diterima dan langsung Paired

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00071` dengan reader
5. Verifikasi slot `RFID TAG` menerima kode `RF-00071`
6. Verifikasi slot `RFID TAG` menampilkan badge `Verified`
7. Klik [Submit]
8. Verifikasi toast "Success, TAG has been replaced."
9. Tutup Popup Detail Assets

### TC-FA-TAG-346: Tag pengganti To be Returned dengan Return Group hanya Read ditolak V-07

10. Ganti akun: klik Logout
11. Login sebagai Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B (`manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD`)
12. Buka Fixed Asset > TAG > Paired
13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
16. Pindai Tag `RF-00072` dengan reader
17. Verifikasi error inline "RF-00072 is not available (To be Returned)."
18. Verifikasi slot `RFID TAG` tetap `Not scanned`
19. Klik [Cancel] pada dialog Replace TAG
20. Tutup Popup Detail Assets

### TC-FA-TAG-347: Tag pengganti To be Returned dengan Return Group di luar scope ditolak V-07

21. Ganti akun: klik Logout
22. Login sebagai Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (`manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`)
23. Buka Fixed Asset > TAG > Paired
24. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
25. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
26. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
27. Pindai Tag `RF-00073` dengan reader
28. Verifikasi error inline "RF-00073 is not available (To be Returned)."
29. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): Ganti akun lewat langkah eksplisit (Logout, login, buka halaman) sebelum TC-FA-TAG-346 dan 347, hook `after` mengembalikan sesi ke akun default suite; Popup Detail Assets ditutup sebelum ganti akun; pemulihan Tag `RF-00330` Paired dan `RF-00071` To be Returned antar-TC dilakukan fixture BE di hook `before`.
- Pembagian TC lintas spec: TC-FA-TAG-348 dan 349 ada di spec 079 dan TC-FA-TAG-350 sampai 353 ada di spec 078.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7); entri TAG Log Global (langkah 7); entri Event Log To Be Returned (Method `Assigned`) (langkah 7).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-345 (`RF-00071` Paired tanpa langkah Receive, hilang dari tab To Be Returned, satu entri Event Log To Be Returned dengan Method `Assigned` dan Final Status `Paired`, TAG Log Paired dengan Previous Status To be Returned), TC-FA-TAG-346 dan 347 (Tag tetap To be Returned).
  - TC-FA-TAG-345 menaruh entri Event Log dan hilangnya Tag dari tab To Be Returned hanya di Post Condition tanpa langkah observasi; QA perlu menambah Expected atau langkah observasinya.
  - Role TC-FA-TAG-345 adalah Total Control, sedangkan Precondition menyebut Return Group 'Disposal Center' sebagai 'dipegang Update oleh user'; spec mengikuti Role TC.
