---
id: TC-AC-PF-E2E-064-estimated-reference-price-create-custom-plan-aktor-distributor-sell-reference-price
title: "Estimated Reference Price Create Custom Plan oleh Distributor Memakai Sell Reference Price Wallet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-143
coverage:
  web: automated
---

# Estimated Reference Price Create Custom Plan oleh Distributor Memakai Sell Reference Price Wallet

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Create-Only (Distributor), akun #12 `createOnlyDistributor_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_PF_DIST_CO_PASSWORD`, nama env baru yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Harga W (Wallet Feature Pricing): Base Reference Price Principal: Asset Name cap 50 = $10, Group count 3 = $25, Group count 25 = $90, Open API ON = $15; Sell Reference Price Distributor: Asset Name cap 50 = $12, Group count 3 = $30, Group count 25 = $110, Open API ON = $20; field lain tanpa harga terdaftar. Dataset Plan A dengan default plan `Growth` (Asset Name cap 50, Group count 3, Open API ON). Kemampuan menyetel Wallet Feature Pricing disediakan tim FE/BE.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada (spec tidak menyimpan plan).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir dengan `[Clear Field]` sehingga form tidak dirty; hook `after` memulihkan Dataset dan Wallet Feature Pricing.

## Test Steps

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Buka dropdown Group count
5. Verifikasi opsi Group count tampil `3 (+$30)` dan `25 (+$110)`
6. Tekan Esc untuk menutup dropdown Group count
7. Verifikasi Estimated Total tampil `$62` (Asset Name cap 50 = $12, Group count 3 = $30, Open API ON = $20)
8. Klik `[Clear Field]` untuk mengembalikan form ke kondisi awal tanpa dirty

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 8.
- TC-AC-PF-143 ada di spec sendiri karena akun aktor pertamanya (Create-Only Distributor) berbeda dari spec 055 yang memakai Total Control Principal; login akun itu di hook `before` tanpa langkah ganti akun.
- Langkah penghubung: `[Clear Field]` sebagai pemulihan akhir.
- Temuan untuk QA: Expected TC-AC-PF-143 tidak menyebut opsi Asset Name cap (`50 (+$12)`) meskipun menjadi bagian total `$62`; spec tidak mengasersinya karena tidak ada Expected TC.
