---
id: TC-AC-ACHS-E2E-252-role-matrix-positif-add-stock-manual
title: "Role Matrix: Add Stock Manual Berhasil per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-110
  - TC-AC-ACHS-111
  - TC-AC-ACHS-112
coverage:
  web: automated
---

# Role Matrix: Add Stock Manual Berhasil per Role

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List untuk akun aktor suite, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`). Flag Guided Tooltip halaman Stock List untuk akun selain Total Control (Create-Only, Default User, Distributor Cakra, Distributor Mitra) disetel true di hook `before` spec ini dan dipulihkan di hook `after`.
- Login di hook `before` spec ini: akun Create-Only (baris pertama tabel); halaman Hardware > Stock dibuka hook `beforeEach` suite. Akun berikutnya login lewat Step ganti akun eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password | Registered By | Blok langkah |
|---|---|---|---|---|
| Create-Only (Principal) | `createOnlyPrincipal_automated_qaTeam1@qwertysystem.net` (#4) | `Spectra.env.AC_CREATE_ONLY_PASSWORD` | `{shortNameCr}` | langkah 1 sampai 8 (TC-110) |
| Default User (Principal) | `defaultUserPrincipal_automated_qaTeam1@qwertysystem.net` (#2) | `Spectra.env.AC_DEFAULT_USER_PASSWORD` | `{shortNameDu}` | langkah 9 sampai 18 (TC-111) |
| Distributor Manage hardware stock, Local Registration aktif | `distributorCakra_automated_qaTeam1@qwertysystem.net` (#10) | `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD` | `{shortNameCakra}` | langkah 19 sampai 27 (TC-112) |
| Total Control (Principal) sebagai pengamat | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (#1) | `Spectra.env.AC_TC_PASSWORD` | - | langkah 28 sampai 33 (TC-112) |
| Distributor sebagai pengamat | `distributorMitra_automated_qaTeam1@qwertysystem.net` (#11) | `Spectra.env.AC_DISTRIBUTOR_MITRA_PASSWORD` | - | langkah 34 sampai 40 (TC-112) |

- Nama env password selain `AC_TC_PASSWORD` mengikuti pola `AC_<ROLE>_PASSWORD` dan ditetapkan tim FE (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`); nama pastinya tidak tertulis di TC (lihat Temuan untuk QA).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `{emailTc}` | #1 | email akun Total Control Principal | `Fixture.hardwareStock.account.p01.totalControl.email` |
| `{emailDu}` | #2 | email akun Default User | `Fixture.hardwareStock.account.p02.defaultUser.email` |
| `{shortNameDu}` | #2 | nama pendek akun Default User (kolom Registered By) | `Fixture.hardwareStock.account.p02.defaultUser.shortName` |
| `{shortNameCr}` | #4 | nama pendek akun Create-Only (kolom Registered By) | `Fixture.hardwareStock.account.p04.createOnly.shortName` |
| `{emailCakra}` | #10 | email akun Distributor PT Cakra Distribusi | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
| `{fullNameCakra}` | #10 | nama lengkap user Distributor PT Cakra Distribusi | `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |
| `{shortNameCakra}` | #10 | nama pendek user Distributor PT Cakra Distribusi (kolom Registered By) | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
| `{emailMitra}` | #11 | email akun Distributor PT Mitra Niaga | `Fixture.hardwareStock.account.p11.distributorMitra.email` |
| `{fullNameMitra}` | #11 | nama lengkap user Distributor PT Mitra Niaga | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |

- Data Pre-setup: SKU `{skuFx}` (Pre-setup #16, #27); lima unit Available milik entitas Distributor akun `{fullNameCakra}` (termasuk `{snCakraFx}`) dan tiga unit Available milik entitas Distributor akun `{fullNameMitra}` (Pre-setup #27).
- Data Dinamis (suffix per run): `SN-CR-0001-{runId}-252`, `SN-DU-0001-{runId}-252`, `SN-DIST-0001-{runId}-252`; dibuat langkah 5, 15, 25 dan dihapus hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang menghapus unit bersuffix `-{runId}-252` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA); mengatur flag Guided Tooltip per akun.
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuFx} berubah selama spec berjalan (SKU Pre-setup tidak dapat dimiliki spec); tiga unit dihapus hook `after`.

## Test Steps

### TC-AC-ACHS-110: Create-Only

1. Ketik Search `{skuFx}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuFx}`
3. Klik opsi `Add Stock`
4. Ketik `SN-CR-0001-{runId}-252`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, unit has been added to stock."
7. Verifikasi unit `SN-CR-0001-{runId}-252` berstatus `Available` pada Tab Available
8. Verifikasi Registered By unit itu `{shortNameCr}`

### TC-AC-ACHS-111: Default User

9. Logout, lalu login sebagai Default User `{emailDu}` (`Spectra.env.AC_DEFAULT_USER_PASSWORD`)
10. Buka Hardware > Stock lewat sidebar
11. Ketik Search `{skuFx}`, tekan Enter
12. Klik `(⋯)` pada baris SKU `{skuFx}`
13. Klik opsi `Add Stock`
14. Ketik `SN-DU-0001-{runId}-252`
15. Klik `[Submit]`
16. Verifikasi toast sukses "Success, unit has been added to stock."
17. Verifikasi unit `SN-DU-0001-{runId}-252` berstatus `Available` pada Tab Available
18. Verifikasi Registered By unit itu `{shortNameDu}`

### TC-AC-ACHS-112: Distributor dengan Local Registration aktif

19. Logout, lalu login sebagai Distributor `{emailCakra}` (`Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`)
20. Buka Hardware > Stock lewat sidebar
21. Ketik Search `{skuFx}`, tekan Enter
22. Klik `(⋯)` pada baris SKU `{skuFx}`
23. Klik opsi `Add Stock`
24. Ketik `SN-DIST-0001-{runId}-252`
25. Klik `[Submit]`
26. Verifikasi toast sukses "Success, unit has been added to stock."
27. Verifikasi Tab Available aktor Distributor memuat `SN-DIST-0001-{runId}-252` dengan Registered By `{shortNameCakra}`
28. Tunggu aksi selesai, lalu logout dan login sebagai Total Control `{emailTc}` (`Spectra.env.AC_TC_PASSWORD`)
29. Buka Hardware > Stock lewat sidebar
30. Ketik Search `{skuFx}`, tekan Enter
31. Klik row action `Detail` pada baris SKU `{skuFx}`
32. Ketik Search `SN-DIST-0001-{runId}-252` pada Tab Available, tekan Enter
33. Verifikasi Principal melihat unit `SN-DIST-0001-{runId}-252` di Tab Available
34. Logout, lalu login sebagai Distributor `{emailMitra}` (`Spectra.env.AC_DISTRIBUTOR_MITRA_PASSWORD`)
35. Buka Hardware > Stock lewat sidebar
36. Ketik Search `{skuFx}`, tekan Enter
37. Klik row action `Detail` pada baris SKU `{skuFx}`
38. Verifikasi Tab Available akun `{fullNameMitra}` menampilkan sedikitnya satu baris
39. Ketik Search `SN-DIST-0001-{runId}-252` pada Tab Available, tekan Enter
40. Verifikasi akun `{fullNameMitra}` tidak melihat unit `SN-DIST-0001-{runId}-252`: hasil Search menampilkan empty state `No results found`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-110, 111, 112). Tidak ada TC hanya-BE di spec ini.
- Spec Role Matrix positif varian A (bagian 3a) ditulis per blok role karena langkah tiap role tidak identik (blok Distributor memuat pengamat Principal dan Distributor lain) dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 11, 21, 30, 36), logout dan login pada Step ganti akun (langkah 9, 19, 28, 34), buka Hardware > Stock lewat sidebar (langkah 10, 20, 29, 35), dan Search di Tab Available (langkah 32, 39). Langkah 28 memuat "Tunggu aksi selesai" sebelum ganti akun (bagian 8b butir 8).
- Total Control tidak punya blok sendiri sebagai pelaku Add Stock: TC-111 menuliskan "Default User dan Total Control berhasil" pada judul, sedangkan Expected hanya memuat unit dengan Registered By `{shortNameDu}`; Add Stock oleh Total Control diuji di spec 249 (TC-80).
- Spec di atas smell 35 langkah (40 langkah). Alasan: tiga TC Role Matrix positif satu kelas yang berjalan per blok role; tiap blok butuh login ulang, Search, dan pembuatan unit sendiri sehingga dipecah per role hanya menggandakan Step ganti akun.
- Kombinasi role x aksi tanpa TC sumber tidak dikarang; role Additional Approver Create dicakup spec Sync (TC-143, 144).
- Temuan untuk QA:
  - Judul TC-111 menyebut Total Control, Expected hanya Default User (lihat atas).
  - Nama env password Create-Only, Default User, Distributor Cakra, dan Distributor Mitra tidak tertulis di TC; disediakan tim FE.
  - TC-112 Post Condition ("Entri Activity Log `Add Stock` dan System Log Detail User {fullNameCakra}") tidak punya langkah observasi dan tidak diasersi.
  - TC-112 butir d ("Distributor akun `{fullNameMitra}` tidak melihat unit tersebut") tidak menyebut Pre-setup akun Mitra untuk SKU {skuFx}; spec memakai akun Pre-setup #11 yang memiliki tiga unit Available pada SKU itu (Pre-setup #27) sebagai anchor.
