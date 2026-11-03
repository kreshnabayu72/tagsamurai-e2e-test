---
id: TC-FA-CF-E2E-022-placeholder-default-per-data-type
title: "Placeholder Default per Data Type pada Create"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-59
  - TC-FA-CF-86
  - TC-FA-CF-87
coverage:
  web: automated
---

# Placeholder Default per Data Type pada Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup (hanya dibaca): Pre-setup #35, empat belas field `Sample Item` pada tab Purchasing Company Alpha, satu per Data Type, Placeholder dikosongkan, Scope General. Keempat belas baris melebihi ukuran halaman default tabel (10); langkah 1 menaikkan ukuran halaman menjadi 25 baris (TC-FA-CF-59 langkah 1) agar semuanya tampil dalam satu halaman.
- Tabel Placeholder default (parameter langkah 4; urutan Data Type mengikuti Expected TC-FA-CF-59):

    | No | Data Type | Placeholder default |
    |---|---|---|
    | 1 | `Text` | `Enter sample item` |
    | 2 | `Text Area` | `Enter sample item` |
    | 3 | `Dropdown` | `Select sample item` |
    | 4 | `Multi-Dropdown` | `Select sample item` |
    | 5 | `Date` | `Select date` |
    | 6 | `DateTime` | `Select date and time` |
    | 7 | `Numeric` | `Enter sample item` |
    | 8 | `Percentage` | `Enter percentage` |
    | 9 | `Currency` | `Enter amount` |
    | 10 | `Phone` | `Enter phone number` |
    | 11 | `Email` | `Enter email address` |
    | 12 | `URL` | `Enter URL` |
    | 13 | `Document` | `Upload document` |
    | 14 | `Formula` | `—` |

- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit):
  - D-1: Field Name `Serial Number {runId}-022`, Data Type Text, Placeholder kosong (nilai efektif `Enter serial number {runId}-022`).
  - D-2: Field Name `Serial Number Scan {runId}-022`, Data Type Text, Placeholder `Scan the sticker`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-022`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-59: Placeholder default terisi otomatis menurut keempat belas Data Type

1. Atur ukuran halaman tabel menjadi 25 baris
2. Klik tab `Purchasing`
3. Ketik Search `Sample Item`, tekan Enter
4. Untuk setiap baris tabel Placeholder default pada Prerequisites (langkah 4; 14 iterasi): Verifikasi kolom Placeholder baris `Sample Item` ber-Data Type baris tabel menampilkan nilai Placeholder default baris tabel
5. Klik `(←)` pada kotak Search
6. Klik tab `General`

### TC-FA-CF-86: Placeholder dikosongkan memakai placeholder default tipe data pada field tersimpan

7. Klik `[+ Custom Field]`
8. Isi Field Name `Serial Number {runId}-022`, Data Type `Text`, Placeholder dikosongkan
9. Klik `[Submit]`
10. Ketik Search `Serial Number {runId}-022`, tekan Enter
11. Verifikasi kolom Placeholder baris `Serial Number {runId}-022` menampilkan `Enter serial number {runId}-022`

### TC-FA-CF-87: Placeholder yang diisi dipakai sebagai nilai efektif

12. Klik `[+ Custom Field]`
13. Isi Field Name `Serial Number Scan {runId}-022`, Data Type `Text`, Placeholder `Scan the sticker`
14. Klik `[Submit]`
15. Ganti isi kotak search dengan `Serial Number Scan {runId}-022`, tekan Enter
16. Verifikasi kolom Placeholder baris `Serial Number Scan {runId}-022` menampilkan `Scan the sticker`
17. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 4 diulang 14 kali (satu per baris tabel Placeholder default); parameter iterasi ada di tabel Prerequisites; dihitung dengan ekspansi spec ini 30 langkah.
- Field Dinamis bernama bersuffix `{runId}-022` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Nilai efektif Placeholder default mengikuti Field Name bersuffix: `Enter ` diikuti nama field huruf kecil (`Enter serial number {runId}-022`).
- Langkah penghubung (aksi tanpa `Verifikasi`): mengatur ukuran halaman tabel menjadi 25 baris (langkah 1; S-14, supaya keempat belas baris `Sample Item` tampil dalam satu halaman, mengikuti TC-FA-CF-59 langkah 1), klik tab `Purchasing` dan `General`, Search untuk menemukan baris target (langkah 3, 10, 15, R-16), dan `Klik (←)` untuk mereset Search.
- TC-FA-CF-204 (Placeholder default dari Field Name huruf kecil) ada di spec 166 (pembagian TC lintas spec: TC-FA-CF-204 hanya di spec 166).
- Temuan untuk QA:
  - TC-FA-CF-59 langkah 1 menyebut ukuran halaman "25 baris atau lebih" tanpa nilai pasti dan Data Uji tidak mencantumkan N; spec memakai 25 baris. Kontrol ukuran halaman tidak disebut TC; spec menulis "Atur ukuran halaman tabel menjadi 25 baris".
  - Urutan Expected TC-FA-CF-59 butir g sampai i (Numeric, Percentage, Currency) berbeda dari urutan daftar Data Type PRD pada TC-FA-CF-58 (Currency, Numeric, Percentage); spec mengikuti Expected TC dan mengidentifikasi baris lewat kolom Data Type.
