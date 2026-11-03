---
id: TC-AC-LA-E2E-014-role-matrix-visibilitas-menu
title: "Role Matrix: Visibilitas Menu License Allocation dan Approvals per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-60
  - TC-AC-LA-61
  - TC-AC-LA-62
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu License Allocation dan Approvals per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor tanpa capability Manage allocation (Pre-setup #12) `noCapabilityLic_automated_{namaCompany}@qwertysystem.net` (`Tono Kusuma`), password `Spectra.env.AC_LA_NO_CAP_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Additional Approver (Pre-setup #11) `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`; Distributor Read saja (Pre-setup #7) `readCapLic_automated_{namaCompany}@qwertysystem.net` (`Bayu Aditya`), password `Spectra.env.AC_LA_DIST_READ_PASSWORD`; Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`; Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Default User Principal (Pre-setup #2) `defaultUserLic_automated_{namaCompany}@qwertysystem.net` (`Sari Pratama`), password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`; Read Only Principal (Pre-setup #3) `readOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`), password `Spectra.env.AC_LA_READ_ONLY_PASSWORD`; Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Menu `License Allocation` | Menu `Approvals > License Allocation` |
|---|---|---|
| `noCapabilityLic` (`Tono Kusuma`) | Hidden | Hidden |
| `additionalApproverLic` (`Maya Tanjung`) | Hidden | Show |
| `readCapLic` (`Bayu Aditya`) | Show | Hidden |
| `createOnlyLic` (`Doni Prasetyo`) | Show | tidak diuji |
| `gmApproveOnlyLic` (`Rian Hartono`) | Show | Show |
| `totalControlDistLic` (`Fajar Nugroho`) | Show | Show |
| `defaultUserLic` (`Sari Pratama`) | Show | tidak diuji |
| `readOnlyLic` (`Rina Wijaya`) | Show | tidak diuji |
| `dewiFullLic` (`Dewi Anggraini`) | tidak diuji | Hidden |

- Spec tidak membuat atau mengubah data; yang diuji adalah sidebar dan halaman yang terbuka dari menu.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### Akun `noCapabilityLic` (TC-AC-LA-60 butir a, TC-AC-LA-62 butir b)

1. Periksa sidebar Allocation dan sidebar Approvals
2. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
3. Verifikasi menu `License Allocation` (Allocation) Hidden (tidak dirender) bagi `Tono Kusuma`
4. Verifikasi menu `Approvals > License Allocation` Hidden bagi `Tono Kusuma`

### Akun `additionalApproverLic` (TC-AC-LA-60 butir b, TC-AC-LA-62 butir a)

5. Ganti akun: Logout lalu login sebagai Additional Approver (`additionalApproverLic`)
6. Periksa sidebar Allocation dan sidebar Approvals
7. Verifikasi menu `License Allocation` (Allocation) Hidden (tidak dirender) bagi `Maya Tanjung`; List, Allocation Log, dan Allocate tidak dapat diakses
8. Verifikasi menu `Approvals > License Allocation` Show bagi `Maya Tanjung`
9. Klik menu `Approvals > License Allocation`
10. Verifikasi halaman Approvals > License Allocation terbuka bagi `Maya Tanjung`

### Akun `readCapLic` (TC-AC-LA-61, TC-AC-LA-62 butir b)

11. Ganti akun: Logout lalu login sebagai Distributor Read (`readCapLic`)
12. Periksa sidebar Allocation dan sidebar Approvals
13. Verifikasi menu `License Allocation` Show bagi `Bayu Aditya`
14. Klik menu `License Allocation`
15. Verifikasi List terbuka bagi `Bayu Aditya` dengan data dalam scope-nya
16. Verifikasi menu `Approvals > License Allocation` Hidden bagi `Bayu Aditya`

### Akun `createOnlyLic` (TC-AC-LA-61)

17. Ganti akun: Logout lalu login sebagai Distributor Create+Read (`createOnlyLic`)
18. Periksa sidebar Allocation
19. Verifikasi menu `License Allocation` Show bagi `Doni Prasetyo`
20. Klik menu `License Allocation`
21. Verifikasi List terbuka bagi `Doni Prasetyo` dengan data dalam scope-nya

### Akun `gmApproveOnlyLic` (TC-AC-LA-61, TC-AC-LA-62 butir a)

22. Ganti akun: Logout lalu login sebagai Group Manager approve-only (`gmApproveOnlyLic`)
23. Periksa sidebar Allocation dan sidebar Approvals
24. Verifikasi menu `License Allocation` Show bagi `Rian Hartono`
25. Klik menu `License Allocation`
26. Verifikasi List terbuka bagi `Rian Hartono` dengan data dalam scope-nya
27. Verifikasi menu `Approvals > License Allocation` Show bagi `Rian Hartono`
28. Klik menu `Approvals > License Allocation`
29. Verifikasi halaman Approvals > License Allocation terbuka bagi `Rian Hartono`

### Akun `totalControlDistLic` (TC-AC-LA-61, TC-AC-LA-62 butir a)

30. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`)
31. Periksa sidebar Allocation dan sidebar Approvals
32. Verifikasi menu `License Allocation` Show bagi `Fajar Nugroho`
33. Klik menu `License Allocation`
34. Verifikasi List terbuka bagi `Fajar Nugroho` dengan data dalam scope-nya
35. Verifikasi menu `Approvals > License Allocation` Show bagi `Fajar Nugroho`
36. Klik menu `Approvals > License Allocation`
37. Verifikasi halaman Approvals > License Allocation terbuka bagi `Fajar Nugroho`

### Akun `defaultUserLic` (TC-AC-LA-61)

38. Ganti akun: Logout lalu login sebagai Default User Principal (`defaultUserLic`)
39. Periksa sidebar Allocation
40. Verifikasi menu `License Allocation` Show bagi `Sari Pratama`
41. Klik menu `License Allocation`
42. Verifikasi List terbuka bagi `Sari Pratama` dengan data dalam scope-nya

### Akun `readOnlyLic` (TC-AC-LA-61)

43. Ganti akun: Logout lalu login sebagai Read Only Principal (`readOnlyLic`)
44. Periksa sidebar Allocation
45. Verifikasi menu `License Allocation` Show bagi `Rina Wijaya`
46. Klik menu `License Allocation`
47. Verifikasi List terbuka bagi `Rina Wijaya` dengan data dalam scope-nya

### Akun `dewiFullLic` (TC-AC-LA-62 butir b)

48. Ganti akun: Logout lalu login sebagai Distributor Create+Read+Update (`dewiFullLic`)
49. Periksa sidebar Approvals
50. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
51. Verifikasi menu `Approvals > License Allocation` Hidden bagi `Dewi Anggraini`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah `Periksa sidebar`, `Klik menu`, dan ganti akun eksplisit (S-07). Langkah dikelompokkan per akun (bukan per TC) karena ganti akun menuntut Step eksplisit dan akun yang sama muncul di beberapa TC; subjudul `###` menyebut TC dan butir Expected yang diasersi.
- Spec ditulis per blok role (bagian 3a, 2026-10-30): tiap blok berdiri sendiri dan hasilnya berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (visibilitas menu per role) dan satu kelas harness (Role Matrix); sembilan akun diuji dan tiap akun adalah blok yang berdiri sendiri, sehingga kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Absence menu diawali `Verifikasi` item menu lain tampil pada sidebar yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-60 Expected b (`List, Allocation Log, dan Allocate tidak dapat diakses`) hanya ditinjau dari menu Hidden; TC tidak memberi langkah untuk mencoba akses langsung (akses URL).
  - TC-AC-LA-61 Expected b (`List terbuka ... dengan data dalam scope masing-masing`) tidak merinci data scope tiap akun; spec mengasersi List terbuka dengan data dalam scope.
