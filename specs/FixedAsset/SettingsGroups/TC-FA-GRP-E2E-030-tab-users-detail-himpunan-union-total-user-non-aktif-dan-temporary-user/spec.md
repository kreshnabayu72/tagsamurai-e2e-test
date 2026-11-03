---
id: TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user
title: "Tab Users Detail Group: Himpunan UNION Total User, Total User Tidak Pernah 0, dan User Non-Aktif/Temporary User Lewat Temporary Until"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-293
  - TC-FA-GRP-294
  - TC-FA-GRP-295
  - TC-FA-GRP-988
coverage:
  web: automated
---

# Tab Users Detail Group: Himpunan UNION Total User, Total User Tidak Pernah 0, dan User Non-Aktif/Temporary User Lewat Temporary Until

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Warehouse A dengan 1 user Group Role, 1 user Group Manager langsung, 1 user Transaction Role approver (tidak dihitung), 1 user Group Role di Rack 1 (child, tidak dihitung), 1 user Home Group Warehouse A tanpa role (tidak dihitung); client punya 2 Total Control, 1 Default User, dan 1 Read Only. Branch Office tanpa assignment. Total User Warehouse A = 6.
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; node level 1 milik spec agar Total User Warehouse A tidak berubah, S-06):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-988 | Warehouse A | `User State Node {runId}-030` | Level 1, Assignable, kosong aset |
| TC-FA-GRP-988 | user A | `userA+{runId}-030@qwertysystem.net` | Activation Status non-aktif, ber-Group Role pada node |
| TC-FA-GRP-988 | user B | `userB+{runId}-030@qwertysystem.net` | Temporary User dengan Temporary Until sudah lewat, ber-Group Role pada node |

- Setup Column Tab Users: kolom Activation Status dan Temporary Until ditampilkan oleh langkah 27 sampai 29; konfigurasi kolom dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat [Reset to Default]).
- Kemampuan teknis: fixture BE (seeding, pembacaan himpunan user distinct per node, pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini mengubah konfigurasi kolom Tab Users akun aktor (dipulihkan di hook `after`) dan tidak mengubah state global lain.

## Test Steps

### TC-FA-GRP-293: Klik angka Total User membuka Tab Users

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total User pada baris Warehouse A
3. Verifikasi Popup Detail Group terbuka pada Tab Users (aktif)
4. Verifikasi header berisi Group Name Warehouse A (full path), Code, dan Description
5. Verifikasi Toolbar Tab Users memuat Search, Filter, Download
6. Verifikasi kolom Name ([Avatar] Full Name), Email, Position, Division, Group Role, dan Column Visibility (⋯)
7. Verifikasi kolom Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif tersembunyi secara default
8. Verifikasi default sort Name A–Z
9. Verifikasi Tab Assets tersedia
10. Tutup popup dengan [X]

### TC-FA-GRP-294: Total User, himpunan UNION exact-match

11. Verifikasi angka Total User pada baris Warehouse A adalah 6 (2 assignment langsung, 2 Total Control, 1 Default User, 1 Read Only)
12. Verifikasi user Transaction Role approver tidak dihitung dalam angka itu
13. Klik angka Total User pada baris Warehouse A
14. Verifikasi himpunan baris Tab Users sama dengan himpunan 6 user pembacaan fixture BE, tanpa user Rack 1 dan tanpa user Home Group-only
15. Tutup popup dengan [X]

### TC-FA-GRP-295: Total User tidak pernah 0

16. Ganti isi kotak search dengan `Branch Office`, tekan Enter
17. Verifikasi angka Total User pada baris Branch Office bernilai 1 atau lebih dan tampil sebagai elemen yang dapat diklik
18. Klik angka Total User pada baris Branch Office
19. Verifikasi Tab Users berisi seluruh Total Control, Default User, dan Read Only client sesuai pembacaan fixture BE
20. Tutup popup dengan [X]

### TC-FA-GRP-988: Total User menghitung user non-aktif dan Temporary User kedaluwarsa

21. Ganti isi kotak search dengan `User State Node {runId}-030`, tekan Enter
22. Catat angka Total User pada baris `User State Node {runId}-030` di tabel
23. Verifikasi angka itu menghitung user A dan user B sesuai pembacaan fixture BE
24. Klik node `User State Node {runId}-030` di sidebar
25. Verifikasi Total User di header sama dengan angka yang dicatat pada langkah 22
26. Klik angka Total User pada header
27. Klik header kolom Column Visibility (⋯) pada Tab Users
28. Centang kolom Activation Status dan Temporary Until pada Setup Column
29. Klik [Save]
30. Verifikasi kolom Activation Status dan Temporary Until tampil pada Tab Users
31. Verifikasi baris user A dan user B tampil pada Tab Users
32. Verifikasi Activation Status user A non-aktif dan Temporary Until user B berisi tanggal yang sudah lewat, hanya sebagai informasi
33. Verifikasi jumlah baris Tab Users sama dengan angka pada langkah 22 dan 25
34. Tutup popup dengan [X]

## Notes

- Spec 34 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 10, 15, 20, 34 (menutup popup), langkah 22 (mencatat angka sebagai baseline), langkah 24 (memilih node agar header tampil), langkah 26 sampai 29 (menampilkan kolom curated sebagai precondition asersi TC-FA-GRP-988). Langkah 1, 16, dan 21 (Ketik Search `Warehouse A`, lalu ganti isi kotak search dengan `Branch Office` dan `User State Node {runId}-030`) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; Search tetap aktif selama popup dibuka dan ditutup (R-16).
- Urutan TC dalam spec: 293, 294, 295, 988 (TC-FA-GRP-988 terakhir karena mengubah konfigurasi kolom).
- Temuan untuk QA:
  - TC-FA-GRP-988 memakai Warehouse A sebagai node pengujian user A dan B; spec memakai node bersuffix milik spec agar Total User Warehouse A (6) tidak berubah.
  - TC-FA-GRP-294 tidak menyebut identitas user pada himpunan 6; spec mengasersi lewat jumlah dan himpunan hasil pembacaan fixture BE.
  - TC-FA-GRP-988 butir b ("hanya informasi") tidak menyebut nilai kolom; spec mengasersi nilai Activation Status non-aktif dan Temporary Until lewat.
