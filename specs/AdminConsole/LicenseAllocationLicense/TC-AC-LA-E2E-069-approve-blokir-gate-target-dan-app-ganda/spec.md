---
id: TC-AC-LA-E2E-069-approve-blokir-gate-target-dan-app-ganda
title: "Approve Ditolak karena Kondisi Data: Target Tidak Eligible, Gate Station Storage, dan App Ganda"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-250
  - TC-AC-LA-251
  - TC-AC-LA-252
coverage:
  web: automated
---

# Approve Ditolak karena Kondisi Data: Target Tidak Eligible, Gate Station Storage, dan App Ganda

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (Pre-setup #10, Total Control Distributor PT Maju Bersama); halaman License Allocation dibuka hook `beforeEach` suite (tab Current), dan spec ini berpindah ke Approvals sebagai langkah pertama.
- Akun: `totalControlDistLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: CV Mitra Sejati (Pre-setup #22), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval ON (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`, status `Waiting for Approval`; tidak memakai baris Pre-setup #41, #44, dan #45 bersama):
  - `{idTerm}`: Concurrent User +5, requester Dewi Anggraini (Pre-setup #4), Cost $150.00 di-Reserve, pada term Subscription Paid Active milik spec `{termTarget}` yang disediakan fixture backend;
  - `{idStation}` dan `{idStorage}`: Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide`, requester Dewi Anggraini, pada Client milik spec `{clientGate}` yang punya Subscription Paid Active milik spec (disediakan fixture backend);
  - `{idApp1}` (requester Dewi Anggraini) dan `{idApp2}` (requester Doni Prasetyo, Pre-setup #5): dua alokasi Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati, Subscription yang belum punya Asset Control App Active atau Pending pada awal spec.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi, term, dan Client milik spec beserta pembersihannya di hook `after`; sesi aktor lain (API) untuk Cancel Subscription term `{termTarget}` dan seluruh Subscription Paid Active `{clientGate}` (langkah penghubung dengan format "... hingga ... tersimpan", R-20); kemampuan membaca Status dan Reserve record.
- State global: term `{termTarget}` dan Subscription `{clientGate}` dibatalkan pada langkah 1 dan 8; keduanya adalah data milik spec dan dibersihkan di hook `after`, sehingga tidak ada Pre-setup bersama yang berubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Approve ditolak V-07: term Target tidak lagi Active atau Pending

1. Cancel Subscription term `{termTarget}` lewat sesi aktor lain hingga status Canceled tersimpan
2. Buka Approvals > License Allocation
3. Klik `[Review]` pada alokasi `{idTerm}`
4. Pilih Approve
5. Klik Submit
6. Verifikasi Approve ditolak dengan pesan `This target no longer exists. Please select another.`
7. Verifikasi Status `{idTerm}` tetap `Waiting for Approval` dan Reserve utuh

### Approve Station dan Storage ditolak V-09 dan V-11

8. Cancel seluruh Subscription Paid Active Client `{clientGate}` lewat sesi aktor lain hingga status Canceled tersimpan
9. Buka Approvals > License Allocation
10. Klik `[Review]` pada alokasi Asset Control Station `{idStation}`
11. Pilih Approve
12. Klik Submit
13. Verifikasi pesan `Asset Control Station requires at least one active paid subscription.`
14. Buka Approvals > License Allocation
15. Klik `[Review]` pada alokasi Storage `{idStorage}`
16. Pilih Approve
17. Klik Submit
18. Verifikasi pesan `Storage requires at least one active paid subscription.`
19. Verifikasi Status `{idStation}` dan `{idStorage}` tetap `Waiting for Approval`

### Dua pengajuan Asset Control App serentak ditolak V-12

20. Buka Approvals > License Allocation
21. Klik `[Review]` pada pengajuan pertama `{idApp1}`
22. Pilih Approve
23. Klik Submit
24. Verifikasi Approve pertama berhasil: toast sukses "Success, transaction has been approved."
25. Klik `[Review]` pada pengajuan kedua `{idApp2}`
26. Pilih Approve
27. Klik Submit
28. Verifikasi Approve kedua ditolak dengan pesan `Asset Control App is already active for this subscription.`
29. Verifikasi pengajuan kedua `{idApp2}` tetap `Waiting for Approval`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 8 (pemicu kondisi data lewat sesi aktor lain), langkah 2, 9, 14, dan 20 (berpindah halaman).
- Kondisi data yang ditolak (Target tidak eligible, gate Paid Active gugur, App ganda) adalah objek uji spec ini sehingga pemicunya dijalankan sebagai langkah eksplisit sebelum aksi Approve (prinsip 12).
- Temuan untuk QA:
  - TC-AC-LA-250 dan TC-AC-LA-251 membatalkan term `SUBS-20260101-A1B2C` dan seluruh Subscription Paid Active Klinik Harapan Bunda (Pre-setup #19 dan #24) yang dipakai banyak TC lain, tanpa menyebut cara memulihkannya; spec memakai term dan Client milik spec yang disediakan fixture backend supaya Pre-setup bersama tidak rusak (S-06).
  - TC-AC-LA-250 dan TC-AC-LA-251 tidak menyebut akun pelaku Cancel Subscription di sesi lain; ditulis sebagai sesi aktor lain yang disediakan tim FE (S-13).
  - TC-AC-LA-252 memakai Pre-setup #44 untuk Subscription `SUBS-20260105-K2L3M`, sedangkan Pre-setup #53 menyatakan Subscription yang sama sudah punya Asset Control App Active; Approve pertama tidak mungkin berhasil bila #53 berlaku. Spec mensyaratkan Subscription tanpa App Active atau Pending pada awal spec.
  - TC-AC-LA-250 butir b, TC-AC-LA-251 butir c, dan TC-AC-LA-252 butir b ("Status tidak berubah", "Reserve utuh") tidak menyebut cara mengamati; spec memakai kemampuan baca state record dari tim FE/BE.
  - TC-AC-LA-251 langkah 2 ("Ulangi untuk alokasi Storage") tidak menyebut apakah halaman kembali ke Approvals sesudah pesan penolakan; spec membuka Approvals di langkah 14 sebagai langkah penghubung.
