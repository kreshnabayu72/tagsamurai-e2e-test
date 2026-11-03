---
id: TC-FA-PREF-E2E-001-screening-tab-preferences-initial-state-dan-sectioncard-general-capitalization-depreciation
title: "Screening Tab Preferences: Initial State dan SectionCard General, Capitalization, Depreciation dengan Nilai Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-1
  - TC-FA-PREF-3
  - TC-FA-PREF-4
  - TC-FA-PREF-5
coverage:
  web: automated
---

# Screening Tab Preferences: Initial State dan SectionCard General, Capitalization, Depreciation dengan Nilai Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi: Fiscal Year Start January; First Accounting Period March 2026; Default Capitalization Threshold 5.000.000; In-service Date Source Activation date; Depreciation in Disposal Month Up to previous month; Default Gain, Loss, Capitalization Offset, dan Found Asset Credit Account kosong; Disposal Documents keenam jenis Optional; Journal Grouping Group. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-1: Screening tab Preferences saat pertama dibuka

1. Verifikasi Breadcrumb "Settings > Accounting > Preferences" tampil
2. Verifikasi tidak ada Page Title (Breadcrumb menggantikan Page Title)
3. Verifikasi Tab `Preferences (aktif) | Chart of Accounts | Tax Depreciation Class | Asset Class` tampil berurutan
4. Verifikasi ikon View history tampil di header tab
5. Verifikasi Banner Setup Incomplete tidak tampil
6. Verifikasi daftar anchor sticky di sisi kiri: `General | Capitalization | Depreciation | Disposal | Chart of Accounts | Journal Export`
7. Verifikasi SectionCard berurutan: `General | Capitalization | Depreciation | Disposal | Chart of Accounts | Journal Export`
8. Verifikasi masing-masing SectionCard terpisah
9. Verifikasi tidak ada tabel, Drawer, atau sidebar data pada Body
10. Verifikasi `[Cancel]` (variant text) lalu `[Save changes]` (variant filled) tampil di Footer
11. Verifikasi `[Cancel]` dan `[Save changes]` Disabled

### TC-FA-PREF-3: Screening SectionCard General

12. Gulir ke SectionCard General
13. Verifikasi judul SectionCard "General"
14. Verifikasi label Fiscal Year Start* dengan ikon ⓘ tampil
15. Verifikasi Select Fiscal Year Start bernilai "January"
16. Verifikasi Select Fiscal Year Start Enabled tanpa ikon gembok
17. Verifikasi label First Accounting Period* dengan ikon ⓘ tampil
18. Verifikasi dua Select First Accounting Period: bulan "March" dan tahun "2026"
19. Verifikasi kedua Select First Accounting Period Enabled tanpa ikon gembok

### TC-FA-PREF-4: Screening SectionCard Capitalization

20. Gulir ke SectionCard Capitalization
21. Verifikasi judul SectionCard "Capitalization"
22. Verifikasi label Default Capitalization Threshold* dengan ikon ⓘ tampil
23. Verifikasi CurrencyInput Default Capitalization Threshold bernilai "Rp 5.000.000,00"
24. Verifikasi label In-service Date Source* dengan ikon ⓘ tampil
25. Verifikasi Select In-service Date Source bernilai "Activation date"

### TC-FA-PREF-5: Screening SectionCard Depreciation

26. Gulir ke SectionCard Depreciation
27. Verifikasi judul SectionCard "Depreciation"
28. Verifikasi label Depreciation in Disposal Month* dengan ikon ⓘ tampil
29. Verifikasi Select Depreciation in Disposal Month bernilai "Up to previous month"

## Notes

- Langkah penghubung (S-03): langkah 12, 20, dan 26 (gulir ke SectionCard yang diperiksa). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang di spec ini.
- Urutan TC dalam spec: TC-FA-PREF-1, 3, 4, 5 (screening keseluruhan tab lebih dulu, lalu per SectionCard). Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- Temuan untuk QA: tidak ada temuan pada TC sumber spec ini.
