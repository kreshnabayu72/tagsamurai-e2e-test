---
id: TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager
title: "Hapus Photo / Damaged Photo lewat File Manager: foto tampil kosong pada node Missing Log, status record, status global aset, dan Damage Report tidak berubah"
layer: ui-e2e
priority: Critical
caseType: Edge
status: ready-for-automation
sourceRules: ["§1.2#r124", "§1.2#r125", "§1.2#r129", "§9.2#b24", "§9.4.2#r36", "§9.4.4#r10", "§9.7#r11", "§10#r8", "§11#r14", "§9.4.1#r14", "§8.1#r14", "§8.1#r12"]
smoke: []
dependsOn: ["File Manager: Delete File", "Damaged: Damage Log"]
trace:
  "§1.2#r124": [10, 12, 37, 54]
  "§1.2#r125": 5
  "§1.2#r129": [29, 32, 33, 45, 47, 50, 51, 62, 63, 64, 66]
  "§9.2#b24": [6, 27, 32, 33, 45, 47, 51, 62, 64]
  "§9.4.2#r36": [14, 16, 18, 23, 27, 32, 33, 41, 45, 47, 50, 51, 58, 62, 64, 66]
  "§9.4.4#r10": [32, 33, 47, 64]
  "§9.7#r11": [27, 32, 33, 45, 47, 50, 51, 64]
  "§10#r8": [5, 27, 29, 32, 33, 45, 47, 51, 64]
  "§11#r14": [10, 12, 24, 37, 32, 33, 47, 54, 64]
  "§9.4.1#r14": [18, 23, 41, 32, 33, 47, 58, 64]
  "§8.1#r14": [30, 31, 46, 32, 33, 47, 63, 64]
  "§8.1#r12": [33]
anchor: [3, 4]
coverage:
  web: automated
---

# Hapus Photo / Damaged Photo lewat File Manager: foto tampil kosong pada node Missing Log, status record, status global aset, dan Damage Report tidak berubah

## Prerequisites
- Aktor: Total Control `Rina W`, Aktor Missing dan pemegang aksi Delete di File Manager.
- Layar awal: halaman Missing, sub-tab History.
- Data:
  - DU-048-1: Record Found `Camera DSLR Canon R6 {runId}`, aset tanpa TAG, Group `Finance Room`, Source `Manual`, dengan node `Reported found by Sari Dewanti {runId}` memuat Photo `foto-laporan-ditemukan {runId}.png`, dan node `Marked as found by Rina W` memuat Found at `Finance Room`, Asset Status `Normal`, Note `Ditemukan di rak server lantai 2`, dan Photo `foto-ditemukan {runId}.png`.
  - DU-048-2: Record Found `Laptop Dell Latitude 5420 {runId}`, aset tanpa TAG, Group `Finance Room`, Source `Manual`, dengan node `Marked as found by Rina W` memuat Asset Status `Damaged`, Note `Layar retak dan engsel patah saat ditemukan`, dan Damaged Photo `foto-kerusakan-laptop {runId}.png` (Source File Manager `Damaged Photo`), serta satu Damage Report dengan Source `Missing Asset`.
  - DU-048-3: pengguna `Rina W`, Role Total Control, cakupan seluruh client.
  - DU-048-5: Berkas `foto-ditemukan {runId}.png`, Source File Manager `Found Photo`, aset `Camera DSLR Canon R6 {runId}`; toast hapus `Success, foto-ditemukan {runId}.png has been deleted.`.
  - DU-048-6: Berkas `foto-laporan-ditemukan {runId}.png`, Source File Manager `Found Photo`, aset `Camera DSLR Canon R6 {runId}`; toast hapus `Success, foto-laporan-ditemukan {runId}.png has been deleted.`.
  - DU-048-7: Berkas `foto-kerusakan-laptop {runId}.png`, Source File Manager `Damaged Photo`, aset `Laptop Dell Latitude 5420 {runId}`; toast hapus `Success, foto-kerusakan-laptop {runId}.png has been deleted.`.
  - DU-048-4: pengguna `Sari Dewanti {runId}`, Role Read Only, cakupan seluruh client, pengirim `I found it` pada DU-048-1.
  - DU-048-8: Record Found `Printer HP LaserJet M404 {runId}`, aset asal `Damaged + Missing` tanpa TAG, Group `Finance Room`, Source `Manual`, dengan node `Marked as found by Rina W` memuat Asset Status `Damaged`, Note `Rumah printer retak sejak sebelum hilang`, dan Damaged Photo `foto-kerusakan-printer {runId}.png`.
  - DU-048-9: Berkas `foto-kerusakan-printer {runId}.png`, Source File Manager `Damaged Photo`, aset `Printer HP LaserJet M404 {runId}`; toast hapus `Success, foto-kerusakan-printer {runId}.png has been deleted.`.
  - Keempat berkas diunggah lewat Mark as Found dan `I found it` sebelum spec berjalan, dan tidak ada record Missing lain untuk kedua aset.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps

### Foto tampil pada node sebelum dihapus
1. Ketik Search `{runId}`, tekan Enter
2. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
3. Verifikasi node `Marked as found by Rina W` memuat Photo `foto-ditemukan {runId}.png`
4. Verifikasi node `Reported found by Sari Dewanti {runId}` memuat Photo `foto-laporan-ditemukan {runId}.png`
5. Verifikasi node `Marked as found by Rina W` tidak menyediakan kontrol untuk mengganti atau mengosongkan Photo
6. Verifikasi badge status record `Found` tampil
7. Klik `✕` pada dialog Missing Log
8. Buka halaman `Settings > File Manager`
9. Ketik Search `foto-ditemukan {runId}.png`, tekan Enter
10. Verifikasi baris `foto-ditemukan {runId}.png` tampil dengan Source `Found Photo` dan aset `Camera DSLR Canon R6 {runId}`
11. Ganti isi kotak search dengan `foto-laporan-ditemukan {runId}.png`, tekan Enter
12. Verifikasi baris `foto-laporan-ditemukan {runId}.png` tampil dengan Source `Found Photo` dan aset `Camera DSLR Canon R6 {runId}`

### Hapus Photo lewat File Manager tidak diblokir
13. Klik `⋯` pada baris `foto-laporan-ditemukan {runId}.png`
14. Verifikasi aksi `Delete` tampil dan Enabled
15. Klik `Delete`
16. Verifikasi dialog `Delete File` tampil
17. Klik `[Delete]` pada dialog
18. Verifikasi toast `Success, foto-laporan-ditemukan {runId}.png has been deleted.` tampil
19. Ganti isi kotak search dengan `foto-ditemukan {runId}.png`, tekan Enter
20. Klik `⋯` pada baris `foto-ditemukan {runId}.png`
21. Klik `Delete`
22. Klik `[Delete]` pada dialog `Delete File`
23. Verifikasi toast `Success, foto-ditemukan {runId}.png has been deleted.` tampil
24. Verifikasi baris `foto-ditemukan {runId}.png` tidak tampil lagi pada tab Files

### Node Missing Log menampilkan foto kosong, status record tidak berubah
25. Buka sub-tab `History` pada tab `Missing` di halaman `Assets`
26. Ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
27. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` tetap `Found`
28. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
29. Verifikasi badge status record `Found` tampil
30. Verifikasi node `Marked as found by Rina W` memuat Found at `Finance Room`
31. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Normal` dan Note `Ditemukan di rak server lantai 2`
32. Verifikasi node `Marked as found by Rina W` tidak menampilkan baris Photo
33. Verifikasi node `Reported found by Sari Dewanti {runId}` tidak menampilkan baris Photo
34. Klik `✕` pada dialog Missing Log

### Damaged Photo dihapus: Damage Report dan status aset tidak berubah
35. Buka halaman `Settings > File Manager`
36. Ketik Search `foto-kerusakan-laptop {runId}.png`, tekan Enter
37. Verifikasi baris `foto-kerusakan-laptop {runId}.png` tampil dengan Source `Damaged Photo` dan aset `Laptop Dell Latitude 5420 {runId}`
38. Klik `⋯` pada baris `foto-kerusakan-laptop {runId}.png`
39. Klik `Delete`
40. Klik `[Delete]` pada dialog `Delete File`
41. Verifikasi toast `Success, foto-kerusakan-laptop {runId}.png has been deleted.` tampil
42. Buka sub-tab `History` pada tab `Missing` di halaman `Assets`
43. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
44. Klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
45. Verifikasi badge status record `Found` tampil
46. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Damaged` dan Note `Layar retak dan engsel patah saat ditemukan`
47. Verifikasi node `Marked as found by Rina W` tidak menampilkan baris Damaged Photo
48. Klik `✕` pada dialog Missing Log
49. Buka Damage Log milik aset `Laptop Dell Latitude 5420 {runId}`
50. Verifikasi Damage Report dengan Source `Missing Asset` tetap tampil di Damage Log
51. Verifikasi Asset Status `Laptop Dell Latitude 5420 {runId}` tetap `Damaged`

### Asal Damaged + Missing: Damaged Photo dihapus, node Missing Log dan status aset tidak berubah
52. Buka halaman `Settings > File Manager`
53. Ketik Search `foto-kerusakan-printer {runId}.png`, tekan Enter
54. Verifikasi baris `foto-kerusakan-printer {runId}.png` tampil dengan Source `Damaged Photo` dan aset `Printer HP LaserJet M404 {runId}`
55. Klik `⋯` pada baris `foto-kerusakan-printer {runId}.png`
56. Klik `Delete`
57. Klik `[Delete]` pada dialog `Delete File`
58. Verifikasi toast `Success, foto-kerusakan-printer {runId}.png has been deleted.` tampil
59. Buka sub-tab `History` pada tab `Missing` di halaman `Assets`
60. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
61. Klik nama `Printer HP LaserJet M404 {runId}` pada kolom Name
62. Verifikasi badge status record `Found` tampil
63. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Damaged` dan Note `Rumah printer retak sejak sebelum hilang`
64. Verifikasi node `Marked as found by Rina W` tidak menampilkan baris Damaged Photo
65. Klik `✕` pada dialog Missing Log
66. Verifikasi Asset Status `Printer HP LaserJet M404 {runId}` tetap `Damaged`
