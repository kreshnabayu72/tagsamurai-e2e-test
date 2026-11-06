---
id: TC-AC-LA-E2E-017-role-matrix-visibilitas-row-action-resubmit-dan-review
title: "Role Matrix: Visibilitas Row Action Resubmit dan Tombol Review di Approvals"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-67
  - TC-AC-LA-68
coverage:
  web: automated
---

# Role Matrix: Visibilitas Row Action Resubmit dan Tombol Review di Approvals

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Read+Update tanpa Create (Pre-setup #6) `updateOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Yuni Lestari`), password `Spectra.env.AC_LA_DIST_UPDATE_PASSWORD`; Distributor Read saja (Pre-setup #7) `readCapLic_automated_{namaCompany}@qwertysystem.net` (`Bayu Aditya`), password `Spectra.env.AC_LA_DIST_READ_PASSWORD`; Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Additional Approver (Pre-setup #11) `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`; Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Resubmit (tab History) | Review di Approvals |
|---|---|---|---|
| `createOnlyLic` (`Doni Prasetyo`) | Create+Read | Show pada record `Canceled` miliknya | - |
| `updateOnlyLic` (`Yuni Lestari`) | Read+Update tanpa Create | Hidden pada semua baris `Canceled` | - |
| `readCapLic` (`Bayu Aditya`) | Read | Hidden | menu Approvals Hidden |
| `gmApproveOnlyLic` (`Rian Hartono`) | Group Manager approve-only | Hidden | `[Review]` Show |
| `totalControlDistLic` (`Fajar Nugroho`) | Total Control Distributor | Show pada record `Canceled` miliknya, Hidden pada milik orang lain | `[Review]` Show |
| `additionalApproverLic` (`Maya Tanjung`) | Additional Approver | - | `[Review]` Show |
| `dewiFullLic` (`Dewi Anggraini`) | Create+Read+Update | - | menu Approvals Hidden |

- Data Pre-setup yang dibaca: #48 alokasi `Canceled` milik `Dewi A`, #59 alokasi `Canceled` milik `Doni P` dan alokasi `Canceled` milik `Fajar N`, #41 alokasi `Waiting for Approval` (untuk `[Review]`). Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed48, seed59Doni, seed59Fajar, seed41). Seed hanya dibaca; tidak ada aksi Resubmit atau Review yang dijalankan.
- Urutan akun: `createOnlyLic` (hook `before`), `updateOnlyLic`, `readCapLic`, `gmApproveOnlyLic`, `totalControlDistLic`, `additionalApproverLic`, `dewiFullLic`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### Akun `createOnlyLic` (TC-AC-LA-67 butir a dan d)

1. Klik tab `History`
2. Ketik Search Allocation ID seed `Canceled` milik `Doni P` (`Fixture.license-allocation-license.seed59Doni`), tekan Enter
3. Klik ikon `⋯` pada baris milik sendiri
4. Verifikasi row action `Resubmit` Show pada record `Canceled` milik `Doni Prasetyo`
5. Ganti isi kotak search dengan Allocation ID seed `Canceled` milik `Dewi A` (`Fixture.license-allocation-license.seed48`), tekan Enter
6. Klik ikon `⋯` pada baris milik orang lain
7. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` milik orang lain (anchor menu terbuka)
8. Verifikasi row action `Resubmit` Hidden pada record `Canceled` milik orang lain

### Akun `updateOnlyLic` (TC-AC-LA-67 butir b dan d)

9. Ganti akun: Logout lalu login sebagai Distributor Read+Update (`updateOnlyLic`), lalu buka Allocation > License Allocation tab Current
10. Klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` milik `Doni P` (`Fixture.license-allocation-license.seed59Doni`), tekan Enter
11. Klik ikon `⋯` pada baris `Canceled`
12. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` (anchor menu terbuka)
13. Verifikasi row action `Resubmit` Hidden pada baris `Canceled` bagi `Yuni Lestari` (tanpa Create)
14. Ganti isi kotak search dengan Allocation ID seed `Canceled` milik `Dewi A` (`Fixture.license-allocation-license.seed48`), tekan Enter
15. Klik ikon `⋯` pada baris `Canceled`
16. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` milik orang lain (anchor menu terbuka)
17. Verifikasi row action `Resubmit` Hidden pada baris `Canceled` milik orang lain bagi `Yuni Lestari`

### Akun `readCapLic` (TC-AC-LA-67 butir c, TC-AC-LA-68 butir b)

18. Ganti akun: Logout lalu login sebagai Distributor Read (`readCapLic`), lalu buka Allocation > License Allocation tab Current
19. Klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` milik `Doni P` (`Fixture.license-allocation-license.seed59Doni`), tekan Enter
20. Klik ikon `⋯` pada baris `Canceled`
21. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` (anchor menu terbuka)
22. Verifikasi row action `Resubmit` Hidden bagi `Bayu Aditya`
23. Periksa sidebar Approvals
24. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
25. Verifikasi menu `Approvals > License Allocation` Hidden bagi `Bayu Aditya` sehingga tidak ada `[Review]`

### Akun `gmApproveOnlyLic` (TC-AC-LA-67 butir c, TC-AC-LA-68 butir a)

26. Ganti akun: Logout lalu login sebagai Group Manager approve-only (`gmApproveOnlyLic`), lalu buka Allocation > License Allocation tab Current
27. Klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` milik `Doni P` (`Fixture.license-allocation-license.seed59Doni`), tekan Enter
28. Klik ikon `⋯` pada baris `Canceled`
29. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` (anchor menu terbuka)
30. Verifikasi row action `Resubmit` Hidden bagi `Rian Hartono`
31. Buka Approvals > License Allocation dan ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
32. Verifikasi `[Review]` Show pada baris alokasi dalam scope bagi `Rian Hartono`

### Akun `totalControlDistLic` (TC-AC-LA-67 butir a dan d, TC-AC-LA-68 butir a dan c)

33. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`), lalu buka Allocation > License Allocation tab Current
34. Klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` milik `Fajar N` (`Fixture.license-allocation-license.seed59Fajar`), tekan Enter
35. Klik ikon `⋯` pada baris milik sendiri
36. Verifikasi row action `Resubmit` Show pada record `Canceled` milik `Fajar Nugroho`
37. Ganti isi kotak search dengan Allocation ID seed `Canceled` milik `Doni P` (`Fixture.license-allocation-license.seed59Doni`), tekan Enter
38. Klik ikon `⋯` pada baris milik orang lain
39. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` milik orang lain (anchor menu terbuka)
40. Verifikasi row action `Resubmit` Hidden pada record `Canceled` milik orang lain
41. Buka Approvals > License Allocation dan ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
42. Verifikasi `[Review]` Show pada baris alokasi dalam scope bagi `Fajar Nugroho`
43. Verifikasi tidak ada tombol Approve atau Reject inline pada baris alokasi di Approvals
44. Buka Allocation > License Allocation, ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter, lalu klik ikon `⋯` pada baris itu
45. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Waiting for Approval` (anchor menu terbuka)
46. Verifikasi tidak ada opsi Approve atau Reject pada row action List License Allocation
47. Klik `Allocation Log` pada menu `⋯`
48. Verifikasi modal `Allocation Log` terbuka (anchor modal)
49. Verifikasi tidak ada tombol Approve atau Reject pada modal Allocation Log
50. Tutup modal dengan `[×]`

### Akun `additionalApproverLic` (TC-AC-LA-68 butir a)

51. Ganti akun: Logout lalu login sebagai Additional Approver (`additionalApproverLic`)
52. Buka Approvals > License Allocation dan ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
53. Verifikasi `[Review]` Show pada baris alokasi dalam scope bagi `Maya Tanjung`

### Akun `dewiFullLic` (TC-AC-LA-68 butir b)

54. Ganti akun: Logout lalu login sebagai Distributor Create+Read+Update (`dewiFullLic`)
55. Periksa sidebar Approvals
56. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
57. Verifikasi menu `Approvals > License Allocation` Hidden bagi `Dewi Anggraini` sehingga tidak ada `[Review]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah membuka menu `⋯`, langkah `Periksa sidebar`, langkah membuka Approvals dan List, dan ganti akun eksplisit (S-07). Subjudul `###` per akun menyebut TC dan butir Expected.
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (visibilitas row action Resubmit dan tombol Review) dan satu kelas harness (Role Matrix), data seed baca-saja yang sama, dan tiap blok akun berdiri sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Asersi tambahan (S-03): langkah 7, 12, 16, 21, 29, 39, dan 45 (`Allocation Log` Show pada menu `⋯`) serta langkah 48 (modal `Allocation Log` terbuka) adalah anchor positif pada surface yang sama sebelum asersi Hidden atau absence; alasannya bagian 8b butir 2 dan keputusan 2026-11-04 (Role Matrix Hidden pada row action wajib punya `Verifikasi` pembanding).
- Asersi `tidak ada tombol Approve atau Reject` (TC-AC-LA-68 butir c) dilakukan untuk `totalControlDistLic` sebagai sampel akun; TC menyebut `akun mana pun`, tanpa daftar akun.
- Temuan untuk QA:
  - TC-AC-LA-67 Expected b (`Hidden pada semua baris Canceled`) tidak merinci baris; spec mengasersi baris #59 Doni P dan #48 Dewi A.
  - TC-AC-LA-68 Expected c menyebut `akun mana pun` untuk absence tombol Approve/Reject tanpa daftar akun; spec memakai satu akun (`totalControlDistLic`).
  - TC-AC-LA-68 Expected c (`tidak ada tombol Approve atau Reject`) adalah absence tanpa klausa anchor di TC; spec menambah anchor di langkah 45 dan 48 (S-03).
  - TC-AC-LA-68 langkah 2 tidak menyebut cara menemukan baris di Approvals (kolom, filter diuji di TC modul Approvals); spec memakai Search Allocation ID seed #41.
