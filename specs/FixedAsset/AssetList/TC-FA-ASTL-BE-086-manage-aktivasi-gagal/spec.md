---
id: TC-FA-ASTL-BE-086-manage-aktivasi-gagal
title: "Aktivasi Manage gagal setelah jeda transisi"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-15t, ASTL-LOGIC-15u, ASTL-LOGIC-15v, ASTL-LOGIC-15w, ASTL-LOGIC-16n, EC-50, F-ASTL-16.k5]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-15t: [4, 9, 16]
  ASTL-LOGIC-15u: 5
  ASTL-LOGIC-15v: [9, 10]
  ASTL-LOGIC-15w: [15, 35]
  ASTL-LOGIC-16n: [20, 21, 24, 28, 40, 41, 44]
  EC-50: [4, 5, 6, 10, 11, 15, 26, 29, 30, 35, 36]
  F-ASTL-16.k5: [6, 11, 29, 30, 31]
anchor: []
---

# Aktivasi Manage gagal setelah jeda transisi

## Prerequisites
- Aktor: Total Control (Hendra).
- Data:
  - DU-086-1: User, total Control seluruh client: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-086-2: Group, group quota untuk aktivasi gagal: Name `Cabang Surabaya Q {runId}`, Available license `2`.
  - DU-086-3: Asset, aset Unmanaged yang di-Manage lewat Available quota: Name `Tablet Inventaris - Q1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya Q {runId}`.
  - DU-086-4: Group, group Switch dengan aset tukar masih ada: Name `Cabang Surabaya S {runId}`, Available license `0`.
  - DU-086-5: Asset, aset Unmanaged yang di-Manage lewat Switch: Name `Tablet Inventaris - S1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya S {runId}`.
  - DU-086-6: Asset, aset managed yang ditukar dan masih ada: Name `Printer Laser - S2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Surabaya S {runId}`.
  - DU-086-7: Group, group Switch dengan aset tukar dihapus: Name `Cabang Surabaya W {runId}`, Available license `0`.
  - DU-086-8: Asset, aset Unmanaged yang di-Manage lewat Switch: Name `Tablet Inventaris - W1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya W {runId}`.
  - DU-086-9: Asset, aset managed yang ditukar lalu dihapus: Name `Printer Laser - W2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Surabaya W {runId}`.
  - DU-086-10: Group, group quota untuk aset Pending Activation yang dihapus: Name `Cabang Surabaya P {runId}`, Available license `1`.
  - DU-086-11: Asset, aset Unmanaged yang dihapus saat Pending Activation: Name `Tablet Inventaris - P1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya P {runId}`.
  - DU-086-12: Group, group Switch untuk aset Pending Activation yang dihapus: Name `Cabang Surabaya X {runId}`, Available license `0`.
  - DU-086-13: Asset, aset Unmanaged yang di-Manage lewat Switch lalu dihapus: Name `Tablet Inventaris - X1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya X {runId}`.
  - DU-086-14: Asset, aset managed yang ditukar dan tetap Unmanaged: Name `Printer Laser - X2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Surabaya X {runId}`.
  - DU-086-15: Asset, aset Unmanaged kedua di group Q untuk mencoba Manage selama jeda: Name `Tablet Inventaris - Q2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya Q {runId}`.
  - DU-086-16: Asset, aset Unmanaged kedua di group P untuk mencoba Manage selama jeda: Name `Tablet Inventaris - P2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya P {runId}`.
  - DU-086-17: Group, group Switch untuk aset tukar yang masuk proses pelepasan aset: Name `Cabang Surabaya Y {runId}`, Available license `0`.
  - DU-086-18: Asset, aset Unmanaged yang di-Manage lewat Switch: Name `Tablet Inventaris - Y1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya Y {runId}`.
  - DU-086-19: Asset, aset managed yang ditukar lalu masuk proses pelepasan aset: Name `Printer Laser - Y2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Surabaya Y {runId}`.
  - DU-086-20: Group, group quota untuk aset Pending Activation yang masuk proses pelepasan aset: Name `Cabang Surabaya R {runId}`, Available license `1`.
  - DU-086-21: Asset, aset Unmanaged yang masuk proses pelepasan aset saat Pending Activation: Name `Tablet Inventaris - R1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya R {runId}`.
  - DU-086-22: Group, group Switch untuk aset Pending Activation yang masuk proses pelepasan aset: Name `Cabang Surabaya Z {runId}`, Available license `0`.
  - DU-086-23: Asset, aset Unmanaged yang di-Manage lewat Switch lalu masuk proses pelepasan aset: Name `Tablet Inventaris - Z1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Surabaya Z {runId}`.
  - DU-086-24: Asset, aset managed yang ditukar dan tetap Unmanaged: Name `Printer Laser - Z2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Surabaya Z {runId}`.
- Kondisi: aktivasi aset yang di-Manage gagal ketika Managed Transition Time berakhir.

## Test Steps

### Aktivasi gagal dengan sumber Available quota
1. Catat jumlah entri Changelog aset `Tablet Inventaris - Q1 {runId}`
2. Hendra meng-Manage aset `Tablet Inventaris - Q1 {runId}` dengan sumber `Available quota`
3. Aktivasi `Tablet Inventaris - Q1 {runId}` gagal ketika Managed Transition Time group `Cabang Surabaya Q {runId}` berakhir
4. Verifikasi `Tablet Inventaris - Q1 {runId}` kembali `Unmanaged` dan tidak berstatus `Pending Activation`
5. Verifikasi slot Reserved dikembalikan otomatis sehingga Available group `Cabang Surabaya Q {runId}` kembali `2`
6. Verifikasi Changelog `Tablet Inventaris - Q1 {runId}` memuat entri `Pending Activation` ke `Unmanaged` dengan pelaku `System`

### Aktivasi gagal dengan sumber Switch, aset yang ditukar masih ada
7. Hendra meng-Manage aset `Tablet Inventaris - S1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - S2 {runId}`
8. Aktivasi `Tablet Inventaris - S1 {runId}` gagal ketika Managed Transition Time group `Cabang Surabaya S {runId}` berakhir
9. Verifikasi `Tablet Inventaris - S1 {runId}` kembali `Unmanaged` dan pertukaran dibatalkan
10. Verifikasi `Printer Laser - S2 {runId}` kembali managed karena masih ada dan masih `Unmanaged`
11. Verifikasi Changelog `Printer Laser - S2 {runId}` memuat entri `Unmanaged` ke `Managed` dengan pelaku `System`

### Aktivasi gagal dengan sumber Switch, aset yang ditukar sudah dihapus
12. Hendra meng-Manage aset `Tablet Inventaris - W1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - W2 {runId}`
13. Hendra menjalankan Delete Asset Data pada aset `Printer Laser - W2 {runId}` selama jeda transisi
14. Aktivasi `Tablet Inventaris - W1 {runId}` gagal ketika Managed Transition Time group `Cabang Surabaya W {runId}` berakhir
15. Verifikasi license `Printer Laser - W2 {runId}` kembali sebagai slot Available sehingga Available group `Cabang Surabaya W {runId}` menjadi `1`, dan tidak ada kuota yang hilang
16. Verifikasi `Tablet Inventaris - W1 {runId}` kembali `Unmanaged`

### Aset Pending Activation keluar sebelum jeda transisi berakhir
17. Catat jumlah entri Changelog aset `Tablet Inventaris - P1 {runId}`
18. Hendra meng-Manage aset `Tablet Inventaris - P1 {runId}` dengan sumber `Available quota`
19. Hendra menjalankan Delete Asset Data pada aset `Tablet Inventaris - P1 {runId}` sebelum jeda transisi berakhir
20. Verifikasi aktivasi terjadwal `Tablet Inventaris - P1 {runId}` dibatalkan tanpa entri `Pending Activation` ke `Managed` maupun ke `Unmanaged`
21. Verifikasi kuota Reserved dilepas sehingga Available group `Cabang Surabaya P {runId}` kembali `1`
22. Hendra meng-Manage aset `Tablet Inventaris - X1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - X2 {runId}`
23. Hendra menjalankan Delete Asset Data pada aset `Tablet Inventaris - X1 {runId}` sebelum jeda transisi berakhir
24. Verifikasi `Printer Laser - X2 {runId}` tetap `Unmanaged` dan tidak dikembalikan managed

### Jeda Manage group tetap berjalan setelah aktivasi gagal atau aset keluar
25. Hendra meng-Manage aset `Tablet Inventaris - Q2 {runId}` dengan sumber `Available quota` selama Managed Action Retry Delay group `Cabang Surabaya Q {runId}` berjalan, setelah aktivasi `Tablet Inventaris - Q1 {runId}` gagal
26. Verifikasi permintaan ditolak karena jeda walau Available `2`, `Tablet Inventaris - Q2 {runId}` tetap `Unmanaged`, dan jeda tidak dimulai ulang oleh kegagalan aktivasi sehingga titik awalnya tetap waktu submit Manage `Tablet Inventaris - Q1 {runId}` yang berhasil
27. Hendra meng-Manage aset `Tablet Inventaris - P2 {runId}` dengan sumber `Available quota` selama Managed Action Retry Delay group `Cabang Surabaya P {runId}` berjalan, setelah `Tablet Inventaris - P1 {runId}` dihapus
28. Verifikasi permintaan ditolak karena jeda group `Cabang Surabaya P {runId}` tetap berjalan sampai selesai walau `Tablet Inventaris - P1 {runId}` sudah dihapus, dan `Tablet Inventaris - P2 {runId}` tetap `Unmanaged`

### Penyelesaian transisi oleh sistem tercatat di Activity Log tanpa System Log
29. Verifikasi Activity Log `Tablet Inventaris - Q1 {runId}` memuat entri `Pending Activation` ke `Unmanaged` dengan Modified By `System`
30. Verifikasi Activity Log `Printer Laser - S2 {runId}` memuat entri `Unmanaged` ke `Managed` dengan Modified By `System`
31. Verifikasi System Log tidak memuat entri untuk penyelesaian transisi `Tablet Inventaris - Q1 {runId}` dan `Printer Laser - S2 {runId}`

### Aktivasi gagal dengan sumber Switch, aset yang ditukar masuk proses pelepasan aset
32. Hendra meng-Manage aset `Tablet Inventaris - Y1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - Y2 {runId}`
33. Aset `Printer Laser - Y2 {runId}` masuk proses pelepasan aset selama jeda transisi
34. Aktivasi `Tablet Inventaris - Y1 {runId}` gagal ketika Managed Transition Time group `Cabang Surabaya Y {runId}` berakhir
35. Verifikasi license `Printer Laser - Y2 {runId}` kembali sebagai slot Available sehingga Available group `Cabang Surabaya Y {runId}` menjadi `1`, dan tidak ada kuota yang hilang
36. Verifikasi `Tablet Inventaris - Y1 {runId}` kembali `Unmanaged`

### Aset Pending Activation keluar lewat pelepasan aset sebelum jeda transisi berakhir
37. Catat jumlah entri Changelog aset `Tablet Inventaris - R1 {runId}`
38. Hendra meng-Manage aset `Tablet Inventaris - R1 {runId}` dengan sumber `Available quota`
39. Aset `Tablet Inventaris - R1 {runId}` masuk proses pelepasan aset sebelum jeda transisi berakhir
40. Verifikasi aktivasi terjadwal `Tablet Inventaris - R1 {runId}` dibatalkan tanpa entri `Pending Activation` ke `Managed` maupun ke `Unmanaged`
41. Verifikasi kuota Reserved dilepas sehingga Available group `Cabang Surabaya R {runId}` kembali `1`
42. Hendra meng-Manage aset `Tablet Inventaris - Z1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - Z2 {runId}`
43. Aset `Tablet Inventaris - Z1 {runId}` masuk proses pelepasan aset sebelum jeda transisi berakhir
44. Verifikasi `Printer Laser - Z2 {runId}` tetap `Unmanaged` dan tidak dikembalikan managed
