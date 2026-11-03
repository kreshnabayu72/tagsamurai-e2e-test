---
id: TC-AC-PF-E2E-144-isi-berkas-download-plans-list-tab-custom-bom-sheet-kutip
title: Isi Berkas Download Plans List Tab Custom BOM, Sheet, dan Kutip pada Plan Name
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-402
  - TC-AC-PF-403
  - TC-AC-PF-715
coverage:
  web: automated
---

# Isi Berkas Download Plans List Tab Custom BOM, Sheet, dan Kutip pada Plan Name

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max` (semuanya Paid) untuk langkah 1 sampai 10; Dataset Plan CS (Pre-setup #58): custom plan Principal `Kutip "Dua", Koma` (FAMS, Paid, v1, Clients 0) ditambahkan pada langkah 11 untuk langkah 12 sampai 14.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal dan menambahkan Dataset Plan CS (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before`, `after`, dan pada langkah 11. Kemampuan membaca isi berkas CSV (mentah sebagai teks) dan XLSX yang terunduh disediakan tim FE/BE. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup selain menambah Dataset Plan CS lewat fixture BE.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).
- Kelas harness: f (binary buffer).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-402 Isi berkas CSV

2. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
3. Verifikasi baris header sama dengan kolom yang tampil tanpa kolom Actions.
4. Verifikasi jumlah baris data adalah empat (`alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`).
5. Verifikasi berkas berencoding UTF-8 dengan BOM.
6. Verifikasi berkas berpemisah koma.
7. Verifikasi badge ditulis sebagai teks labelnya.

### TC-AC-PF-403 Isi berkas XLSX

8. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas XLSX.
9. Verifikasi berkas memuat satu sheet bernama `Sheet1`.
10. Verifikasi header dan baris data sama dengan tabel.

### TC-AC-PF-715 Kutip dan koma pada Plan Name

11. Tambahkan Dataset Plan CS lewat fixture BE, lalu muat ulang halaman tab Custom > Active.
12. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV sebagai teks mentah.
13. Verifikasi sel Plan Name ditulis `"Kutip ""Dua"", Koma"` (dibungkus kutip ganda, tiap kutip di dalamnya digandakan).
14. Verifikasi baris data memuat jumlah kolom yang sama dengan header (koma di dalam nama tidak memecah kolom).

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 11 menambah Dataset Plan CS lewat fixture BE dan membuka kembali tab Custom > Active.
- Dataset Plan CS menambah satu baris di tab Custom Active; karena itu blok TC-AC-PF-402 (empat baris data) dijalankan sebelum langkah 11.
- Jumlah langkah 14: di bawah ambang sekitar 35.
