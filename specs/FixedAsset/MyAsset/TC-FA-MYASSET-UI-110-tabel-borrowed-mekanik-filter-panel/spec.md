---
id: TC-FA-MYASSET-UI-110-tabel-borrowed-mekanik-filter-panel
title: "Tabel Borrowed: mekanik Filter Panel dan filter pada kolom yang disembunyikan"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.9#p1", "EB-FLT-2@tabel-borrowed", "EB-FLT-6@tabel-borrowed"]
smoke: []
dependsOn: []
trace:
  "§9.9#p1": 38
  "EB-FLT-2@tabel-borrowed": [6, 7, 9, 10, 11, 14, 16, 17, 23, 26, 27, 35, 37, 39, 44, 47, 49, 51, 55]
  "EB-FLT-6@tabel-borrowed": [66, 67, 68, 69, 74]
anchor: [25, 33, 46, 61, 64, 65]
coverage:
  web: automated
---

# Tabel Borrowed: mekanik Filter Panel dan filter pada kolom yang disembunyikan

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > tab Borrowed.
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-110-1: baris pinjaman dengan Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0147`, Source `Self-service`, Duration `4 days`, Handed Over At `07/11/26, 09:10`.
  - DU-110-2: baris pinjaman dengan Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Overdue`, Due Date `06/11/26`, Remaining `3 days overdue`, Borrower `Me`, Transaction ID `BRW-2026-0148`, Source `Admin`, Duration `4 days`, Handed Over At `03/11/26, 09:00`.
  - DU-110-3: baris pinjaman dengan Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Extension Request`, Due Date `11/11/26`, Remaining `Due in 2 days`, Borrower `Me`, Transaction ID `BRW-2026-0164`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`.
  - DU-110-4: opsi field `Asset Name` di Filter Panel (10 opsi): `Laptop Dell Latitude 5420 - 2`, `Laptop Dell Latitude 5420 - 7`, `Laptop Dell Latitude 5420 - 8`, `Laptop Dell Latitude 5420 - 9`, `Laptop Dell Latitude 5420 - 10`, `Laptop Dell Latitude 5420 - 11`, `Laptop Dell Latitude 5420 - 51`, `Laptop Dell Latitude 5420 - 53`, `Meeting Mic Set - 2`, dan `Projector Epson EB-X06 - 12`.
  - DU-110-5: kata kunci pencarian di dalam dropdown: `Epson` (potongan dari tengah nama opsi), `epson` (huruf kecil), dan `Printer` (tidak cocok dengan opsi mana pun).
  - DU-110-6: opsi field `Asset Name` di Filter Panel berjumlah `0`.
  - DU-110-7: opsi field `Status` di Filter Panel: `Borrowed`, `Overdue`, dan `Extension Request`.
- Kondisi:
  - K1: daftar berisi DU-110-1 sampai DU-110-3, opsi Status memuat DU-110-7, dan filter Status `Borrowed` dijawab dengan DU-110-1 saja, filter Status `Borrowed` dan `Overdue` dijawab dengan DU-110-1 dan DU-110-2, filter Status `Overdue` dijawab dengan DU-110-2 saja, serta permintaan tanpa filter dijawab dengan DU-110-1 sampai DU-110-3. Date Format bernilai `dd/MM/yy`.
  - K2: daftar berisi DU-110-1 sampai DU-110-3 dan opsi Asset Name memuat DU-110-4.
  - K3: daftar berisi DU-110-1 sampai DU-110-3 dan opsi Asset Name memuat DU-110-6.

## Test Steps

### Isian Filter Panel adalah draf sampai Apply, dan chip yang dihapus ikut keluar dari saringan
1. Tampilkan Tabel Borrowed dengan kondisi K1
2. Klik ikon Filter
3. Klik field `Status`
4. Centang opsi `Borrowed`
5. Centang opsi `Overdue`
6. Verifikasi chip `Borrowed` dan `Overdue` tampil pada field `Status`
7. Verifikasi tabel belum berubah sebelum `[Apply]`: `Laptop Dell Latitude 5420 - 51` masih tampil
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan `Laptop Dell Latitude 5420 - 2` dan `Laptop Dell Latitude 5420 - 9`
10. Verifikasi `Laptop Dell Latitude 5420 - 51` tidak tampil sesudah `[Apply]`
11. Verifikasi indikator filter aktif tampil pada ikon Filter
12. Klik `(✕)` pada chip `Overdue`
13. Klik field `Status`
14. Verifikasi opsi `Overdue` tidak tercentang sesudah chipnya dihapus
15. Klik `[Apply]`
16. Verifikasi `Laptop Dell Latitude 5420 - 2` tampil
17. Verifikasi `Laptop Dell Latitude 5420 - 9` tidak tampil sesudah chip `Overdue` dihapus dan `[Apply]` diklik

### Menutup Filter Panel tanpa Apply membuang draf
18. Tampilkan Tabel Borrowed dengan kondisi K1
19. Klik ikon Filter
20. Klik field `Status`
21. Centang opsi `Overdue`
22. Klik ikon Filter
23. Verifikasi tabel tetap menampilkan `Laptop Dell Latitude 5420 - 2`, `Laptop Dell Latitude 5420 - 9`, dan `Laptop Dell Latitude 5420 - 51`
24. Klik ikon Filter
25. Verifikasi field `Status` tampil di Filter Panel
26. Verifikasi field `Status` tidak berisi opsi terpilih dan menampilkan placeholder `All statuses`
27. Verifikasi indikator filter aktif tidak tampil pada ikon Filter

### Clear Field hanya mengosongkan panel dan Apply tanpa isian tidak divalidasi
28. Tampilkan Tabel Borrowed dengan kondisi K1
29. Klik ikon Filter
30. Klik field `Status`
31. Centang opsi `Borrowed`
32. Klik `[Apply]`
33. Verifikasi `Laptop Dell Latitude 5420 - 2` tampil
34. Klik `[Clear Field]`
35. Verifikasi tabel belum berubah sesudah `[Clear Field]`: `Laptop Dell Latitude 5420 - 9` belum tampil
36. Klik `[Apply]`
37. Verifikasi tabel menampilkan kembali `Laptop Dell Latitude 5420 - 9` dan `Laptop Dell Latitude 5420 - 51`
38. Verifikasi tidak ada pesan error validasi pada Filter Panel sesudah `[Apply]` dengan seluruh field kosong
39. Verifikasi indikator filter aktif tidak tampil sesudah filter dilepas

### Chip overflow dan pencarian di dalam dropdown
40. Tampilkan Tabel Borrowed dengan kondisi K2
41. Klik ikon Filter
42. Klik field `Asset Name`
43. Pilih opsi `Laptop Dell Latitude 5420 - 2`, `Laptop Dell Latitude 5420 - 7`, `Laptop Dell Latitude 5420 - 8`, `Laptop Dell Latitude 5420 - 9`, `Laptop Dell Latitude 5420 - 11`, `Laptop Dell Latitude 5420 - 51`, `Laptop Dell Latitude 5420 - 53`, dan `Meeting Mic Set - 2`
44. Verifikasi chip ringkasan `+N more` tampil pada field `Asset Name`
45. Ketik di kotak cari dropdown `Epson`
46. Verifikasi opsi `Projector Epson EB-X06 - 12` tampil
47. Verifikasi opsi `Laptop Dell Latitude 5420 - 10` tidak tampil sesudah pencarian `Epson`
48. Ganti isi kotak cari dropdown dengan `epson`
49. Verifikasi opsi `Projector Epson EB-X06 - 12` tampil untuk kata kunci `epson` yang beda huruf kapital
50. Ganti isi kotak cari dropdown dengan `Printer`
51. Verifikasi `No results found.` tampil di dropdown[^drift-1]

### Sumber opsi kosong
52. Tampilkan Tabel Borrowed dengan kondisi K3
53. Klik ikon Filter
54. Klik field `Asset Name`
55. Verifikasi dropdown menampilkan `No options available`

### Filter tetap ada dan tetap berlaku sesudah kolom disembunyikan
56. Tampilkan Tabel Borrowed dengan kondisi K1
57. Klik ikon Filter
58. Klik field `Status`
59. Centang opsi `Borrowed`
60. Klik `[Apply]`
61. Verifikasi `Laptop Dell Latitude 5420 - 2` tampil
62. Klik header `⋯` (Column Visibility)
63. Hapus centang kolom `Status`
64. Verifikasi kolom `Asset ID` tampil di tabel
65. Verifikasi kolom `Status` tidak tampil di tabel
66. Verifikasi `Laptop Dell Latitude 5420 - 2` masih tampil sesudah kolom `Status` disembunyikan
67. Verifikasi `Laptop Dell Latitude 5420 - 9` tidak tampil sesudah kolom `Status` disembunyikan
68. Verifikasi indikator filter aktif tetap tampil pada ikon Filter
69. Verifikasi field `Status` tetap ada di Filter Panel dengan chip `Borrowed`
70. Klik `(✕)` pada chip `Borrowed`
71. Klik field `Status`
72. Centang opsi `Overdue`
73. Klik `[Apply]`
74. Verifikasi `Laptop Dell Latitude 5420 - 9` tampil sesudah kolom `Status` yang disembunyikan difilter ulang

[^drift-1]: Drift foundation vs kontrak komponen. PRD modul: tidak memuat teks ini dan menunjuk `prd-conventions.md` §9.8. foundation `prd-conventions.md` §9.8: dropdown filter menampilkan teks `"No results found"` bila pencarian di dalam dropdown tidak cocok. Kontrak `MultiSelect#41`: teks bawaan `No results found.` (dengan titik di akhir). Diasersi: kontrak, karena dropdown filter adalah MultiSelect wangs-ui dan teks bawaan komponen mengikuti kontraknya (SB-7).
