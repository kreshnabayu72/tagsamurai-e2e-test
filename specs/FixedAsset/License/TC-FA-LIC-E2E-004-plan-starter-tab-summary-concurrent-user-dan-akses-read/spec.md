---
id: TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read
title: "Plan Starter: Tab, License Summary, Concurrent User, dan Akses Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-3
  - TC-FA-LIC-19
  - TC-FA-LIC-20
  - TC-FA-LIC-29
  - TC-FA-LIC-71
  - TC-FA-LIC-111
  - TC-FA-LIC-405
  - TC-FA-LIC-484
coverage:
  web: automated
---

# Plan Starter: Tab, License Summary, Concurrent User, dan Akses Read Only

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control client Starter Pre-setup #9 `totalControlStarter_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_STARTER_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 31): Read Only client Starter Pre-setup #9 `readOnlyStarter_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_STARTER_RO_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Data Pre-setup #9: client plan Starter (Free), term live non-Trial, cap plan Asset 500, Used 120, Reserved 0, Unmanaged 3, ledger Concurrent User seed 1.
- State yang diubah spec dan dipulihkan: ledger Asset License client Starter diisi Total 999 (precondition TC-FA-LIC-19, tidak boleh dipakai untuk plan Free non-Trial), cap plan Starter diubah ke 600 (TC-FA-LIC-20), dan 1 aset Active ditambahkan (TC-FA-LIC-405). Fixture BE penyetel state dan pemulih Pre-setup #9 disediakan tim FE/BE; hook `after` memulihkan ledger, cap plan 500, dan aset. Pemulihan cap plan dilakukan juga di langkah 24 dan pemulihan aset serta ledger di langkah 30 sebagai langkah penghubung.
- Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-3: Tabs Bar plan Starter, tab Allocation Quota Hidden total

1. Verifikasi Tabs: `All License | Concurrent User`
2. Verifikasi Tab `Allocation Quota` tidak dirender sama sekali (bukan disabled, tanpa chip Upgrade)
3. Verifikasi Tab `All License` aktif

### TC-FA-LIC-484: Tab Allocation Quota Hidden pada Starter, bukan disabled maupun chip Upgrade

4. Verifikasi Tab `All License` dan Tab `Concurrent User` tampil
5. Verifikasi tidak ada tab, chip, atau tombol `Allocation Quota`/`Upgrade` dalam bentuk apa pun, termasuk yang tampil nonaktif

### TC-FA-LIC-19: License Summary plan Starter

6. Isi ledger Asset License client dengan Total 999 lewat fixture BE
7. Muat ulang halaman License
8. Verifikasi kolom `Asset`: `Total` 500 (cap konfigurasi plan, bukan ledger Asset License 999)
9. Verifikasi kolom `Asset`: `Used` 120, `Reserved` 0, `Remaining` 380, `Unmanaged` 3
10. Verifikasi kolom `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`: `Total` = `Not Available`
11. Verifikasi kolom addon yang sama: `Used`, `Reserved`, `Remaining`, `Unmanaged` = `—`
12. Verifikasi Sub-Tab `Subscription History` dan `Allocation History` tidak dirender
13. Verifikasi tabel License Summary tetap tampil lengkap beserta tombol Download

### TC-FA-LIC-29: Sub-tab riwayat tidak dirender pada plan Starter

14. Verifikasi SectionCard riwayat (Subscription History dan Allocation History) tidak ada di halaman

### TC-FA-LIC-71: Concurrent User tersedia pada plan Starter dengan seat 1

15. Klik Tab `Concurrent User`
16. Verifikasi Tab `Concurrent User` tersedia
17. Verifikasi Metric Summary Bar `Online Users: 1/1`

### TC-FA-LIC-20: Total Asset plan Starter mengikuti perubahan cap konfigurasi plan

18. Klik Tab `All License`
19. Verifikasi awal `Total` = 500
20. Ubah cap plan Starter menjadi 600 lewat fixture BE
21. Muat ulang halaman License
22. Verifikasi `Total` = 600
23. Verifikasi `Remaining` = 480 (600 − 120 − 0)
24. Pulihkan cap plan Starter ke 500 lewat fixture BE
25. Muat ulang halaman License

### TC-FA-LIC-405: Used dihitung live dari status aset

26. Catat nilai `Used`
27. Daftarkan 1 aset Active tanpa approval lewat fixture BE
28. Muat ulang halaman License
29. Verifikasi `Used` naik 1 dari nilai yang dicatat
30. Pulihkan aset yang ditambahkan dan ledger Asset License lewat fixture BE

### TC-FA-LIC-111: Role Read Only pada plan Starter

31. Ganti akun: Logout, lalu login sebagai Read Only client Starter Pre-setup #9 (`Spectra.env.FA_STARTER_RO_PASSWORD`)
32. Klik menu License pada sidebar
33. Verifikasi License Summary terbaca (tampil dengan nilai)
34. Klik Tab `Concurrent User`
35. Verifikasi Tab `Concurrent User` terbaca (daftar sesi tampil)
36. Verifikasi tidak ada kontrol tulis pada License Summary dan Tab `Concurrent User`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-3, 19, 20, 29, 71, 111, 405, 484). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: blok baca di awal, TC-20 dan TC-405 (mengubah state) di akhir, dan TC-111 (ganti akun) terakhir sehingga hanya satu kali ganti akun (S-07, S-10).
- Spec di atas 35 langkah (36 langkah): seluruh blok satu topik (plan Starter pada client yang sama), tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 6 dan 7 (precondition TC-19: ledger 999), langkah 18 (kembali ke Tab `All License`), langkah 24 dan 25 (pemulihan cap plan), langkah 30 (pemulihan aset dan ledger), langkah 31 dan 32 (ganti akun dan membuka License). Langkah TC-3 dan TC-484 "Buka License" dipenuhi hook `beforeEach` suite.
- TC-405 menyebut "registrasi 1 aset tanpa approval"; spec memakai fixture BE sebagai pemicu penambahan aset Active (registrasi bukan objek uji TC ini).
- Langkah 12 dan 14 memverifikasi klausa yang sama dari TC-19 butir c dan TC-29; keduanya dipertahankan karena tiap TC memiliki Expected sendiri.
- Temuan untuk QA:
  - TC-111 Expected "tidak ada kontrol tulis" tidak menyebut elemen tertentu; spec mengasersi atas aksi tulis yang ada di tab (tombol `[Force Logout]` dan `[Edit]`).
  - TC-405 Expected "tanpa membaca ledger Asset License" tidak dapat dibedakan secara langsung di UI; spec mengasersi kenaikan `Used` sebesar 1 dari nilai yang dicatat.
