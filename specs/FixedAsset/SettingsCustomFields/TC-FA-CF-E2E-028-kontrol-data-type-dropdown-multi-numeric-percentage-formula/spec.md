---
id: TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula
title: "Kontrol Data Type Dropdown, Multi-Dropdown, Numeric, Percentage, dan Formula"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-72
  - TC-FA-CF-73
  - TC-FA-CF-74
  - TC-FA-CF-75
  - TC-FA-CF-76
coverage:
  web: automated
---

# Kontrol Data Type Dropdown, Multi-Dropdown, Numeric, Percentage, dan Formula

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup: tidak ada data yang dibuat atau diubah; spec hanya membuka modal Create, memilih Data Type, dan mengamati kontrol.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Custom Field]`

#### TC-FA-CF-72: Memilih Data Type Dropdown menampilkan builder Values tanpa kontrol Value Type

2. Pilih Data Type `Dropdown`
3. Verifikasi section Values tampil dengan input chip `Enter value`
4. Verifikasi section Values menampilkan helper `Press enter to add new value or click the badge to edit`
5. Verifikasi kontrol Value Type disembunyikan
6. Verifikasi Placeholder dan toggle Required tetap tampil
7. Verifikasi kontrol Decimal Places dan Formula Builder tidak tampil

#### TC-FA-CF-73: Memilih Data Type Multi-Dropdown menampilkan builder Values tanpa kontrol Value Type

8. Pilih Data Type `Multi-Dropdown`
9. Verifikasi section Values tampil dengan helper `Press enter to add new value or click the badge to edit`
10. Verifikasi kontrol Value Type disembunyikan
11. Verifikasi Required dan Placeholder tetap tampil

#### TC-FA-CF-74: Memilih Data Type Numeric menampilkan radio Decimal Places default 0

12. Pilih Data Type `Numeric`
13. Verifikasi radio Decimal Places tampil: `0 (Integer)`, `1 (.0)`, `2 (.00)`
14. Verifikasi radio `0 (Integer)` terpilih
15. Verifikasi radio Decimal Places tampil tanpa placeholder dan helper
16. Verifikasi kontrol Values dan Formula Builder tidak tampil

#### TC-FA-CF-75: Memilih Data Type Percentage menampilkan radio Decimal Places default 0

17. Pilih Data Type `Percentage`
18. Verifikasi radio Decimal Places tampil: `0 (Integer)`, `1 (.0)`, `2 (.00)`
19. Verifikasi radio `0 (Integer)` terpilih

#### TC-FA-CF-76: Memilih Data Type Formula menampilkan Formula Builder dan menyembunyikan Placeholder, Value Type, dan Required

20. Pilih Data Type `Formula`
21. Verifikasi Formula Builder tampil
22. Verifikasi kontrol Placeholder, Value Type, dan toggle Required disembunyikan
23. Verifikasi Scope tetap tampil

#### Penutupan form

24. Klik `[✕]`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Create dibuka sekali di langkah 1 dan Data Type diganti berurutan untuk lima TC (halaman yang sama dipakai berulang, prinsip 13 bagian 3); satu-satunya kejadian menutup modal adalah langkah 24 (S-08).
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih Data Type pada tiap TC sebagai bagian langkah TC dan penutupan form dirty pada langkah 24 dan dua langkah berikutnya.
- Temuan untuk QA:
  - TC-FA-CF-72 sampai 76 tidak menyebut apakah mengganti Data Type pada form Create menampilkan dialog konfirmasi; spec mengasumsikan penggantian tanpa dialog sesuai TC (tidak ada Expected dialog).
  - Dropdown pada TC-FA-CF-72 butir a menyebut helper dan chip input dalam satu butir; spec memecahnya per klausa (S-01).
