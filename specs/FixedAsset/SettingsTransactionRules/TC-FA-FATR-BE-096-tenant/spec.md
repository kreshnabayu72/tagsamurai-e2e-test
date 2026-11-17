---
id: TC-FA-FATR-BE-096-tenant
title: "Write-lock entitas Suspended atau Expired"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b49", "§9.2#b50", "§9.2#b51", "§9.2#b62", "§9.2#b63", "§9.2#b168", "§9.2#b169", "§9.2#b300", "§9.2#b375", "§9.4.2#r24", "§9.4.2#r31", "§9.4.2#r47", "§9.4.2#r52", "§9.4.2#r93", "§9.4.2#r95", "§9.4.3#b1", "§9.4.4#r16", "§9.4.4#r28", "§9.4.4#r39", "§9.4.4#r43", "§9.11#p1", EB-AKS-7]
smoke: []
dependsOn: []
trace:
  "§9.2#b49": [31, 56]
  "§9.2#b50": [42, 45, 66, 69]
  "§9.2#b51": [52, 74]
  "§9.2#b62": [31, 56]
  "§9.2#b63": [47, 71]
  "§9.2#b168": [35, 59]
  "§9.2#b169": [38, 61]
  "§9.2#b300": [52, 74]
  "§9.2#b375": [42, 45, 66]
  "§9.4.2#r24": [35, 59]
  "§9.4.2#r31": [38, 61]
  "§9.4.2#r47": [52, 74]
  "§9.4.2#r52": [42, 45, 66, 69]
  "§9.4.2#r93": [31, 56]
  "§9.4.2#r95": [47, 69]
  "§9.4.3#b1": [32, 35, 38, 57, 59, 61]
  "§9.4.4#r16": [33, 63]
  "§9.4.4#r28": [36, 39, 62]
  "§9.4.4#r39": [52, 74]
  "§9.4.4#r43": [43, 67]
  "§9.11#p1": [8, 9, 11, 13, 15, 17, 19, 21, 23, 25, 26, 27, 48, 49, 50]
  EB-AKS-7: [2, 4, 6, 31, 32, 56, 57]
---
# Write-lock entitas Suspended atau Expired

## Prerequisites
- Aktor: Maya Pengelola (DU-096-2), Total Control dengan cakupan seluruh Group; Operator Status (DU-096-3), operator Admin Console di luar entitas; Dewi Distributor (DU-096-28), pengguna entitas Distributor dengan cakupan seluruh Group di entitas Distributor sendiri; dan Pandu Partner (DU-096-29), pengguna entitas Partner dengan cakupan seluruh Group di entitas Partner sendiri.
- Data:
  - DU-096-1: Entitas, entitas khusus spec ini, awalnya Active: Name `Entitas Status {runId}`; Status `Active`; Dipegang oleh `Partner Jaringan {runId}`.
  - DU-096-2: User, pengelola Total Control yang menyimpan dan mengelola override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-096-3: User, operator Admin Console yang mengubah status entitas dan menjalankan job: Name `Operator Status {runId}`; Peran `operator Admin Console di luar entitas`.
  - DU-096-4: Category, Category leaf yang mewarisi seluruh nilai: Name `Perangkat Status {runId}`.
  - DU-096-5: Group, Group target Add override saat Active: Name `Tim Status Baru {runId}`.
  - DU-096-6: Group, Group target Add override yang ditolak saat Suspended: Name `Tim Status Ditolak {runId}`.
  - DU-096-7: Group, Group target Add override yang ditolak saat Expired: Name `Tim Status Ditolak Dua {runId}`.
  - DU-096-8: Group, Group target override yang dihapus saat Active: Name `Tim Hapus Aktif {runId}`.
  - DU-096-9: Group, Group target override yang Delete-nya ditolak: Name `Tim Hapus Tolak {runId}`.
  - DU-096-10: Override, override yang dihapus saat entitas Active: Scope `Group`; Target `Tim Hapus Aktif {runId}`; Category `Perangkat Status {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-096-11: Override, override yang Delete-nya ditolak saat Suspended dan Expired: Scope `Group`; Target `Tim Hapus Tolak {runId}`; Category `Perangkat Status {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-096-18: Asset, aset pada transaksi peminjaman yang menunggu approval saat Suspended: Name `Aset Timeout Satu {runId}`; Asset Name `Aset Timeout {runId}`; Category `Perangkat Status {runId}`; Group `Tim Status Baru {runId}`.
  - DU-096-19: Asset, aset pada transaksi peminjaman yang menunggu approval saat Expired: Name `Aset Timeout Dua {runId}`; Asset Name `Aset Timeout {runId}`; Category `Perangkat Status {runId}`; Group `Tim Status Baru {runId}`.
  - DU-096-20: Transaksi, transaksi peminjaman yang menunggu approval melewati Transaction timeout, untuk job saat Suspended: Jenis `peminjaman`; Status `Waiting for Approval`; Aset `Aset Timeout Satu {runId}`; Diajukan `H-8`.
  - DU-096-21: Transaksi, transaksi peminjaman yang menunggu approval dan baru melewati Transaction timeout sesudah entitas Expired, untuk job saat Expired: Jenis `peminjaman`; Status `Waiting for Approval`; Aset `Aset Timeout Dua {runId}`; Diajukan `H-6`, sehingga 6 hari sejak diajukan pada awal spec.
  - DU-096-22: Entitas, Client kedua yang tidak diubah, pembanding isolasi: Name `Entitas Lain {runId}`; Status `Active`; Dipegang oleh `Partner Jaringan {runId}`.
  - DU-096-23: Category, Category leaf pada entitas kedua dengan nama yang sama dengan Category entitas ini: Name `Perangkat Status {runId}`; Entitas `Entitas Lain {runId}`.
  - DU-096-24: Group, Group target override pada entitas kedua: Name `Tim Entitas Lain {runId}`; Entitas `Entitas Lain {runId}`.
  - DU-096-25: Override, override bernama pada entitas kedua: Scope `Group`; Target `Tim Entitas Lain {runId}`; Category `Perangkat Status {runId}`; Entitas `Entitas Lain {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `8`.
  - DU-096-26: Entitas, Distributor pemegang jaringan: Name `Distributor Jaringan {runId}`; Jenis `Distributor`; Status `Active`.
  - DU-096-27: Entitas, Partner di bawah Distributor Jaringan yang memegang langsung `Entitas Status {runId}` dan `Entitas Lain {runId}`: Name `Partner Jaringan {runId}`; Jenis `Partner`; Distributor `Distributor Jaringan {runId}`; Status `Active`.
  - DU-096-28: User, pengguna entitas Distributor: Name `Dewi Distributor {runId}`; Peran `pengguna entitas Distributor Jaringan {runId}`; Cakupan `seluruh Group di entitas Distributor sendiri`.
  - DU-096-29: User, pengguna entitas Partner: Name `Pandu Partner {runId}`; Peran `pengguna entitas Partner Jaringan {runId}`; Cakupan `seluruh Group di entitas Partner sendiri`.
  - DU-096-30: Group, Group target Add override aktor jaringan yang ditolak: Name `Tim Jaringan Tolak {runId}`; Entitas `Entitas Status {runId}`.
  - DU-096-12 sampai DU-096-17 dan DU-096-31 sampai DU-096-33 adalah nilai input Save dan Add override di langkah masing-masing, bukan record yang sudah ada.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Status {runId}` (DU-096-1) yang tidak dipakai spec lain, karena status entitas diubah menjadi Suspended lalu Expired.
  - Seluruh field Category `Perangkat Status {runId}` bernilai Inherit, dan Transaction timeout Company default bernilai default `7` hari.
  - Level Feature Suite Borrowing entitas `Entitas Status {runId}` bernilai `Full`.
  - Job Transaction timeout tidak berjalan sendiri selama spec ini; Operator Status menjalankannya pada langkah yang menyebutnya.
  - Jumlah entri Changelog dan Activity Log serta versi setting dibaca sebagai selisih terhadap nilai yang dicatat sebelum aksi.
  - Entitas `Entitas Lain {runId}` (DU-096-22) adalah Client kedua yang tetap Active selama spec ini dan tidak diubah; Category `Perangkat Status {runId}` ada di kedua entitas, dan hanya override milik entitas ini yang boleh muncul pada daftar dan berkas Export rules entitas ini.

## Test Steps

### Entitas Active: Save, Add override, dan Delete override diterima
1. Maya Pengelola menyimpan Category `Perangkat Status {runId}` dengan Max extensions nilai sendiri `2`
2. Verifikasi Save diterima dan Max extensions Category `Perangkat Status {runId}` bernilai `2`
3. Maya Pengelola menambahkan override Group `Tim Status Baru {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman dengan Max duration `5`
4. Verifikasi override Group `Tim Status Baru {runId}` terbuat
5. Maya Pengelola menghapus override Group `Tim Hapus Aktif {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman
6. Verifikasi override Group `Tim Hapus Aktif {runId}` terhapus

### Entitas Active: aksi tulis ke data Client lain ditolak
7. Maya Pengelola mengirim langsung ke server Save Category `Perangkat Status {runId}` milik entitas `Entitas Lain {runId}` dengan Max extensions nilai sendiri `6`
8. Verifikasi Save ditolak server karena Category itu milik Client lain, bukan milik Client Maya Pengelola
9. Verifikasi Max extensions Category `Perangkat Status {runId}` pada entitas `Entitas Lain {runId}` tetap Inherit
10. Maya Pengelola mengirim langsung ke server Delete override Group `Tim Entitas Lain {runId}` pada Category `Perangkat Status {runId}` milik entitas `Entitas Lain {runId}` untuk transaksi peminjaman
11. Verifikasi Delete ditolak server karena override itu milik Client lain, dan override Group `Tim Entitas Lain {runId}` pada entitas `Entitas Lain {runId}` masih ada

### Entitas Active: aktor jaringan Distributor dan Partner tidak memperoleh akses baca atau tulis ke setting Client
12. Dewi Distributor membaca daftar override Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}`
13. Verifikasi Dewi Distributor tidak memperoleh override Group `Tim Status Baru {runId}`, walau entitas `Entitas Status {runId}` ada di jaringan Distributor Jaringan, karena halaman tidak memakai jaringan Distributor
14. Dewi Distributor membaca daftar override Category `Perangkat Status {runId}` milik entitas `Entitas Lain {runId}`
15. Verifikasi Dewi Distributor tidak memperoleh override Group `Tim Entitas Lain {runId}`, walau entitas `Entitas Lain {runId}` ada di jaringan yang sama
16. Dewi Distributor membaca nilai Max extensions Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}`
17. Verifikasi Dewi Distributor tidak memperoleh nilai Max extensions `2` Category itu
18. Dewi Distributor mengirim langsung ke server Save Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}` dengan Max extensions nilai sendiri `5`
19. Verifikasi Save ditolak server karena Category itu milik satu Client, dan jaringan Distributor tidak memberi akses tulis
20. Dewi Distributor mengirim langsung ke server Add override Group `Tim Jaringan Tolak {runId}` pada Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}` untuk transaksi peminjaman dengan Max duration `9`
21. Verifikasi Add override ditolak server karena data milik satu Client, dan jaringan Distributor tidak memberi akses tulis
22. Pandu Partner membaca daftar override Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}`
23. Verifikasi Pandu Partner tidak memperoleh override Group `Tim Status Baru {runId}`, walau entitas `Entitas Status {runId}` dipegang langsung oleh Partner Jaringan, karena halaman tidak memakai jaringan Partner
24. Pandu Partner mengirim langsung ke server Save Category `Perangkat Status {runId}` milik entitas `Entitas Status {runId}` dengan Max extensions nilai sendiri `5`
25. Verifikasi Save ditolak server karena Category itu milik satu Client, dan jaringan Partner tidak memberi akses tulis
26. Verifikasi Max extensions Category `Perangkat Status {runId}` pada entitas `Entitas Status {runId}` tetap `2`, tidak berubah oleh aksi tulis aktor jaringan
27. Verifikasi tidak ada override untuk Group `Tim Jaringan Tolak {runId}` pada entitas `Entitas Status {runId}`

### Entitas Suspended: Save ditolak server
28. Operator Status menetapkan entitas `Entitas Status {runId}` menjadi Suspended
29. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
30. Maya Pengelola mengirim langsung ke server Save Category `Perangkat Status {runId}` dengan Max extensions nilai sendiri `3`
31. Verifikasi Save ditolak server sebagai larangan akses dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
32. Verifikasi Max extensions Category `Perangkat Status {runId}` tetap `2`, karena server tidak menerima Save saat entitas Suspended
33. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah Save yang ditolak saat Suspended

### Entitas Suspended: Add override dan Delete override ditolak server
34. Maya Pengelola mengirim langsung ke server Add override Group `Tim Status Ditolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman dengan Max duration `6`
35. Verifikasi Add override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
36. Verifikasi tidak ada override untuk Group `Tim Status Ditolak {runId}` terbuat dan tidak ada entri log baru
37. Maya Pengelola mengirim langsung ke server Delete override Group `Tim Hapus Tolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman
38. Verifikasi Delete override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
39. Verifikasi override Group `Tim Hapus Tolak {runId}` masih ada dan tidak ada entri log baru

### Entitas Suspended: aksi baca tidak diblokir
40. Maya Pengelola mencatat jumlah entri Activity Log
41. Maya Pengelola menjalankan Export rules pada Category `Perangkat Status {runId}`
42. Verifikasi berkas Export rules terunduh
43. Verifikasi Activity Log bertambah tepat satu entri Export rules dari Maya Pengelola dibanding yang dicatat sebelum Export, walau entitas Suspended
44. Maya Pengelola membuka Changelog
45. Verifikasi Changelog terbaca dan memuat entri Save Max extensions `2` dari Maya Pengelola
46. Maya Pengelola membuka daftar override Category `Perangkat Status {runId}`
47. Verifikasi daftar override terbaca dan memuat override Group `Tim Hapus Tolak {runId}`, karena aksi baca tidak diblokir
48. Verifikasi daftar override Category `Perangkat Status {runId}` tidak memuat override Group `Tim Entitas Lain {runId}` milik entitas `Entitas Lain {runId}`, walau Category bernama sama ada di kedua entitas
49. Verifikasi berkas Export rules yang terunduh memuat override Group `Tim Hapus Tolak {runId}` milik entitas ini, sebagai pembanding bahwa berkas terbaca isinya
50. Verifikasi berkas Export rules yang terunduh tidak memuat override Group `Tim Entitas Lain {runId}` milik entitas `Entitas Lain {runId}`

### Entitas Suspended: job Transaction timeout tanpa aktor tetap berjalan
51. Operator Status menjalankan job Transaction timeout
52. Verifikasi transaksi peminjaman atas aset `Aset Timeout Satu {runId}`, yang menunggu approval melewati Transaction timeout, berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` dan tercatat di log transaksi dengan Modified By `System`, serta aset kembali ke Draft baru tanpa nomor BRW

### Entitas Expired: Save, Add override, dan Delete override ditolak server
53. Operator Status menetapkan entitas `Entitas Status {runId}` menjadi Expired
54. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
55. Maya Pengelola mengirim langsung ke server Save Category `Perangkat Status {runId}` dengan Max extensions nilai sendiri `4`
56. Verifikasi Save ditolak server sebagai larangan akses dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, pesan yang sama dengan entitas Suspended
57. Verifikasi Max extensions Category `Perangkat Status {runId}` tetap `2`
58. Maya Pengelola mengirim langsung ke server Add override Group `Tim Status Ditolak Dua {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman dengan Max duration `7`
59. Verifikasi Add override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
60. Maya Pengelola mengirim langsung ke server Delete override Group `Tim Hapus Tolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman
61. Verifikasi Delete override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
62. Verifikasi override Group `Tim Hapus Tolak {runId}` masih ada dan tidak ada override untuk Group `Tim Status Ditolak Dua {runId}` terbuat
63. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah ketiga aksi tulis yang ditolak saat Expired

### Entitas Expired: aksi baca tidak diblokir dan job tanpa aktor tetap berjalan
64. Maya Pengelola mencatat jumlah entri Activity Log
65. Maya Pengelola menjalankan Export rules pada Category `Perangkat Status {runId}`
66. Verifikasi berkas Export rules terunduh
67. Verifikasi Activity Log bertambah tepat satu entri Export rules dari Maya Pengelola dibanding yang dicatat sebelum Export, walau entitas Expired
68. Maya Pengelola membuka Changelog
69. Verifikasi Changelog terbaca
70. Maya Pengelola membuka daftar override Category `Perangkat Status {runId}`
71. Verifikasi daftar override terbaca, karena aksi baca tidak diblokir
72. Waktu berlalu sampai transaksi peminjaman atas aset `Aset Timeout Dua {runId}` genap 8 hari sejak diajukan, melewati Transaction timeout `7` hari
73. Operator Status menjalankan job Transaction timeout
74. Verifikasi transaksi peminjaman atas aset `Aset Timeout Dua {runId}`, yang menunggu approval melewati Transaction timeout, berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` dan tercatat di log transaksi dengan Modified By `System`, serta aset kembali ke Draft baru tanpa nomor BRW
