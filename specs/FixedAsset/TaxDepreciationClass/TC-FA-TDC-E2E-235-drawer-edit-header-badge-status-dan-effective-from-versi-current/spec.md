---
id: TC-FA-TDC-E2E-235-drawer-edit-header-badge-status-dan-effective-from-versi-current
title: "Drawer Edit: Effective From Versi Current Read-Only dan Header Badge Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-32
  - TC-FA-TDC-179
coverage:
  web: automated
---

# Drawer Edit: Effective From Versi Current Read-Only dan Header Badge Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data: tabel berisi 9 class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data, disediakan lewat seed (nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE). Yang dipakai spec ini (hanya dibuka dan ditutup tanpa Save, tidak ada yang diubah):

| Class Code | Nilai yang dipakai langkah |
|---|---|
| `NB-4` | Non-building, versi Current Effective From Jan 2026, Active, Used By 0 |
| `NB-1` | Active, Class Name `Bukan bangunan – Kelompok 1` |
| `NB-OLD` | Inactive, Class Name `Kelompok khusus lama` |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-179: Effective From versi Current dan tautan View versions

1. Ketik Search `NB-4`, tekan Enter
2. Klik link Class Code `NB-4`
3. Verifikasi Effective From berupa teks read-only `Jan 2026`
4. Verifikasi tautan `View versions` tampil di bawah nilai Effective From
5. Klik field Effective From dan coba ketik `2030`
6. Verifikasi field Effective From tidak menerima input: nilai tetap `Jan 2026`
7. Klik ikon ✕

### TC-FA-TDC-32: Header Drawer mode Edit

8. Ganti isi kotak search dengan `NB-1`, tekan Enter
9. Klik link Class Code `NB-1`
10. Verifikasi Header Drawer memuat judul `Edit Tax Depreciation Class`
11. Verifikasi Header Drawer memuat badge Status `Active` (severity success)
12. Verifikasi Header Drawer memuat ikon ✕
13. Verifikasi satu baris teks polos di bawah judul `Class Name: Bukan bangunan – Kelompok 1`
14. Verifikasi judul tidak berisi Class Code maupun Class Name
15. Klik ikon ✕
16. Ganti isi kotak search dengan `NB-OLD`, tekan Enter
17. Klik link Class Code `NB-OLD`
18. Verifikasi Header Drawer memuat judul `Edit Tax Depreciation Class`
19. Verifikasi Header Drawer memuat badge Status `Inactive` (severity danger)
20. Verifikasi baris teks polos `Class Name: Kelompok khusus lama`
21. Klik ikon ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 8, dan 16 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 7, 15, dan 21 menutup Drawer yang bersih (tanpa dialog Unsaved Changes). Langkah 5 (mencoba mengetik `2030`) ditambahkan sebagai aksi untuk Expected c TC-FA-TDC-179 "tidak menerima input"; TC tidak memberi langkah itu (lihat Temuan untuk QA).
- Urutan TC: TC-FA-TDC-179 lebih dulu, lalu TC-FA-TDC-32 (kedua blok berdiri sendiri; urutan mengikuti data yang dibuka).
- Pembagian TC lintas spec: TC-FA-TDC-177 dan TC-FA-TDC-178 (screening tiga zona dan row action) ada di spec 056.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - TC-FA-TDC-179 Expected c ("Field Effective From tidak dapat diubah (tidak menerima input)") tidak punya langkah mencoba mengetik; spec menambah langkah 5 (S-15).
  - TC-FA-TDC-32 dan TC-FA-TDC-179 membuka class Example Data Pre-setup (NB-1, NB-4, NB-OLD) tanpa mengubahnya; state Pre-setup tidak berubah (S-06).
