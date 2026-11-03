---
id: TC-AC-LA-E2E-024-scope-group-manager-hierarki-dan-read-only-detail
title: "Scope Group Manager Hierarki, Cancel Pending Lintas Partner, dan Tab License Detail Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-94
  - TC-AC-LA-95
  - TC-AC-LA-507
coverage:
  web: automated
---

# Scope Group Manager Hierarki, Cancel Pending Lintas Partner, dan Tab License Detail Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager dengan Manage allocation (Pre-setup #9) `gmAllocLic_automated_{namaCompany}@qwertysystem.net` (`Hadi Setiawan`), password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Read Only Principal (Pre-setup #3) `readOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`), password `Spectra.env.AC_LA_READ_ONLY_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Aksi | Data milik spec |
|---|---|---|---|
| `gmAllocLic` (`Hadi Setiawan`) | Group Manager + Manage allocation (Region Jawa) | Cancel `Pending` pada Gudang Cimahi Retail (level 3); Pending Client di luar Region Jawa tidak tampil | alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending FAMS Professional Gudang Cimahi Retail, requester `Dewi A`, Cost $3,650.00 di-Reserve (menyerupai Pre-setup #62) |
| `gmApproveOnlyLic` (`Rian Hartono`) | Group Manager approve-only | Cancel `Pending` pada Client yang dipegang Partner dalam scope group | alokasi `Pending` Concurrent User +10 ke term Pending `SUBS-20270101-C1D2F` PT Abadi Jaya, requester `Rian T`, Cost $3,650.00 di-Reserve (menyerupai Pre-setup #73) |
| `readOnlyLic` (`Rina Wijaya`) | Read Only Principal | Tab License Detail Distributor dan Detail Partner: tombol mutasi Disabled dengan tooltip | - |

- Data Pre-setup: #32 hierarki group Region Jawa > Cabang Bandung > Gudang Cimahi (Group Manager `gmAllocLic` di-assign pada Region Jawa), #25 PT Abadi Jaya, #46 alokasi `Pending` Toko Serba Ada (di luar Region Jawa, hanya dibaca), #54 (alokasi pada Distributor PT Maju Bersama dan Partner CV Karya Mandiri). Data milik spec dibuat lewat seeding backend di hook `before`, dibersihkan di hook `after`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci ownPending94, ownPending95, seed46).
- Kemampuan teknis (disediakan tim FE/BE): seeding record alokasi atas nama akun tertentu; mekanisme tidak tertulis di TC.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-94: Group Manager scope Region Jawa mencakup descendant sampai level ke-3

1. Ketik Search Allocation ID alokasi `Pending` milik spec pada Gudang Cimahi Retail (`Fixture.license-allocation-license.ownPending94`), tekan Enter
2. Verifikasi baris Pending `Gudang Cimahi Retail` (descendant level 3) tampil
3. Klik ikon `⋯` pada baris itu
4. Verifikasi row action `Cancel Allocation` Show
5. Klik `Cancel Allocation`, lalu klik `[Cancel Request]`
6. Klik tab `History`, lalu ketik Search Allocation ID `Fixture.license-allocation-license.ownPending94`, tekan Enter
7. Verifikasi Status baris: `Canceled`
8. Klik tab `Current`, lalu ketik Search Allocation ID seed `Pending` Toko Serba Ada di luar Region Jawa (`Fixture.license-allocation-license.seed46`), tekan Enter
9. Verifikasi empty state `No results found` tampil
10. Verifikasi baris Client di luar Region Jawa tidak tampil
11. Klik `(←)` pada kotak Search

### TC-AC-LA-95: Group Manager Distributor membatalkan Pending pada Client yang dipegang Partner

12. Ganti akun: Logout lalu login sebagai Group Manager approve-only (`gmApproveOnlyLic`)
13. Ketik Search Allocation ID alokasi `Pending` milik spec pada `PT Abadi Jaya` (`Fixture.license-allocation-license.ownPending95`), tekan Enter
14. Verifikasi baris `Pending` pada `PT Abadi Jaya` tampil (READ jaringan)
15. Klik ikon `⋯` pada baris itu
16. Verifikasi row action `Cancel Allocation` Show (Client dalam scope group Group Manager)
17. Klik `Cancel Allocation`, lalu klik `[Cancel Request]`
18. Klik tab `History`, lalu ketik Search Allocation ID `Fixture.license-allocation-license.ownPending95`, tekan Enter
19. Verifikasi Status baris: `Canceled`
20. Klik `(←)` pada kotak Search

### TC-AC-LA-507: Tab License pada Detail Distributor dan Detail Partner

21. Ganti akun: Logout lalu login sebagai Read Only Principal (`readOnlyLic`)
22. Buka dashboard Admin Console, lalu buka Distributor > Detail `PT Maju Bersama` > tab License
23. Verifikasi data lisensi Distributor tampil
24. Hover tombol mutasi alokasi lisensi pada Detail Distributor
25. Verifikasi tombol mutasi alokasi Disabled pada Detail Distributor
26. Verifikasi tooltip pada Detail Distributor: "You do not have permission to allocate licenses for entities in this group."
27. Buka Partner > Detail `CV Karya Mandiri` > tab License
28. Verifikasi data lisensi Partner tampil
29. Hover tombol mutasi alokasi lisensi pada Detail Partner
30. Verifikasi tombol mutasi alokasi Disabled pada Detail Partner
31. Verifikasi tooltip pada Detail Partner: "You do not have permission to allocate licenses for entities in this group."

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `Klik (←)` pada kotak Search dan pindah tab, langkah `Klik [Cancel Request]`, dan ganti akun eksplisit (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Aksi Cancel memakai record milik spec yang menyerupai Pre-setup #62 dan #73; Pre-setup bersama tidak diubah (S-06).
- Temuan untuk QA:
  - TC-AC-LA-94 langkah 3 (`Cari baris Pending Client di luar Region Jawa`) tidak menyebut Allocation ID; spec memakai seed Pre-setup #46 (Toko Serba Ada) dengan anchor empty state `No results found`.
  - TC-AC-LA-94 Expected a (`Cancel Allocation Show lalu berhasil`) tidak menyebut toast; spec mengasersi hasil lewat Status `Canceled` di tab History.
  - TC-AC-LA-507 langkah 1 dan 2 menyebut `tombol mutasi alokasi lisensi` tanpa label tombol; spec memakai istilah TC.
  - TC-AC-LA-95 Pre-setup #73 memakai term successor `SUBS-20270101-C1D2F` (Pending); Allocation ID alokasi seed tidak ditulis di TC.
