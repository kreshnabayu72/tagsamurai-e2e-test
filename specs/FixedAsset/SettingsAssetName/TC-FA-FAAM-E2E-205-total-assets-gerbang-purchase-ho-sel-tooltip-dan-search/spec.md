---
id: TC-FA-FAAM-E2E-205-total-assets-gerbang-purchase-ho-sel-tooltip-dan-search
title: "Tab Total Assets Gerbang Akses: Aktor Purchase HO (Sel, Tooltip, dan Search)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-786
  - TC-FA-FAAM-789
  - TC-FA-FAAM-792
coverage:
  web: automated
---

# Tab Total Assets Gerbang Akses: Aktor Purchase HO (Sel, Tooltip, dan Search)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Purchase HO (Pre-setup #32c) `managePurchaseHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PHO_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Purchase HO memegang `Manage purchase` pada `Head Office` beserta `Finance` (tidak pada `Warehouse`); tanpa View asset value dan tanpa Manage accounting. Custom field Purchasing `Purchase Price`: `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200 (Pre-setup #33e).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-786: Gerbang akses sel: aktor Manage purchase pada Head Office (Warranty dan Purchasing berhak per group, Asset Value No access)

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati kolom yang tersedia
3. Verifikasi Setup Column memuat `Asset Value`, `Warranty Expiry`, dan `Purchase Price`
4. Verifikasi Setup Column tidak memuat `Accounting Code`
5. Centang Asset Value, Warranty Expiry, dan Purchase Price (kolom `Accounting Code` tidak tersedia pada daftar), klik `[Save]`
6. Verifikasi Asset Value: keenam baris `No access` (aktor tidak memegang View asset value maupun Manage accounting)
7. Verifikasi Warranty Expiry: `AST-2001` 31 Mar 2027, `AST-2002` `—`, `AST-2003` 15 Jan 2026 (Finance termasuk descendant Head Office)
8. Verifikasi Warranty Expiry: `AST-2004`, `AST-2005`, `AST-2006` `No access`
9. Verifikasi Purchase Price: `AST-2001` 2500, `AST-2002` `—`, `AST-2003` `0`
10. Verifikasi Purchase Price: `AST-2004`, `AST-2005`, `AST-2006` `No access`
11. Verifikasi sel kolom Name, Asset ID, Brand, Group, Status tetap tampil normal pada keenam baris

### TC-FA-FAAM-789: Tooltip sel No access: Asset Value menunjuk View asset value, Warranty dan Purchasing menunjuk Manage purchase

12. Hover sel Asset Value baris `AST-2004`
13. Verifikasi tooltip Asset Value `No access`: `Requires View asset value access in this group.`
14. Hover sel Warranty Expiry baris `AST-2004`
15. Verifikasi tooltip Warranty Expiry `No access`: `Requires Manage purchase access in this group.`
16. Hover sel Purchase Price baris `AST-2004`
17. Verifikasi tooltip Purchase Price `No access`: `Requires Manage purchase access in this group.`

### TC-FA-FAAM-792: Search tidak mencocokkan nilai maupun teks No access

18. Ketik Search `1800`, tekan Enter
19. Verifikasi empty state: Title `No results found` dan Description `Try adjusting your search or filter.` (nilai `AST-2004` tidak terkirim karena sel `No access`)
20. Ganti isi kotak search dengan `2500`, tekan Enter
21. Verifikasi keyword `2500` menampilkan hanya `AST-2001`
22. Ganti isi kotak search dengan `No access`, tekan Enter
23. Verifikasi empty state: Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-FA-FAAM-789 dan 792 memakai konfigurasi kolom yang disimpan blok TC-FA-FAAM-786 (Asset Value, Warranty Expiry, dan Purchase Price tercentang); LK TC-789 mencentang Asset Value, Warranty Expiry, Purchase Price dan LK TC-792 mencentang Purchase Price, sehingga langkah mencentang tidak diulang agar tidak membatalkan centang yang tersimpan. Aksi mencentang tersebut sudah dilakukan pada blok TC-FA-FAAM-786.
- Langkah penghubung: mengamati kolom Setup Column sebelum mencentang.
- Asersi hover diasersi segera sesudah pemicu hover (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAM-786 LK langkah 4 bersyarat ("bila tersedia"); spec menulis centang hanya pada kolom yang terbukti tersedia lewat Expected a.
  - TC-FA-FAAM-792: Expected c (`No access`) tidak menyebut apakah keyword dicocokkan pada teks sel; spec mengasersi tabel kosong sesuai Expected.
