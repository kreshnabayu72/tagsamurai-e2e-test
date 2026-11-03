---
id: TC-AC-ACHS-E2E-137-download-tab-available-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Stock Detail Tab Available: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-310
  - TC-AC-ACHS-311
  - TC-AC-ACHS-312
  - TC-AC-ACHS-315
coverage:
  web: automated
---

# Download Stock Detail Tab Available: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | Nilai turunan searchDeviceNameU20 | turunan dari `Fixture.hardwareStock.p17.e[20].deviceName` | keyword Search: bagian Device Name unit 20 Tabel E yang juga cocok dengan unit 21 sampai 28 (`Scanner - 2`; 9 baris; sama dengan keyword TC-AC-ACHS-263) | `Fixture.hardwareStock.derived.searchDeviceNameU20` |
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV dan XLSX yang terunduh (jumlah baris, header kolom, isi sel) dari lokasi unduhan unik per langkah unduh sehingga nama berkas yang sama tidak bertabrakan.
- State global yang diubah: visibilitas kolom Registered By (langkah 27 sampai 30) dipulihkan di langkah 30. Preferensi kolom di browser dihapus oleh hook suite `after`. Berkas terunduh disimpan di lokasi unduhan unik per langkah.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-310: CSV dan XLSX, nama berkas, tanpa toast sukses

3. Arahkan kursor ke icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Hardware-Stock-{Fixture.hardwareStock.p16.a[4].sku}.csv` terunduh
10. Klik icon Download, pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Hardware-Stock-{Fixture.hardwareStock.p16.a[4].sku}.xlsx` terunduh
13. Buka berkas CSV
14. Verifikasi kolom berkas CSV: Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power (SKU Long Range)
15. Verifikasi CSV berenkode UTF-8 dengan BOM
16. Verifikasi urutan baris CSV mengikuti sort default
17. Buka berkas XLSX
18. Verifikasi kolom berkas XLSX: Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power (SKU Long Range)
19. Verifikasi XLSX berisi satu sheet bernama `Sheet1`
20. Verifikasi urutan baris XLSX mengikuti sort default

### TC-AC-ACHS-311: Cakupan mengikuti Search atau Filter aktif dan seluruh halaman

21. Klik icon Download, pilih `Download as CSV`
22. Verifikasi berkas CSV berisi seluruh 19 baris (bukan hanya 10 baris halaman pertama)
23. Ketik Search `Fixture.hardwareStock.derived.searchDeviceNameU20`, tekan Enter
24. Klik icon Download, pilih `Download as CSV`
25. Verifikasi berkas CSV hanya berisi 9 baris hasil search
26. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-312: Kolom yang di-hide tidak ikut, ikut kembali setelah unhide

27. Klik header kolom Actions `(⋯)`, hilangkan centang `Registered By`, tutup overlay Column Visibility
28. Klik icon Download, pilih `Download as CSV`
29. Verifikasi berkas CSV tidak memuat kolom Registered By
30. Klik header kolom Actions `(⋯)`, ceklis kembali `Registered By`, tutup overlay Column Visibility
31. Klik icon Download, pilih `Download as CSV`
32. Verifikasi berkas CSV memuat kolom Registered By

### TC-AC-ACHS-315: Hasil filter kosong tetap aktif dan berisi header saja

33. Ketik Search `zzqx-tidak-ada`, tekan Enter
34. Verifikasi tombol Download tetap aktif
35. Klik icon Download, pilih `Download as CSV`
36. Verifikasi tidak ada toast
37. Verifikasi berkas CSV berisi baris header kolom visible saja tanpa baris data
38. Klik `✕` pada Search, tekan Enter

## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Scanner - 2` (TC-AC-ACHS-263). Dicocokkan dengan Tabel E Pre-setup #17 (Device Name unit 20 sampai 28 = 9 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Nama berkas unduhan memakai pola `Hardware-Stock-{SKU}.csv` / `.xlsx` dengan `{SKU}` = `Fixture.hardwareStock.p16.a[4].sku`. Asersi absence toast (langkah 8, 11, dan 37) diletakkan segera setelah pemicu unduh dan sebelum `Verifikasi` berkas (butir 8b nomor 11); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", pengosongan Search, pembukaan berkas (membaca isi lewat kemampuan pembaca CSV dan XLSX), dan pemulihan visibilitas kolom Registered By (langkah 30).
- TC-AC-ACHS-310 memuat Expected tentang isi berkas (BOM, `Sheet1`, urutan baris) selain nama berkas dan kolom; seluruh Expected TC itu ditulis di spec ini agar TC tetap berada di satu spec (lihat Temuan). Isi sel berkas diasersi di spec kelas binary buffer (TC-AC-ACHS-314).
- Spec memiliki 38 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Download pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan tidak ada perulangan atau langkah bersyarat; sebagian besar langkah adalah Verifikasi per klausa Expected TC-AC-ACHS-310.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-310 Expected f, g, dan h (BOM, `Sheet1`, urutan baris berkas) termasuk isi berkas (kelas binary buffer, bagian 3 prinsip 13f) tetapi satu TC tetap berada di satu spec; QA diminta memisahkan TC itu di sumber atau menyetujui penempatannya di spec fungsional.
  - TC-AC-ACHS-311 tidak menyebut asersi isi sel; spec hanya menghitung baris berkas.
