---
id: TC-FA-FAAM-E2E-191-total-assets-kolom-transactional-policy-dan-last-scanned
title: "Tab Total Assets: Kolom Transactional Policy dan Last Scanned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-763
  - TC-FA-FAAM-767
coverage:
  web: automated
---

# Tab Total Assets: Kolom Transactional Policy dan Last Scanned

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Policy transaksi `Column Matrix Item`: Borrow On, Assign On, Self Service Borrow Off, Transfer Off (Pre-setup #33c); `Policy Off Item` (Total Asset 1, aset `AST-2101`, seluruh policy Off; Pre-setup #33f).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- Format tanggal Last Scanned mengikuti General Settings; waktu pemindaian terbaru dari Audit (`task_item.scanned_at`) di-seed sebagai Pre-setup #33b.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-767: Kolom Last Scanned (curated): default tersembunyi, format tanggal General Settings, strip bila belum dipindai

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Amati header kolom tabel
3. Verifikasi pada kondisi default kolom Last Scanned tidak tampil di tabel
4. Klik header Actions (⋯), pilih `Setup Column...`
5. Verifikasi di Popup Setup Column Last Scanned `☐ Curated` (unchecked, enabled)
6. Centang Last Scanned, klik `[Save]`
7. Verifikasi `AST-2001` menampilkan 10 Oct 2026 09:00 dalam format General Settings
8. Verifikasi `AST-2003` menampilkan 05 Oct 2026 14:30 dalam format General Settings
9. Verifikasi `AST-2005` menampilkan 12 Sep 2026 08:15 dalam format General Settings
10. Verifikasi `AST-2002`, `AST-2004`, `AST-2006` (belum pernah dipindai) menampilkan `—`

### TC-FA-FAAM-763: Kolom Transactional Policy (curated): default tersembunyi, ikon transaksi On, kosong bila semua Off

11. Amati header kolom tabel sebelum Transactional Policy dicentang
12. Verifikasi pada kondisi default kolom Transactional Policy tidak tampil di tabel
13. Klik header Actions (⋯), pilih `Setup Column...`
14. Verifikasi di Popup Setup Column Transactional Policy `☐ Curated` (unchecked, enabled)
15. Centang Transactional Policy, klik `[Save]`
16. Verifikasi setiap baris `Column Matrix Item` menampilkan dua ikon berurutan Borrow lalu Assign
17. Verifikasi Self Service Borrow dan Transfer tidak tampil karena Off
18. Hover masing-masing ikon pada satu baris
19. Verifikasi hover ikon menampilkan nama transaksi `Borrow` dan `Assign`
20. Verifikasi keenam baris menampilkan ikon yang sama karena policy dimiliki Asset Name
21. Tutup popup Detail, klik nama `Policy Off Item`, klik tab `Total Assets (1)`
22. Klik header Actions (⋯), pilih `Setup Column...`, pastikan Transactional Policy tercentang, klik `[Save]`
23. Verifikasi baris `Policy Off Item` (seluruh policy Off) menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TC-FA-FAAM-763, Dependensi NC-25): bentuk ikon tidak diasersi; hanya jumlah ikon, urutan Borrow lalu Assign, dan label aksesibilitas (nama transaksi pada hover).
- Urutan TC: 767 lalu 763 (763 menyentuh dua fixture dan dikerjakan terakhir).
- Langkah penghubung: mengamati header kolom, menutup popup Detail, serta centang kolom Transactional Policy pada `Policy Off Item` sebagai precondition TC.
- Temuan untuk QA:
  - TC-FA-FAAM-763 LK langkah 8 ("tampilkan kolom Transactional Policy") berlaku pada fixture berbeda; spec mengikuti dengan Setup Column pada `Policy Off Item`.
  - TC-FA-FAAM-767: waktu Last Scanned tampil dalam format General Settings; contoh `10 Oct 2026 09:00` mengikuti format General Settings pengujian.
