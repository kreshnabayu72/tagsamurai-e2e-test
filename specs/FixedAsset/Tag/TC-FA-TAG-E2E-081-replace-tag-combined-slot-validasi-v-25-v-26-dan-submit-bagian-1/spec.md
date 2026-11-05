---
id: TC-FA-TAG-E2E-081-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-1
title: "Replace dengan Tag Combined: Penolakan pada Replace Satu Slot (V-25), Pindai Sebagian Slot, dan Tag Tunggal Bertabrakan (V-26)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-356
  - TC-FA-TAG-359
  - TC-FA-TAG-360
coverage:
  web: automated
---

# Replace dengan Tag Combined: Penolakan pada Replace Satu Slot (V-25), Pindai Sebagian Slot, dan Tag Tunggal Bertabrakan (V-26)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired; 'Server Rack 42U - 102' (AST-0102, TAG Type Asset Name RFID, NFC, dan QR) dengan Tag RFID `RF-00137`, Tag NFC `NF-00095`, dan Tag QR `QR-00302` Paired, bertipe sesuai; Tag combined RFID+QR `RF-00811` / `QR-00811` Available (satu unit); Tag RFID `RF-00412` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); [Submit] pada langkah 14 tertahan validasi V-28 sehingga tidak ada Replace yang tersimpan dan stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 14 ditolak (V-28) dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Dialog Replace TAG ditutup tanpa menyimpan pada langkah 7, 22, dan 33.

## Test Steps

### TC-FA-TAG-356: Tag combined pada Replace satu slot ditolak V-25

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00811` dengan reader
5. Verifikasi error inline "This TAG is combined. It can only fill multiple slots."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-359: Tag combined sebagian slot hanya mengisi slot yang cocok dan Submit tertahan V-28

7. Klik [Cancel] pada dialog Replace TAG
8. Tutup Popup Detail Assets
9. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
10. Klik row action `Replace TAG` pada baris 'Server Rack 42U - 102'
11. Centang baris `RF-00137`, `NF-00095`, dan `QR-00302`
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
13. Pindai Tag `RF-00811` dengan reader
14. Klik [Submit]
15. Verifikasi slot `RFID TAG` terisi dengan badge `Verified`
16. Verifikasi slot `QR TAG` terisi dengan badge `Verified`
17. Verifikasi slot `NFC TAG` tetap `Not scanned`
18. Verifikasi teks error inline "Please verify the replacement TAG" tampil
19. Verifikasi dialog tetap terbuka

### TC-FA-TAG-360: Tag combined mencakup tipe slot yang sudah terisi Tag tunggal ditolak V-26

20. Klik [Cancel] pada dialog Replace TAG
21. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
22. Klik [Discard]
23. Klik row action `Replace TAG` pada baris 'Server Rack 42U - 102'
24. Centang baris `RF-00137`, `NF-00095`, dan `QR-00302`
25. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
26. Pindai Tag `RF-00412` dengan reader
27. Klik ButtonScan `Scan QR` pada slot `QR TAG`
28. Pindai Tag `RF-00811` dengan reader
29. Verifikasi error inline "This combined TAG doesn't match the open slots."
30. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` dengan badge `Verified`
31. Klik [Cancel] pada dialog Replace TAG
32. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
33. Klik [Discard]
34. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; dialog TC-FA-TAG-359 dan 360 yang terisi ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard]; Popup Detail Assets ditutup sebelum berganti Asset Name; TC-FA-TAG-356 berada di awal karena memakai Popup 'Excavator 20 Ton'.
- Pembagian TC lintas spec: TC-FA-TAG-355, 357, 358, dan 361 sampai 364 ada di spec 082 dan TC-FA-TAG-366 sampai 370 ada di spec 083.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 14 ditolak (V-28) dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Dialog Replace TAG ditutup tanpa menyimpan pada langkah 7, 22, dan 33.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Expected butir b pada TC ini menyebut [Submit] tetap tidak menghasilkan mutasi, tetapi langkah TC tidak memuat klik [Submit]; spec hanya mengasersi slot tetap `Not scanned` dan error inline (TC-FA-TAG-356).
  - Post Condition 'Tidak ada data yang berubah' pada TC-FA-TAG-356, 359, dan 360 tidak punya langkah observasi dan tidak diasersi.
