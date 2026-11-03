---
id: TC-FA-FAAM-E2E-211-total-assets-sort-kolom-seragam-measurement-category-dan-policy
title: "Tab Total Assets Sort: Kolom Bernilai Seragam (Measurement, Category, Transactional Policy)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-765
coverage:
  web: automated
---

# Tab Total Assets Sort: Kolom Bernilai Seragam (Measurement, Category, Transactional Policy)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Policy transaksi `Column Matrix Item`: Borrow On, Self Service Borrow Off, Assign On, Transfer Off (Pre-setup #33c); kunci sort Transactional Policy `Assign, Borrow` sama pada seluruh baris.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- Kolom yang diuji (langkah 3 sampai 11):

| Kolom |
|---|
| Measurement |
| Category |
| Transactional Policy |

- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-765: Sort kelas kolom bernilai seragam

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Measurement, Category, Transactional Policy, klik `[Save]`

Untuk setiap baris tabel "Kolom yang diuji" pada Prerequisites (langkah 3 sampai 11):

3. Klik header kolom 1 kali
4. Verifikasi klik 1: indikator ascending aktif tanpa error
5. Verifikasi klik 1: keenam baris tetap tampil
6. Klik header kolom 1 kali lagi
7. Verifikasi klik 2: indikator descending aktif tanpa error
8. Verifikasi klik 2: keenam baris tetap tampil
9. Klik header kolom 1 kali lagi
10. Verifikasi klik 3: indikator netral
11. Verifikasi klik 3: urutan kembali ke default Last Updated Newest First

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 3 sampai 11 diulang untuk tiga kolom (ekspansi 27 langkah, total ekspansi 29 langkah); parameter tiap iterasi ada di tabel "Kolom yang diuji" (bagian 8b butir 7). Untuk Transactional Policy, ascending lalu descending bersifat alfabetis atas label ikon.
- NC-25: urutan diasersi lewat indikator dan jumlah baris; bentuk ikon Transactional Policy tidak diasersi.
- Pembagian TC lintas spec: TC-FA-FAAM-768, 772, dan 776 ada di spec 178.
- Temuan untuk QA:
  - TC-FA-FAAM-765: kolom bernilai seragam tidak memiliki dua nilai distinct (S-11/S-14), sehingga urutan baris tidak diasersi; TC sendiri menyatakannya.
