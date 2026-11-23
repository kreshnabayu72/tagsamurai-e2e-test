---
id: TC-FA-SU-E2E-473-tab-transaction-admin-log-missing-filter-dan-download
title: "Tab Transaction Admin Log Sub-tab Missing: Filter dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1184
  - TC-FA-SU-1185
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Missing: Filter dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Missing berisi 4 baris (Name `Printer HP LaserJet - 3` Source `Audit` Group `Logistics Warehouse`, Name `Monitor LG 24 - 5` Source `Manual` Group `IT Infrastructure`, Name `Laptop Dell Latitude - 10` Source `Borrowed asset` Group `Branch Surabaya`, Name `Camera Sony A7 - 5` Source `Reported by scan` Group `General Affairs`) dengan nilai Date, Activity, Source, dan Group per baris (Source = Source record, sama untuk setiap baris record itu; Group = grup aset saat tindakan dieksekusi) sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.

## Test Steps

### TC-FA-SU-1184: Filter Activity, Name, Group, Source, dan Date

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Missing
2. Klik icon Filter
3. Buka dropdown `Activity`
4. Verifikasi opsi dropdown = DISTINCT nilai kolom Activity pada tabel: `Marked as found`, `Report confirmed`, `Reported missing`, `Update added`
5. Centang `Reported missing`
6. Klik `[Apply]`
7. Verifikasi tabel menyisakan `Monitor LG 24 - 5` (1 baris)
8. Verifikasi chip `Reported missing` tampil di dalam field `Activity`
9. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
10. Buka dropdown `Name`
11. Verifikasi opsi dropdown = DISTINCT nilai kolom Name pada tabel: `Camera Sony A7 - 5`, `Laptop Dell Latitude - 10`, `Monitor LG 24 - 5`, `Printer HP LaserJet - 3`
12. Centang `Printer HP LaserJet - 3`
13. Klik `[Apply]`
14. Verifikasi tabel menyisakan `Printer HP LaserJet - 3` (1 baris)
15. Verifikasi chip `Printer HP LaserJet - 3` tampil di dalam field `Name`
16. Klik `[Clear Field]` pada field `Name`, lalu klik `[Apply]`
17. Buka dropdown `Group`
18. Verifikasi opsi dropdown = DISTINCT nilai kolom Group pada tabel: `Branch Surabaya`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`
19. Centang `Branch Surabaya`
20. Klik `[Apply]`
21. Verifikasi tabel menyisakan `Laptop Dell Latitude - 10` (1 baris)
22. Verifikasi chip `Branch Surabaya` tampil di dalam field `Group`
23. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
24. Buka dropdown `Source`
25. Verifikasi opsi dropdown = DISTINCT nilai kolom Source pada tabel: `Audit`, `Borrowed asset`, `Manual`, `Reported by scan`
26. Centang `Manual`
27. Klik `[Apply]`
28. Verifikasi tabel menyisakan `Monitor LG 24 - 5` (1 baris)
29. Verifikasi chip `Manual` tampil di dalam field `Source`
30. Klik `[Clear Field]` pada field `Source`, lalu klik `[Apply]`
31. Pilih rentang 13/07/26 sampai 17/07/26 pada field `Date`
32. Klik `[Apply]`
33. Verifikasi rentang inklusif 13/07/26 sampai 17/07/26 menyisakan `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5` (2 baris)
34. Verifikasi panel Filter tetap terbuka setelah `[Apply]` (tidak menutup otomatis)
35. Klik `[Clear Field]` pada field `Date`, lalu klik `[Apply]`
36. Klik icon Filter untuk menutup panel
37. Verifikasi panel Filter tertutup

### TC-FA-SU-1185: Download format CSV dan XLSX, nama file, kolom, dan tanpa toast sukses

38. Hover icon Download
39. Verifikasi tooltip `Download` tampil
40. Klik icon Download
41. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
42. Pilih `Download as CSV`
43. Verifikasi tidak ada toast sukses
44. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Missing.csv` terunduh
45. Klik icon Download, lalu pilih `Download as XLSX`
46. Verifikasi tidak ada toast sukses
47. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Missing.xlsx` terunduh
48. Buka berkas CSV dan XLSX yang terunduh
49. Verifikasi berkas memuat seluruh baris sub-tab (empat baris) dalam urutan sort aktif (default Date newest first)
50. Verifikasi berkas memuat kolom `Date`, `Activity`, `Name`, `Source`, dan `Group` tanpa Transaction ID
51. Verifikasi Date mengikuti General Settings
52. Verifikasi Activity, Name, dan Source ditulis apa adanya sebagai teks
53. Verifikasi Group (badge) ditulis sebagai label teks tanpa warna
54. Verifikasi CSV berencoding UTF-8 dengan BOM
55. Verifikasi XLSX berisi satu sheet bernama `Sheet1`


## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), `[Clear Field]` dan penutupan panel Filter; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- `P-10`: klausa isi berkas TC-FA-SU-1185 butir d (BOM UTF-8 dan sheet `Sheet1`) dan butir c (kolom dan nilai berkas) menyangkut isi berkas (kelas f, binary buffer) dan diasersi di spec ini setelah seluruh klausa UI TC itu, satu `Verifikasi` per klausa; alur unduh tidak dapat dipisah dari asersi UI nama berkas dan ketiadaan toast.
- Pembagian TC lintas spec: struktur sub-tab Missing ada di spec 471; Search, guard, dan Sort ada di spec 472.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1184 Langkah Uji nomor 4, 6, dan 8 menyebut `[Clear Field]` lalu `[Apply]` sesudah tiap filter; spec mengikutinya dan menutup panel pada akhir blok (butir d). (2) Pada TC-FA-SU-1185 butir c "seluruh baris sub-tab" diasersi sebagai empat baris seed (satu halaman).
- Spec ini berjumlah 55 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
