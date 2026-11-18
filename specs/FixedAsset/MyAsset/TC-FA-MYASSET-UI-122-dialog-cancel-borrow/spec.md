---
id: TC-FA-MYASSET-UI-122-dialog-cancel-borrow
title: "Dialog Cancel Borrow varian Borrower: isi, toast, dialog Borrow Already Canceled, dan penolakan sesi Handover"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-12", "V-02", "§1.2#r34", "§4.1b#r77", "§4.1b#r80", "§4.1b#r81", "§4.2.5#p14", "§4.2.5#p15", "§4.2.5#r7", "§Dialog aksi baris (tab Borrowed dan Assigned)#p3", "§Dialog aksi baris (tab Borrowed dan Assigned)#p4", "§4.4#r42", "§4.4#r43", "§7.2#r3", "§7.2#r4", "§7.3#r2", "§7.3#r14", "§7.3#r15", "§9.4.2#r72", "§9.4.2#r75", "§9.4.3#b5", "§9.6#r2", "§9.6#p1", "EB-FB-1@cancel-borrow", "EB-FB-2@cancel-borrow", "EB-ERR-1@cancel-borrow"]
smoke: []
dependsOn: []
trace:
  "FI-12": 56
  "V-02": [44, 56]
  "§1.2#r34": 44
  "§4.1b#r77": [4, 10]
  "§4.1b#r80": 18
  "§4.1b#r81": 44
  "§4.2.5#p14": [44, 45, 46, 47]
  "§4.2.5#p15": [50, 51, 61, 62, 63, 64, 66, 67]
  "§4.2.5#r7": 44
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p3": [4, 5, 6, 7, 8]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p4": [9, 10, 18, 44]
  "§4.4#r42": 44
  "§4.4#r43": [50, 51]
  "§7.2#r3": [44, 45, 46, 47]
  "§7.2#r4": [4, 5, 6, 7, 8, 9, 10]
  "§7.3#r2": [18, 30]
  "§7.3#r14": 56
  "§7.3#r15": 23
  "§9.4.2#r72": 44
  "§9.4.2#r75": 56
  "§9.4.3#b5": 10
  "§9.6#r2": [18, 23, 27, 39, 44]
  "§9.6#p1": [23, 24, 26, 35, 36, 38]
  "EB-FB-1@cancel-borrow": [18, 23, 30]
  "EB-FB-2@cancel-borrow": [13, 48]
  "EB-ERR-1@cancel-borrow": [23, 24, 25, 28, 30, 35, 36, 37]
anchor: [12]
coverage:
  web: automated
---

# Dialog Cancel Borrow varian Borrower: isi, toast, dialog Borrow Already Canceled, dan penolakan sesi Handover

## Prerequisites
- Aktor: Borrower `Budi Santoso` pada kondisi K1 sampai K5, dan PIC Borrower, yaitu PIC dari Borrower tanpa akun `Dewi Lestari`, pada kondisi K6.
- Layar awal: My Asset > Borrowed.
- Komponen: Dialog Cancel Borrow (D-BRW-01)
- Data:
  - DU-122-1: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Group `Head Office`, Status `Waiting for Approval`, Borrower `Me`, Transaction ID `BRW-2026-0153`, Source `Admin`, Duration `3 days`.
  - DU-122-2: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 7`, Asset ID `LPT-2026-0007`, Group `Head Office`, Status `Waiting for Handover`, Borrower `Me`, Transaction ID `BRW-2026-0153`, Source `Admin`, Duration `3 days`.
  - DU-122-4: baris Borrowed atas nama Borrower tanpa akun dengan Name `Laptop Dell Latitude 5420 - 18`, Asset ID `LPT-2026-0018`, Group `Head Office`, Status `Waiting for Approval`, Borrower `Dewi Lestari`, Transaction ID `BRW-2026-0166`, Source `Admin`, Duration `3 days`.
  - DU-122-3: penolakan karena baris sudah dibatalkan Aktor Borrow `Rina W` dengan pesan `Rina W already canceled this borrow.` dan `Your action was not saved.`.
- Kondisi:
  - K1: baris DU-122-1 tampil di tab Borrowed dan Cancel dijawab sukses.
  - K2: baris DU-122-1 tampil di tab Borrowed, Cancel pertama dijawab error server, pemuatan ulang tabel sesudahnya mengembalikan baris DU-122-1 tanpa perubahan, dan Cancel berikutnya dijawab sukses.
  - K3: baris DU-122-1 tampil di tab Borrowed, Cancel tidak mendapat respons karena koneksi terputus, dan pemuatan ulang tabel sesudahnya mengembalikan baris DU-122-1 tanpa perubahan.
  - K4: baris DU-122-1 tampil di tab Borrowed dan Cancel ditolak karena baris sudah dibatalkan Aktor Borrow (DU-122-3).
  - K5: baris DU-122-2 tampil di tab Borrowed dan Cancel ditolak karena sesi Handover baris itu sedang berjalan.
  - K6: baris DU-122-4 tampil di tab Borrowed dan Cancel ditolak karena baris sudah dibatalkan Aktor Borrow (DU-122-3).

## Test Steps

### Isi dialog Cancel Borrow dan Go Back menutup tanpa toast
1. Tampilkan Dialog Cancel Borrow dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
3. Klik `Cancel Borrow`
4. Verifikasi judul dialog `Cancel Borrow` tampil
5. Verifikasi nama aset `Laptop Dell Latitude 5420 - 8` tampil di body dialog
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
27. Verifikasi baris `Laptop Dell Latitude 5420 - 8` tetap tampil dengan Status `Waiting for Approval`
28. Verifikasi toast tidak memuat tombol aksi
29. Klik `[Cancel Borrow]`
30. Verifikasi toast `Success, borrow has been canceled.` tampil

### Koneksi terputus pada Cancel Borrow
31. Tampilkan Dialog Cancel Borrow dengan kondisi K3
32. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
33. Klik `Cancel Borrow`
34. Klik `[Cancel Borrow]`
35. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
36. Verifikasi dialog `Cancel Borrow` tetap terbuka
37. Verifikasi tombol `[Cancel Borrow]` aktif lagi
38. Verifikasi tabel My Asset dimuat ulang
39. Verifikasi baris `Laptop Dell Latitude 5420 - 8` tetap tampil dengan Status `Waiting for Approval`

### Baris sudah dibatalkan Aktor Borrow
40. Tampilkan Dialog Cancel Borrow dengan kondisi K4
41. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
42. Klik `Cancel Borrow`
43. Klik `[Cancel Borrow]`
44. Verifikasi dialog `Borrow Already Canceled` tampil
45. Verifikasi pesan `Rina W already canceled this borrow.` tampil
46. Verifikasi pesan `Your action was not saved.` tampil
47. Verifikasi dialog memuat tombol `[OK]`
48. Verifikasi toast tidak tampil
49. Klik `[OK]`
50. Verifikasi dialog `Borrow Already Canceled` tertutup
51. Verifikasi tabel My Asset dimuat ulang

### Sesi Handover baris sedang berjalan
52. Tampilkan Dialog Cancel Borrow dengan kondisi K5
53. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 7`
54. Klik `Cancel Borrow`
55. Klik `[Cancel Borrow]`
56. Verifikasi toast `Error, handover is in progress for this asset.` tampil

### PIC Borrower: baris sudah dibatalkan Aktor Borrow
57. Tampilkan Dialog Cancel Borrow dengan kondisi K6
58. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 18`
59. Klik `Cancel Borrow`
60. Klik `[Cancel Borrow]`
61. Verifikasi dialog `Borrow Already Canceled` tampil
62. Verifikasi pesan `Rina W already canceled this borrow.` tampil
63. Verifikasi pesan `Your action was not saved.` tampil
64. Verifikasi dialog memuat tombol `[OK]`
65. Klik `[OK]`
66. Verifikasi dialog `Borrow Already Canceled` tertutup
67. Verifikasi tabel My Asset dimuat ulang

[^drift-1]: Drift PRD vs foundation. PRD §9.6 Action Resilience Spec: gagal server (5xx atau timeout) pada Cancel Borrow memunculkan toast `T-BRW-26`. foundation `error-handling-convention.md` §2: Timeout / Network memunculkan `Connection problem. Please try again.` tanpa tombol aksi. Diasersi: foundation untuk koneksi terputus, karena toast kegagalan adalah pola bersama (SB-4); kegagalan server 5xx tetap memakai `T-BRW-26` dari PRD.
