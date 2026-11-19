---
id: TC-AC-PF-E2E-059-submit-create-custom-plan-oleh-distributor-dan-partner
title: "Submit Create Custom Plan oleh Distributor dan Partner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-147
  - TC-AC-PF-148
coverage:
  web: automated
---

# Submit Create Custom Plan oleh Distributor dan Partner

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Distributor), akun #10 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_PF_DIST_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite. Ganti akun ke Total Control (Partner), akun #17 `totalControlPartner_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_PF_PARTNER_TC_PASSWORD`), dilakukan lewat langkah eksplisit. Nama env baru ini didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` v5 (Asset Name cap 50, Group count 3, Group hierarchy depth 2, Category count 20, Category hierarchy depth 2, Scheduled reports 1, API call quota 100K/month, Asset ID Configuration ON, License allocation per group ON, Open API ON, SAMP & Document Center OFF, Custom Report Builder OFF, Approval Workflow OFF, Borrowing Basic, Assignment Basic, Transfer None, Disposal Full, Accounting & Depreciation None).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth` v5) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-059`: `Paket Distributor Dua-{runId}-059` (milik Distributor) dan `Paket Partner Dua-{runId}-059` (milik Partner); keduanya tersimpan (v1). Tanggal Last Modified dibandingkan dengan waktu yang dicatat sesudah `[Submit]` (format `dd MMM yy`, Time Zone UTC, toleransi satu menit; jam server dan jam browser sinkron).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus kedua plan buatan spec lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite (Total Control Principal, `Spectra.env.AC_TC_PASSWORD`).

## Test Steps

### Distributor (TC-AC-PF-147)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Distributor Dua-{runId}-059`
4. Verifikasi form tidak memiliki checkbox `Stay on this form after submitting`
5. Klik `[Submit]`
6. Verifikasi toast sukses: "Success, custom plan has been created."
7. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active > Detail terbuka dengan judul `Paket Distributor Dua-{runId}-059 – v1`
8. Verifikasi Status Badge `Active` serta badge Product `FAMS`, Type `Custom`, dan Pricing Type `Paid`
9. Verifikasi Tab Overview memuat nilai yang sama dengan Template `Growth` v5: Group count `3`, Asset Name cap `50`, Open API `Yes`, dan API call quota `100K/month`
10. Verifikasi tidak ada baris Asset cap pada Tab Overview
11. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Distributor Dua-{runId}-059`, tekan Enter
12. Catat waktu sesudah `[Submit]` untuk perbandingan tanggal Last Modified
13. Verifikasi baris list `Paket Distributor Dua-{runId}-059` | `FAMS` | `Paid` | `v1` | `0`
14. Verifikasi tanggal Last Modified pada baris sama dengan waktu aksi (toleransi satu menit)

### Partner (TC-AC-PF-148)

15. Logout, lalu login sebagai Total Control (Partner) `totalControlPartner_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PF_PARTNER_TC_PASSWORD`
16. Buka tab `Custom`, sub-tab `Active`
17. Klik `+ Custom Plan` pada toolbar
18. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Partner Dua-{runId}-059`
19. Verifikasi form tidak memiliki checkbox `Stay on this form after submitting`
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, custom plan has been created."
22. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active > Detail terbuka dengan judul `Paket Partner Dua-{runId}-059 – v1`
23. Verifikasi Status Badge `Active` serta badge Product `FAMS`, Type `Custom`, dan Pricing Type `Paid`
24. Verifikasi Tab Overview memuat nilai yang sama dengan Template `Growth` v5: Group count `3`, Asset Name cap `50`, Open API `Yes`, dan API call quota `100K/month`
25. Verifikasi tidak ada baris Asset cap pada Tab Overview
26. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Partner Dua-{runId}-059`, tekan Enter
27. Catat waktu sesudah `[Submit]` untuk perbandingan tanggal Last Modified
28. Verifikasi baris list `Paket Partner Dua-{runId}-059` | `FAMS` | `Paid` | `v1` | `0`
29. Verifikasi tanggal Last Modified pada baris sama dengan waktu aksi (toleransi satu menit)

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 11, 12, 16, 26, 27.
- Ganti akun: akun pertama (Distributor) login di hook `before`; ganti ke Partner punya langkah eksplisit, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Langkah penghubung: Search untuk menemukan baris target (R-16) dan `Buka tab Custom, sub-tab Active` sesudah login; Search di-reset otomatis oleh Logout.
- Temuan untuk QA: (1) Post Condition TC-AC-PF-147 dan TC-AC-PF-148 (plan aktif milik entitas aktor tanpa approval, tidak ada relasi tersimpan ke Template, tidak terlihat oleh entitas lain) tidak punya langkah observasi di TC dan tidak diasersi. (2) Email akun #10 dan #17 tidak ditulis di TC selain pola `<namaAkun>_automated_{namaCompany}`; nilai `{namaCompany}` mengikuti Pre-setup TC.
