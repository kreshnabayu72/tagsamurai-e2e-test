---
id: TC-FA-FAAM-E2E-198-total-assets-formula-dan-filter-range-nilai-full-value
title: "Tab Total Assets: Custom Field Formula dan Filter Range Asset Value-Warranty (Full Value Access)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-773
  - TC-FA-FAAM-777
  - TC-FA-FAAM-814
coverage:
  web: automated
---

# Tab Total Assets: Custom Field Formula dan Filter Range Asset Value-Warranty (Full Value Access)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field `Qty Count` (Numeric; `AST-2001` 4711) dan `Calc Field` (Formula `Qty Count` dikali 2; `AST-2001` 9422; Pre-setup #33g).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-773: Filter Asset Value (Commercial) range Min–Max tidak mencocokkan nilai kosong

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik Filter, amati field Asset Value
3. Verifikasi field `Asset Value` bertipe range dengan placeholder `Min` dan `Max`
4. Isi Min `1000000` dan Max `16000000`, klik `[Apply]`
5. Verifikasi hanya `AST-2001` dan `AST-2004` tampil
6. Verifikasi `AST-2002` (0) tidak tampil
7. Verifikasi baris `—` tidak tampil
8. Klik Filter, klik `[Clear Field]` pada field itu, isi Min `10000000` saja, klik `[Apply]`
9. Verifikasi Min 10000000 saja: hanya `AST-2001` dan `AST-2005` tampil

### TC-FA-FAAM-777: Filter Warranty Expiry date range tidak mencocokkan nilai kosong

10. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter Asset Value)
11. Klik Filter, amati field Warranty Expiry
12. Verifikasi field `Warranty Expiry` bertipe date range picker dengan placeholder `Select date`
13. Pilih rentang 01 Jan 2026 sampai 31 Dec 2027, klik `[Apply]`
14. Verifikasi hanya `AST-2003` dan `AST-2001` tampil
15. Verifikasi `AST-2004` dan `AST-2005` tidak tampil
16. Verifikasi baris `—` tidak tampil

### TC-FA-FAAM-814: Custom field Formula: tanpa Search, Sort, dan Filter

17. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter Warranty Expiry)
18. Klik header Actions (⋯), pilih `Setup Column...`, centang `Calc Field`, klik `[Save]`
19. Amati sel `AST-2001` dan header kolom
20. Verifikasi `AST-2001` menampilkan 9422 (dihitung saat dibaca)
21. Verifikasi header `Calc Field` tidak memiliki ikon Sort
22. Klik header `Calc Field`
23. Verifikasi klik header tidak mengubah urutan baris
24. Ketik Search `9422`, tekan Enter
25. Verifikasi empty state: Title `No results found` dan Description `Try adjusting your search or filter.`
26. Klik `(←)` pada kotak Search, klik Filter, amati daftar field
27. Verifikasi Filter Panel tidak memuat field `Calc Field`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: `[Clear Field]` dan `[Apply]` untuk menghapus filter antar blok (S-09), `(←)` pada Search, dan mengamati sel serta header.
- Asersi absence ikon Sort dan field Filter didahului anchor positif: sel `AST-2001` 9422 dan Filter Panel terbuka tampil.
- Temuan untuk QA:
  - TC-FA-FAAM-814: "Header tidak memiliki ikon Sort dan klik header tidak mengubah urutan baris" adalah dua klausa dan diasersi terpisah.
