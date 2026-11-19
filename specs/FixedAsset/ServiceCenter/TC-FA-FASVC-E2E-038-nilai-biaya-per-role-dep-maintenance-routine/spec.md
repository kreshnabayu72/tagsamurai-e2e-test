---
id: TC-FA-FASVC-E2E-038-nilai-biaya-per-role-dep-maintenance-routine
title: "Nilai Biaya di Tab Usage: Tampil bagi Role Berhak dan Download"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r6", "§4.8#r9", "§2.1#b3", "§2.2#r2", "§9.4.3#b6"]
smoke: []
dependsOn: ["Maintenance Routine: Task"]
trace:
  "§2.1#r6": [3, 6, 7, 21, 22, 23, 28, 29, 30, 35, 36, 37, 42, 43, 44]
  "§4.8#r9": [3, 21, 22, 23, 28, 29, 30, 35, 36, 37, 42, 43, 44]
  "§2.1#b3": [3, 4, 5, 6, 7, 10, 13, 16, 21, 22, 23, 28, 29, 30, 35, 36, 37, 42, 43, 44]
  "§2.2#r2": [3, 4, 5, 21, 22, 23, 28, 29, 30, 35, 36, 37, 42, 43, 44]
  "§9.4.3#b6": 16
anchor: []
coverage:
  web: automated
---

# Nilai Biaya di Tab Usage: Tampil bagi Role Berhak dan Download

## Prerequisites
- Aktor: Read Only `Gita Ramadhani {runId}`, cakupan Group `Cabang Biaya {runId}`. Aktor lain: Asset Admin `Hari Setiawan {runId}` tanpa Role Transaksi Maintenance Routine maupun Repair; Total Control `Taufik Hidayat {runId}`, Group Manager `Gina Marlina {runId}`, Asset Admin pemegang Role Transaksi Maintenance Routine `Joko Wibowo {runId}`, dan Monitoring & Report `Maya Kusuma {runId}`.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-038-1: Group `Cabang Biaya {runId}`.
  - DU-038-2: User `Gita Ramadhani {runId}`, Role Read Only, cakupan Group `Cabang Biaya {runId}`.
  - DU-038-3: User `Hari Setiawan {runId}`, Role Asset Admin tanpa Role Transaksi Maintenance Routine maupun Repair, cakupan Group `Cabang Biaya {runId}`.
  - DU-038-4: Service Center `Teknik Biaya Terukur {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Biaya {runId}`, City `Makassar`.
  - DU-038-5: Task aset `Panel Biaya Satu {runId}`, Status `Completed`, Result `Normal`, selesai `T0 − 7 hari, pukul 10:30`, pelaksana `Teknik Biaya Terukur {runId}`, total biaya `1500000`.
  - DU-038-6: Task aset `Pompa Biaya Dua {runId}`, Status `Completed`, Result `Needs attention`, selesai `T0 − 12 hari, pukul 15:45`, pelaksana `Teknik Biaya Terukur {runId}`, total biaya `500000`.
  - DU-038-8: User `Taufik Hidayat {runId}`, Role Total Control.
  - DU-038-9: User `Gina Marlina {runId}`, Role Group Manager, cakupan Group `Cabang Biaya {runId}`.
  - DU-038-10: User `Joko Wibowo {runId}`, Role Asset Admin dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Biaya {runId}`.
  - DU-038-11: User `Maya Kusuma {runId}`, Role Monitoring & Report dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Biaya {runId}`.
  - DU-038-7: Task aset `Mesin Biaya Tiga {runId}`, Status `Completed`, Result `Normal`, selesai `T0 − 3 hari, pukul 09:20`, pelaksana `Teknik Biaya Terukur {runId}`, tanpa baris biaya.
  - Mata uang General Settings bernilai `IDR`, sehingga nilai biaya tampil dengan mata uang dan 2 desimal, misalnya `Rp 1.500.000,00`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Akun semua user di Data aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Kolom Cost dan ringkasan biaya tampil bagi role yang berhak
1. Ketik Search `Teknik Biaya Terukur {runId}`, tekan Enter
2. Klik angka Usage pada baris `Teknik Biaya Terukur {runId}`
3. Verifikasi kolom `Cost` tampil di tabel tab Usage
4. Verifikasi baris Task aset `Panel Biaya Satu {runId}` menampilkan Cost `Rp 1.500.000,00`
5. Verifikasi baris Task aset `Pompa Biaya Dua {runId}` menampilkan Cost `Rp 500.000,00`
6. Verifikasi ringkasan `Total cost` tampil bernilai `Rp 2.000.000,00`, jumlah Cost Task `Completed` yang memiliki biaya
7. Verifikasi ringkasan `Avg cost per task` tampil bernilai `Rp 1.000.000,00`, yaitu `Rp 2.000.000,00` dibagi 2 Task `Completed` yang memiliki biaya (Task `Mesin Biaya Tiga {runId}` tanpa baris biaya tidak dihitung)

### Kolom Cost ikut di Download tab Usage
8. Klik `Download`
9. Pilih `Download as CSV`
10. Verifikasi berkas `Service-Center-Usage.csv` memuat kolom `Cost` yang terisi untuk baris Task aset `Panel Biaya Satu {runId}` dan `Pompa Biaya Dua {runId}`
11. Klik `Download`
12. Pilih `Download as XLSX`
13. Verifikasi berkas `Service-Center-Usage.xlsx` memuat kolom `Cost` yang terisi untuk baris Task aset `Panel Biaya Satu {runId}` dan `Pompa Biaya Dua {runId}`

### Role tanpa hak atas Service Center tidak melihat nilai biaya
14. Masuk sebagai Asset Admin `Hari Setiawan {runId}`
15. Buka URL Detail Service Center `Teknik Biaya Terukur {runId}` pada tab Usage secara langsung
16. Verifikasi empty state `You do not have access to Service Center.` tampil tanpa kolom `Cost`, `Total cost`, dan `Avg cost per task`

### Kolom Cost dan ringkasan biaya tampil bagi Total Control
17. Masuk sebagai Total Control `Taufik Hidayat {runId}`
18. Buka Add-ons > Service Center
19. Ketik Search `Teknik Biaya Terukur {runId}`, tekan Enter
20. Klik angka Usage pada baris `Teknik Biaya Terukur {runId}`
21. Verifikasi baris Task aset `Panel Biaya Satu {runId}` menampilkan Cost `Rp 1.500.000,00`
22. Verifikasi ringkasan `Total cost` tampil bernilai `Rp 2.000.000,00`
23. Verifikasi ringkasan `Avg cost per task` tampil bernilai `Rp 1.000.000,00`

### Kolom Cost dan ringkasan biaya tampil bagi Group Manager
24. Masuk sebagai Group Manager `Gina Marlina {runId}`
25. Buka Add-ons > Service Center
26. Ketik Search `Teknik Biaya Terukur {runId}`, tekan Enter
27. Klik angka Usage pada baris `Teknik Biaya Terukur {runId}`
28. Verifikasi baris Task aset `Panel Biaya Satu {runId}` menampilkan Cost `Rp 1.500.000,00`
29. Verifikasi ringkasan `Total cost` tampil bernilai `Rp 2.000.000,00`
30. Verifikasi ringkasan `Avg cost per task` tampil bernilai `Rp 1.000.000,00`

### Kolom Cost dan ringkasan biaya tampil bagi Asset Admin pemegang Role Transaksi Maintenance Routine
31. Masuk sebagai Asset Admin `Joko Wibowo {runId}`
32. Buka Add-ons > Service Center
33. Ketik Search `Teknik Biaya Terukur {runId}`, tekan Enter
34. Klik angka Usage pada baris `Teknik Biaya Terukur {runId}`
35. Verifikasi baris Task aset `Panel Biaya Satu {runId}` menampilkan Cost `Rp 1.500.000,00`
36. Verifikasi ringkasan `Total cost` tampil bernilai `Rp 2.000.000,00`
37. Verifikasi ringkasan `Avg cost per task` tampil bernilai `Rp 1.000.000,00`

### Kolom Cost dan ringkasan biaya tampil bagi Monitoring & Report
38. Masuk sebagai Monitoring & Report `Maya Kusuma {runId}`
39. Buka Add-ons > Service Center
40. Ketik Search `Teknik Biaya Terukur {runId}`, tekan Enter
41. Klik angka Usage pada baris `Teknik Biaya Terukur {runId}`
42. Verifikasi baris Task aset `Panel Biaya Satu {runId}` menampilkan Cost `Rp 1.500.000,00`
43. Verifikasi ringkasan `Total cost` tampil bernilai `Rp 2.000.000,00`
44. Verifikasi ringkasan `Avg cost per task` tampil bernilai `Rp 1.000.000,00`
