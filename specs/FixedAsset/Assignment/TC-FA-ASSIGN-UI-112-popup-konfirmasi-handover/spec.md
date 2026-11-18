---
id: TC-FA-ASSIGN-UI-112-popup-konfirmasi-handover
title: "Popup Waiting for Confirmation dan dialog Confirm Receipt"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-21, D-ASG-22, S-ASG-10, S-ASG-14, FLD-ASG-16, FLD-ASG-17, V-ASG-22, V-ASG-23, DO-ASG-04, DO-ASG-05, "§4.4#r14", "§4.1#r16"]
smoke: []
dependsOn: []
trace:
  D-ASG-21: [2, 3, 4, 5, 6, 7, 10, 12, 14, 16, 18, 19, 20, 21, 22, 24, 25, 27, 28, 30, 67, 69, 71, 73]
  D-ASG-22: [35, 36, 37, 38, 39, 40, 41, 43, 52, 58, 61]
  S-ASG-10: [45, 47, 53]
  S-ASG-14: [3, 4, 5]
  FLD-ASG-16: 75
  FLD-ASG-17: [38, 45, 47, 52, 53]
  V-ASG-22: [3, 27]
  V-ASG-23: [45, 47]
  DO-ASG-04: 63
  DO-ASG-05: [64, 65]
  "§4.4#r14": 33
  "§4.1#r16": 33
anchor: []
coverage:
  web: automated
---
# Popup Waiting for Confirmation dan dialog Confirm Receipt

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`.
- Layar awal: halaman Handover dengan `[Request Confirmation]` sudah ditekan.
- Komponen: Popup Waiting for Confirmation
- Data:
  - DU-112-1: ASG Transaction ID `ASG-2026-0071`, Assignee `Budi Santoso`, Group `Head Office`.
  - DU-112-2: ASG Transaction ID `ASG-2026-0072`, Assignee `Finance`, PIC `Sari Dewi`, Group `Head Office`.
  - DU-112-3: Aset sesi konfirmasi Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Confirmation `Yes`.
  - DU-112-4: Aset sesi konfirmasi Name `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Confirmation `Yes`.
  - DU-112-5: Aset sesi konfirmasi Name `Camera Sony A7 - 9`, Asset ID `CAM-2026-0009`, Confirmation `Yes`.
  - DU-112-6: Aset sesi konfirmasi Name `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Confirmation `Yes`.
  - DU-112-7: 12 aset sesi konfirmasi Name `Monitor Dell P2422H - {n}`, Asset ID `MON-2026-{n}`, Confirmation `Yes`, dengan `{n}` dari 1 sampai 12.
- Kondisi:
  - K1: sesi konfirmasi berjalan untuk DU-112-1 dengan aset DU-112-3 dan DU-112-4; Jendela konfirmasi Handover bernilai `15 menit`; teks yang diharapkan `Waiting for Budi Santoso to confirm…`, dari Assignee `Budi Santoso`.
  - K2: seperti K1; satu baris siap DU-112-6 belum terscan; teks yang diharapkan `1 asset will stay Waiting for Handover.`, dari 1 baris siap yang belum terscan.
  - K3: seperti K1; sisa jendela konfirmasi 60 detik.
  - K4: sesi konfirmasi untuk DU-112-1 dengan aset DU-112-3, DU-112-4, dan DU-112-5; Assignee mengonfirmasi DU-112-3 dan DU-112-4; hasil yang diharapkan `Budi Santoso confirmed 2 assets.` dan `1 asset not received.`, dari 2 aset terkonfirmasi dan 1 aset tidak diterima.
  - K5: seperti K4; Assignee hanya mengonfirmasi DU-112-3; hasil yang diharapkan `Budi Santoso confirmed 1 asset.` dan `2 assets not received.`.
  - K6: sesi konfirmasi untuk DU-112-2 (Assignee Division) dan jendela konfirmasi habis tanpa konfirmasi; teks yang diharapkan `Sari Dewi didn't confirm. Try again.`, dari PIC `Sari Dewi`.
  - K7: dialog Confirm Receipt dibuka dari `[Confirm on This Device]` untuk DU-112-1 dengan checklist DU-112-3 dan DU-112-4, semua tercentang, dan pernyataan belum dicentang; teks yang diharapkan `Uncheck any asset Budi Santoso didn't receive.`, dari Assignee `Budi Santoso`; pernyataan yang diharapkan `I confirm that Budi Santoso is here and has received these assets and accepted responsibility for them.`.
  - K8: seperti K7 untuk DU-112-2; teks yang diharapkan `Uncheck any asset Sari Dewi didn't receive.`, dari PIC `Sari Dewi`.
  - K9: sesi konfirmasi untuk DU-112-1 dengan aset DU-112-3 dan DU-112-4 masih berjalan di server dengan sisa jendela 10 menit; Hand Over dibuka lagi pada ASG itu sesudah popup tertutup tanpa sengaja.
  - K10: sesi konfirmasi berjalan untuk DU-112-1 dengan 12 aset DU-112-7; jendela konfirmasi bernilai `15 menit`.
  - K11: seperti K1; sisa jendela konfirmasi 61 detik.
  - K12: sesi konfirmasi berjalan untuk DU-112-2 (Assignee Division) dengan aset DU-112-3; jendela konfirmasi bernilai `15 menit`; teks yang diharapkan `Waiting for Sari Dewi to confirm…`, dari PIC `Sari Dewi`.

## Test Steps

### Popup menunggu: teks tunggu, countdown, daftar aset, dan tombol
1. Tampilkan Popup Waiting for Confirmation dengan kondisi K1
2. Verifikasi judul popup `Waiting for Confirmation`
3. Verifikasi popup memuat teks `Waiting for Budi Santoso to confirm…`
4. Verifikasi popup memuat countdown sisa jendela konfirmasi `15 menit`
5. Verifikasi daftar aset sesi memuat `Laptop Dell Latitude 5420 - 10` dengan Asset ID `LPT-2026-0010` dan `Laptop Dell Latitude 5420 - 11` dengan Asset ID `LPT-2026-0011`
6. Verifikasi setiap aset sesi berbadge `Waiting`
7. Verifikasi popup memuat tombol `[Cancel Request]` dan `[Confirm on This Device]`

### Popup tidak tertutup lewat klik di luar maupun Esc
8. Tampilkan Popup Waiting for Confirmation dengan kondisi K1
9. Klik di luar popup
10. Verifikasi popup Waiting for Confirmation tetap terbuka
11. Tekan Esc
12. Verifikasi popup Waiting for Confirmation tetap terbuka setelah Esc, karena pengecualian atas aturan Esc `toast-copy.md` §7

### Aset siap yang belum terscan tetap Waiting for Handover
13. Tampilkan Popup Waiting for Confirmation dengan kondisi K2
14. Verifikasi popup memuat teks `1 asset will stay Waiting for Handover.`

### Countdown berubah ke penanda danger saat sisa 60 detik
15. Tampilkan Popup Waiting for Confirmation dengan kondisi K3
16. Verifikasi countdown memakai penanda `danger` karena sisa jendela 60 detik

### Hasil: sebagian terkonfirmasi dan sebagian tidak diterima
17. Tampilkan Popup Waiting for Confirmation dengan kondisi K4
18. Verifikasi popup memuat hasil `Budi Santoso confirmed 2 assets.`
19. Verifikasi popup memuat hasil `1 asset not received.`
20. Verifikasi `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11` berbadge `Confirmed`
21. Verifikasi `Camera Sony A7 - 9` berbadge `Not received`
22. Verifikasi popup memuat tombol `[Done]`

### Hasil: satu aset terkonfirmasi dan beberapa tidak diterima
23. Tampilkan Popup Waiting for Confirmation dengan kondisi K5
24. Verifikasi popup memuat hasil `Budi Santoso confirmed 1 asset.`
25. Verifikasi popup memuat hasil `2 assets not received.`

### Jendela habis tanpa konfirmasi
26. Tampilkan Popup Waiting for Confirmation dengan kondisi K6
27. Verifikasi popup memuat teks `Sari Dewi didn't confirm. Try again.`
28. Verifikasi popup tidak memuat daftar aset
29. Klik `[Done]`
30. Verifikasi popup Waiting for Confirmation tertutup dan halaman kembali ke langkah scan

### Confirm on This Device membuka dialog Confirm Receipt
31. Tampilkan Popup Waiting for Confirmation dengan kondisi K1
32. Klik `[Confirm on This Device]`
33. Verifikasi dialog `Confirm Receipt` tampil

### Dialog Confirm Receipt: teks, checklist, dan pernyataan
34. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
35. Verifikasi dialog memuat nama Assignee `Budi Santoso`
36. Verifikasi dialog memuat teks `Uncheck any asset Budi Santoso didn't receive.`
37. Verifikasi checklist memuat `Laptop Dell Latitude 5420 - 10` dengan Asset ID `LPT-2026-0010` dan `Laptop Dell Latitude 5420 - 11` dengan Asset ID `LPT-2026-0011`
38. Verifikasi semua aset di checklist tercentang secara default
39. Verifikasi dialog memuat checkbox pernyataan `I confirm that Budi Santoso is here and has received these assets and accepted responsibility for them.`
40. Verifikasi dialog tidak memuat tanda tangan
41. Verifikasi dialog memuat tombol `[Cancel]` dan `[Confirm]`

### Confirm Receipt untuk Assignee Division memakai nama PIC
42. Tampilkan Popup Waiting for Confirmation dengan kondisi K8
43. Verifikasi dialog memuat teks `Uncheck any asset Sari Dewi didn't receive.`

### Confirm nonaktif sampai pernyataan dicentang
44. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
45. Verifikasi `[Confirm]` disabled karena pernyataan belum dicentang
46. Centang checkbox pernyataan
47. Verifikasi `[Confirm]` aktif karena pernyataan dicentang dan aset tercentang

### Confirm nonaktif bila tidak ada aset tercentang
48. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
49. Centang checkbox pernyataan
50. Hapus centang `Laptop Dell Latitude 5420 - 10`
51. Hapus centang `Laptop Dell Latitude 5420 - 11`
52. Verifikasi pesan `Check at least one asset received.` tampil
53. Verifikasi `[Confirm]` disabled karena tidak ada aset tercentang

### Aset tidak tercentang tetap Not received
54. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
55. Centang checkbox pernyataan
56. Hapus centang `Laptop Dell Latitude 5420 - 11`
57. Klik `[Confirm]`
58. Verifikasi `Laptop Dell Latitude 5420 - 11` berbadge `Not received` dan tetap Waiting for Handover

### Cancel menutup dialog Confirm Receipt
59. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
60. Klik `[Cancel]`
61. Verifikasi dialog Confirm Receipt tertutup


### Popup tertutup tanpa sengaja: sesi tetap berjalan dan dibuka lagi dengan sisa countdown
62. Tampilkan Popup Waiting for Confirmation dengan kondisi K9
63. Verifikasi popup menampilkan aset sesi yang sama, `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11`, tetap berbadge `Waiting`
64. Verifikasi countdown menunjukkan sisa jendela 10 menit, bukan jendela penuh `15 menit`
65. Verifikasi popup yang tampil adalah sesi yang sama, bukan sesi baru

### Daftar aset sesi dapat di-scroll
66. Tampilkan Popup Waiting for Confirmation dengan kondisi K10
67. Verifikasi daftar aset sesi dapat di-scroll
68. Gulir daftar aset sesi sampai aset terakhir
69. Verifikasi aset `Monitor Dell P2422H - 12` dengan Asset ID `MON-2026-12` tampil di daftar

### Countdown berpenanda primary saat sisa lebih dari 60 detik
70. Tampilkan Popup Waiting for Confirmation dengan kondisi K11
71. Verifikasi countdown memakai penanda `primary` karena sisa jendela 61 detik

### Teks tunggu untuk Assignee Division memakai nama PIC
72. Tampilkan Popup Waiting for Confirmation dengan kondisi K12
73. Verifikasi popup memuat teks `Waiting for Sari Dewi to confirm…`

### Pernyataan Confirm Receipt tidak tercentang secara default
74. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
75. Verifikasi checkbox pernyataan tidak tercentang saat dialog Confirm Receipt dibuka


