---
id: TC-AC-ACHS-E2E-010-screening-approvals-tab-active-history-dan-isi-sel
title: "Screening Approvals Hardware Stock Tab Active dan Tab History, Isi Sel, dan Hover Nama Lengkap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-51
  - TC-AC-ACHS-52
  - TC-AC-ACHS-53
  - TC-AC-ACHS-593
coverage:
  web: automated
---

# Screening Approvals Hardware Stock Tab Active dan Tab History, Isi Sel, dan Hover Nama Lengkap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`), anggota approver pool. Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Approvals Tab Active 12 Subject pending (Tabel C; baris pertama Requested At terlama; Register Duplicate milik Distributor Pre-setup No 12; Activation Collision tanpa SKU) dan Tab History 12 Subject terputus (Tabel D; Approver `System`, baris Canceled, Approver user Pre-setup No 1) (Pre-setup No 21, 22); unit In Use N = 7 Registered By user Pre-setup No 10 (Tabel F, No 18). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini; baris Subject dikenali lewat Matched Identifier bernilai penuh):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p21.c[1].matchedIdentifier}` | No 21, Tabel C baris 1 | Matched Identifier Subject Active dengan Requested At terlama (Activation Collision) | `Fixture.hardwareStock.p21.c[1].matchedIdentifier` |
  | `{Fixture.hardwareStock.p21.c[10].matchedIdentifier}` | No 21, Tabel C baris 10 | Matched Identifier Subject Register Duplicate Category `Handheld Reader - Long Range`, Registrant dan Requested By Distributor No 12 | `Fixture.hardwareStock.p21.c[10].matchedIdentifier` |
  | `{Fixture.hardwareStock.p21.c[10].existingRecord}` | No 21, Tabel C baris 10 | Existing Record Subject Register Duplicate (Available, Registrant Distributor No 12) | `Fixture.hardwareStock.p21.c[10].existingRecord` |
  | `{Fixture.hardwareStock.p21.c[10].requestedBy}` | No 21, Tabel C baris 10 | Requested By Subject Register Duplicate (Distributor No 12 `(Distributor)`) | `Fixture.hardwareStock.p21.c[10].requestedBy` |
  | `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` | No 21, Tabel C baris 9 | Matched Identifier Subject Activation Collision tanpa SKU | `Fixture.hardwareStock.p21.c[9].matchedIdentifier` |
  | `{Fixture.hardwareStock.p21.c[9].existingRecord}` | No 21, Tabel C baris 9 | Existing Record Subject Activation Collision tanpa SKU (Active, Client di bawah Partner No 14) | `Fixture.hardwareStock.p21.c[9].existingRecord` |
  | `{Fixture.hardwareStock.p21.c[9].requestedBy}` | No 21, Tabel C baris 9 | Requested By Subject Activation Collision tanpa SKU (Client `UD` No 23 `(Client)`) | `Fixture.hardwareStock.p21.c[9].requestedBy` |
  | `{Fixture.hardwareStock.p21.c[9].deviceNameSku}` | No 21, Tabel C baris 9 | Device Name (SKU) Subject Activation Collision tanpa SKU (SKU `(—)`) | `Fixture.hardwareStock.p21.c[9].deviceNameSku` |
  | `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}` | No 22, Tabel D baris 1 | Matched Identifier Subject History Canceled, Approver `—` | `Fixture.hardwareStock.p22.d[1].matchedIdentifier` |
  | `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}` | No 22, Tabel D baris 2 | Matched Identifier Subject History Approved oleh user Pre-setup No 1 dengan Approval Note berisi teks | `Fixture.hardwareStock.p22.d[2].matchedIdentifier` |
  | `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}` | No 22, Tabel D baris 7 | Matched Identifier Subject History Approved oleh `System` (Approval Note `—`) | `Fixture.hardwareStock.p22.d[7].matchedIdentifier` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p18.f[7].deviceName}` | No 18, Tabel F baris 7 | Device Name unit In Use SKU Long Range (N = 7) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}` | No 10 | singkatan tampil user Distributor No 10 | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.fullName}` | No 10 | nama lengkap user Distributor No 10 (tampil pada hover) | `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |
  | `{Fixture.hardwareStock.account.p01.totalControl.shortName}` | No 1 | singkatan tampil `[Nama Depan] [Inisial]` user akun Total Control | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | `{Fixture.hardwareStock.account.p01.totalControl.fullName}` | No 1 | nama lengkap user akun Total Control | `Fixture.hardwareStock.account.p01.totalControl.fullName` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List dan Approvals Hardware Stock (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-51: Screening Approvals Tab Active

1. Klik menu Approvals > Hardware Stock di sidebar
2. Verifikasi Breadcrumb `Approvals > Hardware Stock`
3. Verifikasi Tabs `Active (aktif) | History`
4. Verifikasi Table Tools `Search | Filter | Download`
5. Verifikasi kolom `Type (sortable) | Device Name (SKU) (sortable) | Category (sortable) | Matched Identifier (sortable) | Existing Record (sortable) | Requested By (sortable) | Requested At (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi urutan default Requested At terlama di atas dengan baris pertama `{Fixture.hardwareStock.p21.c[1].matchedIdentifier}`
7. Verifikasi row action `Review` tersedia pada baris
8. Verifikasi pagination default 10 baris per halaman
9. Verifikasi info pagination `Showing 1–10 of 12 entries`

### TC-AC-ACHS-52: Screening Approvals Tab History

10. Klik Tab `History`
11. Verifikasi Breadcrumb `Approvals > Hardware Stock`
12. Verifikasi Tabs `Active | History (aktif)`
13. Verifikasi Table Tools `Search | Filter | Download`
14. Verifikasi kolom `Type (sortable) | Device Name (SKU) (sortable) | Category (sortable) | Matched Identifier (sortable) | Existing Record (sortable) | Requested By (sortable) | Approval (sortable) | Approver (sortable) | Requested At (sortable) | Resolved At (sortable) | Column Visibility (⋯) (unsortable)`
15. Verifikasi urutan default Resolved At terbaru di atas
16. Verifikasi row action `Detail` tersedia pada baris
17. Verifikasi pagination default 10 baris per halaman
18. Verifikasi info pagination `Showing 1–10 of 12 entries`

### TC-AC-ACHS-53: Isi sel Approvals

19. Klik Tab `Active`
20. Verifikasi baris `{Fixture.hardwareStock.p21.c[10].matchedIdentifier}` menampilkan Type `Register Duplicate` sebagai badge secondary
21. Verifikasi baris `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` menampilkan Type `Activation Collision` sebagai badge warning
22. Verifikasi baris `{Fixture.hardwareStock.p21.c[10].matchedIdentifier}` menampilkan Existing Record `{Fixture.hardwareStock.p21.c[10].existingRecord}`
23. Verifikasi baris `{Fixture.hardwareStock.p21.c[10].matchedIdentifier}` menampilkan Requested By `{Fixture.hardwareStock.p21.c[10].requestedBy}`
24. Verifikasi baris `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` menampilkan Existing Record `{Fixture.hardwareStock.p21.c[9].existingRecord}`
25. Verifikasi baris `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` menampilkan Requested By `{Fixture.hardwareStock.p21.c[9].requestedBy}`
26. Verifikasi baris `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` menampilkan Device Name (SKU) `{Fixture.hardwareStock.p21.c[9].deviceNameSku}`
27. Verifikasi baris `{Fixture.hardwareStock.p21.c[9].matchedIdentifier}` menampilkan Category `—`
28. Verifikasi baris `{Fixture.hardwareStock.p21.c[10].matchedIdentifier}` menampilkan Category `Handheld Reader - Long Range`
29. Klik Tab `History`
30. Verifikasi baris `{Fixture.hardwareStock.p22.d[7].matchedIdentifier}` menampilkan Approver `System`
31. Verifikasi baris `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}` menampilkan Approval `Canceled`
32. Verifikasi baris `{Fixture.hardwareStock.p22.d[1].matchedIdentifier}` menampilkan Approver `—`

### TC-AC-ACHS-593: Hover nama lengkap Registered By Tab In Use dan Approver Tab History

33. Klik menu Hardware > Stock di sidebar
34. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
35. Klik Tab `In Use`
36. Hover nilai Registered By `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}` pada baris `{Fixture.hardwareStock.p18.f[7].deviceName}`
37. Verifikasi hover menampilkan nama lengkap `{Fixture.hardwareStock.account.p10.distributorCakra.fullName}`
38. Verifikasi teks sel Registered By tetap `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}`
39. Klik menu Approvals > Hardware Stock di sidebar
40. Klik Tab `History`
41. Hover nilai Approver `{Fixture.hardwareStock.account.p01.totalControl.shortName}` pada baris `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}`
42. Verifikasi hover menampilkan nama lengkap `{Fixture.hardwareStock.account.p01.totalControl.fullName}`
43. Verifikasi teks sel Approver tetap `{Fixture.hardwareStock.account.p01.totalControl.shortName}`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-51, 52, 53, 593). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 19 (kembali ke Tab Active sebelum TC-53), langkah 33 sampai 35 dan 39 (berpindah antar surface untuk TC-593; Expected tidak menyebut kembali ke Approvals).
- TC-53 hanya mengasersi baris contoh per variasi Type, Existing Record, dan Approver, bukan seluruh 12 baris.
- Spec di atas smell 35 langkah (43 langkah). Alasan: seluruh blok adalah screening Approvals yang berbagi Population yang sama (Tabel C dan D), keempat TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-51 dan TC-52 Expected menyebut "row action `Review`" dan "`Detail`" tanpa menyebut baris yang diperiksa; spec mengasersi ketersediaan row action pada baris.
  - TC-593 Expected c ("teks sel tetap `[First Name] [Last Initial]` sebelum dan sesudah hover") diasersi sesudah hover saja (langkah 38 dan 43); TC tidak memberi langkah pengamatan sebelum hover.
  - Population Approvals tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites (nilai persis dari Tabel C, D, F TC) sehingga tidak memerlukan pengecualian S-12. Nilai UI (Type, Approval, Approver `System`, Category generik, `—`) dipertahankan sebagai salinan UI. Rujukan `{Fixture.hardwareStock.account.p01.totalControl.shortName}` dan `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}` adalah singkatan tampil user Pre-setup No 1 dan No 10 menurut format `[First Name] [Last Initial]`.
