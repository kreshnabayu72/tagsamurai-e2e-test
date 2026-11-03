---
id: TC-AC-ACHS-E2E-092-hardware-log-screening-urutan-read-only-dan-scope
title: "Hardware Log: Screening, Urutan, Read-Only, dan Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-526
  - TC-AC-ACHS-527
  - TC-AC-ACHS-528
  - TC-AC-ACHS-529
  - TC-AC-ACHS-530
  - TC-AC-ACHS-531
  - TC-AC-ACHS-552
  - TC-AC-ACHS-589
coverage:
  web: automated
---

# Hardware Log: Screening, Urutan, Read-Only, dan Scope

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; penahanan dan kegagalan respons lewat intercept parsial di atas backend nyata).
- Akun aktor pertama: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-531): Distributor Manage hardware stock (entitas `{Fixture.hardwareStock.p10.entityName}`), Local Registration aktif, `{Fixture.hardwareStock.account.p10.distributorCakra.email}` (Pre-setup #10, `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after` (juga untuk Distributor di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #20 dan #27; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `{Fixture.hardwareStock.p16.a[4].sku}` dengan unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}` (Registered By `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}`, entri terbaru `Hardware Registered by {Fixture.hardwareStock.account.p11.distributorMitra.shortName}`), unit Waiting for Approval `{Fixture.hardwareStock.p17.e[28].deviceName}`, dan unit In Use `{Fixture.hardwareStock.p18.f[1].deviceName}` (Pre-setup #17, #18, Hardware Log Pre-setup #17c: satu unit tanpa entri dan satu unit dengan beberapa event, termasuk entri bertimestamp sama); SKU `{Fixture.hardwareStock.p16.a[3].sku}` (Smart Fixed Reader) dengan 8 unit Available, 5 milik `{Fixture.hardwareStock.p10.entityName}` (Pre-setup #27).

- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.email}` | No 10 | email akun Pre-setup No 10 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p17.e[10].deviceName}` | No 17, Tabel E baris N = 10 | Device Name unit Available SKU Long Range dengan N terkecil (N = 10) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | `{Fixture.hardwareStock.p17.e[11].deviceName}` | No 17, Tabel E baris N = 11 | Device Name unit Available SKU Long Range (N = 11) | `Fixture.hardwareStock.p17.e[11].deviceName` |
  | `{Fixture.hardwareStock.p17.e[28].deviceName}` | No 17, Tabel E baris N = 28 | Device Name unit Waiting for Approval SKU Long Range (N = 28; Current Power `—`) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | `{Fixture.hardwareStock.p18.f[1].deviceName}` | No 18, Tabel F baris 1 | Device Name unit In Use SKU Long Range (N = 1) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | `{Fixture.hardwareStock.p27.fx[6].serialNumber}` | No 27 | Serial Number unit Available Smart Fixed Reader ke-6 (milik Distributor No 11) | `Fixture.hardwareStock.p27.fx[6].serialNumber` |
  | `{Fixture.hardwareStock.p27.fx[8].serialNumber}` | No 27 | Serial Number unit Available Smart Fixed Reader ke-8 (milik Distributor No 11) | `Fixture.hardwareStock.p27.fx[8].serialNumber` |
  | `{Fixture.hardwareStock.p10.entityName}` | No 10 | nama entitas Distributor akun No 10 | `Fixture.hardwareStock.p10.entityName` |
  | `{Fixture.hardwareStock.p11.entityName}` | No 11 | nama entitas Distributor akun No 11 | `Fixture.hardwareStock.p11.entityName` |
  | `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}` | No 11 | singkatan tampil user Distributor No 11 | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
  | `{Fixture.hardwareStock.account.p11.distributorMitra.fullName}` | No 11 | nama lengkap user Distributor No 11 (tampil pada hover) | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |

- Kemampuan teknis (disediakan tim FE): intercept respons HTTP Hardware Log dengan status 500 (pemicu error load, `P-2`) dan penahanan respons selama 3 detik (nilai dari Data Uji TC-589) lalu melepasnya.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15 (`DD MMM YYYY`, `HH:mm`); tidak ada pergeseran jam.

## Test Steps

### TC-AC-ACHS-526: Screening popup Hardware Log

1. Klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[4].sku}`
2. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[10].deviceName}`
3. Klik `Hardware Log`
4. Verifikasi Header: Title `Hardware Log`, Badge Status `Available`, dan tombol close `[✕]`
5. Verifikasi Header: grid label:value `Device Name`, `Serial Number`, `Type`, `Range Type`, `SKU`, `Brand`, `Model/Type`
6. Verifikasi Body: daftar kronologis (timeline, bukan tabel) terbaru di atas
7. Verifikasi Body: scroll vertikal dengan header tetap
8. Verifikasi Body: tanpa Search, Filter, Sort, Setup Column, Download, dan paginasi
9. Verifikasi tidak ada footer dan tidak ada tombol `[Close]`

### TC-AC-ACHS-552: Komponen pelaku

10. Verifikasi pelaku pada judul entri `Hardware Registered by` tampil ikon user generik dan `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}`
11. Hover pelaku `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}`
12. Verifikasi hover menampilkan nama lengkap `{Fixture.hardwareStock.account.p11.distributorMitra.fullName}`
13. Verifikasi judul tampil teks biasa (bukan badge)
14. Verifikasi tanggal dan jam mengikuti General Settings

### TC-AC-ACHS-530: Hardware Log read-only

15. Verifikasi tidak ada aksi ubah atau hapus pada entri maupun popup (entri append-only)
16. Tekan Esc
17. Verifikasi popup ditutup lewat Esc

### TC-AC-ACHS-529: Urutan Hardware Log

18. Klik `(⋯)` pada unit yang memiliki beberapa event (Pre-setup #17c), lalu klik `Hardware Log`
19. Verifikasi entri berurutan dari terbaru ke terlama
20. Verifikasi entri bertimestamp sama menampilkan yang ditulis lebih akhir di atas
21. Verifikasi format tanggal dan jam mengikuti General Settings
22. Klik `[✕]`

### TC-AC-ACHS-589: Loading popup Hardware Log

23. Pasang penahanan respons Hardware Log selama 3 detik
24. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[10].deviceName}`, lalu klik `Hardware Log`
25. Verifikasi area daftar entri popup `Hardware Log` menampilkan Loading component sampai data tiba
26. Lepas penahanan respons
27. Verifikasi entri tampil terbaru di atas
28. Klik `[✕]`

### TC-AC-ACHS-528: Empty state dan error load

29. Klik `(⋯)` pada unit tanpa entri (Pre-setup #17c), lalu klik `Hardware Log`
30. Verifikasi empty state: ilustrasi dengan Title `No log yet` dan Description `Events for this hardware will appear here.`
31. Klik `[✕]`
32. Pasang intercept respons Hardware Log dengan status 500
33. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[11].deviceName}`, lalu klik `Hardware Log`
34. Verifikasi popup menampilkan `Unable to load this data.`
35. Verifikasi popup menampilkan tombol `[Try Again]`
36. Lepas intercept, lalu klik `[✕]`

### TC-AC-ACHS-527: Header Hardware Log lintas jenis SKU dan status

37. Klik segmen breadcrumb `Stock`, lalu klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[3].sku}`
38. Klik `(⋯)` pada unit Available, lalu klik `Hardware Log`
39. Verifikasi grid header tanpa baris Range Type
40. Verifikasi atribut katalog yang kosong tampil `—`
41. Klik `[✕]`
42. Klik segmen breadcrumb `Stock`, klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[4].sku}`, lalu pastikan Tab `Available` aktif
43. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[28].deviceName}`, lalu klik `Hardware Log`
44. Verifikasi Badge Status `Waiting for Approval`
45. Verifikasi Range Type `Long Range` tampil di grid header
46. Klik `[✕]`
47. Klik Tab `In Use`
48. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p18.f[1].deviceName}`, lalu klik `Hardware Log`
49. Verifikasi Badge Status `In Use`
50. Klik `[✕]`
51. Logout, lalu login sebagai Distributor (Pre-setup #10); tunggu aksi selesai

### TC-AC-ACHS-531: Scope Distributor

52. Buka Hardware > Stock, klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[3].sku}`
53. Verifikasi Tab Available memuat 5 unit `{Fixture.hardwareStock.p10.entityName}`
54. Verifikasi unit `{Fixture.hardwareStock.p11.entityName}` (`{Fixture.hardwareStock.p27.fx[6].serialNumber}` sampai `{Fixture.hardwareStock.p27.fx[8].serialNumber}`) tidak terlihat
55. Klik `(⋯)` pada salah satu unit milik sendiri, lalu klik `Hardware Log`
56. Verifikasi popup `Hardware Log` unit milik sendiri terbuka
57. Klik `[✕]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-526, 527, 528, 529, 530, 531, 552, 589). Tidak ada TC hanya-BE di spec ini.
- `P-2`: error load pada TC-528 dipaksa lewat intercept 500 hanya sebagai pemicu state UI error yang diuji (`Unable to load this data.` dan `[Try Again]`); intercept dilepas pada langkah 36 (S-09).
- Urutan menyimpang dari TC: TC-552 dan TC-530 mengikuti TC-526 pada popup yang sama untuk menghemat pembukaan; TC-527 dan TC-531 di akhir (SKU lain dan ganti akun).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 3, 11, 16, 18, 22, 24, 28, 29, 31, 33, 36, 37, 38, 41, 42, 43, 46, 47, 48, 50, 52, 55, 57 (navigasi, membuka dan menutup popup), 23 dan 26 (menahan dan melepas respons), 32 (intercept), 51 (ganti akun).
- Spec ini 57 langkah, lebih dari sekitar 35 langkah. Alasan: delapan TC satu surface popup Hardware Log, semuanya fungsional dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Penahanan respons pada TC-589 hanya mengamati state Loading (bukan kelas b).
- Temuan untuk QA:
  - TC-527 butir b ("atribut katalog kosong tampil `—`") tidak menyebut atribut mana yang kosong pada SKU `{Fixture.hardwareStock.p16.a[3].sku}`; spec mengasersi atribut kosong yang ada.
  - TC-527 langkah 5 menyebut "unit In Use" tanpa nama; spec memakai `{Fixture.hardwareStock.p18.f[1].deviceName}` (Pre-setup #18). Langkah 4 menyebut "unit Available" FX9600 tanpa nama; spec memakai unit pertama.
  - TC-529 dan TC-528 menyebut unit Pre-setup #17c tanpa nama unit; spec menyebut unit dengan beberapa event atau tanpa entri sesuai #17c.
  - TC-530 butir b ("entri append-only") adalah kesimpulan dari butir a dan tidak punya observasi terpisah; ditulis satu `Verifikasi` (langkah 15).
