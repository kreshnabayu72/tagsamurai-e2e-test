---
id: TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search
title: "Tab User Log sub-tab Borrow: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-805
  - TC-FA-SU-806
  - TC-FA-SU-807
  - TC-FA-SU-808
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-805: Screening Table Tools, kolom, dan default sort

2. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi placeholder Search `Search transaction ID, name, or PIC...` tampil
7. Klik `←` pada kotak Search
8. Hover icon Filter
9. Verifikasi tooltip `Filter` tampil
10. Hover icon Download
11. Verifikasi tooltip `Download` tampil
12. Verifikasi kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `PIC`, dan header kolom `⋯` (Column Visibility)
13. Verifikasi kolom `Date`, `Transaction ID`, `Name`, dan `PIC` sortable (memiliki icon sort)
14. Verifikasi kolom `Activity` unsortable (tanpa icon sort)
15. Verifikasi kolom `⋯` pada setiap baris kosong tanpa row action
16. Klik header kolom `⋯`
17. Verifikasi overlay Column Visibility terbuka
18. Tutup overlay Column Visibility dengan Esc
19. Verifikasi lima baris teratas default sort Date descending: `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260712-0347`, `Returned|BRW-20260615-0305`, `Borrowed|BRW-20260320-0188`, `Returned|BRW-20260205-0102`
20. Verifikasi footer pagination menampilkan 10 data per halaman
21. Klik dropdown page size
22. Verifikasi pilihan page size 10, 25, 50, 100
23. Tutup dropdown page size dengan Esc

### TC-FA-SU-806: Search kelas enum, kolom Activity

24. Ketik Search `Returned`, tekan Enter
25. Verifikasi tabel menyisakan `Returned|BRW-20260320-0188`, `Returned|BRW-20260615-0305`, `Returned|BRW-20260205-0102` (3 baris)
26. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-807: Search kelas teks, kolom Transaction ID dan Name

27. Ketik Search `0188`, tekan Enter
28. Verifikasi tabel menyisakan `Returned|BRW-20260320-0188`, `Borrowed|BRW-20260320-0188` (2 baris)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `Monitor`, tekan Enter
31. Verifikasi tabel menyisakan `Returned|BRW-20260615-0305` (1 baris)
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-808: Search kelas user, kolom PIC

33. Ketik Search `Lestari`, tekan Enter
34. Verifikasi tabel menyisakan `Returned|BRW-20260615-0305` (1 baris)
35. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan input Search, penutupan dropdown page size, dan pengosongan Search di akhir tiap TC; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pre-setup #30 menyatakan sub-tab Borrow berisi 6 baris, sedangkan TC mencantumkan lima baris pada daftar urutan; spec mengasersi lima baris teratas sesuai daftar TC dan keenam baris untuk jumlah total (S-14).
- Parenthetical TC-FA-SU-805 butir b (header `⋯` membuka overlay Column Visibility) juga diasersi di spec 271 (TC-FA-SU-824); spec ini mengasersi overlay terbuka (langkah 17). Pembukaan header `⋯` dan penutupan overlay dengan Esc (langkah 16 dan 18) adalah langkah penghubung.
- Baris default sort pada langkah 19 menjadi pembanding bahwa tabel berisi baris sebelum Search diterapkan (bagian 8b butir 2).
- Temuan untuk QA (S-15): daftar urutan descending pada TC-FA-SU-805 butir c dan TC-FA-SU-812 butir a bukan kebalikan daftar ascending (descending dimulai `Returned|BRW-20260320-0188`, ascending berakhir `Borrowed|BRW-20260712-0347`) bila hanya lima baris teratas yang dicantumkan; enam baris Pre-setup #30 membuat daftar TC kemungkinan terpotong dari baris keenam. Spec mengikuti daftar TC. Tooltip hover pada TC-FA-SU-805 butir a tidak diberi daftar; spec memakai `Search`, `Filter`, `Download` mengikuti TC-FA-SU-835.
