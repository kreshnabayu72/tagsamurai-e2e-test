---
id: TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column
title: Download modal Changelog Default nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-486
  - TC-AC-PF-489
  - TC-AC-PF-490
  - TC-AC-PF-491
coverage:
  web: automated
---

# Download modal Changelog Default nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pembaca berkas CSV yang terunduh (nama berkas, baris header, jumlah dan isi baris); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: blok TC-AC-PF-490 menyembunyikan kolom `Old Value` lewat Overlay Column Visibility dan menampilkannya kembali di akhir blok; hook `after` menghapus preferensi kolom modal Changelog Default di browser (kemampuan disediakan tim FE).

## Test Steps

### Nama berkas dan overlay Download (TC-AC-PF-486)

1. Klik ikon Changelog pada toolbar tab Default
2. Hover ikon Download
3. Verifikasi tooltip `Download`
4. Klik ikon Download
5. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Changelog-Plans-Features-Default.csv` terunduh
9. Klik ikon Download
10. Pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Changelog-Plans-Features-Default.xlsx` terunduh

### Download mengikuti Search (TC-AC-PF-489)

13. Ketik Search `growth`, tekan Enter
14. Klik ikon Download
15. Pilih `Download as CSV`
16. Buka berkas CSV
17. Verifikasi berkas hanya memuat baris `Archive Growth Plus (old)` dan `Edit Growth` hasil Search

### Download mengikuti Column Visibility (TC-AC-PF-490)

18. Klik `(←)` pada kotak Search
19. Sembunyikan kolom `Old Value` lewat Overlay Column Visibility
20. Klik ikon Download
21. Pilih `Download as CSV`
22. Verifikasi tidak ada toast atau dialog peringatan
23. Buka berkas CSV
24. Verifikasi header berkas memuat kolom lain yang tampil (`Date`, `Action`, `Plan Name`, `Field`, `New Value`, `Modified By`)
25. Verifikasi header berkas tidak memuat kolom `Old Value`
26. Tampilkan kembali kolom `Old Value` lewat Overlay Column Visibility

### Download dengan hasil kosong (TC-AC-PF-491)

27. Ketik Search `zzzzz`, tekan Enter
28. Verifikasi tombol Download tetap aktif
29. Klik ikon Download
30. Pilih `Download as CSV`
31. Verifikasi tidak ada toast sukses
32. Buka berkas CSV
33. Verifikasi berkas hanya berisi baris header kolom yang tampil
34. Verifikasi berkas tidak memuat baris data

## Notes

- Langkah penghubung (S-03): langkah 18 menutup input Search dan mereset tabel; langkah 26 memulihkan visibilitas kolom.
- Verifikasi "tidak ada toast sukses" atau "tidak ada toast atau dialog peringatan" diletakkan segera setelah pemicu Download dan sebelum Verifikasi berkas (bagian 8b butir 11); pemicu Download menjadi anchor positif yang buktinya menyusul pada Verifikasi berkas.
- Verifikasi langkah 24 (kolom lain tampil) mendahului langkah 25 sebagai anchor absence; Verifikasi langkah 33 (baris header ada) mendahului langkah 34.
- Isi sel berkas (nilai, BOM, tipe sel) diuji di spec 189 dan 190; spec ini hanya mengasersi nama berkas, header, dan jumlah serta identitas baris.
- Temuan untuk QA:
  - TC-AC-PF-491 menulis "tidak ada toast sukses" sebagai butir terpisah tanpa langkah observasi; spec mengamatinya setelah klik pilihan format.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
