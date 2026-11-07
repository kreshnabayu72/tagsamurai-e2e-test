---
id: TC-FA-SU-E2E-195-tab-changelog-search-dan-sort
title: "Tab Changelog: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-579
  - TC-FA-SU-580
  - TC-FA-SU-581
  - TC-FA-SU-582
coverage:
  web: automated
---

# Tab Changelog: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Date, Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Date `18/08/26, 13:10`, Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Date `12/08/26, 11:41`, Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Date `12/08/26, 11:40`, Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Date `02/08/26, 10:05`, Field `Home Group`, Modified By `Lina M`
  - T-5: Date `20/07/26, 14:30`, Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Date `15/07/26, 09:15`, Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Date `10/06/26, 08:02`, Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-579: Siklus interaksi Search

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu klik tab Changelog
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, field, or value...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Home` (`H`)
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Home` (`ome`) lalu tekan Enter
12. Verifikasi tabel tersaring menjadi `Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik `Home`, tekan Enter, lalu klik icon ←
21. Verifikasi search bar menutup
22. Verifikasi keyword dikosongkan
23. Verifikasi tabel langsung kembali ke semua baris
24. Klik icon Search
25. Ketik `  Home  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Home` tanpa spasi (`Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil))
27. Verifikasi isi input tidak berubah

### TC-FA-SU-580: Guard kolom non-searchable Date

28. Kosongkan isi kotak search, tekan Enter
29. Verifikasi sel Date baris T-1 menampilkan `18/08/26, 13:10`
30. Ketik Search `18/08/26, 13:10` (nilai kolom Date), tekan Enter
31. Verifikasi nilai Date tidak mencocokkan baris melalui Search; empty state `No results found` tampil
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-581: Search terikat visibilitas kolom Action

33. Ketik Search `Home`, tekan Enter
34. Verifikasi sebelum hide: keyword `Home` menyisakan `Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
35. Klik header Column Visibility (⋯), hilangkan centang Action
36. Ganti isi kotak search dengan `Home`, tekan Enter
37. Verifikasi setelah kolom Action di-hide: keyword yang sama menyisakan `Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
38. Klik header Column Visibility (⋯), centang kembali Action
39. Ganti isi kotak search dengan `Home`, tekan Enter
40. Verifikasi setelah kolom Action di-unhide: hasil kembali `Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
41. Klik `(←)` pada kotak Search

### TC-FA-SU-582: Sort kelas date (Date)

42. Klik header Date satu kali
43. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-7, T-6, T-5, T-4, T-3
44. Klik header Date kedua kali
45. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5
46. Klik header Date ketiga kali
47. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tambahan (S-03, R-16, bagian 8b butir 13): langkah 1 mengetik Search `Budi Santoso` lalu Enter supaya baris Budi Santoso tampil di User List (25 baris) sebelum nama diklik.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 28 (Kosongkan Search supaya baris seed T-1 tampil sebelum asersi sel Date). Langkah 29 adalah Verifikasi tambahan di luar Expected (S-03): sel Date baris T-1 menampilkan nilai yang diketik pada langkah 30, sebagai anchor positif sebelum asersi absence (bagian 8b butir 2); nilai Date seed mengikuti Example Data PRD dan dicatat di alias baris Prerequisites.
- Spec ini berjumlah 47 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) Expected b TC-FA-SU-581 menyatakan hasil setelah kolom Action di-hide sama dengan sebelum di-hide, karena kolom lain yang tampil tetap dicari; spec mengikuti Expected.
