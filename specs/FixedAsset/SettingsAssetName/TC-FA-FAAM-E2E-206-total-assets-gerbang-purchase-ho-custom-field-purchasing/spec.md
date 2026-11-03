---
id: TC-FA-FAAM-E2E-206-total-assets-gerbang-purchase-ho-custom-field-purchasing
title: "Tab Total Assets Gerbang Akses: Aktor Purchase HO (Custom Field Purchasing di Luar Scope dan Filter)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-803
  - TC-FA-FAAM-815
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Purchase HO (Custom Field Purchasing di Luar Scope dan Filter)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field Purchasing (Pre-setup #33e): `Out Of Scope Purchase` (Scope `Dell Latitude`) dan `Purchase Price` (Scope `Column Matrix Item`; `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200). Group baris: `AST-2001` sampai `AST-2003` di `Head Office`/`Finance`, `AST-2004` sampai `AST-2006` di `Warehouse`. Purchase HO memegang `Manage purchase` pada `Head Office` beserta `Finance`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-803: Kolom custom field Purchasing di luar Scope berisi strip di semua baris walau baris berada di luar hak

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat kolom `Out Of Scope Purchase` dan `Purchase Price` (aktor memegang Manage purchase di Head Office)
4. Centang `Out Of Scope Purchase` dan `Purchase Price`, klik `[Save]`
5. Verifikasi `Out Of Scope Purchase`: keenam baris `—`, termasuk `AST-2004`, `AST-2005`, `AST-2006` di Warehouse (field tidak berlaku bagi Asset Name sehingga `—` berlaku tanpa memandang hak)
6. Verifikasi `Purchase Price`: `AST-2004`, `AST-2005`, `AST-2006` `No access` (field berlaku dan aktor tidak berhak atas Warehouse)

### TC-FA-FAAM-815: Filter kolom custom field Purchasing tidak mencocokkan baris No access

7. Klik Filter, amati field `Purchase Price`
8. Verifikasi Filter Panel memuat field `Purchase Price` bertipe range dengan placeholder `Min` dan `Max`
9. Isi `Purchase Price` Min `0` Max `99999`, klik `[Apply]`
10. Verifikasi hanya `AST-2001` (2500) dan `AST-2003` (0) tampil
11. Verifikasi `AST-2004` (1800) dan `AST-2005` (3200) tidak tampil walau nilainya dalam rentang, karena sel keduanya `No access`
12. Verifikasi `AST-2002` dan `AST-2006` (`—`) tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: mengamati kolom Setup Column dan Filter Panel sebelum asersi.
- Asersi absence baris (TC-FA-FAAM-815) didahului anchor positif: `AST-2001` dan `AST-2003` tampil pada tabel hasil Filter yang sama.
- Temuan untuk QA:
  - TC-FA-FAAM-803 butir b menyatakan `—` tanpa memandang hak untuk field di luar scope, sedangkan Pre-setup #33e menyebut `Out Of Scope Purchase` Scope `Dell Latitude`.
