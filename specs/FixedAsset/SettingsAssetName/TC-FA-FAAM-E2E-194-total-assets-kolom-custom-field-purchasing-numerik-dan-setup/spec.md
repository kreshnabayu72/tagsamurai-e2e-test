---
id: TC-FA-FAAM-E2E-194-total-assets-kolom-custom-field-purchasing-numerik-dan-setup
title: "Tab Total Assets: Kolom Custom Field Purchasing Numerik dan Setup Column Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-782
  - TC-FA-FAAM-783
coverage:
  web: automated
---

# Tab Total Assets: Kolom Custom Field Purchasing Numerik dan Setup Column Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Code `CMX`, Category `Laptop` anak `Electronics`, Brand `Dell` model `5420`, UoM `Kilogram` Symbol `kg`, Total Asset 6; Pre-setup #33, #33b, #33c, #33d, #33e). Enam aset berstatus `Active`, Last Updated menurun dari `AST-2001` (20 Oct 2026 10:00) sampai `AST-2006` (15 Oct 2026): `AST-2001` Group `Head Office`, tag aktif `QR` (Tag Code `TGC-2001`) dan `RFID`, Asset Value (Commercial) 15000000, Warranty Expiry 31 Mar 2027, Last Scanned 10 Oct 2026 09:00; `AST-2002` `Head Office`, tag `QR`, Asset Value 0, tanpa Warranty, belum dipindai; `AST-2003` `Finance` (anak `Head Office`), tanpa tag aktif, tanpa Asset Value, Warranty 15 Jan 2026, Last Scanned 05 Oct 2026 14:30; `AST-2004` `Warehouse`, tag `RFID`, Asset Value 5000000, Warranty 30 Jun 2028, belum dipindai; `AST-2005` `Warehouse`, tag `NFC` dan `QR`, Asset Value 20000000, Warranty 01 Feb 2025, Last Scanned 12 Sep 2026 08:15; `AST-2006` `Warehouse`, tag `NFC`, tanpa Asset Value, tanpa Warranty, belum dipindai. Custom field (Pre-setup #33e): `Serial Notes` (Text, General; `SN-1` `AST-2001`, `SN-3` `AST-2003`, `SN-4` `AST-2004`), `Purchase Price` (Number, Purchasing, Scope `Column Matrix Item`; `AST-2001` 2500, `AST-2003` 0, `AST-2004` 1800, `AST-2005` 3200).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kemampuan teknis: pembacaan berkas CSV yang terunduh (nama berkas, header, dan isi sel) disediakan tim FE.
- Kelas harness: fungsional; TC-FA-FAAM-782 memuat asersi isi berkas CSV dalam TC yang sama (bagian 3 prinsip 13f).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-782: Kolom custom field Purchasing numerik (`Purchase Price`): nilai, nol, Sort, Search, Export

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang `Purchase Price`, klik `[Save]`
3. Verifikasi `AST-2001` 2500, `AST-2004` 1800, `AST-2005` 3200 tampil sebagai angka
4. Verifikasi `AST-2003` (nilai nol) menampilkan `0`, bukan `—`
5. Verifikasi `AST-2002` dan `AST-2006` (nilai belum diisi) menampilkan `—`
6. Klik header `Purchase Price` 1 kali
7. Verifikasi klik 1 (ascending numerik): `AST-2003` (0), `AST-2004`, `AST-2001`, `AST-2005`, lalu baris `—` di akhir
8. Klik header `Purchase Price` 1 kali lagi
9. Verifikasi klik 2 (descending): baris `—` di awal, lalu `AST-2005`, `AST-2001`, `AST-2004`, `AST-2003`
10. Klik header `Purchase Price` 1 kali lagi
11. Verifikasi klik 3: kembali ke default Last Updated Newest First
12. Ketik Search `1800`, tekan Enter
13. Verifikasi Search `1800` menampilkan hanya `AST-2004`
14. Klik `(←)` pada kotak Search
15. Klik Download lalu `Download as CSV`
16. Verifikasi berkas CSV terunduh
17. Verifikasi `AST-2003` pada berkas berisi nilai nol
18. Verifikasi sel tanpa nilai pada berkas ditulis hyphen tunggal `-`
19. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Purchase Price`, klik `[Save]`

### TC-FA-FAAM-783: Setup Column kelas custom field (curated): ceklis, geser urutan, pin

20. Klik header Actions (⋯), pilih `Setup Column...`, centang `Serial Notes` dan `Purchase Price`
21. Geser (drag) `Serial Notes` ke posisi lain
22. Klik icon Pin pada `Purchase Price`
23. Verifikasi perubahan ceklis dan urutan tampil di Live Preview dan tabel
24. Klik `[Save]`
25. Scroll tabel horizontal
26. Verifikasi kolom yang di-pin membeku (sticky) saat scroll horizontal
27. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
28. Verifikasi perubahan tersimpan dan tetap setelah popup dibuka kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: `(←)` pada Search, menutup popup Detail, serta menghapus centang `Purchase Price` di akhir blok TC-FA-FAAM-782 agar blok TC-FA-FAAM-783 memulai dari konfigurasi default (S-09).
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" tidak diasersi.
- Temuan untuk QA:
  - TC-FA-FAAM-782 dan TC-FA-FAAM-783 mencentang `Purchase Price` pada LK masing-masing; spec TC-783 bergantung pada konfigurasi yang tersimpan dari TC-782 (bukan dari preferensi default).
  - TC-FA-FAAM-782 memuat asersi nilai sel berkas CSV (kelas f) di TC fungsional; spec mengikuti TC.
