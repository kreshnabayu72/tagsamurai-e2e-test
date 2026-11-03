---
id: TC-AC-LA-E2E-013-role-matrix-entity-gate
title: "Role Matrix: Entity Gate Menu License Allocation per Entitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-55
  - TC-AC-LA-56
  - TC-AC-LA-57
  - TC-AC-LA-58
  - TC-AC-LA-59
coverage:
  web: automated
---

# Role Matrix: Entity Gate Menu License Allocation per Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`; Partner satu kantong (Pre-setup #15) `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`; user Client PT Sejahtera (Pre-setup #18) `clientUserLic_automated_{namaCompany}@qwertysystem.net` (`Sinta Dewi`), password `Spectra.env.AC_LA_CLIENT_USER_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Entitas | Akun | Hasil yang diuji |
|---|---|---|
| Principal | `totalControlLic` (`Hendra Wijaya`) | menu `License Allocation` tampil, List terbuka |
| Distributor | `dewiFullLic` (`Dewi Anggraini`) | menu `License Allocation` tampil, List terbuka |
| Partner | `partnerFullLic` (`Rian Tarigan`) | menu `License Allocation` tampil, List terbuka |
| Client | `clientUserLic` (`Sinta Dewi`) | menu tidak tampil, akses URL langsung ditolak |

- Kemampuan teknis (disediakan tim FE/BE): tetapkan dan cabut capability Manage allocation pada group Client uji untuk akun `clientUserLic` (TC-AC-LA-59 Precondition b; mekanisme tidak tertulis di TC); baca daftar alokasi dengan sesi API akun `clientUserLic` lewat fixture BE.
- State yang diubah: capability Manage allocation akun `clientUserLic` dicabut kembali di langkah penghubung akhir dan di hook `after` (Pre-setup #18 dipulihkan, suite serial).
- Data Pre-setup: #18 user Client PT Sejahtera (Pre-setup #19). Spec tidak membuat data alokasi.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-55: Entitas Principal

1. Buka dashboard Admin Console dan buka sidebar Allocation
2. Verifikasi menu `License Allocation` tampil di sidebar Allocation untuk entitas Principal
3. Klik menu `License Allocation`
4. Verifikasi List terbuka di Allocation > License Allocation tanpa error

### TC-AC-LA-56: Entitas Distributor

5. Ganti akun: Logout lalu login sebagai Distributor Create+Read+Update (`dewiFullLic`)
6. Buka dashboard Admin Console dan buka sidebar Allocation
7. Verifikasi menu `License Allocation` tampil di sidebar Allocation untuk entitas Distributor
8. Klik menu `License Allocation`
9. Verifikasi List terbuka di Allocation > License Allocation tanpa error

### TC-AC-LA-57: Entitas Partner

10. Ganti akun: Logout lalu login sebagai Partner satu kantong (`partnerFullLic`)
11. Buka dashboard Admin Console dan buka sidebar Allocation
12. Verifikasi menu `License Allocation` tampil di sidebar Allocation untuk entitas Partner
13. Klik menu `License Allocation`
14. Verifikasi List terbuka di Allocation > License Allocation tanpa error

### TC-AC-LA-58: Entitas Client tidak dapat mengakses menu

15. Ganti akun: Logout lalu login sebagai user Client (`clientUserLic`)
16. Periksa sidebar
17. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
18. Verifikasi menu `License Allocation` dan seluruh menu Allocation tidak tampil untuk entitas Client
19. Ketik URL `/admin-console/allocation/license` langsung di address bar
20. Verifikasi toast error "You don't have permission to do this." tampil
21. Verifikasi UI di-refresh
22. Verifikasi tidak ada redirect ke halaman terpisah

### TC-AC-LA-59: Entity Gate menang atas role

23. Tetapkan capability Manage allocation pada group Client uji ke akun `clientUserLic` lewat fixture backend
24. Muat ulang aplikasi lalu periksa sidebar
25. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
26. Verifikasi menu `License Allocation` tetap tidak tampil
27. Baca daftar alokasi dengan sesi API akun `clientUserLic` lewat fixture BE
28. Verifikasi tidak ada data alokasi yang dapat dibaca akun ini
29. Cabut capability Manage allocation dari akun `clientUserLic` lewat fixture backend

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah `Buka dashboard Admin Console` (precondition tiap TC), langkah `Periksa sidebar`, langkah menetapkan dan mencabut capability, dan ganti akun eksplisit (S-07).
- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30); langkah tiap entitas identik dengan hasil berbeda.
- Absence menu pada Client diawali `Verifikasi` item menu lain tampil pada sidebar yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-58 dan TC-AC-LA-59 tidak menyebut menu apa yang tampil bagi user Client; anchor memakai `sedikitnya satu item menu lain`.
  - TC-AC-LA-59 Expected b (`Tidak ada data alokasi yang dapat dibaca akun ini`) tidak memberi cara mengamati; spec memakai pembacaan lewat sesi API fixture BE tanpa endpoint karangan, dan mekanisme menetapkan capability pada akun Client tidak tertulis di TC.
  - TC-AC-LA-58 Expected b menyebut `toast error ... dan UI di-refresh, tanpa redirect ke halaman terpisah`; perilaku ini dari PRD §9.3 dan perlu dikonfirmasi bahwa halaman tetap di URL yang diketik atau kembali ke halaman sebelumnya.
