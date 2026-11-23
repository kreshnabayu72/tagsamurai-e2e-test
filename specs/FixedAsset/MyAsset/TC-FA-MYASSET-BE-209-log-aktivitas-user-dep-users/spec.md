---
id: TC-FA-MYASSET-BE-209-log-aktivitas-user-dep-users
title: "Aksi My Asset tercatat sebagai Activity di User Log Borrow dan Assignment"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8#p1", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8#r5", "§8#r6", "§8#r7", "§8#r8", "§8#r9", "§8#r10", "§8#r11", "§8#p3", "§9.7#r18"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§8#p1": [15, 26, 32]
  "§8#r1": 2
  "§8#r2": [3, 4]
  "§8#r3": 6
  "§8#r4": 8
  "§8#r5": 10
  "§8#r6": [12, 13]
  "§8#r7": 17
  "§8#r8": 19
  "§8#r9": [21, 25, 26]
  "§8#r10": 23
  "§8#r11": [28, 29]
  "§8#p3": [32, 33, 34, 36, 38, 40, 42, 44, 47, 48, 49]
  "§9.7#r18": 50
---

# Aksi My Asset tercatat sebagai Activity di User Log Borrow dan Assignment

## Prerequisites
- Aktor: Borrower dan Assignee Dewi (DU-209-1), Borrower tanpa akun Rahmat (DU-209-2) beserta PIC Siti (DU-209-3), PIC Division Budi (DU-209-4), anggota Division Fajar (DU-209-5), pemegang yang juga memegang hak Aktor Missing Agus (DU-209-6), dan Aktor Borrow dan Aktor Assignment Rina (DU-209-7).
- Data:
  - DU-209-1: User: Name `Dewi Lestari {runId}`, Peran `Borrower dan Assignee tanpa hak lain`.
  - DU-209-2: Karyawan: Name `Rahmat Hidayat {runId}`, Akun login `tidak ada`, PIC `Siti Nurhaliza {runId}`.
  - DU-209-3: User: Name `Siti Nurhaliza {runId}`, Peran `PIC Borrower tanpa akun`.
  - DU-209-4: User: Name `Budi Santoso {runId}`, Peran `PIC Division Finance`.
  - DU-209-5: User: Name `Fajar Nugroho {runId}`, Peran `anggota Division Finance, bukan PIC`.
  - DU-209-6: User: Name `Agus Pratama {runId}`, Peran `Borrower yang juga memegang hak Aktor Missing pada Group Head Office`.
  - DU-209-7: User: Name `Rina Wulandari {runId}`, Peran `Aktor Borrow dan Aktor Assignment pada Group Head Office`.
  - DU-209-8: Division: Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota `Fajar Nugroho {runId}`.
  - DU-209-9: Pinjaman: Aset 1 `Laptop Lenovo ThinkPad T14 {runId}`, Aset 2 `Mouse Logitech MX Master 3 {runId}`, Aset 3 `Webcam Logitech C920 {runId}`, Status `Waiting for Handover`, Sesi Handover `aktif, menunggu konfirmasi`, Borrower `Dewi Lestari {runId}`.
  - DU-209-10: Pinjaman: Name `Monitor Dell 24 Inci {runId}`, Status `Waiting for Approval`, Borrower `Dewi Lestari {runId}`.
  - DU-209-11: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-209-12: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Source `Self-service`.
  - DU-209-13: Pinjaman: Name `Printer HP M404 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-209-14: Pinjaman: Name `Proyektor Epson EB-X06 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-209-15: Pinjaman: Name `Laptop HP ProBook 450 {runId}`, Status `Borrowed`, Borrower `Agus Pratama {runId}`.
  - DU-209-16: Aset: Name `Tablet Samsung Galaxy Tab A9 {runId}`, Status `Available`, Source `Self-service`.
  - DU-209-17: Pinjaman: Name `Scanner Canon LiDE 300 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-209-18: Pinjaman: Name `Laptop Asus ZenBook 14 {runId}`, Status `Borrowed`, Borrower `Rahmat Hidayat {runId}`.
  - DU-209-19: Penugasan: Name `Keyboard Logitech MX Keys {runId}`, Status `Waiting for Handover`, Sesi Handover `aktif, menunggu konfirmasi`, Assignee `Dewi Lestari {runId}`.
  - DU-209-20: Penugasan: Name `Monitor LG 27 Inci {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-209-21: Penugasan: Name `Headset Jabra Evolve2 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-209-22: Penugasan: Assigned To `Finance {runId}`, Aset `Printer Epson L3250 {runId}`, Status `Assigned`, PIC `Budi Santoso {runId}`.

## Test Steps

### Confirm Handover dengan aset dicentang dan tidak dicentang tercatat
1. Dewi mengonfirmasi serah terima pinjaman yang memuat `Laptop Lenovo ThinkPad T14 {runId}`, `Mouse Logitech MX Master 3 {runId}`, dan `Webcam Logitech C920 {runId}`, dengan hanya `Laptop Lenovo ThinkPad T14 {runId}` tercentang
2. Verifikasi User Log Borrow Dewi memuat Activity `Handed over` untuk `Laptop Lenovo ThinkPad T14 {runId}`
3. Verifikasi User Log Borrow Dewi memuat satu Activity `Handover not confirmed` untuk tiap aset tidak tercentang, yaitu `Mouse Logitech MX Master 3 {runId}` dan `Webcam Logitech C920 {runId}`
4. Verifikasi baris `Mouse Logitech MX Master 3 {runId}` dan `Webcam Logitech C920 {runId}` tetap `Waiting for Handover`

### Cancel Borrow tercatat
5. Dewi membatalkan pinjaman `Monitor Dell 24 Inci {runId}` lewat Cancel Borrow
6. Verifikasi User Log Borrow Dewi memuat Activity `Canceled` untuk `Monitor Dell 24 Inci {runId}`

### Request Extension dan Cancel Extension Request tercatat
7. Dewi mengajukan Extend atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Kegiatan dokumentasi proyek belum selesai`
8. Verifikasi User Log Borrow Dewi memuat Activity `Extension requested` untuk pinjaman itu
9. Dewi menarik pengajuan Extend itu lewat Cancel Extension Request
10. Verifikasi User Log Borrow Dewi memuat Activity `Extension canceled` untuk pinjaman itu

### Return pinjaman self-service dan Return oleh Aktor Borrow tercatat
11. Dewi melakukan Return atas pinjaman self-service `Drone DJI Mini 3 {runId}`
12. Verifikasi User Log Borrow Dewi memuat Activity `Returned` untuk `Drone DJI Mini 3 {runId}`
13. Verifikasi judul node entri itu adalah `Returned via self-service by Dewi Lestari {runId}`
14. Rina melakukan Return atas pinjaman Admin `Scanner Canon LiDE 300 {runId}` milik Dewi
15. Verifikasi User Log Borrow Dewi memuat Activity `Returned` untuk `Scanner Canon LiDE 300 {runId}`, sebagai peristiwa yang dipicu Aktor Borrow

### Report Damaged dan Cancel Damage Report tercatat
16. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
17. Verifikasi User Log Borrow Dewi memuat Activity `Damage reported` untuk `Printer HP M404 {runId}`
18. Dewi mengirim Cancel Damage Report atas laporan itu
19. Verifikasi User Log Borrow Dewi memuat Activity `Damage report canceled` untuk `Printer HP M404 {runId}`

### Report Missing dan Cancel Missing Report tercatat
20. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
21. Verifikasi User Log Borrow Dewi memuat Activity `Reported missing` untuk `Proyektor Epson EB-X06 {runId}`
22. Dewi mengirim Cancel Missing Report atas laporan itu
23. Verifikasi User Log Borrow Dewi memuat Activity `Missing report canceled` untuk `Proyektor Epson EB-X06 {runId}`

### Report Missing oleh pemegang dengan hak Aktor Missing tercatat tanpa entri konfirmasi
24. Agus mengirim Report Missing atas pinjaman `Laptop HP ProBook 450 {runId}`
25. Verifikasi User Log Borrow Agus memuat Activity `Reported missing` untuk `Laptop HP ProBook 450 {runId}`
26. Verifikasi User Log Borrow Agus untuk `Laptop HP ProBook 450 {runId}` tidak memuat entri konfirmasi laporan

### Borrow an Asset self-service tercatat
27. Dewi melakukan Borrow Now atas aset self-service `Tablet Samsung Galaxy Tab A9 {runId}`
28. Verifikasi User Log Borrow Dewi memuat Activity `Borrow requested` untuk `Tablet Samsung Galaxy Tab A9 {runId}`
29. Verifikasi User Log Borrow Dewi memuat Activity `Handed over` untuk aset itu dengan judul node `Borrowed via self-service by Dewi Lestari {runId}`

### Tindakan PIC Borrower tercatat sekali atas nama Borrower
30. Catat jumlah entri User Log Borrow Siti
31. Siti mengirim Report Damaged atas nama Rahmat untuk pinjaman `Laptop Asus ZenBook 14 {runId}` dengan Damaged Photo `laptop-layar-retak.jpg` dan What happened `Layar laptop retak setelah terjatuh dari meja`
32. Verifikasi User Log Borrow karyawan Rahmat, yang tidak punya akun login, memuat Activity `Damage reported` dengan pelaku `Siti Nurhaliza {runId} on behalf of Rahmat Hidayat {runId}`
33. Verifikasi entri `Damage reported` di User Log Borrow Rahmat dicatat `by Siti Nurhaliza {runId} on behalf of Rahmat Hidayat {runId}`
34. Verifikasi jumlah entri User Log Borrow Siti sama dengan jumlah yang dicatat

### Aksi Assignment oleh Assignee tercatat di sub-tab Assignment User Log
35. Dewi mengonfirmasi serah terima penugasan `Keyboard Logitech MX Keys {runId}`
36. Verifikasi sub-tab Assignment User Log Dewi memuat entri Confirm atas penugasan `Keyboard Logitech MX Keys {runId}`
37. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
38. Verifikasi sub-tab Assignment User Log Dewi memuat entri Report Damaged atas `Monitor LG 27 Inci {runId}`
39. Dewi mengirim Cancel Damage Report atas laporan itu
40. Verifikasi sub-tab Assignment User Log Dewi memuat entri Cancel Damage Report atas `Monitor LG 27 Inci {runId}`
41. Dewi mengirim Report Missing atas penugasan `Headset Jabra Evolve2 {runId}`
42. Verifikasi sub-tab Assignment User Log Dewi memuat entri Report Missing atas `Headset Jabra Evolve2 {runId}`
43. Dewi mengirim Cancel Missing Report atas laporan itu
44. Verifikasi sub-tab Assignment User Log Dewi memuat entri Cancel Missing Report atas `Headset Jabra Evolve2 {runId}`

### Tindakan PIC Division tercatat di User Log PIC atas nama Division
45. Catat jumlah entri sub-tab Assignment User Log milik `Fajar Nugroho {runId}`
46. Budi mengirim Report Damaged atas nama Division `Finance {runId}` untuk penugasan `Printer Epson L3250 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
47. Verifikasi sub-tab Assignment User Log Budi memuat entri Report Damaged atas `Printer Epson L3250 {runId}` dengan penanda `on behalf of Finance {runId}`
48. Verifikasi jumlah entri sub-tab Assignment User Log milik `Fajar Nugroho {runId}` sama dengan jumlah yang dicatat
49. Verifikasi sub-tab Assignment User Log Dewi tidak memuat entri atas penugasan `Printer Epson L3250 {runId}`

### Borrow Now self-service menghasilkan baris Borrowed di tab Borrowed
50. Verifikasi data My Asset tab Borrowed milik Dewi, setelah dipersempit ke aset `Tablet Samsung Galaxy Tab A9 {runId}` yang diperoleh lewat Borrow Now, memuat tepat satu baris berstatus `Borrowed`
