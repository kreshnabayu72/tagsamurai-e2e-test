---
id: TC-FA-ASTL-BE-084-manage-kuota-lisensi
title: "Aturan server Manage dan kuota lisensi"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-15i, ASTL-LOGIC-15j, ASTL-LOGIC-15l, ASTL-LOGIC-15m, ASTL-LOGIC-15n, ASTL-LOGIC-15p, ASTL-LOGIC-15q, ASTL-LOGIC-15s, EC-49, F-ASTL-16.k4, "§9.2#p6"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-15i: [2, 5, 7]
  ASTL-LOGIC-15j: [13, 14]
  ASTL-LOGIC-15l: 19
  ASTL-LOGIC-15m: [3, 5, 7]
  ASTL-LOGIC-15n: 18
  ASTL-LOGIC-15p: [9, 10]
  ASTL-LOGIC-15q: 11
  ASTL-LOGIC-15s: [16, 33]
  EC-49: [9, 10, 16]
  F-ASTL-16.k4: [9, 11]
  "§9.2#p6": [2, 3, 21, 23, 25, 27, 29, 31]
anchor: []
---

# Aturan server Manage dan kuota lisensi

## Prerequisites
- Aktor: Total Control (Hendra), Group Manager (Dewi).
- Data:
  - DU-084-1: User, total Control seluruh client: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-084-2: Group, group dengan kuota cukup di atas jumlah aset: Name `Cabang Medan A {runId}`, Available license `3`.
  - DU-084-3: Asset, aset Unmanaged di group A: Name `Tablet Inventaris - A1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan A {runId}`.
  - DU-084-4: Asset, aset Unmanaged di group A: Name `Tablet Inventaris - A2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan A {runId}`.
  - DU-084-5: Asset, aset Unmanaged di group A: Name `Tablet Inventaris - A3 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan A {runId}`.
  - DU-084-6: Group, group dengan kuota tepat sama dengan jumlah aset: Name `Cabang Medan B {runId}`, Available license `2`.
  - DU-084-7: Asset, aset Unmanaged di group B: Name `Tablet Inventaris - B1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan B {runId}`.
  - DU-084-8: Asset, aset Unmanaged di group B: Name `Tablet Inventaris - B2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan B {runId}`.
  - DU-084-9: Group, group dengan kuota kurang dari jumlah aset: Name `Cabang Medan C {runId}`, Available license `2`.
  - DU-084-10: Asset, aset Unmanaged di group C: Name `Tablet Inventaris - C1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan C {runId}`.
  - DU-084-11: Asset, aset Unmanaged di group C: Name `Tablet Inventaris - C2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan C {runId}`.
  - DU-084-12: Asset, aset Unmanaged di group C: Name `Tablet Inventaris - C3 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan C {runId}`.
  - DU-084-13: Group, group dengan satu slot tersisa: Name `Cabang Medan D {runId}`, Available license `1`.
  - DU-084-14: Asset, aset Unmanaged di group D: Name `Tablet Inventaris - D1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan D {runId}`.
  - DU-084-15: Group, group tanpa Available license untuk jalur Switch: Name `Cabang Medan E {runId}`, Available license `0`.
  - DU-084-16: Asset, aset Unmanaged yang di-Manage lewat Switch: Name `Tablet Inventaris - E1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan E {runId}`.
  - DU-084-17: Asset, aset managed yang ditukar: Name `Printer Laser - E2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Medan E {runId}`.
  - DU-084-18: Asset, aset managed yang ditolak sebagai sasaran Manage: Name `Server Rack - E3 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Medan F {runId}`.
  - DU-084-19: Group, group tanpa riwayat submit Manage untuk penolakan aset bukan Unmanaged: Name `Cabang Medan F {runId}`, Available license `1`.
  - DU-084-20: Asset, aset Unmanaged di group F: Name `Tablet Inventaris - F1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan F {runId}`.
  - DU-084-21: Group, group kedua untuk seleksi lintas group: Name `Cabang Medan H {runId}`, Available license `1`.
  - DU-084-22: Asset, aset Unmanaged di group H: Name `Tablet Inventaris - H1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan H {runId}`.
  - DU-084-23: Asset, aset managed di group H sebagai pasangan Switch dari group lain: Name `Printer Laser - H2 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Medan H {runId}`.
  - DU-084-24: Group, group Switch tanpa Available license: Name `Cabang Medan G {runId}`, Available license `0`.
  - DU-084-25: Asset, aset Unmanaged yang di-Manage lewat Switch di group G: Name `Tablet Inventaris - G1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan G {runId}`.
  - DU-084-26: Asset, aset Unmanaged yang bukan pasangan sah: Name `Tablet Inventaris - G2 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan G {runId}`.
  - DU-084-27: Asset, aset managed pasangan sah pertama: Name `Printer Laser - G3 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Medan G {runId}`.
  - DU-084-28: Asset, aset managed pasangan kedua (kelebihan jumlah): Name `Printer Laser - G4 {runId}`, Lifecycle `Active`, Status `Managed`, Group `Cabang Medan G {runId}`.
  - DU-084-29: Group, group di luar cakupan Dewi: Name `Cabang Medan I {runId}`, Available license `1`.
  - DU-084-30: Asset, aset Unmanaged di group I: Name `Tablet Inventaris - I1 {runId}`, Lifecycle `Active`, Status `Unmanaged`, Group `Cabang Medan I {runId}`.
  - DU-084-31: User, group Manager group F: Name `Dewi Lestari {runId}`, Role `Group Manager`, Cakupan `Cabang Medan F {runId}`.
- Kondisi: Date Format bernilai `dd/MM/yy`.

## Test Steps

### Manage dengan sumber Available quota mengurangi Available
1. Hendra meng-Manage aset `Tablet Inventaris - A1 {runId}` dan `Tablet Inventaris - A2 {runId}` dengan sumber `Available quota`
2. Verifikasi server memeriksa kuota Available group `Cabang Medan A {runId}` terhadap dua aset yang di-Manage, dan permintaan diterima karena Available `3` mencukupi
3. Verifikasi Available group `Cabang Medan A {runId}` langsung berkurang dari `3` menjadi `1` sebagai slot Reserved
4. Hendra meng-Manage aset `Tablet Inventaris - B1 {runId}` dan `Tablet Inventaris - B2 {runId}` dengan sumber `Available quota`
5. Verifikasi permintaan diterima walau jumlah aset yang di-Manage tepat sama dengan Available `2`, dan Available group `Cabang Medan B {runId}` menjadi `0`
6. Hendra meng-Manage aset `Tablet Inventaris - D1 {runId}` dengan sumber `Available quota`
7. Verifikasi permintaan diterima dengan sisa satu slot, dan Available group `Cabang Medan D {runId}` menjadi `0`

### Jeda antar aksi Manage berlaku per group
8. Hendra meng-Manage aset `Tablet Inventaris - A3 {runId}` dengan sumber `Available quota` selama Managed Action Retry Delay group `Cabang Medan A {runId}` berjalan
9. Verifikasi permintaan ditolak karena jeda antar aksi Manage, walau Available `1` masih tersisa, dan `Tablet Inventaris - A3 {runId}` tetap `Unmanaged`
10. Verifikasi Manage pada group `Cabang Medan D {runId}` diterima pada langkah sebelumnya, sehingga jeda `Cabang Medan A {runId}` tidak memengaruhi group lain
11. Verifikasi waktu Manage tersedia kembali pada group `Cabang Medan A {runId}` sama dengan waktu submit Manage yang berhasil ditambah nilai Managed Action Retry Delay, dalam Time Zone client dan format tanggal-waktu `dd/MM/yy`

### Kuota tidak cukup menolak seluruh aksi dan tidak memulai jeda
12. Hendra meng-Manage aset `Tablet Inventaris - C1 {runId}`, `Tablet Inventaris - C2 {runId}`, dan `Tablet Inventaris - C3 {runId}` dengan sumber `Available quota`
13. Verifikasi seluruh permintaan ditolak dengan `QUOTA_EXCEEDED` karena Available `2` kurang dari tiga aset
14. Verifikasi ketiga aset `Tablet Inventaris - C1 {runId}`, `Tablet Inventaris - C2 {runId}`, dan `Tablet Inventaris - C3 {runId}` tetap `Unmanaged` dan Available group `Cabang Medan C {runId}` tetap `2`
15. Hendra meng-Manage aset `Tablet Inventaris - C1 {runId}` dan `Tablet Inventaris - C2 {runId}` dengan sumber `Available quota`
16. Verifikasi permintaan diterima tanpa menunggu jeda, karena submit yang ditolak sebelumnya tidak memulai jeda

### Manage dengan sumber Switch tidak mengubah Available
17. Hendra meng-Manage aset `Tablet Inventaris - E1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - E2 {runId}`
18. Verifikasi `Printer Laser - E2 {runId}` langsung menjadi `Unmanaged`
19. Verifikasi license `Printer Laser - E2 {runId}` dipakai `Tablet Inventaris - E1 {runId}`, sehingga Available group `Cabang Medan E {runId}` tetap `0`

### Server hanya menerima aset Unmanaged
20. Hendra meng-Manage aset `Server Rack - E3 {runId}` yang berstatus managed di group `Cabang Medan F {runId}` dengan sumber `Available quota`, dengan Available `1` dan tanpa jeda di group itu
21. Verifikasi permintaan ditolak karena aset terpilih tidak berstatus `Unmanaged` (bukan karena jeda atau kuota), dan `Server Rack - E3 {runId}` tetap managed

### Server menolak Manage atas aset dari lebih dari satu group
22. Hendra meng-Manage aset `Tablet Inventaris - F1 {runId}` dan `Tablet Inventaris - H1 {runId}` dengan sumber `Available quota`
23. Verifikasi permintaan ditolak karena aset terpilih tidak berada pada satu group, kedua aset tetap `Unmanaged`, dan Available group `Cabang Medan F {runId}` serta `Cabang Medan H {runId}` tetap `1`

### Server menolak Manage di luar cakupan group pemanggil
24. Dewi meng-Manage aset `Tablet Inventaris - I1 {runId}` dengan sumber `Available quota`
25. Verifikasi permintaan ditolak dengan pesan `You don't have permission to do this.` karena `Cabang Medan I {runId}` di luar cakupan Dewi, `Tablet Inventaris - I1 {runId}` tetap `Unmanaged`, dan Available group `Cabang Medan I {runId}` tetap `1`

### Switch dengan pasangan yang tidak sesuai ditolak dan membatalkan seluruh aksi
26. Hendra meng-Manage aset `Tablet Inventaris - G1 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - H2 {runId}` dari group `Cabang Medan H {runId}`
27. Verifikasi permintaan ditolak `422` karena pasangan tidak berada pada group yang sama, `Tablet Inventaris - G1 {runId}` tetap `Unmanaged`, dan `Printer Laser - H2 {runId}` tetap managed
28. Hendra meng-Manage aset `Tablet Inventaris - G1 {runId}` dengan sumber Switch, menukar aset `Tablet Inventaris - G2 {runId}` yang berstatus `Unmanaged`
29. Verifikasi permintaan ditolak `422` karena pasangan bukan aset managed, `Tablet Inventaris - G1 {runId}` dan `Tablet Inventaris - G2 {runId}` tetap `Unmanaged`
30. Hendra meng-Manage aset `Tablet Inventaris - G1 {runId}` dengan sumber Switch, menukar `Printer Laser - G3 {runId}` dan `Printer Laser - G4 {runId}` sekaligus
31. Verifikasi permintaan ditolak `422` karena jumlah pasangan tidak sama dengan jumlah aset yang di-Manage, seluruh aksi dibatalkan, `Tablet Inventaris - G1 {runId}` tetap `Unmanaged`, serta `Printer Laser - G3 {runId}` dan `Printer Laser - G4 {runId}` tetap managed
32. Hendra meng-Manage aset `Tablet Inventaris - G1 {runId}` dengan sumber Switch, menukar `Printer Laser - G3 {runId}`
33. Verifikasi permintaan diterima tanpa menunggu jeda karena ketiga submit yang ditolak sebelumnya tidak memulai jeda, dan `Printer Laser - G3 {runId}` langsung menjadi `Unmanaged`
