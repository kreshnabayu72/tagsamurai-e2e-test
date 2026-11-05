---
id: TC-AC-LA-E2E-021-role-matrix-positif-cancel-pending-dan-approve-per-peran
title: "Role Matrix Positif: Cancel Pending dan Approve oleh Group Manager, Total Control, dan Additional Approver"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-78
  - TC-AC-LA-79
  - TC-AC-LA-81
coverage:
  web: automated
---

# Role Matrix Positif: Cancel Pending dan Approve oleh Group Manager, Total Control, dan Additional Approver

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager approve-only (Pre-setup #8) `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Additional Approver (Pre-setup #11) `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Aksi | Data milik spec |
|---|---|---|---|
| `gmApproveOnlyLic` (`Rian Hartono`) | Group Manager approve-only | Cancel alokasi `Pending` milik `Dewi A` | alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester `Dewi A`, Cost $3,650.00 di-Reserve (menyerupai Pre-setup #46) |
| `totalControlDistLic` (`Fajar Nugroho`) | Total Control Distributor | Cancel alokasi `Pending` milik `Dewi A` | alokasi `Pending` kedua dengan data yang sama |
| `additionalApproverLic` (`Maya Tanjung`) | Additional Approver | Approve dari Approvals | alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester `Dewi A`, Cost $150.00 di-Reserve (menyerupai Pre-setup #41) |

- Data milik spec dibuat lewat seeding backend di hook `before` dan dibersihkan di hook `after`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci ownPending78, ownPending79, ownWaiting81). Pre-setup lain: #21 Toko Serba Ada, #19 PT Sejahtera, #33 saldo kantong wallet, #38 Require Approval ON (toggle ON untuk record `Waiting for Approval`).
- Kemampuan teknis (disediakan tim FE/BE): baca Reserve kantong Distributor PT Maju Bersama dan baca status record (`Completed` berstatus lisensi) lewat fixture BE.
- Urutan akun: `gmApproveOnlyLic` (hook `before`), `totalControlDistLic`, `additionalApproverLic`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-78: Group Manager approve-only membatalkan alokasi Pending milik orang lain

1. Catat Reserve kantong Distributor PT Maju Bersama sebagai baseline lewat fixture BE
2. Ketik Search Allocation ID alokasi `Pending` milik spec (`Fixture.license-allocation-license.ownPending78`), tekan Enter
3. Klik row action `Cancel Allocation` pada baris `Pending` milik `Dewi A`
4. Klik `[Cancel Request]`
5. Verifikasi toast sukses: "Success, license allocation has been canceled."
6. Klik tab `History`, lalu ketik Search Allocation ID `Fixture.license-allocation-license.ownPending78`, tekan Enter
7. Verifikasi Status baris: `Canceled`
8. Klik row action `Allocation Log` pada baris itu
9. Verifikasi entri Allocation Log: `Allocation canceled by Rian H`
10. Tutup modal dengan `[×]`
11. Verifikasi Reserve kantong Distributor berkurang $3,650.00 dari baseline (Reserve dilepas)

### TC-AC-LA-79: Total Control Distributor membatalkan alokasi Pending milik orang lain

12. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`), lalu buka Allocation > License Allocation tab Current
13. Ketik Search Allocation ID alokasi `Pending` milik spec (`Fixture.license-allocation-license.ownPending79`), tekan Enter
14. Klik row action `Cancel Allocation` pada baris `Pending` milik `Dewi A`
15. Klik `[Cancel Request]`
16. Verifikasi toast sukses: "Success, license allocation has been canceled."
17. Klik tab `History`, lalu ketik Search Allocation ID `Fixture.license-allocation-license.ownPending79`, tekan Enter
18. Verifikasi Status baris: `Canceled`
19. Klik row action `Allocation Log` pada baris itu
20. Verifikasi entri Allocation Log: `Allocation canceled by Fajar N`
21. Tutup modal dengan `[×]`

### TC-AC-LA-81: Additional Approver menyetujui dari Approvals

22. Ganti akun: Logout lalu login sebagai Additional Approver (`additionalApproverLic`)
23. Buka Approvals > License Allocation dan ketik Search Allocation ID alokasi `Waiting for Approval` milik spec (`Fixture.license-allocation-license.ownWaiting81`), tekan Enter
24. Klik `[Review]` pada alokasi
25. Pilih Approve lalu klik Submit
26. Tunggu aksi selesai
27. Verifikasi keputusan Approve berhasil diproses dan alokasi menjadi `Completed` berstatus lisensi `Active` (dibaca lewat fixture BE)
28. Verifikasi sedikitnya satu item menu lain tampil pada sidebar
29. Verifikasi menu `License Allocation` tetap Hidden bagi `Maya Tanjung`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah baseline Reserve, langkah `Tunggu aksi selesai`, penutupan modal, pindah tab, dan ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Aksi Cancel dan Approve memakai record milik spec yang menyerupai Pre-setup #46 dan #41; Pre-setup bersama tidak diubah (S-06).
- Temuan untuk QA:
  - TC-AC-LA-81 langkah 3 (`Pilih Approve lalu Submit`) tidak menyebut kontrol dan teks UI di halaman Review Approvals (diuji di TC modul Approvals); spec mengikuti teks TC.
  - TC-AC-LA-81 Expected a (`alokasi menjadi Completed berstatus lisensi Active`) tidak punya cara observasi di UI untuk akun tanpa akses menu License Allocation; spec membacanya lewat fixture BE (disediakan tim FE/BE).
  - TC-AC-LA-81 Post Condition (`Entri Allocation Log Allocation approved by Maya T`) tidak punya langkah observasi dan tidak diasersi.
  - TC-AC-LA-78 Expected b (`Reserve dilepas`) dan Post Condition (`Reserve $3,650.00 dilepas`) tidak memberi cara membaca Reserve; spec memakai kemampuan baca Reserve lewat fixture BE.
