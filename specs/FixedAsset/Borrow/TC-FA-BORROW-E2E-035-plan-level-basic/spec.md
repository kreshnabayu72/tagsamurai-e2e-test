---
id: TC-FA-BORROW-E2E-035-plan-level-basic
title: "Level Basic menyembunyikan Draft, Self-service, Duration Hours, dan Request Extension dari My Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.11#b1", "§9.11#b2", "§9.11#b4", "§9.11#b5", "§9.11#b6", "§9.11#b7"]
smoke: []
dependsOn: []
trace:
  "§9.11#b1": [4, 9, 18, 19, 26, 29, 31]
  "§9.11#b2": [37, 38, 41, 42]
  "§9.11#b4": [44, 45, 46]
  "§9.11#b5": [52, 57, 59, 60]
  "§9.11#b6": [71, 72, 73, 74]
  "§9.11#b7": [29, 31, 62, 63, 66, 68]
anchor: [3, 51, 65]
coverage:
  web: automated
---

# Level Basic menyembunyikan Draft, Self-service, Duration Hours, dan Request Extension dari My Asset

## Prerequisites
- Aktor: Total Control, lalu Borrower pada langkah «Masuk sebagai Borrower».
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-035-1: Entitas `Mitra Logistik {runId}`, status Active, level Feature Suite Borrowing `Basic`.
  - DU-035-2: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-035-3: User `Rudi Hartono {runId}`, karyawan tanpa role Borrow, aktif, Home Group `Head Office {runId}`.
  - DU-035-4: Group `Head Office {runId}`.
  - DU-035-5: Group `Branch Surabaya {runId}`.
  - DU-035-6: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-035-7: Aset `Scanner Epson DS-530 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-035-8: Aset `Forklift Toyota 8FD {runId}`, Group `Branch Surabaya {runId}`, status Available.
  - DU-035-9: BRW berstatus Waiting for Handover (dibuat saat level `Full`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Maya Putri {runId}`.
  - DU-035-10: BRW berstatus Waiting for Handover (melewati batas pengambilan `Not picked up`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Maya Putri {runId}`.
  - DU-035-11: BRW berstatus Borrowed dengan Source `Self-service` (dibuat saat level `Full`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Maya Putri {runId}`.
  - DU-035-12: Transaction Settings tersimpan: Self service `ON` dan Duration unit `Hours`.
  - DU-035-13: BRW dibuat langkah spec: Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Scanner Epson DS-530 {runId}`, Duration `2`, Purpose `Pengukuran lapangan`.
  - DU-035-14: BRW dibuat langkah spec: Group `Branch Surabaya {runId}`, Borrower `Rudi Hartono {runId}`, aset `Forklift Toyota 8FD {runId}`, Duration `3`, Purpose `Angkut material`.
- Kondisi:
  - Spec ini memakai entitas khusus `Mitra Logistik {runId}` yang tidak dipakai spec lain.
  - Level Feature Suite Borrowing entitas itu bernilai `Basic`.
  - Akun `Rudi Hartono {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Form Borrow Request tanpa Save Draft menerima aset dari beberapa Group dan memecahnya saat Submit
1. Klik menu `Transactions > Borrow`
2. Klik `[+ Borrow]`
3. Verifikasi tombol `[Submit]` tampil di form `Borrow Request`
4. Verifikasi tombol `[Save Draft]` tidak tampil di form `Borrow Request`
5. Klik `[Select Borrower]`
6. Pilih Borrower `Rudi Hartono {runId}` pada dialog Select Borrower
7. Klik `[+ Asset]`
8. Pilih aset `Scanner Epson DS-530 {runId}` dan `Forklift Toyota 8FD {runId}` pada dialog Select Asset
9. Verifikasi tabel aset di form memuat `Scanner Epson DS-530 {runId}` dengan Group `Head Office {runId}` dan `Forklift Toyota 8FD {runId}` dengan Group `Branch Surabaya {runId}` dalam satu form
10. Isi Duration baris `Scanner Epson DS-530 {runId}` dengan `2`
11. Isi Purpose baris `Scanner Epson DS-530 {runId}` dengan `Pengukuran lapangan`
12. Isi Duration baris `Forklift Toyota 8FD {runId}` dengan `3`
13. Isi Purpose baris `Forklift Toyota 8FD {runId}` dengan `Angkut material`
14. Klik `[Submit]`
15. Konfirmasi dialog `D-BRW-03`
16. Klik tab `Transactions`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi BRW tersendiri untuk aset `Scanner Epson DS-530 {runId}` dengan Group `Head Office {runId}` tampil di tabel
19. Verifikasi BRW tersendiri untuk aset `Forklift Toyota 8FD {runId}` dengan Group `Branch Surabaya {runId}` tampil di tabel

### Isian form yang belum dikirim ditawarkan dipulihkan
20. Klik `[+ Borrow]`
21. Klik `[Select Borrower]`
22. Pilih Borrower `Rudi Hartono {runId}` pada dialog Select Borrower
23. Klik `[+ Asset]`
24. Pilih aset `Laptop Lenovo T14 {runId}` pada dialog Select Asset
25. Klik `✕` pada form
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]` pada dialog Unsaved Changes
28. Klik `[+ Borrow]`
29. Verifikasi dialog `Restore your unsent borrow?` tampil
30. Klik `[Restore]`
31. Verifikasi form `Borrow Request` memuat Borrower `Rudi Hartono {runId}` dan aset `Laptop Lenovo T14 {runId}`
32. Klik `✕` pada form
33. Klik `[Leave]` pada dialog Unsaved Changes

### Tabel aset: Add to Borrow Draft tidak tampil dan Borrow tetap ada
34. Klik menu `Assets > All`
35. Ketik Search `{runId}`, tekan Enter
36. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
37. Verifikasi aksi `Borrow` tampil pada menu baris
38. Verifikasi aksi `Add to Borrow Draft` tidak tampil pada menu baris
39. Centang baris aset `Laptop Lenovo T14 {runId}`
40. Klik `Bulk Action`
41. Verifikasi aksi `Borrow` tampil pada menu bulk
42. Verifikasi aksi `Add to Borrow Draft` tidak tampil pada menu bulk

### Transaction Settings: Self service dan Duration unit disabled
43. Buka halaman Transaction Settings
44. Verifikasi field `Self service` tampil disabled dengan tooltip `Available on plans with full Borrowing.`
45. Verifikasi field `Duration unit` tampil disabled dengan tooltip `Available on plans with full Borrowing.`
46. Verifikasi nilai tersimpan Self service `ON` dan Duration unit `Hours` dipertahankan

### Cancel Borrow tanpa Save as Draft to edit dan timeout menutup Canceled tanpa Draft baru
47. Klik menu `Transactions > Borrow`
48. Ketik Search `{runId}`, tekan Enter
49. Buka menu ⋯ pada baris BRW milik DU-035-9
50. Klik `Cancel Borrow`
51. Verifikasi dialog Cancel Borrow terbuka
52. Verifikasi checkbox `Save as Draft to edit` tidak tampil di dialog Cancel Borrow untuk BRW yang dibuat saat level Full
53. Klik `✕` pada dialog Cancel Borrow
54. Job batas pengambilan `Not picked up` berjalan untuk BRW milik DU-035-10
55. Klik tab `History`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi BRW milik DU-035-10 berstatus `Canceled` tampil di tabel
58. Buka Borrow Log lewat menu ⋯ pada baris BRW milik DU-035-10
59. Verifikasi node `Canceled by System` dengan alasan `Not picked up` tampil di Borrow Log
60. Verifikasi node `Canceled by System` tidak memuat tautan `Restored from`

### URL tab Drafts dan view borrower menampilkan tab dan sub-tab yang ada
61. Buka URL halaman Borrow dengan `?tab=drafts` secara langsung
62. Verifikasi tab `Transactions` yang tampil sebagai gantinya
63. Verifikasi tab `Drafts` tidak tampil
64. Klik tab `Borrowed Assets`
65. Verifikasi sub-tab `By Asset` tampil
66. Verifikasi sub-tab `By Borrower` tidak tampil
67. Buka URL halaman Borrowed Assets dengan `?view=borrower` secara langsung
68. Verifikasi sub-tab `By Asset` yang tampil sebagai gantinya

### Borrower dengan pinjaman self-service lama
69. Masuk sebagai Borrower `Rudi Hartono {runId}`
70. Buka halaman pinjaman pribadi Borrower dari menu Profile
71. Verifikasi tab `Borrowed` tampil dan memuat pinjaman self-service aset `Projector Epson EB-X06 {runId}`
72. Verifikasi aksi `Return` tampil pada baris pinjaman aset `Projector Epson EB-X06 {runId}`
73. Verifikasi aksi `Request Extension` tidak tampil pada baris pinjaman aset `Projector Epson EB-X06 {runId}`
74. Verifikasi aksi `Borrow an Asset` tidak tampil
