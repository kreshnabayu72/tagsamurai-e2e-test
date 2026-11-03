---
id: TC-FA-CF-E2E-053-create-sukses-email-url-document-formula
title: "Create Sukses per Data Type: Email, URL, Document, dan Formula"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-167
  - TC-FA-CF-168
  - TC-FA-CF-169
  - TC-FA-CF-170
coverage:
  web: automated
---

# Create Sukses per Data Type: Email, URL, Document, dan Formula

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Field standar numerik yang dirujuk Formula: `Purchase Price` (satu-satunya operan yang disebut PRD, NC-16).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-053`; Placeholder, Scope, Value Type, dan Required dibiarkan default). Parameter iterasi Create (langkah 1 sampai 6):

  | No | Field Name | Data Type | Isi kolom yang diverifikasi |
  |---|---|---|---|
  | 1 | HP Email {runId}-053 | Email | Placeholder `Enter email address` |
  | 2 | HP URL {runId}-053 | URL | Placeholder `Enter URL` |
  | 3 | HP Document {runId}-053 | Document | Placeholder `Upload document` |

  Field Formula `HP Formula {runId}-053` dengan formula `Purchase Price + 1` dibuat pada langkah 7 sampai 12.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-053`.
- Kemampuan teknis: penyusunan token Formula Builder (token field, konstanta angka, operator); pembacaan sel tabel (Data Type, Placeholder, Scope, Value Type, Required) dan state switch Active.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-167 sampai TC-FA-CF-169: Create field Email, URL, dan Document

1. Untuk setiap baris tabel Create pada Prerequisites (langkah 1 sampai 6): klik [+ Custom Field]
2. Isi Field Name dan pilih Data Type baris itu
3. Klik [Submit]
4. Verifikasi modal tertutup
5. Verifikasi toast "Success, custom field has been created." tampil
6. Tunggu toast lama hilang otomatis

### TC-FA-CF-170: Create field Data Type Formula

7. Klik [+ Custom Field]
8. Isi Field Name `HP Formula {runId}-053`, pilih Data Type `Formula`
9. Susun token field `Purchase Price`, operator `+`, konstanta `1`
10. Klik [Submit]
11. Verifikasi modal tertutup
12. Verifikasi toast "Success, custom field has been created." tampil

### Baris tabel hasil Create

13. Ketik Search `{runId}-053`, tekan Enter
14. Verifikasi tabel menampilkan 4 baris baru pada tab General (`HP Document {runId}-053`, `HP Email {runId}-053`, `HP Formula {runId}-053`, `HP URL {runId}-053`)
15. Untuk setiap baris tabel Create pada Prerequisites (langkah 15 sampai 16): Verifikasi Data Type baris itu sesuai kolom Data Type
16. Verifikasi isi kolom Placeholder baris itu sesuai kolom "Isi kolom yang diverifikasi"
17. Verifikasi Data Type baris `HP Formula {runId}-053` adalah `Formula`
18. Verifikasi Scope baris Email, URL, dan Document adalah `General`
19. Verifikasi Value Type baris Email, URL, dan Document adalah `Specific`
20. Verifikasi Required baris Email, URL, dan Document adalah `No`
21. Verifikasi switch Active setiap baris ON
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 sampai 6 diulang untuk tiga baris tabel Create (TC-FA-CF-167 sampai TC-FA-CF-169); langkah 15 sampai 16 diulang untuk tiga baris yang sama (parameter di Prerequisites). TC-FA-CF-170 ditulis eksplisit (langkah 7 sampai 12) karena memakai Formula Builder. Urutan mengikuti TC sumber. Expected b diasersi sekali pada hasil Search (langkah 15 sampai 21) karena keempat baris tampil bersamaan di tab General.
- Spec berada di sekitar batas 35 langkah dengan ekspansi (3 iterasi enam langkah, 3 iterasi dua langkah, dan 15 langkah lain): satu topik (Create sukses per Data Type), satu dataset, dan tiap Create memakai nama field sendiri sehingga kegagalan satu Data Type tidak menghilangkan makna Data Type lain (bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3, 7 sampai 10 (membuka modal, mengisi form, menyusun token, Submit; bagian langkah TC), 13 (Search), dan 22 (`(←)` menutup Search). Langkah 14 adalah pembanding sebelum asersi universal langkah 18 sampai 21 (bagian 8b butir 2, S-03), bukan Expected TC.
- Expected b TC-FA-CF-170 hanya Data Type `Formula` dan switch Active ON (langkah 17 dan 21); kolom lain baris Formula tidak diasersi di spec ini (nilai `—` untuk Placeholder, Value Type, dan Required diasersi di spec lain).
- Langkah penghubung toast (S-03, R-22): langkah 6 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) berada di akhir badan perulangan sehingga tiap iterasi dimulai tanpa toast lama; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-169: Placeholder `Upload document` diasersi pada kolom Placeholder tabel; TC tidak menyebut kontrol unggah pada baris.
  - Nama field memakai suffix `{runId}-053` (S-12) sehingga tidak sama dengan `HP Email`, `HP URL`, `HP Document`, dan `HP Formula` pada Data Uji TC.
