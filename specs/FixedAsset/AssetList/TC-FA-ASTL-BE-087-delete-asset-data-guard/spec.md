---
id: TC-FA-ASTL-BE-087-delete-asset-data-guard
title: "Aturan server Delete Asset Data dan blokirnya"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-16k, ASTL-LOGIC-16l, ASTL-LOGIC-17b, ASTL-LOGIC-17e, ASTL-LOGIC-17f, ASTL-LOGIC-17g, ASTL-LOGIC-17h, ASTL-LOGIC-17i, ASTL-LOGIC-17j, ASTL-LOGIC-17p, ASTL-LOGIC-17q, ASTL-LOGIC-17o, ASTL-LOGIC-17u, ASTL-LOGIC-17v, ASTL-LOGIC-17z, V-05, T-06, EC-27, EC-28, EC-31, EC-41, EC-48, F-ASTL-17.k3, "404", "422", "§9.2#p7", "§9.6#r6", EB-ERR-3, EB-EDG-1, EB-EDG-3]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-16k: 2
  ASTL-LOGIC-16l: 17
  ASTL-LOGIC-17b: [10, 12, 39, 50, 53]
  ASTL-LOGIC-17e: 14
  ASTL-LOGIC-17f: 16
  ASTL-LOGIC-17g: 17
  ASTL-LOGIC-17h: 19
  ASTL-LOGIC-17i: [2, 50]
  ASTL-LOGIC-17j: 21
  ASTL-LOGIC-17p: [23, 25, 27, 29]
  ASTL-LOGIC-17q: [31, 33]
  ASTL-LOGIC-17o: 41
  ASTL-LOGIC-17u: 3
  ASTL-LOGIC-17v: 4
  ASTL-LOGIC-17z: [35, 37]
  V-05: [14, 16, 21, 23, 35, 37, 39, 50, 53]
  T-06: 8
  EC-27: [16, 19]
  EC-28: 21
  EC-31: [23, 25, 27, 29]
  EC-41: [43, 44, 45, 46, 47]
  EC-48: [31, 33]
  F-ASTL-17.k3: [2, 16, 19, 21, 23, 25, 27, 29, 31, 33]
  "404": 8
  "422": [14, 16, 21, 41, 50, 53]
  "§9.2#p7": [5, 6]
  "§9.6#r6": [6, 8]
  EB-ERR-3: 8
  EB-EDG-1: 8
  EB-EDG-3: [43, 44, 45, 46]
anchor: []
---

# Aturan server Delete Asset Data dan blokirnya

## Prerequisites
- Aktor: Total Control (Hendra).
- Data:
  - DU-087-1: User, total Control seluruh client: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-087-2: Group, group kantor pusat dan cabang dengan Available license nol: Name `Kantor Pusat {runId}`, Group lain `Cabang Palembang {runId}`, Available license Cabang Palembang `0`.
  - DU-087-3: Asset, aset Unmanaged tanpa jejak finansial beserta berkas: Name `Kamera CCTV - U1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Available`, Jejak finansial `tidak ada`, Berkas 1 `Faktur Kamera U1 {runId}.pdf`, Berkas 2 `Foto Kamera U1 {runId}.jpg`.
  - DU-087-4: Asset, aset Pending Activation dengan kuota Reserved: Name `Kamera CCTV - U2 {runId}`, Lifecycle `Active`, Status `Pending Activation`, Group `Cabang Palembang {runId}`.
  - DU-087-5: Asset, aset Disposed tanpa jejak finansial: Name `Monitor Dell - D1 {runId}`, Lifecycle `Disposed`, Group `Kantor Pusat {runId}`, Jejak finansial `tidak ada`.
  - DU-087-6: Asset, aset managed belum Disposed: Name `Server Rack - M1 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Kantor Pusat {runId}`.
  - DU-087-7: Asset, aset Unmanaged berjejak Posted: Name `Genset Diesel - P1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Jejak finansial `Penyusutan Posted`.
  - DU-087-8: Asset, aset Disposed berjejak Posted: Name `Genset Diesel - P2 {runId}`, Lifecycle `Disposed`, Group `Kantor Pusat {runId}`, Jejak finansial `Jurnal Posted`.
  - DU-087-9: Asset, aset dengan Disposal Executed jurnal belum Posted: Name `Forklift - E1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Disposal `Executed`, Jurnal pelepasan `belum Posted`.
  - DU-087-10: Asset, aset dengan record Missing berstatus Waiting for Confirmation: Name `Forklift - S1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Record Missing `Waiting for Confirmation`.
  - DU-087-11: Asset, aset dengan record Missing berstatus Missing: Name `Forklift - S2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Record Missing `Missing`.
  - DU-087-12: Asset, aset dengan record Missing berstatus Reported Disposal: Name `Forklift - S3 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Record Missing `Reported Disposal`.
  - DU-087-13: Asset, aset dengan record Missing berstatus In Disposal Process: Name `Forklift - S4 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Record Missing `In Disposal Process`.
  - DU-087-14: Asset, aset dengan Disposal Report Reported: Name `Printer Laser - R1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Disposal Report `Reported`, Condition `Reported Disposal`.
  - DU-087-15: Asset, aset dengan baris DSP aktif: Name `Printer Laser - R2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, DSP `aktif`, Condition `In Disposal Process`.
  - DU-087-16: Asset, aset terkunci In Audit: Name `Pompa Air - L1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Activity Lock `In Audit`.
  - DU-087-17: Asset, aset terkunci Under Maintenance: Name `Pompa Air - L2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Activity Lock `Under Maintenance`.
  - DU-087-18: Asset, aset Unmanaged yang sedang dipinjam: Name `Tablet Inventaris - B1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Borrowed`.
  - DU-087-19: Asset, aset Unmanaged memenuhi syarat untuk seleksi campuran: Name `Kursi Kerja - U3 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Available`, Jejak finansial `tidak ada`.
  - DU-087-20: Asset, aset Unmanaged dengan TAG, draft, dan record multi-aset: Name `Laptop Pro 16 - T1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Available`, TAG terpasang `satu TAG`.
  - DU-087-21: Asset, aset lain dalam record multi-aset: Name `Meja Rapat - T2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Available`.
  - DU-087-22: Record, draft transaksi peminjaman yang memuat aset: Name `Draft Pinjam T1 {runId}`, Aset `Laptop Pro 16 - T1 {runId}`.
  - DU-087-23: Record, record multi-aset yang memuat dua aset: Name `Paket Transaksi M {runId}`, Aset `Laptop Pro 16 - T1 {runId}, Meja Rapat - T2 {runId}`.
  - DU-087-24: Record, record multi-aset yang hanya memuat satu aset: Name `Paket Transaksi S {runId}`, Aset `Laptop Pro 16 - T1 {runId}`.
  - DU-087-25: Asset, aset Unmanaged dengan Purchase Pending tanpa jejak finansial yang predikat berjejak Posted-nya tidak terbaca: Name `Pompa Air - K1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Kantor Pusat {runId}`, Custody `Available`, Status Purchase `Pending`, Jejak finansial `tidak ada`, Predikat berjejak Posted `tidak terbaca`.
  - DU-087-26: Asset, aset Disposed tanpa jejak finansial yang predikat Disposal belum Posted-nya tidak terbaca: Name `Monitor Dell - K2 {runId}`, Lifecycle `Disposed`, Group `Kantor Pusat {runId}`, Jejak finansial `tidak ada`, Predikat Disposal belum Posted `tidak terbaca`.

## Test Steps

### Aset Unmanaged tanpa jejak finansial dapat dihapus permanen
1. Hendra menjalankan Delete Asset Data pada aset `Kamera CCTV - U1 {runId}`
2. Verifikasi penghapusan berhasil karena `Kamera CCTV - U1 {runId}` berstatus `Unmanaged`, Custody `Available`, dan tanpa jejak finansial
3. Verifikasi data `Kamera CCTV - U1 {runId}` terhapus permanen dan tidak ada di Recycle Bin, serta tidak berpindah ke Lifecycle `Deleted`
4. Verifikasi berkas terlampir `Faktur Kamera U1 {runId}.pdf` dan `Foto Kamera U1 {runId}.jpg` ikut terhapus permanen dari penyimpanan berkas
5. Verifikasi seluruh Changelog `Kamera CCTV - U1 {runId}` ikut terhapus
6. Verifikasi kejadian penghapusan hanya tercatat sebagai entri User Action di Activity Log pengguna, tanpa entri Changelog Asset
7. Hendra menjalankan Delete Asset Data pada aset `Kamera CCTV - U1 {runId}` yang sudah terhapus
8. Verifikasi permintaan ditolak dengan pesan `This asset is no longer available.` dan tidak ada data yang berubah

### Aset Pending Activation dapat dihapus dan kuota Reserved dilepas
9. Hendra menjalankan Delete Asset Data pada aset `Kamera CCTV - U2 {runId}`
10. Verifikasi penghapusan berhasil dan kuota `Reserved` dilepas sehingga Available group `Cabang Palembang {runId}` menjadi `1`

### Aset Disposed tanpa jejak finansial dapat dihapus
11. Hendra menjalankan Delete Asset Data pada aset `Monitor Dell - D1 {runId}`
12. Verifikasi penghapusan berhasil karena `Monitor Dell - D1 {runId}` ber-Lifecycle `Disposed` dan tanpa jejak finansial

### Aset managed yang belum Disposed tidak dapat dihapus
13. Hendra menjalankan Delete Asset Data pada aset managed `Server Rack - M1 {runId}`
14. Verifikasi permintaan ditolak karena aset managed yang belum `Disposed` tidak dapat dihapus, dan `Server Rack - M1 {runId}` tetap ada

### Aset berjejak Posted tidak dapat dihapus
15. Hendra menjalankan Delete Asset Data pada aset `Genset Diesel - P1 {runId}`
16. Verifikasi permintaan ditolak karena `Genset Diesel - P1 {runId}` berstatus `Unmanaged` dan punya penyusutan Posted, dan aset tetap ada
17. Verifikasi `Genset Diesel - P1 {runId}` tetap `Unmanaged` dengan penyusutan Posted utuh dan tidak terhapus, karena Delete Asset Data bukan jalur keluar aset `Unmanaged` berjejak Posted
18. Hendra menjalankan Delete Asset Data pada aset `Genset Diesel - P2 {runId}` lewat permintaan langsung
19. Verifikasi permintaan ditolak karena `Genset Diesel - P2 {runId}` ber-Lifecycle `Disposed` dan punya jurnal Posted, dan aset tetap ada

### Disposal Executed dengan jurnal pelepasan belum Posted memblokir penghapusan
20. Hendra menjalankan Delete Asset Data pada aset `Forklift - E1 {runId}`
21. Verifikasi permintaan ditolak karena pelepasan aset `Forklift - E1 {runId}` berstatus `Executed` dan jurnal pelepasannya belum Posted, dan aset tetap ada

### Record Missing berjalan memblokir penghapusan
22. Hendra menjalankan Delete Asset Data pada aset `Forklift - S1 {runId}`
23. Verifikasi permintaan ditolak karena record kehilangan berstatus `Waiting for Confirmation`, dan aset tetap ada
24. Hendra menjalankan Delete Asset Data pada aset `Forklift - S2 {runId}`
25. Verifikasi permintaan ditolak karena record kehilangan berstatus `Missing`, dan aset tetap ada
26. Hendra menjalankan Delete Asset Data pada aset `Forklift - S3 {runId}`
27. Verifikasi permintaan ditolak karena record kehilangan berstatus `Reported Disposal`, dan aset tetap ada
28. Hendra menjalankan Delete Asset Data pada aset `Forklift - S4 {runId}`
29. Verifikasi permintaan ditolak karena record kehilangan berstatus `In Disposal Process`, dan aset tetap ada

### Disposal berjalan memblokir penghapusan
30. Hendra menjalankan Delete Asset Data pada aset `Printer Laser - R1 {runId}`
31. Verifikasi permintaan ditolak karena laporan pelepasan `Reported` dengan Condition `Reported Disposal`, dan aset tetap ada
32. Hendra menjalankan Delete Asset Data pada aset `Printer Laser - R2 {runId}`
33. Verifikasi permintaan ditolak karena baris DSP aktif dengan Condition `In Disposal Process`, dan aset tetap ada

### Aset terkunci Activity Lock tidak dapat dihapus
34. Hendra menjalankan Delete Asset Data pada aset `Pompa Air - L1 {runId}` lewat permintaan langsung
35. Verifikasi permintaan ditolak karena Activity Lock `In Audit`, dan aset tetap ada
36. Hendra menjalankan Delete Asset Data pada aset `Pompa Air - L2 {runId}` lewat permintaan langsung
37. Verifikasi permintaan ditolak karena Activity Lock `Under Maintenance`, dan aset tetap ada

### Aset Unmanaged yang Custody-nya bukan Available tidak dapat dihapus
38. Hendra menjalankan Delete Asset Data pada aset `Tablet Inventaris - B1 {runId}`
39. Verifikasi permintaan ditolak karena Custody `Borrowed` bukan `Available`, dan aset tetap ada

### Seleksi dengan aset terblokir ditolak seluruhnya
40. Hendra menjalankan Delete Asset Data pada `Kursi Kerja - U3 {runId}` dan `Genset Diesel - P1 {runId}` sekaligus
41. Verifikasi seluruh permintaan ditolak dan `Kursi Kerja - U3 {runId}` tetap ada walau memenuhi syarat sendiri

### Penghapusan aset yang masih dipakai transaksi dan record lain
42. Hendra menjalankan Delete Asset Data pada aset `Laptop Pro 16 - T1 {runId}`
43. Verifikasi `Draft Pinjam T1 {runId}` tidak disentuh
44. Verifikasi TAG yang terpasang pada `Laptop Pro 16 - T1 {runId}` terlepas
45. Verifikasi baris `Laptop Pro 16 - T1 {runId}` dikeluarkan dari `Paket Transaksi M {runId}`, sedangkan record itu dan baris `Meja Rapat - T2 {runId}` tetap ada
46. Verifikasi `Paket Transaksi S {runId}` ikut terhapus karena hanya memuat `Laptop Pro 16 - T1 {runId}`
47. Verifikasi pengeluaran baris itu dicatat hanya di entri User Action modul ini dan tidak di log record pemilik

### Predikat yang tidak terbaca memblokir Delete Asset Data
48. Predikat berjejak Posted aset `Pompa Air - K1 {runId}` tidak terbaca
49. Hendra menjalankan Delete Asset Data pada aset `Pompa Air - K1 {runId}` lewat permintaan langsung
50. Verifikasi permintaan ditolak `422` karena nilai yang tidak terbaca diperlakukan terblokir, walau `Pompa Air - K1 {runId}` berstatus `Unmanaged`, Custody `Available`, Purchase `Pending`, dan tanpa jejak finansial, dan aset tetap ada
51. Predikat jurnal pelepasan belum Posted aset `Monitor Dell - K2 {runId}` tidak terbaca
52. Hendra menjalankan Delete Asset Data pada aset `Monitor Dell - K2 {runId}` lewat permintaan langsung
53. Verifikasi permintaan ditolak `422` karena nilai yang tidak terbaca diperlakukan terblokir, walau `Monitor Dell - K2 {runId}` ber-Lifecycle `Disposed` dan tanpa jejak finansial, dan aset tetap ada
