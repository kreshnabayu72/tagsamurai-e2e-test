---
id: TC-FA-FAAM-E2E-196-total-assets-custom-field-dropdown-dan-date
title: "Tab Total Assets Custom Field: Dropdown, Multi-Dropdown, Date, dan DateTime"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-810
  - TC-FA-FAAM-811
coverage:
  web: automated
---

# Tab Total Assets Custom Field: Dropdown, Multi-Dropdown, Date, dan DateTime

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field Active tambahan (General, Scope `Column Matrix Item`; Pre-setup #33g): `Pick Status` (Dropdown; opsi `Opt-Alpha`, `Opt-Beta`; `AST-2001` `Opt-Alpha`, `AST-2002` `Opt-Beta`, `AST-2004` `Opt-Alpha`), `Pick Tags` (Multi-Dropdown; opsi `Tag-X`, `Tag-Y`, `Tag-Z`; `AST-2001` `Tag-X`+`Tag-Y`, `AST-2002` `Tag-Z`, `AST-2004` `Tag-Y`), `Due Date` (Date; `AST-2001` 15 Nov 2026, `AST-2002` 20 Dec 2026, `AST-2004` 22 Nov 2026), `Check Time` (DateTime; `AST-2001` 10 Nov 2026 09:00, `AST-2002` 12 Dec 2026 10:00, `AST-2004` 18 Nov 2026 14:00).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-810: Dropdown dan Multi-Dropdown: Search, Filter multi-select (OR), dan Sort

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang `Pick Status` dan `Pick Tags`, klik `[Save]`
3. Ketik Search `opt-alpha`, tekan Enter
4. Verifikasi Search `opt-alpha` menampilkan `AST-2001` dan `AST-2004`
5. Ganti isi kotak search dengan `tag-y`, tekan Enter
6. Verifikasi Search `tag-y` menampilkan `AST-2001` dan `AST-2004`
7. Klik `(←)` pada kotak Search, klik Filter, amati field `Pick Status` dan `Pick Tags`
8. Verifikasi Filter Panel memuat field `Pick Status` dan `Pick Tags` bertipe multi-select searchable dengan opsi nilai field
9. Pilih `Pick Status` `Opt-Beta`, klik `[Apply]`
10. Verifikasi `Pick Status` `Opt-Beta`: hanya `AST-2002` tampil
11. Klik Filter, klik `[Clear Field]` pada kedua field, pilih `Pick Tags` `Tag-X` dan `Tag-Z`, klik `[Apply]`
12. Verifikasi `Pick Tags` `Tag-X` dan `Tag-Z`: `AST-2001` dan `AST-2002` tampil (OR)
13. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
14. Klik header `Pick Status` 1 kali
15. Verifikasi klik 1 (A–Z): `Opt-Alpha` (`AST-2001`, `AST-2004`), `Opt-Beta` (`AST-2002`), lalu baris `—` di akhir
16. Klik header `Pick Status` 1 kali lagi
17. Verifikasi klik 2 (Z–A): baris `—` di awal, lalu `Opt-Beta`, `Opt-Alpha`
18. Klik header `Pick Status` 1 kali lagi
19. Verifikasi klik 3: kembali ke default Last Updated Newest First
20. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Pick Status` dan `Pick Tags`, klik `[Save]`

### TC-FA-FAAM-811: Date dan DateTime: tidak Searchable, Filter date range picker, dan Sort tanggal

21. Klik header Actions (⋯), pilih `Setup Column...`, centang `Due Date` dan `Check Time`, klik `[Save]`
22. Ketik Search teks tanggal `Due Date` `AST-2001` sebagaimana tampil, tekan Enter
23. Verifikasi empty state: Title `No results found` dan Description `Try adjusting your search or filter.`
24. Ganti isi kotak search dengan teks `Check Time` `AST-2001` sebagaimana tampil, tekan Enter
25. Verifikasi empty state: Title `No results found` dan Description `Try adjusting your search or filter.`
26. Klik `(←)` pada kotak Search, klik Filter, amati field `Due Date` dan `Check Time`
27. Verifikasi Filter Panel memuat field `Due Date` dan `Check Time` bertipe date range picker dengan placeholder `Select date`
28. Isi `Due Date` rentang 01 Nov 2026 sampai 30 Nov 2026, klik `[Apply]`
29. Verifikasi `Due Date` 01 Nov 2026 sampai 30 Nov 2026: `AST-2001` dan `AST-2004` tampil
30. Klik Filter, klik `[Clear Field]`, isi `Check Time` rentang 01 Nov 2026 sampai 30 Nov 2026, klik `[Apply]`
31. Verifikasi `Check Time` 01 Nov 2026 sampai 30 Nov 2026: `AST-2001` dan `AST-2004` tampil
32. Klik Filter, klik `[Clear Field]`, klik `[Apply]` (menghapus filter)
33. Klik header `Due Date` 1 kali
34. Verifikasi sort `Due Date` klik 1 (`Oldest First`): `AST-2001`, `AST-2004`, `AST-2002`, lalu baris `—` di akhir

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: `(←)` pada Search, `[Clear Field]` dan `[Apply]` untuk menghapus filter antar bagian (S-09), serta menghapus centang kolom di akhir blok TC-FA-FAAM-810 agar blok TC-FA-FAAM-811 memulai dari konfigurasi default.
- Empty state `No results found` dipakai sebagai anchor positif atas Search tanpa hasil; baris data ditampilkan sebelumnya pada tabel yang sama.
- Spec ini berisi sekitar 33 langkah; seluruh TC satu kelas harness (fungsional Search, Filter, Sort kolom custom field) dan satu dataset.
- Temuan untuk QA:
  - TC-FA-FAAM-811 Expected e hanya menyebut Sort klik 1; klik 2 dan 3 tidak diasersi. Teks tanggal Search dibaca dari sel sesuai format General Settings.
  - TC-FA-FAAM-810: LK langkah 8 menghapus filter sebelum Sort; spec menuliskannya sebagai langkah penghubung.
