---
id: TC-FA-FAAM-E2E-170-total-assets-search-measurement-dan-tag
title: "Tab Total Assets Search: Kelas Measurement dan Kelas TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-758
  - TC-FA-FAAM-801
coverage:
  web: automated
---

# Tab Total Assets Search: Kelas Measurement dan Kelas TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Column Matrix Item` (Total Asset 6, `AST-2001` sampai `AST-2006`, UoM `Kilogram` Symbol `kg`, tag aktif: `AST-2001` `QR` (Tag Code `TGC-2001`) dan `RFID`, `AST-2002` `QR`, `AST-2003` tanpa tag aktif, `AST-2004` `RFID`, `AST-2005` `NFC` dan `QR`, `AST-2006` `NFC`; Pre-setup #33, #33b, #33d).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kebutuhan NC-25: spec tidak mengasersi bentuk ikon tipe tag; hanya hasil pencarian per baris (jumlah dan urutan baris), sesuai keputusan menunggu konfirmasi NC-25.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-758: Search kelas Measurement (Symbol) dan terikat visibilitas kolom

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Measurement, klik `[Save]`
3. Ketik Search `kg`, tekan Enter
4. Verifikasi keyword `kg` menampilkan keenam baris (cocok pada Symbol yang tampil)
5. Ganti isi kotak search dengan `Kilogram`, tekan Enter
6. Verifikasi keyword `Kilogram` tidak menemukan baris karena hanya Symbol yang tampil
7. Klik `(←)` pada kotak Search
8. Verifikasi keenam baris aset tampil
9. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Measurement, klik `[Save]` (sembunyikan kolom Measurement)
10. Ketik Search `kg`, tekan Enter
11. Verifikasi saat Measurement di-hide keyword `kg` tidak menemukan baris

### TC-FA-FAAM-801: Search kelas TAG (label aksesibilitas ikon, Tag Code tidak dicari, terikat visibilitas kolom)

12. Klik `(←)` pada kotak Search
13. Verifikasi keenam baris aset tampil
14. Ketik Search `rfid`, tekan Enter
15. Verifikasi keyword `rfid` menampilkan `AST-2001` dan `AST-2004`
16. Ganti isi kotak search dengan `qr`, tekan Enter
17. Verifikasi keyword `qr` menampilkan `AST-2001`, `AST-2002`, dan `AST-2005`
18. Ganti isi kotak search dengan `nfc`, tekan Enter
19. Verifikasi keyword `nfc` menampilkan `AST-2005` dan `AST-2006`
20. Ganti isi kotak search dengan `barcode`, tekan Enter
21. Verifikasi Title `No results found`
22. Verifikasi Description `Try adjusting your search or filter.`
23. Ganti isi kotak search dengan `TGC-2001`, tekan Enter
24. Verifikasi keyword `TGC-2001` (Tag Code) tidak menemukan baris karena Tag Code tidak ditampilkan
25. Klik `(←)` pada kotak Search
26. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang TAG, klik `[Save]` (sembunyikan kolom TAG)
27. Ketik Search `rfid`, tekan Enter
28. Verifikasi saat TAG di-hide keyword `rfid` tidak menemukan baris
29. Klik `(←)` pada kotak Search
30. Klik header Actions (⋯), pilih `Setup Column...`, centang kembali TAG, klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- NC-25 (TC-FA-FAAM-801, Dependensi NC-25): ikon final tipe tag belum dikonfirmasi; asersi hanya pada baris hasil pencarian atas label aksesibilitas tipe tag, bukan bentuk ikon.
- Langkah penghubung: `(←)` pada Search antar bagian, menyembunyikan lalu memulihkan kolom, dan memulihkan centang TAG di akhir blok TC-FA-FAAM-801.
- Asersi absence (tidak ada baris) didahului anchor positif: keenam baris aset tampil atau hasil pencarian sebelumnya pada surface yang sama.
- Temuan untuk QA:
  - TC-FA-FAAM-801 butir d dan e: `barcode` dan `TGC-2001` Expected tidak seragam; butir e tidak menyebut copy empty state, sehingga tidak diasersi.
