---
id: TC-FA-MYASSET-BE-205-cancel-borrow-aturan-server-dep-borrow
title: "Aturan server Cancel Borrow: syarat status, sesi Handover berjalan, sudah dibatalkan, dan Custody"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-02", "§1.2#r31", "§1.2#r32", "§1.2#r33", "§4.1b#r76", "§4.1b#r79", "§9.2#r4", "§9.2#r7", "§9.4.2#r68", "§9.4.2#r69", "§9.4.2#r71", "§9.4.2#r74", "§9.4.2#r75", "§9.4.2#r76", "§9.6#r2", "EB-ERR-4", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "V-02": [29, 31, 36, 40]
  "§1.2#r31": [2, 4, 15, 21, 23]
  "§1.2#r32": [21, 23, 25, 26]
  "§1.2#r33": [8, 9]
  "§4.1b#r76": 29
  "§4.1b#r79": [11, 17]
  "§9.2#r4": [4, 15, 19, 21, 23]
  "§9.2#r7": [11, 17]
  "§9.4.2#r68": [6, 9, 11]
  "§9.4.2#r69": 8
  "§9.4.2#r71": [40, 52]
  "§9.4.2#r74": [42, 44, 54]
  "§9.4.2#r75": 29
  "§9.4.2#r76": 36
  "§9.6#r2": [13, 33, 44, 46, 48, 56]
  "EB-ERR-4": [25, 26, 31, 33, 42, 44, 54, 56]
  "EB-CON-3": [29, 40, 52]
  "EB-EDG-1": [46, 48]
owner: BE
---

# Aturan server Cancel Borrow: syarat status, sesi Handover berjalan, sudah dibatalkan, dan Custody

## Prerequisites
- Aktor: Maya (Borrower), Wulan (PIC Borrower atas nama Anton), dan Gita (Aktor Borrow yang membatalkan pinjaman, menekan `Cancel Request`, dan membaca Custody aset).
- Data:
  - DU-205-1: User `Maya Anggraini {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, Borrower pada DU-205-5 sampai DU-205-10.
  - DU-205-2: User `Gita Permata {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Aktor Borrow Group `Head Office`.
  - DU-205-3: Borrower tanpa akun `Anton Saputra {runId}`, PIC-nya Wulan, Borrower pada DU-205-11 dan DU-205-12.
  - DU-205-4: User `Wulan Pratiwi {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, PIC Anton.
  - DU-205-5: Satu pinjaman Maya berisi dua aset, `Laptop Dell Latitude 5420 - 51 {runId}` dan `Laptop Dell Latitude 5420 - 52 {runId}`, Group `Head Office`, keduanya berstatus `Waiting for Approval`.
  - DU-205-6: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 53 {runId}`, Group `Head Office`, status `Waiting for Handover`, tanpa sesi Handover berjalan.
  - DU-205-7: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 54 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-205-8: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 55 {runId}`, Group `Head Office`, status `Overdue`, Due date sudah terlewati.
  - DU-205-9: Pinjaman Maya dengan sesi Handover berjalan, aset `Laptop Dell Latitude 5420 - 56 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-205-10: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 57 {runId}`, Group `Head Office`, status `Waiting for Approval`.
  - DU-205-11: Pinjaman Anton, aset `Laptop Dell Latitude 5420 - 58 {runId}`, Group `Head Office`, status `Waiting for Approval`.
  - DU-205-12: Pinjaman Anton, aset `Laptop Dell Latitude 5420 - 59 {runId}`, Group `Head Office`, status `Waiting for Approval`.

## Test Steps

### Cancel Borrow pada baris Waiting for Approval berhasil per baris dan Custody menjadi Available
1. Maya meminta data tab Borrowed
2. Verifikasi data memuat baris aset `Laptop Dell Latitude 5420 - 51 {runId}` dan baris aset `Laptop Dell Latitude 5420 - 52 {runId}` berstatus `Waiting for Approval`
3. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 51 {runId}`
4. Verifikasi pembatalan diterima server
5. Maya meminta data tab History
6. Verifikasi data memuat baris aset `Laptop Dell Latitude 5420 - 51 {runId}` dengan Type `Borrow` dan status `Canceled`
7. Maya meminta data tab Borrowed
8. Verifikasi baris aset `Laptop Dell Latitude 5420 - 52 {runId}` pada pinjaman yang sama tetap berstatus `Waiting for Approval`
9. Verifikasi data tidak memuat baris aset `Laptop Dell Latitude 5420 - 51 {runId}`
10. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 51 {runId}`
11. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 51 {runId}` bernilai `Available`
12. Maya meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 51 {runId}`
13. Verifikasi Borrow Log memuat satu node `Canceled`

### Cancel Borrow pada baris Waiting for Handover tanpa sesi Handover berhasil
14. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 53 {runId}`
15. Verifikasi pembatalan diterima server
16. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 53 {runId}`
17. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 53 {runId}` bernilai `Available`

### PIC membatalkan baris Borrower tanpa akun atas nama Borrower
18. Wulan mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 58 {runId}` milik Anton
19. Verifikasi pembatalan diterima server

### Baris Borrowed dan Overdue tidak dapat dibatalkan Borrower
20. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 54 {runId}`
21. Verifikasi pembatalan ditolak server karena baris berstatus `Borrowed`
22. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 55 {runId}`
23. Verifikasi pembatalan ditolak server karena baris berstatus `Overdue`
24. Maya meminta data tab Borrowed
25. Verifikasi baris aset `Laptop Dell Latitude 5420 - 54 {runId}` tetap berstatus `Borrowed`
26. Verifikasi baris aset `Laptop Dell Latitude 5420 - 55 {runId}` tetap berstatus `Overdue`

### Pembatalan selama sesi Handover berjalan ditolak dan dapat diulang sesudah sesi berakhir
27. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 56 {runId}`
28. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 56 {runId}`
29. Verifikasi pembatalan ditolak server dengan pesan `Error, handover is in progress for this asset.`
30. Maya meminta data tab Borrowed
31. Verifikasi baris aset `Laptop Dell Latitude 5420 - 56 {runId}` tetap berstatus `Waiting for Handover`
32. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 56 {runId}`
33. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 56 {runId}` sama dengan Custody pada langkah 27
34. Gita menekan `Cancel Request` pada sesi Handover baris aset `Laptop Dell Latitude 5420 - 56 {runId}`
35. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 56 {runId}`
36. Verifikasi pembatalan sesudah sesi Handover berakhir diterima server

### Pembatalan pada baris yang sudah dibatalkan Aktor Borrow ditolak
37. Gita membatalkan pinjaman baris aset `Laptop Dell Latitude 5420 - 57 {runId}`
38. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 57 {runId}`
39. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 57 {runId}`
40. Verifikasi pembatalan ditolak server karena baris sudah dibatalkan Aktor Borrow
41. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 57 {runId}`
42. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 57 {runId}` sama dengan Custody pada langkah 38
43. Maya meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 57 {runId}`
44. Verifikasi Borrow Log tetap memuat satu node `Canceled`, dari pembatalan oleh Gita

### Pembatalan ulang pada baris yang sudah Canceled tidak diproses ulang
45. Maya mengirim Cancel Borrow untuk baris aset `Laptop Dell Latitude 5420 - 51 {runId}` yang sudah `Canceled`
46. Verifikasi pembatalan kedua ditolak server karena baris sudah `Canceled`
47. Maya meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 51 {runId}`
48. Verifikasi Borrow Log tetap memuat satu node `Canceled`

### PIC pada baris Borrower tanpa akun yang sudah dibatalkan Aktor Borrow ditolak
49. Gita membatalkan pinjaman baris aset `Laptop Dell Latitude 5420 - 59 {runId}` milik Anton
50. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 59 {runId}`
51. Wulan mengirim Cancel Borrow atas nama Anton untuk baris aset `Laptop Dell Latitude 5420 - 59 {runId}`
52. Verifikasi pembatalan oleh PIC ditolak server karena baris sudah dibatalkan Aktor Borrow
53. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 59 {runId}`
54. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 59 {runId}` sama dengan Custody pada langkah 50
55. Wulan meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 59 {runId}`
56. Verifikasi Borrow Log tetap memuat satu node `Canceled`, dari pembatalan oleh Gita
