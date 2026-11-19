---
id: TC-FA-BORROW-E2E-024-return-hasil-damaged
title: "Report Damaged dari halaman Return memasang penanda Damaged pada baris Returned"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-137", "FI-BRW-138", "FI-BRW-139", "FI-BRW-140", "FI-BRW-141", "FI-BRW-142", "FI-BRW-143", "FI-BRW-144", "FI-BRW-145", "V-BRW-36"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-137": 17
  "FI-BRW-138": 23
  "FI-BRW-139": [26, 31, 40, 44, 46, 63]
  "FI-BRW-140": [49, 52]
  "FI-BRW-141": [55, 56]
  "FI-BRW-142": 59
  "FI-BRW-143": [60, 61]
  "FI-BRW-144": [60, 61, 62]
  "FI-BRW-145": 64
  "V-BRW-36": 19
anchor: [14, 54]
coverage:
  web: automated
---

# Report Damaged dari halaman Return memasang penanda Damaged pada baris Returned

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`, tanpa hak Aktor Damaged; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-024-1: BRW Group `Head Office`, Borrower `Lukman Hakim {runId}`, Photo at end OFF, berisi baris `Borrowed` aset DU-024-2, DU-024-3, DU-024-4, dan DU-024-5.
  - DU-024-2: aset `Laptop Lenovo Yoga {runId}`, TAG `RFID`; laporan yang dicoba: What happened `Layar retak setelah terjatuh`, diubah menjadi `Layar retak dan engsel longgar setelah terjatuh`, Photo `foto-kerusakan-laptop.jpg`.
  - DU-024-3: aset `Kamera Fuji X {runId}`, TAG `QR`; laporan yang dicoba: What happened `Lensa tergores`, Photo `foto-kerusakan-kamera.jpg`.
  - DU-024-4: aset `Mouse Logitech MX {runId}`, TAG `NFC`, dengan laporan Damaged buatan `Agus Pratama {runId}` berstatus `Waiting for Confirmation` (What happened `Tombol kiri tidak responsif`).
  - DU-024-5: aset `Headset Sony {runId}`, TAG `RFID`, dengan laporan Damaged buatan Borrower `Lukman Hakim {runId}` berstatus `Waiting for Confirmation` (What happened `Kabel putus di sambungan`).

## Test Steps

### Menyiapkan daftar Return dengan empat aset terverifikasi
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Borrowed Assets`
4. Ketik Search `Laptop Lenovo Yoga {runId}`, tekan Enter
5. Klik menu ⋯ pada baris aset DU-024-2
6. Klik `Return`
7. Klik `[+ Asset]`
8. Pilih aset DU-024-3, DU-024-4, dan DU-024-5 pada dialog Select Asset
9. Klik `[Select]`
10. Scan TAG aset DU-024-2 lewat `[Verify Asset]`
11. Scan TAG aset DU-024-3 lewat `[Verify Asset]`
12. Scan TAG aset DU-024-4 lewat `[Verify Asset]`
13. Scan TAG aset DU-024-5 lewat `[Verify Asset]`
14. Verifikasi baris DU-024-2, DU-024-3, DU-024-4, dan DU-024-5 `Verified`

### Report Damaged dari halaman Return mewajibkan Photo dan What happened
15. Klik menu ⋯ pada baris DU-024-2
16. Klik `Report Damaged`
17. Verifikasi dialog `Report Damaged` tampil dengan field Photo dan What happened
18. Klik `[Report]`
19. Verifikasi caption `Photo must not be empty` dan `What happened must not be empty` tampil
20. Unggah Photo `foto-kerusakan-laptop.jpg`
21. Isi What happened dengan `Layar retak setelah terjatuh`
22. Klik `[Report]`
23. Verifikasi kolom Status baris DU-024-2 menampilkan badge `Reported Damaged` karena laporan baru tersimpan saat `[Submit]`

### Laporan yang dibuat di halaman Return diperbaiki atau dibuang bersama asetnya
24. Klik menu ⋯ pada baris DU-024-2
25. Klik `Edit Damage Report`
26. Verifikasi dialog `Report Damaged` terisi Photo `foto-kerusakan-laptop.jpg` dan What happened `Layar retak setelah terjatuh`
27. Isi What happened dengan `Layar retak dan engsel longgar setelah terjatuh`
28. Klik `[Report]`
29. Klik menu ⋯ pada baris DU-024-2
30. Klik `Edit Damage Report`
31. Verifikasi dialog `Report Damaged` terisi What happened `Layar retak dan engsel longgar setelah terjatuh`
32. Klik `[Report]`
33. Klik menu ⋯ pada baris DU-024-3
34. Klik `Report Damaged`
35. Unggah Photo `foto-kerusakan-kamera.jpg`
36. Isi What happened dengan `Lensa tergores`
37. Klik `[Report]`
38. Klik menu ⋯ pada baris DU-024-3
39. Klik `Remove from List`
40. Verifikasi baris DU-024-3 hilang dari daftar beserta laporannya
41. Klik `[+ Asset]`
42. Pilih aset DU-024-3 pada dialog Select Asset
43. Klik `[Select]`
44. Verifikasi baris DU-024-3 kembali ke daftar dengan Verification `Unverified`
45. Klik menu ⋯ pada baris DU-024-3
46. Verifikasi menu ⋯ baris DU-024-3 memuat `Report Damaged` dan `Remove from List`, serta tidak memuat `Edit Damage Report`, karena laporan yang terbuang tidak ikut kembali
47. Klik `Remove from List`

### Cancel Damage Report hanya untuk laporan milik pengguna sendiri
48. Klik menu ⋯ pada baris DU-024-4
49. Verifikasi menu ⋯ baris DU-024-4 memuat `Cancel Damage Report` karena laporannya milik Aktor ini dan masih `Waiting for Confirmation`
50. Klik `Cancel Damage Report`
51. Klik tombol konfirmasi pada dialog Cancel Damage Report
52. Verifikasi badge `Reported Damaged` pada baris DU-024-4 hilang
53. Klik menu ⋯ pada baris DU-024-5
54. Verifikasi menu ⋯ baris DU-024-5 memuat `Remove from List`
55. Verifikasi menu ⋯ baris DU-024-5 tidak memuat `Cancel Damage Report` karena laporan Borrower tidak diubah dari halaman ini
56. Verifikasi menu ⋯ baris DU-024-5 tidak memuat `Edit Damage Report` dan `Report Damaged` karena laporan Borrower tidak diubah dari halaman ini
57. Tekan Esc untuk menutup menu ⋯

### Submit mengembalikan semua aset dengan penanda Damaged mengikuti record
58. Klik `[Submit]`
59. Verifikasi halaman Borrow Detail BRW milik DU-024-1 tampil dengan baris aset DU-024-2, DU-024-4, dan DU-024-5 `Returned`
60. Verifikasi baris aset DU-024-2 `Returned` dengan penanda `Damaged` dari laporan yang dibuat pada halaman Return
61. Verifikasi baris aset DU-024-5 `Returned` dengan penanda `Damaged` dari laporan Borrower yang ditautkan
62. Verifikasi baris aset DU-024-4 `Returned` tanpa penanda `Damaged` karena laporannya dibatalkan
63. Verifikasi baris aset DU-024-3 tetap `Borrowed` tanpa badge `Reported Damaged`
64. Verifikasi baris aset DU-024-2 dan DU-024-5 `Returned` tanpa menunggu keputusan atas laporan `Waiting for Confirmation`
