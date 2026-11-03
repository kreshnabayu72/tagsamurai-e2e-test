---
id: TC-AC-PF-E2E-191-download-modal-changelog-custom-dan-global-settings-nama
title: Download modal Changelog Custom dan Global Settings nama berkas dan jumlah baris
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-499
  - TC-AC-PF-517
coverage:
  web: automated
---

# Download modal Changelog Custom dan Global Settings nama berkas dan jumlah baris

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log C, Changelog Custom Principal enam entri (Push Update `Region Jawa Client`; Edit `Growth Tier` API call quota; Edit `Growth Tier` Custom Report Builder; Create `Growth Tier`; Delete `Pilot Reseller`; Archive `Enterprise Reseller`; tanggal 10 Jun 26 sampai 29 Jun 26). Dataset Log G, Changelog Global Settings lima entri Edit (30 Jun 26 11:21, 30 Jun 26 11:20, 22 Jun 26 09:05, 15 Jun 26 14:40, 02 Jun 26 10:00). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log C dan Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before`, dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pembaca berkas CSV yang terunduh (nama berkas, header, jumlah baris); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Modal Changelog Custom (TC-AC-PF-499)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Klik ikon Download
4. Pilih `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Changelog-Plans-Features-Custom.csv` terunduh
7. Buka berkas CSV
8. Verifikasi berkas memuat enam baris data
9. Tutup modal dengan icon (X)

### Modal Changelog Global Settings (TC-AC-PF-517)

10. Klik tab Global Settings
11. Klik ikon Changelog di pojok kanan atas Card
12. Klik ikon Download
13. Pilih `Download as CSV`
14. Verifikasi tidak ada toast sukses
15. Verifikasi berkas `Changelog-Plans-Features-Global-Settings.csv` terunduh
16. Buka berkas CSV
17. Verifikasi berkas memuat lima baris data
18. Verifikasi berkas tidak memuat kolom Plan Name

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) pada langkah 9.
- Verifikasi "tidak ada toast sukses" pada langkah 5 dan 14 diletakkan segera setelah pemicu Download dan sebelum Verifikasi berkas (bagian 8b butir 11). Verifikasi langkah 18 didahului langkah 17 sebagai anchor positif bahwa berkas berisi data.
- Temuan untuk QA:
  - TC-AC-PF-517 menyebut berkas "tanpa kolom Plan Name" tanpa menyebut header lain; spec hanya mengasersi ketiadaan kolom Plan Name sesuai TC.
  - TC menetapkan jumlah entri Changelog sebagai seluruh isi log. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
