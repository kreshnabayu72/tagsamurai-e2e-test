---
id: TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom
title: "Download List: Seluruh Baris, Baris Terfilter, Nama Berkas History, dan Kolom Disembunyikan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-340
  - TC-AC-LA-341
  - TC-AC-LA-342
  - TC-AC-LA-343
coverage:
  web: automated
---

# Download List: Seluruh Baris, Baris Terfilter, Nama Berkas History, dan Kolom Disembunyikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; Client `PT Sejahtera`; Product `FAMS`). Jumlah total baris tab Current (N) dan tab History diturunkan dari seeding #54, bukan dibaca dari satu halaman tabel (konvensi bagian 8b butir 10). Seed bersifat baca-saja untuk spec ini.
- Kemampuan teknis: membaca berkas hasil unduhan peramban untuk nama berkas, jumlah baris, dan baris header (bukan isi sel; isi sel diuji spec Download isi berkas), disediakan tim FE. Berkas unduhan dihapus di hook `after`. Spec menyembunyikan kolom `Client` lewat overlay Column Visibility; hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`), disediakan tim FE.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-340: Download tab Current tanpa penyaring

1. Download as CSV
2. Verifikasi tidak ada toast sukses tampil
3. Verifikasi berkas `License-Allocation-Current.csv` terunduh
4. Verifikasi berkas memuat seluruh baris tab Current (lebih dari 10; jumlah baris sama dengan N tab Current dari seeding)

### TC-AC-LA-341: Download dengan Search dan Filter aktif

5. Ketik Search `Sejahtera`, tekan Enter
6. Terapkan filter Product `FAMS`
7. Download as XLSX
8. Verifikasi berkas `License-Allocation-Current.xlsx` terunduh
9. Verifikasi berkas hanya memuat baris yang cocok kedua kriteria dari semua halaman (jumlah baris sama dengan jumlah total hasil pada tabel)
10. Verifikasi sheet bernama `Sheet1`

### TC-AC-LA-342: Download tab History

11. Klik menu `License Allocation` di sidebar
12. Klik tab `History`
13. Download as CSV
14. Verifikasi berkas `License-Allocation-History.csv` terunduh
15. Verifikasi berkas hanya memuat baris tab History (jumlah baris sama dengan N tab History dari seeding)

### TC-AC-LA-343: Kolom disembunyikan tidak ikut diekspor

16. Klik menu `License Allocation` di sidebar
17. Klik `⋯` pada header kolom Actions
18. Hapus centang `Client` di overlay Column Visibility
19. Tekan `Esc` untuk menutup overlay
20. Download as CSV
21. Verifikasi tidak ada toast peringatan tampil
22. Verifikasi berkas pertama terunduh tanpa kolom Client
23. Klik `⋯` pada header kolom Actions
24. Centang `Client` di overlay Column Visibility
25. Tekan `Esc` untuk menutup overlay
26. Download as CSV
27. Verifikasi berkas kedua memuat kolom Client

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-344, TC-AC-LA-345, TC-AC-LA-346, dan TC-AC-LA-423 (isi berkas) ada di spec 111; TC-AC-LA-348 ada di spec 112.
- Langkah `Download as CSV` dan `Download as XLSX` berarti: klik ikon Download lalu pilih opsi dengan nama itu. Langkah `Terapkan filter <Field> <opsi>` berarti: klik ikon Filter, buka dropdown Field, centang opsi, klik `[Apply]`.
- Absence toast (langkah 2 dan 21) diletakkan segera setelah pemicu dan sebelum asersi berkas; pemicu dan berkas terunduh menjadi anchor positif (konvensi bagian 8b butir 11).
- Langkah penghubung (S-03): langkah 11 dan 16 (klik menu sidebar mereset Search, Sort, Filter, dan paginasi), langkah 19, 25 (menutup overlay).
- Temuan untuk QA:
  - TC-AC-LA-340 butir b ("Tidak ada toast sukses") bersifat absence atas toast dan tidak menyebut waktu pengamatan; spec memakai anchor pemicu dan berkas terunduh.
  - TC-AC-LA-343 butir a ("tanpa toast peringatan") tidak menyebut teks toast peringatan yang dimaksud; spec mengasersi tidak ada toast tampil.
  - TC-AC-LA-340 dan TC-AC-LA-342 menyebut "seluruh baris" tanpa N; N diturunkan dari seeding Pre-setup #54.
