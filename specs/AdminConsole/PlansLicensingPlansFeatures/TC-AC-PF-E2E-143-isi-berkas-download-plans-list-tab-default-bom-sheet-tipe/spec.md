---
id: TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe
title: Isi Berkas Download Plans List Tab Default BOM, Sheet, Tipe Sel, dan Format Tanggal
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-351
  - TC-AC-PF-352
  - TC-AC-PF-635
  - TC-AC-PF-642
  - TC-AC-PF-766
coverage:
  web: automated
---

# Isi Berkas Download Plans List Tab Default BOM, Sheet, Tipe Sel, dan Format Tanggal

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif berurutan `Starter` (FAMS, Free, v2, Clients 12, 15 Jun 26 10:00), `Growth` (FAMS, Paid, v5, 47, 15 Jun 26 10:00), `Professional` (FAMS, Paid, v3, 23, 15 Jun 26 10:00), `Enterprise` (FAMS, Paid, v1, 8, 12 Aug 26 09:00), `SIEM` (SIEM, Paid, v1, 5, 09 Jul 26 11:00). Waktu tersimpan dalam UTC.
- General Settings: baseline (Pre-setup #44) Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC untuk langkah 1 sampai 17; varian Pre-setup #61 untuk langkah 18 sampai 27 (Date Format `dd/MM/yy` dengan Time Format 24-hour dan Time Zone UTC; lalu Date Format `dd MMM yy` dengan Time Format 12-hour dan Time Zone UTC).
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup dan pengaturan General Settings (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung. Kemampuan membaca isi berkas CSV dan XLSX yang terunduh (encoding, BOM, pemisah, nama sheet, tipe sel, nilai sel) disediakan tim FE/BE. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini mengubah General Settings (Date Format, Time Format) dan memulihkannya ke baseline di hook `after` dan pada langkah 28 (S-09).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).
- Kelas harness: f (binary buffer) untuk seluruh asersi isi berkas.

## Test Steps

### TC-AC-PF-351 Isi berkas CSV

1. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
2. Verifikasi baris header sama dengan kolom yang tampil tanpa kolom Actions.
3. Verifikasi jumlah baris data adalah lima (`Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`).
4. Verifikasi berkas berencoding UTF-8 dengan BOM.
5. Verifikasi berkas berpemisah koma.
6. Verifikasi badge ditulis sebagai teks labelnya.

### TC-AC-PF-352 Isi berkas XLSX

7. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas XLSX.
8. Verifikasi berkas memuat satu sheet bernama `Sheet1`.
9. Verifikasi header dan baris data sama dengan tabel.

### TC-AC-PF-635 Version bilangan bulat dan sel angka

10. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
11. Verifikasi tidak ada toast sukses.
12. Verifikasi CSV memuat baris berurutan `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
13. Verifikasi kolom Version bernilai `2`, `5`, `3`, `1`, `1` (tanpa awalan `v`).
14. Verifikasi kolom Clients bernilai `12`, `47`, `23`, `8`, `5`.
15. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas XLSX.
16. Verifikasi tidak ada toast sukses.
17. Verifikasi sel kolom Version dan Clients bertipe angka (number), bukan teks.

### TC-AC-PF-642 Format tanggal General Settings pada berkas

18. Ubah General Settings Date Format menjadi `dd/MM/yy` (Time Format 24-hour, Time Zone UTC) lewat fixture BE, lalu muat ulang halaman.
19. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
20. Verifikasi kolom Last Modified pada CSV bernilai `15/06/26, 10:00` untuk `Starter`, `Growth`, `Professional`, `09/07/26, 11:00` untuk `SIEM`, dan `12/08/26, 09:00` untuk `Enterprise`.
21. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas XLSX.
22. Verifikasi kolom Last Modified pada XLSX bernilai `15/06/26, 10:00` untuk `Starter`, `Growth`, `Professional`, `09/07/26, 11:00` untuk `SIEM`, dan `12/08/26, 09:00` untuk `Enterprise`.
23. Verifikasi nilai Last Modified di berkas sama dengan nilai di tabel layar (bukan format tetap `dd MMM yy`).

### TC-AC-PF-766 Time Format 12-hour

24. Pulihkan Date Format `dd MMM yy` dan ubah Time Format menjadi 12-hour (Time Zone UTC) lewat fixture BE, lalu muat ulang halaman.
25. Verifikasi kolom Last Modified di layar: `Starter` `15 Jun 26, 10:00 AM`, `SIEM` `09 Jul 26, 11:00 AM`, `Enterprise` `12 Aug 26, 09:00 AM`.
26. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
27. Verifikasi kolom Last Modified pada CSV bernilai sama dengan tabel di layar (jam 12-hour dengan penanda AM).
28. Pulihkan General Settings ke baseline (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) lewat fixture BE.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 18, 24, dan 28 mengubah serta memulihkan General Settings lewat fixture BE; mengubah General Settings lewat UI bukan objek uji spec ini.
- Verifikasi "tidak ada toast sukses" (langkah 11 dan 16) ditempatkan segera setelah pemicu download dan sebelum asersi berkas (bagian 8b butir 11).
- Langkah 23 membandingkan berkas dengan tabel layar sesuai Expected TC-AC-PF-642 butir b.
- Temuan untuk QA: TC-AC-PF-351 butir b (UTF-8 BOM dan pemisah koma) dan butir a (jumlah baris) tidak menyebut isi sel; spec hanya mengasersi hal yang disebut TC.
- Jumlah langkah 28: di bawah ambang sekitar 35.
