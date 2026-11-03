---
id: TC-AC-LA-E2E-006-isi-tab-current-dan-history-serta-toolbar
title: "Isi Tab Current dan History: Status per Tab dan Toolbar per Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-28
  - TC-AC-LA-29
  - TC-AC-LA-34
coverage:
  web: automated
---

# Isi Tab Current dan History: Status per Tab dan Toolbar per Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #41 alokasi `Waiting for Approval`, #46 alokasi `Pending`, #47 alokasi `Active`, #48 alokasi `Canceled`, #50 alokasi `Rejected`, #51 alokasi `Expired`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed46, seed47, seed48, seed50, seed51). Seluruh seed hanya dibaca.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-28: Tab Current hanya memuat status Waiting for Approval, Pending, dan Active

1. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
2. Verifikasi baris berstatus `Waiting for Approval` tampil pada tab Current
3. Ganti isi kotak search dengan Allocation ID seed `Pending` (`Fixture.license-allocation-license.seed46`), tekan Enter
4. Verifikasi baris berstatus `Pending` tampil pada tab Current
5. Ganti isi kotak search dengan Allocation ID seed `Active` (`Fixture.license-allocation-license.seed47`), tekan Enter
6. Verifikasi baris berstatus `Active` tampil pada tab Current
7. Ganti isi kotak search dengan Allocation ID seed `Expired` (`Fixture.license-allocation-license.seed51`), tekan Enter
8. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Expired` tidak tampil di tab Current
9. Ganti isi kotak search dengan Allocation ID seed `Rejected` (`Fixture.license-allocation-license.seed50`), tekan Enter
10. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Rejected` tidak tampil di tab Current
11. Ganti isi kotak search dengan Allocation ID seed `Canceled` (`Fixture.license-allocation-license.seed48`), tekan Enter
12. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Canceled` tidak tampil di tab Current
13. Klik `(←)` pada kotak Search

### TC-AC-LA-29: Tab History hanya memuat status Expired, Rejected, dan Canceled

14. Klik tab `History`
15. Ketik Search Allocation ID seed `Expired` (`Fixture.license-allocation-license.seed51`), tekan Enter
16. Verifikasi baris berstatus `Expired` tampil pada tab History
17. Ganti isi kotak search dengan Allocation ID seed `Rejected` (`Fixture.license-allocation-license.seed50`), tekan Enter
18. Verifikasi baris berstatus `Rejected` tampil pada tab History
19. Ganti isi kotak search dengan Allocation ID seed `Canceled` (`Fixture.license-allocation-license.seed48`), tekan Enter
20. Verifikasi baris berstatus `Canceled` tampil pada tab History
21. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
22. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Waiting for Approval` tidak tampil di tab History
23. Ganti isi kotak search dengan Allocation ID seed `Pending` (`Fixture.license-allocation-license.seed46`), tekan Enter
24. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Pending` tidak tampil di tab History
25. Ganti isi kotak search dengan Allocation ID seed `Active` (`Fixture.license-allocation-license.seed47`), tekan Enter
26. Verifikasi hasil Search kosong dengan empty state `No results found`; baris `Active` tidak tampil di tab History
27. Klik `(←)` pada kotak Search

### TC-AC-LA-34: Toolbar tab History hanya Search, Filter, dan Download

28. Klik tab `Current`
29. Amati toolbar tab Current
30. Verifikasi toolbar tab Current: Search, Filter, Download, Changelog, dan `[+ Allocation]` tampil
31. Klik tab `History`
32. Amati toolbar tab History
33. Verifikasi toolbar tab History: hanya Search, Filter, dan Download
34. Verifikasi ikon Changelog dan `[+ Allocation]` tidak dirender pada tab History

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `(←)` pada kotak Search, pindah tab, dan langkah `Amati`. Hasil Search kosong dengan empty state `No results found` dipakai sebagai anchor positif absence (bagian 8b butir 2).
- Status Completed tidak diuji di sini; TC-AC-LA-30 (Asset Control Station dan Storage tetap `Active` di tab Current sesudah Expiry Transition) ada di spec `TC-AC-LA-E2E-025-job-expiry-station-dan-storage-tetap-active`.
- Temuan untuk QA:
  - TC-AC-LA-28 dan TC-AC-LA-29 Expected menyebut seluruh baris tab (`Amati seluruh baris`) tetapi tab berisi lebih dari 30 baris dengan paginasi 10 baris; spec memeriksa tiap status dengan Search Allocation ID seed, bukan seluruh baris.
  - TC-AC-LA-28 dan TC-AC-LA-29 tidak menyebut Allocation ID seed; identitas baris dibaca dari fixture.
