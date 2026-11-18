---
id: TC-FA-BORROW-E2E-024-return-hasil-damaged
title: "Report Damaged dari halaman Return memasang penanda Damaged pada baris Returned"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-137", "FI-BRW-138", "FI-BRW-139", "FI-BRW-140", "FI-BRW-141", "FI-BRW-142", "FI-BRW-143", "FI-BRW-144", "FI-BRW-145", "V-BRW-36"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-137": 17
  "FI-BRW-138": 23
  "FI-BRW-139": [26, 36, 51]
  "FI-BRW-140": [38, 41]
  "FI-BRW-141": 44
  "FI-BRW-142": 47
  "FI-BRW-143": [48, 49]
  "FI-BRW-144": [48, 49, 50]
  "FI-BRW-145": 52
  "V-BRW-36": 19
anchor: [14, 43]
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
26. Verifikasi dialog `Report Damaged` terisi What happened `Layar retak setelah terjatuh`
27. Isi What happened dengan `Layar retak dan engsel longgar setelah terjatuh`
28. Klik `[Report]`
29. Klik menu ⋯ pada baris DU-024-3
30. Klik `Report Damaged`
31. Unggah Photo `foto-kerusakan-kamera.jpg`
32. Isi What happened dengan `Lensa tergores`
33. Klik `[Report]`
34. Klik menu ⋯ pada baris DU-024-3
35. Klik `Remove from List`
36. Verifikasi baris DU-024-3 hilang dari daftar beserta laporannya

### Cancel Damage Report hanya untuk laporan milik pengguna sendiri
37. Klik menu ⋯ pada baris DU-024-4
38. Verifikasi menu ⋯ baris DU-024-4 memuat `Cancel Damage Report` karena laporannya milik Aktor ini dan masih `Waiting for Confirmation`
39. Klik `Cancel Damage Report`
40. Klik tombol konfirmasi pada dialog Cancel Damage Report
41. Verifikasi badge `Reported Damaged` pada baris DU-024-4 hilang
42. Klik menu ⋯ pada baris DU-024-5
43. Verifikasi menu ⋯ baris DU-024-5 memuat `Remove from List`
44. Verifikasi menu ⋯ baris DU-024-5 tidak memuat `Cancel Damage Report` karena laporan Borrower tidak diubah dari halaman ini
45. Tekan Esc untuk menutup menu ⋯

### Submit mengembalikan semua aset dengan penanda Damaged mengikuti record
46. Klik `[Submit]`
47. Verifikasi halaman Borrow Detail BRW milik DU-024-1 tampil dengan baris aset DU-024-2, DU-024-4, dan DU-024-5 `Returned`
48. Verifikasi baris aset DU-024-2 `Returned` dengan penanda `Damaged` dari laporan yang dibuat pada halaman Return
49. Verifikasi baris aset DU-024-5 `Returned` dengan penanda `Damaged` dari laporan Borrower yang ditautkan, tanpa laporan kedua
50. Verifikasi baris aset DU-024-4 `Returned` tanpa penanda `Damaged` karena laporannya dibatalkan
51. Verifikasi baris aset DU-024-3 tetap `Borrowed` tanpa badge `Reported Damaged`
52. Verifikasi baris aset DU-024-2 dan DU-024-5 `Returned` tanpa menunggu keputusan atas laporan `Waiting for Confirmation`
