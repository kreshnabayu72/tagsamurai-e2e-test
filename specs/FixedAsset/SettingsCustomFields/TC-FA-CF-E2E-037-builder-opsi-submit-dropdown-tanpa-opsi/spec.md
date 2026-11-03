---
id: TC-FA-CF-E2E-037-builder-opsi-submit-dropdown-tanpa-opsi
title: "Builder Opsi: Submit Dropdown dan Multi-Dropdown Tanpa Opsi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-119
  - TC-FA-CF-120
coverage:
  web: automated
---

# Builder Opsi: Submit Dropdown dan Multi-Dropdown Tanpa Opsi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name `Zero Multi {runId}-037`, `Removed Last {runId}-037`; opsi `Temp`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-119: Submit Multi-Dropdown tanpa opsi ditolak dengan pesan Dropdown options

1. Klik `[+ Custom Field]`
2. Pilih Data Type `Multi-Dropdown`
3. Isi Field Name `Zero Multi {runId}-037`
4. Klik `[Submit]`
5. Verifikasi pesan inline `Dropdown options must not be empty` tampil

#### TC-FA-CF-120: Submit setelah opsi terakhir dihapus dari form ditolak

6. Klik `[Clear Field]`
7. Pilih Data Type `Dropdown`
8. Isi Field Name `Removed Last {runId}-037`
9. Ketik `Temp` pada input Values lalu tekan Enter
10. Klik `✕` pada badge `Temp`
11. Klik `[Submit]`
12. Verifikasi pesan inline `Dropdown options must not be empty` tampil
13. Klik `[✕]`
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Verifikasi tabel tab General memuat 8 baris (TC-FA-CF-119 dan TC-FA-CF-120 butir b: field tidak tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 13 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-037` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-119 dan TC-FA-CF-120 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
