---
id: TC-AC-ACHS-E2E-022-scope-stock-list-detail-download-per-aktor-distributor-principal
title: "Scope Stock List, Stock Detail, dan Download per Aktor Distributor dan Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-15
  - TC-AC-ACHS-16
  - TC-AC-ACHS-17
  - TC-AC-ACHS-74
  - TC-AC-ACHS-565
  - TC-AC-ACHS-566
coverage:
  web: automated
---

# Scope Stock List, Stock Detail, dan Download per Aktor Distributor dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun default suite: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun eksplisit (password memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE; belum terdaftar, lihat Temuan untuk QA):
  - Distributor Pre-setup No 10, Local Registration aktif, `{Fixture.hardwareStock.account.p10.distributorCakra.email}` (Pre-setup No 10).
  - Distributor Pre-setup No 11, Local Registration aktif, `{Fixture.hardwareStock.account.p11.distributorMitra.email}` (Pre-setup No 11).
- Data Pre-setup (hanya dibaca): kepemilikan unit Distributor (No 27: `{Fixture.hardwareStock.p16.a[3].sku}` 8 unit, 5 unit pertama milik Distributor No 10, 3 unit berikutnya milik Distributor No 11; `{Fixture.hardwareStock.p16.a[5].sku}` tanpa unit milik atau In Use ke jaringan Distributor No 10), unit In Use `{Fixture.hardwareStock.p16.a[4].sku}` (No 18: `{Fixture.hardwareStock.p18.f[1].client}` 3 unit, `{Fixture.hardwareStock.p18.f[4].client}` 2 unit, `{Fixture.hardwareStock.p18.f[6].client}` 1 unit, `{Fixture.hardwareStock.p18.f[7].client}` 1 unit), jaringan Client (No 23: `{Fixture.hardwareStock.p18.f[7].client}` adalah Client Partner Pre-setup No 14 di bawah Distributor No 10). Hitungan yang diharapkan: lihat langkah.
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.email}` | No 10 | email akun Pre-setup No 10 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
  | `{Fixture.hardwareStock.account.p11.distributorMitra.email}` | No 11 | email akun Pre-setup No 11 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p11.distributorMitra.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p16.a[5].sku}` | No 16, 27, Tabel A baris 5 | kode SKU BLE Gateway (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
  | `{Fixture.hardwareStock.p16.a[4].brand}` | No 16, Tabel A baris 4 | Brand SKU Handheld Reader Long Range (kata kunci Search dan opsi Filter) | `Fixture.hardwareStock.p16.a[4].brand` |
  | `{Fixture.hardwareStock.p18.f[1].client}` | No 18, 21, 22, Tabel F baris 1 | Client unit In Use N = 1 (juga N = 2 dan 3); muncul di Tab Active; kata kunci Search | `Fixture.hardwareStock.p18.f[1].client` |
  | `{Fixture.hardwareStock.p18.f[4].client}` | No 18, 23, Tabel F baris 4 | Client unit In Use N = 4 (juga N = 5), jaringan Distributor No 10 | `Fixture.hardwareStock.p18.f[4].client` |
  | `{Fixture.hardwareStock.p18.f[7].client}` | No 18, 23, Tabel F baris 7 | Client unit In Use N = 7 (Client Partner No 14 di bawah Distributor No 10) | `Fixture.hardwareStock.p18.f[7].client` |
  | `{Fixture.hardwareStock.p18.f[6].client}` | No 18, 23, Tabel F baris 6 | Client unit In Use N = 6, jaringan Distributor No 11 | `Fixture.hardwareStock.p18.f[6].client` |

- Kemampuan teknis (disediakan tim FE/BE): membaca isi berkas CSV hasil Download (nama berkas, kolom, jumlah baris dan nilai baris; bukan isi biner).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun default suite. Flag halaman Stock List dan Stock Detail untuk kedua akun Distributor disetel true di hook `before` spec ini dan dipulihkan di hook `after`; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Distributor Pre-setup No 10 (TC-AC-ACHS-15, 74, 565, 566)

1. Logout, lalu login sebagai Distributor (Pre-setup No 10)
2. Klik menu Hardware > Stock di sidebar
3. Ketik Search Brand `{Fixture.hardwareStock.p16.a[4].brand}`, tekan Enter
4. Verifikasi baris `{Fixture.hardwareStock.p16.a[4].sku}` tampil dengan Total Registered `12`, Available `6`, In Use `6`
5. Verifikasi baris `{Fixture.hardwareStock.p16.a[3].sku}` tampil dengan Total Registered `5`, Available `5`, In Use `0`
6. Verifikasi tidak ada kolom `Allocated`
7. Ganti isi kotak search dengan SKU `{Fixture.hardwareStock.p16.a[5].sku}`, tekan Enter
8. Verifikasi empty state `No results found` (SKU `{Fixture.hardwareStock.p16.a[5].sku}` tidak tampil)
9. Klik `(←)` pada kotak Search
10. Klik icon Download, pilih `Download as CSV`, buka berkas
11. Verifikasi berkas memuat baris `{Fixture.hardwareStock.p16.a[4].sku}` dengan Total Registered `12`, Available `6`, In Use `6`
12. Verifikasi berkas memuat baris `{Fixture.hardwareStock.p16.a[3].sku}` dengan Total Registered `5`, Available `5`, In Use `0`
13. Verifikasi berkas tidak memuat SKU lain di luar scope (tidak ada baris `{Fixture.hardwareStock.p16.a[5].sku}`)
14. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
15. Klik Tab `In Use`
16. Verifikasi Tab In Use memuat unit untuk Client `{Fixture.hardwareStock.p18.f[1].client}`, `{Fixture.hardwareStock.p18.f[4].client}`, dan `{Fixture.hardwareStock.p18.f[7].client}` (melalui Partner) sebanyak 6 baris dengan info `Showing 1–6 of 6 entries`
17. Verifikasi tidak ada unit Client `{Fixture.hardwareStock.p18.f[6].client}` di Tab In Use
18. Klik icon Download, pilih `Download as CSV`, buka berkas
19. Verifikasi berkas hanya memuat 6 unit In Use ke Client jaringan Distributor Pre-setup No 10

### Distributor Pre-setup No 11 (TC-AC-ACHS-16)

20. Logout, lalu login sebagai Distributor (Pre-setup No 11)
21. Klik menu Hardware > Stock di sidebar
22. Ketik Search Brand `{Fixture.hardwareStock.p16.a[4].brand}`, tekan Enter
23. Verifikasi baris `{Fixture.hardwareStock.p16.a[4].sku}` tampil dengan Total Registered `7`, Available `6`, In Use `1`
24. Verifikasi baris `{Fixture.hardwareStock.p16.a[3].sku}` tampil dengan Total Registered `3`, Available `3`, In Use `0` (5 unit milik Distributor No 10 tidak terlihat)

### Principal (TC-AC-ACHS-17)

25. Logout, lalu login sebagai Total Control (Pre-setup No 1)
26. Klik menu Hardware > Stock di sidebar
27. Verifikasi baris `{Fixture.hardwareStock.p16.a[3].sku}` tampil dengan Total Registered `8`, Available `8`, In Use `0` (gabungan unit Distributor No 10 dan Distributor No 11)
28. Verifikasi baris `{Fixture.hardwareStock.p16.a[4].sku}` tampil dengan Total Registered `25`, Available `18`, In Use `7`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-15, 16, 17, 74, 565, 566). Tidak ada TC hanya-BE di spec ini.
- Spec memuat Step ganti akun eksplisit (langkah 1, 20, 25). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras karena tiap aktor membaca scope sendiri dari Population yang sama (verifikasi baca murni, satu kelas harness; bagian 3 konvensi, pemisah beda akun butir b). Asersi berkas Download (nama, kolom, jumlah dan nilai baris) adalah asersi fungsional, bukan isi biner (kelas f).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): Step ganti akun, klik menu Hardware > Stock di sidebar (mereset Search), `(←)` pada kotak Search, dan Search `{Fixture.hardwareStock.p16.a[5].sku}` (TC-15 langkah 4 "Cari SKU" ditulis sebagai Search).
- Spec di atas smell 35 langkah (28 langkah). Alasan: seluruh blok adalah verifikasi scope baca atas Population yang sama pada tiga aktor, tiap aktor berdiri sendiri, dan memecahnya menambah login dan hook tanpa pemisah nyata.
- Temuan untuk QA:
  - TC-74 Expected a ("angka dari unit dalam scope") tidak menyebut baris dan angka; spec memakai angka TC-15 (RFD40 `12 | 6 | 6`, FX9600 `5 | 5 | 0`) sebagai nilai berkas, diturunkan dari Expected TC-15 untuk aktor yang sama.
  - TC-566 Expected tidak menyebut nama atau kolom berkas; spec mengasersi 6 baris unit In Use dan memerlukan kemampuan membaca isi CSV (disediakan tim FE/BE). Nilai kolom user pada berkas ditulis nama lengkap (NC-14) dan tidak diasersi di spec ini.
  - TC-565 Expected a menyebut "6 baris" (`{Fixture.hardwareStock.p18.f[1].client}` 3, `{Fixture.hardwareStock.p18.f[4].client}` 2, `{Fixture.hardwareStock.p18.f[7].client}` 1); spec mengasersi info `Showing 1–6 of 6 entries` dan Client.
  - TC-15 menyebut Pre-setup No 18 sebagai "Client jaringan" padahal jaringan Client ada pada No 23; spec mengikuti Pre-setup No 23 dan No 27.
  - Password akun Distributor memakai nama env `AC_<ROLE>_PASSWORD` yang belum terdaftar; diminta dari tim FE.
  - Population Stock tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites sehingga tidak memerlukan pengecualian S-12. Hitungan numerik dipertahankan.
  - Perbandingan kata kunci Search terhadap substring TC (S-12): Search Brand `Zebra` (TC-15, 16) dan Brand penuh `Zebra`: hasil sama (SKU RFD40 dan FX9600 untuk aktor Distributor; SKU BLE tidak tampil). Search SKU BLE (langkah 7) adalah nilai penuh `Cari SKU` TC-15, sama. Tidak ada perbedaan hasil.
