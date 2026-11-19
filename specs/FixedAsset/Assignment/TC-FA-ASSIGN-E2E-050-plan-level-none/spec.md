---
id: TC-FA-ASSIGN-E2E-050-plan-level-none
title: "Feature Suite Assignment level None"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#p5", "§9.10#r16", "§9.10#r17", "§9.10#r20", "§9.10#r21", "§9.10#r24", "§9.10#r25", "§9.10#r26", "EC-ASG-98", "EC-ASG-100", "ASSIGN-LOGIC-18d", "ASSIGN-LOGIC-18e", "ASSIGN-LOGIC-18f", "ASSIGN-LOGIC-18x"]
smoke: []
dependsOn: []
trace:
  "§9.10#p5": [4, 7]
  "§9.10#r16": [4, 5]
  "§9.10#r17": [9, 11]
  "§9.10#r20": 13
  "§9.10#r21": [22, 24, 25, 27, 29, 30, 32, 33]
  "§9.10#r24": 15
  "§9.10#r25": [17, 19]
  "§9.10#r26": 35
  "EC-ASG-98": [3, 30, 40, 43, 46, 48, 56, 57, 60]
  "EC-ASG-100": [48, 53]
  "ASSIGN-LOGIC-18d": [4, 5]
  "ASSIGN-LOGIC-18e": [7, 8]
  "ASSIGN-LOGIC-18f": [8, 9, 11]
  "ASSIGN-LOGIC-18x": 7
anchor: [23, 26, 28, 51]
coverage:
  web: automated
---

# Feature Suite Assignment level None

## Prerequisites
- Aktor: Total Control `Wulan Hartati {runId}` (DU-050-2), yang juga Assignee, di entitas khusus DU-050-1 yang tidak dipakai spec lain
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-050-1: Entitas (Entitas khusus dengan Feature Suite Assignment level Full yang akan turun ke None), Name `Entitas None {runId}`, Level Feature Suite Assignment `Full`, Level setelah downgrade `None`
  - DU-050-2: User (Aktor Total Control yang juga Assignee), Name `Wulan Hartati {runId}`, Role `Total Control`, Cakupan `Seluruh client`, Tampil sebagai Assignee `Wulan H`
  - DU-050-3: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-050-4: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-050-5: Group (Group utama), Name `Head Office {runId}`
  - DU-050-6: Draft (Draft yang dihapus saat downgrade), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-050-7: Assignment (ASG Waiting for Handover dengan sesi Confirm Handover aktif), Assignee `Wulan Hartati {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Sesi Confirm Handover `Aktif untuk Printer HP M404 {runId}`
  - DU-050-8: Assignment (ASG Waiting for Approval yang ditutup saat downgrade), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`
  - DU-050-9: Assignment (ASG Assigned milik Budi), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Camera Sony A7 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-050-10: Assignment (ASG Assigned milik aktor sebagai Assignee), Assignee `Wulan Hartati {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Scanner Canon DR-C225 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-050-11: Assignment (ASG Unassigned milik aktor sebagai Assignee untuk riwayat), Assignee `Wulan Hartati {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Unassigned`, Aset `Webcam Logitech C920 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-050-12: Assignment (ASG Assigned milik aktor dengan laporan Damaged dan Missing), Assignee `Wulan Hartati {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset 1 `Laptop Asus ExpertBook {runId}`, Aset 2 `Tablet Lenovo Tab M10 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Laporan Damaged `Laptop Asus ExpertBook {runId} dilaporkan oleh Wulan Hartati {runId}, Waiting for Confirmation`, Laporan Missing `Tablet Lenovo Tab M10 {runId} dilaporkan oleh Wulan Hartati {runId}, Waiting for Confirmation`
- Kondisi:
  - Feature Suite Assignment pada entitas berada pada level `Full` sebelum downgrade
  - Sesi Confirm Handover untuk aset `Printer HP M404 {runId}` aktif sebelum downgrade dan jendela konfirmasi Handover bernilai `15 menit` belum habis
  - Akun `Agus Prasetyo {runId}` dan `Budi Santoso {runId}` aktif, dan kredensial keduanya disediakan fase 2

## Test Steps

### Plan turun ke None dan penugasan yang menunggu ditutup otomatis
1. Catat jumlah notifikasi pada Bell icon aktor
2. Downgrade plan entitas ke level `None` berjalan di T-0
3. Verifikasi jumlah notifikasi pada Bell icon aktor bertambah satu untuk pembatalan otomatis ASG yang memuat aset `Printer HP M404 {runId}`

### Menu Assignment disabled dengan chip Upgrade
4. Verifikasi menu `Transactions > Assignment` tampil Disabled di sidebar
5. Verifikasi chip `Upgrade` tampil di sebelah menu `Transactions > Assignment`

### URL langsung tidak membuka fitur
6. Buka alamat halaman Assignment secara langsung
7. Verifikasi halaman Assignment tidak memuat isi modul Assignment dan fitur Assignment tidak dapat dipakai dari halaman itu
8. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tidak tampil

### Approvals, Quick Action, dan entri Assignment tidak tampil
9. Verifikasi menu `Approvals > Assignment` tidak tampil di sidebar
10. Klik Quick Action pada navbar
11. Verifikasi item `Assign` tidak tampil pada menu Quick Action

### Transaction Settings, Role & Permission, dan Reports pada level None
12. Buka halaman Transaction Settings
13. Verifikasi tab `Assign` tidak tampil
14. Buka halaman Role & Permission
15. Verifikasi pengaturan role Assignment tidak tampil
16. Buka halaman Reports
17. Verifikasi laporan Assignment tidak tampil
18. Buka halaman Dashboard
19. Verifikasi widget Assignment tidak tampil

### My Asset pada level None
20. Buka menu Profile pada navbar
21. Klik `My Asset`
22. Verifikasi item `My Asset` tampil karena masih ada penugasan berjalan
23. Verifikasi tab `Assigned` memuat aset `Scanner Canon DR-C225 {runId}`
24. Verifikasi aksi `Report Damaged` tidak tampil pada aset `Scanner Canon DR-C225 {runId}`
25. Verifikasi aksi `Report Missing` tidak tampil pada aset `Scanner Canon DR-C225 {runId}`
26. Verifikasi tab `Assigned` memuat aset `Laptop Asus ExpertBook {runId}`
27. Verifikasi aksi `Cancel Damage Report` tidak tampil pada aset `Laptop Asus ExpertBook {runId}` yang laporan kerusakannya milik aktor masih `Waiting for Confirmation`
28. Verifikasi tab `Assigned` memuat aset `Tablet Lenovo Tab M10 {runId}`
29. Verifikasi aksi `Cancel Missing Report` tidak tampil pada aset `Tablet Lenovo Tab M10 {runId}` yang laporan hilangnya milik aktor masih `Waiting for Confirmation`
30. Verifikasi Task `Confirm Handover` untuk aset `Printer HP M404 {runId}` tidak tampil
31. Klik tab `History`
32. Verifikasi baris aset `Webcam Logitech C920 {runId}` berstatus `Unassigned` tampil
33. Verifikasi baris aset `Printer HP M404 {runId}` berstatus `Canceled` tampil

### User Detail pada level None
34. Buka User Detail `Wulan Hartati {runId}`
35. Verifikasi Transaction admin log dan User log tampil dan terbaca

### Penugasan yang menunggu tercatat ditutup oleh System
36. Upgrade plan entitas kembali ke level `Full`
37. Klik menu `Transactions > Assignment`
38. Klik tab `History`
39. Ketik Search `Printer HP M404 {runId}`, tekan Enter
40. Verifikasi baris aset `Printer HP M404 {runId}` berstatus `Canceled` dengan alasan `Assignment not available on plan`
41. Buka menu ⋯ pada baris aset `Printer HP M404 {runId}`
42. Klik `Assignment Log`
43. Verifikasi node `Canceled by System` tampil pada Assignment Log
44. Tutup dialog Assignment Log
45. Ganti isi kotak Search dengan `Server Dell R740 {runId}`, tekan Enter
46. Verifikasi baris aset `Server Dell R740 {runId}` berstatus `Canceled` dengan alasan `Assignment not available on plan`

### Upgrade kembali tidak memulihkan Draft dan penugasan yang dibatalkan
47. Klik tab `Drafts`
48. Verifikasi tab `Drafts` menampilkan `No drafts`
49. Klik tab `Transactions`
50. Ketik Search `Camera Sony A7 {runId}`, tekan Enter
51. Verifikasi ASG aktif yang memuat aset `Camera Sony A7 {runId}` tampil
52. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
53. Verifikasi tidak ada ASG aktif yang memuat aset `Printer HP M404 {runId}`

### Notifikasi pembatalan otomatis dikirim sekali ke pengaju dan Assignee lain
54. Masuk sebagai pengaju `Agus Prasetyo {runId}`
55. Buka daftar notifikasi pada Bell icon aktor
56. Verifikasi tepat satu notifikasi pembatalan otomatis untuk ASG yang memuat aset `Printer HP M404 {runId}` tampil pada daftar
57. Verifikasi tepat satu notifikasi pembatalan otomatis untuk ASG yang memuat aset `Server Dell R740 {runId}` tampil pada daftar
58. Masuk sebagai Assignee `Budi Santoso {runId}`
59. Buka daftar notifikasi pada Bell icon aktor
60. Verifikasi tepat satu notifikasi pembatalan otomatis untuk ASG yang memuat aset `Server Dell R740 {runId}` tampil pada daftar
