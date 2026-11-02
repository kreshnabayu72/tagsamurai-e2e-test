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

- Setup Column Tab Users: kolom Activation Status dan Temporary Until ditampilkan oleh langkah 24 sampai 26; konfigurasi kolom dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat [Reset to Default]).
- Kemampuan teknis: fixture BE (seeding, pembacaan himpunan user distinct per node, pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini mengubah konfigurasi kolom Tab Users akun aktor (dipulihkan di hook `after`) dan tidak mengubah state global lain.

## Test Steps

### TC-FA-GRP-293: Klik angka Total User membuka Tab Users

1. Klik angka Total User pada baris Warehouse A
2. Verifikasi Popup Detail Group terbuka pada Tab Users (aktif)
3. Verifikasi header berisi Group Name Warehouse A (full path), Code, dan Description
4. Verifikasi Toolbar Tab Users memuat Search, Filter, Download
5. Verifikasi kolom Name ([Avatar] Full Name), Email, Position, Division, Group Role, dan Column Visibility (⋯)
6. Verifikasi kolom Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif tersembunyi secara default
7. Verifikasi default sort Name A–Z
8. Verifikasi Tab Assets tersedia
9. Tutup popup dengan [X]

### TC-FA-GRP-294: Total User, himpunan UNION exact-match

10. Verifikasi angka Total User pada baris Warehouse A adalah 6 (2 assignment langsung, 2 Total Control, 1 Default User, 1 Read Only)
11. Verifikasi user Transaction Role approver tidak dihitung dalam angka itu
12. Klik angka Total User pada baris Warehouse A
13. Verifikasi himpunan baris Tab Users sama dengan himpunan 6 user pembacaan fixture BE, tanpa user Rack 1 dan tanpa user Home Group-only
14. Tutup popup dengan [X]

### TC-FA-GRP-295: Total User tidak pernah 0

15. Verifikasi angka Total User pada baris Branch Office bernilai 1 atau lebih dan tampil sebagai elemen yang dapat diklik
16. Klik angka Total User pada baris Branch Office
17. Verifikasi Tab Users berisi seluruh Total Control, Default User, dan Read Only client sesuai pembacaan fixture BE
18. Tutup popup dengan [X]

### TC-FA-GRP-988: Total User menghitung user non-aktif dan Temporary User kedaluwarsa

19. Catat angka Total User pada baris `User State Node {runId}-030` di tabel
20. Verifikasi angka itu menghitung user A dan user B sesuai pembacaan fixture BE
21. Klik node `User State Node {runId}-030` di sidebar
22. Verifikasi Total User di header sama dengan angka yang dicatat pada langkah 19
23. Klik angka Total User pada header
24. Klik header kolom Column Visibility (⋯) pada Tab Users
25. Centang kolom Activation Status dan Temporary Until pada Setup Column
26. Klik [Save]
27. Verifikasi kolom Activation Status dan Temporary Until tampil pada Tab Users
28. Verifikasi baris user A dan user B tampil pada Tab Users
29. Verifikasi Activation Status user A non-aktif dan Temporary Until user B berisi tanggal yang sudah lewat, hanya sebagai informasi
30. Verifikasi jumlah baris Tab Users sama dengan angka pada langkah 19 dan 22
31. Tutup popup dengan [X]

## Notes

- Spec 31 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 9, 14, 18, 31 (menutup popup), langkah 19 (mencatat angka sebagai baseline), langkah 21 (memilih node agar header tampil), langkah 23 sampai 26 (menampilkan kolom curated sebagai precondition asersi TC-FA-GRP-988).
- Urutan TC dalam spec: 293, 294, 295, 988 (TC-FA-GRP-988 terakhir karena mengubah konfigurasi kolom).
- Temuan untuk QA:
  - TC-FA-GRP-988 memakai Warehouse A sebagai node pengujian user A dan B; spec memakai node bersuffix milik spec agar Total User Warehouse A (6) tidak berubah.
  - TC-FA-GRP-294 tidak menyebut identitas user pada himpunan 6; spec mengasersi lewat jumlah dan himpunan hasil pembacaan fixture BE.
  - TC-FA-GRP-988 butir b ("hanya informasi") tidak menyebut nilai kolom; spec mengasersi nilai Activation Status non-aktif dan Temporary Until lewat.
