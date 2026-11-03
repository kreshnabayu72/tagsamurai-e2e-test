---
id: TC-FA-FAAM-E2E-193-total-assets-kolom-custom-field-daftar-scope-dan-purchasing
title: "Tab Total Assets: Kolom Custom Field (Daftar Aktif, Scope General, Di Luar Scope)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-779
  - TC-FA-FAAM-780
  - TC-FA-FAAM-781
coverage:
  web: automated
---

# Tab Total Assets: Kolom Custom Field (Daftar Aktif, Scope General, Di Luar Scope)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field (Pre-setup #33e): `Serial Notes` (Text, General, Scope `Column Matrix Item`; `SN-1` `AST-2001`, `SN-3` `AST-2003`, `SN-4` `AST-2004`), `Out Of Scope Field` (Text, General, Scope `Dell Latitude`), `Inactive Field` (Text, General, Scope `Column Matrix Item`, status Inactive).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.
- Kelas harness: fungsional; TC-FA-FAAM-780 dan 781 memuat asersi isi berkas CSV dalam TC yang sama (bagian 3 prinsip 13f membolehkan nama berkas, header, dan jumlah baris di spec fungsional; asersi nilai sel mengikuti TC sumber).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-779: Kolom custom field: himpunan field Active yang tersedia, default tersembunyi

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati baris custom field
3. Verifikasi daftar kolom custom field memuat seluruh custom field Active yang tersedia bagi aktor, termasuk `Out Of Scope Field` yang scope-nya bukan `Column Matrix Item` (bukan hanya field pada Tab Linked Custom Fields)
4. Verifikasi `Inactive Field` (status Inactive) tidak menjadi kolom
5. Verifikasi setiap kolom custom field `☐ Curated` (unchecked, enabled)
6. Verifikasi setiap kolom custom field tidak tampil pada tabel sebelum dicentang
7. Centang `Serial Notes` dan `Out Of Scope Field`, klik `[Save]`
8. Verifikasi kolom `Serial Notes` dan `Out Of Scope Field` tampil di Live Preview dan tabel, di antara `Warranty Expiry` dan `Last Updated`
9. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Serial Notes` dan `Out Of Scope Field`, klik `[Save]`

### TC-FA-FAAM-780: Kolom custom field General dalam Scope (`Serial Notes`): nilai, strip, Search, Sort, Export

10. Klik header Actions (⋯), pilih `Setup Column...`, centang `Serial Notes`, klik `[Save]`
11. Verifikasi nilai tampil sebagai teks: `AST-2001` `SN-1`, `AST-2003` `SN-3`, `AST-2004` `SN-4`
12. Verifikasi `AST-2002`, `AST-2005`, `AST-2006` (nilai belum diisi) menampilkan `—`
13. Ketik Search `SN-3`, tekan Enter
14. Verifikasi Search `SN-3` menampilkan hanya `AST-2003`
15. Klik `(←)` pada kotak Search
16. Klik header `Serial Notes` 1 kali
17. Verifikasi klik 1 (A–Z): `SN-1`, `SN-3`, `SN-4`, lalu baris `—` di akhir
18. Klik header `Serial Notes` 1 kali lagi
19. Verifikasi klik 2 (Z–A): baris `—` di awal, lalu `SN-4`, `SN-3`, `SN-1`
20. Klik header `Serial Notes` 1 kali lagi
21. Verifikasi klik 3: kembali ke default Last Updated Newest First
22. Klik Download lalu `Download as CSV`
23. Verifikasi berkas CSV terunduh
24. Verifikasi kolom `Serial Notes` pada berkas berisi nilai teks dan sel tanpa nilai ditulis hyphen tunggal `-`
25. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Serial Notes`, klik `[Save]`

### TC-FA-FAAM-781: Kolom custom field di luar Scope Asset Name berisi strip di semua baris

26. Klik header Actions (⋯), pilih `Setup Column...`, centang `Out Of Scope Field`, klik `[Save]`
27. Verifikasi keenam baris menampilkan `—` pada kolom `Out Of Scope Field` (field General dengan Scope `Dell Latitude` tidak berlaku bagi Asset Name `Column Matrix Item`)
28. Verifikasi tidak ada sel `No access` pada kolom itu
29. Klik Download lalu `Download as CSV`
30. Verifikasi berkas CSV terunduh
31. Verifikasi sel kolom `Out Of Scope Field` pada berkas ditulis hyphen tunggal `-` pada keenam baris

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 779, 780, 781; kolom custom field dikembalikan ke tersembunyi di akhir tiap blok (langkah penghubung) agar blok berikutnya memulai dari keadaan default.
- Langkah penghubung: `(←)` pada Search dan Setup Column untuk menghapus centang kolom.
- Temuan untuk QA:
  - TC-FA-FAAM-780 dan 781 memuat asersi nilai sel berkas CSV (kelas f) di TC fungsional; spec mengikuti TC dan tidak memindahkannya.
  - TC-FA-FAAM-780 LK langkah 6 ("Hapus keyword Search") ditulis sebagai klik `(←)` pada Search.
