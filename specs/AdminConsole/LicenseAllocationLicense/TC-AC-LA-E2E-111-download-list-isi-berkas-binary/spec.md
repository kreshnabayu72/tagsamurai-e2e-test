---
id: TC-AC-LA-E2E-111-download-list-isi-berkas-binary
title: "Download List: Isi Berkas CSV dan XLSX, BOM, Urutan Baris, dan Tanggal Mengikuti General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-344
  - TC-AC-LA-345
  - TC-AC-LA-346
  - TC-AC-LA-423
coverage:
  web: automated
---

# Download List: Isi Berkas CSV dan XLSX, BOM, Urutan Baris, dan Tanggal Mengikuti General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada tab Current dan 25 entri Changelog; Status `Waiting for Approval`; Quantity `+50 GB`; Cost `$3,650.00`; sel kosong `—`) bersifat baca-saja untuk spec ini.
- State global: General Settings Date Format `dd MMM yy` dan Time Format 24 jam (precondition TC-AC-LA-423), diatur fixture backend yang disediakan tim FE di hook `before` dan dipulihkan ke nilai awal di hook `after`; suite berjalan serial.
- Kemampuan teknis (kelas harness binary buffer): membaca isi berkas CSV dan XLSX hasil unduhan (nilai sel, tipe sel, BOM encoding UTF-8, nama sheet) disediakan tim FE; berkas unduhan dihapus di hook `after`. Spec menyimpan konfigurasi kolom Setup Column (menampilkan `Cost` dan `Paid From`); hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`), disediakan tim FE.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-344: Transformasi isi berkas

1. Buka Popup Setup Column
2. Centang `Cost` dan `Paid From`
3. Klik `[Save]`
4. Download as XLSX
5. Buka berkas XLSX hasil unduhan
6. Verifikasi Status ditulis sebagai teks label (`Waiting for Approval`) tanpa warna
7. Verifikasi Quantity dan Cost ditulis sebagai sel angka asli tanpa simbol dan pemisah ribuan (`50`, `3650`)
8. Verifikasi nilai kosong ditulis `-` (hyphen tunggal)
9. Verifikasi Last Updated memakai Date Format dan Time Format General Settings

### TC-AC-LA-345: CSV UTF-8 dengan BOM, Sheet1, dan nol baris

10. Ketik Search `zzzzqqqq`, tekan Enter
11. Verifikasi `No results found` tampil
12. Verifikasi tombol Download tetap aktif
13. Download as CSV
14. Verifikasi tidak ada toast tampil
15. Download as XLSX
16. Verifikasi tidak ada toast tampil
17. Buka berkas CSV hasil unduhan
18. Verifikasi berkas CSV berencoding UTF-8 dengan BOM
19. Verifikasi berkas CSV hanya memuat baris header kolom yang tampil
20. Buka berkas XLSX hasil unduhan
21. Verifikasi berkas XLSX memakai sheet `Sheet1`
22. Verifikasi berkas XLSX hanya memuat baris header

### TC-AC-LA-346: Urutan baris berkas mengikuti Sort

23. Klik ikon panah `(←)`
24. Klik header Quantity
25. Download as CSV
26. Buka berkas CSV hasil unduhan
27. Verifikasi urutan baris berkas sama dengan urutan tabel

### TC-AC-LA-423: Tanggal dan jam berkas mengikuti General Settings

28. Download as XLSX pada List
29. Klik ikon Changelog
30. Download as XLSX pada Modal Changelog
31. Klik `[✕]` pada Modal Changelog
32. Buka berkas XLSX List hasil unduhan
33. Verifikasi kolom tanggal berkas List memakai Date Format `dd MMM yy` dan Time Format 24 jam General Settings
34. Buka berkas XLSX Changelog hasil unduhan
35. Verifikasi kolom tanggal berkas Changelog memakai Date Format `dd MMM yy` dan Time Format 24 jam General Settings

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Kelas harness spec: binary buffer (isi berkas); nama berkas dan jumlah baris diasersi spec 110.
- Langkah `Download as CSV` dan `Download as XLSX` berarti: klik ikon Download lalu pilih opsi dengan nama itu. Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions, lalu klik `Setup Column...`.
- Absence toast (langkah 14 dan 16) diletakkan segera setelah pemicu dan sebelum asersi berkas; `No results found` dan tombol Download aktif (langkah 11 dan 12) menjadi anchor positif (konvensi bagian 8b butir 11).
- Langkah penghubung (S-03): langkah 5, 17, 20, 26, 32, 34 (membuka berkas hasil unduhan), langkah 23 (menutup search bar), langkah 31 (menutup modal).
- Temuan untuk QA:
  - TC-AC-LA-344 butir d tidak menyebut nilai Date Format dan Time Format; spec memakai nilai precondition TC-AC-LA-423 (`dd MMM yy`, 24 jam) yang diatur fixture backend sebelum spec.
  - TC-AC-LA-423 mengubah state global General Settings tetapi tidak menyebut cara dan akun pengaturannya; ditulis "disediakan tim FE" (S-13).
  - TC-AC-LA-344 menyebut Quantity `+50 GB` menjadi `50` tanpa menyebut satuan; spec mengasersi `50` apa adanya.
