---
id: TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press
title: "Mobile: Long Press, Select All Card, Mode Seleksi, dan Dialog Delete"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-297
  - TC-FA-FAAM-298
  - TC-FA-FAAM-299
  - TC-FA-FAAM-300
  - TC-FA-FAAM-301
coverage:
  web: unsupported
  mobile: automated
---

# Mobile: Long Press, Select All Card, Mode Seleksi, dan Dialog Delete

## Prerequisites

- Mode: FE+BE (backend nyata), aplikasi FAMS mobile native Android.
- Perangkat: perangkat atau emulator Android dengan aplikasi FAMS terpasang (disediakan tim FE). Perangkat bersama: `parallel: false`.
- Role yang diuji dan akun:

| Role | Akun (Pre-setup) | Env password | Dipakai di |
|---|---|---|---|
| Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` (#1) | `Spectra.env.FA_TC_PASSWORD` | TC-FA-FAAM-297, 299, 300, 301 (login di hook `before`) |
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` (#5) | `Spectra.env.FA_UO_PASSWORD` | TC-FA-FAAM-298 (Ganti akun eksplisit, langkah 31) |

- Login akun pertama (Total Control) di aplikasi di hook `before` spec ini; halaman Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, tidak dihapus karena dialog Delete dibatalkan; dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Bulk Clean A` dan `Bulk Clean B` (#13c, Total Asset 0), `Bulk Used X` (#14o, Total Asset 3), `Seed Item 01` s.d. `Seed Item 30` (#15) dan fixture #10 s.d. #14 sehingga daftar lebih dari satu halaman data.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-297: Mobile: long press masuk selection mode tanpa checkbox permanen

1. Ketik Search `Bulk Clean A`, tekan Enter
2. Verifikasi sedikitnya satu card tampil
3. Verifikasi tidak ada checkbox di card pada keadaan normal
4. Long press (sekitar 500 ms) card `Bulk Clean A`
5. Verifikasi kotak seleksi muncul di seluruh card
6. Verifikasi Floating Contextual Bottom Bulk Action Bar tampil dengan `[✕]`, counter `1 Selected`, `[Select All]`, dan `[Delete]` (merah)
7. Tap `[✕]` untuk mengakhiri mode seleksi

### TC-FA-FAAM-299: Mobile: Select All memilih seluruh card yang dimuat

8. Tutup Search inline sehingga seluruh card yang dimuat tampil
9. Long press satu card
10. Tap `[Select All]`
11. Verifikasi tidak ada toast cap Selection Limit
12. Verifikasi seluruh card yang saat ini dimuat terpilih
13. Verifikasi counter menampilkan `[N] Selected` dengan N sama dengan jumlah card yang tampil di daftar
14. Tap `[✕]` untuk mengakhiri mode seleksi

### TC-FA-FAAM-300: Mobile: mode seleksi berakhir lewat [✕], seleksi 0, atau tombol Back

15. Long press card
16. Tap `[✕]`
17. Verifikasi checkbox hilang dan Bulk Action Bar menghilang
18. Long press card
19. Un-tap card terpilih sampai `0 Selected`
20. Verifikasi checkbox hilang dan Bulk Action Bar menghilang
21. Long press card
22. Tekan tombol Back Android
23. Verifikasi checkbox hilang dan Bulk Action Bar menghilang

### TC-FA-FAAM-301: Mobile: tombol Delete menjalankan dialog yang sama dengan web

24. Ketik Search `Bulk`, tekan Enter
25. Long press card `Bulk Clean A`
26. Tap card `Bulk Used X`
27. Tap `[Delete]`
28. Verifikasi dialog campuran `Delete Asset Names` (D-04) tampil
29. Tap `[Cancel]` pada dialog
30. Tap `[✕]` untuk mengakhiri mode seleksi

### TC-FA-FAAM-298: Mobile: long press tidak aktif bagi pemegang tanpa hak Delete

31. Ganti akun: Logout, login sebagai Update-Only (`updateOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_UO_PASSWORD`), lalu buka Settings > Asset Master > Asset Name
32. Ketik Search `Bulk Clean A`, tekan Enter
33. Long press card `Bulk Clean A`
34. Verifikasi selection mode tidak aktif

## Notes

- Mode: FE+BE (aplikasi FAMS Android native). Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular. `coverage.web: unsupported` dan `coverage.mobile: automated`.
- Urutan TC di spec: 297, 299, 300, 301, 298. Ganti akun Update-Only terakhir (S-07, S-10). Setiap TC yang masuk mode seleksi mengakhirinya sebelum TC berikutnya (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 24, 32 (Search untuk menemukan card target, R-16), langkah 7, 14, 30 (mengakhiri mode seleksi), langkah 8 (menutup Search inline), langkah 29 (membatalkan dialog sehingga tidak ada Asset Name yang terhapus), langkah 31 (Ganti akun eksplisit).
- Langkah 2 adalah anchor positif untuk asersi absence checkbox pada langkah 3; langkah 11 (absence toast) ditulis segera setelah pemicu `[Select All]` dan sebelum asersi hasil (bagian 8b butir 11).
- Langkah 17, 20, dan 23 memuat dua elemen yang sama-sama tidak ada (checkbox dan bar) dan ditulis satu `Verifikasi` dengan daftar disebut utuh (S-01).
- Langkah 34 (absence) memakai card `Bulk Clean A` yang ditemukan Search sebagai anchor permukaan.
- Temuan untuk QA:
  - TC-297 Langkah 2 long press `Bulk Clean A` (Pre-setup #13c) tidak mengubah data; TC-301 membatalkan dialog; spec tidak menghapus fixture #13c.
  - TC-299 Expected a "N sama dengan jumlah card yang tampil" tidak menyebut nilai N konkret; spec tidak menulis angka literal.
