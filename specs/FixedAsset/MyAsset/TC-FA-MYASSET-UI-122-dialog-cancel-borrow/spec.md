---
id: TC-FA-MYASSET-UI-122-dialog-cancel-borrow
title: "Dialog Cancel Borrow varian Borrower: isi, toast, dialog Borrow Already Canceled, dan penolakan sesi Handover"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FI-12", "V-02", "§1.2#r34", "§4.1b#r77", "§4.1b#r80", "§4.1b#r81", "§4.2.5#p14", "§4.2.5#p15", "§4.2.5#r7", "§Dialog aksi baris (tab Borrowed dan Assigned)#p3", "§Dialog aksi baris (tab Borrowed dan Assigned)#p4", "§4.4#r42", "§4.4#r43", "§7.2#r3", "§7.2#r4", "§7.3#r2", "§7.3#r14", "§7.3#r15", "§9.4.2#r72", "§9.4.2#r75", "§9.4.3#b5", "§9.6#r2", "§9.6#p1", "EB-FB-1@cancel-borrow", "EB-FB-2@cancel-borrow", "EB-ERR-1@cancel-borrow"]
smoke: []
dependsOn: []
trace:
  "FI-12": 54
  "V-02": [42, 54]
  "§1.2#r34": 42
  "§4.1b#r77": [4, 10]
  "§4.1b#r80": 18
  "§4.1b#r81": 42
  "§4.2.5#p14": [42, 43, 44, 45]
  "§4.2.5#p15": [48, 49]
  "§4.2.5#r7": 42
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p3": [4, 5, 6, 7, 8]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p4": [9, 10, 18, 42]
  "§4.4#r42": 42
  "§4.4#r43": [48, 49]
  "§7.2#r3": [42, 43, 44, 45]
  "§7.2#r4": [4, 5, 6, 7, 8, 9, 10]
  "§7.3#r2": [18, 29]
  "§7.3#r14": 54
  "§7.3#r15": 23
  "§9.4.2#r72": 42
  "§9.4.2#r75": 54
  "§9.4.3#b5": 10
  "§9.6#r2": [18, 23, 42]
  "§9.6#p1": [23, 24, 26, 34, 35, 37]
  "EB-FB-1@cancel-borrow": [18, 23, 29]
  "EB-FB-2@cancel-borrow": [13, 46]
  "EB-ERR-1@cancel-borrow": [23, 24, 25, 27, 29, 34, 35, 36]
anchor: [12]
coverage:
  web: automated
---

# Dialog Cancel Borrow varian Borrower: isi, toast, dialog Borrow Already Canceled, dan penolakan sesi Handover

## Prerequisites
- Aktor: Borrower `Budi Santoso`.
- Layar awal: My Asset > Borrowed.
- Komponen: Dialog Cancel Borrow (D-BRW-01)
- Data:
  - DU-122-1: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Group `Head Office`, Status `Waiting for Approval`, Borrower `Me`, Transaction ID `BRW-2026-0153`, Source `Admin`, Duration `3 days`.
  - DU-122-2: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 7`, Asset ID `LPT-2026-0007`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Me`, Transaction ID `BRW-2026-0153`, Source `Admin`, Duration `3 days`.
  - DU-122-3: penolakan karena baris sudah dibatalkan Aktor Borrow `Rina W` dengan pesan `Rina W already canceled this borrow.` dan `Your action was not saved.`.
- Kondisi:
  - K1: baris DU-122-1 tampil di tab Borrowed dan Cancel dijawab sukses.
  - K2: baris DU-122-1 tampil di tab Borrowed, Cancel pertama dijawab error server, dan Cancel berikutnya dijawab sukses.
  - K3: baris DU-122-1 tampil di tab Borrowed dan Cancel tidak mendapat respons karena koneksi terputus.
  - K4: baris DU-122-1 tampil di tab Borrowed dan Cancel ditolak karena baris sudah dibatalkan Aktor Borrow (DU-122-3).
  - K5: baris DU-122-2 tampil di tab Borrowed dan Cancel ditolak karena sesi Handover baris itu sedang berjalan.

## Test Steps

### Isi dialog Cancel Borrow dan Go Back menutup tanpa toast
1. Tampilkan Dialog Cancel Borrow dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
3. Klik `Cancel Borrow`
4. Verifikasi judul dialog `Cancel Borrow` tampil
5. Verifikasi nama aset `Laptop Dell Latitude 5420 - 8` tampil sebagai satu bullet
6. Verifikasi teks `The asset becomes available again and the Asset Admin is notified.` tampil
7. Verifikasi teks `Are you sure you want to cancel it?` tampil
8. Verifikasi tombol `[Go Back]` dan `[Cancel Borrow]` tampil
9. Verifikasi dialog tidak memuat field Reason
10. Verifikasi dialog tidak memuat checkbox `Save as Draft to edit`
11. Klik `[Go Back]`
12. Verifikasi dialog `Cancel Borrow` tertutup
13. Verifikasi toast tidak tampil

### Cancel Borrow berhasil
14. Tampilkan Dialog Cancel Borrow dengan kondisi K1
15. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
16. Klik `Cancel Borrow`
17. Klik `[Cancel Borrow]`
18. Verifikasi toast `Success, borrow has been canceled.` tampil

### Gagal server pada Cancel Borrow lalu dicoba ulang
19. Tampilkan Dialog Cancel Borrow dengan kondisi K2
20. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
21. Klik `Cancel Borrow`
22. Klik `[Cancel Borrow]`
23. Verifikasi toast `Error, failed to cancel borrow.` tampil
24. Verifikasi dialog `Cancel Borrow` tetap terbuka
25. Verifikasi tombol `[Cancel Borrow]` aktif lagi
26. Verifikasi tabel My Asset dimuat ulang
27. Verifikasi toast tidak memuat tombol aksi
28. Klik `[Cancel Borrow]`
29. Verifikasi toast `Success, borrow has been canceled.` tampil

### Koneksi terputus pada Cancel Borrow
30. Tampilkan Dialog Cancel Borrow dengan kondisi K3
31. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
32. Klik `Cancel Borrow`
33. Klik `[Cancel Borrow]`
34. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
35. Verifikasi dialog `Cancel Borrow` tetap terbuka
36. Verifikasi tombol `[Cancel Borrow]` aktif lagi
37. Verifikasi tabel My Asset dimuat ulang

### Baris sudah dibatalkan Aktor Borrow
38. Tampilkan Dialog Cancel Borrow dengan kondisi K4
39. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
40. Klik `Cancel Borrow`
41. Klik `[Cancel Borrow]`
42. Verifikasi dialog `Borrow Already Canceled` tampil
43. Verifikasi pesan `Rina W already canceled this borrow.` tampil
44. Verifikasi pesan `Your action was not saved.` tampil
45. Verifikasi dialog memuat tombol `[OK]`
46. Verifikasi toast tidak tampil
47. Klik `[OK]`
48. Verifikasi dialog `Borrow Already Canceled` tertutup
49. Verifikasi tabel My Asset dimuat ulang

### Sesi Handover baris sedang berjalan
50. Tampilkan Dialog Cancel Borrow dengan kondisi K5
51. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 7`
52. Klik `Cancel Borrow`
53. Klik `[Cancel Borrow]`
54. Verifikasi toast `Error, handover is in progress for this asset.` tampil

[^drift-1]: Drift PRD vs foundation. PRD §9.6 Action Resilience Spec: gagal server (5xx atau timeout) pada Cancel Borrow memunculkan toast `T-BRW-26`. foundation `error-handling-convention.md` §2: Timeout / Network memunculkan `Connection problem. Please try again.` tanpa tombol aksi. Diasersi: foundation untuk koneksi terputus, karena toast kegagalan adalah pola bersama (SB-4); kegagalan server 5xx tetap memakai `T-BRW-26` dari PRD.
