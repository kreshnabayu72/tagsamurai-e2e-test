---
id: TC-AC-ACHS-E2E-278-hardware-log-event-registered-waiting-approved
title: "Hardware Log: Event Registered, Waiting for Approval, dan Approved"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-546
  - TC-AC-ACHS-547
  - TC-AC-ACHS-548
  - TC-AC-ACHS-549
  - TC-AC-ACHS-550
coverage:
  web: automated
---

# Hardware Log: Event Registered, Waiting for Approval, dan Approved

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-550): Additional Approver dengan capability Create `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` (Pre-setup #6, `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after` (juga untuk `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #22 dan #27; suite serial `parallel: false` (lihat suite.md).
- Aksi sumber (dipakai sebagai precondition TC, dijalankan hook `before` lewat sesi API aktor, kemampuan disediakan tim BE/FE, tidak diasersi): Add Stock manual unit `SN-ZEBRA-FX9600-{runId}-278M` pada SKU `Fixture.hardwareStock.p16.a[3].sku` oleh `Fixture.hardwareStock.account.p01.totalControl.fullName` (TC-80); Add Stock Sync unit valid `SN-ZEBRA-RFD40-{runId}-278S` pada SKU `Fixture.hardwareStock.p16.a[4].sku` oleh `Fixture.hardwareStock.account.p01.totalControl.fullName` (TC-135); bypass E2a unit `SN-ZEBRA-RFD40-{runId}-278B` oleh `Fixture.hardwareStock.account.p01.totalControl.fullName` (TC-140); Approve Register Duplicate unit Waiting for Approval milik spec `SN-ZEBRA-RFD40-{runId}-278W` (Registered By Distributor Pre-setup #12) dengan Approval Note `Dokumen pengadaan sudah diperiksa` (TC-180); auto-approve E3 unit milik spec `SN-ZEBRA-RFD40-{runId}-278E` pada SKU `Fixture.hardwareStock.p16.a[4].sku` oleh `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` (TC-144) dengan fixture pool approver Pre-setup #28 (hanya `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName`) disetel selama pembuatan unit lalu dipulihkan oleh hook sebelum langkah UI dan di `after`.
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai read-only: SKU `Fixture.hardwareStock.p16.a[3].sku` dan `Fixture.hardwareStock.p16.a[4].sku`, serta Registered By `Fixture.hardwareStock.account.p12.distributorSumberJaya.shortName` (Pre-setup #12).
- Data milik spec (S-06, S-12): unit `SN-ZEBRA-FX9600-{runId}-278M`, `SN-ZEBRA-RFD40-{runId}-278S`, `SN-ZEBRA-RFD40-{runId}-278B`, unit Waiting for Approval beserta Subject Register Duplicate `SN-ZEBRA-RFD40-{runId}-278W` (struktur sama dengan unit Pre-setup #17 Tabel E baris N = 28 dan Subject #21 Tabel C baris ke-10, requester Distributor #12), dan unit E3 `SN-ZEBRA-RFD40-{runId}-278E`. Seeding oleh hook `before` (sesi API aktor, disediakan tim BE/FE tanpa endpoint karangan; kunci fixture-nya belum ada). Data Pre-setup tidak diubah spec ini.
- Cleanup (R-08): hook `after` menghapus secara idempotent unit dan Subject milik spec di atas (`{runId}-278M`, `{runId}-278S`, `{runId}-278B`, `{runId}-278W`, `{runId}-278E`) dan memulihkan pool approver Pre-setup #28 ke keadaan awal. Entri Hardware Log dan Activity Log adalah audit trail permanen dan tidak dihapus.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `abbrDistC` | #12 | Singkatan `[Nama Depan] [Inisial]` user akun #12 | `Fixture.hardwareStock.account.p12.distributorSumberJaya.shortName` |
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snWfa` | data milik spec (struktur #17 Tabel E baris N = 28, #21 Tabel C baris ke-10) | Serial Number unit Waiting for Approval milik spec; sekaligus Matched Identifier Subject Register Duplicate pending (requester Distributor #12) | `SN-ZEBRA-RFD40-{runId}-278W` |
| `snE3` | data milik spec | Serial Number unit hasil auto-approve E3 milik spec pada `skuLong` | `SN-ZEBRA-RFD40-{runId}-278E` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `akun additionalApproverCreatePrincipal` | #6 | Akun Additional Approver dengan capability Create | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` |

## Test Steps

### TC-AC-ACHS-546: Registered Source Manual

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[3].sku`
2. Klik `(⋯)` pada baris unit hasil Add Stock manual `SN-ZEBRA-FX9600-{runId}-278M`, lalu klik `Hardware Log`
3. Hover pelaku `Fixture.hardwareStock.account.p01.totalControl.shortName` pada judul entri
4. Verifikasi judul entri `Hardware Registered by 👤 Fixture.hardwareStock.account.p01.totalControl.shortName` dengan pelaku berkomponen user (ikon)
5. Verifikasi hover pelaku menampilkan nama lengkap `Fixture.hardwareStock.account.p01.totalControl.fullName`
6. Verifikasi entri memuat Date & Time
7. Verifikasi Description `Source: Manual`
8. Klik `[✕]`

### TC-AC-ACHS-547: Registered Source Sync

9. Klik segmen breadcrumb `Stock`, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
10. Ketik Search `{runId}-278S`, tekan Enter
11. Klik `(⋯)` pada baris hasil `SN-ZEBRA-RFD40-{runId}-278S`, lalu klik `Hardware Log`
12. Verifikasi entri `Hardware Registered by 👤 Fixture.hardwareStock.account.p01.totalControl.shortName` dengan Description `Source: Sync`
13. Verifikasi entri tidak memuat baris `Approval`
14. Klik `[✕]`

### TC-AC-ACHS-548: Registered hasil bypass E2a

15. Ganti isi kotak search dengan `{runId}-278B`, tekan Enter
16. Klik `(⋯)` pada baris hasil `SN-ZEBRA-RFD40-{runId}-278B`, lalu klik `Hardware Log`
17. Verifikasi entri `Hardware Registered by 👤 Fixture.hardwareStock.account.p01.totalControl.shortName` dengan Description `Source: Sync`
18. Verifikasi Description memuat `Approval: Bypass`
19. Klik `[✕]`

### TC-AC-ACHS-549: Waiting for Approval dan Approved

20. Ganti isi kotak search dengan `{runId}-278W`, tekan Enter
21. Klik `(⋯)` pada baris hasil `SN-ZEBRA-RFD40-{runId}-278W`, lalu klik `Hardware Log`
22. Verifikasi entri teratas `Hardware Approved by 👤 Fixture.hardwareStock.account.p01.totalControl.shortName` dengan Description `Approval Note: Dokumen pengadaan sudah diperiksa`
23. Verifikasi di bawahnya `Hardware Sent for Approval by 👤 Fixture.hardwareStock.account.p12.distributorSumberJaya.shortName` dengan Description `Source: Sync`
24. Klik `[✕]`
25. Logout, lalu login sebagai `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName`; tunggu aksi selesai

### TC-AC-ACHS-550: Approved auto-approve E3

26. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
27. Ketik Search `SN-ZEBRA-RFD40-{runId}-278E`, tekan Enter
28. Klik `(⋯)` pada baris hasil `SN-ZEBRA-RFD40-{runId}-278E`, lalu klik `Hardware Log`
29. Verifikasi judul entri `Hardware Approved by System`
30. Hover `System` pada judul entri
31. Verifikasi `System` tampil teks biasa tanpa ikon user dan tanpa tooltip

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-546 sampai TC-550). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 3, 8, 9, 11, 14, 16, 19, 21, 24, 26, 28, 30 (navigasi, hover, dan membuka/menutup popup; langkah 30 hover `System` pada judul entri agar absence tooltip di langkah 31 benar-benar diuji), 10, 15, 20, 27 (Search untuk menemukan baris target, R-16), 25 (ganti akun).
- Pencarian memakai suffix `{runId}-278S`, `{runId}-278B`, dan `{runId}-278W` karena Serial Number hasil seed bersuffix menggantikan nama literal TC (`100051`, `100091`) dan unit Pre-setup yang diputuskan.
- Judul entri berikut ikon user (langkah 4) dan hover nama lengkap (langkah 5) ditulis sebagai dua `Verifikasi` terpisah; hover dilakukan di langkah 3.
- Temuan untuk QA:
  - TC-550 langkah 2 membuka Detail SKU `Fixture.hardwareStock.p16.a[4].sku` sementara Pre-setup dinamis (TC-144) menyebut unit E3 milik SKU Handheld Reader lain; spec memakai SKU `Fixture.hardwareStock.p16.a[4].sku` sesuai langkah TC dan mencatat bahwa SKU unit hasil E3 tidak dinyatakan tegas.
  - TC-550 tidak menyebut Serial Number unit E3 di langkah; spec memakai unit E3 milik spec `SN-ZEBRA-RFD40-{runId}-278E` (data Pre-setup #24 tidak diubah, S-06).
  - TC-547 dan TC-548 menyebut Serial Number literal `SN-ZEBRA-RFD40-100051` dan `-100091`; spec memakai Serial Number bersuffix (S-12).
  - Pembuatan fixture pool approver Pre-setup #28 (hanya `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName`) menonaktifkan Total Control lain sementara; pemulihan pool dijamin tim BE/FE (suite serial).
  - Seeding unit dan Subject milik spec (`{runId}-278M`, `-278S`, `-278B`, `-278W`, `-278E`) beserta cleanup `after` tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE dan kunci fixture-nya belum ada.
