---
id: TC-FA-ASSIGN-UI-116-tabel-transactions-search-sort-paginasi
title: "Tabel Transactions: siklus Search, siklus Sort, dan paginasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRC-4@tabel-transactions", "EB-SRT-3@tabel-transactions", "EB-TBL-7@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "EB-SRC-4@tabel-transactions": [2, 4, 6, 8, 9, 15, 16, 17, 19, 25, 26]
  "EB-SRT-3@tabel-transactions": [29, 31, 33, 37, 38, 41]
  "EB-TBL-7@tabel-transactions": [44, 46, 49, 51, 55, 57, 59]
anchor: [13, 23, 40]
coverage:
  web: automated
---

# Tabel Transactions: siklus Search, siklus Sort, dan paginasi

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: Transactions > Assignment, tab Transactions.
- Komponen: Tabel Transactions
- Data:
  - DU-116-1: Assignment `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `09 Nov 2026, 19:00`, Last Updated `09 Nov 2026, 20:40`.
  - DU-116-2: Assignment `ASG-2026-0070`, Status `Waiting for Approval`, Group `Head Office`, Assignee `Sari D`, Assignee Type `Employee`, Total Asset `2`, Requested By `Agus P`, Request Date `09 Nov 2026, 14:00`, Last Updated `09 Nov 2026, 14:00`.
  - DU-116-3: 120 Assignment dengan pola `ASG-2025-{n}`, Status `Assigned`, Group `Head Office`, Assignee `Dewi K`, Assignee Type `Employee`, Total Asset `2`, Requested By `Agus P`, Request Date `02 Nov 2026, 08:30`, Last Updated `03 Nov 2026, 10:00`.
  - DU-116-4: kata kunci Search `Budi`, hanya terkandung di Assignee DU-116-1.
  - DU-116-5: nomor halaman tidak valid `abc`.
  - DU-116-6: nomor halaman di atas halaman terakhir `99`.
  - DU-116-7: nomor halaman di bawah 1 `0`.
- Kondisi:
  - K1: daftar berisi DU-116-1 dan DU-116-2.
  - K2: daftar berisi DU-116-3, ukuran halaman bawaan `10`, sehingga ada 12 halaman.

## Test Steps

### Ikon Search membuka input dan pencarian berjalan saat Enter
1. Tampilkan Tabel Transactions dengan kondisi K1
2. Verifikasi ikon Search tampil dan input Search belum tampil
3. Klik ikon Search
4. Verifikasi input Search tampil dan fokus berada di input itu
5. Ketik `Budi` pada input Search
6. Verifikasi tabel masih memuat baris `ASG-2026-0071` dan `ASG-2026-0070`
7. Tekan Enter
8. Verifikasi tabel memuat baris `ASG-2026-0071`
9. Verifikasi tabel tidak memuat baris `ASG-2026-0070`

### Klik ✕ sebelum Enter tidak mereset dan Enter dengan input kosong mereset
10. Tampilkan Tabel Transactions dengan kondisi K1
11. Klik ikon Search
12. Ketik Search `Budi`, tekan Enter
13. Verifikasi tabel memuat baris `ASG-2026-0071`
14. Klik `✕` pada input Search
15. Verifikasi input Search tetap terbuka
16. Verifikasi input Search kosong
17. Verifikasi tabel tidak memuat baris `ASG-2026-0070`
18. Tekan Enter pada input Search yang kosong
19. Verifikasi tabel memuat baris `ASG-2026-0070`

### Klik (←) menutup input sekaligus mereset
20. Tampilkan Tabel Transactions dengan kondisi K1
21. Klik ikon Search
22. Ketik Search `Budi`, tekan Enter
23. Verifikasi tabel memuat baris `ASG-2026-0071`
24. Klik `(←)` pada kotak Search
25. Verifikasi tabel memuat baris `ASG-2026-0070`
26. Verifikasi input Search tidak tampil

### Siklus tiga klik Sort pada satu kolom
27. Tampilkan Tabel Transactions dengan kondisi K1
28. Klik header kolom `Transaction ID`
29. Verifikasi header kolom `Transaction ID` menampilkan indikator `(↑)`
30. Klik header kolom `Transaction ID`
31. Verifikasi header kolom `Transaction ID` menampilkan indikator `(↓)`
32. Klik header kolom `Transaction ID`
33. Verifikasi header kolom `Transaction ID` tidak menampilkan indikator sort aktif

### Klik kolom lain memindahkan indikator Sort
34. Tampilkan Tabel Transactions dengan kondisi K1
35. Klik header kolom `Transaction ID`
36. Klik header kolom `Total Asset`
37. Verifikasi header kolom `Total Asset` menampilkan indikator `(↑)`
38. Verifikasi header kolom `Transaction ID` tidak menampilkan indikator sort aktif

### Kolom aksi baris tidak punya ikon sort
39. Tampilkan Tabel Transactions dengan kondisi K1
40. Verifikasi header kolom `Transaction ID` memiliki ikon sort
41. Verifikasi tidak ada ikon sort pada header kolom aksi baris

### Mengganti page size kembali ke halaman 1
42. Tampilkan Tabel Transactions dengan kondisi K2
43. Klik tombol halaman `3`
44. Verifikasi halaman `3` aktif
45. Pilih `25` pada dropdown `Rows per page`
46. Verifikasi halaman `1` aktif

### Mengganti sort tetap di halaman sekarang
47. Tampilkan Tabel Transactions dengan kondisi K2
48. Klik tombol halaman `3`
49. Verifikasi halaman `3` aktif
50. Klik header kolom `Transaction ID`
51. Verifikasi halaman `3` tetap aktif

### Nomor halaman tidak valid
52. Tampilkan Tabel Transactions dengan kondisi K2
53. Klik tombol halaman `3`
54. Ganti isi `Jump to page` dengan `abc`, tekan Enter
55. Verifikasi halaman `3` tetap aktif
56. Ganti isi `Jump to page` dengan `99`, tekan Enter
57. Verifikasi halaman `12` aktif
58. Ganti isi `Jump to page` dengan `0`, tekan Enter
59. Verifikasi halaman `1` aktif
