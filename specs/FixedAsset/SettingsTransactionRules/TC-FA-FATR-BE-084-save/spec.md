---
id: TC-FA-FATR-BE-084-save
title: "Validasi dan atomisitas Save Changes"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: ["§8.1#b1", "§8.1#b2", "§9.2#b23", "§9.2#b25", "§9.2#b28", "§9.2#b29", "§9.2#b38", "§9.2#b39", "§9.2#b40", "§9.2#b41", "§9.2#b44", "§9.2#b45", "§9.2#b46", "§9.2#b53", "§9.2#b60", "§9.2#b198", "§9.2#b202", "§9.2#b209", "§9.2#b210", "§9.2#b211", "§9.2#b299", "§9.4.2#r5", "§9.4.2#r81", "§9.4.4#r14", "§9.6#r6", "§9.6#r7", "§9.6#r10", "§9.6#r16", "§9.6#r17", "§9.9#r1", "§9.9#r2", "§9.9#r3", "§9.9#r4", "§9.9#r5", "§9.9#r6", "§9.9#r7", "§9.9#r8", "§9.9#r9", "§9.9#r10", "§9.9#r11", "§9.10.4#b3", EB-ERR-4]
smoke: []
dependsOn: []
trace:
  "§8.1#b1": [73, 74]
  "§8.1#b2": [60, 61]
  "§9.2#b23": [4, 7]
  "§9.2#b25": 3
  "§9.2#b28": 6
  "§9.2#b29": 6
  "§9.2#b38": 69
  "§9.2#b39": 70
  "§9.2#b40": 65
  "§9.2#b41": [65, 66]
  "§9.2#b44": 76
  "§9.2#b45": 76
  "§9.2#b46": 77
  "§9.2#b53": 60
  "§9.2#b60": 8
  "§9.2#b198": 52
  "§9.2#b202": 54
  "§9.2#b209": [52, 54]
  "§9.2#b210": 56
  "§9.2#b211": 54
  "§9.2#b299": 56
  "§9.4.2#r5": 60
  "§9.4.2#r81": 3
  "§9.4.4#r14": [60, 61]
  "§9.6#r6": 61
  "§9.6#r7": 60
  "§9.6#r10": 3
  "§9.6#r16": 8
  "§9.6#r17": 7
  "§9.9#r1": [10, 12]
  "§9.9#r2": [14, 16]
  "§9.9#r3": [18, 20]
  "§9.9#r4": [22, 24]
  "§9.9#r5": [26, 28]
  "§9.9#r6": [30, 32]
  "§9.9#r7": [34, 36]
  "§9.9#r8": [38, 40]
  "§9.9#r9": [42, 44]
  "§9.9#r10": [46, 48]
  "§9.9#r11": 50
  "§9.10.4#b3": 79
  EB-ERR-4: 7
---
# Validasi dan atomisitas Save Changes

## Prerequisites
- Aktor: Maya Pengelola (DU-084-2) dan Budi Penyunting (DU-084-3), keduanya Total Control dengan cakupan seluruh entitas.
- Data:
  - DU-084-1: Entitas, entitas khusus spec ini: Name `Entitas Simpan {runId}`.
  - DU-084-2: User, pengelola yang mengirim Save: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-084-3: User, pengelola kedua yang mengirim Save lebih dulu: Name `Budi Penyunting {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-084-4: Category, Category leaf yang mewarisi seluruh nilai: Name `Kendaraan Dinas {runId}`.
  - DU-084-5: Category, Category leaf yang mewarisi seluruh nilai: Name `Peralatan Kantor {runId}`.
  - DU-084-6: Category, Category leaf yang berstatus excess pada masa Grace: Name `Aset Lama {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Simpan {runId}` (DU-084-1) yang tidak dipakai spec lain, karena yang diasersi adalah setting Company default dan setting Category.
  - Seluruh setting Company default bernilai default: Max duration `14`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Max assets per assignee (concurrent) `0`, In-transit overdue after `7`, Min asset age warning `12`, Max deviation from book value `30`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Require approval `ON`, Transaction timeout `7`, dan Long missing after `30`.
  - Allowed disposal types Company default berisi `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, dan `Write-off`.
  - Seluruh field setiap Category pada entitas ini bernilai Inherit.
  - Entitas berada pada masa Grace dan Category `Aset Lama {runId}` berstatus excess.
  - Nilai di langkah ditulis pada tab transaksi pemilik fieldnya; Max duration, Max extensions, Max assets per borrower (concurrent), dan Auto-approve when duration ≤ ada pada transaksi Borrow, yang di langkah disebut «transaksi peminjaman».

## Test Steps

### Save yang valid menyimpan seluruh perubahan dari beberapa node sekaligus
1. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
2. Maya Pengelola mengirim satu Save berisi Max duration Company default `21`, In-transit overdue after Category `Kendaraan Dinas {runId}` `10`, dan Min asset age warning Category `Peralatan Kantor {runId}` `6`
3. Verifikasi ketiga perubahan tersimpan: Max duration Company default `21`, In-transit overdue after Category `Kendaraan Dinas {runId}` `10`, dan Min asset age warning Category `Peralatan Kantor {runId}` `6`
4. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat tiga entri, satu per field yang berubah

### Draft tidak valid di node lain menolak seluruh Save secara atomik
5. Maya Pengelola mengirim satu Save berisi Max duration Company default `25` dan Max deviation from book value Category `Peralatan Kantor {runId}` `0`
6. Verifikasi Save tidak diproses karena seluruh draft divalidasi, termasuk draft pada node Category lain
7. Verifikasi Max duration Company default tetap `21` dan Max deviation from book value Category `Peralatan Kantor {runId}` tetap Inherit, karena Save atomik: semua perubahan draft tersimpan atau tidak ada yang tersimpan
8. Verifikasi Save yang tidak berhasil diproses tidak meninggalkan perubahan tersimpan di node mana pun

### Max duration kosong atau di bawah minimum ditolak server
9. Maya Pengelola mengirim Save pada Company default dengan Max duration dikosongkan
10. Verifikasi Save ditolak dan Max duration tetap `21`, tidak ada yang tersimpan
11. Maya Pengelola mengirim Save pada Company default dengan Max duration `0`
12. Verifikasi Save ditolak dan Max duration tetap `21`, tidak ada yang tersimpan

### Max extensions kosong atau di bawah minimum ditolak server
13. Maya Pengelola mengirim Save pada Company default dengan Max extensions dikosongkan
14. Verifikasi Save ditolak dan Max extensions tetap `1`, tidak ada yang tersimpan
15. Maya Pengelola mengirim Save pada Company default dengan Max extensions `-1`
16. Verifikasi Save ditolak dan Max extensions tetap `1`, tidak ada yang tersimpan

### Max assets per borrower (concurrent) kosong atau di bawah minimum ditolak server
17. Maya Pengelola mengirim Save pada Company default dengan Max assets per borrower (concurrent) dikosongkan
18. Verifikasi Save ditolak dan Max assets per borrower (concurrent) tetap `3`, tidak ada yang tersimpan
19. Maya Pengelola mengirim Save pada Company default dengan Max assets per borrower (concurrent) `0`
20. Verifikasi Save ditolak dan Max assets per borrower (concurrent) tetap `3`, tidak ada yang tersimpan

### Max assets per assignee (concurrent) kosong atau di bawah minimum ditolak server
21. Maya Pengelola mengirim Save pada Company default dengan Max assets per assignee (concurrent) dikosongkan
22. Verifikasi Save ditolak dan Max assets per assignee (concurrent) tetap `0`, tidak ada yang tersimpan
23. Maya Pengelola mengirim Save pada Company default dengan Max assets per assignee (concurrent) `-1`
24. Verifikasi Save ditolak dan Max assets per assignee (concurrent) tetap `0`, tidak ada yang tersimpan

### In-transit overdue after kosong atau di bawah minimum ditolak server
25. Maya Pengelola mengirim Save pada Company default dengan In-transit overdue after dikosongkan
26. Verifikasi Save ditolak dan In-transit overdue after tetap `7`, tidak ada yang tersimpan
27. Maya Pengelola mengirim Save pada Company default dengan In-transit overdue after `0`
28. Verifikasi Save ditolak dan In-transit overdue after tetap `7`, tidak ada yang tersimpan

### Min asset age warning kosong atau di bawah minimum ditolak server
29. Maya Pengelola mengirim Save pada Company default dengan Min asset age warning dikosongkan
30. Verifikasi Save ditolak dan Min asset age warning tetap `12`, tidak ada yang tersimpan
31. Maya Pengelola mengirim Save pada Company default dengan Min asset age warning `0`
32. Verifikasi Save ditolak dan Min asset age warning tetap `12`, tidak ada yang tersimpan

### Max deviation from book value kosong atau di bawah minimum ditolak server
33. Maya Pengelola mengirim Save pada Company default dengan Max deviation from book value dikosongkan
34. Verifikasi Save ditolak dan Max deviation from book value tetap `30`, tidak ada yang tersimpan
35. Maya Pengelola mengirim Save pada Company default dengan Max deviation from book value `0`
36. Verifikasi Save ditolak dan Max deviation from book value tetap `30`, tidak ada yang tersimpan

### Auto-approve when duration ≤ kosong atau di bawah minimum ditolak server
37. Maya Pengelola mengirim Save pada Company default dengan Auto-approve when duration ≤ dikosongkan
38. Verifikasi Save ditolak dan Auto-approve when duration ≤ tetap `3`, tidak ada yang tersimpan
39. Maya Pengelola mengirim Save pada Company default dengan Auto-approve when duration ≤ `0`
40. Verifikasi Save ditolak dan Auto-approve when duration ≤ tetap `3`, tidak ada yang tersimpan

### Transaction timeout kosong atau di bawah minimum ditolak server
41. Maya Pengelola mengirim Save pada Company default dengan Transaction timeout dikosongkan
42. Verifikasi Save ditolak dan Transaction timeout tetap `7`, tidak ada yang tersimpan
43. Maya Pengelola mengirim Save pada Company default dengan Transaction timeout `0`
44. Verifikasi Save ditolak dan Transaction timeout tetap `7`, tidak ada yang tersimpan

### Long missing after kosong atau di bawah minimum ditolak server
45. Maya Pengelola mengirim Save pada Company default dengan Long missing after dikosongkan
46. Verifikasi Save ditolak dan Long missing after tetap `30`, tidak ada yang tersimpan
47. Maya Pengelola mengirim Save pada Company default dengan Long missing after `-1`
48. Verifikasi Save ditolak dan Long missing after tetap `30`, tidak ada yang tersimpan

### Allowed disposal types tanpa satu jenis pun ditolak server
49. Maya Pengelola mengirim Save pada Company default dengan Allowed disposal types dikosongkan
50. Verifikasi Save ditolak dan Allowed disposal types tetap berisi `Sell`, `Scrap`, `Lost`, `Donate`, `Trade-in`, dan `Write-off`, tidak ada yang tersimpan

### Transaction timeout hanya menerima bilangan bulat minimal 1
51. Maya Pengelola mengirim Save pada Company default dengan Transaction timeout `1.5`
52. Verifikasi Save ditolak karena nilai bukan bilangan bulat dan Transaction timeout tetap `7`
53. Maya Pengelola mengirim Save pada Company default dengan Transaction timeout `0`
54. Verifikasi Save ditolak karena nilai kurang dari 1 dan Transaction timeout tetap `7`
55. Maya Pengelola mengirim satu Save berisi Max duration Company default `30` dan Transaction timeout `0`
56. Verifikasi Save tidak diproses seluruhnya: Max duration Company default tetap `21` dan Transaction timeout tetap `7`

### Save tanpa selisih diproses sebagai sukses tanpa perubahan dan idempotent
57. Maya Pengelola mengirim Save pada Company default dengan Max extensions `2`
58. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
59. Maya Pengelola mengirim ulang Save yang identik dengan Max extensions `2`
60. Verifikasi Save kedua diproses sebagai sukses tanpa perubahan, dan Max extensions tetap `2`
61. Verifikasi Changelog dan Activity Log tidak bertambah entri, dan Save yang sama dapat dikirim ulang tanpa efek ganda

### Save yang tiba di server dibandingkan dengan nilai tersimpan saat diterima
62. Budi Penyunting menyimpan Max assets per borrower (concurrent) Company default `5`
63. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
64. Maya Pengelola mengirim Save yang berisi Max assets per borrower (concurrent) `5`, nilai yang sama dengan nilai tersimpan saat Save diterima
65. Verifikasi Save itu diperlakukan sebagai tanpa selisih karena server membandingkan setiap field dengan nilai tersimpan saat Save diterima
66. Verifikasi Changelog dan Activity Log tidak bertambah entri

### Payload hanya memuat field yang berubah dan field lain tidak ditulis
67. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log
68. Maya Pengelola mengirim Save pada Company default yang hanya memuat Max extensions `3`
69. Verifikasi Max extensions tersimpan `3` dan Max duration Company default tetap `21`
70. Verifikasi Changelog dan Activity Log masing-masing bertambah tepat satu entri, untuk Max extensions, karena field yang tidak disentuh draft tidak ditulis

### Perpindahan dari Inherit ke nilai sendiri dengan angka yang sama dihitung sebagai perubahan
71. Maya Pengelola mencatat jumlah entri Changelog
72. Maya Pengelola mengirim Save pada Category `Peralatan Kantor {runId}` dengan Max extensions nilai sendiri `3`, sama dengan nilai Company default `3` yang saat itu berlaku dan sebelumnya diwarisi
73. Verifikasi Save diproses sebagai perubahan nyata dan Max extensions Category `Peralatan Kantor {runId}` tersimpan sebagai nilai sendiri `3`
74. Verifikasi Changelog bertambah tepat satu entri dengan Old Value `Inherit`

### Field yang disembunyikan dilewati validasi dan nilai tersimpannya dipertahankan
75. Maya Pengelola mengirim Save pada Company default dengan Require approval `OFF` pada transaksi peminjaman dan Auto-approve when duration ≤ `0`, field yang tersembunyi bila Require approval `OFF`
76. Verifikasi Save diterima karena validasi minimum hanya berlaku untuk field yang tampil dan aktif
77. Verifikasi nilai tersimpan Auto-approve when duration ≤ tetap `3`, dipertahankan walau field itu tersembunyi

### Setting Category excess dapat disimpan seperti biasa
78. Maya Pengelola mengirim Save pada Category `Aset Lama {runId}` dengan Max extensions nilai sendiri `4`
79. Verifikasi Save diterima dan Max extensions Category `Aset Lama {runId}` tersimpan `4`, karena Save tidak memeriksa status excess
