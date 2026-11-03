---
id: TC-FA-CF-E2E-049-formula-builder-validasi-token
title: "Formula Builder: Validasi Token Kosong, Tanpa Operator, Diawali Operator, dan Dua Operator Berurutan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-150
  - TC-FA-CF-151
  - TC-FA-CF-152
  - TC-FA-CF-153
coverage:
  web: automated
---

# Formula Builder: Validasi Token Kosong, Tanpa Operator, Diawali Operator, dan Dua Operator Berurutan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Field standar numerik yang dirujuk Formula: `Purchase Price` (satu-satunya operan yang disebut PRD, NC-16).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-049`): `Formula Test {runId}-049` (Formula; tidak tersimpan). Tidak ada field yang tersimpan oleh spec ini.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-049`.
- Kemampuan teknis: penyusunan token Formula Builder (token field, konstanta angka, operator `+`, `−`, `×`, `÷`); label kontrol builder tidak diasersi sampai Open Item OI-01 PRD dijawab.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-150: Formula tanpa token ditolak saat Submit

2. Isi Field Name `Formula Test {runId}-049`, pilih Data Type `Formula`
3. Biarkan Formula Builder kosong
4. Klik [Submit]
5. Verifikasi pesan inline "Formula must contain at least one field or number" tampil
6. Verifikasi field tidak tersimpan: modal tetap terbuka
7. Klik [Clear Field]

### TC-FA-CF-151: Dua nilai berturutan tanpa operator ditolak langsung saat menyusun token

8. Isi Field Name `Formula Test {runId}-049`, pilih Data Type `Formula`
9. Susun token field `Purchase Price` lalu konstanta `10` tanpa operator di antaranya
10. Verifikasi pesan inline "Insert an operator between values" tampil langsung di builder
11. Klik [Clear Field]

### TC-FA-CF-152: Formula diawali operator ditolak langsung saat menyusun token

12. Isi Field Name `Formula Test {runId}-049`, pilih Data Type `Formula`
13. Tambahkan operator `+` sebagai token pertama
14. Verifikasi pesan inline "Formula cannot start with an operator" tampil langsung
15. Klik [Clear Field]

### TC-FA-CF-153: Dua operator berurutan ditolak langsung dengan pesan nilai di antara operator

16. Isi Field Name `Formula Test {runId}-049`, pilih Data Type `Formula`
17. Susun token field `Purchase Price`, operator `+`, lalu operator `×`
18. Verifikasi pesan inline "Insert a value between operators" tampil langsung
19. Klik `[✕]`
20. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`

### Penutup: field yang ditolak tidak tersimpan

22. Ketik Search `Formula Test {runId}-049`, tekan Enter
23. Verifikasi empty state "No results found" tampil (field `Formula Test {runId}-049` tidak tersimpan)
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (150, 151, 152, 153). Keempat TC memakai modal yang sama tanpa Submit sukses; [Clear Field] (langkah 7, 11, 15) mengosongkan builder dan pesan inline tanpa menutup modal sehingga langkah "Klik [+ Custom Field]" TC-FA-CF-151 sampai TC-FA-CF-153 tidak diulang (jumlah buka form 1 sama dengan kejadian menutup pada langkah 19 sampai 21; R-12 untuk pesan inline berurutan).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 11, 15, 19, 21, 22, 24, serta penyusunan token dan pengisian form sebagai bagian langkah TC. Langkah 22 sampai 24 memakai empty state hasil Search sebagai anchor positif (bagian 8b butir 2) bahwa field tidak tersimpan.
- Teks Expected TC-FA-CF-151 sampai TC-FA-CF-153 ("tampil langsung") diasersi sesaat sesudah token disusun, sebelum langkah berikutnya (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-CF-151 sampai TC-FA-CF-153 tidak menyebut label kontrol Formula Builder ataupun cara memilih token; spec memakai istilah PRD (token field, konstanta, operator) sesuai NC-16.
  - Nama field memakai suffix `{runId}-049` (S-12) sehingga tidak sama dengan `Formula Test` pada Data Uji TC.
