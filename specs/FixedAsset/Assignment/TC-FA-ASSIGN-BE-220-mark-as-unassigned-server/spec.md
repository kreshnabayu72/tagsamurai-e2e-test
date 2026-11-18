---
id: TC-FA-ASSIGN-BE-220-mark-as-unassigned-server
title: "Wind-down Mark as Unassigned pada level None di server"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-20b", "ASSIGN-LOGIC-20c", "ASSIGN-LOGIC-20d", "ASSIGN-LOGIC-20e", "ASSIGN-LOGIC-20f", "ASSIGN-LOGIC-20g", "ASSIGN-LOGIC-20h", "ASSIGN-LOGIC-20i", "ASSIGN-LOGIC-20j", "ASSIGN-LOGIC-20k", "ASSIGN-LOGIC-20l", "ASSIGN-LOGIC-20m", "ASSIGN-LOGIC-20n", "ASSIGN-LOGIC-20o", "ASSIGN-LOGIC-20p", "ASSIGN-LOGIC-20q", "ASSIGN-LOGIC-20r", "ASSIGN-LOGIC-20s", "ASSIGN-LOGIC-20t", "ASSIGN-LOGIC-20u", "ASSIGN-LOGIC-20v", "ASSIGN-LOGIC-20w", "ASSIGN-LOGIC-20x", "ASSIGN-LOGIC-20y", "ASSIGN-LOGIC-20z", "ASSIGN-LOGIC-20aa", "ASSIGN-LOGIC-20ab", "ASSIGN-LOGIC-20ac", "ASSIGN-LOGIC-20ad"]
smoke: []
dependsOn: []
owner: BE
trace:
  "ASSIGN-LOGIC-20b": [4, 56]
  "ASSIGN-LOGIC-20c": [2, 4]
  "ASSIGN-LOGIC-20d": 13
  "ASSIGN-LOGIC-20e": [13, 44, 46, 48]
  "ASSIGN-LOGIC-20f": [9, 50]
  "ASSIGN-LOGIC-20g": 30
  "ASSIGN-LOGIC-20h": 30
  "ASSIGN-LOGIC-20i": 32
  "ASSIGN-LOGIC-20j": 28
  "ASSIGN-LOGIC-20k": [9, 30]
  "ASSIGN-LOGIC-20l": 11
  "ASSIGN-LOGIC-20m": 11
  "ASSIGN-LOGIC-20n": 7
  "ASSIGN-LOGIC-20o": [11, 26]
  "ASSIGN-LOGIC-20p": [19, 21]
  "ASSIGN-LOGIC-20q": [25, 54]
  "ASSIGN-LOGIC-20r": 27
  "ASSIGN-LOGIC-20s": 26
  "ASSIGN-LOGIC-20t": 38
  "ASSIGN-LOGIC-20u": 40
  "ASSIGN-LOGIC-20v": 16
  "ASSIGN-LOGIC-20w": [17, 52]
  "ASSIGN-LOGIC-20x": 11
  "ASSIGN-LOGIC-20y": 34
  "ASSIGN-LOGIC-20z": 32
  "ASSIGN-LOGIC-20aa": 36
  "ASSIGN-LOGIC-20ab": [14, 15, 42]
  "ASSIGN-LOGIC-20ac": 28
  "ASSIGN-LOGIC-20ad": 23
---

# Wind-down Mark as Unassigned pada level None di server

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Hendra Kusuma {runId}` (Asset Admin, juga Assignee Employee dan PIC `Finance {runId}`); `Lina Marlina {runId}` (Asset Admin lain); `Citra Dewi {runId}` (PIC Division tanpa Role Assignment); Assignee Employee `Budi Santoso {runId}` ber-akun login; Total Control `Taufik Hidayat {runId}`; Group Manager `Wahyu Hidayat {runId}` (cakupan Group `Head Office {runId}`); `Agus Pratama {runId}` (Asset Admin, cakupan Group `Branch Surabaya {runId}`). Semua langkah berjalan di entitas ber-Feature Suite Assignment level `None` kecuali yang menyebut level `Full`.
- Data:
  - DU-220-1: User, Aktor Assignment dalam cakupan Group aset: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-220-2: User, Aktor Assignment yang juga Assignee Employee dan PIC Division: Nama `Hendra Kusuma {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`, PIC Division `Finance {runId}`.
  - DU-220-3: User, Aktor Assignment lain yang memproses: Nama `Lina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-220-4: User, PIC Division tanpa hak Aktor Assignment: Nama `Citra Dewi {runId}`, Role `tanpa Role Assignment`, Cakupan Group `Head Office {runId}`.
  - DU-220-5: Assignment, ASG dengan baris Assigned untuk hasil Unassigned: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Acer Swift {runId}`, Status baris `Assigned`, Reason `Plan turun ke level None`.
  - DU-220-6: Assignment, ASG dengan baris Assigned yang punya laporan Damaged aktif: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Sony Alpha {runId}`, Status baris `Assigned`, Laporan `Damaged, Waiting for Confirmation`.
  - DU-220-7: Assignment, ASG dengan baris Assigned untuk hasil Missing: Assignee `Fani Rahmawati {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Status baris `Assigned`.
  - DU-220-8: Assignment, ASG dengan baris Assigned untuk hasil Damaged: Assignee `Gani Mahendra {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor Epson EB {runId}`, Status baris `Assigned`, Reason `Lensa retak`.
  - DU-220-9: Assignment, ASG dengan dua baris Assigned dan satu baris yang bukan Assigned untuk Bulk: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor LG UltraWide {runId}`, Baris 2 `Monitor Dell P2422 {runId}`, Baris 3 `Printer HP LaserJet {runId}`, Status baris 1 `Assigned`, Status baris 2 `Assigned`, Status baris 3 `Unassigned`.
  - DU-220-10: Assignment, ASG dengan baris Assigned yang Assignee-nya adalah Aktor sendiri: Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell XPS {runId}`, Status baris `Assigned`.
  - DU-220-11: Assignment, ASG Division dengan baris Assigned yang PIC-nya adalah Aktor sendiri: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Honda EU {runId}`, Status baris `Assigned`, PIC `Hendra Kusuma {runId}`.
  - DU-220-12: Assignment, ASG dengan baris Assigned yang terkunci pada level None: Assignee `Indra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Genset Cummins {runId}`, Status baris `Assigned`.
  - DU-220-13: Assignment, ASG dengan baris Assigned pada entitas level Full: Assignee `Joko Susilo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker Polytron {runId}`, Status baris `Assigned`.
  - DU-220-14: Assignment, ASG dengan baris yang ditutup otomatis di T-0: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Staff {runId}`, Status baris `Canceled`, Alasan `Assignment not available on plan`.
  - DU-220-15: Assignment, ASG dengan baris Assigned yang punya laporan Missing aktif: Assignee `Lutfi Hakim {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Scanner Epson DS {runId}`, Status baris `Assigned`, Laporan `Missing, Waiting for Confirmation`.
  - DU-220-16: User, Total Control: Nama `Taufik Hidayat {runId}`, Role `Total Control`, Cakupan Group `semua Group`.
  - DU-220-17: User, Group Manager dalam cakupan Group aset: Nama `Wahyu Hidayat {runId}`, Role `Group Manager`, Cakupan Group `Head Office {runId}`.
  - DU-220-18: User, Aktor Assignment di luar cakupan Group aset: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Branch Surabaya {runId}`.
  - DU-220-19: Assignment, ASG dengan tiga baris Assigned untuk pelaku berbeda: Assignee `Mario Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Direksi {runId}`, Baris 2 `Sofa Tamu Informa {runId}`, Baris 3 `Lemari Brankas {runId}`, Status baris `Assigned`.
  - DU-220-20: Assignment, ASG Division dengan baris Assigned yang PIC-nya bukan Aktor Assignment: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Perkins {runId}`, Status baris `Assigned`, PIC `Citra Dewi {runId}`.
- Kondisi:
  - Feature Suite Assignment pada entitas langkah bernilai `None`, kecuali langkah yang menyebut level `Full`.

## Test Steps

### Hanya level None, hanya aset Assigned, dan hanya Aktor Assignment
1. Rina menjalankan `Mark as Unassigned` untuk baris `Speaker Polytron {runId}` pada DU-220-13 di entitas level `Full`
2. Verifikasi permintaan ditolak karena `Mark as Unassigned` tersedia hanya pada level `None`
3. Rina mengirim `Mark as Unassigned` untuk baris `Kursi Staff {runId}` pada DU-220-14 yang sudah ditutup `Canceled`
4. Verifikasi permintaan ditolak karena hanya aset ber-Custody `Assigned` yang dapat diproses dan tidak ada aksi Cancel untuk baris menunggu karena sudah ditutup otomatis di T-0
5. Rina memverifikasi tag baris `Speaker Polytron {runId}` pada halaman Unassign di entitas level `Full`
6. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Joko Susilo {runId}`
7. Verifikasi Unassign pada level `Full` tetap mengikuti aturan Unassign tanpa pilihan hasil manual sehingga baris `Unassigned` tanpa marker
8. Assignee `Budi Santoso {runId}` mengirim `Mark as Unassigned` langsung ke server untuk baris `Laptop Acer Swift {runId}` pada DU-220-5
9. Verifikasi permintaan ditolak server karena Assignee tidak dapat memulai aksi ini dan baris `Laptop Acer Swift {runId}` tetap `Assigned`

### Hasil Unassigned dengan Reason opsional
10. Rina menjalankan `Mark as Unassigned` untuk baris `Laptop Acer Swift {runId}` dari aksi baris pada daftar aset tanpa memilih hasil dan tanpa scan atau foto
11. Verifikasi pilihan hasil bernilai default `Unassigned` dan baris `Laptop Acer Swift {runId}` berstatus `Unassigned` dengan Custody `Available`
12. Rina menjalankan `Mark as Unassigned` untuk baris `Kamera Sony Alpha {runId}` dari aksi header pada halaman detail aset dengan Reason `Plan turun ke level None`
13. Verifikasi aksi dapat dijalankan dari aksi baris, aksi bulk, dan aksi header oleh Aktor Assignment dalam cakupan Group aset
14. Verifikasi baris `Kamera Sony Alpha {runId}` berstatus `Unassigned` dengan marker `Damaged` yang mengikuti record aktif aset
15. Verifikasi baris `Laptop Acer Swift {runId}` berstatus `Unassigned` tanpa marker karena tidak ada record aktif
16. Verifikasi Assignment Log baris `Laptop Acer Swift {runId}` memuat node `Unassigned by [pelaku]` dengan penanda `Plan change`
17. Verifikasi Assignee `Budi Santoso {runId}` menerima notifikasi `assignment_unassigned` varian Plan change

### Hasil Missing dan Damaged lewat aksi per aset
18. Rina menjalankan `Mark as Unassigned` untuk baris `Tablet iPad {runId}` pada DU-220-7 dengan hasil `Missing`
19. Verifikasi baris `Tablet iPad {runId}` ditutup `Unassigned` dengan marker `Missing` dan laporan dibuat mengikuti aturan Report Missing saat ditugaskan
20. Rina menjalankan `Mark as Unassigned` untuk baris `Proyektor Epson EB {runId}` pada DU-220-8 dengan hasil `Damaged` dan Reason `Lensa retak`
21. Verifikasi baris `Proyektor Epson EB {runId}` ditutup `Unassigned` dengan marker `Damaged` dan laporan dibuat mengikuti aturan Report Damaged saat ditugaskan
22. Rina menjalankan Bulk `Mark as Unassigned` dengan hasil `Missing` untuk baris `Monitor LG UltraWide {runId}` pada DU-220-9
23. Verifikasi hasil `Missing` atau `Damaged` ditolak pada Bulk dan hanya tersedia lewat aksi per aset

### Bulk Mark as Unassigned dan aset penugasan sendiri
24. Hendra menjalankan Bulk `Mark as Unassigned` untuk baris `Monitor LG UltraWide {runId}`, `Monitor Dell P2422 {runId}`, `Printer HP LaserJet {runId}`, `Laptop Dell XPS {runId}`, dan `Genset Honda EU {runId}` pada DU-220-9, DU-220-10, dan DU-220-11
25. Verifikasi Bulk tersedia karena sedikitnya satu aset terpilih berstatus `Assigned`
26. Verifikasi baris `Monitor LG UltraWide {runId}` dan `Monitor Dell P2422 {runId}` berstatus `Unassigned` dengan hasil selalu `Unassigned`
27. Verifikasi baris `Printer HP LaserJet {runId}` yang bukan `Assigned`, baris `Laptop Dell XPS {runId}` milik Hendra sebagai Assignee, dan baris `Genset Honda EU {runId}` milik Hendra sebagai PIC dilewati
28. Verifikasi caption skipped menghitung terpisah `1` aset yang bukan `Assigned` dan `2` aset milik Aktor sendiri
29. Hendra mengirim `Mark as Unassigned` langsung ke server untuk baris `Laptop Dell XPS {runId}` yang Assignee-nya adalah Hendra
30. Verifikasi permintaan ditolak server karena `Mark as Unassigned` tidak diizinkan atas aset penugasan sendiri dan baris tetap `Assigned`
31. Hendra mengirim `Mark as Unassigned` langsung ke server untuk baris `Genset Honda EU {runId}` pada DU-220-11 sebagai PIC `Finance {runId}`
32. Verifikasi permintaan ditolak server karena `Mark as Unassigned` tidak diizinkan bagi PIC Division aset itu dan baris `Genset Honda EU {runId}` tetap `Assigned`
33. Lina menjalankan `Mark as Unassigned` untuk baris `Laptop Dell XPS {runId}`
34. Verifikasi baris `Laptop Dell XPS {runId}` berstatus `Unassigned` karena Aktor Assignment lain yang memproses
35. Hendra menjalankan Bulk `Mark as Unassigned` hanya untuk baris `Genset Honda EU {runId}` yang semuanya miliknya sendiri
36. Verifikasi permintaan ditolak dengan pesan `Error, you can't unassign your own assigned assets.` tanpa dialog hasil

### Aset Assigned tetap terkunci dan laporan hanya lewat hasil Mark as Unassigned
37. Rina mengirim permintaan `Transfer`, `Dispose`, dan `Borrow` untuk baris `Genset Cummins {runId}` pada DU-220-12 yang masih `Assigned`
38. Verifikasi ketiga permintaan ditolak sampai aset di-Mark as Unassigned
39. Rina melaporkan baris `Genset Cummins {runId}` hilang atau rusak dari halaman Assignment
40. Verifikasi permintaan ditolak karena laporan untuk aset Assigned pada level None hanya lewat hasil `Mark as Unassigned`

### Marker Missing mengikuti record Missing aktif
41. Rina menjalankan `Mark as Unassigned` untuk baris `Scanner Epson DS {runId}` pada DU-220-15 tanpa memilih hasil
42. Verifikasi baris `Scanner Epson DS {runId}` berstatus `Unassigned` dengan marker `Missing` yang mengikuti laporan hilang aktif aset itu

### Pelaku Total Control dan Group Manager diterima, Aktor di luar cakupan Group aset ditolak
43. Taufik menjalankan `Mark as Unassigned` untuk baris `Meja Direksi {runId}` pada DU-220-19
44. Verifikasi baris `Meja Direksi {runId}` berstatus `Unassigned` karena Total Control termasuk Aktor Assignment
45. Wahyu menjalankan `Mark as Unassigned` untuk baris `Sofa Tamu Informa {runId}` pada DU-220-19
46. Verifikasi baris `Sofa Tamu Informa {runId}` berstatus `Unassigned` karena Group Manager berada dalam cakupan Group aset
47. Agus mengirim `Mark as Unassigned` langsung ke server untuk baris `Lemari Brankas {runId}` pada DU-220-19
48. Verifikasi permintaan ditolak server karena cakupan Agus tidak meliputi Group `Head Office {runId}` dan baris `Lemari Brankas {runId}` tetap `Assigned`

### PIC bukan Aktor Assignment ditolak dan PIC menerima notifikasi
49. PIC `Citra Dewi {runId}` mengirim `Mark as Unassigned` langsung ke server untuk baris `Genset Perkins {runId}` pada DU-220-20
50. Verifikasi permintaan ditolak server karena PIC tidak dapat memulai aksi ini dan baris `Genset Perkins {runId}` tetap `Assigned`
51. Rina menjalankan `Mark as Unassigned` untuk baris `Genset Perkins {runId}`
52. Verifikasi baris `Genset Perkins {runId}` berstatus `Unassigned` dan PIC `Citra Dewi {runId}` menerima notifikasi `assignment_unassigned` varian Plan change

### Bulk tanpa aset Assigned
53. Rina menjalankan Bulk `Mark as Unassigned` untuk baris `Printer HP LaserJet {runId}` pada DU-220-9 dan `Kursi Staff {runId}` pada DU-220-14 yang tidak berstatus `Assigned`
54. Verifikasi Bulk ditolak karena tidak ada aset terpilih yang berstatus `Assigned`

### Tidak ada aksi Cancel untuk baris menunggu pada level None
55. Rina mengirim permintaan Cancel Assignment langsung ke server untuk baris `Kursi Staff {runId}` pada DU-220-14 di entitas level `None`
56. Verifikasi permintaan ditolak dan baris `Kursi Staff {runId}` tetap `Canceled` dengan alasan `Assignment not available on plan`
