---
id: TC-FA-TAG-E2E-064-dialog-replace-tag-scan-current-tag-badge-dan-penolakan-bagian-2
title: "Dialog Replace TAG: Scan Current TAG, Penolakan Tag Milik Aset Lain, Tidak Paired, Tidak Dikenal, dan Produk Lain (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-288
  - TC-FA-TAG-289
  - TC-FA-TAG-290
  - TC-FA-TAG-291
  - TC-FA-TAG-292
coverage:
  web: automated
---

# Dialog Replace TAG: Scan Current TAG, Penolakan Tag Milik Aset Lain, Tidak Paired, Tidak Dikenal, dan Produk Lain (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor tambahan (ganti akun lewat langkah eksplisit): Manage asset & TAG (Read + Update) dengan Update pada Group Plant A `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired; 'Excavator 20 Ton - 211' (AST-0211, Group Plant A) dengan Tag RFID `RF-00101` Paired (TC-FA-TAG-288); 'Excavator 20 Ton - 11' (AST-0011, Group Plant B) dengan Tag RFID `RF-00101` Paired (TC-FA-TAG-289; fixture BE memindahkan `RF-00101` dari AST-0211 ke AST-0011 sebelum TC itu); Tag RFID `RF-00600` Available; Tag `SA-00020` terdaftar di produk Supply Asset.
- Cakupan akun tambahan: scope group Update Plant A (AST-0011 di Plant B berada di luar scope).
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-288: Scan Current TAG: Tag milik aset lain menampilkan dialog blok D-05

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
4. Pindai Tag `RF-00101` dengan reader
5. Verifikasi dialog judul "Wrong TAG", body "RF-00101 belongs to AST-0211.", tombol [OK]
6. Verifikasi baris `RF-00130` tidak berstatus terverifikasi
7. Klik [OK]

### TC-FA-TAG-290: Scan Current TAG: Tag tidak Paired menampilkan D-07

8. Klik [Cancel] pada dialog Replace TAG
9. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
10. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
11. Pindai Tag `RF-00600` dengan reader
12. Verifikasi dialog judul "Cannot Replace TAG", body "RF-00600 is not paired to an asset.", tombol [OK]
13. Klik [OK]

### TC-FA-TAG-291: Scan Current TAG: Tag tidak dikenal menampilkan error inline V-23

14. Klik [Cancel] pada dialog Replace TAG
15. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
16. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
17. Pindai Tag `RF-09999` dengan reader
18. Verifikasi error inline "Error, can't recognize TAG."
19. Verifikasi baris `RF-00130` tetap berbadge `Not scanned`

### TC-FA-TAG-292: Scan Current TAG: Tag dipakai produk lain menampilkan pesan inline S-19

20. Klik [Cancel] pada dialog Replace TAG
21. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
22. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
23. Pindai Tag `SA-00020` dengan reader
24. Verifikasi pesan inline "This TAG is used by Supply Asset."
25. Klik [Cancel] pada dialog Replace TAG
26. Tutup Popup Detail Assets
27. Pindahkan Tag `RF-00101` ke aset AST-0011 (Group Plant B) lewat fixture BE

### TC-FA-TAG-289: Scan Current TAG: Tag milik aset di luar scope menampilkan D-06 sebelum D-05

28. Ganti akun: klik Logout
29. Login sebagai Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (`manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`)
30. Buka Fixed Asset > TAG > Paired
31. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
32. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
33. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
34. Pindai Tag `RF-00101` dengan reader
35. Verifikasi dialog judul "Access Restricted", body "You don't have access to this asset.", tombol [OK]
36. Verifikasi dialog D-05 tidak tampil
37. Verifikasi Asset ID AST-0011 tidak ditampilkan
38. Klik [OK]
39. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; [OK] menutup dialog penolakan; urutan TC-FA-TAG-289 dipindah ke akhir karena memakai akun lain (ganti akun lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite); `RF-00101` dipindahkan fixture BE ke AST-0011 sebelum TC-FA-TAG-289.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: semua blok satu kelas (fungsional, penolakan scan), satu dialog dan satu dataset aset; lima TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tambahan langkah berasal dari penghubung antar-TC dan ganti akun.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Tag RFID `RF-00101` Paired di AST-0211 (TC-FA-TAG-288 dan 294) dan di AST-0011 (TC-FA-TAG-289) pada TC; satu kode tidak dapat Paired di dua aset sekaligus, sehingga fixture BE memindahkannya antar-TC.
  - Tidak ada Post Condition berobservasi: 'Tidak ada data yang berubah' pada TC-FA-TAG-288 sampai 292 tidak punya langkah observasi dan tidak diasersi.
