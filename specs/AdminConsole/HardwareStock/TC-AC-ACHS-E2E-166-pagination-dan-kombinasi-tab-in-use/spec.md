---
id: TC-AC-ACHS-E2E-166-pagination-dan-kombinasi-tab-in-use
title: "Pagination dan Kombinasi Empat Kontrol Tab In Use"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-361
  - TC-AC-ACHS-368
coverage:
  web: automated
---

# Pagination dan Kombinasi Empat Kontrol Tab In Use

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca):
  - SKU `Fixture.hardwareStock.p18.sku` (Long Range) dengan 7 unit In Use (Pre-setup #18, Tabel F TC): baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya; Client sama pada baris 1 sampai 3 (`Fixture.hardwareStock.p18.f[1].client`). Keyword Search `Fixture.hardwareStock.derived.inUseClientA` = kata nama Client baris 1 setelah awalan badan usaha.
  - SKU `Fixture.hardwareStock.p19.sku` (Short Range, Pre-setup #19 TC): 16 unit In Use (10 milik Client `Fixture.hardwareStock.p18.f[1].client`, 6 milik Client `Fixture.hardwareStock.p18.f[4].client`; nama Client yang sama dengan Tabel F menurut TC #18 dan #19), tanpa kolom Power.
- Pilihan spec (bukan nilai TC): TC-361 tidak menyebut Filter, sort, dan ukuran halaman yang dipakai; spec memakai Filter Client = `Fixture.hardwareStock.p18.f[1].client`, sort Device Name Ascending, dan rows per page 25.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Client baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].client` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Client baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 4, Tabel F (#18) | `Fixture.hardwareStock.p18.f[4].client` |
  | SKU Short Range 16 unit In Use | #19 SKU TC52 (sama dengan Tabel A baris 1) | kode SKU Handheld Reader Short Range: 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p19.sku` |
  | Nilai turunan inUseClientA | turunan dari `Fixture.hardwareStock.p18.f[1].client` | keyword Search: kata nama Client baris 1 Tabel F setelah awalan badan usaha (`Sejahtera`; substring Client baris 1 sampai 3; sama dengan keyword TC-AC-ACHS-318) | `Fixture.hardwareStock.derived.inUseClientA` |

## Test Steps

### Kombinasi empat kontrol dan pemulihan dari 0 hasil (TC-AC-ACHS-361)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
4. Klik icon Filter, isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
5. Klik header kolom Device Name sekali (Ascending)
6. Ubah rows per page menjadi 25
7. Verifikasi keyword `Fixture.hardwareStock.derived.inUseClientA` tetap terisi di kotak Search
8. Verifikasi badge titik tampil pada ikon Filter
9. Verifikasi indikator Ascending aktif pada Device Name
10. Verifikasi rows per page menunjukkan 25
11. Verifikasi tabel menampilkan 3 baris berurutan `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`
12. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
13. Verifikasi empty state: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
14. Kosongkan isi kotak search, tekan Enter
15. Verifikasi tabel kembali menampilkan 3 baris `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` sesuai Filter, Sort, dan page size yang masih aktif
16. Verifikasi badge titik Filter, indikator Ascending Device Name, dan rows per page 25 masih aktif
17. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
18. Klik header kolom Device Name dua kali sampai netral, ganti rows per page ke 10
19. Klik icon `(←)` pada kotak Search

### Pagination SKU dengan 16 unit In Use (TC-AC-ACHS-368)

20. Klik menu Hardware > Stock di sidebar
21. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p19.sku`
22. Klik Tab `In Use`
23. Verifikasi footer halaman 1: `Showing 1–10 of 16 entries`
24. Klik `Next`
25. Verifikasi footer halaman 2: `Showing 11–16 of 16 entries`
26. Verifikasi halaman 2 berisi 6 baris
27. Isi input halaman `1`, tekan Enter
28. Verifikasi tabel kembali ke halaman 1
29. Ganti rows per page ke 25
30. Verifikasi tabel menampilkan 16 baris pada satu halaman
31. Verifikasi Tab In Use SKU Short Range tidak memiliki kolom Min Power, Max Power, dan Current Power

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-361 dan 368). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Sejahtera` (TC-AC-ACHS-318). Dicocokkan dengan Tabel F Pre-setup #18 (Client baris 1 sampai 3 = 3 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah penghubung (bukan dari langkah TC): langkah 17, 18, 19 (memulihkan Filter, sort, dan Search, S-09); langkah 20 (klik menu sidebar yang mereset Search, Sort, Filter, dan membawa ke Stock List sebelum membuka SKU lain, bagian 4 konvensi).
- TC-368 punya precondition SKU berbeda dari TC-361 (unit 16 In Use) sehingga ada dua kali buka Stock Detail; keduanya satu topik (Pagination dan kombinasi kontrol Tab In Use).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, #19, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-361 langkah 5 sampai 7 ("Terapkan satu Filter", "Klik header sort", "Ubah rows per page") tidak menyebut nilai; spec memilih sesuai Prerequisites. Dengan 3 baris hasil, Pagination (halaman berikutnya) tidak teramati pada kombinasi ini.
  - TC-368 Expected c sampai d tidak menyebut footer sesudah rows per page 25; spec hanya mengasersi 16 baris pada satu halaman.
