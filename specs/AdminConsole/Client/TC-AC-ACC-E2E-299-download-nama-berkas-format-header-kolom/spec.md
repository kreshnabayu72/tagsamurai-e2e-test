---
id: TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom
title: "Download Client List: Nama Berkas CSV dan XLSX, Tanpa Toast Sukses, serta Header Kolom Mengikuti Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-409
  - TC-AC-ACC-698
  - TC-AC-ACC-414
  - TC-AC-ACC-700
  - TC-AC-ACC-701
coverage:
  web: automated
---

# Download Client List: Nama Berkas CSV dan XLSX, Tanpa Toast Sukses, serta Header Kolom Mengikuti Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Kemampuan teknis: mengamati berkas yang terunduh di browser (nama berkas) dan membaca isinya (CSV/XLSX) di sisi test runner; disediakan tim FE. Tidak butuh intercept atau jam server.
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Spec ini hanya mengasersi nama berkas dan nama kolom (header); isi sel berkas ada di spec 300 (kelas f).

## Test Steps

### Download CSV dan XLSX sub-tab Active (TC-AC-ACC-409 dan TC-AC-ACC-698)

1. Klik ikon Download
2. Verifikasi overlay format memuat opsi `Download as CSV` dan `Download as XLSX`
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Clients.csv` terunduh
6. Klik ikon Download, lalu klik `Download as XLSX`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Clients.xlsx` terunduh

### Download sub-tab Archived (TC-AC-ACC-414)

9. Klik sub-tab Archived
10. Klik ikon Download, lalu klik `Download as CSV`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Clients.csv` terunduh (nama sama dengan sub-tab lain)
13. Klik sub-tab Active

### Header kolom mengikuti Column Visibility (TC-AC-ACC-700 dan TC-AC-ACC-701)

14. Klik header kolom Actions `(⋯)` lalu hapus centang PIC Name dan Client Code
15. Klik ikon Download, lalu klik `Download as CSV`
16. Buka berkas `Clients.csv` dan baca baris header
17. Verifikasi baris header memuat Company Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, dan Last Updated
18. Verifikasi baris header tidak memuat PIC Name dan Client Code
19. Klik header kolom Actions `(⋯)` lalu centang kembali PIC Name dan Client Code (pemulihan kolom)
20. Klik header kolom Actions `(⋯)`, hapus centang PIC Name, lalu centang kembali PIC Name
21. Klik ikon Download, lalu klik `Download as CSV`
22. Buka berkas `Clients.csv` dan baca baris header
23. Verifikasi baris header memuat PIC Name bersama Company Name, Client Code, Managed By, Group, FAMS, SAMS, SIEM, Modified By, dan Last Updated

## Notes

- Urutan `Verifikasi` untuk TC-AC-ACC-409/698/414 mengikuti bagian 8b butir 11: absence toast ditulis segera setelah pemicu (klik pilihan format) dan sebelum asersi artefak; pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh.
- Langkah penghubung (S-03): kembali ke sub-tab Active, pemulihan kolom PIC Name dan Client Code sebelum TC-AC-ACC-701.
- Temuan untuk QA
  - TC-AC-ACC-414: Expected menulis `Clients.csv/Clients.xlsx`; Langkah hanya mengunduh CSV, sehingga nama `Clients.xlsx` untuk sub-tab Archived tidak diasersi.
  - TC-AC-ACC-701: Expected daftar header 10 kolom mensyaratkan kolom Client Code tercentang; Langkah TC tidak memulihkan kolom dari TC-AC-ACC-700 sebelumnya sehingga spec menambah langkah pemulihan.
