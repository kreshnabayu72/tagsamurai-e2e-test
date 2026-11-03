---
id: TC-AC-LA-E2E-096-sort-list-payment-pindah-kolom-dan-default
title: "Sort List: Payment, Pindah Kolom, dan Default Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-309
  - TC-AC-LA-310
  - TC-AC-LA-311
coverage:
  web: automated
---

# Sort List: Payment, Pindah Kolom, dan Default Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; Quantity `+2`, `+5`, `+10`, `+50 GB`, `—`; Payment `Free` dan `Wallet`) bersifat baca-saja untuk spec ini. Ukuran halaman 100 dipakai agar seluruh nilai Payment berada di halaman teramati (S-14).
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Payment`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-309: Sort Payment dan header Actions

1. Ubah page size ke 100
2. Klik `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Centang `Payment`
5. Klik `[Save]`
6. Klik header Payment
7. Verifikasi ascending `Free` sebelum `Wallet`
8. Klik header Payment
9. Verifikasi descending `Wallet` sebelum `Free`
10. Verifikasi header kolom Actions tidak punya ikon sort

### TC-AC-LA-310: Pindah kolom sort

11. Klik header Client
12. Klik header Quantity
13. Verifikasi indikator sort Client kembali netral
14. Verifikasi Quantity mulai dari ascending

### TC-AC-LA-311: Default sort kedua tab

15. Klik menu `License Allocation` di sidebar
16. Verifikasi tab Current terurut Last Updated dari yang terbaru
17. Klik tab `History`
18. Verifikasi tab History terurut Last Updated dari yang terbaru

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC sort Quantity, Cost, dan Allocated By ada di spec 103.
- Langkah penghubung (S-03): langkah 1 (ukuran halaman 100 agar seluruh nilai Payment teramati), langkah 2 sampai 5 (menampilkan kolom Payment sesuai langkah TC), langkah 15 (klik menu sidebar mereset Sort ke default).
- Temuan untuk QA:
  - TC-AC-LA-309 tidak menyebut ukuran halaman; spec memakai 100 agar nilai `Free` dan `Wallet` berada di halaman teramati.
  - TC-AC-LA-311 tidak menyebut apakah urutan default tab History diuji tanpa sort sebelumnya; spec mereset lewat klik menu sidebar.
