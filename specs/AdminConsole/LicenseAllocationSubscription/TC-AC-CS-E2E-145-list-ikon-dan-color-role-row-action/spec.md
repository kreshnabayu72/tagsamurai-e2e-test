---
id: TC-AC-CS-E2E-145-list-ikon-dan-color-role-row-action
title: "List: Ikon dan Color Role Row Action"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-541
coverage:
  web: automated
---

# List: Ikon dan Color Role Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, capability Create saja, Distributor PT Maju Bersama; Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`
  - `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`, capability Create saja, Partner CV Karya Mandiri; Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #69 `SUBS-20250815-00001` (Warung Kopi Senja, Active, tanpa trial), #60 `SUBS-20260810-00001` (PT Sejahtera, Trial Active), #49 `SUBS-20260819-00001` (Waiting for Approval, requester Fajar Nugroho #6), #56 `SUBS-20260805-00001` (Canceled, requester Rina Pratama #12).

## Test Steps

### TC-AC-CS-541: Ikon dan Color Role tiap row action sesuai tabel Row Actions

1. Ketik Search `SUBS-20250815-00001`, tekan Enter
2. Klik ikon `⋯` pada baris Active
3. Verifikasi Detail memakai ikon `FileInfoLine` severity dark
4. Verifikasi Subscription Log memakai ikon `FileHistoryLine` severity dark
5. Verifikasi Renew memakai ikon `RefreshLine` severity dark
6. Verifikasi Cancel Subscription memakai ikon `CloseLine` severity danger
7. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
8. Klik ikon `⋯` pada baris Trial Active
9. Verifikasi Convert memakai ikon `ExchangeLine` severity dark
10. Logout lalu login sbg Role: Create-Only (Distributor) `Fajar Nugroho`
11. Buka menu `Allocation > Client Subscription`
12. Ketik Search `SUBS-20260819-00001`, tekan Enter
13. Klik ikon `⋯` pada baris Waiting for Approval
14. Verifikasi Edit memakai ikon `Edit2Line` severity dark
15. Verifikasi Cancel Request memakai ikon `CloseLine` severity danger
16. Logout lalu login sbg Role: Create-Only (Partner) `Rina Pratama`
17. Buka menu `Allocation > Client Subscription`
18. Klik tab `History`
19. Ketik Search `SUBS-20260805-00001`, tekan Enter
20. Klik ikon `⋯` pada baris Canceled
21. Verifikasi Resubmit memakai ikon `RefreshLine` severity dark

## Notes

- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16) dan klik tab `History`. Ganti akun punya langkah eksplisit (S-07).
- Temuan untuk QA:
  - TC-AC-CS-541 tidak menyebut cara mengamati ikon dan warna (nama ikon, severity); kemampuan membaca nama ikon dan severity elemen ditulis sebagai disediakan tim FE (S-11).
  - TC-AC-CS-541 menyebut akun Create-Only Distributor `Fajar Nugroho` (#6) dan Create-Only Partner `Rina Pratama` (#12) tanpa menyebut email; email dirujuk lewat `Fixture.license-allocation-subscription`.
