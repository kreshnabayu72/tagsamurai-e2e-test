---
id: TC-FA-TAG-E2E-067-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-3
title: "Dialog Replace TAG: Scan Tag Pengganti, Penolakan Tidak Berlaku di Client, Tipe Tidak Sesuai, Tag Sama, dan Produk Supply Asset (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-303
  - TC-FA-TAG-304
  - TC-FA-TAG-305
  - TC-FA-TAG-306
  - TC-FA-TAG-1461
coverage:
  web: automated
---

# Dialog Replace TAG: Scan Tag Pengganti, Penolakan Tidak Berlaku di Client, Tipe Tidak Sesuai, Tag Sama, dan Produk Supply Asset (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired; Tag RFID `RF-00605` terdaftar tetapi tidak berlaku di client ini; Tag NFC `NF-00500` Available; Tag `SA-00020` terdaftar di produk Supply Asset (stok dan SKU); kode `RF-09999` belum diaktivasi di Global; Tag RFID `RF-00412` Available.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-303: Tag pengganti yang tidak berlaku di client ini ditolak V-27

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00605` dengan reader
5. Verifikasi error inline "Error, TAG isn't authorized. Please contact Admin."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-304: Tag pengganti bertipe tidak sesuai slot ditolak V-08

7. Klik [Cancel] pada dialog Replace TAG
8. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
9. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
10. Pindai Tag `NF-00500` dengan reader
11. Verifikasi error inline "This slot needs a RFID TAG."
12. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-305: Tag pengganti sama dengan Tag lama menampilkan caption S-33 dan tidak diterima

13. Klik [Cancel] pada dialog Replace TAG
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
16. Pindai Tag `RF-00130` dengan reader
17. Verifikasi caption "This TAG is the same as the current TAG."
18. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-1461: Tag milik produk Supply Asset di slot pengganti menampilkan S-19, bukan V-07

19. Klik [Cancel] pada dialog Replace TAG
20. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
21. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
22. Pindai Tag `SA-00020` dengan reader
23. Verifikasi pesan inline "This TAG is used by Supply Asset." tampil pada slot `RFID TAG`
24. Verifikasi pesan V-07 "[TAG Code] is not available ([Status])." tidak tampil
25. Verifikasi slot `RFID TAG` tetap `Not scanned` dan tidak terverifikasi

### TC-FA-TAG-306: Pindai ulang Tag valid setelah penolakan mengisi slot pengganti

26. Klik [Cancel] pada dialog Replace TAG
27. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
28. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
29. Pindai Tag `RF-09999` dengan reader
30. Verifikasi error inline "Error, can't recognize TAG."
31. Pindai Tag `RF-00412` dengan reader
32. Verifikasi error inline hilang
33. Verifikasi slot `RFID TAG` menampilkan kode `RF-00412`
34. Verifikasi slot `RFID TAG` menampilkan badge `Verified`
35. Klik [Cancel] pada dialog Replace TAG
36. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
37. Klik [Discard]

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; TC-FA-TAG-306 dipindah ke akhir karena menyisakan slot terisi (dirty), ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard].
- Pembagian TC lintas spec: TC-FA-TAG-293 sampai 302 ada di spec 065 dan 066.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: semua blok satu kelas (fungsional, penolakan scan), satu dialog dan satu aset; lima TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tambahan langkah berasal dari penghubung antar-TC dan penutupan dialog dirty.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Expected butir b pada TC ini menyebut [Submit] tetap tidak menghasilkan mutasi, tetapi langkah TC tidak memuat klik [Submit]; spec hanya mengasersi slot tetap `Not scanned` dan error inline (TC-FA-TAG-303 sampai 305, 1461).
  - Post Condition 'Tidak ada data yang berubah' pada TC-FA-TAG-303 sampai 305 dan 1461 tidak punya langkah observasi dan tidak diasersi.
