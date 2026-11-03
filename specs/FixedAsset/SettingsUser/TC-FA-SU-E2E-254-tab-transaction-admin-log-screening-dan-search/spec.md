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
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps


### TC-FA-SU-765: Screening Table Tools, kolom, dan default sort Sub-tab Borrowing & Assignment

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment
2. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi placeholder Search `Search transaction ID, group, or role...` tampil
7. Klik `←` pada kotak Search
8. Hover icon Filter
9. Verifikasi tooltip `Filter` tampil
10. Hover icon Download
11. Verifikasi tooltip `Download` tampil
12. Verifikasi kolom berurutan `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status`, dan header kolom `⋯` (Column Visibility)
13. Verifikasi kolom `Transaction ID`, `Group`, dan `Date` sortable (memiliki icon sort)
14. Verifikasi kolom `Role`, `Action Taken`, dan `Transaction Status` unsortable (tanpa icon sort)
15. Verifikasi kolom `⋯` pada setiap baris kosong tanpa row action
16. Klik header kolom `⋯`
17. Verifikasi overlay Column Visibility terbuka
18. Tutup overlay Column Visibility dengan Esc
19. Verifikasi default sort Date descending: `BRW-20260718-0315`, `BRW-20260716-0314`, `BRW-20260715-0313`, `BRW-20260713-0312`, `BRW-20260712-0311`
20. Verifikasi footer pagination menampilkan 10 data per halaman
21. Klik dropdown page size
22. Verifikasi pilihan page size 10, 25, 50, 100
23. Tutup dropdown page size dengan Esc

### TC-FA-SU-766: Search kelas teks, kolom Transaction ID

24. Ketik Search `0313`, tekan Enter
25. Verifikasi tabel menyisakan `BRW-20260715-0313` (1 baris)
26. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-767: Search kelas badge, kolom Group

27. Ketik Search `Surabaya`, tekan Enter
28. Verifikasi tabel menyisakan `BRW-20260716-0314` (1 baris)
29. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-768: Search kelas enum, kolom Role, Action Taken, dan Transaction Status

30. Ketik Search `Approver`, tekan Enter
31. Verifikasi tabel menyisakan `BRW-20260716-0314`, `BRW-20260712-0311` (2 baris)
32. Kosongkan isi kotak search, tekan Enter
33. Ketik Search `Processed`, tekan Enter
34. Verifikasi tabel menyisakan `BRW-20260718-0315`, `BRW-20260713-0312` (2 baris)
35. Kosongkan isi kotak search, tekan Enter
36. Ketik Search `Completed`, tekan Enter
37. Verifikasi tabel menyisakan `BRW-20260715-0313`, `BRW-20260712-0311` (2 baris)
38. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan input Search, penutupan dropdown page size, dan pengosongan Search di akhir tiap TC (S-09).
- Baris sumber pada Expected dibaca sebagai hasil Search/sort yang menyisakan baris bernama; urutan default sort pada langkah 19 menjadi pembanding bahwa tabel berisi lima baris sebelum Search diterapkan (bagian 8b butir 2).
- Parenthetical TC-FA-SU-765 butir b (header `⋯` membuka overlay Column Visibility) juga diasersi di spec 259 (TC-FA-SU-783); spec ini mengasersi overlay terbuka (langkah 17) dan kolom `⋯` pada baris kosong tanpa row action. Pembukaan header `⋯` dan penutupan overlay dengan Esc (langkah 16 dan 18) adalah langkah penghubung.
- Temuan untuk QA (S-15): (1) TC-FA-SU-765 butir a menyebut "tooltip hover masing-masing sesuai nama ikon" tanpa daftar; spec memakai `Search`, `Filter`, `Download` mengikuti TC-FA-SU-794. (2) Pilihan page size diasersi lewat membuka dropdown page size; TC tidak menyebut cara membukanya. (3) Post Condition tidak ada.
- Spec ini berjumlah 38 langkah dan sedikit di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
