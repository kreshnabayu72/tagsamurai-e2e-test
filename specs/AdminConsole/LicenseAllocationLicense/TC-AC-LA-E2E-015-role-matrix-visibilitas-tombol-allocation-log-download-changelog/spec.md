---
id: TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog
title: "Role Matrix: Visibilitas Tombol + Allocation, Row Action Allocation Log, Download, dan Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-63
  - TC-AC-LA-64
  - TC-AC-LA-44
  - TC-AC-LA-69
coverage:
  web: automated
---

# Role Matrix: Visibilitas Tombol + Allocation, Row Action Allocation Log, Download, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Read saja (Pre-setup #7) `readCapLic_automated_{namaCompany}@qwertysystem.net` (`Bayu Aditya`), password `Spectra.env.AC_LA_DIST_READ_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`; Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Additional Approver (Pre-setup #11) `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`; Distributor tanpa capability Manage allocation (Pre-setup #12) `noCapabilityLic_automated_{namaCompany}@qwertysystem.net` (`Tono Kusuma`), password `Spectra.env.AC_LA_NO_CAP_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | `[+ Allocation]` tab Current | Allocation Log row action | Download dan Changelog |
|---|---|---|---|
| `readCapLic` (`Bayu Aditya`) | Hidden | Show | Show |
| `createOnlyLic` (`Doni Prasetyo`) | Show | Show | Show |
| `totalControlDistLic` (`Fajar Nugroho`) | Show | Show | Show |
| `gmApproveOnlyLic` (`Rian Hartono`) | Hidden | Show | Show |
| `additionalApproverLic` (`Maya Tanjung`) | menu Hidden | menu Hidden | menu Hidden |
| `noCapabilityLic` (`Tono Kusuma`) | menu Hidden | menu Hidden | menu Hidden |

- Data Pre-setup yang dibaca: #41 alokasi `Waiting for Approval` dan #47 alokasi `Active`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed47). Seed hanya dibaca.
- Urutan akun: `readCapLic` (hook `before`), lalu `createOnlyLic`, `totalControlDistLic`, `gmApproveOnlyLic`, `additionalApproverLic`, `noCapabilityLic`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### Akun `readCapLic` (TC-AC-LA-63 butir b dan e, TC-AC-LA-64 butir a, TC-AC-LA-69 butir a)

1. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
2. Verifikasi `[+ Allocation]` Hidden pada toolbar tab Current bagi `Bayu Aditya`
3. Verifikasi ikon Download dan ikon Changelog Show dan aktif bagi `Bayu Aditya`
4. Klik ikon `⋯` pada baris `Waiting for Approval`
5. Verifikasi row action `Allocation Log` Show pada baris `Waiting for Approval`
6. Ganti isi kotak search dengan Allocation ID seed `Active` (`Fixture.license-allocation-license.seed47`), tekan Enter
7. Klik ikon `⋯` pada baris `Active`
8. Verifikasi row action `Allocation Log` Show pada baris `Active`
9. Klik `(←)` pada kotak Search, lalu klik tab `History`
10. Verifikasi `[+ Allocation]` tidak dirender pada tab History bagi `Bayu Aditya`
11. Klik tab `Current`

### Akun `createOnlyLic`, `totalControlDistLic`, dan `gmApproveOnlyLic` (TC-AC-LA-63, TC-AC-LA-64, TC-AC-LA-69; `gmApproveOnlyLic` juga TC-AC-LA-44)

12. Ganti akun: Logout lalu login sebagai akun baris tabel berikutnya (urutan `createOnlyLic`, `totalControlDistLic`, `gmApproveOnlyLic`; langkah 12 sampai 23 diulang tiga kali), lalu buka Allocation > License Allocation tab Current
13. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
14. Verifikasi `[+ Allocation]` pada toolbar tab Current sesuai kolom `[+ Allocation] tab Current` baris tabel akun itu
15. Verifikasi ikon Download dan ikon Changelog Show dan aktif
16. Klik ikon `⋯` pada baris `Waiting for Approval`
17. Verifikasi row action `Allocation Log` Show pada baris `Waiting for Approval`
18. Ganti isi kotak search dengan Allocation ID seed `Active` (`Fixture.license-allocation-license.seed47`), tekan Enter
19. Klik ikon `⋯` pada baris `Active`
20. Verifikasi row action `Allocation Log` Show pada baris `Active`
21. Klik `(←)` pada kotak Search, lalu klik tab `History`
22. Verifikasi `[+ Allocation]` tidak dirender pada tab History
23. Klik tab `Current`

### Akun `gmApproveOnlyLic` (TC-AC-LA-44)

24. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
25. Klik Allocation ID baris `Waiting for Approval`
26. Verifikasi modal `Allocation Log` terbuka untuk record itu
27. Tutup modal dengan `[×]`
28. Ganti isi kotak search dengan Allocation ID seed `Active` (`Fixture.license-allocation-license.seed47`), tekan Enter
29. Klik ikon `⋯` baris `Active`, lalu klik `Allocation Log`
30. Verifikasi modal `Allocation Log` terbuka untuk record `Active`
31. Tutup modal dengan `[×]`, lalu klik `(←)` pada kotak Search

### Akun `additionalApproverLic` dan `noCapabilityLic` (TC-AC-LA-63 butir f, TC-AC-LA-64 butir b, TC-AC-LA-69 butir b)

32. Ganti akun: Logout lalu login sebagai akun baris tabel berikutnya (urutan `additionalApproverLic`, `noCapabilityLic`; langkah 32 sampai 35 diulang dua kali)
33. Periksa sidebar Allocation
34. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
35. Verifikasi menu `License Allocation` Hidden sehingga `[+ Allocation]`, row action `Allocation Log`, ikon Download, dan ikon Changelog tidak ada

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `(←)` pada kotak Search, pindah tab, dan ganti akun eksplisit (S-07). Urutan akun disusun supaya `gmApproveOnlyLic` tepat sebelum blok TC-AC-LA-44.
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (visibilitas tombol dan row action pada List per role) dan satu kelas harness (Role Matrix), data seed baca-saja yang sama, dan tiap blok akun berdiri sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Langkah 12 sampai 23 diulang tiga kali (ekspansi 36 langkah) dan langkah 32 sampai 35 dua kali; parameter tiap iterasi ada di tabel `Role yang diuji`.
- Blok `gmApproveOnlyLic` TC-AC-LA-44 dijalankan sebagai blok terpisah setelah iterasi ketiga supaya sesi akun yang sama dipakai tanpa ganti akun tambahan.
- Temuan untuk QA:
  - TC-AC-LA-69 Expected a menyebut ikon Download dan Changelog `Show dan dapat dibuka`; spec mengasersi tampil dan aktif, sedangkan isi hasil membuka diuji di TC lain.
  - TC-AC-LA-63 langkah 1 menyebut `akun yang melihat menu` tanpa mengulang Additional Approver dan tanpa capability di langkah; spec mengasersi menu Hidden bagi keduanya.
  - TC-AC-LA-64 Precondition menyebut baris Pre-setup #41 dan #47 tanpa menyebut Allocation ID; spec memakai fixture seed.
