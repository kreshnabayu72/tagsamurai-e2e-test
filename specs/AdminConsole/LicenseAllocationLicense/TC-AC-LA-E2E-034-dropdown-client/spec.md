---
id: TC-AC-LA-E2E-034-dropdown-client
title: "Dropdown Client: Opsi Eligible, Search, dan Badge Status Suspended Expired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-120
  - TC-AC-LA-121
  - TC-AC-LA-122
coverage:
  web: automated
---

# Dropdown Client: Opsi Eligible, Search, dan Badge Status Suspended Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, Client Code, dan ID Subscription.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`), Klinik Beku (#29, status Suspended), Gudang Lawas (#30, status Expired), Kafe Baru (#31, Client Active tanpa data Client Subscription). Client Code PT Sejahtera tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan dibaca dari fixture.
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- State global: tidak ada yang diubah; status Suspended dan Expired Client adalah data Pre-setup yang hanya dibaca.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-122: Target disabled sebelum Client dipilih dan Type disabled sebelum Target dipilih

2. Verifikasi Target dan Type Disabled pada kondisi awal
3. Pilih Client `PT Sejahtera`
4. Verifikasi Target aktif
5. Verifikasi Type masih Disabled
6. Pilih Target `SUBS-20260101-A1B2C`
7. Verifikasi Type aktif

### TC-AC-LA-120: Dropdown Client hanya memuat Client yang punya data Client Subscription dan dapat dicari

8. Buka dropdown Client
9. Verifikasi opsi `PT Sejahtera` tampil sebagai opsi
10. Ketik `Kafe Baru` pada kotak pencarian dropdown Client
11. Verifikasi `Kafe Baru` tidak muncul pada opsi
12. Ganti isi kotak pencarian dengan `Sejahtera`
13. Verifikasi `PT Sejahtera` muncul dengan format opsi `PT Sejahtera` saja
14. Ganti isi kotak pencarian dengan Client Code milik PT Sejahtera
15. Verifikasi `PT Sejahtera` muncul sehingga pencarian mencocokkan Client Code (selain Company Name pada langkah 13)

### TC-AC-LA-121: Client Suspended dan Expired tetap tampil di dropdown dengan badge status

16. Ganti isi kotak pencarian dengan `Klinik Beku`
17. Verifikasi `Klinik Beku` tampil dengan badge status `Suspended` severity warning
18. Ganti isi kotak pencarian dengan `Gudang Lawas`
19. Verifikasi `Gudang Lawas` tampil dengan badge status `Expired` severity warning
20. Pilih Client `Klinik Beku`
21. Buka dropdown Client dan ganti isi kotak pencarian dengan `Klinik Beku`
22. Verifikasi opsi `Klinik Beku` tetap tampil di dropdown
23. Pilih Client `Gudang Lawas`
24. Buka dropdown Client dan ganti isi kotak pencarian dengan `Gudang Lawas`
25. Verifikasi opsi `Gudang Lawas` tetap tampil di dropdown
26. Klik `[×]` pada header
27. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
28. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 26 sampai 28).
- Penyimpangan urutan (S-10): TC-AC-LA-122 dijalankan lebih dahulu karena mengamati state Disabled yang hanya benar pada form yang baru dibuka, lalu TC-AC-LA-120 dan TC-AC-LA-121 melanjutkan di form yang sama (prinsip 6: halaman yang sama dipakai berulang tanpa Submit). Langkah 9 menjadi anchor positif bagi asersi absence langkah 11 (bagian 8b butir 2).
- Langkah penghubung (S-03): langkah 8 dan 21 sampai 24 (membuka dropdown dan mencari agar opsi dapat diamati), langkah 20 dan 23 (memilih Client untuk asersi "memilih keduanya tidak menyembunyikan opsi"), dan langkah 26 sampai 28 (menutup form dirty, S-08).
- Pencarian pada dropdown Client adalah kotak pencarian di dalam Select, bukan Search tabel (tanpa Enter).
- Temuan untuk QA:
  - TC-AC-LA-120 Langkah 3 memakai "Client Code milik PT Sejahtera" tetapi Pre-setup #19 tidak menyebut Client Code; spec membacanya dari fixture (disediakan tim FE).
  - TC-AC-LA-121 Expected b ("Memilih keduanya tidak menyembunyikan opsi") tidak menjelaskan maksud "memilih": spec menafsirkannya sebagai opsi tetap tampil setelah dipilih (langkah 20 sampai 25).
  - TC-AC-LA-121 tidak menyebut apakah Client Suspended atau Expired dapat dipilih tanpa tertolak; penolakan write-lockdown dibahas di TC lain.
