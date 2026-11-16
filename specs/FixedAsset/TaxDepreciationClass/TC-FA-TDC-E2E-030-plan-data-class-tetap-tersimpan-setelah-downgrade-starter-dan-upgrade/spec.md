---
id: TC-FA-TDC-E2E-030-plan-data-class-tetap-tersimpan-setelah-downgrade-starter-dan-upgrade
title: "Plan: Data Class Tetap Tersimpan Setelah Downgrade ke Starter dan Upgrade, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-99
  - TC-FA-TDC-766
  - TC-FA-TDC-767
  - TC-FA-TDC-768
  - TC-FA-TDC-769
sourceRules: ["§9.10#b1", "§9.10#b2", "§4.1.1#r3", "ST-30", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3", "ST-27"]
smoke: []
dependsOn: []
trace:
  "§9.10#b1": [4, 16]
  "§9.10#b2": [5, 10]
  "§4.1.1#r3": 6
  "ST-30": 12
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3": 19
  "ST-27": 20
coverage:
  web: automated
---

# Plan: Data Class Tetap Tersimpan Setelah Downgrade ke Starter dan Upgrade, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): company pada plan Growth dengan 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data, Class Name NB-2 diubah menjadi `Bukan bangunan – Kelompok 2 Revisi`, NB-4 Active dengan Used By 0, NB-OLD Inactive, dan satu versi Scheduled pada BLD-NP. Tabel memuat 9 baris pada satu halaman.
- Tabel "Plan uji" (parameter langkah 14 sampai 20): Growth untuk TC-FA-TDC-767, Professional untuk TC-FA-TDC-768, Enterprise untuk TC-FA-TDC-769.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengubah plan client (Starter, Growth, Professional, Enterprise) lewat fixture BE; mengaktifkan kembali NB-4 lewat fixture BE.
- State global: plan company dan status Active NB-4. Hook `after` memulihkan plan ke Growth dan NB-4 ke Active.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-99: Data class tetap tersimpan setelah downgrade lalu upgrade

1. Turunkan plan client ke Starter lalu naikkan kembali ke Growth lewat fixture BE hingga tersimpan
2. Klik menu sidebar `Accounting`
3. Klik tab `Tax Depreciation Class`
4. Verifikasi tab terbuka
5. Verifikasi tabel menampilkan 9 class seperti sebelum downgrade tanpa perubahan
6. Verifikasi Class Name NB-2 `Bukan bangunan – Kelompok 2 Revisi` tampil

### TC-FA-TDC-766: Isi tabel sama persis setelah downgrade dan upgrade

7. Catat isi tabel Tax Depreciation Class (Class Code, Active, Used By, Effective From)
8. Turunkan plan client ke Starter lalu naikkan kembali ke Growth lewat fixture BE hingga tersimpan
9. Buka tab Tax Depreciation Class
10. Verifikasi isi tabel (jumlah baris, Class Code, status Active, Used By, dan Effective From) sama persis dengan catatan sebelum downgrade
11. Klik Class Code BLD-NP
12. Verifikasi Alert versi Scheduled pada Drawer Edit BLD-NP masih tampil
13. Tutup Drawer dengan `[×]`

### TC-FA-TDC-767, TC-FA-TDC-768, TC-FA-TDC-769: Tab tersedia penuh per plan

Untuk setiap plan pada tabel "Plan uji" di Prerequisites (langkah 14 sampai 20):

14. Atur plan client ke plan tersebut dan aktifkan NB-4 lewat fixture BE hingga tersimpan
15. Buka tab Tax Depreciation Class
16. Verifikasi tab Tax Depreciation Class terbuka dengan tabel berisi class
17. Klik toggle `Active` baris NB-4
18. Klik `[Deactivate]` pada dialog
19. Verifikasi toast sukses "Success, tax depreciation class has been deactivated." tampil
20. Verifikasi toggle NB-4 menjadi Off

## Notes

- Langkah penghubung (S-03): langkah 1 dan 8 (downgrade dan upgrade plan) membentuk precondition TC-FA-TDC-99 dan TC-FA-TDC-766 lewat fixture BE; langkah 7 mencatat isi tabel; langkah 13 menutup Drawer yang tidak dirty; langkah 14 mengatur plan dan memulihkan NB-4 ke Active sebelum tiap iterasi.
- Langkah 14 sampai 20 diulang tiga kali; parameter tiap iterasi ada di tabel "Plan uji" (8b.7). Ekspansi: 34 langkah.
- Temuan untuk QA:
  - TC-FA-TDC-766 menyebut perubahan plan "lewat Admin Console"; spec memakai fixture BE (kemampuan disediakan tim FE/BE) tanpa mengarang endpoint.
  - TC-FA-TDC-99 menyebut nilai kolom "persis Example Data" tanpa memuat nilai per kolom; asersi 9 class memakai Example Data PRD.
  - TC tidak menyebut akun, email, dan company Total Control.
  - TC-FA-TDC-767 sampai 769 mengubah status NB-4 (data seed literal); spec memakai dataset company uji khusus automation yang dipulihkan fixture, karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
