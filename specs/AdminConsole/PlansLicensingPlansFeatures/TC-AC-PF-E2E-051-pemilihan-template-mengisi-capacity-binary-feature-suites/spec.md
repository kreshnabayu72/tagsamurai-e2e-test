---
id: TC-AC-PF-E2E-051-pemilihan-template-mengisi-capacity-binary-feature-suites
title: "Pemilihan Template Mengisi Capacity, Binary, Feature Suites, dan Opsi Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-128
  - TC-AC-PF-129
coverage:
  web: automated
---

# Pemilihan Template Mengisi Capacity, Binary, Feature Suites, dan Opsi Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` v5 (Asset Name cap 50, Group count 3, Group hierarchy depth 2, Category count 20, Category hierarchy depth 2, Scheduled reports 1, API call quota 100K/month, Asset ID Configuration ON, License allocation per group ON, Open API ON, SAMP & Document Center OFF, Custom Report Builder OFF, Approval Workflow OFF, Borrowing Basic, Assignment Basic, Transfer None, Disposal Basic, Accounting & Depreciation None).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth` v5) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada (spec tidak menyimpan plan).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir dengan `[Clear Field]` sehingga form tidak dirty; hook `after` memulihkan Dataset.

## Test Steps

### Isi nilai Template (TC-AC-PF-128)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS`
4. Pilih Template `Growth`
5. Verifikasi Capacity Toggles: Asset Name cap `50`, Group count `3`, Group hierarchy depth `2`, Category count `20`, Category hierarchy depth `2`, Scheduled reports `1`, API call quota `100K/month`
6. Verifikasi Binary Toggles: Asset ID Configuration ON, License allocation per group ON, Open API ON, SAMP & Document Center OFF, Custom Report Builder OFF, Approval Workflow OFF
7. Verifikasi Feature Suites aktif (tidak terkunci): Borrowing `Basic`, Assignment `Basic`, Transfer `None`, Disposal `Basic`, Accounting & Depreciation `None`

### Opsi dropdown (TC-AC-PF-129)

8. Buka dropdown Asset Name cap
9. Verifikasi opsi Asset Name cap: `10`, `50`, `500`, `Unlimited`
10. Tekan Esc, lalu buka dropdown Group count
11. Verifikasi opsi Group count: `1`, `3`, `25`, `Unlimited`
12. Tekan Esc, lalu buka dropdown Group hierarchy depth
13. Verifikasi opsi Group hierarchy depth: `1`, `2`, `5`, `Unlimited`
14. Tekan Esc, lalu buka dropdown Category count
15. Verifikasi opsi Category count: `5`, `20`, `100`, `Unlimited`
16. Tekan Esc, lalu buka dropdown Category hierarchy depth
17. Verifikasi opsi Category hierarchy depth: `1`, `2`, `5`, `Unlimited`
18. Tekan Esc, lalu buka dropdown Scheduled reports
19. Verifikasi opsi Scheduled reports: `—`, `1`, `5`, `Unlimited`
20. Tekan Esc, lalu buka dropdown API call quota
21. Verifikasi opsi API call quota: `100K/month`, `1M/month`, `Custom`
22. Tekan Esc, lalu buka dropdown Borrowing
23. Verifikasi opsi Borrowing: `None`, `Basic`, `Full`
24. Tekan Esc, lalu buka dropdown Assignment
25. Verifikasi opsi Assignment: `None`, `Basic`, `Full`
26. Tekan Esc, lalu buka dropdown Transfer
27. Verifikasi opsi Transfer: `None`, `Basic`, `Full`
28. Tekan Esc, lalu buka dropdown Disposal
29. Verifikasi opsi Disposal: `None`, `Basic`, `Full`
30. Tekan Esc, lalu buka dropdown Accounting & Depreciation
31. Verifikasi opsi Accounting & Depreciation: `None`, `Single Depreciation`, `Multi Depreciation`
32. Tekan Esc, lalu klik `[Clear Field]` untuk mengembalikan form ke kondisi awal tanpa dirty

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32.
- Pengelompokan `Verifikasi` (S-01): nilai satu SectionCard yang disebut utuh dalam satu butir Expected TC-AC-PF-128 (a, b, c) ditulis satu `Verifikasi` per butir; setiap dropdown pada TC-AC-PF-129 punya `Verifikasi` sendiri.
- Langkah penghubung: tutup dropdown dengan Esc sebelum membuka dropdown berikutnya, dan `[Clear Field]` sebagai pemulihan akhir; tidak ada dialog `Unsaved Changes` karena form dikembalikan ke kondisi awal (TC-AC-PF-153).
