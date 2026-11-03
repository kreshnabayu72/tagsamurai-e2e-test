---
id: TC-AC-ACHS-E2E-127-download-stock-list-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Stock List: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-251
  - TC-AC-ACHS-252
  - TC-AC-ACHS-253
  - TC-AC-ACHS-256
coverage:
  web: automated
---

# Download Stock List: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Brand baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19); Brand yang sama pada baris 3 dan 4 | `Fixture.hardwareStock.p16.a[1].brand` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV dan XLSX yang terunduh (jumlah baris, header kolom, isi sel) dari lokasi unduhan unik per langkah unduh sehingga nama berkas yang sama tidak bertabrakan.
- State global yang diubah: visibilitas kolom Range Type (langkah 25 sampai 28) dipulihkan di langkah 28. Preferensi kolom di browser dihapus oleh hook suite `after`. Berkas terunduh disimpan di lokasi unduhan unik per langkah.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-251: CSV dan XLSX, nama berkas, tanpa toast sukses

1. Arahkan kursor ke icon Download
2. Verifikasi tooltip `Download`
3. Klik icon Download
4. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
5. Pilih `Download as CSV`
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas `Hardware-Stock.csv` terunduh
8. Klik icon Download, pilih `Download as XLSX`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Hardware-Stock.xlsx` terunduh
11. Buka berkas CSV
12. Verifikasi kolom berkas CSV: Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated (kolom Photo tidak ikut)
13. Verifikasi CSV berenkode UTF-8 dengan BOM
14. Verifikasi urutan baris CSV mengikuti sort default
15. Buka berkas XLSX
16. Verifikasi kolom berkas XLSX: Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated (kolom Photo tidak ikut)
17. Verifikasi XLSX berisi satu sheet bernama `Sheet1`
18. Verifikasi urutan baris XLSX mengikuti sort default

### TC-AC-ACHS-252: Cakupan mengikuti Search atau Filter aktif dan seluruh halaman

19. Klik icon Download, pilih `Download as CSV`
20. Verifikasi berkas CSV berisi seluruh 30 baris (bukan hanya 10 baris halaman pertama)
21. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi berkas CSV hanya berisi 3 baris hasil search
24. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-253: Kolom yang di-hide tidak ikut, ikut kembali setelah unhide

25. Klik header kolom Actions `(⋯)`, hilangkan centang `Range Type`, tutup overlay Column Visibility
26. Klik icon Download, pilih `Download as CSV`
27. Verifikasi berkas CSV tidak memuat kolom Range Type
28. Klik header kolom Actions `(⋯)`, ceklis kembali `Range Type`, tutup overlay Column Visibility
29. Klik icon Download, pilih `Download as CSV`
30. Verifikasi berkas CSV memuat kolom Range Type

### TC-AC-ACHS-256: Hasil filter kosong tetap aktif dan berisi header saja

31. Ketik Search `zzqx-tidak-ada`, tekan Enter
32. Verifikasi tombol Download tetap aktif
33. Klik icon Download, pilih `Download as CSV`
34. Verifikasi tidak ada toast
35. Verifikasi berkas CSV berisi baris header kolom visible saja tanpa baris data
36. Klik `✕` pada Search, tekan Enter


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword `Zebra` (`Fixture.hardwareStock.p16.a[1].brand`) adalah nilai kolom Brand penuh yang sama persis dengan keyword literal TC (TC-AC-ACHS-204, 211, 249, 250, 258 menurut spec ini). Dicocokkan dengan Tabel A Pre-setup #16: kolom Brand bernilai `Zebra` hanya pada baris 1, 3, dan 4, dan tidak ada kolom searchable lain di baris lain yang memuat `Zebra`, sehingga himpunan hasil 3 baris sama dengan hasil keyword TC. Tidak ada perbedaan.
- Asersi absence toast (langkah 6, 9, dan 35 sebelum `Verifikasi` berkas) diletakkan segera setelah pemicu unduh dan sebelum `Verifikasi` artefak (butir 8b nomor 11); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search, pembukaan berkas (membaca isi lewat kemampuan pembaca CSV dan XLSX), dan pemulihan visibilitas kolom Range Type (langkah 28).
- TC-AC-ACHS-251 memuat Expected tentang isi berkas (BOM, `Sheet1`, urutan baris) selain nama berkas dan kolom; seluruh Expected TC itu ditulis di spec ini agar TC tetap berada di satu spec (lihat Temuan untuk QA). Isi sel berkas (nilai, tipe sel, escaping) diasersi di spec kelas binary buffer (TC-AC-ACHS-255 dan 261).
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Download pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan tidak ada perulangan atau langkah bersyarat; sebagian besar langkah adalah Verifikasi per klausa Expected TC-AC-ACHS-251.
- Temuan untuk QA:
  - TC-AC-ACHS-251 Expected f, g, dan h (BOM, `Sheet1`, urutan baris berkas) termasuk isi berkas (kelas binary buffer, bagian 3 prinsip 13f) tetapi satu TC tetap berada di satu spec; QA diminta memisahkan TC itu di sumber (nama berkas dan kolom di satu TC, isi berkas di TC lain) atau menyetujui penempatannya di spec fungsional.
  - TC-AC-ACHS-252 tidak menyebut asersi isi sel; spec hanya menghitung baris berkas.
  - TC-AC-ACHS-253 menyebut "buka" berkas CSV tanpa menyebut cara membaca header; dicatat sebagai kemampuan pembaca CSV yang disediakan tim FE.
