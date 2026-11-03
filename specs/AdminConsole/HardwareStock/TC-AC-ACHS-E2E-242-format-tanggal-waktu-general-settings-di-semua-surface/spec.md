---
id: TC-AC-ACHS-E2E-242-format-tanggal-waktu-general-settings-di-semua-surface
title: "Format Tanggal dan Waktu General Settings di Semua Surface Hardware Stock"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-567
  - TC-AC-ACHS-568
  - TC-AC-ACHS-569
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings di Semua Surface Hardware Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- State global yang diubah: General Settings entitas Principal diubah dari baseline Pre-setup No 15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`, Timezone `Asia/Jakarta (UTC+07:00)`) ke Pre-setup No 15b (Date Format `DD/MM/YYYY`, Time Format 12-hour `hh:mm A`, Timezone `Asia/Makassar (UTC+08:00)`). Pelaku dan mekanisme mengubah General Settings tidak disebut TC; kemampuan disediakan tim FE/BE. Pemulihan ke No 15 dilakukan di langkah terakhir dan di hook `after` spec ini (tetap jalan walau spec gagal di tengah). Suite berjalan serial.
- Data Pre-setup (hanya dibaca; nilai persis dibaca dari Tabel A sampai F TC): Last Updated `{skuLong}` `12 Jun 2026, 16:05`; unit `{deviceNameAvail10}` Registered At `10 May 2026, 09:00` dan `{deviceNameInUse1}` Registered At `20 Apr 2026, 09:00` serta Activated At `02 May 2026, 09:00`; Event Log baris `Delete Stock` oleh user Pre-setup No 1 (`{shortNameTc}`) `24 May 2026, 10:55`; Hardware Log `{deviceNameAvail10}` entri terbaru `Hardware Registered by {shortNameMitra}`; Approvals Tab Active baris pertama `09 Jun 2026, 12:00`, Subject `{subjectRdLong}` Requested at `18 Jun 2026, 09:15`, Tab History baris pertama Resolved At `20 Jun 2026, 09:10` (Pre-setup No 15, 17, 18, 20, 21, 22; semua nilai dalam `Asia/Jakarta (UTC+07:00)`). Nilai yang diharapkan pada format baru diturunkan dengan menambah satu jam (selisih Asia/Jakarta ke Asia/Makassar). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Rentang tanggal Filter Panel adalah pilihan spec (5 Juni 2026 sampai 20 Juni 2026 pada Last Updated dan 1 Mei 2026 sampai 31 Mei 2026 pada Registered At dan Activated At).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{deviceNameAvail10}` | #17 Tabel E baris N = 10 | Device Name unit Available pertama SKU Long Range | `Fixture.hardwareStock.p17.e[10].deviceName` |
| `{deviceNameInUse1}` | #18 Tabel F baris N = 1 | Device Name unit In Use N = 1 | `Fixture.hardwareStock.p18.f[1].deviceName` |
| `{subjectRdLong}` | #21 Tabel C baris 10 | Matched Identifier Subject Register Duplicate Category Handheld Reader - Long Range, Existing Record milik Distributor Pre-setup #12, Requested At 18 Jun 2026 | `Fixture.hardwareStock.p21.c[10].matchedIdentifier` |
| `{shortNameTc}` | #1 | nama pendek akun Total Control (kolom Registered By dan Modified By) | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `{shortNameMitra}` | #11 | nama pendek user Distributor PT Mitra Niaga | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List dan Approvals Hardware Stock (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Persiapan

1. Ubah General Settings: Date Format `DD/MM/YYYY`, Time Format 12-hour `hh:mm A`, Timezone `Asia/Makassar (UTC+08:00)`

### TC-AC-ACHS-567: Tabel utama dan Filter Panel

2. Klik menu Hardware > Stock di sidebar
3. Verifikasi Last Updated baris `{skuLong}` tampil `12/06/2026, 05:05 PM`
4. Klik icon Filter, pilih rentang tanggal 05/06/2026 sampai 20/06/2026 pada Last Updated
5. Verifikasi teks tanggal terpilih di kotak input date range picker Last Updated memakai format `DD/MM/YYYY`
6. Tutup Filter Panel dengan `Esc`
7. Klik `(⋯)` pada baris `{skuLong}`, klik row action `Detail`
8. Ketik Search Device Name `{deviceNameAvail10}`, tekan Enter
9. Verifikasi Registered At baris `{deviceNameAvail10}` tampil `10/05/2026, 10:00 AM`
10. Klik icon Filter, pilih rentang tanggal 01/05/2026 sampai 31/05/2026 pada Registered At
11. Verifikasi teks tanggal terpilih di kotak input date range picker Registered At Tab Available memakai format `DD/MM/YYYY`
12. Tutup Filter Panel dengan `Esc`
13. Klik `(←)` pada kotak Search
14. Klik Tab `In Use`
15. Verifikasi Registered At baris `{deviceNameInUse1}` tampil `20/04/2026, 10:00 AM`
16. Verifikasi Activated At baris `{deviceNameInUse1}` tampil `02/05/2026, 10:00 AM`
17. Klik icon Filter, pilih rentang tanggal 01/05/2026 sampai 31/05/2026 pada Activated At
18. Verifikasi teks tanggal terpilih di kotak input date range picker Activated At memakai format `DD/MM/YYYY`
19. Tutup Filter Panel dengan `Esc`

### TC-AC-ACHS-568: Popup Event Log dan Hardware Log

20. Klik Tab `Available`
21. Klik icon `[Event Log]`
22. Verifikasi kolom Date baris `Delete Stock` oleh `{shortNameTc}` tampil `24/05/2026, 11:55 AM`
23. Tutup popup Event Log dengan `Esc`
24. Ketik Search Device Name `{deviceNameAvail10}`, tekan Enter
25. Klik `(⋯)` pada baris `{deviceNameAvail10}`, klik `Hardware Log`
26. Verifikasi Date & Time entri `Hardware Registered by {shortNameMitra}` memakai format `DD/MM/YYYY`, jam 12-hour `hh:mm A`, dan zona waktu `Asia/Makassar (UTC+08:00)`
27. Tutup popup Hardware Log dengan `Esc`
28. Klik `(←)` pada kotak Search

### TC-AC-ACHS-569: Approvals dan Dialog Detail Approval

29. Klik menu Approvals > Hardware Stock di sidebar
30. Verifikasi Requested At baris pertama Tab Active tampil `09/06/2026, 01:00 PM`
31. Klik Tab `History`
32. Verifikasi Resolved At baris pertama Tab History tampil `20/06/2026, 10:10 AM`
33. Klik Tab `Active`
34. Klik `[Review]` pada baris dengan Matched Identifier `{subjectRdLong}`
35. Verifikasi Requested at pada blok New Request tampil `18/06/2026, 10:15 AM`
36. Verifikasi Registered at dan Synced at pada blok Existing Record dan New Request memakai format `DD/MM/YYYY`, jam 12-hour `hh:mm A`, dan zona waktu `Asia/Makassar (UTC+08:00)`
37. Klik `[Cancel]` pada dialog Detail Approval

### Pemulihan

38. Pulihkan General Settings ke Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`, Timezone `Asia/Jakarta (UTC+07:00)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-567, 568, 569). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 38 (mengubah dan memulihkan state global General Settings), langkah 6, 12, 19, 23, 27 (menutup Filter Panel dan popup), langkah 13 dan 28 (membersihkan Search), langkah 8 dan 24 (Search untuk menemukan baris target, R-16), langkah 14, 20, dan 33 (berpindah tab).
- Spec di atas smell 35 langkah (38 langkah). Alasan: seluruh blok adalah asersi format General Settings yang sama pada tiga kelompok surface, ketiga TC berdiri sendiri, dan satu perubahan state global dipakai bersama sehingga memecahnya menambah dua kali perubahan dan pemulihan General Settings.
- Spec ini mengubah state global (General Settings); P-5 butir (b) tidak dipakai karena kelas h tidak dilibatkan (format tanggal bukan state tenant).
- Temuan untuk QA:
  - Identitas Population (SKU, unit, Subject, user) tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup sehingga tidak memerlukan pengecualian S-12. Nilai tanggal dan waktu Pre-setup (Tabel A sampai F) beserta hasil konversi ke format dan zona waktu baru dipertahankan sebagai nilai asersi inti TC-567 sampai TC-569, bukan nama record.
  - TC-567 Expected a menyebut Activated At, tetapi Langkah Uji tidak membuka Tab In Use; spec menambah pengamatan Tab In Use (langkah 14 sampai 19). Langkah 4 TC ("amati Registered At dan field Registered At") tidak menyebut field Activated At; spec memilih rentang tanggal pada Activated At di Tab In Use.
  - Pemisah antara tanggal dan waktu pada format baru (koma dan spasi) tidak disebut TC; spec mengasumsikan pola baseline `DD MMM YYYY, HH:mm` menjadi `DD/MM/YYYY, hh:mm A`.
  - Kemampuan mengubah General Settings tidak didefinisikan di TC (aktor dan endpoint tidak disebut); diminta dari tim FE/BE.
  - TC-568 dan TC-569 tidak menyebut nilai spesifik untuk Hardware Log (Date & Time) dan Registered at serta Synced at; spec mengasersi pola format dan zona waktu, bukan nilai.
  - TC-569 langkah 3 ("Buka `Review` ...") tidak menyebut baris; spec memakai Subject Register Duplicate `{subjectRdLong}`, yang memuat Registered at dan Synced at.
