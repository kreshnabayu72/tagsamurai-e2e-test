---
id: TC-FA-FATR-BE-087-override-add
title: "Validasi Add override"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
owner: BE
sourceRules: ["§Aturan Logika Modul#r38", "§Aturan Logika Modul#r39", "§Aturan Logika Modul#r40", "§Aturan Logika Modul#r41", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r43", "§Aturan Logika Modul#r50", "§Aturan Logika Modul#r52", "§9.2#b74", "§9.2#b75", "§9.2#b76", "§9.2#b77", "§9.2#b80", "§9.2#b81", "§9.2#b84", "§9.2#b87", "§9.2#b90", "§9.2#b91", "§9.2#b94", "§9.2#b95", "§9.2#b96", "§9.2#b97", "§9.2#b101", "§9.2#b102", "§9.2#b143", "§9.2#b144", "§9.2#b174", "§9.2#b175", "§9.2#b182", "§9.2#b197", "§9.4.2#r26", "§9.4.2#r56", "§9.4.2#r104", "§9.4.2#r107", "§9.4.2#r110", "§9.4.3#b6", "§9.4.3#b7", "§9.4.4#r21", "§9.4.4#r30", "§9.6#r2", "§9.6#r20", "§9.6#r22", "§9.9#r13", "§9.9#r14", "§9.9#r15", "§9.9#r16", "§9.9#r21", "§9.10.4#b3", "§10#b2", EB-FRM-5@target-add-override]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r38": [2, 7]
  "§Aturan Logika Modul#r39": 2
  "§Aturan Logika Modul#r40": 2
  "§Aturan Logika Modul#r41": 3
  "§Aturan Logika Modul#r42": [17, 20]
  "§Aturan Logika Modul#r43": 15
  "§Aturan Logika Modul#r50": 40
  "§Aturan Logika Modul#r52": 32
  "§9.2#b74": [9, 10]
  "§9.2#b75": 2
  "§9.2#b76": 2
  "§9.2#b77": 3
  "§9.2#b80": 5
  "§9.2#b81": 5
  "§9.2#b84": [42, 44, 46, 48]
  "§9.2#b87": [50, 52, 54]
  "§9.2#b90": 12
  "§9.2#b91": 13
  "§9.2#b94": 32
  "§9.2#b95": 25
  "§9.2#b96": 33
  "§9.2#b97": 25
  "§9.2#b101": 26
  "§9.2#b102": [29, 30, 77, 78]
  "§9.2#b143": 20
  "§9.2#b144": 22
  "§9.2#b174": 32
  "§9.2#b175": [30, 34]
  "§9.2#b182": 15
  "§9.2#b197": 42
  "§9.4.2#r26": 32
  "§9.4.2#r56": 15
  "§9.4.2#r104": 32
  "§9.4.2#r107": 20
  "§9.4.2#r110": 22
  "§9.4.3#b6": 22
  "§9.4.3#b7": 26
  "§9.4.4#r21": [23, 70]
  "§9.4.4#r30": 32
  "§9.6#r2": 25
  "§9.6#r20": 37
  "§9.6#r22": 20
  "§9.9#r13": 57
  "§9.9#r14": 61
  "§9.9#r15": 63
  "§9.9#r16": [65, 67, 69]
  "§9.9#r21": 21
  "§9.10.4#b3": [72, 74]
  "§10#b2": 59
  EB-FRM-5@target-add-override: 21
---
# Validasi Add override

## Prerequisites
- Aktor: Maya Pengelola (DU-087-1) dan Budi Penyunting (DU-087-2), keduanya Total Control dengan cakupan seluruh Group.
- Data:
  - DU-087-1: User, pengelola yang menambahkan override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-087-2: User, pengelola kedua yang menghapus Group target: Name `Budi Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-087-3: Category, Category leaf tempat override dibuat: Name `Sensor Tambah {runId}`.
  - DU-087-4: Group, Group tujuan override pertama dan target duplikat: Name `Tim Tambah Satu {runId}`.
  - DU-087-5: Group, Group target override All categories dan Category leaf: Name `Tim Tambah Dua {runId}`.
  - DU-087-6: Group, Group target multi-target bersama duplikat: Name `Tim Tambah Tiga {runId}`.
  - DU-087-7: Group, Group target multi-target bersama duplikat: Name `Tim Tambah Empat {runId}`.
  - DU-087-8: Group, Group yang dihapus sebelum Submit: Name `Tim Hapus Tambah {runId}`.
  - DU-087-9: Group, Group pasangan target yang dihapus: Name `Tim Pasangan {runId}`.
  - DU-087-10: Group, Group target nilai sama dengan nilai berlaku: Name `Tim Nilai Sama {runId}`.
  - DU-087-11: Group, Group target field yang ditolak: Name `Tim Field Tolak {runId}`.
  - DU-087-12: Group, Group target Self service: Name `Tim Self Service {runId}`.
  - DU-087-13: Group, Group target validasi isian: Name `Tim Validasi {runId}`.
  - DU-087-14: Group, Group induk target override: Name `Divisi Induk Tambah {runId}`.
  - DU-087-15: Group, Group turunan dari Divisi Induk Tambah: Name `Seksi Anak Tambah {runId}`; Parent `Divisi Induk Tambah {runId}`.
  - DU-087-16: Group, Group volume target multi-target tanpa batas (12 record): Name `Tim Massal {n} {runId}`.
  - DU-087-17: Group, Group excess pada masa Grace: Name `Tim Excess Tambah {runId}`.
  - DU-087-18: Asset Name, Asset Name target override: Name `Nama Aset Tambah {runId}`; Category `Sensor Tambah {runId}`.
  - DU-087-19: Asset Name, Asset Name excess pada masa Grace: Name `Nama Excess Tambah {runId}`; Category `Sensor Tambah {runId}`.
  - DU-087-20: Asset, aset target override: Name `Perangkat Tambah {runId}`; Asset Name `Nama Aset Tambah {runId}`; Category `Sensor Tambah {runId}`; Group `Tim Tambah Satu {runId}`.
  - DU-087-21: Asset, aset di Group turunan: Name `Perangkat Seksi Tambah {runId}`; Asset Name `Nama Aset Tambah {runId}`; Category `Sensor Tambah {runId}`; Group `Seksi Anak Tambah {runId}`.
  - DU-087-24: Group, Group yang dinonaktifkan sebelum Submit: Name `Tim Nonaktif Tambah {runId}`.
  - DU-087-25: Group, Group pasangan target yang dinonaktifkan: Name `Tim Pasangan Dua {runId}`.
  - DU-087-22 dan DU-087-23 adalah nilai input yang ditolak server, bukan record yang sudah ada.
- Kondisi:
  - Belum ada override apa pun untuk seluruh target di atas.
  - Level Feature Suite Borrowing entitas bernilai `Full`.
  - Group `Tim Excess Tambah {runId}` dan Asset Name `Nama Excess Tambah {runId}` berstatus excess pada masa Grace.
  - Transaksi Borrow disebut «transaksi peminjaman» dan transaksi Assign disebut «transaksi penugasan» di langkah.

## Test Steps

### Satu override memiliki satu target, satu Category, satu transaksi, dan hanya field yang diubah
1. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Satu {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
2. Verifikasi terbentuk satu override dengan satu target `Tim Tambah Satu {runId}`, Category `Sensor Tambah {runId}`, dan satu transaksi
3. Verifikasi override itu hanya memuat Max duration `5`, dan field lain tidak tercantum di override
4. Maya Pengelola menambahkan override scope `Asset Name` dengan target `Nama Aset Tambah {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
5. Verifikasi terbentuk satu override untuk satu Asset Name dan satu transaksi, dengan Category `Sensor Tambah {runId}` sesuai node tempat override dibuat
6. Maya Pengelola menambahkan override scope aset dengan target `Perangkat Tambah {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
7. Verifikasi terbentuk satu override untuk satu target aset `Perangkat Tambah {runId}` dengan Category `Sensor Tambah {runId}` sesuai node tempat override dibuat

### Group sebagai target berlaku juga untuk turunannya tanpa override tersendiri
8. Maya Pengelola menambahkan override scope `Group` dengan target `Divisi Induk Tambah {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
9. Verifikasi hanya satu override yang terbentuk, untuk Group induk, dan tidak ada override tersendiri untuk Group turunan `Seksi Anak Tambah {runId}`
10. Verifikasi nilai efektif Max duration untuk aset `Perangkat Seksi Tambah {runId}` di Group turunan adalah `5`, karena override Group induk berlaku untuk turunannya

### Override All categories adalah satu override, bukan salinan per Category
11. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Dua {runId}` dari node All categories untuk transaksi peminjaman dengan Max duration `6`
12. Verifikasi terbentuk tepat satu override untuk Group `Tim Tambah Dua {runId}` dengan Category `All categories`
13. Verifikasi tidak ada salinan override untuk Group `Tim Tambah Dua {runId}` pada Category `Sensor Tambah {runId}`

### Override All categories dan Category leaf, atau transaksi berbeda, bukan duplikat
14. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Dua {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `7`
15. Verifikasi Add override diterima, bukan ditolak sebagai duplikat, sehingga override All categories dan override Category `Sensor Tambah {runId}` untuk Group `Tim Tambah Dua {runId}` dan transaksi yang sama tersimpan bersamaan
16. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Dua {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi penugasan dengan Max assets per assignee (concurrent) `2`
17. Verifikasi Add override diterima karena duplikat hanya bila Category, target, dan transaksi sama persis

### Override aktif yang sama ditolak dan tidak menulis log
18. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
19. Maya Pengelola menambahkan lagi override scope `Group` dengan target `Tim Tambah Satu {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`
20. Verifikasi Add override ditolak seluruhnya karena override aktif untuk Category, target, dan transaksi yang sama sudah ada
21. Verifikasi server menjawab penolakan itu dengan pesan `An active override already exists for this target, category, and transaction. Delete it first`
22. Verifikasi tetap ada tepat satu override untuk Group `Tim Tambah Satu {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman, dengan Max duration `5`, dan tidak ada override kedua
23. Verifikasi Changelog dan Activity Log tidak bertambah entri karena submit ditolak

### Satu target duplikat menolak seluruh submit multi-target secara atomik
24. Maya Pengelola menambahkan dalam satu submit override scope `Group` dengan target `Tim Tambah Satu {runId}`, `Tim Tambah Tiga {runId}`, dan `Tim Tambah Empat {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`, padahal `Tim Tambah Satu {runId}` sudah punya override aktif
25. Verifikasi seluruh submit ditolak karena satu target duplikat, tanpa memproses target lain
26. Verifikasi tidak ada override untuk Group `Tim Tambah Tiga {runId}` dan `Tim Tambah Empat {runId}`, sehingga tidak ada override yang tersimpan sebagian

### Target yang sudah dihapus antara pemilihan dan Submit menolak seluruh submit
27. Budi Penyunting menghapus Group `Tim Hapus Tambah {runId}`
28. Maya Pengelola menambahkan dalam satu submit override scope `Group` dengan target `Tim Hapus Tambah {runId}` dan `Tim Pasangan {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`
29. Verifikasi seluruh submit ditolak karena sebuah target sudah dihapus
30. Verifikasi tidak ada override untuk Group `Tim Pasangan {runId}`, sehingga semua terbuat atau tidak ada

### Banyak target dalam satu submit menjadi satu override per target tanpa batas jumlah
31. Maya Pengelola menambahkan dalam satu submit override scope `Group` dengan target dua belas Group `Tim Massal {n} {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `8`
32. Verifikasi terbentuk tepat dua belas override, satu per target, dan setiap Group `Tim Massal {n} {runId}` punya tepat satu override
33. Verifikasi submit dengan dua belas target tidak ditolak karena jumlah targetnya
34. Verifikasi seluruh dua belas override terbuat sekaligus

### Tiap Submit menambah override dan nilai baru boleh sama dengan nilai yang berlaku
35. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Tiga {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`
36. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Tambah Empat {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`
37. Verifikasi setiap Submit menambah tepat satu override, sehingga Add override tidak idempotent
38. Maya Pengelola membaca nilai Max duration yang berlaku untuk Group `Tim Nilai Sama {runId}` pada Category `Sensor Tambah {runId}`
39. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Nilai Sama {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration bernilai sama dengan nilai yang berlaku itu
40. Verifikasi Add override diterima dan override tersimpan walau nilainya sama dengan nilai yang berlaku

### Field multi-pilih dan field khusus All categories ditolak sebagai field override
41. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Field Tolak {runId}` pada Category `Sensor Tambah {runId}` dengan Transaction timeout `3`
42. Verifikasi Add override ditolak karena Transaction timeout tidak dapat dioverride, dan tidak ada override terbuat untuk Group `Tim Field Tolak {runId}`
43. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Field Tolak {runId}` pada Category `Sensor Tambah {runId}` dengan Send email notifications `ON`
44. Verifikasi Add override ditolak karena Send email notifications adalah field khusus All categories, dan tidak ada override terbuat
45. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Field Tolak {runId}` pada Category `Sensor Tambah {runId}` dengan Change Cost Center with Group `Always`
46. Verifikasi Add override ditolak karena Change Cost Center with Group adalah field khusus All categories, dan tidak ada override terbuat
47. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Field Tolak {runId}` pada Category `Sensor Tambah {runId}` dengan Allowed disposal types `Sell`
48. Verifikasi Add override ditolak karena Allowed disposal types adalah field multi-pilih, dan tidak ada override terbuat

### Semua scope menerima field yang sama termasuk Self service
49. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Self Service {runId}` dari node All categories dengan Self service `ON`
50. Verifikasi Add override scope `Group` diterima dan Self service `ON` tersimpan
51. Maya Pengelola menambahkan override scope `Asset Name` dengan target `Nama Aset Tambah {runId}` dari node All categories dengan Self service `ON`
52. Verifikasi Add override scope `Asset Name` diterima, Self service `ON` tersimpan, dan override itu memuat Category `All categories` sesuai node tempat override dibuat
53. Maya Pengelola menambahkan override scope aset dengan target `Perangkat Tambah {runId}` dari node All categories dengan Self service `ON`
54. Verifikasi Add override scope aset diterima, Self service `ON` tersimpan, dan override itu memuat Category `All categories` sesuai node tempat override dibuat

### Isian tidak valid ditolak server dan tidak membuat override
55. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
56. Maya Pengelola menambahkan override tanpa scope dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` dengan Max duration `5`
57. Verifikasi Add override ditolak dan tidak ada override untuk Group `Tim Validasi {runId}`
58. Maya Pengelola menambahkan override scope `Category` dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` dengan Max duration `5`
59. Verifikasi Add override ditolak karena override hanya untuk scope Group, Asset Name, dan aset, dan tidak ada override untuk Group `Tim Validasi {runId}`
60. Maya Pengelola menambahkan override scope `Group` tanpa target pada Category `Sensor Tambah {runId}` dengan Max duration `5`
61. Verifikasi Add override ditolak karena target minimal satu, dan tidak ada override terbuat
62. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` tanpa field
63. Verifikasi Add override ditolak karena minimal satu baris Field + Value diperlukan, dan tidak ada override untuk Group `Tim Validasi {runId}`
64. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` dengan Max duration dikosongkan
65. Verifikasi Add override ditolak karena value angka kosong, dan tidak ada override untuk Group `Tim Validasi {runId}`
66. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` dengan Max duration `0`
67. Verifikasi Add override ditolak karena value angka di bawah minimum 1, dan tidak ada override untuk Group `Tim Validasi {runId}`
68. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Validasi {runId}` pada Category `Sensor Tambah {runId}` dengan Allow Borrow tanpa value
69. Verifikasi Add override ditolak karena value pilihan kosong, dan tidak ada override untuk Group `Tim Validasi {runId}`
70. Verifikasi Changelog dan Activity Log tidak bertambah entri karena seluruh penolakan isian tidak valid di atas

### Status excess pada target tidak menghalangi Add override
71. Maya Pengelola menambahkan override scope `Group` dengan target `Tim Excess Tambah {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
72. Verifikasi Add override diterima untuk Group excess, karena Add override tidak memeriksa status excess
73. Maya Pengelola menambahkan override scope `Asset Name` dengan target `Nama Excess Tambah {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `5`
74. Verifikasi Add override diterima untuk Asset Name excess

### Target yang dinonaktifkan antara pemilihan dan Submit menolak seluruh submit
75. Budi Penyunting menonaktifkan Group `Tim Nonaktif Tambah {runId}`
76. Maya Pengelola menambahkan dalam satu submit override scope `Group` dengan target `Tim Nonaktif Tambah {runId}` dan `Tim Pasangan Dua {runId}` pada Category `Sensor Tambah {runId}` untuk transaksi peminjaman dengan Max duration `9`
77. Verifikasi seluruh submit ditolak karena sebuah target sudah dinonaktifkan
78. Verifikasi tidak ada override untuk Group `Tim Pasangan Dua {runId}`, sehingga semua terbuat atau tidak ada
