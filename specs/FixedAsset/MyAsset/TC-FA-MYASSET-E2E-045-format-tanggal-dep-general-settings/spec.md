---
id: TC-FA-MYASSET-E2E-045-format-tanggal-dep-general-settings
title: "Perubahan Date Format dan Time Format General Settings sampai ke kolom tanggal My Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1b#r10", "EB-XM-1"]
smoke: []
dependsOn: ["General Settings: Date Format, Time Format, dan Time Zone", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#r10": [4, 5, 12, 13, 20, 21, 28, 29, 36, 37, 44, 45, 52, 53]
  "EB-XM-1": [4, 5, 12, 13, 20, 21, 28, 29, 36, 37, 44, 45, 52, 53]
anchor: []
coverage:
  web: automated
---

# Perubahan Date Format dan Time Format General Settings sampai ke kolom tanggal My Asset

## Prerequisites
- Aktor: Total Control `Anton Wijaya {runId}` (DU-045-1), yang juga Borrower atas pinjamannya sendiri dan dapat mengubah General Settings.
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-045-1: pengguna `Anton Wijaya {runId}`, role `Total Control`, Group `Head Office`.
  - DU-045-2: pinjaman aset `Laptop Acer Swift 3 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`.
  - DU-045-3: pinjaman aset `Proyektor Optoma HD146X {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Duration `6 hours`, Handed Over At `T0`, Due Date `T0 + 6 jam`.
  - DU-045-4: setting awal entitas Date Format `dd/MM/yy` dan Time Format `24h`.
  - DU-045-5: Date Format diubah ke `M/d/yy`.
  - DU-045-6: Date Format diubah ke `dd MMM yy`.
  - DU-045-7: Date Format diubah ke `DDD, MMM dd, yy`.
  - DU-045-8: Date Format diubah ke `DDD, MMM dd, yyyy`.
  - DU-045-9: Time Format diubah ke `12h`.
  - DU-045-10: setting awal entitas Time Zone `UTC`.
  - DU-045-11: Time Zone diubah ke `UTC+7`, sehingga jam yang tampil 7 jam lebih maju dari tampilan Time Zone `UTC`.
- Kondisi:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, karena mengubah setting format tanggal dan waktu tingkat entitas.
  - Date Format entitas bernilai `dd/MM/yy`, Time Format entitas bernilai `24h`, dan Time Zone entitas bernilai `UTC` saat langkah 1.
  - `T0` adalah waktu handover kedua pinjaman, yaitu waktu run. Tab Borrowed aktor memuat 2 baris, yaitu DU-045-2 dan DU-045-3.

## Test Steps

### Nilai awal Date Format `dd/MM/yy` dan Time Format `24h` tampil di kolom Due Date
1. Masuk sebagai Total Control `Anton Wijaya {runId}`
2. Buka `My Asset` dari menu profil pada navbar
3. Klik tab `Borrowed`
4. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `dd/MM/yy` tanpa jam
5. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `dd/MM/yy` dan Time Format `24h`

### Date Format `M/d/yy` sampai ke kolom Due Date
6. Buka General Settings
7. Pilih Date Format `M/d/yy`
8. Simpan perubahan General Settings
9. Buka `My Asset` dari menu profil pada navbar
10. Muat ulang halaman
11. Klik tab `Borrowed`
12. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `M/d/yy` tanpa jam
13. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `M/d/yy` dan Time Format `24h`

### Date Format `dd MMM yy` sampai ke kolom Due Date
14. Buka General Settings
15. Pilih Date Format `dd MMM yy`
16. Simpan perubahan General Settings
17. Buka `My Asset` dari menu profil pada navbar
18. Muat ulang halaman
19. Klik tab `Borrowed`
20. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `dd MMM yy` tanpa jam
21. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `dd MMM yy` dan Time Format `24h`

### Date Format `DDD, MMM dd, yy` sampai ke kolom Due Date
22. Buka General Settings
23. Pilih Date Format `DDD, MMM dd, yy`
24. Simpan perubahan General Settings
25. Buka `My Asset` dari menu profil pada navbar
26. Muat ulang halaman
27. Klik tab `Borrowed`
28. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `DDD, MMM dd, yy` tanpa jam
29. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `DDD, MMM dd, yy` dan Time Format `24h`

### Date Format `DDD, MMM dd, yyyy` sampai ke kolom Due Date
30. Buka General Settings
31. Pilih Date Format `DDD, MMM dd, yyyy`
32. Simpan perubahan General Settings
33. Buka `My Asset` dari menu profil pada navbar
34. Muat ulang halaman
35. Klik tab `Borrowed`
36. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `DDD, MMM dd, yyyy` tanpa jam
37. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `DDD, MMM dd, yyyy` dan Time Format `24h`

### Time Format `12h` sampai ke kolom Due Date
38. Buka General Settings
39. Pilih Time Format `12h`
40. Simpan perubahan General Settings
41. Buka `My Asset` dari menu profil pada navbar
42. Muat ulang halaman
43. Klik tab `Borrowed`
44. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Date Format `DDD, MMM dd, yyyy` tanpa jam
45. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Date Format `DDD, MMM dd, yyyy` dan Time Format `12h`

### Time Zone `UTC+7` sampai ke kolom Due Date
46. Buka General Settings
47. Pilih Time Zone `UTC+7`
48. Simpan perubahan General Settings
49. Buka `My Asset` dari menu profil pada navbar
50. Muat ulang halaman
51. Klik tab `Borrowed`
52. Verifikasi kolom `Due Date` pada baris `Laptop Acer Swift 3 {runId}` menampilkan tanggal `T0 + 3 hari` dalam Time Zone `UTC+7` dan Date Format `DDD, MMM dd, yyyy` tanpa jam
53. Verifikasi kolom `Due Date` pada baris `Proyektor Optoma HD146X {runId}` menampilkan tanggal dan jam `T0 + 6 jam` dalam Time Zone `UTC+7`, 7 jam lebih maju dari tampilan Time Zone `UTC`, dengan Date Format `DDD, MMM dd, yyyy` dan Time Format `12h`
