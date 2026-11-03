---
id: TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime
title: "Klik Total Asset: Membuka Tab Assets, Total Asset 0 Empty State, dan Angka Realtime Setelah Aset Ditambah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-277
  - TC-FA-GRP-286
  - TC-FA-GRP-287
  - TC-FA-GRP-292
coverage:
  web: automated
---

# Klik Total Asset: Membuka Tab Assets, Total Asset 0 Empty State, dan Angka Realtime Setelah Aset Ditambah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Warehouse A (Total Asset 24, Code `WH-A`, Description terisi) dan Branch Office (Assignable, tanpa aset aktif, Total Asset 0).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; node level 1 milik spec agar Total Asset Warehouse A tidak berubah, S-06):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-292 | Warehouse A (Total Asset dicatat sebelum uji) | `Count Node {runId}-028` | Level 1, Assignable, berisi 3 aset aktif |
| TC-FA-GRP-292 | aset baru (modul Asset) | `Count Asset {runId}-028` | Didaftarkan ke `Count Node {runId}-028` oleh langkah 20 |

- Kemampuan teknis: fixture BE (seeding group dan aset, pemulihan data milik spec) dan sesi API aktor yang mendaftarkan aset baru pada modul Asset sebagai pemicu state, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-286: Klik angka Total Asset lebih dari 0

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset (24) pada baris Warehouse A
3. Verifikasi Popup Detail Group terbuka pada Tab Assets (aktif)
4. Verifikasi header berisi Group Name Warehouse A (full path), Code `WH-A`, dan Description
5. Verifikasi Toolbar Tab Assets memuat Search, Filter, Download
6. Verifikasi kolom Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated, dan Column Visibility (⋯)
7. Verifikasi kolom Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, dan Custom Field tersembunyi secara default
8. Verifikasi tidak ada kolom Group
9. Verifikasi default sort Name A–Z
10. Verifikasi Tab Users tersedia
11. Tutup popup dengan [X]

### TC-FA-GRP-277: Tab Assets genuine empty state via Detail

12. Ganti isi kotak search dengan `Branch Office`, tekan Enter
13. Klik (⋯) pada baris Branch Office
14. Klik `Detail`
15. Verifikasi area tabel menampilkan Illustration dengan title `No assets assigned` dan body `No assets are currently assigned to this group.`
16. Tutup popup dengan [X]

### TC-FA-GRP-287: Angka Total Asset 0 dapat diklik

17. Klik angka `0` pada baris Branch Office
18. Verifikasi Popup Detail Group terbuka pada Tab Assets
19. Verifikasi empty state Illustration dengan title `No assets assigned` dan body `No assets are currently assigned to this group.`
20. Tutup popup dengan [X]

### TC-FA-GRP-292: Angka realtime setelah aset ditambah

21. Ganti isi kotak search dengan `Count Node {runId}-028`, tekan Enter
22. Catat angka Total Asset pada baris `Count Node {runId}-028` (3)
23. Daftarkan 1 aset baru `Count Asset {runId}-028` ke `Count Node {runId}-028` lewat modul Asset (sesi API) hingga tersimpan
24. Muat ulang halaman Settings > Groups dengan F5
25. Ketik Search `Count Node {runId}-028`, tekan Enter
26. Verifikasi angka Total Asset pada baris `Count Node {runId}-028` bertambah 1 menjadi 4
27. Klik angka Total Asset pada kolom baris `Count Node {runId}-028`
28. Verifikasi Tab Assets berisi 4 aset (bertambah 1 dari angka yang dicatat pada langkah 22)
29. Tutup popup dengan [X]
30. Klik node `Count Node {runId}-028` di sidebar
31. Verifikasi Total Asset di header menjadi 4

## Notes

- Spec 31 langkah, di bawah batas sekitar 35 langkah. Penambahan aset (TC-FA-GRP-292) diletakkan paling akhir (S-10).
- Langkah penghubung (S-03): langkah 11, 16, 20 (menutup popup), langkah 22 (mencatat angka sebagai baseline), langkah 24 (muat ulang sebagai pengganti "Buka Fixed Asset > Settings > Groups" karena halaman sudah dibuka hook `beforeEach`), langkah 30 (memilih node agar header tampil), langkah 27 (klik angka kolom agar tab Assets tampil). Langkah Search (Ketik Search `Warehouse A`, ganti isi kotak search dengan `Branch Office` dan `Count Node {runId}-028`, serta Ketik Search `Count Node {runId}-028` sesudah F5 yang menutup kotak Search) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1 (R-16). Langkah klik angka Total Asset baris `Count Node` dan penutupan popup dikerjakan sebelum memilih node di sidebar, karena sesudah node dipilih tabel berisi direct children node itu dan baris `Count Node` tidak ada lagi.
- Pemicu pelaku kedua lewat sesi API ditulis "... hingga ... tersimpan" (R-20); bukan konteks kedua (P-2 `[KEPUTUSAN 2026-10-30]`).
- Urutan TC dalam spec: 286, 277, 287, 292.
- Temuan untuk QA:
  - TC-FA-GRP-292 menyebut "Warehouse A" untuk uji penambahan aset; spec memakai node milik spec agar Total Asset Warehouse A Tabel A (24) tidak berubah.
  - TC-FA-GRP-292 tidak menyebut cara mendaftarkan aset; spec memakai sesi API modul Asset (disediakan tim FE/BE tanpa endpoint karangan).
