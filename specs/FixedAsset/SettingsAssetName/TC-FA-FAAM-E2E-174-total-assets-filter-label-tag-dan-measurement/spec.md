---
id: TC-FA-FAAM-E2E-174-total-assets-filter-label-tag-dan-measurement
title: "Tab Total Assets Filter: Label OR, TAG, dan Measurement"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-712
  - TC-FA-FAAM-753
  - TC-FA-FAAM-759
coverage:
  web: automated
---

# Tab Total Assets Filter: Label OR, TAG, dan Measurement

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26). Setiap aset berlabel `Finance` dan `High Priority` (Default Label), aset `Dell Latitude - 42` diberi tambahan label `Fragile`.
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Dependensi NC-25 (ikon final Borrow, Self Service Borrow, Assign, Transfer) belum dikonfirmasi: spec tidak mengasersi bentuk ikon, hanya jumlah, urutan, dan label aksesibilitas.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-712: Filter Label multi-select berlaku OR

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC: kolom curated Label sudah ditampilkan; dipakai sebagai precondition, tidak diasersi)
3. Klik Filter, amati field Label
4. Verifikasi placeholder field `All labels`
5. Buka dropdown Label
6. Verifikasi opsi berbadge warna label sama dengan label distinct pada data tabel (`Finance`, `Fragile`, `High Priority`)
7. Pilih `Fragile`, klik `[Apply]`
8. Verifikasi label `Fragile` menampilkan 1 aset (`Dell Latitude - 42`)
9. Klik Filter, tambahkan `Finance` (sehingga `Fragile` dan `Finance`), klik `[Apply]`
10. Verifikasi `Fragile` dan `Finance` menampilkan seluruh 42 aset (OR di dalam field)

### TC-FA-FAAM-753: Filter TAG multi-select dengan opsi tipe tag distinct dari data tabel

11. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
12. Klik Filter, amati field TAG
13. Verifikasi field `TAG` bertipe multi-select searchable dengan placeholder `All tags`
14. Buka dropdown TAG
15. Verifikasi opsi hanya tipe tag yang muncul pada data tabel: `NFC`, `QR`, `RFID`
16. Verifikasi `BARCODE` tidak muncul karena tidak dipakai aset mana pun
17. Pilih `RFID`, klik `[Apply]`
18. Verifikasi hanya `AST-2001` dan `AST-2004` tampil
19. Klik Filter, tambahkan `NFC`, klik `[Apply]`
20. Verifikasi `AST-2001`, `AST-2004`, `AST-2005`, dan `AST-2006` tampil (OR di dalam field)

### TC-FA-FAAM-759: Filter Measurement multi-select dengan opsi Symbol distinct dari data tabel

21. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (membersihkan filter TAG)
22. Klik Filter, amati field Measurement
23. Verifikasi field `Measurement` bertipe multi-select searchable dengan placeholder `All units`
24. Buka dropdown Measurement
25. Verifikasi opsi hanya `kg` (Symbol distinct dari data tabel)
26. Verifikasi `Kilogram` tidak menjadi opsi
27. Pilih `kg`, klik `[Apply]`
28. Verifikasi keenam baris tetap tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 712 (`Dell Latitude`), 753 dan 759 (`Column Matrix Item`).
- NC-25 (TC-FA-FAAM-753 tidak berdependensi, tetapi opsi filter TAG berupa tipe tag): spec tidak mengasersi bentuk ikon.
- Langkah penghubung: centang Label (precondition), `[Clear Field]` dan `[Apply]` untuk membersihkan filter TAG sebelum TC berikutnya (S-09), dan menutup popup Detail sebelum berpindah fixture.
- Temuan untuk QA:
  - TC-FA-FAAM-712 memerlukan kolom Label tampil (precondition) tanpa langkah memunculkannya di LK; spec menambah langkah centang Label.
  - TC-FA-FAAM-759 Expected c ("keenam baris tetap tampil") tidak membedakan hasil filter dari keadaan tanpa filter; spec mengasersinya apa adanya.
