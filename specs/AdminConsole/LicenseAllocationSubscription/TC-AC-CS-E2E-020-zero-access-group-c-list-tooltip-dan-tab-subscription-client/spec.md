---
id: TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client
title: "Zero Access Group C: List, Tooltip, dan Tab Subscription Client Detail"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-82
  - TC-AC-CS-100
  - TC-AC-CS-564
  - TC-AC-CS-634
coverage:
  web: automated
---

# Zero Access Group C: List, Tooltip, dan Tab Subscription Client Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `groupCZeroSub_automated_{namaCompany}@qwertysystem.net` (`Indra Kusuma`, Group C Zero Access, Distributor; Pre-setup #18), password `Spectra.env.AC_SUB_GROUPC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: Client `Toko Group C` (binaan langsung PT Maju Bersama pada Group C) dengan term Active `SUBS-20260401-00004` (FAMS Growth, 01/04/26 sampai 31/03/27; #128), Zero Access bagi akun `Indra Kusuma` (#18) yang tetap punya akses Tab Subscription di Client Detail.
- Kemampuan teknis: pengamatan respons jaringan atas klik baris riwayat (status 403 dan kode `FORBIDDEN_GROUP_ACCESS`, TC-AC-CS-634 Expected b) disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD (S-13).

## Test Steps

### TC-AC-CS-82: Group C Zero Access: baris tersembunyi total di list, filter, dan dropdown Client

1. Ketik Search `Toko Group C`, tekan Enter
2. Verifikasi EmptyState "No results found" tampil dan tidak ada baris term Client Group C di tab `Current`
3. Klik tab `History`
4. Ganti isi kotak search dengan `Toko Group C`, tekan Enter
5. Verifikasi EmptyState "No results found" tampil dan tidak ada baris term Client Group C di tab `History`
6. Klik ikon Filter di toolbar
7. Buka dropdown Client
8. Verifikasi dropdown filter Client memuat sedikitnya satu opsi Client lain di luar Group C
9. Verifikasi opsi filter Client tidak memuat Client Group C
10. Tutup Filter Panel
11. Klik tab `Current`
12. Klik `[+ Subscription]`
13. Buka dropdown Client
14. Verifikasi dropdown Client form memuat sedikitnya satu opsi Client lain di luar Group C
15. Verifikasi dropdown Client form tidak memuat Client Group C
16. Klik `✕` pada modal `Add Subscription`

### TC-AC-CS-100: Aksi tulis pada Tab Subscription Client Detail Disabled untuk Zero Access

17. Buka Client Detail `Toko Group C` lalu buka tab Subscription
18. Verifikasi riwayat langganan tetap tampil
19. Verifikasi tombol `[+ Subscription]`, `[Renew]`, dan `[Cancel]` berstatus Disabled
20. Arahkan kursor ke tombol `[+ Subscription]`
21. Verifikasi tooltip "You do not have permission to manage subscriptions for clients in this group."
22. Arahkan kursor ke tombol `[Renew]`
23. Verifikasi tooltip "You do not have permission to manage subscriptions for clients in this group."
24. Arahkan kursor ke tombol `[Cancel]`
25. Verifikasi tooltip "You do not have permission to manage subscriptions for clients in this group."

### TC-AC-CS-564: Tooltip tombol Disabled dapat diakses lewat keyboard focus dengan lebar maksimum 400px

26. Pindahkan fokus ke tombol `[Renew]` (Disabled) lewat tombol `Tab` tanpa memakai mouse
27. Verifikasi tooltip "You do not have permission to manage subscriptions for clients in this group." tampil saat tombol `[Renew]` mendapat keyboard focus (tanpa hover)
28. Verifikasi lebar tooltip tidak melebihi 400px
29. Verifikasi teks tooltip dibungkus ke baris berikutnya tanpa dipotong elipsis

### TC-AC-CS-634: Zero Access mengklik baris riwayat di Tab Subscription Client Detail: Subscription Detail tidak terbuka

30. Klik baris riwayat `SUBS-20260401-00004`
31. Verifikasi riwayat langganan tetap tampil, termasuk baris `SUBS-20260401-00004`
32. Verifikasi server menolak permintaan dengan `403 FORBIDDEN_GROUP_ACCESS` (ACCS-LOGIC-03c)
33. Verifikasi Subscription Detail tidak terbuka dan halaman tetap di Tab Subscription
34. Verifikasi muncul toast error "You don't have permission to do this." tanpa redirect

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik tab `Current` dan `History`, tutup Filter Panel, dan `✕` pada modal. Urutan TC: 82, 100, 564, 634 (S-10).
- TC-AC-CS-82 langkah 3 menulis "Klik [+ Subscription] jika tersedia"; spec mengikuti Expected c (dropdown Client form diasersi) dan menulis klik `[+ Subscription]` tanpa syarat karena akun `Indra Kusuma` punya Group Role Manage allocation pada Group lain.
- Anchor absence (butir 8b.2): `Verifikasi` dropdown memuat sedikitnya satu opsi Client lain (langkah 8 dan 14) mendahului absence Client Group C (langkah 9 dan 15) pada dropdown filter dan dropdown form yang sama, supaya hasil tanpa Client Group C bukan karena dropdown belum dimuat.
- Penolakan 403 pada TC-AC-CS-634 adalah akibat klik baris di UI, bukan request langsung ke server (bagian 8b butir 1 tidak berlaku).
- Temuan untuk QA:
  - TC-AC-CS-82 langkah 1 menulis "Cari Client yang berada di Group C lewat Search" tanpa nama Client; spec memakai `Toko Group C` dari Precondition.
  - TC-AC-CS-82 langkah 3 "jika tersedia" memuat kondisi bersyarat yang tidak diperbolehkan di spec (S-08/bagian 3 tidak boleh langkah bersyarat); spec menulisnya tanpa kondisi dan Preconditionnya perlu menyatakan capability Create akun #18.
  - TC-AC-CS-634 Expected b (`403 FORBIDDEN_GROUP_ACCESS`) membutuhkan pengamatan respons jaringan; kemampuan disediakan tim FE/BE (S-11).
