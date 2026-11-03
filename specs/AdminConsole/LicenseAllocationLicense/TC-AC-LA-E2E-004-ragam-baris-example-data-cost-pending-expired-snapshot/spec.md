---
id: TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot
title: "Ragam Baris Example Data: Cost Snapshot, Term Pending, Expired, dan Plan Snapshot"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-23
  - TC-AC-LA-24
  - TC-AC-LA-25
  - TC-AC-LA-26
  - TC-AC-LA-27
coverage:
  web: automated
---

# Ragam Baris Example Data: Cost Snapshot, Term Pending, Expired, dan Plan Snapshot

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #19 PT Sejahtera (diubah namanya sementara di TC-AC-LA-27 lalu dipulihkan), #46 alokasi `Completed` berstatus lisensi `Pending` (Concurrent User +10, Toko Serba Ada, `SUBS-20260819-00001`, Cost $3,650.00), #48 alokasi `Canceled` (Cost $150.00), #50 alokasi `Rejected` (Cost $225.00), #51 alokasi `Expired` (Concurrent User +3, PT Abadi Jaya), #52 alokasi `Active` Storage +50 GB (Cost $100.00), dan satu alokasi `Active` dengan Plan snapshot `Professional` pada seed #54. Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seedStorage, seed48, seed50, seed46, seed51, seedActiveProfessional).
- Kemampuan teknis: baca saldo kantong Distributor PT Maju Bersama; ubah nama Client dan ubah Plan term lewat Push Update Plans & Features; pulihkan nama Client dan Plan term. Seluruhnya disediakan tim FE/BE lewat fixture backend (S-06, pengecualian 2026-10-30).
- State Pre-setup yang berubah: nama Client PT Sejahtera menjadi `PT Sejahtera Makmur` dan Plan term Client; keduanya dipulihkan fixture backend di langkah penghubung akhir spec dan di hook `after`. Efeknya: Last Updated Client dan entri audit trail Client bertambah; suite berjalan serial.
- Konfigurasi kolom Setup Column yang disimpan spec (kolom Plan dan Cost) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-23: Baris Storage tampil Quantity berformat plus N GB

1. Klik ikon `⋯` pada header kolom, lalu klik `Setup Column...`
2. Centang kolom Plan dan Cost, lalu klik `[Save]`
3. Ketik Search Allocation ID seed Storage +50 GB (`Fixture.license-allocation-license.seedStorage`), tekan Enter
4. Verifikasi Quantity baris Storage: `+50 GB`
5. Verifikasi Cost baris Storage: `$100.00`

### TC-AC-LA-24: Cost snapshot alokasi Rejected dan Canceled

6. Klik `(←)` pada kotak Search
7. Klik tab `History`
8. Catat saldo kantong Distributor PT Maju Bersama sebagai baseline
9. Ketik Search Allocation ID seed `Rejected` milik `Dewi A` (`Fixture.license-allocation-license.seed50`), tekan Enter
10. Verifikasi Cost baris `Rejected`: `$225.00`
11. Ganti isi kotak search dengan Allocation ID seed `Canceled` milik `Dewi A` (`Fixture.license-allocation-license.seed48`), tekan Enter
12. Verifikasi Cost baris `Canceled`: `$150.00`
13. Verifikasi saldo kantong Distributor PT Maju Bersama sama dengan baseline (tidak berkurang oleh kedua alokasi itu)

### TC-AC-LA-25: Alokasi ke term Pending berstatus Pending di tab Current

14. Klik `(←)` pada kotak Search, lalu klik tab `Current`
15. Ketik Search `SUBS-20260819-00001`, tekan Enter
16. Verifikasi baris Concurrent User +10 pada Toko Serba Ada tampil pada tab Current
17. Verifikasi Status baris: `Pending` dengan severity warning
18. Verifikasi Cost baris: `$3,650.00`

### TC-AC-LA-26: Baris Expired di tab History dengan Last Updated saat transisi

19. Klik tab `History`
20. Ketik Search Allocation ID seed `Expired` Concurrent User +3 PT Abadi Jaya (`Fixture.license-allocation-license.seed51`), tekan Enter
21. Verifikasi Status baris: `Expired` dengan severity danger
22. Verifikasi Last Updated baris memuat waktu transisi Auto-Expire
23. Klik tab `Current`
24. Ketik Search Allocation ID seed `Expired` (`Fixture.license-allocation-license.seed51`), tekan Enter
25. Verifikasi empty state `No results found` tampil pada tab Current (anchor hasil Search)
26. Verifikasi baris `Expired` Concurrent User +3 PT Abadi Jaya tidak tampil pada tab Current

### TC-AC-LA-27: Plan snapshot, Client dan Product relasi live

27. Ganti isi kotak search dengan Allocation ID seed `Active` Plan snapshot `Professional` (`Fixture.license-allocation-license.seedActiveProfessional`), tekan Enter
28. Verifikasi kolom Plan baris tersebut menampilkan nilai awal `Professional`
29. Ubah nama Client `PT Sejahtera` menjadi `PT Sejahtera Makmur` di Client Detail
30. Ubah Plan term Client `PT Sejahtera Makmur` lewat Push Update Plans & Features
31. Klik menu `License Allocation` di sidebar
32. Ketik Search Allocation ID seed `Active` Plan snapshot `Professional` (`Fixture.license-allocation-license.seedActiveProfessional`), tekan Enter
33. Verifikasi kolom Plan tetap menampilkan nilai snapshot `Professional` (tidak ikut berubah)
34. Verifikasi kolom Client menampilkan `PT Sejahtera Makmur` (relasi live)
35. Pulihkan nama Client menjadi `PT Sejahtera` dan Plan term ke nilai awal lewat fixture backend

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah Setup Column (tanpa `Verifikasi`), langkah `Catat saldo`, pindah tab, `(←)` pada kotak Search, dan langkah pemulihan nama Client dan Plan term di akhir.
- Kolom Plan dan Cost ditampilkan sekali di awal spec lewat Setup Column dan dipakai TC-AC-LA-23 sampai TC-AC-LA-27 (langkah 1 TC-AC-LA-24, TC-AC-LA-25, dan TC-AC-LA-27 yang berbunyi `Tampilkan kolom ... lewat Setup Column` dipenuhi oleh langkah awal itu).
- Search tidak dibawa antar tab (ACLA-LOGIC-12d): setelah pindah tab Current di langkah 23, langkah 24 mengetik Search baru; langkah 25 (empty state `No results found`) menjadi anchor hasil Search sebelum absence langkah 26.
- Klik menu `License Allocation` di sidebar pada TC-AC-LA-27 mereset Search dan membuka tab Current (bagian 4).
- Temuan untuk QA:
  - TC-AC-LA-24 Expected c (`Saldo kantong Distributor tidak berkurang`) tidak memberi cara membaca saldo; spec memakai kemampuan baca saldo yang disediakan tim FE/BE (S-11, S-13).
  - TC-AC-LA-26 Expected c (`Last Updated memuat waktu transisi Auto-Expire`) tidak menyebut nilai yang dibandingkan; spec mengasersi isi kolom Last Updated tanpa nilai pembanding.
  - TC-AC-LA-27 tidak menyebut Allocation ID baris Active dengan Plan snapshot `Professional`, tidak menyebut Plan tujuan Push Update Plans & Features, dan tidak menyebut cara mengubah nama Client dan Plan term selain lewat Client Detail; baris dibaca dari fixture seed dan perubahan dilakukan lewat kemampuan fixture FE/BE.
  - TC-AC-LA-24, TC-AC-LA-25, dan TC-AC-LA-26 tidak menyebut Allocation ID baris yang dicari (kecuali Subscription ID di TC-AC-LA-25); baris dibaca dari fixture seed.
