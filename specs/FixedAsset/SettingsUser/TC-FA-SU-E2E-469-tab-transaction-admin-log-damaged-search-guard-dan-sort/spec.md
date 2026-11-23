---
id: TC-FA-SU-E2E-469-tab-transaction-admin-log-damaged-search-guard-dan-sort
title: "Tab Transaction Admin Log Sub-tab Damaged: Search, Guard Kolom, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1175
  - TC-FA-SU-1176
  - TC-FA-SU-1177
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Damaged: Search, Guard Kolom, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged berisi 4 baris (Name `Laptop Dell Latitude - 9` Group `IT Infrastructure`, Name `Projector Epson - 2` Group `General Affairs`, Name `Tablet Samsung Tab - 5` Group `Logistics Warehouse`, Name `Camera Sony A7 - 4` Group `Finance & Accounting`) dengan nilai Date, Activity, dan Group per baris (Group = grup aset saat tindakan dieksekusi) sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

### TC-FA-SU-1175: Search kelas teks dan badge, kolom Activity, Name, dan Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Damaged
2. Klik icon Search
3. Ketik Search `confirmed`, tekan Enter
4. Verifikasi tabel menyisakan `Projector Epson - 2` (1 baris)
5. Kosongkan isi kotak search, tekan Enter
6. Ketik Search `repaired`, tekan Enter
7. Verifikasi tabel menyisakan `Laptop Dell Latitude - 9` (1 baris, Activity `Marked as repaired`)
8. Kosongkan isi kotak search, tekan Enter
9. Ketik Search `Camera`, tekan Enter
10. Verifikasi tabel menyisakan `Camera Sony A7 - 4` (1 baris)
11. Kosongkan isi kotak search, tekan Enter
12. Ketik Search `Logistics`, tekan Enter
13. Verifikasi tabel menyisakan `Tablet Samsung Tab - 5` (1 baris)
14. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1176: Guard kolom Date tidak searchable dan kolom Activity tidak sortable

15. Ketik Search `22/07/26`, tekan Enter
16. Verifikasi empty state `No results found` tampil (kolom Date tidak dicari; penyaringan kolom ini hanya lewat Filter Panel)
17. Kosongkan isi kotak search, tekan Enter
18. Hover dan klik header `Activity`
19. Verifikasi header `Activity` tidak memiliki icon sort
20. Verifikasi klik header `Activity` tidak mengubah urutan baris

### TC-FA-SU-1177: Sort kolom Name, Date, dan Group

21. Klik header `Name` satu kali
22. Verifikasi ascending (↑): `Camera Sony A7 - 4`, `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`
23. Klik header `Name` kedua kali
24. Verifikasi descending (↓): `Tablet Samsung Tab - 5`, `Projector Epson - 2`, `Laptop Dell Latitude - 9`, `Camera Sony A7 - 4`
25. Klik header `Name` ketiga kali
26. Verifikasi netral kembali ke default: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`
27. Klik header `Date` satu kali
28. Verifikasi ascending (↑): `Camera Sony A7 - 4`, `Tablet Samsung Tab - 5`, `Projector Epson - 2`, `Laptop Dell Latitude - 9`
29. Klik header `Date` kedua kali
30. Verifikasi descending (↓): `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`
31. Klik header `Date` ketiga kali
32. Verifikasi netral kembali ke default: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`
33. Klik header `Group` satu kali
34. Verifikasi ascending (↑): `Camera Sony A7 - 4`, `Projector Epson - 2`, `Laptop Dell Latitude - 9`, `Tablet Samsung Tab - 5`
35. Klik header `Group` kedua kali
36. Verifikasi descending (↓): `Tablet Samsung Tab - 5`, `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Camera Sony A7 - 4`
37. Klik header `Group` ketiga kali
38. Verifikasi netral kembali ke default: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`


## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan Search dan pengosongan Search; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09). Klik ketiga tiap header sort mengembalikan sort ke default sehingga tidak perlu reset lain.
- Order yang diasersi pada TC-FA-SU-1177 mengikuti Expected TC (empat baris seed, nilai distinct per kolom; S-11).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1176 langkah 4 "Hover dan klik header kolom Activity" tidak menyebut apa yang diamati saat hover; spec mengasersi hanya ketiadaan icon sort dan urutan tidak berubah. (2) Sub-tab Damaged tidak memiliki kolom Transaction ID, sehingga baris dirujuk lewat Name.
- Spec ini berjumlah 38 langkah dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
