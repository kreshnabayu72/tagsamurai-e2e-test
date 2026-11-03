---
id: TC-FA-FAAM-E2E-189-total-assets-kolom-urutan-setup-column-dan-tag
title: "Tab Total Assets: Urutan Kolom Setup Column Sesuai Tabel dan Kolom TAG Tanpa Tag Code"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-750
  - TC-FA-FAAM-751
coverage:
  web: automated
---

# Tab Total Assets: Urutan Kolom Setup Column Sesuai Tabel dan Kolom TAG Tanpa Tag Code

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field Active (Pre-setup #33e): `Serial Notes` dan `Out Of Scope Field` (General), `Out Of Scope Purchase` dan `Purchase Price` (Purchasing), `Accounting Code` (Accounting).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-750: Urutan kolom di Setup Column mengikuti tabel Setup Column Popup Detail

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`
3. Verifikasi urutan baris kolom di Setup Column: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Measurement`, `Category`, `Group`, `Label`, `Status`, `Transactional Policy`, `Last Scanned`, `Asset Value`, `Warranty Expiry`, kolom custom field, `Last Updated`
4. Verifikasi kolom custom field berurutan per grup: General (`Out Of Scope Field` sebelum `Serial Notes`), Purchasing (`Out Of Scope Purchase` sebelum `Purchase Price`), lalu Accounting (`Accounting Code`)
5. Verifikasi checkbox `☑ Hideable` pada `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
6. Verifikasi checkbox `☐ Curated` pada `Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value`, `Warranty Expiry`, dan setiap kolom custom field
7. Verifikasi `Last Updated` menjadi kolom data terakhir sebelum Actions (⋯)
8. Tekan Esc untuk menutup popup Setup Column
9. Verifikasi header tabel hanya memuat 8 kolom default: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
10. Tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-751: Kolom TAG menampilkan ikon tipe tag aktif tanpa Tag Code

11. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`)
12. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
13. Verifikasi kolom TAG tampil secara default setelah kolom Asset ID
14. Verifikasi `AST-2001` menampilkan dua ikon (tipe `QR` dan `RFID`) tampil penuh tanpa `+N more`
15. Verifikasi `AST-2002` menampilkan satu ikon tipe `QR`
16. Verifikasi `AST-2003` (tanpa tag aktif) menampilkan `—`
17. Verifikasi Tag Code `TGC-2001` tidak tampil di sel
18. Hover ikon tag pada baris `AST-2001`
19. Verifikasi hover ikon menampilkan label tipe (`QR`, `RFID`)
20. Verifikasi Tag Code `TGC-2001` tidak tampil di hover

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TC-FA-FAAM-751): bentuk ikon tipe tag tidak diasersi; hanya jumlah ikon, nilai `—`, dan label tipe pada hover.
- Urutan TC: 750 (Full Value Access, Pre-setup #32e), lalu ganti akun ke Total Control untuk 751 (S-07: ganti akun punya langkah eksplisit).
- Langkah penghubung: menutup popup Setup Column dengan Esc (diikuti `Verifikasi` header tabel sesuai Expected f), menutup popup Detail, dan Logout sebelum ganti akun.
- Temuan untuk QA:
  - TC-FA-FAAM-750 Expected a menulis kolom custom field sebagai satu entri, sedangkan custom field aktif adalah lima kolom (Expected b merincinya); spec mengasersi keduanya.
