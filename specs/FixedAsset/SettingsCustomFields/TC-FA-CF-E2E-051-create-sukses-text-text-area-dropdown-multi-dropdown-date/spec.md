---
id: TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date
title: "Create Sukses per Data Type: Text, Text Area, Dropdown, Multi-Dropdown, dan Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-157
  - TC-FA-CF-158
  - TC-FA-CF-159
  - TC-FA-CF-160
  - TC-FA-CF-161
coverage:
  web: automated
---

# Create Sukses per Data Type: Text, Text Area, Dropdown, Multi-Dropdown, dan Date

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-051`; Placeholder, Scope, Value Type, dan Required dibiarkan default). Parameter iterasi Create (langkah 1 sampai 6):

  | No | Field Name | Data Type | Value yang diketik | Isi kolom yang diverifikasi |
  |---|---|---|---|---|
  | 1 | HP Text {runId}-051 | Text | - | Placeholder `Enter hp text {runId}-051` |
  | 2 | HP Text Area {runId}-051 | Text Area | - | Placeholder `Enter hp text area {runId}-051` |
  | 3 | HP Dropdown {runId}-051 | Dropdown | `Class A`, `Class B` | Value Setting `Class A, Class B` |
  | 4 | HP Multi {runId}-051 | Multi-Dropdown | `Charger`, `Cable` | Value Setting `Charger, Cable` |
  | 5 | HP Date {runId}-051 | Date | - | Placeholder `Select date` |

- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-051`.
- Kemampuan teknis: pengisian input Values Dropdown dan Multi-Dropdown (ketik lalu Enter); pembacaan sel tabel (Data Type, Placeholder, Value Setting, Scope, Value Type, Required) dan state switch Active.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-157 sampai TC-FA-CF-161: Create field per Data Type

1. Untuk setiap baris tabel Create pada Prerequisites (langkah 1 sampai 6): klik [+ Custom Field]
2. Isi Field Name dan pilih Data Type baris itu; untuk Dropdown dan Multi-Dropdown ketik tiap Value lalu tekan Enter
3. Klik [Submit]
4. Verifikasi modal tertutup
5. Verifikasi toast "Success, custom field has been created." tampil
6. Tunggu toast lama hilang otomatis

### Baris tabel hasil Create

7. Ketik Search `{runId}-051`, tekan Enter
8. Verifikasi tabel menampilkan 5 baris baru pada tab General (`HP Date {runId}-051`, `HP Dropdown {runId}-051`, `HP Multi {runId}-051`, `HP Text {runId}-051`, `HP Text Area {runId}-051`)
9. Untuk setiap baris tabel Create pada Prerequisites (langkah 9 sampai 10): Verifikasi Data Type baris itu sesuai kolom Data Type
10. Verifikasi isi kolom Placeholder atau Value Setting baris itu sesuai kolom "Isi kolom yang diverifikasi"
11. Verifikasi Scope setiap baris adalah `General`
12. Verifikasi Value Type setiap baris adalah `Specific`
13. Verifikasi Required setiap baris adalah `No`
14. Verifikasi switch Active setiap baris ON
15. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 sampai 6 diulang untuk lima baris tabel Create (TC-FA-CF-157 sampai TC-FA-CF-161); langkah 9 sampai 10 diulang untuk lima baris yang sama (parameter di Prerequisites). Urutan baris mengikuti TC sumber. Langkah 1 sampai 5 per iterasi adalah Expected a ("modal tertutup", "toast sukses"); langkah 9 sampai 14 adalah Expected b dan diasersi sekali pada hasil Search karena kelima baris tampil bersamaan di tab General.
- Spec melewati sekitar 35 langkah dengan ekspansi (5 iterasi enam langkah, 5 iterasi dua langkah, dan 11 langkah lain; bagian 3 prinsip 13 konvensi): satu topik (Create sukses per Data Type), satu dataset, dan tiap Create memakai nama field sendiri sehingga kegagalan satu Data Type tidak menghilangkan makna Data Type lain; blok ulang berparameter di tabel Prerequisites (bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3 (membuka modal, mengisi form, Submit; bagian langkah TC), 7 (Search), dan 15 (`(←)` menutup Search). Langkah 8 adalah pembanding sebelum asersi universal langkah 11 sampai 14 (bagian 8b butir 2, S-03), bukan Expected TC.
- Nilai Placeholder default diturunkan dari Field Name bersuffix (`Enter hp text {runId}-051`); asersi memakai nama bersuffix yang sama (R-06). Placeholder `Select date` untuk Date bernilai tetap.
- Langkah penghubung toast (S-03, R-22): langkah 6 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) berada di akhir badan perulangan sehingga tiap iterasi dimulai tanpa toast lama; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-157 sampai TC-FA-CF-161: Expected Placeholder `Enter hp text` diturunkan dari Field Name `HP Text` pada Data Uji TC; TC tidak menyatakan aturan penurunannya untuk nama yang diberi suffix. Spec mengasumsikan Placeholder default mengikuti Field Name secara lengkap (huruf kecil) termasuk suffix, dan asersi dapat gagal bila backend memangkas atau mengubah suffix.
  - TC-FA-CF-159 dan TC-FA-CF-160: Value Setting `Class A, Class B` dan `Charger, Cable` ditulis sebagai teks berurutan penambahan; TC tidak menyatakan tampilan badge terpisah atau teks tunggal.
  - Nama field memakai suffix `{runId}-051` (S-12) sehingga tidak sama dengan `HP Text`, `HP Text Area`, `HP Dropdown`, `HP Multi`, dan `HP Date` pada Data Uji TC.
