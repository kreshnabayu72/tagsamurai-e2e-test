---
id: TC-FA-ASSIGN-BE-218-plan-gating-server
title: "Plan gating server: level Full, Basic, None dan penutupan T-0"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.10#p1", "§9.10#r1", "§9.10#r2", "§9.10#r3", "§9.10#r4", "§9.10#r5", "§9.10#r6", "§9.10#r7", "§9.10#r8", "§9.10#r9", "§9.10#r10", "§9.10#r11", "§9.10#r12", "§9.10#r13", "§9.10#r14", "§9.10#r15", "§9.10#p9", "§9.10#r29", "§9.10#r30", "§9.10#r31", "§9.10#r32", "EC-ASG-105", "EC-ASG-114", "ASSIGN-LOGIC-18b", "ASSIGN-LOGIC-18c", "ASSIGN-LOGIC-18g", "ASSIGN-LOGIC-18h", "ASSIGN-LOGIC-18i", "ASSIGN-LOGIC-18j", "ASSIGN-LOGIC-18k", "ASSIGN-LOGIC-18l", "ASSIGN-LOGIC-18m", "ASSIGN-LOGIC-18o", "ASSIGN-LOGIC-18p", "ASSIGN-LOGIC-18q", "ASSIGN-LOGIC-18r", "ASSIGN-LOGIC-18s", "ASSIGN-LOGIC-18t", "ASSIGN-LOGIC-18u", "ASSIGN-LOGIC-18v", "ASSIGN-LOGIC-18w", "ASSIGN-LOGIC-18y", "ASSIGN-LOGIC-18z", "ASSIGN-LOGIC-18aa", "ASSIGN-LOGIC-18ab", "ASSIGN-LOGIC-18ac", "ASSIGN-LOGIC-18ad"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.10#p1": 2
  "§9.10#r1": 2
  "§9.10#r2": [4, 60]
  "§9.10#r3": [6, 62]
  "§9.10#r4": [8, 64]
  "§9.10#r5": [4, 19, 77, 78, 80]
  "§9.10#r6": [4, 14, 17, 77]
  "§9.10#r7": [17, 20]
  "§9.10#r8": [14, 78]
  "§9.10#r9": 24
  "§9.10#r10": 11
  "§9.10#r11": 28
  "§9.10#r12": 28
  "§9.10#r13": 30
  "§9.10#r14": [32, 84]
  "§9.10#r15": 20
  "§9.10#p9": 50
  "§9.10#r29": [56, 95]
  "§9.10#r30": 35
  "§9.10#r31": [50, 51]
  "§9.10#r32": [58, 68, 69, 71]
  "EC-ASG-105": [2, 44]
  "EC-ASG-114": [24, 26]
  "ASSIGN-LOGIC-18b": [8, 60, 62, 64]
  "ASSIGN-LOGIC-18c": [9, 65]
  "ASSIGN-LOGIC-18g": [2, 44]
  "ASSIGN-LOGIC-18h": 45
  "ASSIGN-LOGIC-18i": 46
  "ASSIGN-LOGIC-18j": 50
  "ASSIGN-LOGIC-18k": 50
  "ASSIGN-LOGIC-18l": 52
  "ASSIGN-LOGIC-18m": 53
  "ASSIGN-LOGIC-18o": 11
  "ASSIGN-LOGIC-18p": [22, 73]
  "ASSIGN-LOGIC-18q": 35
  "ASSIGN-LOGIC-18r": 24
  "ASSIGN-LOGIC-18s": [24, 26]
  "ASSIGN-LOGIC-18t": [24, 26]
  "ASSIGN-LOGIC-18u": [36, 87, 90, 93]
  "ASSIGN-LOGIC-18v": 9
  "ASSIGN-LOGIC-18w": 9
  "ASSIGN-LOGIC-18y": 54
  "ASSIGN-LOGIC-18z": 51
  "ASSIGN-LOGIC-18aa": 48
  "ASSIGN-LOGIC-18ab": 33
  "ASSIGN-LOGIC-18ac": 24
  "ASSIGN-LOGIC-18ad": [38, 40, 42, 67]
---

# Plan gating server: level Full, Basic, None dan penutupan T-0

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}` dan `Branch Surabaya {runId}`); Approver `Mira Handayani {runId}` (cakupan Group `Head Office {runId}`); Assignee Employee dan PIC ber-akun login seperti di entri data; level Feature Suite Assignment tiap langkah menyebut slot plan atau level entitas yang dipakai.
- Data:
  - DU-218-1: User, Aktor Assignment dengan cakupan dua Group: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId} dan Branch Surabaya {runId}`.
  - DU-218-2: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-218-3: Asset, Aset Available untuk pengajuan di entitas slot free, paid_1, paid_2, dan paid_3: Nama 1 `Laptop Asus Zenbook {runId}`, Nama 2 `Laptop HP EliteBook {runId}`, Nama 3 `Laptop Dell Inspiron {runId}`, Nama 4 `Laptop Lenovo ThinkPad {runId}`, Custody `Available`, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`.
  - DU-218-4: Asset, Aset Available untuk pengajuan Assignee Division dan form dua Group di level Basic: Nama aset Division `Genset Kohler {runId}`, Nama aset Head Office `Meja Kerja A {runId}`, Nama aset Branch Surabaya `Meja Kerja B {runId}`, Custody `Available`, Assignee Division `Finance {runId}`, PIC `Hendra Kusuma {runId}`, Assignee Employee `Citra Dewi {runId}`.
  - DU-218-5: Assignment, ASG Employee di level Basic untuk Handover dengan konfirmasi, Unassign, dan Cancel: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Epson L3250 {runId}`, Baris 2 `Proyektor BenQ MX {runId}`, Baris 3 `Speaker JBL {runId}`, Baris 4 `Mouse Logitech MX {runId}`, Baris 5 `Keyboard Logitech K380 {runId}`, Status baris 1 `Waiting for Handover`, Status baris 2 `Assigned`, Status baris 3 `Waiting for Handover`, Status baris 4 `Assigned`, Status baris 5 `Assigned`, Need recipient confirmation `Yes`, PIC `tidak ada`, PIC pengganti `Wati Susanti {runId}`, What happened laporan `Tombol macet`, Foto laporan `satu foto`.
  - DU-218-6: Assignment, ASG Employee di level Basic yang di-Cancel dengan Save as Draft to edit dan yang melewati Transaction timeout: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor Dell P2422 {runId}`, Baris 2 `Kulkas Sharp {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, ASG dibuat saat level `Full`.
  - DU-218-7: Aset, Aset Available untuk pengajuan di level Basic dengan Require approval ON: Nama `Kamera Canon EOS {runId}`, Custody `Available`, Assignee `Fajar Nugroho {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Require approval `ON`, Approver `Mira Handayani {runId}`, Approval Workflow `tersedia di plan`.
  - DU-218-8: Assignment, ASG Division yang sudah berjalan saat downgrade Full ke Basic: menunggu approval, menunggu handover, dan Assigned: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Printer Canon G3010 {runId}`, Baris 2 `Genset Honda EU {runId}`, Baris 3 `Genset Perkins {runId}`, Status baris 1 `Waiting for Approval`, Status baris 2 `Waiting for Handover`, Status baris 3 `Assigned`, PIC `Hendra Kusuma {runId}`, PIC pengganti `Wati Susanti {runId}`, Need recipient confirmation snapshot baris 2 `No`, Override Asset Need recipient confirmation baris 2 setelah pengajuan `Yes`.
  - DU-218-9: Assignment, ASG Division yang berjalan dengan No PIC saat downgrade Full ke Basic: Assignee `Pemasaran {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Proyektor Hitachi {runId}`, Status baris `Waiting for Handover`, PIC `Novi Andriani {runId}, dinonaktifkan`, PIC pengganti `Yanti Susanti {runId}`.
  - DU-218-10: Draft, Draft yang ada saat downgrade ke Basic atau None: Assignee `Gani Mahendra {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Meja Rapat Olympic {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-218-11: Assignment, ASG yang berjalan saat downgrade ke None: menunggu approval, menunggu handover dengan sesi konfirmasi aktif, dan Assigned: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor Samsung S27 {runId}`, Baris 2 `Laptop Lenovo V14 {runId}`, Baris 3 `Kamera Sony Alpha {runId}`, Status baris 1 `Waiting for Approval`, Status baris 2 `Waiting for Handover`, Status baris 3 `Assigned`, Sesi Confirm Handover baris 2 `aktif`, Need recipient confirmation `Yes`, Need recipient confirmation tersimpan `Yes`, Pengaju `Rina Wijaya {runId}`.
  - DU-218-12: Assignment, ASG Assigned di level None yang diselesaikan lewat Mark as Unassigned: Assignee `Indra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Status baris `Assigned`.
  - DU-218-13: Asset, Tiga aset Available untuk Save Draft per slot plan: Nama paid_1 `Monitor Philips 243V {runId}`, Nama paid_2 `Monitor LG 24MP {runId}`, Nama paid_3 `Monitor AOC 22B {runId}`, Custody `Available`, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`.
  - DU-218-14: Asset, Aset Available untuk Save Draft sesudah upgrade kembali ke Full: Nama `Meja Kerja C {runId}`, Custody `Available`, Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`.
  - DU-218-15: Asset, Aset Available untuk pengajuan di level Basic dengan Require approval OFF: Nama `Kamera Fujifilm X-T30 {runId}`, Custody `Available`, Assignee `Gunawan Wibisono {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Require approval `OFF`.
  - DU-218-16: Assignment, ASG Employee di level Basic dengan dua baris Waiting for Handover untuk handover sebagian: Assignee `Hendri Gunawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Rapat Jati {runId}`, Baris 2 `Kursi Rapat Jati {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-218-18: Draft, Draft yang ada di entitas yang memasuki T-30 menuju `Basic`: Assignee `Heru Santoso {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Lemari Besi Alba {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-218-19: Assignment, ASG berjalan di entitas yang memasuki T-30 menuju `Basic`: Assignee `Intan Permatasari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Lemari Pendingin Sanyo {runId}`, Status baris 1 `Waiting for Handover`, Baris 2 `Kipas Dinding Maspion {runId}`, Status baris 2 `Assigned`.
  - DU-218-20: Draft, Draft yang ada di entitas yang memasuki T-30 menuju `None`: Assignee `Joko Prasetyo {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Rak Piring Besi {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-218-21: Assignment, ASG berjalan di entitas yang memasuki T-30 menuju `None`: Assignee `Kartini Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mesin Kopi Delonghi {runId}`, Status baris 1 `Waiting for Handover`, Baris 2 `Blender Panasonic {runId}`, Status baris 2 `Assigned`.
- Kondisi:
  - Level Feature Suite Assignment per slot plan mengikuti tabel `plan_tier`: `free` bernilai `None`, `paid_1` bernilai `Basic`, `paid_2` dan `paid_3` bernilai `Full`.

## Test Steps

### Level Feature Suite Assignment mengikuti slot plan
1. Rina mengirim permintaan Submit atas aset `Laptop Asus Zenbook {runId}` pada DU-218-3 di entitas ber-slot plan `free`
2. Verifikasi permintaan ditolak dengan kode kesalahan `PLAN_FEATURE_UNAVAILABLE` karena slot `free` bernilai level `None`
3. Rina mengirim permintaan Submit atas aset `Laptop HP EliteBook {runId}` untuk Assignee Employee di entitas ber-slot plan `paid_1`
4. Verifikasi pengajuan diterima karena slot `paid_1` bernilai level `Basic`
5. Rina mengirim permintaan Submit atas aset `Laptop Dell Inspiron {runId}` untuk Assignee Employee di entitas ber-slot plan `paid_2`
6. Verifikasi pengajuan diterima karena slot `paid_2` bernilai level `Full`
7. Rina mengirim permintaan Submit atas aset `Laptop Lenovo ThinkPad {runId}` untuk Assignee Employee di entitas ber-slot plan `paid_3`
8. Verifikasi pengajuan diterima karena slot `paid_3` bernilai level `Full`
9. Verifikasi level aktif ditetapkan per slot plan tanpa toggle tersendiri dan nama plan tidak memengaruhi level

### Level Basic: fitur yang tersedia untuk Assignee Employee
10. Rina mengirim Submit satu form berisi aset `Meja Kerja A {runId}` Group `Head Office {runId}` dan `Meja Kerja B {runId}` Group `Branch Surabaya {runId}` untuk Assignee Employee `Citra Dewi {runId}` pada DU-218-4 di entitas level `Basic`
11. Verifikasi form multi-Group diterima dan dipecah otomatis menjadi satu ASG per Group
12. Rina memverifikasi tag baris `Printer Epson L3250 {runId}` pada DU-218-5 di entitas level `Basic`
13. Rina menekan `[Request Confirmation]` untuk baris `Printer Epson L3250 {runId}`
14. Verifikasi sesi konfirmasi terbentuk dan Assignee menerima Task `Confirm Handover` di entitas level `Basic`
15. Rina memverifikasi tag baris `Proyektor BenQ MX {runId}`
16. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Dedi Prasetyo {runId}` di entitas level `Basic`
17. Verifikasi baris `Proyektor BenQ MX {runId}` berstatus `Unassigned` dan riwayatnya muncul di History
18. Assignee `Dedi Prasetyo {runId}` melaporkan aset `Mouse Logitech MX {runId}` hilang di entitas level `Basic`
19. Verifikasi laporan hilang diterima untuk Assignee Employee di level `Basic` dan baris `Mouse Logitech MX {runId}` tetap `Assigned` dengan badge `Reported Missing`
20. Verifikasi daftar Assigned Assets By Asset dapat dibaca dan By Assignee tidak tersedia di entitas level `Basic`
21. Rina mengirim permintaan Submit atas aset `Kamera Canon EOS {runId}` untuk Assignee Employee `Fajar Nugroho {runId}` di entitas level `Basic` dengan Require approval `ON` pada DU-218-7
22. Verifikasi baris `Kamera Canon EOS {runId}` tetap `Waiting for Approval` karena approval mengikuti toggle Approval Workflow, terpisah dari level

### Level Basic: fitur terkunci ditolak server
23. Rina mengirim permintaan Submit langsung ke server dengan Assignee tipe `Division` `Finance {runId}` untuk aset `Genset Kohler {runId}` di entitas level `Basic`
24. Verifikasi permintaan ditolak server walau lolos dari UI dan tidak ada ASG yang dibuat
25. Rina mengirim permintaan Change PIC langsung ke server untuk ASG Assignee Employee `Dedi Prasetyo {runId}` pada DU-218-5 dengan PIC pengganti `Wati Susanti {runId}` di entitas level `Basic`
26. Verifikasi permintaan ditolak karena ASG itu tidak bertipe `Division` dan ASG itu tetap tanpa PIC
27. Rina mengirim permintaan Save Draft dan Add to Assignment Draft langsung ke server di entitas level `Basic`
28. Verifikasi kedua permintaan ditolak dan tidak ada Draft yang tersimpan, sehingga tab Drafts tidak memuat Draft
29. Rina membatalkan baris `Monitor Dell P2422 {runId}` pada DU-218-6 dengan `Save as Draft to edit` di entitas level `Basic`
30. Verifikasi baris berstatus `Canceled` tanpa Draft baru, juga untuk ASG yang dibuat saat Full
31. Waktu berlalu sampai baris `Kulkas Sharp {runId}` melewati Transaction timeout di entitas level `Basic`
32. Verifikasi baris `Kulkas Sharp {runId}` ditutup `Canceled` tanpa Draft baru
33. Verifikasi nilai tersimpan dan transaksi berjalan tidak berubah oleh fitur yang terkunci

### Downgrade Full ke Basic: Draft dihapus dan ASG Division berjalan lanjut
34. Entitas turun dari level `Full` ke `Basic` saat T-0 dengan Draft `Gani Mahendra {runId}` pada DU-218-10 dan ASG Assignee `Finance {runId}` pada DU-218-8 berjalan
35. Verifikasi semua Draft dihapus tanpa status akhir
36. Verifikasi ASG Assignee `Finance {runId}` yang berjalan (menunggu approval, menunggu handover, dan Assigned) lanjut normal dengan snapshot aturan saat diajukan
37. Rina mengganti PIC ASG `Finance {runId}` dari `Hendra Kusuma {runId}` menjadi `Wati Susanti {runId}` di entitas level `Basic`
38. Verifikasi Change PIC berhasil hanya untuk ASG itu
39. Rina mengganti PIC ASG `Pemasaran {runId}` pada DU-218-9 yang `No PIC` menjadi `Yanti Susanti {runId}` di entitas level `Basic`
40. Verifikasi Change PIC berhasil untuk ASG `No PIC` dan Handover tidak lagi terblokir
41. Entitas naik kembali ke level `Full`
42. Verifikasi upgrade kembali ke Full berlaku langsung

### Level None: aksi ditolak, riwayat dan wind-down tetap diizinkan
43. Rina mengirim permintaan Unassign langsung ke server untuk baris `Tablet iPad {runId}` pada DU-218-12 di entitas level `None`
44. Verifikasi permintaan ditolak dengan kode kesalahan `PLAN_FEATURE_UNAVAILABLE` dan baris `Tablet iPad {runId}` tetap `Assigned`
45. Verifikasi membaca riwayat dan log, `Mark as Unassigned`, serta job sistem tetap diizinkan
46. Verifikasi riwayat Assignment terbaca di Transaction log aset, Transaction admin log, dan User log di level `None`
47. Rina menekan `[Mark as Unassigned]` untuk baris `Tablet iPad {runId}` pada DU-218-12 di entitas level `None`
48. Verifikasi baris `Tablet iPad {runId}` berstatus `Unassigned` karena baris Assigned diselesaikan lewat `Mark as Unassigned`

### Downgrade ke None di T-0 menutup baris yang menunggu
49. Entitas turun ke level `None` saat T-0 dengan ASG Assignee `Hana Permatasari {runId}` pada DU-218-11 berjalan dan sesi Confirm Handover aktif pada baris `Laptop Lenovo V14 {runId}`
50. Verifikasi baris `Monitor Samsung S27 {runId}` dan `Laptop Lenovo V14 {runId}` berstatus `Canceled` oleh `System` dengan alasan `Assignment not available on plan`, tanpa Draft baru, dan Custody kembali `Available`
51. Verifikasi sesi Confirm Handover pada baris `Laptop Lenovo V14 {runId}` ikut batal dan Task `Confirm Handover` hilang
52. Verifikasi baris `Kamera Sony Alpha {runId}` tetap `Assigned` dan tidak ditutup otomatis
53. Verifikasi notifikasi auto-cancel di T-0 dikirim sekali ke pengaju `Rina Wijaya {runId}` dan Assignee `Hana Permatasari {runId}`
54. Verifikasi nilai Transaction Settings tab Assign yang tersimpan, termasuk Need recipient confirmation `Yes`, dipertahankan
55. Entitas yang akan turun ke level `Basic` memasuki T-30 dengan Draft `Heru Santoso {runId}` pada DU-218-18 dan ASG Assignee `Intan Permatasari {runId}` pada DU-218-19 berjalan
56. Verifikasi daftar langkah Assignment untuk turun ke `Basic` memuat Draft `Heru Santoso {runId}` dan tidak memuat ASG In Assignment Process maupun Assigned milik `Intan Permatasari {runId}`
57. Entitas yang sudah turun ke level `None` naik kembali ke level `Full` pada masa Grace
58. Verifikasi baris `Monitor Samsung S27 {runId}` dan `Laptop Lenovo V14 {runId}` yang sudah dibatalkan otomatis tidak dipulihkan

### Fitur khusus Full ditolak di paid_1 dan diterima di paid_2 dan paid_3
59. Rina mengirim permintaan Save Draft atas aset `Monitor Philips 243V {runId}` untuk Assignee Employee `Budi Santoso {runId}` di entitas ber-slot plan `paid_1` pada DU-218-13
60. Verifikasi permintaan Save Draft ditolak karena slot `paid_1` bernilai level `Basic` dan tidak ada Draft yang tersimpan
61. Rina mengirim permintaan Save Draft atas aset `Monitor LG 24MP {runId}` untuk Assignee Employee `Budi Santoso {runId}` di entitas ber-slot plan `paid_2` pada DU-218-13
62. Verifikasi Draft tersimpan karena slot `paid_2` bernilai level `Full`
63. Rina mengirim permintaan Save Draft atas aset `Monitor AOC 22B {runId}` untuk Assignee Employee `Budi Santoso {runId}` di entitas ber-slot plan `paid_3` pada DU-218-13
64. Verifikasi Draft tersimpan karena slot `paid_3` bernilai level `Full`
65. Verifikasi hasil Save Draft pada ketiga slot ditentukan oleh slot plan saja tanpa pengaturan tersendiri pada Assignment yang diubah

### Upgrade kembali ke Full berlaku langsung dan Draft yang dihapus tidak dipulihkan
66. Rina mengirim permintaan Save Draft atas aset `Meja Kerja C {runId}` untuk Assignee Employee `Citra Dewi {runId}` pada DU-218-14 di entitas yang sudah naik kembali ke level `Full`
67. Verifikasi Draft tersimpan karena upgrade kembali ke Full berlaku langsung
68. Verifikasi Draft `Gani Mahendra {runId}` pada DU-218-10 yang sudah dihapus saat downgrade tidak dipulihkan oleh upgrade kembali ke `Full`

### Rollback ke Full pada masa Grace: nilai tersimpan dan pengajuan ulang
69. Verifikasi nilai Transaction Settings tab Assign `Need recipient confirmation` `Yes` langsung berlaku pada entitas yang naik kembali ke level `Full`
70. Rina mengirim permintaan Submit atas aset `Monitor Samsung S27 {runId}` untuk Assignee `Hana Permatasari {runId}` pada DU-218-11 di entitas yang naik kembali ke level `Full`
71. Verifikasi pengajuan ulang diterima sebagai ASG baru karena pengajuan dibuat ulang bila masih dibutuhkan

### Basic: approval OFF langsung ke Waiting for Handover
72. Rina mengirim permintaan Submit atas aset `Kamera Fujifilm X-T30 {runId}` untuk Assignee Employee `Gunawan Wibisono {runId}` pada DU-218-15 di entitas level `Basic` dengan Require approval `OFF`
73. Verifikasi baris `Kamera Fujifilm X-T30 {runId}` berstatus `Waiting for Handover` dengan Approval `Not required`

### Basic: Confirm on This Device dan kontribusi ke tampilan Assignee
74. Rina memverifikasi tag baris `Speaker JBL {runId}` pada DU-218-5 di entitas level `Basic`
75. Rina menekan `[Request Confirmation]` untuk baris `Speaker JBL {runId}`
76. Rina menekan `Confirm on This Device` dengan pernyataan dicentang atas nama Assignee `Dedi Prasetyo {runId}`
77. Verifikasi baris `Speaker JBL {runId}` berstatus `Assigned` dengan Confirmation `Confirmed by [Aktor] on behalf of [Assignee]` di entitas level `Basic`
78. Verifikasi kontribusi Assignment ke tampilan Assignee `Dedi Prasetyo {runId}` di level `Basic` memuat baris `Speaker JBL {runId}` di tab `Assigned` dan baris `Proyektor BenQ MX {runId}` di tab `History`

### Basic: Report Damaged saat ditugaskan
79. Assignee `Dedi Prasetyo {runId}` melaporkan aset `Keyboard Logitech K380 {runId}` rusak dengan What happened `Tombol macet` dan satu foto di entitas level `Basic`
80. Verifikasi laporan rusak diterima untuk Assignee Employee di level `Basic` dan baris `Keyboard Logitech K380 {runId}` tetap `Assigned` dengan badge `Reported Damaged`

### Basic: sisa baris handover sebagian ditutup tanpa Draft
81. Rina memverifikasi tag baris `Meja Rapat Jati {runId}` pada DU-218-16 di entitas level `Basic`
82. Rina menekan `[Complete Handover]` untuk baris `Meja Rapat Jati {runId}` saja
83. Waktu berlalu sampai baris `Kursi Rapat Jati {runId}` melewati Transaction timeout sejak masuk `Waiting for Handover` di entitas level `Basic`
84. Verifikasi baris `Kursi Rapat Jati {runId}` berstatus `Canceled` dengan alasan `Not handed over` tanpa Draft baru

### Full ke Basic: ASG Division berjalan diselesaikan dengan snapshot saat diajukan
85. Rina mengubah override Asset `Genset Honda EU {runId}` pada DU-218-8 menjadi Need recipient confirmation `Yes` setelah pengajuan
86. Mira menyetujui baris `Printer Canon G3010 {runId}` di entitas level `Basic`
87. Verifikasi baris `Printer Canon G3010 {runId}` berstatus `Waiting for Handover`
88. Rina memverifikasi tag baris `Genset Honda EU {runId}`
89. Rina menekan `[Complete Handover]` untuk baris `Genset Honda EU {runId}`
90. Verifikasi baris `Genset Honda EU {runId}` berstatus `Assigned` tanpa sesi konfirmasi karena snapshot aturan saat diajukan memakai Need recipient confirmation `No`
91. Rina memverifikasi tag baris `Genset Perkins {runId}`
92. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Finance {runId}`
93. Verifikasi baris `Genset Perkins {runId}` berstatus `Unassigned`

### T-30 menuju level None
94. Entitas yang akan turun ke level `None` memasuki T-30 dengan Draft `Joko Prasetyo {runId}` pada DU-218-20 dan ASG Assignee `Kartini Lestari {runId}` pada DU-218-21 berjalan
95. Verifikasi daftar langkah Assignment untuk turun ke `None` memuat Draft `Joko Prasetyo {runId}` serta ASG In Assignment Process dan Assigned milik `Kartini Lestari {runId}`
