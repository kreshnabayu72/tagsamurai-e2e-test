---
id: TC-FA-PREF-E2E-005-opsi-select-dan-multiselect-fiscal-year-start-first-accounting-period-in-service-depreciation-month-journal-grouping
title: "Opsi Select dan MultiSelect: Fiscal Year Start, First Accounting Period, In-service Date Source, Depreciation in Disposal Month, Journal Grouping"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-23
  - TC-FA-PREF-24
  - TC-FA-PREF-25
  - TC-FA-PREF-26
  - TC-FA-PREF-164
  - TC-FA-PREF-165
  - TC-FA-PREF-596
sourceRules: ["SET-01", "§9.5#r3", "§9.5#r4", "§4.1.1#p4", "SET-12", "FAPREF-LOGIC-02i", "FI-06", "§9.5#r7", "FAPREF-LOGIC-09c", "SET-11", "SET-03", "FAPREF-LOGIC-04a", "SET-04", "FAPREF-LOGIC-05a"]
smoke: []
dependsOn: []
trace:
  "SET-01": 2
  "§9.5#r3": 2
  "§9.5#r4": [5, 6, 8, 13, 14, 15, 20]
  "§4.1.1#p4": [5, 13, 20]
  "SET-12": [6, 14]
  "FAPREF-LOGIC-02i": [7, 16, 21]
  "FI-06": 21
  "§9.5#r7": 25
  "FAPREF-LOGIC-09c": [25, 26]
  "SET-11": 26
  "SET-03": 29
  "FAPREF-LOGIC-04a": 29
  "SET-04": 32
  "FAPREF-LOGIC-05a": 32
coverage:
  web: automated
---

# Opsi Select dan MultiSelect: Fiscal Year Start, First Accounting Period, In-service Date Source, Depreciation in Disposal Month, Journal Grouping

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi: Fiscal Year Start January; First Accounting Period March 2026; Journal Grouping Group. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- TC-FA-PREF-596 memakai seri fixture PC-1; nilai awal Preferences PC-1 setara PA-2 (belum ada posting penyusutan, semua periode Open). Seed ulang ke nilai awal PC-1 dilakukan lewat langkah penghubung (langkah 10), disediakan tim FE/BE.
- State global: jam sistem dikendalikan (clock): jam server dan jam browser dibekukan pada 28 Oktober 2026 pukul 10:00 menurut Time Zone entitas Asia/Jakarta (bulan dan tahun berjalan Oktober 2026), dipakai TC-FA-PREF-24 dan 596. Kemampuan kendali jam disediakan tim FE/BE (lihat `suite.md`); jam dipulihkan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-23: Opsi Select Fiscal Year Start

1. Klik Select Fiscal Year Start
2. Verifikasi daftar opsi tepat 12 bulan berurutan kalender: `January | February | March | April | May | June | July | August | September | October | November | December`
3. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-24: Opsi Select tahun First Accounting Period

4. Klik Select tahun pada First Accounting Period
5. Verifikasi opsi pertama "2000"
6. Verifikasi opsi terakhir "2026" (tahun berjalan)
7. Verifikasi tidak ada opsi "2027"
8. Verifikasi opsi berurutan naik `2000 → 2001 → ... → 2026`
9. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-596: Batas opsi tahun First Accounting Period

10. Seed ulang Preferences company ke nilai awal PC-1 hingga tersimpan
11. Muat ulang halaman dengan F5
12. Klik Select tahun pada First Accounting Period
13. Verifikasi opsi pertama "2000"
14. Verifikasi opsi terakhir "2026"
15. Verifikasi opsi berurutan naik
16. Verifikasi tidak ada opsi "1999" maupun "2027"
17. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-25: Opsi Select bulan First Accounting Period pada tahun lampau

18. Pilih tahun "2025" pada Select tahun First Accounting Period
19. Klik Select bulan pada First Accounting Period
20. Verifikasi daftar opsi bulan berurutan kalender `January | February | ... | December`
21. Verifikasi seluruh opsi bulan dapat dipilih
22. Tekan Esc untuk menutup daftar opsi
23. Pilih tahun "2026" pada Select tahun First Accounting Period

### TC-FA-PREF-26: Opsi MultiSelect Journal Grouping

24. Klik MultiSelect Journal Grouping
25. Verifikasi daftar opsi tepat tiga berurutan: `Group | Category | Asset Class`
26. Verifikasi opsi "Group" berstatus terpilih
27. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-164: Opsi Select In-service Date Source

28. Klik Select In-service Date Source
29. Verifikasi daftar opsi tepat dua berurutan: `Activation date | Manual by Accounting`
30. Tekan Esc untuk menutup daftar opsi

### TC-FA-PREF-165: Opsi Select Depreciation in Disposal Month

31. Klik Select Depreciation in Disposal Month
32. Verifikasi daftar opsi tepat tiga berurutan: `Up to previous month | Including disposal month | Daily prorata`
33. Tekan Esc untuk menutup daftar opsi

## Notes

- Langkah penghubung (S-03, S-09): langkah 3, 9, 17, 22, 27, 30, dan 33 (menutup daftar opsi agar daftar berikutnya dapat dibuka), langkah 10 dan 11 (seed ulang seri PC-1 dan muat ulang), serta langkah 23 (mengembalikan tahun First Accounting Period ke nilai tersimpan "2026" supaya form tidak dirty di akhir TC-FA-PREF-25). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang.
- Urutan TC dalam spec: TC-FA-PREF-23, 24, 596 (opsi tahun berdampingan), 25, 26, 164, 165. Spec tidak menyimpan perubahan Preferences.
- Temuan untuk QA:
  - TC-FA-PREF-596 memakai seri PC-1 sedangkan TC lain di spec ini memakai seri PA-2; spec mengasumsikan nilai awal keduanya setara (Catatan TC: seri fixture seed terisolasi).
  - TC-FA-PREF-24 menyebut tanggal sistem uji 28 Oktober 2026 pada Time Zone entitas, sedangkan TC-FA-PREF-596 hanya menyebut bulan berjalan Oktober 2026; spec membekukan jam pada 28 Oktober 2026 pukul 10:00 untuk keduanya.
  - TC-FA-PREF-24 dan 596 sama-sama menguji batas 2000 dan tahun berjalan; spec mengikuti kedua TC apa adanya.
