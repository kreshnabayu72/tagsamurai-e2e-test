---
id: TC-AC-LA-E2E-037-reset-berantai-ganti-client-target-type
title: "Reset Berantai Form Allocate: Ganti Client, Target, dan Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-136
  - TC-AC-LA-137
  - TC-AC-LA-138
coverage:
  web: automated
---

# Reset Berantai Form Allocate: Ganti Client, Target, dan Type

## Prerequisites

- Mode: FE+BE. Respons Current Quota ditahan lewat `Spectra.intercept()` di atas backend nyata untuk mengamati skeleton (langkah 17).
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19, `SUBS-20260101-A1B2C`), Klinik Medika Jaya (#20), Toko Serba Ada (#21, `SUBS-20250201-J7K8L` Active dan `SUBS-20260819-00001` Pending).
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons Current Quota 5 detik lalu melepasnya.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-136: Ganti Client mereset Target, Type, dan Current Quota tetapi mempertahankan Additional Quantity

2. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `7`
3. Ganti Client ke `Klinik Medika Jaya`
4. Verifikasi Target dikosongkan dengan placeholder `Select target`
5. Verifikasi Type dikosongkan
6. Verifikasi Type Disabled
7. Verifikasi Current Quota hilang
8. Verifikasi Additional Quantity tetap `7`

### TC-AC-LA-137: Ganti Target mereset Type dan Current Quota tetapi mempertahankan Client dan Additional Quantity

9. Pilih Client `Toko Serba Ada`, Target `SUBS-20250201-J7K8L`, Type `Concurrent User`, ganti isi Additional Quantity dengan `7`
10. Ganti Target ke `SUBS-20260819-00001`
11. Verifikasi Type dikosongkan
12. Verifikasi Current Quota hilang
13. Verifikasi Client tetap `Toko Serba Ada`
14. Verifikasi Additional Quantity tetap `7`

### TC-AC-LA-138: Ganti Type mereset Current Quota

15. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, ganti isi Additional Quantity dengan `7`
16. Atur intercept: tunda 5 detik respons Current Quota, lalu ganti Type ke `Asset License`
17. Verifikasi skeleton tampil pada Current Quota
18. Lepas tahanan respons Current Quota dan lepas intercept
19. Verifikasi Current Quota dimuat ulang untuk Type `Asset License`
20. Verifikasi Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, dan Additional Quantity `7` tetap
21. Klik `[×]` pada header
22. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
23. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 21 sampai 23).
- Penyimpangan urutan (S-10): ketiga TC memakai satu sesi form (prinsip 6, tanpa Submit). Langkah 9 dan 15 memilih ulang Client agar state awal TC sama dengan pembukaan form baru (mengganti Client mereset Target dan Type); Additional Quantity ditimpa dengan `7` agar nilai awal sesuai Data Uji.
- Langkah penghubung (S-03): langkah 18 (melepas tahanan respons) dan langkah 21 sampai 23 (menutup form dirty, S-08). Intercept pada langkah 16 ditambahkan agar skeleton "dimuat ulang dengan skeleton" (Expected a TC-AC-LA-138) dapat diamati (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-LA-138 Expected a ("dimuat ulang ... dengan skeleton") tidak menyebut penundaan respons; skeleton hanya teramati bila respons ditahan, sehingga spec menambah intercept (langkah 16).
  - TC-AC-LA-136 Expected c ("Additional Quantity tetap `7`") tidak menyebut apakah field Additional Quantity tetap tampil saat Type dikosongkan; spec mengasersi nilai field `7` sesuai Expected.
