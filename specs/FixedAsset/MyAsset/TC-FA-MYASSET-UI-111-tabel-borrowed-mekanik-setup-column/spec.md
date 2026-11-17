---
id: TC-FA-MYASSET-UI-111-tabel-borrowed-mekanik-setup-column
title: "Tabel Borrowed: mekanik Setup Column dan kolom terakhir yang tetap tampil"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§5#r8", "EB-KOL-1@tabel-borrowed"]
smoke: []
dependsOn: []
trace:
  "§5#r8": [65, 67, 69, 73, 74]
  "EB-KOL-1@tabel-borrowed": [4, 5, 6, 7, 8, 9, 16, 17, 18, 24, 31, 33, 35, 42, 46, 48, 54, 57, 60, 65, 67, 69, 73, 74]
anchor: [41]
coverage:
  web: automated
---

# Tabel Borrowed: mekanik Setup Column dan kolom terakhir yang tetap tampil

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > tab Borrowed.
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-111-1: baris pinjaman dengan Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0147`, Source `Self-service`, Duration `4 days`, Handed Over At `07/11/26, 09:10`, TAG `RFID`, Category `Laptop`, Extensions `0 / 2`, Purpose `Presentasi klien`.
  - DU-111-2: konfigurasi kolom tersimpan milik Borrower yang hanya menampilkan kolom `Name` dan `Status`.
- Kondisi:
  - K1: daftar berisi DU-111-1 dan konfigurasi kolom bawaan. Date Format bernilai `dd/MM/yy`.
  - K2: daftar berisi DU-111-1 dan konfigurasi kolom tersimpan DU-111-2.

## Test Steps

### Anatomi modal Setup Column
1. Tampilkan Tabel Borrowed dengan kondisi K1
2. Klik header `⋯` (Column Visibility)
3. Klik `Setup Column...`
4. Verifikasi judul modal `Setup Column`
5. Verifikasi deskripsi modal `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.`
6. Verifikasi footer modal memuat `[Reset to Default]` dan `[Save]`
7. Verifikasi footer modal tidak memuat tombol `[Cancel]`
8. Verifikasi kolom bawaan `Name`, `Brand`, dan `Source` tercentang
9. Verifikasi kolom tambahan `TAG`, `Category`, `Extensions`, dan `Purpose` tidak tercentang

### Hide dan show kolom berlaku sesudah Save
10. Tampilkan Tabel Borrowed dengan kondisi K1
11. Klik header `⋯` (Column Visibility)
12. Klik `Setup Column...`
13. Hapus centang kolom `Brand`
14. Centang kolom `TAG`
15. Klik `[Save]`
16. Verifikasi modal Setup Column tertutup sesudah `[Save]`
17. Verifikasi header `TAG` tampil di tabel
18. Verifikasi header `Brand` tidak tampil di tabel

### Reorder kolom berlaku sesudah Save
19. Tampilkan Tabel Borrowed dengan kondisi K1
20. Klik header `⋯` (Column Visibility)
21. Klik `Setup Column...`
22. Seret baris kolom `Source` ke atas baris kolom `Brand`
23. Klik `[Save]`
24. Verifikasi urutan kolom di tabel menempatkan `Source` sebelum `Brand`

### Pin kolom dan batas tiga kolom
25. Tampilkan Tabel Borrowed dengan kondisi K1
26. Klik header `⋯` (Column Visibility)
27. Klik `Setup Column...`
28. Klik ikon pin kolom `Name`
29. Klik ikon pin kolom `Asset ID`
30. Klik ikon pin kolom `Brand`
31. Verifikasi ikon pin kolom `Group` disabled
32. Arahkan kursor ke ikon pin kolom `Group`
33. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin kolom `Group` yang disabled
34. Klik ikon pin kolom `Brand`
35. Verifikasi ikon pin kolom `Group` aktif kembali sesudah satu kolom di-unpin

### Reset to Default mengembalikan kolom bawaan
36. Tampilkan Tabel Borrowed dengan kondisi K1
37. Klik header `⋯` (Column Visibility)
38. Klik `Setup Column...`
39. Hapus centang kolom `Brand`
40. Klik `[Save]`
41. Verifikasi header `Name` tampil di tabel
42. Verifikasi header `Brand` tidak tampil di tabel sesudah disimpan
43. Klik header `⋯` (Column Visibility)
44. Klik `Setup Column...`
45. Klik `[Reset to Default]`
46. Verifikasi kolom `Brand` tercentang kembali sesudah `[Reset to Default]`
47. Klik `[Save]`
48. Verifikasi header `Brand` tampil di tabel sesudah hasil reset disimpan

### Menutup modal tanpa Save membuang perubahan
49. Tampilkan Tabel Borrowed dengan kondisi K1
50. Klik header `⋯` (Column Visibility)
51. Klik `Setup Column...`
52. Hapus centang kolom `Model/Type`
53. Klik `✕` pada modal Setup Column
54. Verifikasi header `Model/Type` masih tampil di tabel sesudah modal ditutup lewat `✕`
55. Klik header `⋯` (Column Visibility)
56. Klik `Setup Column...`
57. Verifikasi kolom `Model/Type` tercentang, karena perubahan dibuang
58. Hapus centang kolom `Group`
59. Tekan Esc
60. Verifikasi header `Group` masih tampil di tabel sesudah modal ditutup lewat Esc

### Kolom terakhir yang tampil tidak bisa disembunyikan di modal Setup Column
61. Tampilkan Tabel Borrowed dengan kondisi K2
62. Klik header `⋯` (Column Visibility)
63. Klik `Setup Column...`
64. Hapus centang kolom `Status`
65. Verifikasi checkbox kolom `Name` disabled
66. Arahkan kursor ke checkbox kolom `Name`
67. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada checkbox kolom `Name` yang disabled
68. Centang kolom `Status`
69. Verifikasi checkbox kolom `Name` aktif kembali sesudah ada dua kolom yang tampil

### Kolom terakhir yang tampil tidak bisa disembunyikan di panel Column Visibility
70. Tampilkan Tabel Borrowed dengan kondisi K2
71. Klik header `⋯` (Column Visibility)
72. Hapus centang kolom `Status` pada panel Column Visibility
73. Verifikasi checkbox kolom `Name` disabled pada panel Column Visibility
74. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada checkbox kolom `Name` di panel Column Visibility
