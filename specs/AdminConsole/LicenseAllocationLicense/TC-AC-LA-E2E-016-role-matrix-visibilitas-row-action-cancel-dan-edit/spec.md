---
id: TC-AC-LA-E2E-016-role-matrix-visibilitas-row-action-cancel-dan-edit
title: "Role Matrix: Visibilitas Row Action Cancel dan Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-65
  - TC-AC-LA-66
coverage:
  web: automated
---

# Role Matrix: Visibilitas Row Action Cancel dan Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Read saja (Pre-setup #7) `readCapLic_automated_{namaCompany}@qwertysystem.net` (`Bayu Aditya`), password `Spectra.env.AC_LA_DIST_READ_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`; Distributor Read+Update tanpa Create (Pre-setup #6) `updateOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Yuni Lestari`), password `Spectra.env.AC_LA_DIST_UPDATE_PASSWORD`; Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Cancel Allocation | Edit |
|---|---|---|---|
| `readCapLic` (`Bayu Aditya`) | Distributor Read | Hidden pada semua baris | Hidden |
| `createOnlyLic` (`Doni Prasetyo`) | Create+Read tanpa Update | Hidden pada record `Waiting for Approval` miliknya | Hidden |
| `updateOnlyLic` (`Yuni Lestari`) | Read+Update | Show pada record `Waiting for Approval` miliknya | Show pada record miliknya |
| `gmApproveOnlyLic` (`Rian Hartono`) | Group Manager approve-only | Show pada `Pending`, Hidden pada `Waiting for Approval` orang lain | Hidden |
| `totalControlDistLic` (`Fajar Nugroho`) | Total Control Distributor | Show pada `Pending` mana pun, Hidden pada `Waiting for Approval` orang lain | Show hanya pada record miliknya, Hidden pada record orang lain |

- Data Pre-setup yang dibaca (hanya menu `⋯` dibuka, tidak ada aksi dijalankan): #43 alokasi `Waiting for Approval` milik `Yuni L`, #57 alokasi `Waiting for Approval` milik `Doni P`, #46 alokasi `Pending` milik `Dewi A`, #58 alokasi `Pending` milik `Fajar N`. Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed43, seed57, seed46, seed58).
- Urutan akun: `readCapLic` (hook `before`), `createOnlyLic`, `updateOnlyLic`, `gmApproveOnlyLic`, `totalControlDistLic`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### Akun `readCapLic` (TC-AC-LA-65 butir e, TC-AC-LA-66 butir c)

1. Ketik Search Allocation ID seed `Pending` milik `Dewi A` (`Fixture.license-allocation-license.seed46`), tekan Enter
2. Klik ikon `⋯` pada baris `Pending`
3. Verifikasi row action `Cancel Allocation` Hidden bagi `Bayu Aditya` pada baris `Pending`
4. Verifikasi row action `Edit` Hidden bagi `Bayu Aditya` pada baris `Pending`
5. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
6. Klik ikon `⋯` pada baris `Waiting for Approval`
7. Verifikasi row action `Cancel Allocation` Hidden bagi `Bayu Aditya` pada baris `Waiting for Approval`
8. Verifikasi row action `Edit` Hidden bagi `Bayu Aditya` pada baris `Waiting for Approval`

### Akun `createOnlyLic` (TC-AC-LA-65 butir d, TC-AC-LA-66 butir b)

9. Ganti akun: Logout lalu login sebagai Distributor Create+Read (`createOnlyLic`)
10. Ketik Search Allocation ID seed `Waiting for Approval` milik `Doni P` (`Fixture.license-allocation-license.seed57`), tekan Enter
11. Klik ikon `⋯` pada baris milik sendiri
12. Verifikasi row action `Cancel Allocation` Hidden bagi `Doni Prasetyo`
13. Verifikasi row action `Edit` Hidden bagi `Doni Prasetyo` (tidak punya capability Update)

### Akun `updateOnlyLic` (TC-AC-LA-65 butir a, TC-AC-LA-66 butir a)

14. Ganti akun: Logout lalu login sebagai Distributor Read+Update (`updateOnlyLic`)
15. Ketik Search Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
16. Klik ikon `⋯` pada baris milik sendiri
17. Verifikasi row action `Cancel Allocation` Show pada record `Waiting for Approval` milik `Yuni Lestari`
18. Verifikasi row action `Edit` Show pada record `Waiting for Approval` milik `Yuni Lestari`

### Akun `gmApproveOnlyLic` (TC-AC-LA-65 butir b, TC-AC-LA-66 butir c)

19. Ganti akun: Logout lalu login sebagai Group Manager approve-only (`gmApproveOnlyLic`)
20. Ketik Search Allocation ID seed `Pending` milik `Dewi A` (`Fixture.license-allocation-license.seed46`), tekan Enter
21. Klik ikon `⋯` pada baris `Pending`
22. Verifikasi row action `Cancel Allocation` Show pada baris `Pending` dalam scope group
23. Verifikasi row action `Edit` Hidden bagi `Rian Hartono` pada baris `Pending`
24. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
25. Klik ikon `⋯` pada baris `Waiting for Approval` milik orang lain
26. Verifikasi row action `Cancel Allocation` Hidden pada baris `Waiting for Approval` milik orang lain
27. Verifikasi row action `Edit` Hidden bagi `Rian Hartono` pada baris `Waiting for Approval`

### Akun `totalControlDistLic` (TC-AC-LA-65 butir c, TC-AC-LA-66 butir d)

28. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`)
29. Ketik Search Allocation ID seed `Pending` milik `Dewi A` (`Fixture.license-allocation-license.seed46`), tekan Enter
30. Klik ikon `⋯` pada baris `Pending` milik orang lain
31. Verifikasi row action `Cancel Allocation` Show pada baris `Pending` milik `Dewi A`
32. Verifikasi row action `Edit` Hidden pada baris `Pending` milik orang lain
33. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
34. Klik ikon `⋯` pada baris `Waiting for Approval` milik orang lain
35. Verifikasi row action `Cancel Allocation` Hidden pada baris `Waiting for Approval` milik orang lain
36. Ganti isi kotak search dengan Allocation ID seed `Pending` milik `Fajar N` (`Fixture.license-allocation-license.seed58`), tekan Enter
37. Klik ikon `⋯` pada baris `Pending` milik sendiri
38. Verifikasi row action `Edit` Show pada record milik `Fajar Nugroho` sendiri

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah membuka menu `⋯`, dan ganti akun eksplisit (S-07). Langkah dikelompokkan per akun karena akun yang sama muncul di TC-AC-LA-65 dan TC-AC-LA-66; subjudul `###` menyebut TC dan butir Expected.
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (visibilitas row action Cancel dan Edit) dan satu kelas harness (Role Matrix), data seed baca-saja yang sama, dan tiap blok akun berdiri sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Seed #43, #57, #46, dan #58 hanya dibaca; tidak ada aksi Cancel atau Edit yang dijalankan.
- Temuan untuk QA:
  - TC-AC-LA-65 Expected e dan TC-AC-LA-66 Expected c (`semua baris`) tidak merinci baris; spec mengasersi baris seed `Pending` (#46) dan `Waiting for Approval` (#43) untuk `readCapLic`.
  - TC-AC-LA-66 Expected d menyebut `Fajar Nugroho: Edit Show hanya pada record miliknya sendiri dan Hidden pada record orang lain`; spec mengasersi Hidden pada #46 dan Show pada #58 (milik `Fajar N`).
  - TC-AC-LA-65 Expected b dan c mengasersi `Cancel Allocation` Hidden pada `Waiting for Approval` milik orang lain tanpa anchor positif di TC; spec memakai anchor menu `⋯` yang terbuka (Allocation Log tampil).
