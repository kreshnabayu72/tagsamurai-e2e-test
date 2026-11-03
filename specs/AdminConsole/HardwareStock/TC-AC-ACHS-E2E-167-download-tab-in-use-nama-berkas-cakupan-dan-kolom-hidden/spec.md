---
id: TC-AC-ACHS-E2E-167-download-tab-in-use-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Tab In Use Nama Berkas Cakupan dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-362
  - TC-AC-ACHS-363
  - TC-AC-ACHS-364
  - TC-AC-ACHS-367
coverage:
  web: automated
---

# Download Tab In Use Nama Berkas Cakupan dan Kolom Hidden

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` (Long Range) dengan 7 unit In Use (Pre-setup #18, Tabel F TC); baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya; urutan tampil default `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`. Keyword Search `Fixture.hardwareStock.derived.inUseClientA` (kata nama Client baris 1 setelah awalan badan usaha; Client baris 1 sampai 3) menghasilkan 3 baris (`Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`).
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan di browser (nama berkas) dan membaca isi berkas CSV dan XLSX (header, jumlah baris, urutan baris, BOM UTF-8, nama sheet).
- State global browser: spec ini menyembunyikan lalu menampilkan kembali kolom Client (konfigurasi kolom Tab In Use disimpan di browser); hook `after` suite menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Device Name baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 4, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[4].deviceName` |
  | Device Name baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 5, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[5].deviceName` |
  | Device Name baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 6, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[6].deviceName` |
  | Device Name baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 7, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | Nilai turunan inUseClientA | turunan dari `Fixture.hardwareStock.p18.f[1].client` | keyword Search: kata nama Client baris 1 Tabel F setelah awalan badan usaha (`Sejahtera`; substring Client baris 1 sampai 3; sama dengan keyword TC-AC-ACHS-318) | `Fixture.hardwareStock.derived.inUseClientA` |

## Test Steps

### Nama berkas, tooltip, overlay, dan kolom berkas (TC-AC-ACHS-362)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Hover icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Hardware-Stock-InUse-{Fixture.hardwareStock.p18.sku}.csv` terunduh
10. Klik icon Download, pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Hardware-Stock-InUse-{Fixture.hardwareStock.p18.sku}.xlsx` terunduh
13. Buka berkas CSV
14. Verifikasi kolom berkas CSV: Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power (SKU Long Range)
15. Verifikasi CSV UTF-8 dengan BOM
16. Verifikasi urutan baris CSV mengikuti sort default: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
17. Buka berkas XLSX
18. Verifikasi kolom berkas XLSX: Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power
19. Verifikasi XLSX satu sheet bernama `Sheet1`
20. Verifikasi urutan baris XLSX mengikuti sort default: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`

### Cakupan mengikuti Search dan seluruh halaman (TC-AC-ACHS-363)

21. Pastikan tidak ada Search atau Filter aktif dan rows per page 10 (default)
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi berkas CSV berisi seluruh 7 baris (bukan hanya 10 baris halaman pertama)
24. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
25. Klik icon Download, pilih `Download as CSV`
26. Verifikasi berkas CSV hanya berisi 3 baris hasil search
27. Klik icon `(←)` pada kotak Search

### Kolom hidden tidak ikut (TC-AC-ACHS-364)

28. Klik header kolom Actions `(⋯)`, uncheck `Client`
29. Klik icon Download, pilih `Download as CSV`
30. Buka berkas CSV
31. Verifikasi berkas CSV memuat kolom Device Name, Serial Number, dan Status
32. Verifikasi berkas CSV tidak memuat kolom Client
33. Klik header kolom Actions `(⋯)`, check `Client`
34. Klik icon Download, pilih `Download as CSV`
35. Buka berkas CSV
36. Verifikasi berkas CSV memuat kolom Client

### Hasil Search kosong (TC-AC-ACHS-367)

37. Ketik Search `zzqx-tidak-ada`, tekan Enter
38. Verifikasi tombol Download tetap aktif
39. Klik icon Download, pilih `Download as CSV`
40. Verifikasi tidak ada toast
41. Verifikasi berkas CSV berisi baris header kolom visible saja
42. Verifikasi berkas CSV tidak berisi baris data
43. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-362, 363, 364, 367). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Sejahtera` (TC-AC-ACHS-318). Dicocokkan dengan Tabel F Pre-setup #18 (Client baris 1 sampai 3 = 3 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah penghubung (bukan dari langkah TC): langkah 21 (memastikan tidak ada Search atau Filter aktif; rows per page default 10 sudah berlaku di awal), langkah 27 dan 43 (klik `(←)` mereset Search), langkah 33 (check `Client` kembali, memulihkan Column Visibility), langkah 13, 17, 30, 35 (membuka berkas lewat kemampuan baca berkas).
- Asersi nama berkas, nama kolom, jumlah baris, dan urutan baris adalah asersi fungsional (bagian 3 prinsip 13 butir f, `[KEPUTUSAN 2026-10-30]`). Langkah 15 (BOM UTF-8) dan 19 (nama sheet `Sheet1`) berasal dari TC-362 butir f dan g; keduanya adalah isi biner (kelas f) tetapi TC-362 tetap di spec ini karena satu TC satu spec (lihat Temuan untuk QA). Spec kelas f terpisah untuk permukaan ini adalah spec 168.
- Asersi absence toast (langkah 8, 11, 40) diletakkan segera setelah pemicu sebelum asersi artefak (bagian 8b butir 11); pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh. Absence kolom Client (langkah 32) memakai anchor positif langkah 31.
- Spec melewati sekitar 35 langkah (43 langkah): alasan, semua blok satu surface (Download Tab In Use) dan satu dataset; tiap blok mengembalikan Search dan Column Visibility sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state, label Status) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-362 butir f dan g (BOM UTF-8, `Sheet1`) dan butir h (urutan baris mengikuti sort default) adalah isi berkas; menurut prinsip 13 butir f isi berkas dipisah. TC-362 satu TC, spec memuatnya utuh di sini dan TC-366 di spec 168; usulan QA memecah TC-362 menjadi dua TC.
  - TC-363 langkah 4 ("Download CSV tanpa Search/Filter") mengasumsikan ukuran halaman default 10; spec memakai 10 sesuai Expected a ("bukan hanya 10 baris halaman pertama") walau halaman hanya berisi 7 baris.
  - TC-364 dan TC-363 tidak menyebut nama berkas unduhan kedua yang sama dengan pertama; spec menunggu berkas baru terunduh pada tiap pemicu.
