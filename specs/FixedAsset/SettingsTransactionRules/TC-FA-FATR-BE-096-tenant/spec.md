---
id: TC-FA-FATR-BE-096-tenant
title: "Write-lock entitas Suspended atau Expired"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b49", "§9.2#b50", "§9.2#b51", "§9.2#b62", "§9.2#b63", "§9.2#b168", "§9.2#b169", "§9.2#b300", "§9.2#b375", "§9.4.2#r24", "§9.4.2#r31", "§9.4.2#r47", "§9.4.2#r52", "§9.4.2#r85", "§9.4.2#r87", "§9.4.3#b1", "§9.4.4#r16", "§9.4.4#r28", "§9.4.4#r39", "§9.4.4#r43", "§9.11#p1", EB-AKS-7]
smoke: []
dependsOn: []
trace:
  "§9.2#b49": [10, 35]
  "§9.2#b50": [21, 24, 45, 48]
  "§9.2#b51": [31, 53]
  "§9.2#b62": [10, 35]
  "§9.2#b63": [26, 50]
  "§9.2#b168": [14, 38]
  "§9.2#b169": [17, 40]
  "§9.2#b300": [31, 53]
  "§9.2#b375": [21, 24, 45]
  "§9.4.2#r24": [14, 38]
  "§9.4.2#r31": [17, 40]
  "§9.4.2#r47": [31, 53]
  "§9.4.2#r52": [21, 24, 45, 48]
  "§9.4.2#r85": [10, 35]
  "§9.4.2#r87": [26, 48]
  "§9.4.3#b1": [11, 14, 17, 36, 38, 40]
  "§9.4.4#r16": [12, 42]
  "§9.4.4#r28": [15, 18, 41]
  "§9.4.4#r39": [31, 53]
  "§9.4.4#r43": [22, 46]
  "§9.11#p1": [27, 28, 29]
  EB-AKS-7: [2, 4, 6, 10, 11, 35, 36]
---
# Write-lock entitas Suspended atau Expired

## Prerequisites
- Aktor: Maya Pengelola (DU-096-2), Total Control dengan cakupan seluruh Group, dan Operator Status (DU-096-3), operator Admin Console di luar entitas.
- Data:
  - DU-096-1: Entitas, entitas khusus spec ini, awalnya Active: Name `Entitas Status {runId}`; Status `Active`.
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
  - DU-096-22: Entitas, Client kedua yang tidak diubah, pembanding isolasi: Name `Entitas Lain {runId}`; Status `Active`.
  - DU-096-23: Category, Category leaf pada entitas kedua dengan nama yang sama dengan Category entitas ini: Name `Perangkat Status {runId}`; Entitas `Entitas Lain {runId}`.
  - DU-096-24: Group, Group target override pada entitas kedua: Name `Tim Entitas Lain {runId}`; Entitas `Entitas Lain {runId}`.
  - DU-096-25: Override, override bernama pada entitas kedua: Scope `Group`; Target `Tim Entitas Lain {runId}`; Category `Perangkat Status {runId}`; Entitas `Entitas Lain {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `8`.
  - DU-096-12 sampai DU-096-17 adalah nilai input Save dan Add override di langkah masing-masing, bukan record yang sudah ada.
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

### Entitas Suspended: Save ditolak server
7. Operator Status menetapkan entitas `Entitas Status {runId}` menjadi Suspended
8. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
9. Maya Pengelola mengirim langsung ke server Save Category `Perangkat Status {runId}` dengan Max extensions nilai sendiri `3`
10. Verifikasi Save ditolak server sebagai larangan akses dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
11. Verifikasi Max extensions Category `Perangkat Status {runId}` tetap `2`, karena server tidak menerima Save saat entitas Suspended
12. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah Save yang ditolak saat Suspended

### Entitas Suspended: Add override dan Delete override ditolak server
13. Maya Pengelola mengirim langsung ke server Add override Group `Tim Status Ditolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman dengan Max duration `6`
14. Verifikasi Add override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
15. Verifikasi tidak ada override untuk Group `Tim Status Ditolak {runId}` terbuat dan tidak ada entri log baru
16. Maya Pengelola mengirim langsung ke server Delete override Group `Tim Hapus Tolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman
17. Verifikasi Delete override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
18. Verifikasi override Group `Tim Hapus Tolak {runId}` masih ada dan tidak ada entri log baru

### Entitas Suspended: aksi baca tidak diblokir
19. Maya Pengelola mencatat jumlah entri Activity Log
20. Maya Pengelola menjalankan Export rules pada Category `Perangkat Status {runId}`
21. Verifikasi berkas Export rules terunduh
22. Verifikasi Activity Log bertambah tepat satu entri Export rules dari Maya Pengelola dibanding yang dicatat sebelum Export, walau entitas Suspended
23. Maya Pengelola membuka Changelog
24. Verifikasi Changelog terbaca dan memuat entri Save Max extensions `2` dari Maya Pengelola
25. Maya Pengelola membuka daftar override Category `Perangkat Status {runId}`
26. Verifikasi daftar override terbaca dan memuat override Group `Tim Hapus Tolak {runId}`, karena aksi baca tidak diblokir
27. Verifikasi daftar override Category `Perangkat Status {runId}` tidak memuat override Group `Tim Entitas Lain {runId}` milik entitas `Entitas Lain {runId}`, walau Category bernama sama ada di kedua entitas
28. Verifikasi berkas Export rules yang terunduh memuat override Group `Tim Hapus Tolak {runId}` milik entitas ini, sebagai pembanding bahwa berkas terbaca isinya
29. Verifikasi berkas Export rules yang terunduh tidak memuat override Group `Tim Entitas Lain {runId}` milik entitas `Entitas Lain {runId}`

### Entitas Suspended: job Transaction timeout tanpa aktor tetap berjalan
30. Operator Status menjalankan job Transaction timeout
31. Verifikasi transaksi peminjaman atas aset `Aset Timeout Satu {runId}`, yang menunggu approval melewati Transaction timeout, berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` dan tercatat di log transaksi dengan Modified By `System`, serta aset kembali ke Draft baru tanpa nomor BRW

### Entitas Expired: Save, Add override, dan Delete override ditolak server
32. Operator Status menetapkan entitas `Entitas Status {runId}` menjadi Expired
33. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
34. Maya Pengelola mengirim langsung ke server Save Category `Perangkat Status {runId}` dengan Max extensions nilai sendiri `4`
35. Verifikasi Save ditolak server sebagai larangan akses dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, pesan yang sama dengan entitas Suspended
36. Verifikasi Max extensions Category `Perangkat Status {runId}` tetap `2`
37. Maya Pengelola mengirim langsung ke server Add override Group `Tim Status Ditolak Dua {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman dengan Max duration `7`
38. Verifikasi Add override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
39. Maya Pengelola mengirim langsung ke server Delete override Group `Tim Hapus Tolak {runId}` pada Category `Perangkat Status {runId}` untuk transaksi peminjaman
40. Verifikasi Delete override ditolak server dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
41. Verifikasi override Group `Tim Hapus Tolak {runId}` masih ada dan tidak ada override untuk Group `Tim Status Ditolak Dua {runId}` terbuat
42. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah ketiga aksi tulis yang ditolak saat Expired

### Entitas Expired: aksi baca tidak diblokir dan job tanpa aktor tetap berjalan
43. Maya Pengelola mencatat jumlah entri Activity Log
44. Maya Pengelola menjalankan Export rules pada Category `Perangkat Status {runId}`
45. Verifikasi berkas Export rules terunduh
46. Verifikasi Activity Log bertambah tepat satu entri Export rules dari Maya Pengelola dibanding yang dicatat sebelum Export, walau entitas Expired
47. Maya Pengelola membuka Changelog
48. Verifikasi Changelog terbaca
49. Maya Pengelola membuka daftar override Category `Perangkat Status {runId}`
50. Verifikasi daftar override terbaca, karena aksi baca tidak diblokir
51. Waktu berlalu sampai transaksi peminjaman atas aset `Aset Timeout Dua {runId}` genap 8 hari sejak diajukan, melewati Transaction timeout `7` hari
52. Operator Status menjalankan job Transaction timeout
53. Verifikasi transaksi peminjaman atas aset `Aset Timeout Dua {runId}`, yang menunggu approval melewati Transaction timeout, berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` dan tercatat di log transaksi dengan Modified By `System`, serta aset kembali ke Draft baru tanpa nomor BRW
