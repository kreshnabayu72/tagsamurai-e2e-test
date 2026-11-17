---
id: TC-FA-PREF-E2E-002-screening-sectioncard-disposal-chart-of-accounts-journal-export-urutan-dan-nilai-awal
title: "Screening SectionCard Disposal, Chart of Accounts, Journal Export, Urutan SectionCard, dan Nilai Awal Seluruh Setting"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-6
  - TC-FA-PREF-7
  - TC-FA-PREF-8
  - TC-FA-PREF-21
  - TC-FA-PREF-22
sourceRules: ["§4.2a#p1", "SET-05", "§4.1.2#p1", "§4.1.1#p4", "SET-06", "SET-07", "DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06", "§9.5#r5", "SET-08", "SET-09", "SET-11", "§9.5#r1", "SET-01", "SET-12", "FAPREF-LOGIC-02h", "SET-02", "SET-03", "SET-04", "SET-13", "FAPREF-LOGIC-09c"]
smoke: []
dependsOn: []
trace:
  "§4.2a#p1": [2, 11, 17, 20]
  "SET-05": [3, 4, 28]
  "§4.1.2#p1": [3, 5, 7, 12, 14, 18]
  "§4.1.1#p4": [4, 6, 13, 15, 28]
  "SET-06": [5, 6, 28]
  "SET-07": [7, 9, 29]
  "DOC-01": [8, 9, 22, 29]
  "DOC-02": [8, 9, 22, 29]
  "DOC-03": [8, 9, 22, 29]
  "DOC-04": [8, 9, 22, 29]
  "DOC-05": [8, 9, 22, 29]
  "DOC-06": [8, 9, 22, 29]
  "§9.5#r5": [8, 22]
  "SET-08": [12, 13, 28]
  "SET-09": [14, 15, 28]
  "SET-11": [18, 19, 30]
  "§9.5#r1": 20
  "SET-01": 23
  "SET-12": 24
  "FAPREF-LOGIC-02h": 24
  "SET-02": 25
  "SET-03": 26
  "SET-04": 27
  "SET-13": 28
  "FAPREF-LOGIC-09c": 30
coverage:
  web: automated
---

# Screening SectionCard Disposal, Chart of Accounts, Journal Export, Urutan SectionCard, dan Nilai Awal Seluruh Setting

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi: Fiscal Year Start January; First Accounting Period March 2026; Default Capitalization Threshold 5.000.000; In-service Date Source Activation date; Depreciation in Disposal Month Up to previous month; Default Gain, Loss, Disposal Proceeds Account, Capitalization Offset, dan Found Asset Credit Account kosong; Disposal Documents keenam jenis Optional; Journal Grouping Group. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-6: Screening SectionCard Disposal

1. Gulir ke SectionCard Disposal
2. Verifikasi judul SectionCard "Disposal"
3. Verifikasi label Default Gain on Disposal dengan ikon ⓘ tampil tanpa tanda wajib
4. Verifikasi Select Default Gain on Disposal kosong dengan placeholder "Select account"
5. Verifikasi label Default Loss on Disposal dengan ikon ⓘ tampil tanpa tanda wajib
6. Verifikasi Select Default Loss on Disposal kosong dengan placeholder "Select account"
7. Verifikasi label Disposal Documents dengan tanda wajib `*` dan ikon ⓘ tampil
8. Verifikasi enam Select Disposal Documents berurutan: `Sell | Scrap | Lost | Donate | Trade-in | Write-off`
9. Verifikasi keenam Select Disposal Documents bernilai "Optional"

### TC-FA-PREF-7: Screening SectionCard Chart of Accounts

10. Gulir ke SectionCard Chart of Accounts
11. Verifikasi judul SectionCard "Chart of Accounts"
12. Verifikasi label Default Capitalization Offset dengan ikon ⓘ tampil tanpa tanda wajib
13. Verifikasi Select Default Capitalization Offset kosong dengan placeholder "Select account"
14. Verifikasi label Found Asset Credit Account dengan ikon ⓘ tampil tanpa tanda wajib
15. Verifikasi Select Found Asset Credit Account kosong dengan placeholder "Select account"

### TC-FA-PREF-8: Screening SectionCard Journal Export

16. Gulir ke SectionCard Journal Export
17. Verifikasi judul SectionCard "Journal Export"
18. Verifikasi label Journal Grouping dengan ikon ⓘ tampil tanpa tanda wajib
19. Verifikasi MultiSelect Journal Grouping bernilai "Group"

### TC-FA-PREF-21: Urutan SectionCard dan urutan jenis Disposal Documents

20. Verifikasi urutan SectionCard dari atas ke bawah: `General → Capitalization → Depreciation → Disposal → Chart of Accounts → Journal Export`
21. Gulir ke SectionCard Disposal
22. Verifikasi urutan jenis Disposal Documents: `Sell → Scrap → Lost → Donate → Trade-in → Write-off`

### TC-FA-PREF-22: Nilai awal seluruh setting

23. Verifikasi Fiscal Year Start bernilai "January"
24. Verifikasi First Accounting Period bernilai bulan dan tahun aktivasi modul akuntansi company: "March" dan "2026"
25. Verifikasi Default Capitalization Threshold bernilai "Rp 5.000.000,00"
26. Verifikasi In-service Date Source bernilai "Activation date"
27. Verifikasi Depreciation in Disposal Month bernilai "Up to previous month"
28. Verifikasi Default Gain on Disposal, Default Loss on Disposal, Default Disposal Proceeds Account, Default Capitalization Offset, dan Found Asset Credit Account kosong dengan placeholder "Select account"
29. Verifikasi Disposal Documents Sell, Scrap, Lost, Donate, Trade-in, dan Write-off bernilai "Optional"
30. Verifikasi Journal Grouping bernilai "Group"

## Notes

- Langkah penghubung (S-03): langkah 1, 10, 16, dan 21 (gulir ke SectionCard yang diperiksa). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang di spec ini.
- Urutan TC dalam spec: TC-FA-PREF-6, 7, 8, 21, 22 (screening per SectionCard lebih dulu, lalu urutan dan nilai awal seluruh setting). Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- Temuan untuk QA:
  - TC-FA-PREF-22 Expected b menulis First Accounting Period sebagai "bulan dan tahun aktivasi modul akuntansi company" tanpa menyebut sumber tanggal aktivasi; spec mengasersi "March" dan "2026" mengikuti nilai tersimpan PA-2.
  - TC-FA-PREF-22 mengulang sebagian nilai yang sudah diasersi TC-FA-PREF-6, 7, dan 8; spec mengikuti TC apa adanya.
