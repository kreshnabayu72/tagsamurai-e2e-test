---
id: TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover
title: "Screening Groups List All Groups: Header, Kolom, Format Sel, Nama 120 Karakter, Hover Nama dan Table Tools, Halaman Tanpa Page Title"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1
  - TC-FA-GRP-2
  - TC-FA-GRP-3
  - TC-FA-GRP-4
  - TC-FA-GRP-5
  - TC-FA-GRP-952
coverage:
  web: automated
---

# Screening Groups List All Groups: Header, Kolom, Format Sel, Nama 120 Karakter, Hover Nama dan Table Tools, Halaman Tanpa Page Title

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) termasuk Default Group, Head Office, Warehouse A, Branch Office, Warehouse B (Excess). Node level 1 client lebih dari 10 dan page size 10, sehingga baris target yang dinamai (bukan baris pertama) dicari dengan Search, bukan diandalkan berada di halaman 1.
- Data Dinamis (di-seed di hook `before`, dihapus di hook `after`):

| TC | Nama TC | Nama seed | Keterangan |
|---|---|---|---|
| TC-FA-GRP-3, 4 | group bernama 120 karakter (Tabel B TC) | `Aa-{runId}-001-` dilengkapi huruf `a` sampai tepat 120 karakter termasuk suffix | Level 1, Function None, diawali `Aa` agar menjadi baris pertama pada urutan Group A-Z |

- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec, pembacaan agregat Total Asset dan Total User client) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-1: Screening Groups List All Groups

1. Verifikasi Breadcrumb `Settings > Groups` tampil dengan dua segmen
2. Verifikasi tidak ada segmen Breadcrumb yang dapat diklik
3. Verifikasi Group Context Header memuat satu judul `All Groups` diikuti dua metrik berlabel `Total Asset: [N]` dan `Total User: [N]`
4. Verifikasi angka Total Asset dan Total User header sama dengan agregat seluruh client (distinct dedup) yang dibaca lewat fixture BE
5. Verifikasi Table Tools di kanan memuat ikon `Search`, `Filter`, `Download`, `Changelog`
6. Verifikasi Table Tools tidak memuat tombol create
7. Verifikasi urutan kolom tabel: Checkbox, Group, Code, Function, Total Asset, Total User, Modified By, Last Updated, Column Visibility (⋯)
8. Verifikasi kolom Group, Code, Function, Total Asset, Total User, Modified By, Last Updated dapat di-sort dan kolom Column Visibility (⋯) tidak dapat di-sort
9. Klik header Column Visibility (⋯)
10. Verifikasi overlay Column Visibility terbuka
11. Tutup overlay Column Visibility dengan Esc
12. Klik (⋯) pada baris pertama
13. Verifikasi row action menu terbuka pada kolom Column Visibility (⋯) baris itu
14. Tutup row action menu dengan Esc
15. Verifikasi baris tabel adalah node level 1 client dengan urutan Group A→Z case-insensitive
16. Verifikasi sidebar kanan memuat Title `Groups`, Search sidebar sejajar toggle expand/collapse-all, lalu tombol [+] Group, berurutan dari atas
17. Verifikasi node `All Groups` aktif secara default di sidebar
18. Verifikasi pagination footer default 10 per halaman

### TC-FA-GRP-952: Halaman tanpa Page Title terpisah

19. Verifikasi tidak ada Page Title `Groups` terpisah di bawah Breadcrumb dan konten langsung dimulai di SectionCard (Breadcrumb tampil pada langkah 1)

### TC-FA-GRP-2: Format sel Groups List

20. Verifikasi badge Function: Assignable berupa badge primary, None berupa `—`
21. Verifikasi Total Asset berupa angka bulat dan angka `0` (Branch Office) tampil sebagai elemen yang dapat diklik
22. Verifikasi Total User berupa angka bulat dan tidak pernah `0`
23. Verifikasi kolom Modified By berformat `[First Name] [Last Initial]`
24. Hover nilai pada kolom Modified By
25. Verifikasi tooltip menampilkan nama lengkap pengguna
26. Verifikasi Last Updated mengikuti format tanggal-waktu General Settings
27. Ketik Search `Warehouse B`, tekan Enter
28. Verifikasi nama Warehouse B (Excess) di-dim tanpa badge tambahan
29. Klik `(←)` pada kotak Search

### TC-FA-GRP-3: Nama group 120 karakter

30. Verifikasi nama group 120 karakter tampil utuh (wrap/hug content), tidak dipotong `..`
31. Hover nama group 120 karakter
32. Verifikasi tidak ada tooltip yang tampil
33. Verifikasi row height kolom lain pada baris itu tetap 1 baris

### TC-FA-GRP-4: Hover nama Group

34. Hover nama Group pada baris pertama
35. Verifikasi warna teks berubah ke primary Fixed Asset (biru)
36. Verifikasi nama Group tidak bergaris bawah
37. Verifikasi kursor berupa pointer

### TC-FA-GRP-5: Hover icon Table Tools

38. Hover ikon `Search`
39. Verifikasi tooltip `Search` tampil
40. Hover ikon `Filter`
41. Verifikasi tooltip `Filter` tampil
42. Hover ikon `Download`
43. Verifikasi tooltip `Download` tampil
44. Hover ikon `Changelog`
45. Verifikasi tooltip `Changelog` tampil
46. Hover ikon (⋯) pada header kolom Column Visibility
47. Verifikasi tooltip nama aksi ikon (⋯) header tampil

## Notes

- Spec melewati sekitar 35 langkah (47 langkah): seluruh blok adalah screening satu kelas pada layar dan dataset yang sama (Groups List All Groups), tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan cleanup tanpa alur baru.
- Langkah penghubung (S-03): langkah 11 dan 14 (menutup overlay dan menu agar langkah berikutnya tidak tertutup), langkah 24 dan 31 (hover sebagai pemicu tooltip), langkah 27 dan 29 (Search `Warehouse B` lalu `(←)` agar tabel penuh kembali; baris tidak diandalkan berada di halaman 1; R-16).
- Urutan TC dalam spec: 1, 952, 2, 3, 4, 5 (screening statis di awal, aksi hover paling akhir; S-10).
- Temuan untuk QA:
  - TC-FA-GRP-3 dan 1093 menyebut "group bernama 120 karakter (Tabel B)", tetapi Tabel Data Uji Dinamis TC tidak memuat baris group 120 karakter; spec memakai seed bernama 120 karakter bersuffix (S-12).
  - TC-FA-GRP-5 hanya menyebut "tooltip nama aksinya"; teks tooltip yang diasersi adalah nama ikon (`Search`, `Filter`, `Download`, `Changelog`) dan nama aksi ikon (⋯) tidak disebut TC.
  - TC-FA-GRP-1 tidak menyebut cara membaca agregat distinct dedup; spec memakai pembacaan state lewat fixture BE (disediakan tim FE/BE).
  - TC-FA-GRP-2 menyebut data pre-setup "Tabel A (Default Group, Head Office, ...)" tanpa nilai Total Asset dan Total User per baris; spec mengasersi format, bukan nilai.
