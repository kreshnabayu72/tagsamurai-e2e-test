---
id: TC-FA-PREF-E2E-007-tooltip-set-08-set-09-set-11-set-12-format-opsi-dan-placeholder-select
title: "Tooltip Ikon Info ⓘ SET-08, SET-09, SET-11, SET-12, Format Opsi Select Akun, dan Placeholder Select Saat Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-36
  - TC-FA-PREF-37
  - TC-FA-PREF-38
  - TC-FA-PREF-39
  - TC-FA-PREF-46
  - TC-FA-PREF-47
  - TC-FA-PREF-48
  - TC-FA-PREF-49
  - TC-FA-PREF-50
coverage:
  web: automated
---

# Tooltip Ikon Info ⓘ SET-08, SET-09, SET-11, SET-12, Format Opsi Select Akun, dan Placeholder Select Saat Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah) untuk TC-FA-PREF-36 sampai 47: Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi, keempat akun default (Default Gain on Disposal, Default Loss on Disposal, Default Capitalization Offset, Found Asset Credit Account) kosong. Chart of Accounts PA-3 (akun Active: 1-1001 Kas Utama, 1-2900 Biaya Dikapitalisasi, 4-1500 Pendapatan Lain-lain, 4-7002 Gain and Loss on Disposal, 4-9100 Laba Pelepasan Aset, 5-9100 Rugi Pelepasan Aset) dipakai TC-FA-PREF-47. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Data untuk TC-FA-PREF-48 sampai 50: Preferences varian PA-5 dengan Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month tersimpan kosong, serta Journal Grouping tersimpan kosong (seed varian sesuai Precondition TC-FA-PREF-48). Seed varian dan pemulihan ke PA-2 dilakukan lewat langkah penghubung (langkah 14 dan 23), disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-36: Tooltip Default Capitalization Offset (SET-08)

1. Hover ikon ⓘ di sebelah label "Default Capitalization Offset"
2. Verifikasi tooltip tampil dengan teks persis: "Credit account used when a cost is capitalized without a purchase document. You will be asked for it the first time it is needed."

### TC-FA-PREF-37: Tooltip Found Asset Credit Account (SET-09)

3. Hover ikon ⓘ di sebelah label "Found Asset Credit Account"
4. Verifikasi tooltip tampil dengan teks persis: "Credit account for unrecorded assets found during a physical count, usually other income or an equity adjustment. If empty, their journals are held at export."

### TC-FA-PREF-38: Tooltip Journal Grouping (SET-11)

5. Hover ikon ⓘ di sebelah label "Journal Grouping"
6. Verifikasi tooltip tampil dengan teks persis: "Summarize journal lines per account and the selected dimensions, instead of one line per asset."

### TC-FA-PREF-39: Tooltip First Accounting Period (SET-12)

7. Hover ikon ⓘ di sebelah label "First Accounting Period"
8. Verifikasi tooltip tampil dengan teks persis: "The month and year your accounting periods start from. It can be in the past but not in the future. Can be changed until depreciation is posted or a period is closed."

### TC-FA-PREF-46: Placeholder keempat Select akun

9. Verifikasi Select Default Gain on Disposal, Default Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account menampilkan placeholder "Select account"

### TC-FA-PREF-47: Format opsi Select akun

10. Klik Select Found Asset Credit Account
11. Verifikasi sedikitnya satu opsi tampil pada daftar opsi
12. Verifikasi setiap opsi berformat `[Account Code] – [Account Name]`, contoh "1-1001 – Kas Utama" dan "1-2900 – Biaya Dikapitalisasi"
13. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-48 sampai 50: Placeholder saat nilai tersimpan kosong

14. Seed ulang Preferences company ke varian PA-5 dengan Journal Grouping tersimpan kosong hingga tersimpan
15. Muat ulang halaman dengan F5
16. Verifikasi Select Fiscal Year Start menampilkan placeholder "Select fiscal year start"
17. Verifikasi Select In-service Date Source menampilkan placeholder "Select in-service date source"
18. Verifikasi Select Depreciation in Disposal Month menampilkan placeholder "Select depreciation in disposal month"
19. Verifikasi MultiSelect Journal Grouping menampilkan placeholder "Select journal grouping"
20. Verifikasi Select bulan First Accounting Period menampilkan placeholder "Select month"
21. Verifikasi Select tahun First Accounting Period menampilkan placeholder "Select year"
22. Verifikasi CurrencyInput Default Capitalization Threshold menampilkan placeholder "Enter capitalization threshold"
23. Seed ulang Preferences company ke nilai awal PA-2 hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 13 (menutup daftar opsi), langkah 14 dan 15 (seed varian PA-5 dan muat ulang agar form memuat nilai seed), serta langkah 23 (memulihkan Preferences ke PA-2). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang.
- Urutan TC dalam spec: TC-FA-PREF-36, 37, 38, 39, 46, 47 (seed PA-2), lalu TC-FA-PREF-48, 49, 50 (seed varian PA-5) di akhir. TC-FA-PREF-48, 49, dan 50 berbagi satu seed dan satu pemuatan halaman karena hanya mengamati (satu pembukaan untuk kasus tanpa submit).
- Temuan untuk QA:
  - TC-FA-PREF-48 menulis Precondition c "PA-5 ... setting lain bernilai awal" dan d "Seed varian PA-5: Journal Grouping tersimpan kosong (pada PA-5 bernilai Group)"; tabel PA-5 menulis Journal Grouping "Group". Spec mengikuti Precondition d (Journal Grouping kosong) karena Expected d menuntut placeholder "Select journal grouping".
  - TC-FA-PREF-47 menyebut contoh opsi "1-1001 – Kas Utama" pada Select Found Asset Credit Account tanpa menyatakan apakah daftar opsi difilter menurut function akun; spec mengasersi format opsi dan memuat kedua contoh sebagai contoh format, bukan jaminan keberadaan.
