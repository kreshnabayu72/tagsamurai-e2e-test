---
id: TC-FA-MYASSET-BE-208-perpindahan-pic-aturan-server-dep-users
title: "Aturan server perpindahan baris saat PIC diganti, dikosongkan, atau Borrower dibuatkan akun"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r49", "§1.2#r50", "§1.2#r52", "§1.2#r53", "§9.2#r23", "§9.2#r24", "§9.4.2#r10", "§9.4.2#r22", "§9.4.2#r48", "§9.4.2#r49", "§9.4.2#r50", "§9.4.2#r51", "§9.4.2#r64", "§9.4.2#r65"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§1.2#r49": [30, 31, 35]
  "§1.2#r50": [23, 24, 38]
  "§1.2#r52": [5, 8, 9, 10, 11, 18, 20, 36]
  "§1.2#r53": [6, 7, 13, 14, 17, 21, 25, 28]
  "§9.2#r23": 4
  "§9.2#r24": 16
  "§9.4.2#r10": [23, 24, 27]
  "§9.4.2#r22": [38, 40, 41, 43, 45]
  "§9.4.2#r48": 4
  "§9.4.2#r49": 5
  "§9.4.2#r50": 16
  "§9.4.2#r51": 19
  "§9.4.2#r64": [30, 31, 35]
  "§9.4.2#r65": [32, 33]
---

# Aturan server perpindahan baris saat PIC diganti, dikosongkan, atau Borrower dibuatkan akun

## Prerequisites
- Aktor: PIC Borrower awal Siti (DU-208-1) dan PIC pengganti Agus (DU-208-2); PIC Division lama Budi (DU-208-3), PIC Division pengganti Maya (DU-208-4), PIC yang dinonaktifkan Hendra (DU-208-5) dan PIC yang pindah Division Dian (DU-208-6); Aktor Borrow dan Aktor Assignment Rina (DU-208-7); admin pengelola Users Bambang (DU-208-8).
- Data:
  - DU-208-1: User: Name `Siti Nurhaliza {runId}`, Peran `PIC Borrower tanpa akun, tanpa hak lain`.
  - DU-208-2: User: Name `Agus Pratama {runId}`, Peran `PIC Borrower tanpa akun, tanpa hak lain`.
  - DU-208-3: User: Name `Budi Santoso {runId}`, Peran `PIC Division Finance`.
  - DU-208-4: User: Name `Maya Anggraini {runId}`, Peran `pengganti PIC Division Finance dan penerima PIC Division yang tanpa PIC`.
  - DU-208-5: User: Name `Hendra Wijaya {runId}`, Peran `PIC Division Procurement`.
  - DU-208-6: User: Name `Dian Permata {runId}`, Peran `PIC Division Marketing`.
  - DU-208-7: User: Name `Rina Wulandari {runId}`, Peran `Aktor Borrow dan Aktor Assignment`.
  - DU-208-8: User: Name `Bambang Hartono {runId}`, Peran `admin yang mengelola karyawan dan akun di Users`.
  - DU-208-9: Karyawan: Name `Rahmat Hidayat {runId}`, Akun login `tidak ada`, PIC `Siti Nurhaliza {runId}`.
  - DU-208-10: Karyawan: Name `Lina Marlina {runId}`, Akun login `tidak ada`, PIC `Siti Nurhaliza {runId}`.
  - DU-208-11: Karyawan: Name `Joko Susilo {runId}`, Akun login `tidak ada`, PIC `Agus Pratama {runId}`.
  - DU-208-12: Division: Name `Finance {runId}`, PIC `Budi Santoso {runId}`.
  - DU-208-13: Division: Name `Procurement {runId}`, PIC `Hendra Wijaya {runId}`.
  - DU-208-14: Division: Name `Marketing {runId}`, PIC `Dian Permata {runId}`.
  - DU-208-15: Division: Name `Legal {runId}`.
  - DU-208-16: Pinjaman: Name `Laptop Dell Latitude 5420 {runId}`, Status `Waiting for Handover`, Borrower `Rahmat Hidayat {runId}`, Sesi Handover `aktif, menunggu konfirmasi`.
  - DU-208-17: Pinjaman: Name `Printer HP M404 {runId}`, Status `Returned`, Borrower `Rahmat Hidayat {runId}`.
  - DU-208-18: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Status `Borrowed`, Borrower `Rahmat Hidayat {runId}`.
  - DU-208-19: Pinjaman: Name `Laptop Asus ZenBook 14 {runId}`, Status `Waiting for Handover`, Borrower `Lina Marlina {runId}`, Sesi Handover `aktif, menunggu konfirmasi`.
  - DU-208-20: Pinjaman: Name `Printer Canon G3010 {runId}`, Status `Returned`, Borrower `Lina Marlina {runId}`.
  - DU-208-21: Pinjaman: Name `Laptop Acer Aspire 5 {runId}`, Status `Waiting for Handover`, Borrower `Joko Susilo {runId}`, Sesi Handover `aktif, menunggu konfirmasi`.
  - DU-208-22: Penugasan: Assigned To `Finance {runId}`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Status `Waiting for Handover`, Sesi Handover `aktif, menunggu konfirmasi`, PIC `Budi Santoso {runId}`.
  - DU-208-23: Penugasan: Assigned To `Finance {runId}`, Aset `Monitor Dell 24 Inci {runId}`, Status `Assigned`, Damage Report `Waiting for Confirmation, dilaporkan Budi Santoso {runId}`, PIC `Budi Santoso {runId}`.
  - DU-208-24: Penugasan: Assigned To `Procurement {runId}`, Aset `Proyektor Epson EB-X06 {runId}`, Status `Assigned`, PIC `Hendra Wijaya {runId}`.
  - DU-208-25: Penugasan: Assigned To `Marketing {runId}`, Aset `Laptop HP ProBook 450 {runId}`, Status `Assigned`, PIC `Dian Permata {runId}`.

## Test Steps

### PIC Borrower diganti: baris, riwayat, dan Task pindah ke PIC baru
1. Siti mengajukan Extend atas nama Rahmat untuk pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Kegiatan dokumentasi proyek belum selesai`
2. Siti memegang sesi Handover yang aktif atas pinjaman `Laptop Dell Latitude 5420 {runId}` dan belum mengirim Confirm
3. Bambang mengganti PIC Borrower `Rahmat Hidayat {runId}` dari Siti menjadi Agus
4. Verifikasi baris pinjaman `Laptop Dell Latitude 5420 {runId}` tampil di My Asset Agus
5. Verifikasi baris pinjaman `Laptop Dell Latitude 5420 {runId}` tidak lagi tampil di My Asset Siti
6. Verifikasi Task Confirm Handover pinjaman `Laptop Dell Latitude 5420 {runId}` pindah ke My Asset Agus
7. Verifikasi Task itu tidak lagi tampil di My Asset Siti
8. Verifikasi baris riwayat `Printer HP M404 {runId}` berstatus `Returned` tampil di My Asset Agus
9. Verifikasi baris riwayat `Printer HP M404 {runId}` tidak lagi tampil di My Asset Siti
10. Verifikasi PIC yang tertaut pada Holder baris riwayat `Printer HP M404 {runId}` adalah PIC saat ini, `Agus Pratama {runId}`
11. Verifikasi Borrow Log pinjaman `Kamera Canon EOS 200D {runId}` tetap mencatat `Siti Nurhaliza {runId}` sebagai PIC pada entri `Extension requested`
12. Siti mengirim Confirm atas sesi Handover pinjaman `Laptop Dell Latitude 5420 {runId}` yang ia pegang sebelum PIC diganti, dengan aset `Laptop Dell Latitude 5420 {runId}` ditandai diterima
13. Verifikasi Confirm ditolak server karena Siti bukan pemegang pinjaman lagi
14. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tetap `Waiting for Handover` dan Task-nya tetap ada di My Asset Agus

### Borrower dibuatkan akun: baris, riwayat, dan Task pindah ke Borrower
15. Bambang membuatkan akun login untuk Borrower `Lina Marlina {runId}` dengan Email `lina.marlina.{runId}@example.com`
16. Verifikasi baris pinjaman `Laptop Asus ZenBook 14 {runId}` tampil di My Asset Lina
17. Verifikasi Task Confirm Handover pinjaman `Laptop Asus ZenBook 14 {runId}` pindah ke My Asset Lina
18. Verifikasi baris riwayat `Printer Canon G3010 {runId}` berstatus `Returned` tampil di My Asset Lina
19. Verifikasi baris pinjaman `Laptop Asus ZenBook 14 {runId}` tidak lagi tampil di My Asset Siti
20. Verifikasi baris riwayat `Printer Canon G3010 {runId}` tidak lagi tampil di My Asset Siti
21. Verifikasi Task pinjaman `Laptop Asus ZenBook 14 {runId}` tidak lagi tampil di My Asset Siti

### PIC Borrower dikosongkan: baris No PIC tidak tampil di My Asset siapa pun
22. Bambang mengosongkan PIC Borrower `Joko Susilo {runId}`
23. Verifikasi baris pinjaman `Laptop Acer Aspire 5 {runId}` berstatus `No PIC` tidak tampil di My Asset Agus
24. Verifikasi baris pinjaman `Laptop Acer Aspire 5 {runId}` tidak tampil di My Asset Siti
25. Verifikasi Task pinjaman `Laptop Acer Aspire 5 {runId}` tidak tampil di My Asset Agus maupun My Asset Siti
26. Bambang menunjuk Siti sebagai PIC Borrower `Joko Susilo {runId}`
27. Verifikasi baris pinjaman `Laptop Acer Aspire 5 {runId}` tampil di My Asset Siti
28. Verifikasi Task pinjaman `Laptop Acer Aspire 5 {runId}` tampil di My Asset Siti

### Change PIC Division: baris, Task, dan jejak PIC di Assignment Log
29. Rina mengubah PIC penugasan Division `Finance {runId}` atas aset `Laptop Lenovo ThinkPad T14 {runId}` dari Budi menjadi Maya lewat Change PIC
30. Verifikasi baris penugasan `Laptop Lenovo ThinkPad T14 {runId}` tampil di My Asset Maya
31. Verifikasi Task Confirm Handover penugasan itu pindah ke My Asset Maya
32. Verifikasi baris penugasan `Laptop Lenovo ThinkPad T14 {runId}` tidak lagi tampil di My Asset Budi
33. Verifikasi Task penugasan itu tidak lagi tampil di My Asset Budi
34. Rina mengubah PIC penugasan Division `Finance {runId}` atas aset `Monitor Dell 24 Inci {runId}` dari Budi menjadi Maya lewat Change PIC
35. Verifikasi baris penugasan `Monitor Dell 24 Inci {runId}` tampil di My Asset Maya
36. Verifikasi Assignment Log aset `Monitor Dell 24 Inci {runId}` tetap mencatat `Budi Santoso {runId}` sebagai PIC pada aksi pelaporan kerusakan aset yang ia lakukan

### PIC Division dinonaktifkan atau pindah Division: baris No PIC tidak tampil di My Asset siapa pun
37. Bambang menonaktifkan user `Hendra Wijaya {runId}`, PIC penugasan Division `Procurement {runId}`
38. Verifikasi baris penugasan `Proyektor Epson EB-X06 {runId}` berstatus `No PIC` tidak tampil di My Asset Maya
39. Bambang memindahkan user `Dian Permata {runId}`, PIC penugasan Division `Marketing {runId}`, ke Division `Legal {runId}`
40. Verifikasi baris penugasan `Laptop HP ProBook 450 {runId}` berstatus `No PIC` tidak tampil di My Asset Dian
41. Verifikasi baris penugasan `Laptop HP ProBook 450 {runId}` tidak tampil di My Asset Maya

### Baris No PIC tampil lagi sesudah PIC Division ditunjuk
42. Rina menunjuk Maya sebagai PIC penugasan Division `Procurement {runId}` atas aset `Proyektor Epson EB-X06 {runId}` lewat Change PIC
43. Verifikasi baris penugasan `Proyektor Epson EB-X06 {runId}` tampil di My Asset Maya
44. Rina menunjuk Maya sebagai PIC penugasan Division `Marketing {runId}` atas aset `Laptop HP ProBook 450 {runId}` lewat Change PIC
45. Verifikasi baris penugasan `Laptop HP ProBook 450 {runId}` tampil di My Asset Maya
