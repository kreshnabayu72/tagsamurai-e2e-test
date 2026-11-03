---
id: TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner
title: "Scope Baca per Entitas dan Plan Owner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-91
  - TC-AC-CS-92
  - TC-AC-CS-93
  - TC-AC-CS-393
  - TC-AC-CS-431
  - TC-AC-CS-465
coverage:
  web: automated
---

# Scope Baca per Entitas dan Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, Total Control, Distributor PT Maju Bersama; Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`
  - `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`, Total Control, Partner CV Karya Mandiri; Pre-setup #11), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: Client `PT Multi Cabang` (binaan Principal dan PT Maju Bersama) dengan tiga term Active: FAMS (Plan Owner PT Maju Bersama), SAMS (CV Karya Mandiri), SIEM (CV Sinar Abadi dari jaringan PT Nusa Link) (#102); dataset 120 baris term di tab Current dan 60 di tab History untuk Plan Owner PT Maju Bersama dan CV Karya Mandiri (#82); Changelog Client Subscription 24 entri contoh (#84).
- Kemampuan teknis: pembacaan berkas unduhan CSV (nama, isi baris) untuk TC-AC-CS-393, disediakan tim FE.
- Tabel "Role yang diuji": Total Control Principal (#1, TC-AC-CS-91), Total Control Distributor (#9, TC-AC-CS-92), Total Control Partner (#11, TC-AC-CS-93, 393, 431, 465).

## Test Steps

### TC-AC-CS-91: Principal melihat seluruh baris dalam scope dan dapat bertindak atas semua Client

1. Ketik Search `PT Multi Cabang`, tekan Enter
2. Verifikasi tiga baris PT Multi Cabang tampil (FAMS, SAMS, SIEM)
3. Klik `[+ Subscription]`
4. Buka dropdown Client
5. Verifikasi dropdown Client memuat Client dari semua Distributor dan Partner (scope WRITE Principal = semua Client)
6. Klik `✕` pada modal `Add Subscription`
7. Klik `(←)` pada kotak Search

### TC-AC-CS-92: Distributor melihat baris miliknya dan Partner di bawahnya, bukan jaringan lain

8. Logout lalu login sbg Role: Total Control (Distributor) `Eko Saputra`
9. Buka menu `Allocation > Client Subscription`
10. Ketik Search `PT Multi Cabang`, tekan Enter
11. Verifikasi dua baris tampil: FAMS Plan Owner `PT Maju Bersama (Distributor)` dan SAMS Plan Owner `CV Karya Mandiri (Partner)`
12. Verifikasi baris SIEM milik `CV Sinar Abadi` tidak tampil
13. Klik `(←)` pada kotak Search

### TC-AC-CS-93: Partner hanya melihat baris dengan Plan Owner dirinya sendiri

14. Logout lalu login sbg Role: Total Control (Partner) `Lestari Wulandari`
15. Buka menu `Allocation > Client Subscription`
16. Ketik Search `PT Multi Cabang`, tekan Enter
17. Verifikasi satu baris tampil: SAMS Plan Owner `CV Karya Mandiri (Partner)`
18. Verifikasi baris FAMS milik PT Maju Bersama dan baris SIEM milik CV Sinar Abadi tidak tampil
19. Klik `(←)` pada kotak Search

### TC-AC-CS-393: Download mengikuti scope baris pengguna

20. Klik ikon Download
21. Pilih `Download as CSV`
22. Verifikasi berkas memuat sedikitnya satu baris Plan Owner `CV Karya Mandiri (Partner)`
23. Verifikasi berkas hanya memuat baris yang tampil bagi Partner (Plan Owner `CV Karya Mandiri (Partner)`)
24. Verifikasi baris Plan Owner lain tidak ada pada berkas

### TC-AC-CS-431: Entri Changelog mengikuti scope READ per baris

25. Klik ikon Changelog di toolbar
26. Verifikasi modal Changelog memuat sedikitnya satu entri atas term Plan Owner `CV Karya Mandiri (Partner)`
27. Verifikasi hanya entri atas term yang boleh dibaca Partner (Plan Owner `CV Karya Mandiri (Partner)`) yang tampil
28. Verifikasi entri atas term Plan Owner lain, termasuk baris Trial, tidak tampil
29. Klik `✕` pada modal Changelog

### TC-AC-CS-465: Baris log di luar scope READ tidak muncul di Changelog dan Activity Log

30. Klik ikon Changelog di toolbar
31. Verifikasi modal Changelog memuat sedikitnya satu entri atas term Plan Owner `CV Karya Mandiri (Partner)`
32. Verifikasi hanya entri atas term dalam scope READ Partner tampil di modal Changelog
33. Verifikasi entri atas term yang tidak boleh dibaca, termasuk baris Trial, tidak tampil di modal Changelog
34. Klik `✕` pada modal Changelog
35. Buka Admin Console > Activity Log lalu saring Object `Client Subscription`
36. Verifikasi Activity Log memuat sedikitnya satu entri atas term Plan Owner `CV Karya Mandiri (Partner)`
37. Verifikasi hanya entri atas term dalam scope READ Partner tampil di Activity Log
38. Verifikasi entri atas term yang tidak boleh dibaca, termasuk baris Trial, tidak tampil di Activity Log

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok akun karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, dan `✕` pada modal. Spec read-only; tidak menulis data dan Changelog tidak bertambah.
- Ukuran: 38 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (scope baca read-only per entitas dan Plan Owner) dengan tiga akun yang berganti secara eksplisit, dan pertambahan langkah berasal dari Verifikasi pembanding `sedikitnya satu` pada tiap surface (S-01, bagian 8b butir 2); pemecahan menambah login ulang tanpa menambah isolasi.
- Asersi isi Changelog dan Activity Log memakai entri seed (#84 dan seed #82) dan bukan entri baru atau angka absolut total (S-12, S-14).
- Temuan untuk QA:
  - TC-AC-CS-393 dan TC-AC-CS-431 tidak menyebut cara membedakan entri atau baris per Plan Owner pada berkas dan pada Changelog; spec memakai kolom Plan Owner pada baris berkas dan teks entri seed (S-15).
  - TC-AC-CS-465 menyebut dua surface (modal Changelog dan Activity Log) dalam satu langkah dan satu Expected; spec memecahnya per surface.
  - TC-AC-CS-431 dan TC-AC-CS-465 mengasersi "hanya entri" tanpa menyebut pembanding; spec menulis Verifikasi `sedikitnya satu entri` atas term Plan Owner `CV Karya Mandiri (Partner)` pada tiap surface (modal Changelog, Activity Log) dan `sedikitnya satu baris` pada berkas CSV sebelum asersi `hanya` (bagian 8b butir 2).
