---
id: TC-AC-PF-E2E-172-isi-berkas-download-tab-assigned-clients-bom-sheet-plan
title: "Isi berkas Download Tab Assigned Clients: BOM, sheet XLSX, dan format kolom Plan Version"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-445
  - TC-AC-PF-446
  - TC-AC-PF-639
coverage:
  web: automated
---

# Isi berkas Download Tab Assigned Clients: BOM, sheet XLSX, dan format kolom Plan Version

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten, penangkapan berkas unduhan browser, dan pembacaan isi berkas CSV (encoding, BOM, pemisah) serta XLSX (sheet, nilai sel). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Isi berkas CSV (TC-AC-PF-445)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Klik ikon Download → `Download as CSV`.
4. Buka berkas CSV.
5. Verifikasi baris header berkas sama dengan kolom yang tampil tanpa kolom Actions.
6. Verifikasi berkas memuat sembilan baris data, seluruh client termasuk yang di-mask.
7. Verifikasi berkas berencoding UTF-8 dengan BOM.
8. Verifikasi berkas berpemisah koma.
9. Verifikasi badge ditulis sebagai teks labelnya.

### Isi berkas XLSX (TC-AC-PF-446)

10. Klik ikon Download → `Download as XLSX`.
11. Buka berkas XLSX.
12. Verifikasi berkas memuat satu sheet bernama `Sheet1`.
13. Verifikasi header berkas sama dengan header tabel.
14. Verifikasi baris data berkas sama dengan baris data tabel.

### Format kolom Plan Version (TC-AC-PF-639)

15. Verifikasi kolom Plan Version di layar menampilkan `v5` untuk `PT Sejahtera Abadi`.
16. Verifikasi kolom Plan Version di layar menampilkan badge `Outdated` untuk `PT Wahana Nusantara`.
17. Klik ikon Download → `Download as CSV`.
18. Verifikasi tidak ada toast sukses.
19. Buka berkas CSV.
20. Verifikasi kolom Plan Version bernilai `5` untuk `PT Sejahtera Abadi` dan `PT Cahaya Mandiri` (client versi terbaru: bilangan bulat tanpa awalan `v`).
21. Verifikasi kolom Plan Version bernilai `1 (Outdated)` untuk `PT Wahana Nusantara` (client Outdated: versi lalu label badge dalam kurung).
22. Klik ikon Download → `Download as XLSX`.
23. Buka berkas XLSX dan periksa kolom Plan Version.
24. Verifikasi nilai kolom Plan Version pada XLSX sama dengan CSV (tipe sel kolom ini tidak dinilai).

## Notes

- Spec ini memuat kelas f (isi berkas) sebagai satu-satunya kelas harness; nama berkas, header, dan jumlah baris juga diasersi di sini karena melekat pada TC yang sama.
- Absence toast (langkah 18) diletakkan segera setelah pemicu unduhan dan sebelum pembacaan berkas (bagian 8b butir 11); pembacaan berkas pada langkah 19 menjadi bukti bahwa unduhan terjadi.
- Temuan untuk QA:
  - TC-AC-PF-445 Expected a menyebut "termasuk yang di-mask", tetapi Dataset Plan D tidak menandai client yang di-mask untuk aktor Total Control Principal; spec mengasersi sembilan baris data dan tidak memeriksa masking.
  - TC-AC-PF-639 menyebut Dataset Plan D hanya dengan empat client (`PT Sejahtera Abadi`, `PT Wahana Nusantara`, `PT Karya Abadi`, `PT Cahaya Mandiri`), sedangkan Dataset Plan D di TC lain memuat sembilan client; spec memakai Dataset Plan D penuh.
  - TC-AC-PF-639 langkah 2 ("amati kolom Plan Version") dan Expected d ("Tidak ada toast sukses") tidak menyatakan unduhan mana yang dimaksud; toast diasersi pada unduhan CSV.
