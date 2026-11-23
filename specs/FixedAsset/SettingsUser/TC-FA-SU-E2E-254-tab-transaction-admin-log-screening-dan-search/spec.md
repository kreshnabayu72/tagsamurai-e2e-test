---
id: TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search
title: "Tab Transaction Admin Log: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-765
  - TC-FA-SU-766
  - TC-FA-SU-767
  - TC-FA-SU-768
coverage:
  web: automated
---

# Tab Transaction Admin Log: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC: `18/07/26` `Returned · Self-processed` `BRW-2026-0315` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `16/07/26` `Rejected` `BRW-2026-0314` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `15/07/26` `Handed over` `BRW-2026-0313` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `13/07/26` `Requested` `BRW-2026-0312` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; `12/07/26` `Draft created` `—` `Tablet Samsung Tab - 4` `—` `IT Infrastructure`. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: hover ikon dan header kolom, tombol `Esc`.
- State: yang berubah hanya Search, Sort, dan tampilan sisi klien; tidak ada state global dan tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-765: Screening Table Tools, kolom, dan default sort Sub-tab Borrow

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Hover icon Filter
6. Verifikasi tooltip `Filter` tampil
7. Hover icon Download
8. Verifikasi tooltip `Download` tampil
9. Klik icon Search
10. Verifikasi placeholder Search `Search activity, transaction ID, asset, or borrower...` tampil
11. Verifikasi kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`, dan header kolom `⋯` (Column Visibility)
12. Verifikasi kolom `Date`, `Transaction ID`, `Name`, `Borrower`, dan `Group` sortable (memiliki icon sort)
13. Verifikasi kolom `Activity` unsortable (tanpa icon sort)
14. Verifikasi kolom `Role`, `Action Taken`, dan `Transaction Status` tidak ada
15. Verifikasi kolom `⋯` pada setiap baris kosong tanpa row action
16. Klik header kolom `⋯`
17. Verifikasi overlay Column Visibility terbuka
18. Tutup overlay Column Visibility dengan Esc
19. Verifikasi default sort Date terbaru lebih dulu: `BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, baris Draft `Tablet Samsung Tab - 4`
20. Verifikasi baris `BRW-2026-0315` bernilai `18/07/26`, `Returned · Self-processed`, `Laptop Dell Latitude - 3`, `Rina Wijaya`, `General Affairs`
21. Verifikasi baris `BRW-2026-0314` bernilai `16/07/26`, `Rejected`, `Projector Epson - 1`, `Andi Pratama`, `Branch Surabaya`
22. Verifikasi baris `BRW-2026-0313` bernilai `15/07/26`, `Handed over`, `Camera Sony A7 - 2`, `Budi Santoso`, `Logistics Warehouse`
23. Verifikasi baris `BRW-2026-0312` bernilai `13/07/26`, `Requested`, `Laptop Dell Latitude - 5`, `Dewi Lestari`, `Finance & Accounting`
24. Verifikasi baris Draft bernilai `12/07/26`, `Draft created`, Transaction ID `—`, `Tablet Samsung Tab - 4`, Borrower `—`, `IT Infrastructure`
25. Verifikasi Activity tampil sebagai teks biasa tanpa badge berwarna
26. Verifikasi Transaction ID tampil sebagai teks biasa (bukan tautan)
27. Verifikasi Group tampil sebagai badge
28. Verifikasi nilai kosong tampil `—`
29. Verifikasi footer pagination menampilkan 10 data per halaman
30. Klik dropdown page size
31. Verifikasi pilihan page size 10, 25, 50, 100
32. Tutup dropdown page size dengan Esc

### TC-FA-SU-766: Search kelas teks, kolom Transaction ID, Name, dan Borrower

33. Ketik Search `0313`, tekan Enter
34. Verifikasi tabel menyisakan `BRW-2026-0313` (1 baris)
35. Ganti isi kotak search dengan `Projector`, tekan Enter
36. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris, `Projector Epson - 1`)
37. Ganti isi kotak search dengan `Dewi`, tekan Enter
38. Verifikasi tabel menyisakan `BRW-2026-0312` (1 baris, `Dewi Lestari`)

### TC-FA-SU-767: Search kelas badge, kolom Group

39. Ganti isi kotak search dengan `Surabaya`, tekan Enter
40. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris)

### TC-FA-SU-768: Search kelas teks, kolom Activity (nama node, penanda Self-processed, aksi Draft)

41. Ganti isi kotak search dengan `Rejected`, tekan Enter
42. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris)
43. Ganti isi kotak search dengan `Self-processed`, tekan Enter
44. Verifikasi tabel menyisakan `BRW-2026-0315` (1 baris, Activity `Returned · Self-processed`)
45. Ganti isi kotak search dengan `Draft`, tekan Enter
46. Verifikasi tabel menyisakan baris `Draft created` (`Tablet Samsung Tab - 4`, 1 baris)
47. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; Search nama pengguna adalah langkah penghubung, R-16), penutupan overlay Column Visibility (langkah 18), penutupan dropdown page size (langkah 32), dan pengosongan Search di akhir spec (langkah 47, S-09). Antar anggota kata kunci dalam satu TC dan antar TC, kotak Search yang sudah berisi diganti isinya (8b.9) alih-alih dikosongkan lebih dulu; hasilnya sama dengan "kosongkan lalu Enter" yang ditulis TC, karena Enter menyaring ulang dari seluruh baris.
- Tabel berisi lima baris sudah terbukti pada langkah 19 sampai 24 sebelum Search pertama (langkah 33), sehingga hasil "menyisakan 1 baris" tidak lulus semu (8b.2). Absence kolom `Role`, `Action Taken`, `Transaction Status` (langkah 14) didahului `Verifikasi` kolom lain tampil (langkah 11).
- Detail overlay Column Visibility (isi daftar kolom dan `Setup Column...`) diasersi di spec 259 (TC-FA-SU-783); spec ini hanya mengasersi bahwa overlay terbuka (langkah 17).
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-765 sampai 768 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) TC-FA-SU-765 butir a menyebut "tooltip hover masing-masing sesuai nama ikon" tanpa daftar; spec memakai `Search`, `Filter`, `Download` mengikuti TC-FA-SU-794. (3) TC-FA-SU-765 langkah 3 membuka dropdown page size, tetapi butir e hanya menyebut footer; spec mengasersi 10 data per halaman dan empat pilihan page size. (4) Post Condition tidak ada pada keempat TC.
- Spec ini berjumlah 47 langkah dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface dengan data seed yang sama, berdiri sendiri; ukuran berasal dari klausa Expected TC-FA-SU-765 (lima butir, masing-masing beberapa klausa, satu `Verifikasi` per klausa menurut S-01) dan tiga anggota kata kunci TC-FA-SU-766 serta tiga TC-FA-SU-768, bukan dari langkah tambahan.
