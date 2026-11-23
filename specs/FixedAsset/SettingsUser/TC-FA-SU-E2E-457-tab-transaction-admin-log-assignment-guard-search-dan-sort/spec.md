---
id: TC-FA-SU-E2E-457-tab-transaction-admin-log-assignment-guard-search-dan-sort
title: "Tab Transaction Admin Log Sub-tab Assignment: Guard Search, Search Terikat Visibilitas Kolom, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1146
  - TC-FA-SU-1147
  - TC-FA-SU-1148
  - TC-FA-SU-1149
  - TC-FA-SU-1150
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Guard Search, Search Terikat Visibilitas Kolom, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Spec tidak menyimpan konfigurasi kolom; hide dan unhide kolom `Assignee` lewat Column Visibility dikembalikan oleh langkah di spec ini.

## Test Steps

### TC-FA-SU-1146: Guard kolom non-searchable Date

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik icon Search
3. Ketik Search `20/07/26`, tekan Enter
4. Verifikasi empty state `No results found` tampil (kolom Date tidak dicari; penyaringan kolom ini hanya lewat Filter Panel)
5. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1147: Search terikat visibilitas kolom Assignee

6. Ketik Search `Andi`, tekan Enter
7. Verifikasi tabel menyisakan `ASG-20260717-0069` (Assignee `Andi P`)
8. Klik header `⋯`, lalu hilangkan centang `Assignee`
9. Tutup overlay Column Visibility dengan Esc
10. Verifikasi header kolom `Group` tampil
11. Ganti isi kotak search dengan `Andi`, tekan Enter
12. Verifikasi tabel tidak menyisakan baris (kolom tersembunyi tidak dicari)
13. Ganti isi kotak search dengan `Surabaya`, tekan Enter
14. Verifikasi kolom lain yang tampil tetap dicari: tabel menyisakan `ASG-20260720-0071`
15. Klik header `⋯`, lalu beri centang `Assignee`
16. Tutup overlay Column Visibility dengan Esc
17. Ganti isi kotak search dengan `Andi`, tekan Enter
18. Verifikasi tabel kembali menyisakan `ASG-20260717-0069`
19. Klik `←` pada kotak Search

### TC-FA-SU-1148: Sort kelas teks, kolom Transaction ID, Name, dan Group

20. Klik header `Transaction ID` satu kali
21. Verifikasi ascending (↑): `ASG-20260715-0068`, `ASG-20260717-0069`, `ASG-20260719-0070`, `ASG-20260720-0071`
22. Klik header `Transaction ID` kedua kali
23. Verifikasi descending (↓): `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`
24. Klik header `Transaction ID` ketiga kali
25. Verifikasi netral kembali ke default: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`
26. Klik header `Name` satu kali
27. Verifikasi ascending (↑): `ASG-20260717-0069` (`Camera Sony A7 - 3`), `ASG-20260720-0071` (`Laptop Dell Latitude - 8`), `ASG-20260719-0070` (`Monitor LG 24 - 4`), `ASG-20260715-0068` (`Printer HP LaserJet - 2`)
28. Klik header `Name` kedua kali
29. Verifikasi descending (↓): `ASG-20260715-0068`, `ASG-20260719-0070`, `ASG-20260720-0071`, `ASG-20260717-0069`
30. Klik header `Name` ketiga kali
31. Verifikasi netral kembali ke default: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`
32. Klik header `Group` satu kali
33. Verifikasi ascending (↑): `ASG-20260720-0071` (`Branch Surabaya`), `ASG-20260715-0068` (`Finance & Accounting`), `ASG-20260719-0070` (`IT Infrastructure`), `ASG-20260717-0069` (`Logistics Warehouse`)
34. Klik header `Group` kedua kali
35. Verifikasi descending (↓): `ASG-20260717-0069`, `ASG-20260719-0070`, `ASG-20260715-0068`, `ASG-20260720-0071`
36. Klik header `Group` ketiga kali
37. Verifikasi netral kembali ke default: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`

### TC-FA-SU-1149: Sort kelas date, kolom Date

38. Klik header `Date` satu kali
39. Verifikasi ascending (↑): `ASG-20260715-0068`, `ASG-20260717-0069`, `ASG-20260719-0070`, `ASG-20260720-0071`
40. Klik header `Date` kedua kali
41. Verifikasi descending (↓): `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`
42. Klik header `Date` ketiga kali
43. Verifikasi netral kembali ke default: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`

### TC-FA-SU-1150: Guard kolom non-sortable Activity

44. Hover dan klik header `Activity`
45. Verifikasi header `Activity` tidak memiliki icon sort
46. Verifikasi klik header `Activity` tidak mengubah urutan baris

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan dan penutupan Search, hide dan unhide kolom, penutupan overlay, serta pengosongan Search; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09). Klik ketiga tiap header sort mengembalikan sort ke default sehingga tidak perlu reset lain.
- Order yang diasersi pada TC-FA-SU-1148 dan TC-FA-SU-1149 mengikuti Expected TC (empat baris seed, nilai distinct per kolom; S-11).
- Pembagian TC lintas spec: Search kolom Activity, Group, dan siklus interaksi Search ada di spec 456.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1147 butir b menyebut "kolom lain yang tampil tetap dicari" tanpa keyword; spec memakai Search `Surabaya` (kolom Group). (2) TC-FA-SU-1150 langkah 2 "Hover dan klik tiap header" tidak menyebut apa yang diamati saat hover; spec mengasersi hanya ketiadaan icon sort dan urutan tidak berubah.
- Spec ini berjumlah 46 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
