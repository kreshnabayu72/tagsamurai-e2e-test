---
id: TC-FA-CF-E2E-166-placeholder-default-dari-field-name-huruf-kecil
title: "Placeholder Default Memakai Field Name Huruf Kecil"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-204
coverage:
  web: automated
---

# Placeholder Default Memakai Field Name Huruf Kecil

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit):
  - D-1: `Capacity {runId}-166`, Data Type Numeric, Placeholder kosong.
  - D-2: `Description {runId}-166`, Data Type Text Area, Placeholder kosong.
  - D-3: `Brand {runId}-166`, Data Type Dropdown dengan opsi `A`, Placeholder kosong.
  - D-4: `Accessories {runId}-166`, Data Type Multi-Dropdown dengan opsi `B`, Placeholder kosong.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-166`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-204: Placeholder default memakai Field Name dalam huruf kecil pada contoh nama field

1. Klik `[+ Custom Field]`
2. Isi Field Name `Capacity {runId}-166`, Data Type `Numeric`, Placeholder dikosongkan
3. Klik `[Submit]`
4. Klik `[+ Custom Field]`
5. Isi Field Name `Description {runId}-166`, Data Type `Text Area`, Placeholder dikosongkan
6. Klik `[Submit]`
7. Klik `[+ Custom Field]`
8. Isi Field Name `Brand {runId}-166`, Data Type `Dropdown`, Placeholder dikosongkan
9. Ketik `A` pada input Values lalu tekan Enter
10. Klik `[Submit]`
11. Klik `[+ Custom Field]`
12. Isi Field Name `Accessories {runId}-166`, Data Type `Multi-Dropdown`, Placeholder dikosongkan
13. Ketik `B` pada input Values lalu tekan Enter
14. Klik `[Submit]`
15. Ketik Search `{runId}-166`, tekan Enter
16. Verifikasi kolom Placeholder baris `Capacity {runId}-166` menampilkan `Enter capacity {runId}-166`
17. Verifikasi kolom Placeholder baris `Description {runId}-166` menampilkan `Enter description {runId}-166`
18. Verifikasi kolom Placeholder baris `Brand {runId}-166` menampilkan `Select brand {runId}-166`
19. Verifikasi kolom Placeholder baris `Accessories {runId}-166` menampilkan `Select accessories {runId}-166`
20. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Field Dinamis bernama bersuffix `{runId}-166` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Nilai efektif Placeholder default mengikuti Field Name bersuffix: `Enter ` atau `Select ` diikuti nama field huruf kecil termasuk suffix.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-166` pada langkah 15 menampilkan keempat baris spec ini sekaligus (R-16) dan `Klik (←)` untuk mereset Search.
- TC-FA-CF-204 ada di spec ini; spec 022 memuat TC placeholder default lain (pembagian TC lintas spec).
- Temuan untuk QA: TC-FA-CF-204 langkah 2 menulis 'Buat empat field' tanpa menyebut toast sukses dan tanpa Expected penyelesaian; spec tidak mengasersi toast (S-02).
