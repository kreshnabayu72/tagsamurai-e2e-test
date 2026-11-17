---
id: TC-FA-MYASSET-UI-123-dialog-cancel-extension
title: "Dialog Cancel Extension: isi, toast sukses, dan reaksi atas kegagalan"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1b#r58", "§4.1b#r59", "§Dialog aksi baris (tab Borrowed dan Assigned)#p6", "§Dialog aksi baris (tab Borrowed dan Assigned)#p7", "§7.2#r5", "§7.3#r3", "§7.3#r15", "§9.6#r4", "EB-FB-1@cancel-extension-request", "EB-FB-2@cancel-extension-request", "EB-ERR-1@cancel-extension-request"]
smoke: []
dependsOn: []
trace:
  "§4.1b#r58": 4
  "§4.1b#r59": 15
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p6": [4, 5, 6, 7]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p7": 15
  "§7.2#r5": [4, 5, 6, 7]
  "§7.3#r3": 15
  "§7.3#r15": 20
  "§9.6#r4": [15, 20]
  "EB-FB-1@cancel-extension-request": [15, 20, 25]
  "EB-FB-2@cancel-extension-request": 10
  "EB-ERR-1@cancel-extension-request": [20, 21, 22, 23, 25, 30, 31, 32]
anchor: [9]
coverage:
  web: automated
---

# Dialog Cancel Extension: isi, toast sukses, dan reaksi atas kegagalan

## Prerequisites
- Aktor: Borrower `Budi Santoso`.
- Layar awal: My Asset > Borrowed.
- Komponen: Dialog Cancel Extension (D-BRW-14)
- Data:
  - DU-123-1: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Status `Extension Approval`, Due Date `11/11/26`, Borrower `Me`, Transaction ID `BRW-2026-0149`, Source `Admin`, Duration `5 days`.
- Kondisi:
  - K1: baris DU-123-1 tampil di tab Borrowed dan Cancel Extension dijawab sukses. Date Format bernilai `dd/MM/yy`.
  - K2: baris DU-123-1 tampil di tab Borrowed, Cancel Extension pertama dijawab error server, dan Cancel Extension berikutnya dijawab sukses.
  - K3: baris DU-123-1 tampil di tab Borrowed dan Cancel Extension tidak mendapat respons karena koneksi terputus.

## Test Steps

### Isi dialog Cancel Extension dan Go Back menutup tanpa toast
1. Tampilkan Dialog Cancel Extension dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
3. Klik `Cancel Extension Request`
4. Verifikasi judul dialog `Cancel Extension` tampil
5. Verifikasi nama aset `Laptop Dell Latitude 5420 - 10` tampil sebagai satu bullet
6. Verifikasi teks `The approval request will be withdrawn and the current due date stays 11/11/26. Are you sure you want to cancel it?` tampil
7. Verifikasi tombol `[Go Back]` dan `[Cancel Extension]` tampil
8. Klik `[Go Back]`
9. Verifikasi dialog `Cancel Extension` tertutup
10. Verifikasi toast tidak tampil

### Cancel Extension berhasil
11. Tampilkan Dialog Cancel Extension dengan kondisi K1
12. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
13. Klik `Cancel Extension Request`
14. Klik `[Cancel Extension]`
15. Verifikasi toast `Success, extension request has been canceled.` tampil

### Gagal server pada Cancel Extension lalu dicoba ulang
16. Tampilkan Dialog Cancel Extension dengan kondisi K2
17. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
18. Klik `Cancel Extension Request`
19. Klik `[Cancel Extension]`
20. Verifikasi toast `Error, failed to cancel extension request.` tampil
21. Verifikasi dialog `Cancel Extension` tetap terbuka
22. Verifikasi tombol `[Cancel Extension]` aktif lagi
23. Verifikasi toast tidak memuat tombol aksi
24. Klik `[Cancel Extension]`
25. Verifikasi toast `Success, extension request has been canceled.` tampil

### Koneksi terputus pada Cancel Extension
26. Tampilkan Dialog Cancel Extension dengan kondisi K3
27. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
28. Klik `Cancel Extension Request`
29. Klik `[Cancel Extension]`
30. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
31. Verifikasi dialog `Cancel Extension` tetap terbuka
32. Verifikasi tombol `[Cancel Extension]` aktif lagi

[^drift-1]: Drift PRD vs foundation. PRD §9.6 Action Resilience Spec: gagal server (5xx atau timeout) pada aksi tulis memunculkan toast `T-BRW-26` (`Error, failed to [verb] [item].`). foundation `error-handling-convention.md` §2: Timeout / Network memunculkan `Connection problem. Please try again.` tanpa tombol aksi. Diasersi: foundation untuk koneksi terputus, karena toast kegagalan adalah pola bersama (SB-4); kegagalan server 5xx tetap memakai `T-BRW-26` dari PRD.
