---
id: TC-AC-ACHS-E2E-003-empty-state-genuinely-kosong-dan-no-results-detail
title: "Empty State Genuinely Kosong dan No Results Stock Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-18
  - TC-AC-ACHS-46
  - TC-AC-ACHS-47
  - TC-AC-ACHS-48
  - TC-AC-ACHS-54
coverage:
  web: automated
---

# Empty State Genuinely Kosong dan No Results Stock Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor kedua (langkah 18): Total Control Principal pada company automation cadangan tanpa SKU hardware dan tanpa Subject (Pre-setup No 16c). Email dan password akun ini tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup (hanya dibaca): SKU `{Fixture.hardwareStock.p16.a[6].sku}` tanpa unit Available maupun Waiting for Approval (Tabel A), SKU `{Fixture.hardwareStock.p16.a[3].sku}` tanpa unit In Use (Tabel A), SKU `{Fixture.hardwareStock.p16.a[4].sku}` dengan unit (No 17, 18). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[6].sku}` | No 16, Tabel A baris 6 | kode SKU Smart Fixed Reader tanpa unit (Total Registered 0) | `Fixture.hardwareStock.p16.a[6].sku` |
  | `{Fixture.hardwareStock.p16.a[6].modelType}` | No 16, Tabel A baris 6 | Model/Type SKU Smart Fixed Reader tanpa unit (kata kunci Search) | `Fixture.hardwareStock.p16.a[6].modelType` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun aktor pertama (lihat suite.md). Flag halaman Stock List dan Approvals Hardware Stock untuk akun company cadangan (langkah 18) disetel true di langkah 18 dan dipulihkan di hook `after` spec ini; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-46: Tab Available kosong

1. Ketik Search Model/Type `{Fixture.hardwareStock.p16.a[6].modelType}`, tekan Enter
2. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[6].sku}`, klik row action `Detail`
3. Verifikasi empty state Tab Available: Illustration (empty box) dengan Title `No available hardware units` dan Description `Available hardware units ready for deployment will appear here.`
4. Verifikasi Summary bar `0 | 0 | 0`

### TC-AC-ACHS-47: Tab In Use kosong

5. Klik segmen breadcrumb `Stock`
6. Ganti isi kotak search dengan SKU `{Fixture.hardwareStock.p16.a[3].sku}`, tekan Enter
7. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`, klik row action `Detail`
8. Klik Tab `In Use`
9. Verifikasi empty state Tab In Use: Illustration (empty box) dengan Title `No hardware units in use` dan Description `Hardware units activated by clients will appear here.`

### TC-AC-ACHS-48: Stock Detail tanpa hasil Search menampilkan empty state filtered pada kedua tab

10. Klik segmen breadcrumb `Stock`
11. Ganti isi kotak search dengan SKU `{Fixture.hardwareStock.p16.a[4].sku}`, tekan Enter
12. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
13. Ketik Search `zzqx-tidak-ada`, tekan Enter pada Tab Available
14. Verifikasi Tab Available menampilkan Illustration (empty box) dengan Title `No results found` dan Description `Try adjusting your search or filter.`
15. Klik Tab `In Use`
16. Ketik Search `zzqx-tidak-ada`, tekan Enter pada Tab In Use
17. Verifikasi Tab In Use menampilkan Illustration (empty box) dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-AC-ACHS-18 dan TC-AC-ACHS-54: Company cadangan tanpa SKU dan tanpa Subject

18. Logout, lalu login sebagai Total Control Principal company cadangan (Pre-setup No 16c), setelah flag Guided Tooltip halaman Stock List dan Approvals Hardware Stock akun itu disetel true
19. Klik menu Hardware > Stock di sidebar
20. Verifikasi Stock List menampilkan Illustration (empty box) dengan Title `No hardware stock yet` dan Description `Registered hardware inventory and device SKUs will appear here.`
21. Verifikasi tidak ada pagination yang bermakna
22. Verifikasi icon Download tetap tampil
23. Klik menu Approvals > Hardware Stock di sidebar
24. Verifikasi Tab Active menampilkan Illustration dengan Title `No pending approvals` dan Description `You have no pending approval requests at this moment.`
25. Verifikasi Tab Active tanpa CTA
26. Klik Tab `History`
27. Verifikasi Tab History menampilkan Illustration dengan Title `No approval history yet` dan Description `Processed approval requests will appear here.`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-18, 46, 47, 48, 54). Tidak ada TC hanya-BE di spec ini.
- Spec memuat Step ganti akun eksplisit (langkah 18). Bagian sesudah ganti akun (company cadangan) tetap bermakna walau bagian sebelumnya gagal keras karena memakai tenant dan data yang berbeda; kedua bagian adalah verifikasi baca murni tanpa pembuatan data dan satu kelas harness (bagian 3 konvensi, pemisah beda akun butir b).
- Urutan TC pada spec: TC-46, 47, 48, lalu TC-18 dan TC-54 (akun company cadangan) agar ganti akun hanya satu kali.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 6 dan 11 (Search untuk menemukan baris SKU target), langkah 5 dan 10 (kembali ke Stock List lewat breadcrumb), langkah 19 (membuka Stock List company cadangan lewat sidebar).
- Temuan untuk QA:
  - TC-18 Expected b ("Tidak ada pagination yang bermakna") tidak mendefinisikan asersi yang dapat diamati; spec mengasersi kalimat itu apa adanya pada langkah 21.
  - TC-18 dan TC-54 mensyaratkan company automation cadangan (Pre-setup No 16c) tanpa menyebut email akun dan password; akun dan env password disediakan tim FE.
  - Pre-setup No 16c hanya menyebut "company cadangan tanpa SKU hardware"; TC-54 membutuhkan company tanpa Subject juga. Spec mengasumsikan company yang sama (diminta konfirmasi tim FE/BE).
  - Population Katalog SKU (`{Fixture.hardwareStock.p16.a[6].sku}` tanpa unit, `{Fixture.hardwareStock.p16.a[3].sku}` tanpa In Use) tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites sehingga tidak memerlukan pengecualian S-12. Input `zzqx-tidak-ada` adalah string pencarian buatan spec, bukan data Pre-setup.
  - Search penghubung (langkah 1, 6, 11) bukan penggantian substring kata kunci TC (TC-46, 47, 48 membuka baris lewat row action tanpa Search). Perbandingan hasil: Model/Type penuh `IX4` hanya cocok dengan baris SKU IX4 (Tabel A baris 6), sama dengan baris yang dituju; tidak ada perbedaan hasil.
