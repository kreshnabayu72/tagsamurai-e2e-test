---
id: TC-AC-PF-E2E-020-aksesibilitas-aria-required-form-create-default-plan-dan-tab-global-settings
title: "Aksesibilitas: Field Wajib Form Create Default Plan dan Tab Global Settings Memiliki aria-required"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-788
  - TC-AC-PF-790
coverage:
  web: automated
---

# Aksesibilitas: Field Wajib Form Create Default Plan dan Tab Global Settings Memiliki aria-required

## Prerequisites

- Mode: FE+BE (hanya membuka form dan membaca atribut; TC bertanda UI Only, tanpa intercept dan tanpa perubahan data).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21) dan Global FAMS Settings dengan nilai awal Max custom fields per asset name `5` dan Max depreciation methods (Multi Depreciation tier) `2`. Spec hanya membuka form dan membaca atribut tanpa menyimpan, sehingga data tidak berubah. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pembacaan atribut ARIA elemen form (accessibility tree atau atribut DOM), fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-788: Accessibility form Create Default Plan: field wajib memiliki aria-required

1. Klik `+ Default Plan`
2. Pilih Product `SAMS`
3. Verifikasi atribut aria-required field Product bernilai "true"
4. Verifikasi atribut aria-required field Pricing Type bernilai "true"
5. Verifikasi atribut aria-required field Plan Name bernilai "true"
6. Klik segmen Breadcrumb `Plans & Features`
7. Verifikasi dialog `Unsaved Changes` tampil
8. Klik `[Leave]`

### TC-AC-PF-790: Accessibility tab Global Settings: field wajib memiliki aria-required

9. Klik tab Global Settings
10. Verifikasi atribut aria-required input Max custom fields per asset name bernilai "true"
11. Verifikasi atribut aria-required input Max depreciation methods (Multi Depreciation tier) bernilai "true"

## Notes

- Langkah penghubung (S-03): langkah 6 sampai 8 menutup form dirty setelah Product dipilih (S-08, S-09); klik tab Global Settings pada langkah 9 mengarahkan layar ke tab yang disyaratkan TC.
