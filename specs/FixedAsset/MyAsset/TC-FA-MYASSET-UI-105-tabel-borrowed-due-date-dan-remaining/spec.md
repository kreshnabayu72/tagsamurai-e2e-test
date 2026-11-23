---
id: TC-FA-MYASSET-UI-105-tabel-borrowed-due-date-dan-remaining
title: "Tabel Borrowed: teks Remaining dan format Due Date menurut status, satuan pinjaman, dan setting format"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r56", "§1.2#r57", "§1.2#r59", "§1.2#r61", "§1.2#r63", "§4.1b#r10", "§4.1b#r11", "§9.4.2#r90", "EB-XM-1", "§9.7#r17"]
smoke: []
dependsOn: []
trace:
  "§1.2#r56": [2, 4]
  "§1.2#r57": [7, 9, 11, 13, 15, 24]
  "§1.2#r59": [18, 19, 20, 21, 22, 46, 47, 48]
  "§1.2#r61": [3, 5]
  "§1.2#r63": [24, 26, 27, 28, 29, 30, 32, 33, 34]
  "§4.1b#r10": [3, 8, 25, 37, 38]
  "§4.1b#r11": [2, 7, 10, 14, 16, 35]
  "§9.4.2#r90": [13, 14]
  "EB-XM-1": [37, 38, 40, 41, 43, 44]
  "§9.7#r17": [14, 16, 35]
anchor: []
coverage:
  web: automated
---

# Tabel Borrowed: teks Remaining dan format Due Date menurut status, satuan pinjaman, dan setting format

## Prerequisites
- Aktor: Borrower (Budi Santoso, pengguna yang membuka halaman My Asset miliknya).
- Layar awal: Halaman My Asset > tab Borrowed
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-105-1: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Status `Waiting for Approval`, Duration `3 days`, Due Date `null`, Due Date tampil `—`, Remaining `—`.
  - DU-105-2: respons tiruan, satu baris tabel Borrowed: Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Status `Waiting for Handover`, Duration `3 days`, Due Date `null`, Due Date tampil `—`, Remaining `—`.
  - DU-105-3: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 3`, Asset ID `LPT-2026-0003`, Status `Borrowed`, Duration `5 days`, Due Date `2026-11-12`, Due Date tampil `12/11/26`, Remaining `Due in 3 days`.
  - DU-105-4: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Status `Borrowed`, Duration `4 days`, Due Date `2026-11-10`, Due Date tampil `10/11/26`, Remaining `Due in 1 day`.
  - DU-105-5: respons tiruan, satu baris tabel Borrowed: Name `Whiteboard Digital Samsung Flip - 1`, Asset ID `WBD-2026-0001`, Status `Borrowed`, Duration `2 days`, Due Date `2026-11-09`, Due Date tampil `09/11/26`, Remaining `Due today`.
  - DU-105-6: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Status `Overdue`, Duration `3 days`, Due Date `2026-11-08`, Due Date tampil `08/11/26`, Remaining `1 day overdue`.
  - DU-105-7: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Status `Overdue`, Duration `4 days`, Due Date `2026-11-06`, Due Date tampil `06/11/26`, Remaining `3 days overdue`.
  - DU-105-8: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Status `Borrowed`, Duration `3 hours`, Due Date `2026-11-09T21:50:00Z`, Due Date tampil `09/11/26, 21:50`, Remaining `Due in 1 hour`.
  - DU-105-9: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 4`, Asset ID `MIC-2026-0004`, Status `Borrowed`, Duration `8 hours`, Due Date `2026-11-10T02:30:00Z`, Due Date tampil `10/11/26, 02:30`, Remaining `Due in 6 hours`.
  - DU-105-10: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 6`, Asset ID `MIC-2026-0006`, Status `Borrowed`, Duration `2 hours`, Due Date `2026-11-09T20:50:00Z`, Due Date tampil `09/11/26, 20:50`, Remaining `Due in less than 1 hour`.
  - DU-105-11: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 7`, Asset ID `MIC-2026-0007`, Status `Borrowed`, Duration `1 hour`, Due Date `2026-11-09T20:30:00Z`, Due Date tampil `09/11/26, 20:30`, Remaining `Due now`.
  - DU-105-12: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 8`, Asset ID `MIC-2026-0008`, Status `Overdue`, Duration `2 hours`, Due Date `2026-11-09T20:10:00Z`, Due Date tampil `09/11/26, 20:10`, Remaining `less than 1 hour overdue`.
  - DU-105-13: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 9`, Asset ID `MIC-2026-0009`, Status `Overdue`, Duration `3 hours`, Due Date `2026-11-09T19:10:00Z`, Due Date tampil `09/11/26, 19:10`, Remaining `1 hour overdue`.
  - DU-105-14: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 10`, Asset ID `MIC-2026-0010`, Status `Overdue`, Duration `6 hours`, Due Date `2026-11-09T15:40:00Z`, Due Date tampil `09/11/26, 15:40`, Remaining `4 hours overdue`.
  - DU-105-15: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 11`, Asset ID `MIC-2026-0011`, Status `Borrowed`, Duration `12 hours`, Due Date `2026-11-09T23:45:00Z`, Due Date tampil `09/11/26, 23:45`, Remaining `Due in 3 hours`.
  - DU-105-16: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Status `Extension Request`, Duration `5 days`, Due Date `2026-11-11`, Due Date tampil `11/11/26`, Remaining `Due in 2 days`.
  - DU-105-17: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 53`, Asset ID `LPT-2026-0053`, Status `Overdue + Extension Request`, Duration `6 days`, Due Date `2026-11-08`, Due Date tampil `08/11/26`, Remaining `1 day overdue`.
  - DU-105-18: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 14`, Asset ID `LPT-2026-0014`, Status `Borrowed`, Duration `4 days`, Due Date `2026-03-25`, Due Date tampil dd/MM/yy `25/03/26`, Due Date tampil M/d/yy `3/25/26`, Remaining `Due in 1 day`.
  - DU-105-19: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 12`, Asset ID `MIC-2026-0012`, Status `Borrowed`, Duration `6 hours`, Due Date `2026-03-24T23:30:00Z`, Due Date tampil dd/MM/yy `24/03/26, 23:30`, Due Date tampil M/d/yy `3/24/26, 23:30`, Remaining `Due in 3 hours`.
  - DU-105-20: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Status `Extension Approval`, Duration `5 days`, Due Date `2026-11-11`, Due Date tampil `11/11/26`, Remaining `Due in 2 days`.
  - Jenis satuan pinjaman tiap baris mengikuti Duration: `days` untuk Duration berisi hari dan `hours` untuk Duration berisi jam.
- Kondisi:
  - K1: tabel Borrowed berisi DU-105-1 sampai DU-105-7, DU-105-16, DU-105-17, dan DU-105-20, dengan jam sekarang `2026-11-09T20:30:00Z`, Time Zone bernilai `UTC`, Date Format bernilai `dd/MM/yy`, dan Time Format bernilai `24 jam`.
  - K2: tabel Borrowed berisi DU-105-8 sampai DU-105-15, dengan jam sekarang `2026-11-09T20:30:00Z`, Time Zone bernilai `UTC`, Date Format bernilai `dd/MM/yy`, dan Time Format bernilai `24 jam`.
  - K3: tabel Borrowed berisi DU-105-18 dan DU-105-19, dengan jam sekarang `2026-03-24T20:30:00Z`, Time Zone bernilai `UTC`, Date Format bernilai `dd/MM/yy`, dan Time Format bernilai `24 jam`.
  - K4: sama dengan K3, dengan Date Format bernilai `M/d/yy`.
  - K5: sama dengan K3, dengan Time Format bernilai `12 jam`.

## Test Steps

### Remaining dan Due Date kosong sebelum handover
1. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
2. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 8` berisi `—`
3. Verifikasi sel Due Date baris `Laptop Dell Latitude 5420 - 8` berisi `—`
4. Verifikasi sel Remaining baris `Projector Epson EB-X06 - 12` berisi `—`
5. Verifikasi sel Due Date baris `Projector Epson EB-X06 - 12` berisi `—`

### Remaining pinjaman Days menurut selisih hari
6. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
7. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 3` berisi `Due in 3 days`
8. Verifikasi sel Due Date baris `Laptop Dell Latitude 5420 - 3` berisi `12/11/26`
9. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 2` berisi `Due in 1 day`
10. Verifikasi teks Remaining baris `Laptop Dell Latitude 5420 - 2` tidak bersaverity `danger`
11. Verifikasi sel Remaining baris `Whiteboard Digital Samsung Flip - 1` berisi `Due today`

### Remaining pinjaman Days Overdue berteks danger
12. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
13. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 6` berisi `1 day overdue`
14. Verifikasi teks Remaining baris `Laptop Dell Latitude 5420 - 6` bersaverity `danger`
15. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 9` berisi `3 days overdue`
16. Verifikasi teks Remaining baris `Laptop Dell Latitude 5420 - 9` bersaverity `danger`

### Pengajuan Extend tampil di kolom Status dan tidak di Remaining
17. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
18. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 51` berisi `Due in 2 days`
19. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 51` menampilkan badge `Extension Request`
20. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 51` tidak memuat `Extension Request`
21. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 53` menampilkan badge `Overdue` dan badge `Extension Request`
22. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 53` berisi `1 day overdue`

### Remaining pinjaman Hours dihitung dalam jam penuh
23. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
24. Verifikasi sel Remaining baris `Meeting Mic Set - 2` berisi `Due in 1 hour`
25. Verifikasi sel Due Date baris `Meeting Mic Set - 2` berisi `09/11/26, 21:50`
26. Verifikasi sel Remaining baris `Meeting Mic Set - 4` berisi `Due in 6 hours`
27. Verifikasi sel Remaining baris `Meeting Mic Set - 6` berisi `Due in less than 1 hour`
28. Verifikasi sel Remaining baris `Meeting Mic Set - 7` berisi `Due now`
29. Verifikasi sel Remaining baris `Meeting Mic Set - 11` berisi `Due in 3 hours`
30. Verifikasi sel Remaining baris `Meeting Mic Set - 11` tidak berisi `Due today`

### Remaining pinjaman Hours Overdue
31. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
32. Verifikasi sel Remaining baris `Meeting Mic Set - 8` berisi `less than 1 hour overdue`
33. Verifikasi sel Remaining baris `Meeting Mic Set - 9` berisi `1 hour overdue`
34. Verifikasi sel Remaining baris `Meeting Mic Set - 10` berisi `4 hours overdue`
35. Verifikasi teks Remaining baris `Meeting Mic Set - 10` bersaverity `danger`

### Due Date menurut Date Format dd/MM/yy dan Time Format 24 jam
36. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
37. Verifikasi sel Due Date baris `Laptop Dell Latitude 5420 - 14` berisi `25/03/26`
38. Verifikasi sel Due Date baris `Meeting Mic Set - 12` berisi `24/03/26, 23:30`

### Due Date menurut Date Format M/d/yy
39. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K4
40. Verifikasi sel Due Date baris `Laptop Dell Latitude 5420 - 14` berisi `3/25/26`
41. Verifikasi sel Due Date baris `Meeting Mic Set - 12` berisi `3/24/26, 23:30`

### Due Date menurut Time Format 12 jam
42. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K5
43. Verifikasi sel Due Date baris `Meeting Mic Set - 12` menampilkan tanggal `24/03/26` dengan jam dalam format 12 jam
44. Verifikasi jam pada sel Due Date baris `Meeting Mic Set - 12` tidak tampil sebagai `23:30`

### Pengajuan Extend menunggu approval tampil di kolom Status dan tidak di Remaining
45. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
46. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 10` berisi `Due in 2 days`
47. Verifikasi sel Remaining baris `Laptop Dell Latitude 5420 - 10` tidak memuat `Extension Approval`
48. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Extension Approval`
