---
id: TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create
title: "Decimal Places Numeric dan Percentage pada Create"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-123
  - TC-FA-CF-124
  - TC-FA-CF-125
  - TC-FA-CF-126
coverage:
  web: automated
---

# Decimal Places Numeric dan Percentage pada Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit). Tabel Create Decimal Places (parameter langkah 1 sampai 9):

    | No | TC | Field Name | Data Type | Radio Decimal Places | Value Setting |
    |---|---|---|---|---|---|
    | 1 | TC-FA-CF-123 | `Numeric DP1 {runId}-039` | `Numeric` | `1 (.0)` | `1 Decimal Place` |
    | 2 | TC-FA-CF-124 | `Numeric DP2 {runId}-039` | `Numeric` | `2 (.00)` | `2 Decimal Places` |
    | 3 | TC-FA-CF-125 | `Percentage DP1 {runId}-039` | `Percentage` | `1 (.0)` | `1 Decimal Place` |
    | 4 | TC-FA-CF-126 | `Percentage DP2 {runId}-039` | `Percentage` | `2 (.00)` | `2 Decimal Places` |

- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-039`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Untuk setiap baris tabel Create Decimal Places pada Prerequisites (langkah 1 sampai 9; 4 iterasi): klik `[+ Custom Field]`
2. Isi Field Name baris tabel dan pilih Data Type baris tabel
3. Pilih radio Decimal Places baris tabel
4. Klik `[Submit]`
5. Verifikasi toast sukses: "Success, custom field has been created."
6. Ketik Search Field Name baris tabel, tekan Enter
7. Verifikasi kolom Value Setting baris tabel menampilkan Value Setting baris tabel
8. Klik `(←)` pada kotak Search
9. Tunggu toast lama hilang otomatis

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Langkah 1 sampai 9 diulang 4 kali (satu per baris tabel Create Decimal Places; blok berparameter, 8b butir 7); tiap iterasi memuat `Verifikasi` per klausa Expected (S-01) tanpa langkah bersyarat; dihitung dengan ekspansi spec ini 36 langkah. Id TC per iterasi ada di kolom TC tabel Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16) dan `Klik (←)` pada kotak Search di akhir tiap iterasi agar Search berikutnya membuka input (8b butir 9).
- Field Dinamis bernama bersuffix `{runId}-039` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Langkah penghubung toast (S-03, R-22): langkah 9 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) berada di akhir badan perulangan sehingga tiap iterasi dimulai tanpa toast lama; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA: tidak ada.
