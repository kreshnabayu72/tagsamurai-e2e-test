---
id: TC-FA-FAAM-E2E-190-total-assets-kolom-measurement-dan-category
title: "Tab Total Assets: Kolom Measurement (Symbol) dan Kolom Category Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-757
  - TC-FA-FAAM-760
coverage:
  web: automated
---

# Tab Total Assets: Kolom Measurement (Symbol) dan Kolom Category Curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Category aset `Laptop` (anak `Electronics`).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-757: Kolom Measurement (curated): default tersembunyi, ceklis, sel berisi Symbol UoM saja

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Amati header kolom tabel
3. Verifikasi pada kondisi default kolom Measurement tidak tampil di tabel
4. Klik header Actions (⋯), pilih `Setup Column...`
5. Verifikasi di Popup Setup Column Measurement `☐ Curated` (unchecked, enabled)
6. Centang Measurement
7. Verifikasi kolom Measurement tampil di Live Preview
8. Klik `[Save]`
9. Verifikasi kolom Measurement tampil di tabel
10. Verifikasi keenam baris menampilkan `kg` (Symbol UoM saja)
11. Verifikasi Unit Name `Kilogram` tidak tampil
12. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
13. Verifikasi pilihan tersimpan dan tetap setelah popup dibuka kembali (kolom Measurement tetap tampil)

### TC-FA-FAAM-760: Kolom Category (curated): default tersembunyi, badge Primary, hover hierarki

14. Amati header kolom tabel sebelum Category dicentang
15. Verifikasi pada kondisi default kolom Category tidak tampil di tabel
16. Klik header Actions (⋯), pilih `Setup Column...`
17. Verifikasi di Popup Setup Column Category `☐ Curated` (unchecked, enabled)
18. Centang Category, klik `[Save]`
19. Verifikasi keenam baris menampilkan badge Primary `Laptop` yang sama (Category `Column Matrix Item`)
20. Hover badge Category pada salah satu baris
21. Verifikasi hover menampilkan hierarki lengkap `Electronics > Laptop`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 757 lalu 760; TC-FA-FAAM-760 mengasersi "kondisi default" Category (butir a) pada awal blok, sebelum Category dicentang, sementara kolom Measurement dari blok TC-FA-FAAM-757 masih tersimpan.
- Langkah penghubung: mengamati header kolom tabel (langkah amati tanpa `Verifikasi`) dan menutup popup Detail untuk membuka kembali tab.
- Temuan untuk QA:
  - TC-FA-FAAM-760 butir a: "kondisi default" Category diamati sesudah Measurement tersimpan pada TC sebelumnya di spec ini; Category tetap tersembunyi karena preferensi disimpan per kolom.
