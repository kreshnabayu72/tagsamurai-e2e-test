---
id: TC-FA-FAAM-E2E-204-total-assets-gerbang-asset-value-ho-filter-dan-lintas-group
title: "Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Filter dan Baris Lintas Group)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-795
  - TC-FA-FAAM-791
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Filter dan Baris Lintas Group)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Asset Value HO (Pre-setup #32) `assetValueHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AVHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Asset Value HO memegang `View asset value` pada `Head Office` beserta `Finance`; Purchase HO memegang `Manage purchase` pada `Head Office` beserta `Finance`. Group baris: `AST-2001` sampai `AST-2003` di `Head Office`/`Finance`, `AST-2004` sampai `AST-2006` di `Warehouse`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-795: Baris lintas group tetap client-wide: sel lain tampil dan hanya sel bergerbang menjadi No access

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value dan Warranty Expiry, klik `[Save]`
3. Verifikasi label tab `Total Assets (6)` dan keenam baris tampil termasuk tiga baris Group `Warehouse` di luar hak aktor
4. Verifikasi baris `AST-2004`, `AST-2005`, `AST-2006` menampilkan Name, Asset ID, Brand, Model/Type, Group `Warehouse`, dan Status secara normal
5. Verifikasi pada ketiga baris itu hanya sel Asset Value dan Warranty Expiry yang `No access`
6. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Asset Value dan Warranty Expiry, klik `[Save]`

### TC-FA-FAAM-791: Filter kolom bergerbang tidak mencocokkan baris No access

7. Klik Filter, isi Asset Value Min `0` dan Max `99999999`, klik `[Apply]`
8. Verifikasi aktor `Asset Value HO`: hanya `AST-2001` dan `AST-2002` tampil
9. Verifikasi `AST-2004` dan `AST-2005` (nilai 5000000 dan 20000000 di Warehouse, `No access`) tidak tampil
10. Verifikasi `AST-2003` dan `AST-2006` tidak tampil
11. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter), tutup popup Detail, klik tombol akun, pilih Logout
12. Login sebagai Purchase HO (`managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_PHO_PASSWORD`)
13. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
14. Klik Filter, pilih Warranty Expiry 01 Jan 2020 sampai 31 Dec 2030, klik `[Apply]`
15. Verifikasi aktor `Purchase HO`: hanya `AST-2001` dan `AST-2003` tampil
16. Verifikasi `AST-2004` (30 Jun 2028) dan `AST-2005` (01 Feb 2025) tidak tampil walau tanggalnya berada dalam rentang, karena sel keduanya `No access`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix per blok role (bagian 3a): TC-FA-FAAM-791 memakai dua aktor (Asset Value HO lalu Purchase HO) dengan Step ganti akun eksplisit; akun pertama login di hook `before`. Aktor kedua (Purchase HO, Pre-setup #32c) tertulis di ACC TC-FA-FAAM-791.
- Urutan TC: 795 sebelum 791 (795 mengasersi tabel tanpa filter; 791 menyimpan filter dan ganti akun).
- Langkah penghubung: menghapus centang kolom, `[Clear Field]` dan `[Apply]` untuk menghapus filter, menutup popup Detail, dan Logout sebelum ganti akun.
- Asersi absence baris (TC-FA-FAAM-791) didahului anchor positif: baris hasil Filter yang tampil pada tabel yang sama.
