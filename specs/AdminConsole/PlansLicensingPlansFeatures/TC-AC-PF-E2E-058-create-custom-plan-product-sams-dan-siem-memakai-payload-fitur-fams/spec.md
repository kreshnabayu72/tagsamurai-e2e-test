---
id: TC-AC-PF-E2E-058-create-custom-plan-product-sams-dan-siem-memakai-payload-fitur-fams
title: "Create Custom Plan Product SAMS dan SIEM Memakai Payload Fitur FAMS"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-150
  - TC-AC-PF-151
coverage:
  web: automated
---

# Create Custom Plan Product SAMS dan SIEM Memakai Payload Fitur FAMS

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan S (Template SAMS Paid `Supply Pro`) dan Dataset Plan A (Template SIEM Paid `SIEM`).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Supply Pro`, `SIEM`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-058`: `Paket SAMS Baru-{runId}-058` dan `Paket SIEM Baru-{runId}-058`; keduanya tersimpan.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-058`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Product SAMS (TC-AC-PF-150)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `SAMS`
4. Pilih Template `Supply Pro`
5. Amati SectionCard Capacity Toggles, Binary Toggles, dan Feature Suites
6. Verifikasi ketiga SectionCard memuat field-set yang sama dengan Product FAMS: Capacity Toggles (Asset Name cap, Group count, Group hierarchy depth, Category count, Category hierarchy depth, Scheduled reports, API call quota), Binary Toggles (Asset ID Configuration, License allocation per group, Open API, SAMP & Document Center, Custom Report Builder, Approval Workflow), dan Feature Suites (Borrowing, Assignment, Transfer, Disposal, Accounting & Depreciation)
7. Isi Plan Name `Paket SAMS Baru-{runId}-058` lalu klik `[Submit]`
8. Verifikasi toast sukses: "Success, custom plan has been created."
9. Verifikasi Plan Detail menampilkan badge Product `SAMS`

### Product SIEM (TC-AC-PF-151)

10. Klik breadcrumb sub-tab `Active`
11. Klik `+ Custom Plan` pada toolbar
12. Pilih Product `SIEM`
13. Pilih Template `SIEM`
14. Amati SectionCard Capacity Toggles, Binary Toggles, dan Feature Suites
15. Verifikasi ketiga SectionCard memuat field-set yang sama dengan Product FAMS: Capacity Toggles (Asset Name cap, Group count, Group hierarchy depth, Category count, Category hierarchy depth, Scheduled reports, API call quota), Binary Toggles (Asset ID Configuration, License allocation per group, Open API, SAMP & Document Center, Custom Report Builder, Approval Workflow), dan Feature Suites (Borrowing, Assignment, Transfer, Disposal, Accounting & Depreciation)
16. Isi Plan Name `Paket SIEM Baru-{runId}-058` lalu klik `[Submit]`
17. Verifikasi toast sukses: "Success, custom plan has been created."
18. Verifikasi Plan Detail menampilkan badge Product `SIEM`

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 10.
- Langkah penghubung: breadcrumb sub-tab `Active` untuk membuka form baru setelah plan tersimpan; spec berakhir pada Plan Detail tanpa form dirty.
- Temuan untuk QA: (1) Expected a menyebut "field-set yang sama dengan Product FAMS (placeholder sampai field-set SAMS/SIEM ditetapkan)"; spec mengasersi daftar field FAMS dari TC-AC-PF-110 dan tidak mengasersi nilainya. (2) Dataset Plan S (SAMS Paid `Supply Pro`) bertentangan dengan Dataset Plan W TC-AC-PF-127 (SAMS tanpa plan Paid); keduanya dipakai di spec berbeda dan Dataset dipulihkan di antaranya.
