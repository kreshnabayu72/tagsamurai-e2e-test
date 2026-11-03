---
id: TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-tooltip-icon-dan-state-per-sub-tab
title: "Tab Transaction Admin Log: Pagination, Tooltip Icon, dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-789
  - TC-FA-SU-794
  - TC-FA-SU-796
coverage:
  web: automated
---

# Tab Transaction Admin Log: Pagination, Tooltip Icon, dan State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pre-setup untuk state sub-tab lain: sub-tab Transfer milik Budi Santoso dipakai hanya sebagai tempat menerapkan kontrol berbeda; isinya tidak diasersi (NC-23). Keyword `TRF` dipilih spec.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment

### TC-FA-SU-789: Pagination (page size, navigasi, dan kasus tepi)

2. Verifikasi footer pagination menampilkan 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi `All`
5. Tutup dropdown page size dengan Esc
6. Isi nomor halaman `0`, tekan Enter
7. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
8. Isi nomor halaman `-1`, tekan Enter
9. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
10. Isi nomor halaman `999`, tekan Enter
11. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
12. Isi nomor halaman `abc`, tekan Enter
13. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
14. Ganti page size ke 25
15. Verifikasi tabel menampilkan halaman 1
16. Ganti page size kembali ke 10
17. Verifikasi tabel menampilkan halaman 1
18. Klik header `Transaction ID` satu kali
19. Verifikasi tabel menampilkan halaman 1
20. Klik header `Transaction ID` dua kali lagi hingga sort kembali netral
21. Ketik Search `0313`, tekan Enter
22. Verifikasi tabel menampilkan halaman 1
23. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-794: Tooltip icon Table Tools dan header Actions

24. Hover icon Search
25. Verifikasi tooltip `Search` tampil
26. Hover icon Filter
27. Verifikasi tooltip `Filter` tampil
28. Hover icon Download
29. Verifikasi tooltip `Download` tampil
30. Hover header kolom Actions (`⋯`)
31. Verifikasi tooltip `Column Visibility` tampil

### TC-FA-SU-796: State sub-tab dipertahankan per sub-tab

32. Ketik Search `Approver`, tekan Enter
33. Klik icon Filter, buka dropdown `Group`, centang `Branch Surabaya`, lalu klik `[Apply]`
34. Klik header `Transaction ID` satu kali
35. Ganti page size ke 25
36. Klik Sub-tab Transfer
37. Ketik Search `TRF`, klik header `Date` satu kali, lalu ganti page size ke 50
38. Klik Sub-tab Borrowing & Assignment
39. Verifikasi Search `Approver` tersimpan pada sub-tab Borrowing & Assignment
40. Verifikasi Filter `Group` = `Branch Surabaya` tersimpan pada sub-tab Borrowing & Assignment
41. Verifikasi Sort pada kolom `Transaction ID` tersimpan pada sub-tab Borrowing & Assignment
42. Verifikasi page size 25 tersimpan pada sub-tab Borrowing & Assignment
43. Klik Sub-tab Transfer
44. Verifikasi state sub-tab Transfer (Search, Sort, dan page size 50) tidak dipengaruhi state sub-tab Borrowing & Assignment
45. Klik Sub-tab Borrowing & Assignment
46. Klik Back breadcrumb ke User List, lalu buka Detail User Budi Santoso, klik Tab Transaction Admin Log, dan klik Sub-tab Borrowing & Assignment
47. Verifikasi state sub-tab Borrowing & Assignment dipulihkan setelah Back breadcrumb (Search, Filter, Sort, dan page size 25)
48. Tekan F5 pada halaman Detail
49. Verifikasi state sub-tab Borrowing & Assignment dipulihkan setelah refresh F5 (Search, Filter, Sort, dan page size 25)
50. Klik menu Settings > User pada sidebar, lalu buka Detail User Budi Santoso, klik Tab Transaction Admin Log, dan klik Sub-tab Borrowing & Assignment
51. Verifikasi state sub-tab Borrowing & Assignment kembali ke default (Search kosong, tanpa Filter, sort default Date descending, page size 10)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan Search, pemulihan sort ke netral, dan perpindahan sub-tab; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Fixture sub-tab Borrowing & Assignment satu halaman; perpindahan antar halaman tidak dapat dicapai pada surface ini (butir e TC-FA-SU-789 menyatakan perilaku multi-halaman diuji pada TC-FA-SU-359 dan TC-FA-SU-1057) sehingga tidak diasersi di sini.
- Temuan untuk QA (S-15): (1) TC-FA-SU-796 Langkah Uji nomor 2 tidak menyebut sub-tab lain; spec memakai Sub-tab Transfer dan keyword `TRF`. (2) TC-FA-SU-796 Langkah Uji nomor 5 tidak menyebut sub-tab aktif sesudah F5; spec mengasersi state sub-tab Borrowing & Assignment sesuai Expected c. (3) Butir "nomor halaman aktif tidak diuji" pada TC-FA-SU-796 butir a diikuti: nomor halaman tidak diasersi.
- Spec ini berjumlah 51 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
