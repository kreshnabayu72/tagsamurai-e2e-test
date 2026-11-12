---
id: TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc
title: "Scope Group Role: Zero Access dan Group A, B, C pada Satu Akun"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-90
  - TC-AC-LA-91
  - TC-AC-LA-92
  - TC-AC-LA-93
  - TC-AC-LA-96
coverage:
  web: automated
---

# Scope Group Role: Zero Access dan Group A, B, C pada Satu Akun

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Zero Access (Pre-setup #13) `zeroAccessLic_automated_{namaCompany}@qwertysystem.net` (`Wawan Hadi`), password `Spectra.env.AC_LA_ZERO_ACCESS_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Group A/B/C (Pre-setup #17) `mixedGroupLic_automated_{namaCompany}@qwertysystem.net` (`Gita Permata`), password `Spectra.env.AC_LA_MIXED_GROUP_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Group dan Client | Hasil yang diuji |
|---|---|---|---|
| `zeroAccessLic` (`Wawan Hadi`) | Zero Access pada group Client uji | Client `PT Sejahtera` di group tanpa izin | baris, opsi filter Client, dan dropdown Client tidak memuat `PT Sejahtera` |
| `mixedGroupLic` (`Gita Permata`) | Group A/B/C | Group Alpha (Read): `Toko Serba Ada`; Group Beta (Create+Read+Update): `PT Sejahtera`; Group Gamma (tidak di-assign): `Klinik Medika Jaya` | Group Alpha: baris dan `Allocation Log` tampil, `Cancel Allocation` Hidden, dropdown tidak memuat `Toko Serba Ada`; Group Beta: Allocate sukses; Group Gamma: baris dan dropdown tidak memuat `Klinik Medika Jaya`; Client Detail Toko Serba Ada tab License: tombol mutasi Disabled dengan tooltip |

- Data Pre-setup yang dibaca: #19 PT Sejahtera, #20 Klinik Medika Jaya, #21 Toko Serba Ada, #41 alokasi `Waiting for Approval` (PT Sejahtera), #46 alokasi `Pending` (Toko Serba Ada), #33 saldo kantong wallet, #34 Product Price, #39 Require Approval OFF. Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed46). Spec membuat satu alokasi baru (TC-AC-LA-92, data Dinamis) yang dibersihkan baseline automation/fixture backend di hook `after`.
- State global: Require Approval for Allocation diatur OFF pada group Client uji lewat fixture backend yang disediakan tim FE/BE (mekanisme tidak tertulis di TC); nilai awal dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-90: Zero Access: baris, opsi filter, dan dropdown Client tidak tampil

1. Ketik Search Allocation ID seed `Waiting for Approval` PT Sejahtera (`Fixture.license-allocation-license.seed41`), tekan Enter
2. Verifikasi empty state `No results found` tampil pada tab Current
3. Verifikasi baris alokasi `PT Sejahtera` tidak tampil sama sekali
4. Klik `(←)` pada kotak Search, lalu klik ikon Filter dan buka dropdown filter Client
5. Verifikasi opsi filter Client tidak memuat `PT Sejahtera`
6. Tutup panel Filter, lalu klik `[+ Allocation]` dan buka dropdown Client
7. Verifikasi dropdown Client pada form tidak memuat `PT Sejahtera`
8. Tutup form dengan `[×]`

### TC-AC-LA-91: Group A Read-only

9. Ganti akun: Logout lalu login sebagai Distributor Group A/B/C (`mixedGroupLic`), lalu buka Allocation > License Allocation tab Current
10. Ketik Search Allocation ID seed `Pending` Toko Serba Ada (`Fixture.license-allocation-license.seed46`), tekan Enter
11. Verifikasi baris alokasi `Toko Serba Ada` tampil
12. Klik ikon `⋯` pada baris itu
13. Verifikasi row action `Allocation Log` tampil
14. Verifikasi row action `Cancel Allocation` Hidden
15. Klik `(←)` pada kotak Search, lalu klik `[+ Allocation]` dan buka dropdown Client

### TC-AC-LA-92: Group B Create+Read: aksi penuh pada group yang di-assign

16. Verifikasi dropdown Client memuat `PT Sejahtera`
17. Verifikasi dropdown Client tidak memuat `Toko Serba Ada`
18. Verifikasi dropdown Client tidak memuat `Klinik Medika Jaya`
19. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1`
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, license has been allocated."

### TC-AC-LA-93: Group C Zero Access pada akun yang sama

22. Ketik Search `Klinik Medika Jaya`, tekan Enter
23. Verifikasi empty state `No results found` tampil
24. Verifikasi baris `Klinik Medika Jaya` tidak tampil
25. Klik `(←)` pada kotak Search

### TC-AC-LA-96: Tab License pada Detail Client dengan tombol mutasi Disabled dan tooltip

26. Buka Client > Detail `Toko Serba Ada` > tab License
27. Verifikasi data lisensi Client tampil
28. Hover tombol mutasi alokasi lisensi
29. Verifikasi tombol mutasi alokasi Disabled
30. Verifikasi tooltip: "You do not have permission to allocate licenses for entities in this group."

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah penutupan panel dan form, dan ganti akun eksplisit (S-07). Dropdown Client dibuka sekali dan dipakai bersama TC-AC-LA-91 butir c, TC-AC-LA-92 butir a, dan TC-AC-LA-93 butir b; langkah Search nama Client pada TC-AC-LA-93 butir a memakai Search List.
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Absence baris, opsi filter, dan opsi dropdown diawali anchor positif: hasil Search kosong dengan empty state `No results found` (bagian 8b butir 2), dan dropdown Client akun `mixedGroupLic` memuat `PT Sejahtera` sebelum asersi `Toko Serba Ada` dan `Klinik Medika Jaya` tidak ada.
- Temuan untuk QA:
  - TC-AC-LA-90 tidak menjelaskan apakah akun Zero Access melihat baris lain pada List (tidak ada anchor baris pembanding); spec memakai empty state hasil Search sebagai anchor untuk baris, tetapi opsi filter dan dropdown Client `PT Sejahtera` tidak punya anchor di TC.
  - TC-AC-LA-96 menyebut `tombol mutasi alokasi lisensi` tanpa label tombol di Client Detail tab License; spec memakai istilah TC.
  - TC-AC-LA-92 Expected a dan b tidak menyebut apakah Allocated By dan Status diasersi; hanya toast sukses dan dropdown yang diasersi.
  - TC-AC-LA-91 Expected b (`Cancel Allocation Hidden`) pada baris `Pending` Toko Serba Ada (Pre-setup #46) tidak menyebut anchor positif; spec memakai `Allocation Log` pada menu `⋯` yang sama sebagai anchor.
