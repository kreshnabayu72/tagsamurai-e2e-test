---
id: TC-FA-SU-E2E-472-tab-transaction-admin-log-missing-search-guard-dan-sort
title: "Tab Transaction Admin Log Sub-tab Missing: Search, Guard Kolom, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1181
  - TC-FA-SU-1182
  - TC-FA-SU-1183
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Missing: Search, Guard Kolom, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Missing berisi 4 baris (Name `Printer HP LaserJet - 3` Group `Logistics Warehouse`, Name `Monitor LG 24 - 5` Group `IT Infrastructure`, Name `Laptop Dell Latitude - 10` Group `Branch Surabaya`, Name `Camera Sony A7 - 5` Group `General Affairs`) dengan nilai Date, Activity, dan Group per baris (Group = grup aset saat tindakan dieksekusi) sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

### TC-FA-SU-1181: Search kelas teks dan badge, kolom Activity, Name, dan Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Missing
2. Klik icon Search
3. Ketik Search `Reported missing`, tekan Enter
4. Verifikasi tabel menyisakan `Monitor LG 24 - 5` (1 baris)
5. Kosongkan isi kotak search, tekan Enter
6. Ketik Search `found`, tekan Enter
7. Verifikasi tabel menyisakan `Printer HP LaserJet - 3` (1 baris, Activity `Marked as found`)
8. Kosongkan isi kotak search, tekan Enter
9. Ketik Search `Laptop`, tekan Enter
10. Verifikasi tabel menyisakan `Laptop Dell Latitude - 10` (1 baris)
11. Kosongkan isi kotak search, tekan Enter
12. Ketik Search `Surabaya`, tekan Enter
13. Verifikasi tabel menyisakan `Laptop Dell Latitude - 10` (1 baris)
14. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1182: Guard kolom Date tidak searchable dan kolom Activity tidak sortable

15. Ketik Search `21/07/26`, tekan Enter
16. Verifikasi empty state `No results found` tampil (kolom Date tidak dicari; penyaringan kolom ini hanya lewat Filter Panel)
17. Kosongkan isi kotak search, tekan Enter
18. Hover dan klik header `Activity`
19. Verifikasi header `Activity` tidak memiliki icon sort
20. Verifikasi klik header `Activity` tidak mengubah urutan baris

### TC-FA-SU-1183: Sort kolom Name, Date, dan Group

21. Klik header `Name` satu kali
22. Verifikasi ascending (↑): `Camera Sony A7 - 5`, `Laptop Dell Latitude - 10`, `Monitor LG 24 - 5`, `Printer HP LaserJet - 3`
23. Klik header `Name` kedua kali
24. Verifikasi descending (↓): `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
25. Klik header `Name` ketiga kali
26. Verifikasi netral kembali ke default: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
27. Klik header `Date` satu kali
28. Verifikasi ascending (↑): `Camera Sony A7 - 5`, `Laptop Dell Latitude - 10`, `Monitor LG 24 - 5`, `Printer HP LaserJet - 3`
29. Klik header `Date` kedua kali
30. Verifikasi descending (↓): `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
31. Klik header `Date` ketiga kali
32. Verifikasi netral kembali ke default: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
33. Klik header `Group` satu kali
34. Verifikasi ascending (↑): `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`, `Monitor LG 24 - 5`, `Printer HP LaserJet - 3`
35. Klik header `Group` kedua kali
36. Verifikasi descending (↓): `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Camera Sony A7 - 5`, `Laptop Dell Latitude - 10`
37. Klik header `Group` ketiga kali
38. Verifikasi netral kembali ke default: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`


## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan Search dan pengosongan Search; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09). Klik ketiga tiap header sort mengembalikan sort ke default sehingga tidak perlu reset lain.
- Order yang diasersi pada TC-FA-SU-1183 mengikuti Expected TC (empat baris seed, nilai distinct per kolom; S-11).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1182 langkah 4 "Hover dan klik header kolom Activity" tidak menyebut apa yang diamati saat hover; spec mengasersi hanya ketiadaan icon sort dan urutan tidak berubah. (2) Sub-tab Missing tidak memiliki kolom Transaction ID, sehingga baris dirujuk lewat Name.
- Spec ini berjumlah 38 langkah dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
