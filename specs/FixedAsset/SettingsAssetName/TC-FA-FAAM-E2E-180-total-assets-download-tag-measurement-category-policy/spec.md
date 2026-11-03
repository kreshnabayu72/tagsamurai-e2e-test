---
id: TC-FA-FAAM-E2E-180-total-assets-download-tag-measurement-category-policy
title: "Tab Total Assets Download: Kolom TAG, Measurement, Category, Transactional Policy, dan Last Scanned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-756
  - TC-FA-FAAM-766
  - TC-FA-FAAM-770
coverage:
  web: automated
---

# Tab Total Assets Download: Kolom TAG, Measurement, Category, Transactional Policy, dan Last Scanned

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. `Policy Off Item` (Total Asset 1, aset `AST-2101`, Borrow, Self Service Borrow, Assign, Transfer seluruhnya Off; Pre-setup #33f); Policy `Column Matrix Item`: Borrow On, Assign On.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- Kelas harness: binary buffer (isi berkas CSV, bagian 3 prinsip 13f).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-756: Export kolom TAG berisi label tipe tag dipisah koma

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik Download lalu `Download as CSV`
3. Verifikasi berkas CSV terunduh
4. Verifikasi kolom TAG ada pada berkas karena kolom visible default
5. Verifikasi `AST-2001` berisi `QR, RFID` (label tipe, bukan nama komponen icon dan bukan Tag Code)
6. Verifikasi `AST-2002` berisi `QR`
7. Verifikasi `AST-2003` (tanpa tag aktif) ditulis hyphen tunggal `-`

### TC-FA-FAAM-770: Export kolom Last Scanned mengikuti General Settings, kosong ditulis strip

8. Klik header Actions (⋯), pilih `Setup Column...`, centang Last Scanned, klik `[Save]`
9. Klik Download lalu `Download as CSV`
10. Verifikasi berkas CSV terunduh
11. Verifikasi `AST-2001` berisi tanggal 10 Oct 2026 09:00 dalam format General Settings
12. Verifikasi `AST-2002` (belum pernah dipindai) ditulis hyphen tunggal `-`

### TC-FA-FAAM-766: Export kolom Measurement, Category, Transactional Policy

13. Klik header Actions (⋯), pilih `Setup Column...`, centang Measurement, Category, Transactional Policy, klik `[Save]`
14. Klik Download lalu `Download as CSV`
15. Verifikasi berkas CSV pertama terunduh
16. Verifikasi berkas pertama: Measurement berisi `kg` (Symbol)
17. Verifikasi berkas pertama: Category berisi hierarki penuh dari root `Electronics > Laptop`
18. Verifikasi berkas pertama: Transactional Policy berisi `Borrow, Assign` (label transaksi On dipisah `, `)
19. Tutup popup Detail, klik nama `Policy Off Item`, klik tab `Total Assets (1)`
20. Klik header Actions (⋯), pilih `Setup Column...`, pastikan Transactional Policy tercentang, klik `[Save]`
21. Klik Download lalu `Download as CSV`
22. Verifikasi berkas CSV kedua terunduh
23. Verifikasi berkas kedua: Transactional Policy `Policy Off Item` (seluruh policy Off) ditulis hyphen tunggal `-`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 756 (kolom default), 770, lalu 766 (menyentuh dua fixture, dikerjakan terakhir).
- NC-25: isi kolom TAG dan Transactional Policy diasersi lewat teks berkas CSV; bentuk ikon tidak diasersi.
- Langkah penghubung: centang kolom lewat Setup Column sebagai precondition dan menutup popup Detail sebelum berpindah fixture.
- Temuan untuk QA:
  - TC-FA-FAAM-766: precondition berkas kedua ("tampilkan kolom Transactional Policy") menggunakan Setup Column pada fixture berbeda; nilai aset `Policy Off Item` yang diasersi hanya baris `AST-2101`.
