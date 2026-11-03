---
id: TC-AC-ACHS-E2E-001-screening-stock-list-toolbar-overlay-dan-tanpa-allocated
title: "Screening Stock List: Toolbar, Overlay Row Action, dan Tanpa Kolom Allocated atau Checkbox"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-1
  - TC-AC-ACHS-2
  - TC-AC-ACHS-10
  - TC-AC-ACHS-12
  - TC-AC-ACHS-13
  - TC-AC-ACHS-14
coverage:
  web: automated
---

# Screening Stock List: Toolbar, Overlay Row Action, dan Tanpa Kolom Allocated atau Checkbox

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (tidak diubah spec, hanya dibaca): Katalog SKU 30 baris Stock List (No 16, Tabel A), unit SKU `{Fixture.hardwareStock.p16.a[4].sku}` 18 Available dan 7 In Use (No 17, 18), dua SKU non-hardware (Tablet dan GPS Tracker; No 16) yang tidak tampil di Stock List, saldo kuota Device Allocation Handheld Reader - Long Range yang berbeda dari hitungan unit Available (No 27). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[8].sku}` | No 16, 24, Tabel A baris 8 | kode SKU Smart Fixed Reader dengan 120 unit Available (baris pertama default Stock List) | `Fixture.hardwareStock.p16.a[8].sku` |
  | `{Fixture.hardwareStock.p16.a[7].sku}` | No 16, Tabel A baris 7 | kode SKU BLE Gateway dengan Brand bernama panjang (3 Available; baris kedua default Stock List) | `Fixture.hardwareStock.p16.a[7].sku` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p17.e[10].deviceName}` | No 17, Tabel E baris N = 10 | Device Name unit Available SKU Long Range dengan N terkecil (N = 10) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | `{Fixture.hardwareStock.p18.f[1].deviceName}` | No 18, Tabel F baris 1 | Device Name unit In Use SKU Long Range (N = 1) | `Fixture.hardwareStock.p18.f[1].deviceName` |

- Tabel "Elemen tooltip" (parameter langkah 11 sampai 15):

  | Elemen | Tooltip |
  |---|---|
  | icon Search | `Search` |
  | icon Filter | `Filter` |
  | icon Download | `Download` |
  | header kolom Actions `(⋯)` | `Column Visibility` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-1: Screening Stock List (Header, Body, Footer)

1. Verifikasi Breadcrumb `Hardware > Stock` dengan dua segmen statis yang tidak bisa diklik
2. Verifikasi tidak ada Page Title terpisah di bawah breadcrumb
3. Verifikasi Table Tools `Search | Filter | Download` tampil
4. Verifikasi tidak ada `[Add Stock]` dan tidak ada icon Changelog pada Table Tools
5. Verifikasi kolom tabel `Photo (unsortable) | Device Name (sortable) | SKU (sortable) | Type (sortable) | Range Type (sortable) | Brand (sortable) | Model/Type (sortable) | Total Registered (sortable) | Available (sortable) | In Use (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi tidak ada kolom `Allocated` dan tidak ada kolom checkbox
7. Verifikasi baris pertama default `{Fixture.hardwareStock.p16.a[8].sku}`
8. Verifikasi baris kedua default `{Fixture.hardwareStock.p16.a[7].sku}`
9. Verifikasi pagination default 10 baris per halaman
10. Verifikasi info pagination `Showing 1–10 of 30 entries`

### TC-AC-ACHS-2: Tooltip hover icon Table Tools dan header Column Visibility

11. Untuk setiap baris tabel "Elemen tooltip" pada Prerequisites, lakukan langkah 12 sampai 15
12. Hover elemen pada baris tabel
13. Verifikasi tooltip pada kolom Tooltip baris tabel tampil
14. Pindahkan fokus keyboard (Tab) ke elemen pada baris tabel
15. Verifikasi tooltip pada kolom Tooltip baris tabel tampil saat elemen menerima fokus keyboard

### TC-AC-ACHS-10: Katalog SKU Tablet dan GPS Tracker tidak tampil

16. Ketik Search `DUMMY`, tekan Enter
17. Verifikasi empty state `No results found`
18. Klik `(←)` pada kotak Search
19. Klik icon Filter
20. Buka dropdown Type pada Filter Panel
21. Verifikasi opsi Type hanya `Handheld Reader`, `Smart Fixed Reader`, `BLE Gateway`
22. Tutup Filter Panel dengan `Esc`

### TC-AC-ACHS-12: Screening overlay row action Stock List

23. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
24. Verifikasi overlay berisi dua opsi berurutan `Detail` dan `Add Stock`
25. Verifikasi overlay tampil tanpa backdrop
26. Klik di luar overlay
27. Verifikasi overlay tertutup
28. Verifikasi klik di luar overlay tidak memicu aksi (halaman tetap Hardware > Stock, Stock Detail dan halaman Add Stock tidak terbuka)

### TC-AC-ACHS-13: Tanpa kolom atau metrik Allocated, Available bukan kuota

29. Verifikasi header kolom Stock List tidak memuat `Allocated`
30. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
31. Verifikasi Summary bar hanya memuat tiga kartu berurutan `Total Registered`, `Available`, `In Use`
32. Verifikasi nilai Available `18` sama dengan jumlah unit berstatus Available dan tidak mengikuti saldo kuota Device Allocation

### TC-AC-ACHS-14: Tanpa checkbox seleksi, Select All, dan Bulk Action Bar

33. Klik segmen breadcrumb `Stock`
34. Verifikasi Stock List tidak memiliki kolom checkbox maupun tombol `Select All`
35. Verifikasi tidak ada Bulk Action Bar pada Stock List
36. Klik biasa pada area baris `{Fixture.hardwareStock.p16.a[3].sku}`
37. Verifikasi klik baris tidak menyeleksi apa pun pada Stock List
38. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
39. Verifikasi Tab Available tidak memiliki kolom checkbox maupun tombol `Select All`
40. Verifikasi tidak ada Bulk Action Bar pada Tab Available
41. Klik biasa pada area baris `{Fixture.hardwareStock.p17.e[10].deviceName}`
42. Verifikasi klik baris tidak menyeleksi apa pun pada Tab Available
43. Klik Tab `In Use`
44. Verifikasi Tab In Use tidak memiliki kolom checkbox maupun tombol `Select All`
45. Verifikasi tidak ada Bulk Action Bar pada Tab In Use
46. Klik biasa pada area baris `{Fixture.hardwareStock.p18.f[1].deviceName}`
47. Verifikasi klik baris tidak menyeleksi apa pun pada Tab In Use

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-1, 2, 10, 12, 13, 14). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 18 dan 22 (mereset Search dan menutup Filter Panel setelah TC-10), langkah 33 (kembali ke Stock List lewat breadcrumb sebelum TC-14).
- Langkah 11 sampai 15 diulang empat kali (sekali per baris tabel "Elemen tooltip"); blok ulang menjadi 16 langkah setelah ekspansi.
- Spec di atas smell 35 langkah (47 langkah nominal, 59 setelah ekspansi). Alasan: seluruh blok adalah screening satu layar Stock List pada dataset yang sama, keenam TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-1 Expected b.i menjelaskan Column Visibility `(⋯)` ("header klik = buka overlay Column Visibility, body per baris = row action menu") tetapi Langkah Uji hanya mengamati; spec mengasersi daftar kolom dan status unsortable tanpa mengklik header (overlay Column Visibility diuji di spec Setup Column).
  - TC-2 Expected b ("tooltip juga muncul saat elemen menerima fokus keyboard") tidak punya langkah keyboard di Langkah Uji; spec memakai Tab untuk memindahkan fokus ke keempat elemen.
  - TC-13 Expected c ("tidak berubah mengikuti saldo kuota") tidak menyebut cara mengamati saldo kuota Device Allocation; spec mengasersi nilai Available `18` sama dengan hitungan unit Available (Pre-setup No 17, 27).
  - TC-14 langkah 4 ("Centang area baris dengan klik biasa") tidak menyebut tabel yang diuji; spec mengklik baris pada ketiga tabel (Stock List, Tab Available, Tab In Use).
  - Population Katalog SKU tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites sehingga tidak memerlukan pengecualian S-12. Kata kunci Search `DUMMY` (langkah 16) adalah input dari TC-10 dan bukan nama record yang dirujuk.
  - Password akun aktor memakai nama `AC_TC_PASSWORD` menurut bagian 5 konvensi; pendaftaran di `executionConfig.environmentVariables` dan `.env.example` diminta dari tim FE.
