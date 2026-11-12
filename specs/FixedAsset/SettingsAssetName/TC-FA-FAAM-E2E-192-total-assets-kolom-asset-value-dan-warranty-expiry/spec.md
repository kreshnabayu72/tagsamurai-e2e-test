---
id: TC-FA-FAAM-E2E-192-total-assets-kolom-asset-value-dan-warranty-expiry
title: "Tab Total Assets: Kolom Asset Value Commercial dan Warranty Expiry Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-771
  - TC-FA-FAAM-775
coverage:
  web: automated
---

# Tab Total Assets: Kolom Asset Value Commercial dan Warranty Expiry Curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value (Purchase Cost belum ada; sel `Pending`), Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value (Purchase Cost belum ada; sel `Pending`), tanpa Warranty, belum dipindai. Client utama memakai dua buku tetap `Commercial` dan `Fiscal` (Pre-setup #33h): nilai Asset Value pada Pre-setup #33b adalah nilai `Asset Value (Commercial)`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Format tanggal dan currency mengikuti General Settings dan `prd-conventions.md` §32.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-771: Kolom Asset Value (Commercial): default tersembunyi, nilai, nol, dan Pending bagi pemanggil berhak

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Amati header kolom tabel
3. Verifikasi pada kondisi default kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` tidak tampil di tabel
4. Klik header Actions (⋯), pilih `Setup Column...`
5. Verifikasi di Popup Setup Column `Asset Value (Commercial)` dan `Asset Value (Fiscal)` `☐ Curated` (unchecked, enabled)
6. Centang `Asset Value (Commercial)`, klik `[Save]`
7. Verifikasi `AST-2001` (15000000), `AST-2004` (5000000), `AST-2005` (20000000) tampil sebagai currency 2 desimal rata kanan
8. Verifikasi `AST-2002` (nilai nol) menampilkan currency nol sesuai `prd-conventions.md` §32 (mis. `Rp 0,00`), bukan `—`
9. Verifikasi `AST-2003` dan `AST-2006` (tanpa harga perolehan) menampilkan `Pending`, bukan `—`
10. Verifikasi tidak ada sel `No access` karena aktor berhak atas seluruh baris
11. Hover sel `Pending` `AST-2003`
12. Verifikasi tooltip `Purchase cost has not been set.`

### TC-FA-FAAM-775: Kolom Warranty Expiry (curated): default tersembunyi, tanggal General Settings, strip bila belum ada

11. Amati header kolom tabel sebelum Warranty Expiry dicentang
12. Verifikasi pada kondisi default kolom Warranty Expiry tidak tampil di tabel
13. Klik header Actions (⋯), pilih `Setup Column...`
14. Verifikasi di Popup Setup Column Warranty Expiry `☐ Curated` (unchecked, enabled)
15. Centang Warranty Expiry, klik `[Save]`
16. Verifikasi `AST-2001` 31 Mar 2027, `AST-2003` 15 Jan 2026, `AST-2004` 30 Jun 2028, `AST-2005` 01 Feb 2025, seluruhnya dalam format General Settings
17. Verifikasi `AST-2002` dan `AST-2006` (belum ada tanggal garansi) menampilkan `—`
18. Verifikasi tidak ada sel `No access` karena aktor berhak atas seluruh baris

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: mengamati header kolom tabel (tanpa `Verifikasi`) sebelum kolom dicentang.
- Kolom Asset Value pada TC-FA-FAAM-750 sampai 822 berarti `Asset Value (Commercial)` (Pre-setup #33h).
- Temuan untuk QA:
  - TC-FA-FAAM-771 Expected c menyebut "currency 2 desimal rata kanan" tanpa contoh teks; teks nilai dibaca dari sel dan format mengikuti `prd-conventions.md` §32.
