---
id: TC-AC-LA-E2E-119-search-list-kolom-teks-dan-quantity
title: "Search List: Kelas Teks Kolom Tampil dan Kolom Quantity"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-281
  - TC-AC-LA-284
coverage:
  web: automated
---

# Search List: Kelas Teks Kolom Tampil dan Kolom Quantity

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status; Quantity `+2`, `+5`, `+10`, `+50 GB`, `—`; License Type termasuk `Asset Control App` dengan Quantity `—`) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Parameter langkah 1 sampai 5 (TC-AC-LA-281), satu baris per kolom:

| Kolom | Kata kunci | Variasi huruf | Nilai sel yang cocok |
|---|---|---|---|
| Allocation ID | `LALC-2026` | `lalc-2026` | Allocation ID berawalan `LALC-2026` |
| License Type | `audit` | `AUDIT` | `Addon (Audit)` |
| Product | `fams` | `FAMS` | `FAMS` |
| Client | `sejah` | `SEJAH` | `PT Sejahtera` |
| Subscription ID | `A1B2C` | `a1b2c` | `SUBS-20260101-A1B2C` |
| Plan Owner | `maju` | `MAJU` | `PT Maju Bersama (Distributor)` |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-281: Search kelas teks kolom tampil

1. Untuk setiap baris tabel parameter (langkah 1 sampai 5): ketik Search Kata kunci, tekan Enter
2. Verifikasi sedikitnya satu baris dengan Kolom bernilai Nilai sel yang cocok tampil
3. Ganti isi kotak search dengan Variasi huruf, tekan Enter
4. Verifikasi sedikitnya satu baris dengan Kolom bernilai Nilai sel yang cocok tampil, sama seperti hasil Kata kunci
5. Klik `(←)` pada kotak Search
6. Ketik Search `zzzzqqqq`, tekan Enter
7. Verifikasi `No results found` tampil

### TC-AC-LA-284: Search kolom Quantity

8. Ganti isi kotak search dengan `50`, tekan Enter
9. Verifikasi sel Quantity `+50 GB` tampil
10. Ganti isi kotak search dengan `+5`, tekan Enter
11. Verifikasi sel Quantity `+5` dan `+50 GB` tampil
12. Verifikasi baris Asset Control App dengan Quantity `—` tidak tampil
13. Klik ikon panah `(←)`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-280, TC-AC-LA-282, dan TC-AC-LA-283 ada di spec 097.
- Alasan di atas sekitar 35 langkah (13 langkah nominal, sekitar 38 terekspansi): seluruh blok satu topik (Search kolom teks dan Quantity pada List) pada satu dataset baca-saja, dengan langkah berulang berparameter tabel Prerequisites tanpa langkah bersyarat (konvensi bagian 8b butir 7); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 1 sampai 5 diulang untuk enam baris tabel parameter (30 langkah terekspansi; total sekitar 38 langkah terekspansi). Verifikasi tetap satu per klausa per iterasi (butir a sampai f dan klausa tanpa pembedaan huruf pada butir g TC-AC-LA-281).
- Langkah penghubung (S-03): langkah 5 (menutup dan mengosongkan Search antar iterasi), langkah 13 (menutup search bar).
- Temuan untuk QA:
  - TC-AC-LA-281 Expected a menyebut kata kunci `LALC-2026` tanpa nilai Allocation ID lengkap; spec mengasersi baris ber-Allocation ID berawalan `LALC-2026`.
  - TC-AC-LA-284 Expected c ("Sel `—` (Asset Control App) tidak cocok") tidak menyebut baris pembanding; spec memakai baris Asset Control App dengan Quantity `—` dari seed #54 dengan anchor positif langkah 9 dan 11.
