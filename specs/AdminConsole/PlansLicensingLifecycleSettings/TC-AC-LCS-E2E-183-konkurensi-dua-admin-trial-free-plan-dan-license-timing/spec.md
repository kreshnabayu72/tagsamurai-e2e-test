---
id: TC-AC-LCS-E2E-183-konkurensi-dua-admin-trial-free-plan-dan-license-timing
title: "Konkurensi Dua Admin: Save Bersamaan Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-651
  - TC-AC-LCS-652
  - TC-AC-LCS-653
coverage:
  web: automated
---

# Konkurensi Dua Admin: Save Bersamaan Tab Trial Settings, Free Plan Settings, dan License Timing

## Prerequisites

- Mode: FE+BE. Kelas harness c (multi-konteks: dua admin pada dua sesi browser terpisah).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi A = Total Control (nama tampil `Andi Wijaya`; Modified By `Andi W`). Sesi B = Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`; Modified By `Rina K`), password dari `Spectra.env.AC_MPL_PASSWORD` (nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`, di luar folder suite); konteks browser kedua login di hook `before` spec ini, membuka tab yang sama dengan sesi A, dan ditutup di hook `after` dengan sesi login dihapus.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7). Baseline jumlah entri Changelog tab Trial Settings, Free Plan Settings, dan License Timing dicatat di hook `before` spec ini lewat kemampuan baca yang disediakan tim FE/BE (Changelog bersifat permanen, S-12); asersi Changelog memakai selisih terhadap baseline.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): konteks browser kedua yang login dengan akun Manage plans & licensing; Fixture BE untuk memulihkan ketujuh tab ke nilai default dan membaca jumlah entri Changelog.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-651: Dua admin Save tab Trial Settings bersamaan, penulisan terakhir menang tanpa dialog konflik

1. Sesi A: ubah Max Trial Duration menjadi `31` (belum Save)
2. Sesi B: ubah Max Trial Duration menjadi `32` lalu klik `[Save]` dan tunggu toast sukses
3. Verifikasi toast sukses "Success, trial settings have been saved." pada sesi B
4. Sesi A: klik `[Save]`
5. Verifikasi toast sukses "Success, trial settings have been saved." pada sesi A
6. Verifikasi tidak ada dialog konflik pada sesi A
7. Sesi B: muat ulang tab Trial Settings dan amati nilai
8. Verifikasi Max Trial Duration bernilai `31` pada sesi B (penulisan terakhir menang)
9. Sesi B: klik icon Changelog
10. Verifikasi Changelog tab Trial Settings memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)
11. Sesi B: tutup modal Changelog lewat `✕`

### TC-AC-LCS-652: Dua admin Save tab Free Plan Settings bersamaan, penulisan terakhir menang tanpa dialog konflik

12. Sesi A dan sesi B: klik tab Free Plan Settings
13. Sesi A: ubah Free Plan Duration menjadi `366` (belum Save)
14. Sesi B: ubah Free Plan Duration menjadi `367` lalu klik `[Save]` dan tunggu toast sukses
15. Verifikasi toast sukses "Success, free plan settings have been saved." pada sesi B
16. Sesi A: klik `[Save]`
17. Verifikasi toast sukses "Success, free plan settings have been saved." pada sesi A
18. Verifikasi tidak ada dialog konflik pada sesi A
19. Sesi B: muat ulang tab Free Plan Settings dan amati nilai
20. Verifikasi Free Plan Duration bernilai `366` pada sesi B (penulisan terakhir menang)
21. Sesi B: klik icon Changelog
22. Verifikasi Changelog tab Free Plan Settings memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)
23. Sesi B: tutup modal Changelog lewat `✕`

### TC-AC-LCS-653: Dua admin Save tab License Timing bersamaan, penulisan terakhir menang tanpa dialog konflik

24. Sesi A dan sesi B: klik tab License Timing
25. Sesi A: ubah Managed Transition Time menjadi `25` (belum Save)
26. Sesi B: ubah Managed Transition Time menjadi `26` lalu klik `[Save]` dan tunggu toast sukses
27. Verifikasi toast sukses "Success, license timing settings have been saved." pada sesi B
28. Sesi A: klik `[Save]`
29. Verifikasi toast sukses "Success, license timing settings have been saved." pada sesi A
30. Verifikasi tidak ada dialog konflik pada sesi A
31. Sesi B: muat ulang tab License Timing dan amati nilai
32. Verifikasi Managed Transition Time bernilai `25` pada sesi B (penulisan terakhir menang)
33. Sesi B: klik icon Changelog
34. Verifikasi Changelog tab License Timing memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness c.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Konteks browser kedua (sesi B) adalah objek asersi sehingga spec ini kelas c tanpa butir `P-2`.
- Dua TC dalam satu spec memakai tab berbeda; tiap TC memulai dari nilai default tab tersebut sehingga hasil TC sebelumnya tidak dipakai (S-06, S-09).
- Temuan untuk QA:
  - TC 651 sampai 657 dan 675 bertanda `Manual Only` (dua sesi pengguna paralel); spec tetap menulisnya sebagai kelas c dengan kebutuhan dua sesi di Prerequisites (bagian 2 konvensi).
  - TC 651 sampai 657 Expected d "Changelog memuat dua entri terpisah" tanpa baseline; spec mengasersi selisih dua terhadap baseline jumlah entri (S-12).
  - TC 651 sampai 657 tidak menyebut apakah kedua sesi membuka tab target sejak awal; spec menulis langkah klik tab pada kedua sesi di awal tiap TC sesuai precondition "Dua sesi browser terpisah membuka tab yang sama".
  - Post Condition seluruh TC tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 11-12, 23-24.
