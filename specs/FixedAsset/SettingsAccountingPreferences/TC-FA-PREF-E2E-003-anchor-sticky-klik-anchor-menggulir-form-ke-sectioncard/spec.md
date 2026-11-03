---
id: TC-FA-PREF-E2E-003-anchor-sticky-klik-anchor-menggulir-form-ke-sectioncard
title: "Daftar Anchor Sticky: Klik Anchor Menggulir Form ke SectionCard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-9
  - TC-FA-PREF-10
  - TC-FA-PREF-11
  - TC-FA-PREF-12
  - TC-FA-PREF-13
  - TC-FA-PREF-14
coverage:
  web: automated
---

# Daftar Anchor Sticky: Klik Anchor Menggulir Form ke SectionCard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-9: Anchor General

1. Gulir form ke posisi paling atas
2. Klik anchor "General" pada daftar anchor di sisi kiri
3. Verifikasi form menggulir ke SectionCard General
4. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

### TC-FA-PREF-10: Anchor Capitalization

5. Gulir form ke posisi paling atas
6. Klik anchor "Capitalization" pada daftar anchor di sisi kiri
7. Verifikasi form menggulir ke SectionCard Capitalization
8. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

### TC-FA-PREF-11: Anchor Depreciation

9. Gulir form ke posisi paling atas
10. Klik anchor "Depreciation" pada daftar anchor di sisi kiri
11. Verifikasi form menggulir ke SectionCard Depreciation
12. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

### TC-FA-PREF-12: Anchor Disposal

13. Gulir form ke posisi paling atas
14. Klik anchor "Disposal" pada daftar anchor di sisi kiri
15. Verifikasi form menggulir ke SectionCard Disposal
16. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

### TC-FA-PREF-13: Anchor Chart of Accounts

17. Gulir form ke posisi paling atas
18. Klik anchor "Chart of Accounts" pada daftar anchor di sisi kiri
19. Verifikasi form menggulir ke SectionCard Chart of Accounts
20. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

### TC-FA-PREF-14: Anchor Journal Export

21. Gulir form ke posisi paling atas
22. Klik anchor "Journal Export" pada daftar anchor di sisi kiri
23. Verifikasi form menggulir ke SectionCard Journal Export
24. Verifikasi daftar anchor tetap tampil sticky di sisi kiri

## Notes

- Langkah penghubung (S-03): langkah 1, 5, 9, 13, 17, dan 21 (mengembalikan form ke posisi paling atas sebelum tiap anchor diklik; sama dengan langkah TC "pastikan form berada di posisi paling atas"). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang di spec ini.
- Urutan TC dalam spec: TC-FA-PREF-9 sampai 14 sesuai urutan anchor. Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- Temuan untuk QA: TC sumber menyebut "form menggulir ke SectionCard X" tanpa kriteria terukur (posisi SectionCard di viewport); spec mengasersi SectionCard X berada di area terlihat viewport.
