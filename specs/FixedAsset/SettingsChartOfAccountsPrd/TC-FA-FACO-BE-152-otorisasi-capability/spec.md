---
id: TC-FA-FACO-BE-152-otorisasi-capability
title: "Otorisasi baca dan tulis per capability Manage accounting"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: ["§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.3#p1", "§9.3#p2", "§9.4.2#r30", "§9.4.2#r31", "§9.4.2#r34", EB-AKS-3@create-account, EB-AKS-3@edit-account, EB-AKS-3@activate-account, EB-AKS-3@deactivate-account, EB-AKS-3@delete-account]
smoke: []
dependsOn: []
trace:
  "§9.3#r1": [2, 16, 26, 28, 30, 32, 74, 76, 78, 80]
  "§9.3#r2": [6, 18, 34, 44, 54, 60, 64, 70, 82]
  "§9.3#r3": [8, 10, 12, 20, 22, 36, 38, 40, 46, 50, 52, 62, 66, 68, 84, 86, 88]
  "§9.3#r4": [14, 24, 42, 48, 56, 58, 72, 90]
  "§9.3#p1": [4, 34, 36, 38, 40, 42]
  "§9.3#p2": [28, 30, 32, 74, 76, 78, 80]
  "§9.4.2#r30": [34, 36, 38, 40, 42, 46, 48, 54, 56, 60, 62, 66, 68, 70, 72, 82, 84, 86, 88, 90]
  "§9.4.2#r31": [74, 76, 78, 80, 82, 84, 86, 88, 90]
  "§9.4.2#r34": [66, 68, 72]
  EB-AKS-3@create-account: [34, 54, 60, 70, 82]
  EB-AKS-3@edit-account: [36, 46, 62, 66, 84]
  EB-AKS-3@activate-account: [38, 86]
  EB-AKS-3@deactivate-account: [40, 68, 88]
  EB-AKS-3@delete-account: [42, 48, 56, 72, 90]
---

# Otorisasi baca dan tulis per capability Manage accounting

## Prerequisites
- Aktor: sepuluh aktor di client yang sama, DU-152-1 sampai DU-152-10, dengan capability seperti di Data. Semua aktor adalah pengguna terdaftar.
- Data:
  - DU-152-1: User `Budi Total {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-152-2: User `Rina ReadOnly {runId}`, Access Level `Read Only`, cakupan seluruh client.
  - DU-152-3: User `Dewi Akuntansi {runId}`, Global Role `Manage accounting` dengan Read, Create, Update, dan Delete, cakupan seluruh client.
  - DU-152-4: User `Agus Pencatat {runId}`, Global Role `Manage accounting` dengan Read dan Create saja, cakupan seluruh client.
  - DU-152-5: User `Putri Pengubah {runId}`, Global Role `Manage accounting` dengan Read dan Update saja, cakupan seluruh client.
  - DU-152-6: User `Hendra Penghapus {runId}`, Global Role `Manage accounting` dengan Read dan Delete saja, cakupan seluruh client.
  - DU-152-7: User `Joko Pencatat Penghapus {runId}`, Global Role `Manage accounting` dengan Read, Create, dan Delete tanpa Update, cakupan seluruh client.
  - DU-152-8: User `Sari Pengubah Penghapus {runId}`, Global Role `Manage accounting` dengan Read, Update, dan Delete tanpa Create, cakupan seluruh client.
  - DU-152-9: User `Tono Pencatat Pengubah {runId}`, Global Role `Manage accounting` dengan Read, Create, dan Update tanpa Delete, cakupan seluruh client.
  - DU-152-10: User `Gilang Manajer {runId}`, Access Level `Group Manager` tanpa Global Role `Manage accounting`, cakupan satu Group.
  - DU-152-11: Account Code `OTR-{runId}`, Account Name `Kas Otorisasi {runId}`, Account Function `Asset Cost`, Status `Active`, ada di client aktor.
  - DU-152-12: Account Code `OTI-{runId}`, Account Name `Kas Nonaktif Otorisasi {runId}`, Account Function `Asset Cost`, Status `Inactive`, ada di client aktor.
  - DU-152-13: Account Code `OTL-{runId}`, Account Name `Kas Client Lain {runId}`, Account Function `Asset Cost`, ada di client lain, bukan client aktor.
  - DU-152-14: Account Code `EDT1-{runId}`, Account Name `Beban Listrik {runId}`, Account Function `Depreciation Expense`.
  - DU-152-15: Account Code `ACT1-{runId}`, Account Name `Kas Nonaktif Satu {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-152-16: Account Code `DCT1-{runId}`, Account Name `Kas Aktif Satu {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-152-17: Account Code `DEL1-{runId}`, Account Name `Kas Hapus Satu {runId}`, Account Function `Asset Cost`.
  - DU-152-18: Account Code `EDT3-{runId}`, Account Name `Beban Air {runId}`, Account Function `Depreciation Expense`.
  - DU-152-19: Account Code `DCT3-{runId}`, Account Name `Kas Aktif Tiga {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-152-20: Account Code `DEL3-{runId}`, Account Name `Kas Hapus Tiga {runId}`, Account Function `Asset Cost`.
  - DU-152-21: Account Code `EDT5-{runId}`, Account Name `Beban Telepon {runId}`, Account Function `Depreciation Expense`.
  - DU-152-22: Account Code `ACT5-{runId}`, Account Name `Kas Nonaktif Lima {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-152-23: Account Code `DEL6-{runId}`, Account Name `Kas Hapus Enam {runId}`, Account Function `Asset Cost`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class, sehingga tidak ada field yang terkunci.
  - Batas jumlah akun client belum tercapai.

## Test Steps

### Total Control membaca dan menulis
1. Aktor Total Control (DU-152-1) membaca daftar akun client dengan Account Code `OTR-{runId}`
2. Verifikasi permintaan baca diterima dan hasilnya memuat akun `OTR-{runId}` dengan Account Name `Kas Otorisasi {runId}`
3. Aktor Total Control (DU-152-1) membaca daftar akun client dengan Account Code `OTL-{runId}`
4. Verifikasi hasil baca tidak memuat akun dengan Account Code `OTL-{runId}` milik client lain, karena data yang dibaca ter-scope di server
5. Aktor Total Control (DU-152-1) mengirim Create dengan Account Code `CRT1-{runId}`, Account Name `Kas Dibuat Total Control {runId}`, Account Function `Asset Cost`
6. Verifikasi permintaan diterima dan akun dengan Account Code `CRT1-{runId}` tersimpan dengan Account Name `Kas Dibuat Total Control {runId}`
7. Aktor Total Control (DU-152-1) mengirim Edit akun `EDT1-{runId}` dengan Account Name `Beban Listrik Terbaru {runId}`
8. Verifikasi permintaan diterima dan akun `EDT1-{runId}` tersimpan dengan Account Name `Beban Listrik Terbaru {runId}`
9. Aktor Total Control (DU-152-1) mengirim Activate akun `ACT1-{runId}`
10. Verifikasi permintaan diterima dan akun `ACT1-{runId}` berstatus `Active`
11. Aktor Total Control (DU-152-1) mengirim Deactivate akun `DCT1-{runId}`
12. Verifikasi permintaan diterima dan akun `DCT1-{runId}` berstatus `Inactive`
13. Aktor Total Control (DU-152-1) mengirim Delete akun `DEL1-{runId}`
14. Verifikasi permintaan diterima dan tidak ada lagi akun dengan Account Code `DEL1-{runId}`

### Manage accounting dengan Read, Create, Update, dan Delete membaca dan menulis
15. Aktor Manage accounting dengan Read, Create, Update, dan Delete (DU-152-3) membaca daftar akun client dengan Account Code `OTR-{runId}`
16. Verifikasi permintaan baca diterima dan hasilnya memuat akun `OTR-{runId}` dengan Account Name `Kas Otorisasi {runId}`
17. Aktor Manage accounting dengan Read, Create, Update, dan Delete (DU-152-3) mengirim Create dengan Account Code `CRT3-{runId}`, Account Name `Kas Dibuat Manage Accounting {runId}`, Account Function `Asset Cost`
18. Verifikasi permintaan diterima dan akun dengan Account Code `CRT3-{runId}` tersimpan dengan Account Name `Kas Dibuat Manage Accounting {runId}`
19. Aktor Manage accounting dengan Read, Create, Update, dan Delete (DU-152-3) mengirim Edit akun `EDT3-{runId}` dengan Account Name `Beban Air Terbaru {runId}`
20. Verifikasi permintaan diterima dan akun `EDT3-{runId}` tersimpan dengan Account Name `Beban Air Terbaru {runId}`
21. Aktor Manage accounting dengan Read, Create, Update, dan Delete (DU-152-3) mengirim Deactivate akun `DCT3-{runId}`
22. Verifikasi permintaan diterima dan akun `DCT3-{runId}` berstatus `Inactive`
23. Aktor Manage accounting dengan Read, Create, Update, dan Delete (DU-152-3) mengirim Delete akun `DEL3-{runId}`
24. Verifikasi permintaan diterima dan tidak ada lagi akun dengan Account Code `DEL3-{runId}`

### Read Only dapat membaca semua surface baca dan ditolak untuk setiap aksi tulis
25. Aktor Read Only (DU-152-2) membaca daftar akun client dengan Account Code `OTR-{runId}`
26. Verifikasi permintaan baca diterima dan hasilnya memuat akun `OTR-{runId}` dengan Account Name `Kas Otorisasi {runId}`
27. Aktor Read Only (DU-152-2) membaca daftar pemakai (Used By) akun `OTR-{runId}`
28. Verifikasi permintaan baca daftar pemakai diterima
29. Aktor Read Only (DU-152-2) membaca Changelog Chart of Accounts
30. Verifikasi permintaan baca Changelog diterima
31. Aktor Read Only (DU-152-2) meminta Download daftar akun
32. Verifikasi permintaan Download diterima
33. Aktor Read Only (DU-152-2) mengirim Create dengan Account Code `DNY-{runId}`, Account Name `Akun Tanpa Izin {runId}`, Account Function `Asset Cost`
34. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Create, dan tidak ada akun dengan Account Code `DNY-{runId}`
35. Aktor Read Only (DU-152-2) mengirim Edit akun `OTR-{runId}` dengan Account Name `Nilai Ditolak {runId}`
36. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap bernama `Kas Otorisasi {runId}`
37. Aktor Read Only (DU-152-2) mengirim Activate akun `OTI-{runId}`
38. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTI-{runId}` tetap `Inactive`
39. Aktor Read Only (DU-152-2) mengirim Deactivate akun `OTR-{runId}`
40. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap `Active`
41. Aktor Read Only (DU-152-2) mengirim Delete akun `OTR-{runId}`
42. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Delete, dan akun `OTR-{runId}` masih ada dengan Account Name `Kas Otorisasi {runId}`

### Aktor dengan Create saja membuat akun tetapi ditolak untuk Edit dan Delete
43. Aktor dengan Read dan Create saja (DU-152-4) mengirim Create dengan Account Code `CRT4-{runId}`, Account Name `Kas Dibuat Pencatat {runId}`, Account Function `Asset Cost`
44. Verifikasi permintaan diterima dan akun dengan Account Code `CRT4-{runId}` tersimpan dengan Account Name `Kas Dibuat Pencatat {runId}`
45. Aktor dengan Read dan Create saja (DU-152-4) mengirim Edit akun `OTR-{runId}` dengan Account Name `Nilai Ditolak {runId}`
46. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap bernama `Kas Otorisasi {runId}`
47. Aktor dengan Read dan Create saja (DU-152-4) mengirim Delete akun `OTR-{runId}`
48. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Delete, dan akun `OTR-{runId}` masih ada dengan Account Name `Kas Otorisasi {runId}`

### Aktor dengan Update saja mengubah akun tetapi ditolak untuk Create dan Delete
49. Aktor dengan Read dan Update saja (DU-152-5) mengirim Edit akun `EDT5-{runId}` dengan Account Name `Beban Telepon Terbaru {runId}`
50. Verifikasi permintaan diterima dan akun `EDT5-{runId}` tersimpan dengan Account Name `Beban Telepon Terbaru {runId}`
51. Aktor dengan Read dan Update saja (DU-152-5) mengirim Activate akun `ACT5-{runId}`
52. Verifikasi permintaan diterima dan akun `ACT5-{runId}` berstatus `Active`
53. Aktor dengan Read dan Update saja (DU-152-5) mengirim Create dengan Account Code `DNY-{runId}`, Account Name `Akun Tanpa Izin {runId}`, Account Function `Asset Cost`
54. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Create, dan tidak ada akun dengan Account Code `DNY-{runId}`
55. Aktor dengan Read dan Update saja (DU-152-5) mengirim Delete akun `OTR-{runId}`
56. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Delete, dan akun `OTR-{runId}` masih ada dengan Account Name `Kas Otorisasi {runId}`

### Aktor dengan Delete saja menghapus akun tetapi ditolak untuk Create dan Edit
57. Aktor dengan Read dan Delete saja (DU-152-6) mengirim Delete akun `DEL6-{runId}`
58. Verifikasi permintaan diterima dan tidak ada lagi akun dengan Account Code `DEL6-{runId}`
59. Aktor dengan Read dan Delete saja (DU-152-6) mengirim Create dengan Account Code `DNY-{runId}`, Account Name `Akun Tanpa Izin {runId}`, Account Function `Asset Cost`
60. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Create, dan tidak ada akun dengan Account Code `DNY-{runId}`
61. Aktor dengan Read dan Delete saja (DU-152-6) mengirim Edit akun `OTR-{runId}` dengan Account Name `Nilai Ditolak {runId}`
62. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap bernama `Kas Otorisasi {runId}`

### Aktor dengan Create dan Delete tanpa Update ditolak untuk Edit dan Deactivate
63. Aktor dengan Read, Create, dan Delete tanpa Update (DU-152-7) mengirim Create dengan Account Code `CRT7-{runId}`, Account Name `Kas Dibuat Kombinasi {runId}`, Account Function `Asset Cost`
64. Verifikasi permintaan diterima dan akun dengan Account Code `CRT7-{runId}` tersimpan dengan Account Name `Kas Dibuat Kombinasi {runId}`
65. Aktor dengan Read, Create, dan Delete tanpa Update (DU-152-7) mengirim Edit akun `OTR-{runId}` dengan Account Name `Nilai Ditolak {runId}`
66. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap bernama `Kas Otorisasi {runId}`
67. Aktor dengan Read, Create, dan Delete tanpa Update (DU-152-7) mengirim Deactivate akun `OTR-{runId}`
68. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap `Active`

### Aktor dengan Update dan Delete tanpa Create ditolak untuk Create
69. Aktor dengan Read, Update, dan Delete tanpa Create (DU-152-8) mengirim Create dengan Account Code `DNY-{runId}`, Account Name `Akun Tanpa Izin {runId}`, Account Function `Asset Cost`
70. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Create, dan tidak ada akun dengan Account Code `DNY-{runId}`

### Aktor dengan Create dan Update tanpa Delete ditolak untuk Delete
71. Aktor dengan Read, Create, dan Update tanpa Delete (DU-152-9) mengirim Delete akun `OTR-{runId}`
72. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Delete, dan akun `OTR-{runId}` masih ada dengan Account Name `Kas Otorisasi {runId}`

### Aktor Group Manager tanpa Manage accounting ditolak untuk semua aksi baca dan tulis
73. Aktor Group Manager tanpa Manage accounting (DU-152-10) membaca daftar akun client dengan Account Code `OTR-{runId}`
74. Verifikasi permintaan baca daftar akun ditolak (Forbidden), dan tidak ada data akun yang dikembalikan
75. Aktor Group Manager tanpa Manage accounting (DU-152-10) membaca daftar pemakai (Used By) akun `OTR-{runId}`
76. Verifikasi permintaan baca daftar pemakai ditolak (Forbidden)
77. Aktor Group Manager tanpa Manage accounting (DU-152-10) membaca Changelog Chart of Accounts
78. Verifikasi permintaan baca Changelog ditolak (Forbidden)
79. Aktor Group Manager tanpa Manage accounting (DU-152-10) meminta Download daftar akun
80. Verifikasi permintaan Download ditolak (Forbidden)
81. Aktor Group Manager tanpa Manage accounting (DU-152-10) mengirim Create dengan Account Code `DNY-{runId}`, Account Name `Akun Tanpa Izin {runId}`, Account Function `Asset Cost`
82. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Create, dan tidak ada akun dengan Account Code `DNY-{runId}`
83. Aktor Group Manager tanpa Manage accounting (DU-152-10) mengirim Edit akun `OTR-{runId}` dengan Account Name `Nilai Ditolak {runId}`
84. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap bernama `Kas Otorisasi {runId}`
85. Aktor Group Manager tanpa Manage accounting (DU-152-10) mengirim Activate akun `OTI-{runId}`
86. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTI-{runId}` tetap `Inactive`
87. Aktor Group Manager tanpa Manage accounting (DU-152-10) mengirim Deactivate akun `OTR-{runId}`
88. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Update, dan akun `OTR-{runId}` tetap `Active`
89. Aktor Group Manager tanpa Manage accounting (DU-152-10) mengirim Delete akun `OTR-{runId}`
90. Verifikasi permintaan ditolak (Forbidden) karena aktor tidak punya capability Delete, dan akun `OTR-{runId}` masih ada dengan Account Name `Kas Otorisasi {runId}`
