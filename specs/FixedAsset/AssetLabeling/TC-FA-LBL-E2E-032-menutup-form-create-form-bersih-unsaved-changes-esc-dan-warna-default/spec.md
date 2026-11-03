---
id: TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default
title: "Menutup Form Create: Form Bersih, Unsaved Changes, Esc, dan Warna Default (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-92
  - TC-FA-LBL-93
  - TC-FA-LBL-94
  - TC-FA-LBL-95
coverage:
  web: automated
---

# Menutup Form Create: Form Bersih, Unsaved Changes, Esc, dan Warna Default (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Baseline jumlah total label katalog Company Alpha (N0) dicatat di hook `before` lewat fixture BE; tidak ada label yang dibuat spec ini.
- Palet Preset (Pre-setup #33): swatch baris 1 kolom 2 bernilai `#F97316`.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog (jumlah total label).
- Spec ini tidak membuat data; tidak ada cleanup data.

## Test Steps

### TC-FA-LBL-92: Menutup form Create yang bersih lewat ✕ dan Esc tidak memunculkan dialog Unsaved Changes

1. Klik `[+ Label]`
2. Klik icon `[✕]`
3. Verifikasi modal langsung tertutup tanpa dialog `You have unsaved changes. Are you sure you want to leave?`
4. Klik `[+ Label]`
5. Tekan Esc
6. Verifikasi modal langsung tertutup tanpa dialog `You have unsaved changes. Are you sure you want to leave?`

### TC-FA-LBL-93: Menutup form Create yang terisi lewat ✕ memunculkan dialog Unsaved Changes

7. Klik `[+ Label]`
8. Ketik `Unsaved 93` di Label Name
9. Klik icon `[✕]`
10. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]` tampil
11. Klik `[Cancel]` pada dialog
12. Verifikasi dialog tertutup
13. Verifikasi modal tetap terbuka
14. Verifikasi Label Name tetap `Unsaved 93`
15. Klik icon `[✕]` lagi
16. Klik `[Leave]`
17. Verifikasi dialog dan modal tertutup
18. Verifikasi jumlah total label katalog (lewat fixture BE) sama dengan N0, tidak ada label yang dibuat

### TC-FA-LBL-94: Menekan Esc pada form Create yang terisi memunculkan dialog Unsaved Changes

19. Klik `[+ Label]`
20. Ketik `Esc Unsaved 94` di Label Name
21. Tekan Esc
22. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
23. Tekan Esc lagi saat dialog tampil
24. Verifikasi dialog tertutup (Esc setara `[Cancel]`)
25. Verifikasi modal tetap terbuka
26. Verifikasi input Label Name dipertahankan

### TC-FA-LBL-95: Mengubah hanya warna default membuat form dirty

27. Kosongkan Label Name
28. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
29. Klik swatch baris 1 kolom 2
30. Klik icon `[✕]`
31. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil karena Color berbeda dari snapshot saat form dibuka
32. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Modal yang dibuka pada TC-FA-LBL-94 dipakai TC-FA-LBL-95 sesudah Label Name dikosongkan (langkah 27), sehingga hanya Color yang berbeda dari snapshot (prinsip 6, S-09).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 27 (mengosongkan Label Name supaya form kembali bersih) dan langkah 32 (menutup modal lewat `[Leave]`).
- Bagian lain skenario menutup form (form dikembalikan identik, backdrop, reload, dan pindah route) ada di spec 033 (TC-FA-LBL-96 sampai 99).
- Temuan untuk QA: TC-FA-LBL-95 langkah 4 mengklik `[✕]` saat overlay Color Picker masih terbuka; TC tidak menyebut apakah klik pertama menutup overlay atau menutup modal. Spec mengikuti langkah TC.
