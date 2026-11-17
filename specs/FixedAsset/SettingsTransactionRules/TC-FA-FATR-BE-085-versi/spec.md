---
id: TC-FA-FATR-BE-085-versi
title: "Versi setting"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r35", "§Aturan Logika Modul#r36", "§Aturan Logika Modul#r37", "§Aturan Logika Modul#r38", "§4.1#r375", "§9.2#b23", "§9.2#b56", "§9.4.2#r5", "§9.4.4#r34", "§9.6#r8", "§9.7#r3", "§9.7#r20", "§9.7#r21", "§4.4#r7", "§9.2#b191"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r35": [3, 54, 55]
  "§Aturan Logika Modul#r36": [13, 16]
  "§Aturan Logika Modul#r37": [19, 23, 39, 40]
  "§Aturan Logika Modul#r38": [22, 23, 27]
  "§4.1#r375": [26, 27, 45, 46, 50, 51]
  "§9.2#b23": 6
  "§9.2#b56": [9, 10]
  "§9.4.2#r5": 10
  "§9.4.4#r34": [33, 34, 46, 51]
  "§9.6#r8": 10
  "§9.7#r3": [13, 16]
  "§9.7#r20": [19, 23, 39, 40]
  "§9.7#r21": [27, 34]
  "§4.4#r7": 6
  "§9.2#b191": 50
---
# Versi setting

## Prerequisites
- Aktor: Maya Pengelola (DU-085-1), Total Control dengan cakupan seluruh Group; Sari Penata (DU-085-2), Group Role Manage asset & TAG (Read, Update) pada Group `Tim Survei {runId}`; dan pemanggil terotorisasi Rudi Integrasi (DU-085-3).
- Data:
  - DU-085-1: User, pengelola yang menyimpan setting dan mengelola override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-085-2: User, pengelola Group yang hanya berhak pada satu Group: Name `Sari Penata {runId}`; Group Role `Manage asset & TAG (Read, Update)`; Cakupan `Group Tim Survei {runId} beserta turunannya`.
  - DU-085-3: User, pemanggil terotorisasi yang mengajukan transaksi: Name `Rudi Integrasi {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-085-4: Group, Group tempat Sari Penata berhak: Name `Tim Survei {runId}`.
  - DU-085-5: Group, Group di luar cakupan Sari Penata: Name `Tim Lapangan {runId}`.
  - DU-085-6: Group, Group target guard Allowed assignee: Name `Tim Pemetaan {runId}`.
  - DU-085-7: Category, Category leaf milik spec ini yang mewarisi seluruh nilai: Name `Perangkat Survei {runId}`.
  - DU-085-8: Asset, aset untuk pengajuan transaksi baru: Name `Drone Survei {runId}`; Asset Name `Drone Ukur {runId}`; Category `Perangkat Survei {runId}`; Group `Tim Survei {runId}`.
  - DU-085-9: Asset, aset target override Asset pada guard Allowed assignee: Name `Drone Pemetaan {runId}`; Asset Name `Drone Ukur {runId}`; Category `Perangkat Survei {runId}`; Group `Tim Pemetaan {runId}`.
  - DU-085-10: Entitas, entitas khusus spec ini, tidak dipakai spec lain: Name `Entitas Versi {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Versi {runId}` (DU-085-10) yang tidak dipakai spec lain, karena yang diasersi adalah versi setting yang naik pada setting Company default dan setting Category entitas; semua data di atas berada di entitas itu.
  - Level Feature Suite Borrowing dan Assignment entitas bernilai `Full`.
  - Company default pada transaksi Borrow bernilai default: Max duration `14`, Max extensions `1`, dan Max assets per borrower (concurrent) `3`.
  - Seluruh field Category `Perangkat Survei {runId}` bernilai Inherit dan belum ada override pada Category itu.
  - Allowed assignee: Employee `ON` dan Allowed assignee: Division `ON` pada Company default.
  - Allow Assign bernilai `Allow` pada Company default dan Inherit pada Category `Perangkat Survei {runId}`; spec ini tidak mengubahnya, sehingga penolakan guard Allowed assignee berlaku untuk aset yang nilai efektif Allow Assign-nya bukan Deny.
  - Versi setting dibaca sebagai selisih terhadap versi yang dicatat sebelum aksi; nilai awal versi tidak diasersi.

## Test Steps

### Save Changes berselisih menaikkan versi setting satu kali
1. Maya Pengelola mencatat versi setting
2. Maya Pengelola menyimpan Category `Perangkat Survei {runId}` dengan Max extensions nilai sendiri `2` lewat Save Changes
3. Verifikasi versi setting naik tepat satu dari versi yang dicatat

### Transaksi baru memakai versi setting sesudah Save
4. Maya Pengelola mencatat versi setting
5. Rudi Integrasi mengajukan transaksi peminjaman baru atas aset `Drone Survei {runId}`
6. Verifikasi versi setting yang tercatat pada transaksi baru itu sama dengan versi yang dicatat, yaitu versi sesudah Save

### Save tanpa selisih tidak menaikkan versi setting
7. Maya Pengelola mencatat versi setting
8. Maya Pengelola mengirim ulang Save Category `Perangkat Survei {runId}` dengan Max extensions `2`, nilai yang sudah tersimpan
9. Verifikasi Save diproses sebagai sukses tanpa perubahan
10. Verifikasi versi setting tidak naik dari versi yang dicatat

### Add override menaikkan versi setting satu kali per aksi, berapa pun jumlah targetnya
11. Maya Pengelola mencatat versi setting
12. Maya Pengelola menambahkan override Group `Tim Survei {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman dengan Max duration `5`
13. Verifikasi versi setting naik tepat satu dari versi yang dicatat
14. Maya Pengelola mencatat versi setting
15. Maya Pengelola menambahkan dalam satu submit override Group `Tim Lapangan {runId}` dan `Tim Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman dengan Max duration `6`
16. Verifikasi kedua override terbuat dan versi setting naik tepat satu dari versi yang dicatat, bukan dua

### Delete override baris menaikkan versi setting satu kali
17. Maya Pengelola mencatat versi setting
18. Maya Pengelola menghapus override Group `Tim Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman
19. Verifikasi override itu terhapus dan versi setting naik tepat satu dari versi yang dicatat

### Bulk Delete yang melewati sebagian baris tetap menaikkan versi satu kali
20. Maya Pengelola mencatat versi setting
21. Sari Penata menghapus bulk override Group `Tim Survei {runId}` dan override Group `Tim Lapangan {runId}`, padahal ia hanya berhak pada Group `Tim Survei {runId}`
22. Verifikasi override Group `Tim Survei {runId}` terhapus dan override Group `Tim Lapangan {runId}` dilewati karena di luar cakupan Sari Penata
23. Verifikasi versi setting naik tepat satu dari versi yang dicatat, karena sedikitnya satu override terhapus dan baris yang dilewati tidak menaikkan versi

### Bulk Delete yang tidak menghapus apa pun tidak menaikkan versi
24. Maya Pengelola mencatat versi setting
25. Sari Penata menghapus bulk hanya override Group `Tim Lapangan {runId}`, yang di luar cakupannya
26. Verifikasi override Group `Tim Lapangan {runId}` masih ada karena seluruh baris dilewati
27. Verifikasi versi setting tidak naik dari versi yang dicatat

### Delete yang ditolak guard Allowed assignee tidak menaikkan versi
28. Maya Pengelola menyimpan Category `Perangkat Survei {runId}` dengan Allowed assignee: Division nilai sendiri `OFF` lewat Save Changes
29. Maya Pengelola menambahkan override Group `Tim Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan dengan Allowed assignee: Division `ON`
30. Maya Pengelola menambahkan override aset `Drone Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF`
31. Maya Pengelola mencatat versi setting
32. Maya Pengelola menghapus override Group `Tim Pemetaan {runId}`, yang akan membuat kombinasi efektif Allowed assignee: Employee dan Allowed assignee: Division override aset `Drone Pemetaan {runId}` sama-sama `OFF`
33. Verifikasi Delete ditolak server dan override Group `Tim Pemetaan {runId}` masih ada
34. Verifikasi versi setting tidak naik dari versi yang dicatat

### Bulk Delete yang menghapus dua override sekaligus menaikkan versi satu kali
35. Maya Pengelola menambahkan override Group `Tim Survei {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman dengan Max duration `7`
36. Maya Pengelola menambahkan override Group `Tim Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman dengan Max duration `4`
37. Maya Pengelola mencatat versi setting
38. Maya Pengelola menghapus bulk override Group `Tim Survei {runId}` dan override Group `Tim Pemetaan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi peminjaman
39. Verifikasi kedua override terhapus
40. Verifikasi versi setting naik tepat satu dari versi yang dicatat, bukan dua, karena versi naik satu kali per aksi

### Bulk Delete yang seluruh barisnya ditolak guard tidak menaikkan versi
41. Maya Pengelola menambahkan override Group `Tim Survei {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan dengan Allowed assignee: Division `ON`
42. Maya Pengelola menambahkan override aset `Drone Survei {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan dengan Allowed assignee: Employee `OFF`
43. Maya Pengelola mencatat versi setting
44. Maya Pengelola menghapus bulk override Group `Tim Pemetaan {runId}` dan override Group `Tim Survei {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan
45. Verifikasi kedua override Group masih ada karena setiap penghapusan akan membuat kombinasi efektif Allowed assignee: Employee dan Allowed assignee: Division sama-sama `OFF` pada override aset `Drone Pemetaan {runId}` dan `Drone Survei {runId}`
46. Verifikasi versi setting tidak naik dari versi yang dicatat

### Bulk Delete campuran baris ditolak guard dan di luar cakupan tidak menaikkan versi
47. Maya Pengelola menambahkan override Group `Tim Lapangan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan dengan Max assets per assignee (concurrent) `2`
48. Maya Pengelola mencatat versi setting
49. Sari Penata menghapus bulk override Group `Tim Survei {runId}` dan override Group `Tim Lapangan {runId}` pada Category `Perangkat Survei {runId}` untuk transaksi penugasan, padahal ia hanya berhak pada Group `Tim Survei {runId}`
50. Verifikasi kedua override masih ada: override Group `Tim Survei {runId}` ditolak guard dan override Group `Tim Lapangan {runId}` dilewati karena di luar cakupan Sari Penata
51. Verifikasi versi setting tidak naik dari versi yang dicatat

### Save Changes yang mengubah beberapa field sekaligus menaikkan versi satu kali
52. Maya Pengelola mencatat versi setting
53. Maya Pengelola menyimpan Category `Perangkat Survei {runId}` pada transaksi peminjaman dengan Max extensions nilai sendiri `3`, Max duration nilai sendiri `9`, dan Max assets per borrower (concurrent) nilai sendiri `4` dalam satu Save Changes
54. Verifikasi ketiga perubahan tersimpan: Max extensions `3`, Max duration `9`, dan Max assets per borrower (concurrent) `4` pada Category `Perangkat Survei {runId}`
55. Verifikasi versi setting naik tepat satu dari versi yang dicatat, bukan tiga, karena versi naik satu kali per Save Changes berselisih
