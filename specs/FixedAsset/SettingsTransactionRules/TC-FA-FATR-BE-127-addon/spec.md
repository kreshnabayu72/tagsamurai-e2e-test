---
id: TC-FA-FATR-BE-127-addon
title: "Gerbang addon Audit dan Maintenance di server"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.2#b563", "§9.2#b567", "§9.2#b562", "§9.4.2#r66", "§9.4.2#r69", "§9.4.2#r72", "§9.10.5#b1", "§9.10.5#b2", "§9.10.5#b6", "§9.2#b361", "§9.2#b341", "§9.4.2#r67", "§9.2#b561", "§9.10.5#b5"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.2#b361": [2, 3, 4, 6, 26, 27, 28, 30, 31]
  "§9.2#b562": [9, 18, 37]
  "§9.10.5#b6": [9, 18, 37]
  "§9.2#b563": [11, 12]
  "§9.4.2#r69": [11, 12, 27]
  "§9.10.5#b1": [12, 15]
  "§9.4.2#r66": [14, 15]
  "§9.2#b567": [20, 21]
  "§9.4.2#r72": [20, 21, 23, 24, 28, 31]
  "§9.10.5#b2": [21, 24]
  "§9.2#b341": [27, 28, 31]
  "§9.4.2#r67": [27, 28, 34]
  "§9.2#b561": [23, 24, 33, 34]
  "§9.10.5#b5": [24, 34]
anchor: []
---

# Gerbang addon Audit dan Maintenance di server

## Prerequisites
- Aktor: Admin `Rangga Pratama {runId}` (Total Control entitas khusus; mengubah setting Transaction Settings dan menjalankan Export rules). Operator Admin Console (di luar tenant, hanya untuk mencabut dan mengalokasikan kembali lisensi addon pada subscription FAMS entitas).
- Data:
  - DU-127-1: Entitas `Citra Gerbang Addon {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan transaksi Borrow. Subscription FAMS-nya memiliki alokasi lisensi addon Audit dan Maintenance, sehingga kedua addon aktif sampai Operator mencabut alokasinya.
  - DU-127-2: User `Rangga Pratama {runId}`, Role `Total Control entitas`; Admin yang mengubah setting.
  - DU-127-3: Category `Panel Listrik {runId}`, Category leaf tingkat teratas; Reminder before due `7` sebagai nilai Category.
  - DU-127-4: Pengaturan Company default tab Audit: Grace period `5`.
  - DU-127-5: Pengaturan Company default tab Geolocation: Require location Audit `ON`, Require location Maintenance `ON`.
  - DU-127-6: Perubahan Grace period tab Audit menjadi `9`.
  - DU-127-7: Perubahan Require location Audit menjadi `OFF`.
  - DU-127-8: Perubahan Reminder before due Category `Panel Listrik {runId}` menjadi `9`.
  - DU-127-9: Perubahan Require location Maintenance menjadi `OFF`.
- Kondisi:
  - Akun Admin `Rangga Pratama {runId}` aktif dan kredensialnya disediakan fase 2.
  - Jumlah entri Changelog Transaction Settings dibaca sebagai selisih terhadap jumlah yang dicatat sebelum aksi.

## Test Steps

### Addon aktif: field tab `Audit` dan `Maintenance` serta baris Require location ikut diekspor
1. Admin `Rangga Pratama {runId}` menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
2. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Audit`, Field `Grace period`, karena addon `Audit` aktif
3. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Audit`, Field `Require location`, karena addon `Audit` aktif
4. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Maintenance`, Field `Require location`, karena addon Maintenance aktif
5. Admin menjalankan Export rules dengan Category `Panel Listrik {runId}` terpilih di Sidebar Category Tree
6. Verifikasi sheet Rules memuat baris Category `Panel Listrik {runId}`, Transaction `Maintenance`, Field `Reminder before due`, karena addon Maintenance aktif

### Addon `Audit` tidak aktif: server menolak perubahan tab `Audit` dan Require location baris `Audit`
7. Catat jumlah entri Changelog Transaction Settings
8. Operator mencabut alokasi lisensi addon `Audit` dari subscription FAMS entitas `Citra Gerbang Addon {runId}`
9. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan status addon `Audit`
10. Admin mengirim perubahan Grace period pada tab `Audit` menjadi `9`
11. Verifikasi server menolak perubahan Grace period pada tab `Audit` menjadi `9` karena addon `Audit` tidak aktif
12. Verifikasi Grace period pada tab `Audit` tetap `5` sebagai nilai tersimpan
13. Admin mengirim perubahan Require location baris `Audit` menjadi `OFF`
14. Verifikasi server menolak perubahan Require location baris `Audit` menjadi `OFF` karena addon `Audit` tidak aktif
15. Verifikasi Require location baris `Audit` tetap `ON` sebagai nilai tersimpan

### Addon Maintenance tidak aktif: server menolak perubahan tab Maintenance dan Require location Maintenance
16. Catat jumlah entri Changelog Transaction Settings
17. Operator mencabut alokasi lisensi addon Maintenance dari subscription FAMS entitas `Citra Gerbang Addon {runId}`
18. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan status addon Maintenance
19. Admin mengirim perubahan Reminder before due Category `Panel Listrik {runId}` menjadi `9`
20. Verifikasi server menolak perubahan Reminder before due Category `Panel Listrik {runId}` menjadi `9` karena addon Maintenance tidak aktif
21. Verifikasi Reminder before due Category `Panel Listrik {runId}` tetap `7` sebagai nilai tersimpan
22. Admin mengirim perubahan Require location Maintenance menjadi `OFF`
23. Verifikasi server menolak perubahan Require location Maintenance menjadi `OFF` karena addon Maintenance tidak aktif
24. Verifikasi Require location Maintenance tetap `ON` sebagai nilai tersimpan

### Export tanpa addon Audit dan Maintenance: nilai tersimpan tidak diekspor
25. Admin menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
26. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Borrow`, Field `Max duration`
27. Verifikasi sheet Rules tidak memuat baris Transaction `Audit`, Field `Grace period` maupun Field `Require location`
28. Verifikasi sheet Rules tidak memuat baris Transaction `Maintenance`, Field `Require location`
29. Admin menjalankan Export rules dengan Category `Panel Listrik {runId}` terpilih di Sidebar Category Tree
30. Verifikasi sheet Rules memuat baris Category `Panel Listrik {runId}`, Transaction `Borrow`, Field `Max duration`
31. Verifikasi sheet Rules tidak memuat baris Category `Panel Listrik {runId}`, Transaction `Maintenance`, Field `Reminder before due`

### Kedua addon tidak aktif: Require location tersimpan dipertahankan dan perubahannya ditolak
32. Admin mengirim perubahan Require location baris `Audit` menjadi `OFF`
33. Verifikasi server menolak perubahan Require location baris `Audit` menjadi `OFF` karena addon `Audit` dan addon Maintenance sama-sama tidak aktif
34. Verifikasi Require location baris `Audit` tetap `ON` sebagai nilai tersimpan

### Alokasi addon dikembalikan: perubahan status addon bukan perubahan Settings
35. Catat jumlah entri Changelog Transaction Settings
36. Operator mengalokasikan kembali lisensi addon `Audit` ke subscription FAMS entitas `Citra Gerbang Addon {runId}`
37. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan status addon `Audit`
