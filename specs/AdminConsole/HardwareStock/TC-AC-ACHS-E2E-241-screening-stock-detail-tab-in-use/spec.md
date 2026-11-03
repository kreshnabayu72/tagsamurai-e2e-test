---
id: TC-AC-ACHS-E2E-241-screening-stock-detail-tab-in-use
title: "Screening Stock Detail Tab In Use: Layout, Badge Status, Row Action Read-Only, dan Status Null"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-42
  - TC-AC-ACHS-43
  - TC-AC-ACHS-44
  - TC-AC-ACHS-45
coverage:
  web: automated
---

# Screening Stock Detail Tab In Use: Layout, Badge Status, Row Action Read-Only, dan Status Null

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): SKU `{skuLong}` (25 | 18 | 7) dengan 7 unit In Use N = 1 sampai 7 (Tabel F: Status Damaged, Active, Missing, Active, Active, Damaged, Active; empat Client berbeda `{clientInUse1}`, `{clientInUse4}`, `{clientInUse6}`, `{clientInUse7}`; Registered At dan Activated At unit N = 1 pada Tabel F) (Pre-setup No 18). General Settings baseline Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm` (Pre-setup No 15). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Data seed milik spec (Pre-setup No 18b; S-06): satu unit In Use SKU `{skuLong}` dengan Client Reported Condition null (data lama), Serial Number bersuffix `SN-NULL-{runId}-241` (data buatan spec, S-12), Client `{clientInUse1}` (Client unit N = 1). Unit ini menambah unit In Use kedelapan sehingga tidak boleh ada saat TC-42 mengasersi `Showing 1–7 of 7 entries`; karena itu dimuat langkah 24 tepat sebelum TC-45 dan dihapus langkah 32 sesudahnya, bukan di hook `before`. Cadangan cleanup (R-08): hook `after` spec ini menghapus unit `SN-NULL-{runId}-241` bila masih ada (idempotent, dilewati bila sudah dihapus langkah 32). Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat Temuan untuk QA).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{snInUse1}` | #18 Tabel F baris N = 1 | Serial Number unit In Use berstatus Damaged | `Fixture.hardwareStock.p18.f[1].serialNumber` |
| `{snInUse2}` | #18 Tabel F baris N = 2 | Serial Number unit In Use berstatus Active | `Fixture.hardwareStock.p18.f[2].serialNumber` |
| `{snInUse3}` | #18 Tabel F baris N = 3 | Serial Number unit In Use berstatus Missing | `Fixture.hardwareStock.p18.f[3].serialNumber` |
| `{clientInUse1}` | #18 Tabel F baris N = 1 | Client unit In Use N = 1 | `Fixture.hardwareStock.p18.f[1].client` |
| `{clientInUse4}` | #18 Tabel F baris N = 4 | Client unit In Use N = 4 | `Fixture.hardwareStock.p18.f[4].client` |
| `{clientInUse6}` | #18 Tabel F baris N = 6 | Client unit In Use N = 6 | `Fixture.hardwareStock.p18.f[6].client` |
| `{clientInUse7}` | #18 Tabel F baris N = 7 | Client unit In Use N = 7 | `Fixture.hardwareStock.p18.f[7].client` |
| `{registeredAtInUse1}` | #18 Tabel F baris N = 1 | Registered At unit In Use N = 1 (format baseline #15) | `Fixture.hardwareStock.p18.f[1].registeredAt` |
| `{activatedAtInUse1}` | #18 Tabel F baris N = 1 | Activated At unit In Use N = 1 (format baseline #15) | `Fixture.hardwareStock.p18.f[1].activatedAt` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-42: Screening Tab In Use SKU Long Range

1. Klik `(⋯)` pada baris `{skuLong}`, klik row action `Detail`
2. Klik Tab `In Use`
3. Verifikasi Breadcrumb `Hardware > Stock > Detail`
4. Verifikasi SKU Info Header Device Name dan SKU `{skuLong}` sama dengan Tab Available
5. Verifikasi Summary bar `Total Registered 25 | Available 18 | In Use 7` sama dengan Tab Available
6. Verifikasi Tabs `Available | In Use (aktif)`
7. Verifikasi Table Tools `Search | Filter | Download`
8. Verifikasi Table Tools tanpa `[Event Log]` dan tanpa `[Add Stock]`
9. Verifikasi tidak ada Banner Waiting for Approval
10. Verifikasi kolom `Device Name (sortable) | Serial Number (sortable) | Client (sortable) | Status (sortable) | Registered At (sortable) | Registered By (sortable) | Activated At (sortable) | Min Power (sortable) | Max Power (sortable) | Current Power (sortable) | Column Visibility (⋯) (unsortable)`
11. Verifikasi tidak ada kolom Identifier Type, Identifier Value, Activation Method, maupun Subscription
12. Verifikasi pagination default 10 baris per halaman
13. Verifikasi info pagination `Showing 1–7 of 7 entries`

### TC-AC-ACHS-43: Isi sel Tab In Use

14. Verifikasi badge Status `Damaged` severity danger pada baris `{snInUse1}`
15. Verifikasi badge Status `Active` severity success pada baris `{snInUse2}`
16. Verifikasi badge Status `Missing` severity danger pada baris `{snInUse3}`
17. Verifikasi kolom Client menampilkan empat Client berbeda `{clientInUse1}`, `{clientInUse4}`, `{clientInUse6}`, `{clientInUse7}` sesuai Tabel F
18. Verifikasi baris `{snInUse1}` menampilkan Registered At `{registeredAtInUse1}` dan Activated At `{activatedAtInUse1}` dalam format General Settings baseline (Pre-setup No 15)

### TC-AC-ACHS-44: Tab In Use read-only, row action hanya Hardware Log

19. Klik `(⋯)` pada baris `{snInUse1}` (Damaged)
20. Verifikasi overlay hanya berisi `Hardware Log`
21. Verifikasi overlay tanpa `Delete`, `Edit`, maupun aksi Recall
22. Tutup overlay dengan `Esc`
23. Verifikasi unit `{snInUse1}` berstatus Damaged tetap berada di Tab In Use

### TC-AC-ACHS-45: Status null tampil `—` dan tidak ikut opsi filter Status

24. Muat unit In Use dengan Client Reported Condition null (Pre-setup No 18b) lewat seeding
25. Tekan F5
26. Ketik Search `SN-NULL-{runId}-241`, tekan Enter
27. Verifikasi sel Status unit ber-Client Reported Condition null tampil `—`
28. Klik `(←)` pada kotak Search
29. Klik icon Filter, buka dropdown Status pada Filter Panel
30. Verifikasi opsi Status hanya `Active`, `Damaged`, `Missing`
31. Tutup Filter Panel dengan `Esc`
32. Hapus unit seed Client Reported Condition null lewat seeding

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-42, 43, 44, 45). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 22, 28, dan 31 (menutup overlay, membersihkan Search, dan menutup Filter Panel, S-09), langkah 24, 25, dan 32 (memuat dan menghapus unit seed sesaat dan menyegarkan data), langkah 26 (Search untuk menemukan baris target, R-16). TC-45 diletakkan terakhir karena seed menambah unit In Use kedelapan, sedangkan TC-42 mengasersi `Showing 1–7 of 7 entries`.
- Langkah 14 sampai 16 mengasersi satu baris contoh per nilai Status dari Tabel F, bukan seluruh baris.
- Temuan untuk QA:
  - Pre-setup No 18b menyebut "satu unit ber-kondisi null" tanpa Serial Number dan tanpa memasukkannya ke Tabel F (7 unit dengan Status terisi); spec memperlakukannya sebagai unit tambahan (seed sesaat) bukan salah satu dari 7 unit. Bila yang dimaksud adalah salah satu dari 7 unit, hitungan `7` pada TC-42 dan nilai Status Tabel F saling bertentangan.
  - Mekanisme seeding Client Reported Condition null (data lama) tidak didefinisikan di TC, PRD, atau LLD yang dibaca; diminta dari tim FE/BE. Serial Number seed bersuffix `SN-NULL-{runId}-241` dipilih spec (S-12).
  - TC-43 Expected c ("mengikuti format General Settings") tidak menyebut nilai; spec mengasersi nilai Tabel F pada format baseline No 15.
  - Population Stock tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites (nilai persis dari Tabel A dan F TC) sehingga tidak memerlukan pengecualian S-12. Serial Number seed `SN-NULL-{runId}-241` adalah data buatan spec.
