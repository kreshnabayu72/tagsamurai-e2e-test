---
id: TC-FA-PREF-E2E-160-select-setting-wajib-tanpa-kontrol-pengosongan
title: "Select Setting Wajib Tidak Menyediakan Kontrol atau Opsi Kosong untuk Mengosongkan Nilainya"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-618
coverage:
  web: automated
---

# Select Setting Wajib Tidak Menyediakan Kontrol atau Opsi Kosong untuk Mengosongkan Nilainya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` dengan Preferences nilai awal PC-1 (Fiscal Year Start January, First Accounting Period Mar 2026, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month). Spec hanya membaca.
- State yang diubah spec: tidak ada.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-618: Select setting wajib tidak menyediakan kontrol atau opsi kosong

1. Klik Select Fiscal Year Start
2. Verifikasi daftar opsi Select Fiscal Year Start menampilkan sedikitnya satu opsi bulan
3. Verifikasi daftar opsi Select Fiscal Year Start tidak memuat opsi kosong dan tidak menyediakan kontrol untuk mengosongkan nilai
4. Verifikasi nilai Select Fiscal Year Start tetap "January"
5. Tutup daftar opsi Select Fiscal Year Start
6. Klik Select In-service Date Source
7. Verifikasi daftar opsi Select In-service Date Source hanya memuat `Activation date | Manual by Accounting`
8. Verifikasi Select In-service Date Source tanpa opsi kosong dan tanpa kontrol untuk mengosongkan nilai
9. Verifikasi nilai Select In-service Date Source tetap "Activation date"
10. Tutup daftar opsi Select In-service Date Source
11. Klik Select Depreciation in Disposal Month
12. Verifikasi daftar opsi Select Depreciation in Disposal Month hanya memuat `Up to previous month | Including disposal month | Daily prorata`
13. Verifikasi Select Depreciation in Disposal Month tanpa opsi kosong dan tanpa kontrol untuk mengosongkan nilai
14. Verifikasi nilai Select Depreciation in Disposal Month tetap "Up to previous month"
15. Tutup daftar opsi Select Depreciation in Disposal Month
16. Klik Select bulan First Accounting Period
17. Verifikasi daftar opsi Select bulan menampilkan sedikitnya satu opsi bulan
18. Verifikasi daftar opsi Select bulan tidak memuat opsi kosong dan tidak menyediakan kontrol bagi user untuk mengosongkan nilai
19. Tutup daftar opsi Select bulan
20. Klik Select tahun First Accounting Period
21. Verifikasi daftar opsi Select tahun menampilkan sedikitnya satu opsi tahun
22. Verifikasi daftar opsi Select tahun tidak memuat opsi kosong dan tidak menyediakan kontrol bagi user untuk mengosongkan nilai
23. Tutup daftar opsi Select tahun
24. Verifikasi nilai Select bulan dan Select tahun First Accounting Period tetap "March" dan "2026"
25. Verifikasi tidak ada caption pada keempat field
26. Verifikasi tidak ada dialog dan tidak ada toast

## Notes

- Langkah penghubung (S-03): langkah 5, 10, 15, 19, 23 (menutup daftar opsi). Langkah 2, 17, dan 21 adalah anchor positif asersi absence opsi kosong (8b.2) dan tidak ada di Expected TC. Setiap daftar opsi diasersi saat terbuka (8b.5).
- Temuan untuk QA:
  - Expected d menyebut bulan hanya dikosongkan otomatis oleh FI-06 saat Select tahun diganti ke tahun berjalan (TC-FA-PREF-128); itu rujukan ke TC lain dan tidak diasersi di spec ini.
  - Post Condition ("Preferences company belum berubah") tidak punya langkah observasi sehingga tidak diasersi (S-01).
