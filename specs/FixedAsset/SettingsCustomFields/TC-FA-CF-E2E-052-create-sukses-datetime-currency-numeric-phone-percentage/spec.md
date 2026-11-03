---
id: TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage
title: "Create Sukses per Data Type: DateTime, Currency, Numeric, Phone, dan Percentage"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-162
  - TC-FA-CF-163
  - TC-FA-CF-164
  - TC-FA-CF-165
  - TC-FA-CF-166
coverage:
  web: automated
---

# Create Sukses per Data Type: DateTime, Currency, Numeric, Phone, dan Percentage

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-052`; Placeholder, Scope, Value Type, dan Required dibiarkan default; Decimal Places Numeric dibiarkan default). Parameter iterasi Create (langkah 1 sampai 6):

  | No | Field Name | Data Type | Isi kolom yang diverifikasi |
  |---|---|---|---|
  | 1 | HP DateTime {runId}-052 | DateTime | Placeholder `Select date and time` |
  | 2 | HP Currency {runId}-052 | Currency | Placeholder `Enter amount` |
  | 3 | HP Numeric {runId}-052 | Numeric | Value Setting `0 Decimal Places` |
  | 4 | HP Phone {runId}-052 | Phone | Placeholder `Enter phone number` |
  | 5 | HP Percentage {runId}-052 | Percentage | Placeholder `Enter percentage` |

- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-052`.
- Kemampuan teknis: pembacaan sel tabel (Data Type, Placeholder, Value Setting, Scope, Value Type, Required) dan state switch Active.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-162 sampai TC-FA-CF-166: Create field per Data Type

1. Untuk setiap baris tabel Create pada Prerequisites (langkah 1 sampai 6): klik [+ Custom Field]
2. Isi Field Name dan pilih Data Type baris itu
3. Klik [Submit]
4. Verifikasi modal tertutup
5. Verifikasi toast "Success, custom field has been created." tampil
6. Tunggu toast lama hilang otomatis

### Baris tabel hasil Create

7. Ketik Search `{runId}-052`, tekan Enter
8. Verifikasi tabel menampilkan 5 baris baru pada tab General (`HP Currency {runId}-052`, `HP DateTime {runId}-052`, `HP Numeric {runId}-052`, `HP Percentage {runId}-052`, `HP Phone {runId}-052`)
9. Untuk setiap baris tabel Create pada Prerequisites (langkah 9 sampai 10): Verifikasi Data Type baris itu sesuai kolom Data Type
10. Verifikasi isi kolom Placeholder atau Value Setting baris itu sesuai kolom "Isi kolom yang diverifikasi"
11. Verifikasi Scope setiap baris adalah `General`
12. Verifikasi Value Type setiap baris adalah `Specific`
13. Verifikasi Required setiap baris adalah `No`
14. Verifikasi switch Active setiap baris ON
15. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 sampai 6 diulang untuk lima baris tabel Create (TC-FA-CF-162 sampai TC-FA-CF-166); langkah 9 sampai 10 diulang untuk lima baris yang sama (parameter di Prerequisites). Urutan baris mengikuti TC sumber. Langkah 1 sampai 5 per iterasi adalah Expected a ("modal tertutup", "toast sukses"); langkah 9 sampai 14 adalah Expected b dan diasersi sekali pada hasil Search karena kelima baris tampil bersamaan di tab General.
- Spec melewati sekitar 35 langkah dengan ekspansi (5 iterasi enam langkah, 5 iterasi dua langkah, dan 11 langkah lain; bagian 3 prinsip 13 konvensi): satu topik (Create sukses per Data Type), satu dataset, dan tiap Create memakai nama field sendiri sehingga kegagalan satu Data Type tidak menghilangkan makna Data Type lain; blok ulang berparameter di tabel Prerequisites (bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3 (membuka modal, mengisi form, Submit; bagian langkah TC), 7 (Search), dan 15 (`(←)` menutup Search). Langkah 8 adalah pembanding sebelum asersi universal langkah 11 sampai 14 (bagian 8b butir 2, S-03), bukan Expected TC.
- Placeholder default DateTime, Currency, Phone, dan Percentage bernilai tetap (`Select date and time`, `Enter amount`, `Enter phone number`, `Enter percentage`) dan tidak bergantung pada Field Name bersuffix.
- Langkah penghubung toast (S-03, R-22): langkah 6 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) berada di akhir badan perulangan sehingga tiap iterasi dimulai tanpa toast lama; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-164: Value Setting `0 Decimal Places` untuk Numeric mengikuti Decimal Places default; TC tidak menyebut Decimal Places yang dipilih pada Langkah Uji, sehingga spec membiarkan nilai default.
  - Nama field memakai suffix `{runId}-052` (S-12) sehingga tidak sama dengan `HP DateTime`, `HP Currency`, `HP Numeric`, `HP Phone`, dan `HP Percentage` pada Data Uji TC.
