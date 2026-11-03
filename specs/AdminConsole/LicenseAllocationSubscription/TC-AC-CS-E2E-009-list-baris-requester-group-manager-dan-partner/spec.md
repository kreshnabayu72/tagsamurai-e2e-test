---
id: TC-AC-CS-E2E-009-list-baris-requester-group-manager-dan-partner
title: "List: Baris Requester Group Manager dan Partner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-10
  - TC-AC-CS-18
  - TC-AC-CS-53
coverage:
  web: automated
---

# List: Baris Requester Group Manager dan Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Group Manager scope Group `Jawa`, Distributor PT Maju Bersama; Pre-setup #5), password `Spectra.env.AC_SUB_GM_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`, capability Create saja, Partner CV Karya Mandiri; Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`
  - `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`, Total Control, Partner CV Karya Mandiri; Pre-setup #11), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #57 `SUBS-20260819-00002` (Percetakan Mega, FAMS Professional, Pending, 15/09/26 sampai 14/09/27, Plan Owner PT Maju Bersama; requester original aktor Group Manager bypass) dan #56 `SUBS-20260805-00001` (Optik Cahaya, FAMS Growth, Canceled, Plan Owner CV Karya Mandiri; requester original `Rina Pratama` #12, bukan `Lestari Wulandari` #11).
- Toggle Require Approval for Allocation ON untuk CV Karya Mandiri (#23); tidak diubah spec.

## Test Steps

### TC-AC-CS-10: Baris term Pending di tab Current: tanggal terisi dan row action

1. Ketik Search `SUBS-20260819-00002`, tekan Enter
2. Klik ikon `⋯` pada baris itu
3. Verifikasi kolom Status menampilkan badge "Pending" severity warning
4. Verifikasi Start Date `15/09/26` dan End Date `14/09/27` tampil
5. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Edit, Cancel Request
6. Verifikasi Cancel Subscription dan Renew tidak ada di menu
7. Klik `(←)` pada kotak Search
8. Logout lalu login sbg Role: Create-Only (Partner) `Rina Pratama`
9. Buka menu `Allocation > Client Subscription`

### TC-AC-CS-18: Baris Canceled di tab History: Resubmit hanya untuk requester original

10. Klik tab `History`
11. Ketik Search `SUBS-20260805-00001`, tekan Enter
12. Klik ikon `⋯` pada baris itu
13. Verifikasi badge Status "Canceled" severity danger pada baris itu
14. Verifikasi menu baris `SUBS-20260805-00001` berisi tepat: Detail, Subscription Log, Resubmit

### TC-AC-CS-53: Tombol Resubmit pada Detail term Canceled untuk requester original

15. Klik baris `SUBS-20260805-00001`
16. Verifikasi tombol aksi Detail: Resubmit, Subscription Log
17. Klik tombol Resubmit
18. Verifikasi form `+ Subscription` terbuka ter-isi dari record `SUBS-20260805-00001`
19. Klik `✕` pada form
20. Klik segmen `Client Subscription` pada Breadcrumb
21. Logout lalu login sbg Role: Total Control (Partner) `Lestari Wulandari`
22. Buka menu `Allocation > Client Subscription`

### TC-AC-CS-18: Baris Canceled di tab History: tampilan bagi Total Control Partner yang bukan requester

23. Klik tab `History`
24. Ketik Search `SUBS-20260805-00001`, tekan Enter
25. Klik ikon `⋯` pada baris itu
26. Verifikasi menu baris `SUBS-20260805-00001` bagi Total Control (Partner) yang bukan requester berisi tepat dua item: Detail, Subscription Log

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, klik tab `History`, tutup form lewat `✕`, dan klik segmen `Client Subscription` pada Breadcrumb. Ganti akun punya langkah eksplisit (S-07).
- Urutan TC: 10, 18 (bagian requester), 53, 18 (bagian Total Control Partner) supaya akun Partner requester dipakai berurutan dan pindah akun hanya dua kali (S-10). TC-AC-CS-18 muncul dua kali dengan subjudul yang sama.
- Temuan untuk QA:
  - TC-AC-CS-10 tidak menyebut apakah aktor Group Manager `Dewi Anggraini` adalah requester dari baris itu selain Precondition ("aktor adalah requester original (bypass)"); data Pre-setup #57 menyebut requester original `Dewi A`.
  - TC-AC-CS-53 Expected b (Resubmit membuka form terisi) tidak menyebut apakah form dirty untuk dialog `Unsaved Changes`; spec menutup form dengan `✕` tanpa Verifikasi dialog (S-08 butir tidak berlaku bila form tidak berubah).
