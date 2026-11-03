---
id: TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template
title: "Screening Form Create Custom Plan, Dropdown Product, dan Template"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-110
  - TC-AC-PF-123
  - TC-AC-PF-124
  - TC-AC-PF-125
  - TC-AC-PF-126
coverage:
  web: automated
---

# Screening Form Create Custom Plan, Dropdown Product, dan Template

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A (default plan FAMS aktif `Starter` (Free), `Growth`, `Professional`, `Enterprise`; default plan archived `Growth Plus (old)`; default plan SIEM Paid aktif `SIEM`) dan registry products platform FAMS, SAMS, SIEM berstatus aktif berurutan (registry disediakan tim FE/BE).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Starter`, `Growth`, `Professional`, `Enterprise`, `Growth Plus (old)`, `SIEM`) dipakai apa adanya, hanya dibaca (opsi Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada (spec tidak menyimpan plan).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir dengan form dirty; langkah pemulihan ada di bagian Pemulihan.

## Test Steps

### Screening form (TC-AC-PF-110)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Verifikasi halaman New Custom Plan terbuka dengan breadcrumb `Plans & Licensing > Plans & Features > New Custom Plan`, segmen pertama dan terakhir statis dan segmen `Plans & Features` dapat diklik
4. Verifikasi tidak ada Page Title terpisah
5. Susuri halaman dari atas ke bawah tanpa mengisi apa pun
6. Verifikasi SectionCard Plan memuat field Product (placeholder `Select product`), Template (Disabled, placeholder `Select template`), dan Plan Name (placeholder `Enter plan name`)
7. Verifikasi SectionCard Capacity Toggles memuat Asset Name cap, Group count, Group hierarchy depth, Category count, Category hierarchy depth, Scheduled reports, dan API call quota dengan nilai kosong sampai Template dipilih
8. Verifikasi SectionCard Binary Toggles memuat Asset ID Configuration, License allocation per group, Open API, SAMP & Document Center, Custom Report Builder, dan Approval Workflow
9. Verifikasi SectionCard Feature Suites memuat Borrowing, Assignment, Transfer, Disposal, dan Accounting & Depreciation
10. Verifikasi tidak ada field Brand cap, Supplier cap, TAG Features, Asset cap, Concurrent User, dan Storage di seluruh form
11. Verifikasi footer memuat Estimated Total, tombol `[Clear Field]` (text, primary), dan tombol `[Submit]` (filled, success)
12. Verifikasi tidak ada checkbox `Stay on this form after submitting` dan tidak ada tombol `[Cancel]`

### Dropdown Product (TC-AC-PF-123)

13. Klik dropdown Product
14. Verifikasi opsi berurutan `FAMS`, `SAMS`, `SIEM`
15. Verifikasi Product yang tidak aktif di registry tidak muncul (hanya ketiga opsi tersebut yang tampil)
16. Tutup dropdown Product tanpa memilih opsi (Esc)

### Field Template (TC-AC-PF-124)

17. Amati field Template sebelum memilih Product
18. Verifikasi field Template Disabled dengan placeholder `Select template`
19. Pilih Product `FAMS`
20. Verifikasi field Template aktif

### Opsi Template (TC-AC-PF-125)

21. Klik dropdown Template
22. Verifikasi opsi berurutan `Growth`, `Professional`, `Enterprise`
23. Verifikasi `Starter` (Free) dan `Growth Plus (old)` (archived) tidak ada pada opsi
24. Tutup dropdown Template (Esc)
25. Ganti Product ke `SIEM`, lalu klik dropdown Template
26. Verifikasi opsi Template hanya `SIEM`

### Ganti Product (TC-AC-PF-126)

27. Tutup dropdown Template (Esc), lalu pilih Product `FAMS` dan Template `Growth`
28. Verifikasi Group count terisi `3`
29. Ganti Product menjadi `SIEM`
30. Verifikasi Template kembali ke placeholder `Select template`
31. Verifikasi nilai Capacity Toggles, Binary Toggles, dan Feature Suites kosong sampai Template dipilih lagi

### Pemulihan

32. Klik `[Clear Field]` untuk mengembalikan form ke kondisi awal tanpa dirty

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 16, 24, 27, 32.
- Pemulihan form dirty: `[Clear Field]` mengembalikan form Create Custom Plan ke kondisi awal tanpa dialog (TC-AC-PF-153), sehingga spec tidak berakhir dengan form dirty; form full-page tidak memiliki `✕`. Dialog `Unsaved Changes` diuji di spec lain.
- Temuan untuk QA: TC-AC-PF-123 menyebut "Product tidak aktif di registry tidak muncul" tanpa menyebut Product tidak aktif yang di-seed; spec hanya mengasersi bahwa opsi yang tampil tepat tiga.
