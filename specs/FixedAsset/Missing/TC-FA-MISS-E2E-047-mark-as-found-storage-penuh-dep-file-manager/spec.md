---
id: TC-FA-MISS-E2E-047-mark-as-found-storage-penuh-dep-file-manager
title: "Mark as Found saat Storage penuh: Photo / Damaged Photo baru ditolak dengan toast Error persisten, dialog dan isian tetap, tanpa perubahan record; tanpa Photo atau tanpa kuota tidak diblokir"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["MISS-LOGIC-10a", "MISS-LOGIC-10c", "MISS-LOGIC-10d", "MISS-LOGIC-10e", "V-16", "TS-MIS-10", "EC-MIS-36", "F-MISS-04.k5"]
smoke: []
dependsOn: ["File Manager: Storage Usage", "Damaged: Damage Log"]
trace:
  "MISS-LOGIC-10a": [6, 31, 47]
  "MISS-LOGIC-10c": [9, 23, 35, 50, 57, 64]
  "MISS-LOGIC-10d": [35, 36, 37, 38, 50, 51]
  "MISS-LOGIC-10e": [11, 12, 13, 14, 17, 19, 36, 37, 38, 40, 42, 51, 54]
  "V-16": [9, 23, 35, 50]
  "TS-MIS-10": [9, 23, 35, 50]
  "EC-MIS-36": [9, 23, 35, 50, 57, 64]
  "F-MISS-04.k5": [9, 35, 50]
anchor: [17, 40, 53]
coverage:
  web: automated
---

# Mark as Found saat Storage penuh: Photo / Damaged Photo baru ditolak dengan toast Error persisten, dialog dan isian tetap, tanpa perubahan record; tanpa Photo atau tanpa kuota tidak diblokir

## Prerequisites
- Mode: FE+BE.
- Aktor: Rina W, Total Control, Aktor Missing, bukan Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Sumber aturan: tidak ada TestCase untuk aturan ini; spec disusun langsung dari PRD `fixed-asset/missing/PRD/missing.md` (`MISS-LOGIC-10a`, `MISS-LOGIC-10c` s.d. `MISS-LOGIC-10e`, `V-16`, `TS-MIS-10`, `EC-MIS-36`, `F-MISS-04.k5`), sehingga `sourceRules` memuat ID aturan PRD itu langsung.
- Data:
  - DU-047-1: Storage client: kuota 50.0 GB, usage 50.0 GB; varian kedua usage 51.2 GB dengan kuota 50.0 GB; varian ketiga client tanpa kuota dengan usage 50.0 GB.
  - DU-047-2: Record Missing `Camera DSLR Canon R6 {runId}`, aset tanpa TAG, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `—`, Condition `Normal`.
  - DU-047-3: Record Missing `Laptop Dell Latitude 5420 {runId}`, aset tanpa TAG, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `—`, Condition sebelum laporan `Normal`.
  - DU-047-4: Record Missing `Printer HP LaserJet M404 {runId}`, aset tanpa TAG, Group `Head Office`, Status `Missing`, Condition sebelum laporan `Damaged`, dengan satu Damage record yang ditahan (aset tampil `Damaged + Missing`).
  - DU-047-5: Photo `foto-ditemukan.png` (PNG, di bawah 1 MB).
  - DU-047-6: Damaged Photo `foto-kerusakan-laptop.png` dan Note `Layar retak dan engsel patah saat ditemukan` untuk DU-047-3.
  - DU-047-7: Damaged Photo `foto-kerusakan-printer.png` dan Note `Rumah printer retak sejak sebelum hilang` untuk DU-047-4.
- Kondisi:
  - Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE kuota dan usage ledger Storage client (usage 50.0 GB, usage 51.2 GB, client tanpa kuota), dengan pemulihan di akhir spec.
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - Jeda 5 detik pada asersi toast persisten adalah pilihan spec (lebih lama dari auto-hide toast sukses), bukan nilai PRD.
  - State global yang diubah: kuota dan usage Storage client; suite berjalan serial.

## Test Steps

### Storage penuh menolak Mark as Found Normal dengan Photo baru
1. Fixture BE menetapkan usage Storage client 50.0 GB dengan kuota 50.0 GB hingga tersimpan, lalu muat ulang halaman Missing
2. Ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
3. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` menampilkan `Missing`
4. Buka menu `⋯` pada baris `Camera DSLR Canon R6 {runId}`, lalu klik `Mark as Found`
5. Pilih Asset Status `Normal`
6. Pilih berkas `foto-ditemukan.png` pada Photo
7. Verifikasi tombol `[Mark as Found]` pada dialog tidak Disabled
8. Klik `[Mark as Found]` pada dialog
9. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (50.0 GB of 50.0 GB used).` tampil
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi toast Error tidak hilang otomatis
12. Verifikasi dialog `Mark as Found` tetap terbuka
13. Verifikasi Photo `foto-ditemukan.png` masih terpilih pada dialog
14. Verifikasi Asset Status tetap `Normal`
15. Tutup toast Error
16. Klik `[Cancel]` pada dialog `Mark as Found`
17. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` tetap `Missing` di sub-tab Active
18. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
19. Verifikasi dialog Missing Log tidak memuat node `Marked as found by`
20. Klik `✕` pada dialog Missing Log

### Nilai pada toast memakai format Size saat usage melebihi kuota
21. Fixture BE menetapkan usage Storage client 51.2 GB dengan kuota 50.0 GB hingga tersimpan
22. Buka menu `⋯` pada baris `Camera DSLR Canon R6 {runId}`, klik `Mark as Found`, pilih Asset Status `Normal`, lalu pilih berkas `foto-ditemukan.png` pada Photo
23. Klik `[Mark as Found]` pada dialog, lalu verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tampil
24. Tutup toast Error
25. Klik `[Cancel]` pada dialog `Mark as Found`
26. Fixture BE mengembalikan usage Storage client 50.0 GB dengan kuota 50.0 GB hingga tersimpan

### Damaged Photo wajib tidak dikecualikan dari blokir Storage penuh
27. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
28. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`, lalu klik `Mark as Found`
29. Pilih Asset Status `Damaged`
30. Verifikasi label `Damaged Photo` tampil pada isian foto
31. Pilih berkas `foto-kerusakan-laptop.png` pada Damaged Photo
32. Isi Note `Layar retak dan engsel patah saat ditemukan`
33. Verifikasi tombol `[Mark as Found]` pada dialog tidak Disabled
34. Klik `[Mark as Found]` pada dialog
35. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (50.0 GB of 50.0 GB used).` tampil
36. Verifikasi dialog `Mark as Found` tetap terbuka
37. Verifikasi Damaged Photo `foto-kerusakan-laptop.png` masih terpilih pada dialog
38. Verifikasi Note tetap `Layar retak dan engsel patah saat ditemukan`
39. Tutup toast Error, lalu klik `[Cancel]` pada dialog `Mark as Found`
40. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` tetap `Missing` di sub-tab Active
41. Buka Damage Log milik aset `Laptop Dell Latitude 5420 {runId}`
42. Verifikasi Damage Log tidak memuat Damage Report dengan Source `Missing Asset`

### Asal Damaged + Missing: tidak ada node baru pada Damage record yang ditahan
43. Buka halaman `Assets`, klik tab `Missing`
44. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
45. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`, lalu klik `Mark as Found`
46. Verifikasi Asset Status terisi `Damaged` dan disabled
47. Pilih berkas `foto-kerusakan-printer.png` pada Damaged Photo
48. Isi Note `Rumah printer retak sejak sebelum hilang`
49. Klik `[Mark as Found]` pada dialog
50. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (50.0 GB of 50.0 GB used).` tampil
51. Verifikasi dialog `Mark as Found` tetap terbuka dengan Damaged Photo `foto-kerusakan-printer.png` dan Note `Rumah printer retak sejak sebelum hilang` tidak direset
52. Tutup toast Error, lalu klik `[Cancel]` pada dialog `Mark as Found`
53. Buka Damage Log milik aset `Printer HP LaserJet M404 {runId}`
54. Verifikasi Damage Log hanya memuat Damage record yang ditahan, tanpa node baru dengan foto `foto-kerusakan-printer.png`

### Tanpa Photo tidak dicek, client tanpa kuota tidak diblokir
55. Buka halaman `Assets`, klik tab `Missing`, ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
56. Buka menu `⋯` pada baris `Camera DSLR Canon R6 {runId}`, klik `Mark as Found`, pilih Asset Status `Normal`, lalu klik `[Mark as Found]` pada dialog tanpa memilih Photo
57. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name record `Camera DSLR Canon R6 {runId}`
58. Fixture BE menjadikan Storage client tanpa kuota dengan usage 50.0 GB hingga tersimpan
59. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
60. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`, lalu klik `Mark as Found`
61. Pilih berkas `foto-kerusakan-printer.png` pada Damaged Photo
62. Isi Note `Rumah printer retak sejak sebelum hilang`
63. Klik `[Mark as Found]` pada dialog
64. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name record `Printer HP LaserJet M404 {runId}`
65. Fixture BE memulihkan Storage client ke kuota dan usage awal

## Notes
- Aturan tidak punya TestCase sumber. Keterlacakan lewat ID aturan PRD `missing.md` (§1.2 `MISS-LOGIC-10a` s.d. `10f`, §6 `V-16`, §7.3 `TS-MIS-10`, §9.4.4 `EC-MIS-36`, `F-MISS-04.k5`); halaman coverage dan inventaris unit perlu dibangkitkan ulang agar memuat ID ini.
- Urutan evaluasi `format dan ukuran lolos dahulu` (`EC-MIS-36`) tidak dapat dipicu lewat UI: picker hanya menerima PNG / JPG / JPEG dan file besar di-resize otomatis tanpa pesan error (PRD §9.9), sehingga tidak diasersi.
- Langkah penghubung: langkah 1, 21, 26, 58, dan 65 mengatur state Storage lewat fixture BE; langkah 10 adalah jeda 5 detik; langkah 15, 24, 39, dan 52 menutup toast Error.
- Spec memakai satu aset per jalur supaya record yang ditolak tetap `Missing` dan dapat dipakai ulang pada langkah berikutnya.
- Dialog `Mark as Found` dan tombol `[Cancel]` pada footer mengikuti spec TC-FA-MISS-E2E-046.
