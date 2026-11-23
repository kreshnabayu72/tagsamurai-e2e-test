---
id: TC-FA-FAFM-E2E-028-aksi-tulis-entitas-suspended-expired
title: "Entitas Suspended, Expired, atau Grace: halaman terbaca dan aksi tulis ditolak"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [EB-AKS-7, EB-ERR-4, EC-09, V-08, "§9.4.1#r1"]
smoke: []
dependsOn: []
trace:
  EC-09: [15, 17, 23, 25, 35, 37, 43, 45, 55, 57, 63, 65]
  V-08: [15, 17, 23, 25, 35, 37, 43, 45, 55, 57, 63, 65]
  "§9.4.1#r1": [15, 17, 23, 25, 35, 37, 43, 45, 55, 57, 63, 65]
  EB-AKS-7: [12, 13, 15, 17, 21, 23, 25, 32, 33, 35, 37, 41, 43, 45, 52, 53, 55, 57, 61, 63, 65]
  EB-ERR-4: [18, 26, 38, 46, 58, 66]
anchor: [3, 6]
coverage:
  web: automated
---

# Entitas Suspended, Expired, atau Grace: halaman terbaca dan aksi tulis ditolak

## Prerequisites
- Aktor: Total Control `Maya Putri {runId}`; operator Admin Console `Operator Admin Console {runId}` mengubah status entitas dari luar tenant.
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-028-1: Entitas `FAMS State {runId}`, status awal Active.
  - DU-028-2: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-028-3: User `Operator Admin Console {runId}`, operator Admin Console di luar tenant, aktif.
  - DU-028-4: Aset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-028-5: File aktif `damage-aktif-1-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `200.0 KB`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-028-6: File aktif `damage-aktif-2-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `210.0 KB`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-028-7: File di Recycle Bin `damage-bin-1-{runId}.jpg`, Source `Damaged Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, sebagai record pemicu job auto-purge.
  - DU-028-8: File di Recycle Bin `damage-bin-2-{runId}.jpg`, Source `Damaged Photo`, Size `160.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-028-1 yang tidak dipakai spec lain.
  - Akun DU-028-2 aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Entitas aktif: halaman terbaca sebagai pembanding
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` tampil di tab `Damaged`
4. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` tampil di Recycle Bin
7. Tutup modal `Recycle Bin`

### Entitas Suspended: halaman terbaca dan setiap aksi tulis ditolak
8. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `FAMS State {runId}` menjadi `Suspended`
9. Muat ulang halaman
10. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi halaman File Manager terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Suspended`
13. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` tampil di tab `Damaged` pada entitas `Suspended`
14. Kirim Delete atas file `damage-aktif-1-{runId}.jpg`
15. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Kirim Delete bulk atas file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg`
17. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
18. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` masih tampil di tab `Damaged`
19. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
20. Ketik Search `{runId}`, tekan Enter
21. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` tampil di Recycle Bin pada entitas `Suspended`
22. Kirim Permanently Delete atas file `damage-bin-1-{runId}.jpg`
23. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
24. Kirim Permanently Delete bulk atas file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg`
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
26. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` masih tampil di Recycle Bin
27. Tutup modal `Recycle Bin`

### Entitas Expired: halaman terbaca dan setiap aksi tulis ditolak
28. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `FAMS State {runId}` menjadi `Expired`
29. Muat ulang halaman
30. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi halaman File Manager terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired`
33. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` tampil di tab `Damaged` pada entitas `Expired`
34. Kirim Delete atas file `damage-aktif-1-{runId}.jpg`
35. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
36. Kirim Delete bulk atas file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg`
37. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
38. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` masih tampil di tab `Damaged`
39. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` tampil di Recycle Bin pada entitas `Expired`
42. Kirim Permanently Delete atas file `damage-bin-1-{runId}.jpg`
43. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
44. Kirim Permanently Delete bulk atas file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg`
45. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
46. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` masih tampil di Recycle Bin
47. Tutup modal `Recycle Bin`

### Entitas Grace: halaman terbaca dan setiap aksi tulis ditolak
48. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `FAMS State {runId}` menjadi `Expired (Grace)`
49. Muat ulang halaman
50. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi halaman File Manager terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired (Grace)`
53. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` tampil di tab `Damaged` pada entitas `Expired (Grace)`
54. Kirim Delete atas file `damage-aktif-1-{runId}.jpg`
55. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
56. Kirim Delete bulk atas file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg`
57. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
58. Verifikasi file `damage-aktif-1-{runId}.jpg` dan `damage-aktif-2-{runId}.jpg` masih tampil di tab `Damaged`
59. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
60. Ketik Search `{runId}`, tekan Enter
61. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` tampil di Recycle Bin pada entitas `Expired (Grace)`
62. Kirim Permanently Delete atas file `damage-bin-1-{runId}.jpg`
63. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
64. Kirim Permanently Delete bulk atas file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg`
65. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
66. Verifikasi file `damage-bin-1-{runId}.jpg` dan `damage-bin-2-{runId}.jpg` masih tampil di Recycle Bin
67. Tutup modal `Recycle Bin`
