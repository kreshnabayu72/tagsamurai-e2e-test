---
id: TC-AC-LA-E2E-120-filter-list-multi-select-per-field
title: "Filter List: Eksekusi Multi-select Delapan Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-292
coverage:
  web: automated
---

# Filter List: Eksekusi Multi-select Delapan Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada tab Current; setiap nilai pada tabel parameter ada pada sedikitnya satu baris tab Current) bersifat baca-saja untuk spec ini.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Plan` dan `Paid From`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Parameter langkah 6 sampai 15, satu baris per field:

| Field | Opsi yang dicentang |
|---|---|
| License Type | `Concurrent User` |
| Product | `FAMS` |
| Client | `PT Sejahtera` |
| Subscription ID | `SUBS-20260101-A1B2C` |
| Plan | `Professional` |
| Plan Owner | `PT Maju Bersama (Distributor)` |
| Allocated By | `Dewi A` |
| Paid From | `PT ABC (Principal)` |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-292: Eksekusi filter multi-select

1. Klik `⋯` pada header kolom Actions
2. Klik `Setup Column...`
3. Centang `Plan` dan `Paid From`
4. Klik `[Save]`
5. Catat isi halaman pertama tabel sebagai baseline
6. Untuk setiap baris tabel parameter (langkah 6 sampai 15): klik ikon Filter
7. Buka dropdown Field
8. Verifikasi dropdown Field punya kotak cari dan multi-select
9. Centang Opsi yang dicentang
10. Klik `[Apply]`
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi setiap baris hasil ber-Field Opsi yang dicentang
13. Klik ikon Filter
14. Klik `[Clear Field]` lalu `[Apply]`
15. Verifikasi tabel kembali memuat semua baris tab (isi halaman pertama sama dengan baseline langkah 5)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Langkah 6 sampai 15 diulang untuk delapan baris tabel parameter (80 langkah terekspansi, total sekitar 85). Verifikasi tetap satu per klausa per iterasi (butir a sampai h, i, dan j TC-AC-LA-292).
- Alasan spec melewati sekitar 35 langkah: satu TC, satu topik, satu dataset (#54, baca-saja); langkah diulang per field dengan parameter di tabel Prerequisites tanpa langkah bersyarat (konvensi bagian 8b butir 7).
- Langkah penghubung (S-03): langkah 1 sampai 4 (menampilkan kolom Plan dan Paid From agar hasil filter dapat diperiksa, sesuai langkah 1 TC), langkah 5 (baseline), langkah 13 dan 14 (membersihkan filter).
- Temuan untuk QA:
  - TC-AC-LA-292 Expected i ("tabel kembali memuat semua baris tab") tidak menyebut cara membandingkan; spec membandingkan isi halaman pertama dengan baseline.
  - Opsi yang dicentang untuk `Subscription ID`, `Plan`, `Plan Owner`, dan `Paid From` diasumsikan berada pada baris tab Current seed #54 (nilai dari Data Uji TC).
