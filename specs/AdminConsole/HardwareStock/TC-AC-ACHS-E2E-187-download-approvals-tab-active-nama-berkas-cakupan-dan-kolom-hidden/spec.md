---
id: TC-AC-ACHS-E2E-187-download-approvals-tab-active-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Approvals Tab Active Nama Berkas Cakupan dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-410
  - TC-AC-ACHS-411
  - TC-AC-ACHS-412
  - TC-AC-ACHS-415
coverage:
  web: automated
---

# Download Approvals Tab Active Nama Berkas Cakupan dan Kolom Hidden

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C (`Fixture.hardwareStock.p21.c[n]`). Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari fixture lewat kunci pada tabel Parameter Pre-setup (R-06).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #21 Tabel C | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
  | Keyword Search nama Client | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[5].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; nama yang sama muncul pada Existing Record #1 dan #11, sehingga Search menghasilkan tepat tiga baris #1, #5, #11 (semua Activation Collision) | `Fixture.hardwareStock.derived.clientCoreNameActive` |
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan di browser (nama berkas) dan membaca isi berkas CSV dan XLSX (header, jumlah baris, urutan baris, BOM UTF-8, nama sheet).
- State global browser: spec ini menyembunyikan lalu menampilkan kembali kolom Category (konfigurasi kolom Tab Active disimpan di browser); hook `after` suite menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Search `Fixture.hardwareStock.derived.clientCoreNameActive` menghasilkan 3 baris (Pre-setup #21, lihat spec Search): #1, #5, #11.

## Test Steps

### Nama berkas, tooltip, overlay, dan kolom berkas (TC-AC-ACHS-410)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Hover icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Hardware-Stock.csv` terunduh
10. Klik icon Download, pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Hardware-Stock.xlsx` terunduh
13. Buka berkas CSV
14. Verifikasi kolom berkas CSV: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At (sesuai tab aktif)
15. Verifikasi CSV UTF-8 dengan BOM
16. Verifikasi urutan baris CSV mengikuti sort default (FIFO): #1, #2, #3, #4, #5, dan seterusnya
17. Buka berkas XLSX
18. Verifikasi kolom berkas XLSX: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At
19. Verifikasi XLSX satu sheet bernama `Sheet1`
20. Verifikasi urutan baris XLSX mengikuti sort default (FIFO): #1, #2, #3, #4, #5, dan seterusnya

### Cakupan mengikuti Search dan seluruh halaman (TC-AC-ACHS-411)

21. Pastikan tidak ada Search atau Filter aktif dan rows per page 10 (default)
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi berkas CSV berisi seluruh 12 baris (bukan hanya 10 baris halaman pertama)
24. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
25. Klik icon Download, pilih `Download as CSV`
26. Verifikasi berkas CSV hanya berisi 3 baris hasil search
27. Klik icon `(←)` pada kotak Search

### Kolom hidden tidak ikut (TC-AC-ACHS-412)

28. Klik header kolom Actions `(⋯)`, uncheck `Category`
29. Klik icon Download, pilih `Download as CSV`
30. Buka berkas CSV
31. Verifikasi berkas CSV memuat kolom Type, Device Name (SKU), dan Requested At
32. Verifikasi berkas CSV tidak memuat kolom Category
33. Klik header kolom Actions `(⋯)`, check `Category`
34. Klik icon Download, pilih `Download as CSV`
35. Buka berkas CSV
36. Verifikasi berkas CSV memuat kolom Category

### Hasil Search kosong (TC-AC-ACHS-415)

37. Ketik Search `zzqx-tidak-ada`, tekan Enter
38. Verifikasi tombol Download tetap aktif
39. Klik icon Download, pilih `Download as CSV`
40. Verifikasi tidak ada toast
41. Verifikasi berkas CSV berisi baris header kolom visible saja
42. Verifikasi berkas CSV tidak berisi baris data
43. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-410, 411, 412, 415). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 2 (klik Tab `Active`); langkah 21 (memastikan tidak ada Search atau Filter aktif); langkah 27 dan 43 (klik `(←)` mereset Search); langkah 33 (check `Category` kembali, memulihkan Column Visibility); langkah 13, 17, 30, 35 (membuka berkas lewat kemampuan baca berkas).
- Asersi nama berkas, nama kolom, jumlah baris, dan urutan baris adalah asersi fungsional (bagian 3 prinsip 13 butir f, `[KEPUTUSAN 2026-10-30]`). Langkah 15 (BOM UTF-8) dan 19 (nama sheet `Sheet1`) berasal dari TC-410 butir f dan g; keduanya isi biner (kelas f) tetapi TC-410 tetap di spec ini karena satu TC satu spec (lihat Temuan untuk QA). Spec kelas f terpisah untuk permukaan ini adalah spec 188.
- Asersi absence toast (langkah 8, 11, 40) diletakkan segera setelah pemicu sebelum asersi artefak (bagian 8b butir 11); pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh. Absence kolom Category (langkah 32) memakai anchor positif langkah 31.
- Spec melewati sekitar 35 langkah (43 langkah): alasan, semua blok satu surface (Download Approvals Tab Active) dan satu dataset read-only; tiap blok mengembalikan Search dan Column Visibility sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Konfirmasi (#8): `Fixture.hardwareStock.derived.clientCoreNameActive` sama dengan substring yang ditulis TC-411 (nama inti Client, bukan nilai kolom penuh); hasil pada Tabel C: tiga baris #1, #5, #11. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-410 butir f dan g (BOM UTF-8, `Sheet1`) dan butir h (urutan baris) adalah isi berkas; menurut prinsip 13 butir f isi berkas dipisah. TC-410 satu TC, spec memuatnya utuh di sini dan TC-414 di spec 188; usulan QA memecah TC-410 menjadi dua TC.
  - TC-410 Expected h menulis "urutan baris mengikuti sort default" tanpa daftar baris; spec mengasersi lima baris pertama dan lanjutannya mengikuti urutan FIFO.
  - TC-411 langkah 3 mengasumsikan ukuran halaman default 10 (Expected a: "bukan hanya 10 baris halaman pertama"); spec memakai 10.
