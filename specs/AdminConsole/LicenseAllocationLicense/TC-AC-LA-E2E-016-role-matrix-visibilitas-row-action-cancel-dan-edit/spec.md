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
3. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Pending` (anchor menu terbuka)
4. Verifikasi row action `Cancel Allocation` Hidden bagi `Bayu Aditya` pada baris `Pending`
5. Verifikasi row action `Edit` Hidden bagi `Bayu Aditya` pada baris `Pending`
6. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
7. Klik ikon `⋯` pada baris `Waiting for Approval`
8. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Waiting for Approval` (anchor menu terbuka)
9. Verifikasi row action `Cancel Allocation` Hidden bagi `Bayu Aditya` pada baris `Waiting for Approval`
10. Verifikasi row action `Edit` Hidden bagi `Bayu Aditya` pada baris `Waiting for Approval`

### Akun `createOnlyLic` (TC-AC-LA-65 butir d, TC-AC-LA-66 butir b)

11. Ganti akun: Logout lalu login sebagai Distributor Create+Read (`createOnlyLic`), lalu buka Allocation > License Allocation tab Current
12. Ketik Search Allocation ID seed `Waiting for Approval` milik `Doni P` (`Fixture.license-allocation-license.seed57`), tekan Enter
13. Klik ikon `⋯` pada baris milik sendiri
14. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris milik sendiri (anchor menu terbuka)
15. Verifikasi row action `Cancel Allocation` Hidden bagi `Doni Prasetyo`
16. Verifikasi row action `Edit` Hidden bagi `Doni Prasetyo` (tidak punya capability Update)

### Akun `updateOnlyLic` (TC-AC-LA-65 butir a, TC-AC-LA-66 butir a)

17. Ganti akun: Logout lalu login sebagai Distributor Read+Update (`updateOnlyLic`), lalu buka Allocation > License Allocation tab Current
18. Ketik Search Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
19. Klik ikon `⋯` pada baris milik sendiri
20. Verifikasi row action `Cancel Allocation` Show pada record `Waiting for Approval` milik `Yuni Lestari`
21. Verifikasi row action `Edit` Show pada record `Waiting for Approval` milik `Yuni Lestari`

### Akun `gmApproveOnlyLic` (TC-AC-LA-65 butir b, TC-AC-LA-66 butir c)

22. Ganti akun: Logout lalu login sebagai Group Manager approve-only (`gmApproveOnlyLic`), lalu buka Allocation > License Allocation tab Current
23. Ketik Search Allocation ID seed `Pending` milik `Dewi A` (`Fixture.license-allocation-license.seed46`), tekan Enter
24. Klik ikon `⋯` pada baris `Pending`
25. Verifikasi row action `Cancel Allocation` Show pada baris `Pending` dalam scope group
26. Verifikasi row action `Edit` Hidden bagi `Rian Hartono` pada baris `Pending`
27. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
28. Klik ikon `⋯` pada baris `Waiting for Approval` milik orang lain
29. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Waiting for Approval` milik orang lain (anchor menu terbuka)
30. Verifikasi row action `Cancel Allocation` Hidden pada baris `Waiting for Approval` milik orang lain
31. Verifikasi row action `Edit` Hidden bagi `Rian Hartono` pada baris `Waiting for Approval`

### Akun `totalControlDistLic` (TC-AC-LA-65 butir c, TC-AC-LA-66 butir d)

32. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`), lalu buka Allocation > License Allocation tab Current
33. Ketik Search Allocation ID seed `Pending` milik `Dewi A` (`Fixture.license-allocation-license.seed46`), tekan Enter
34. Klik ikon `⋯` pada baris `Pending` milik orang lain
35. Verifikasi row action `Cancel Allocation` Show pada baris `Pending` milik `Dewi A`
36. Verifikasi row action `Edit` Hidden pada baris `Pending` milik orang lain
37. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` milik `Yuni L` (`Fixture.license-allocation-license.seed43`), tekan Enter
38. Klik ikon `⋯` pada baris `Waiting for Approval` milik orang lain
39. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Waiting for Approval` milik orang lain (anchor menu terbuka)
40. Verifikasi row action `Cancel Allocation` Hidden pada baris `Waiting for Approval` milik orang lain
41. Ganti isi kotak search dengan Allocation ID seed `Pending` milik `Fajar N` (`Fixture.license-allocation-license.seed58`), tekan Enter
42. Klik ikon `⋯` pada baris `Pending` milik sendiri
43. Verifikasi row action `Edit` Show pada record milik `Fajar Nugroho` sendiri

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah membuka menu `⋯`, dan ganti akun eksplisit (S-07). Langkah dikelompokkan per akun karena akun yang sama muncul di TC-AC-LA-65 dan TC-AC-LA-66; subjudul `###` menyebut TC dan butir Expected.
- Asersi tambahan (S-03): langkah 3, 8, 14, 29, dan 39 (`Allocation Log` Show) adalah anchor positif pada menu `⋯` yang sama sebelum asersi Hidden; alasannya bagian 8b butir 2 dan keputusan 2026-11-04 (Role Matrix Hidden pada row action wajib punya `Verifikasi` pembanding). `Allocation Log` dipilih sebagai anchor karena tampil bagi akses Read (TC-AC-LA-70).
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (visibilitas row action Cancel dan Edit) dan satu kelas harness (Role Matrix), data seed baca-saja yang sama, dan tiap blok akun berdiri sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Seed #43, #57, #46, dan #58 hanya dibaca; tidak ada aksi Cancel atau Edit yang dijalankan.
- Temuan untuk QA:
  - TC-AC-LA-65 Expected e dan TC-AC-LA-66 Expected c (`semua baris`) tidak merinci baris; spec mengasersi baris seed `Pending` (#46) dan `Waiting for Approval` (#43) untuk `readCapLic`.
  - TC-AC-LA-66 Expected d menyebut `Fajar Nugroho: Edit Show hanya pada record miliknya sendiri dan Hidden pada record orang lain`; spec mengasersi Hidden pada #46 dan Show pada #58 (milik `Fajar N`).
  - TC-AC-LA-65 Expected b dan c mengasersi `Cancel Allocation` Hidden pada `Waiting for Approval` milik orang lain tanpa anchor positif di TC; spec menambah `Verifikasi` row action `Allocation Log` Show pada menu `⋯` yang sama (langkah 3, 8, 14, 29, dan 39) sebagai anchor sebelum tiap asersi Hidden pertama pada menu itu (S-03, bagian 8b butir 2).
