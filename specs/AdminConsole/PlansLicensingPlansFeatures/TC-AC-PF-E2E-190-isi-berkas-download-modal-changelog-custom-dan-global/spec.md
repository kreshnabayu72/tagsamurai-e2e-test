---
id: TC-AC-PF-E2E-190-isi-berkas-download-modal-changelog-custom-dan-global
title: Isi berkas Download modal Changelog Custom dan Global Settings, nilai tersimpan, kolom, dan hasil Filter lintas halaman
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-652
  - TC-AC-PF-653
coverage:
  web: automated
---

# Isi berkas Download modal Changelog Custom dan Global Settings, nilai tersimpan, kolom, dan hasil Filter lintas halaman

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log CX, Changelog Custom Principal enam entri, terbaru dahulu: `20 Jul 26, 10:30` Push Update `PT Kuota Satu` (Plan Version, Old `v1`, New `v2`, Sarah T); `18 Jul 26, 09:00` Edit `Paket Kuota Push` (Scheduled reports, Old `—`, New `5`, John D); `17 Jul 26, 15:00` Edit `Paket Kuota Push` (API call quota, Old `100K/month`, New `150,000/month`, John D); `16 Jul 26, 11:00` Edit `Paket Kuota Push` (Scheduled reports, Old `5`, New `Unlimited`, John D); `15 Jul 26, 08:30` Create `Paket Kuota Push` (Plan Name, Old `—`, New `Paket Kuota Push`, Jane S); `14 Jul 26, 08:00` Delete `Paket Lama` (Plan Name, Old `Paket Lama`, New `—`, Jane S). Dataset Log GX, Changelog Global Settings 25 entri oleh John D: 15 entri Edit `Max custom fields per asset name` dari 1 ke 2 sampai 15 ke 16, dan 10 entri Edit `Max depreciation methods (Multi Depreciation tier)` dari 2 ke 3 sampai 11 ke 12. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log CX dan Changelog Global Settings Principal tepat sama dengan Dataset Log GX di hook `before`, dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pembaca buffer biner berkas CSV yang terunduh (header, jumlah baris, nilai sel); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Nilai tersimpan pada berkas modal Changelog Custom (TC-AC-PF-652)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Verifikasi di modal baris Scheduled reports pertama menampilkan Old Value `—` dan New Value `5`
4. Verifikasi di modal baris API call quota menampilkan Old Value `100K/month` dan New Value `150,000/month`
5. Klik ikon Download
6. Pilih `Download as CSV`
7. Buka berkas CSV
8. Verifikasi header CSV: `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`
9. Verifikasi berkas memuat enam baris data
10. Verifikasi baris Scheduled reports bernilai `-` dan `5`, serta `5` dan `Unlimited`
11. Verifikasi baris API call quota bernilai `100000` dan `150000` (bukan `100K/month` dan bukan `150,000/month`)
12. Verifikasi baris Push Update `PT Kuota Satu` bernilai `1` dan `2` tanpa awalan `v`
13. Verifikasi baris Create bernilai `-` dan `Paket Kuota Push`
14. Verifikasi baris Delete bernilai `Paket Lama` dan `-`
15. Tutup modal dengan icon (X)

### Berkas modal Changelog Global Settings dengan Filter aktif (TC-AC-PF-653)

16. Klik tab Global Settings
17. Klik ikon Changelog di pojok kanan atas Card
18. Klik ikon Filter, pilih Field `Max custom fields per asset name`, lalu klik `[Apply]`
19. Verifikasi footer tabel `Showing 1–10 of 15 entries`
20. Klik ikon Download
21. Pilih `Download as CSV`
22. Verifikasi tidak ada toast sukses
23. Buka berkas CSV
24. Verifikasi header CSV: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` (tanpa `Plan Name`)
25. Verifikasi berkas memuat 15 baris data (seluruh hasil Filter pada kedua halaman)
26. Verifikasi semua baris bernilai Action `Edit` dengan Field `Max custom fields per asset name`
27. Verifikasi Old Value `1` sampai `15` dan New Value `2` sampai `16` sebagai bilangan bulat
28. Verifikasi tidak ada baris Field `Max depreciation methods (Multi Depreciation tier)`

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) pada langkah 15.
- Verifikasi "tidak ada toast sukses" pada langkah 22 diletakkan segera setelah pemicu Download dan sebelum Verifikasi berkas (bagian 8b butir 11). Verifikasi langkah 28 didahului langkah 26 sebagai anchor positif bahwa baris Field lain ada.
- Pengecualian kelas f: isi berkas (nilai sel) diasersi di spec ini; nama berkas, header, dan jumlah baris juga diasersi di spec 188 dan 191.
- Temuan untuk QA:
  - TC-AC-PF-652 Expected c menyebut nilai berkas hanya sebagai pasangan nilai lama dan baru per Field tanpa tanggal; spec mengasersi tiap pasangan sebagai kehadiran baris karena urutan baris berkas tidak dinyatakan TC.
  - TC menetapkan jumlah entri Changelog sebagai seluruh isi log. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
