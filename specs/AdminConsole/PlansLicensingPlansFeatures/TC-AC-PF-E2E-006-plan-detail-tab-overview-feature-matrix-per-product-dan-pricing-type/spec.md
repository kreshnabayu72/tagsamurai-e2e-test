---
id: TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type
title: "Plan Detail Tab Overview: Feature Matrix per Product dan Pricing Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-32
  - TC-AC-PF-33
  - TC-AC-PF-34
  - TC-AC-PF-35
coverage:
  web: automated
---

# Plan Detail Tab Overview: Feature Matrix per Product dan Pricing Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21): default `Starter` (FAMS, Free; nilai Pre-setup: Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, Asset ID Configuration No, License allocation per group No, Scheduled reports —, Approval Workflow No, Borrowing None, Assignment None, Transfer None, Disposal None, SAMP & Document Center No, Accounting & Depreciation None, Custom Report Builder No, Open API No, API call quota —), `Professional` (FAMS, Paid; Group count 25, Group hierarchy depth 5, Category count 100, Category hierarchy depth 5, Asset Name cap 500, Asset ID Configuration Yes, License allocation per group Yes, Scheduled reports Unlimited, Approval Workflow Yes, Borrowing Full, Assignment Full, Transfer Full, Disposal Full, SAMP & Document Center No, Accounting & Depreciation Single Depreciation, Custom Report Builder Yes, Open API Yes, API call quota 1M/month), `SIEM` (SIEM, Paid, v1), custom `Growth Tier` (FAMS, Paid, v20); Dataset Plan S (Pre-setup #31): default SAMS `Supply Starter` (Free) dan `Supply Pro` (Paid). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama dan nilai Plan Pre-setup literal tanpa suffix (`Starter`, `Professional`, `SIEM`, `Growth Tier`, `Supply Pro`) dipakai karena menentukan asersi teks dan nilai fitur; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-32: Tab Overview default plan Free FAMS menampilkan fitur dengan nilai Free termasuk Asset cap dan Suites None

1. Klik teks `Starter` pada kolom Plan Name untuk membuka Plan Detail `Starter`
2. Susuri SectionCard `Fixed Asset Module` dari atas ke bawah
3. Verifikasi SectionCard `Fixed Asset Module` memuat urutan fitur: TAG Features, Asset cap, Group count, Group hierarchy depth, Category count, Category hierarchy depth, Asset Name cap, Asset ID Configuration, License allocation per group, Scheduled reports, Approval Workflow, Borrowing, Assignment, Transfer, Disposal, SAMP & Document Center, Accounting & Depreciation, Custom Report Builder, Open API, API call quota
4. Verifikasi nilai: TAG Features `QR Only`; Asset cap `25`; Group count `1`; Group hierarchy depth `1`; Category count `5`; Category hierarchy depth `1`; Asset Name cap `10`; Asset ID Configuration `No`; License allocation per group `No`; Scheduled reports `—`; Approval Workflow `No`; Borrowing `None`; Assignment `None`; Transfer `None`; Disposal `None`; SAMP & Document Center `No`; Accounting & Depreciation `None`; Custom Report Builder `No`; Open API `No`; API call quota `—`
5. Verifikasi Brand cap, Supplier cap, dan TAG access tidak muncul di Tab Overview

### TC-AC-PF-33: Tab Overview default plan Paid FAMS menampilkan TAG Features All TAGs tanpa baris Asset cap

6. Klik menu Plans & Licensing > Plans & Features di sidebar
7. Klik teks `Professional` pada kolom Plan Name untuk membuka Plan Detail `Professional`
8. Susuri SectionCard `Fixed Asset Module`
9. Verifikasi baris TAG Features bernilai `All TAGs`
10. Verifikasi baris Asset cap tidak muncul
11. Verifikasi nilai: Group count `25`; Group hierarchy depth `5`; Category count `100`; Category hierarchy depth `5`; Asset Name cap `500`; Asset ID Configuration `Yes`; License allocation per group `Yes`; Scheduled reports `Unlimited`; Approval Workflow `Yes`; Borrowing `Full`; Assignment `Full`; Transfer `Full`; Disposal `Full`; SAMP & Document Center `No`; Accounting & Depreciation `Single Depreciation`; Custom Report Builder `Yes`; Open API `Yes`; API call quota `1M/month`

### TC-AC-PF-34: Tab Overview custom plan FAMS menampilkan TAG Features All TAGs tanpa baris Asset cap

12. Klik menu Plans & Licensing > Plans & Features di sidebar
13. Klik tab Custom
14. Klik teks `Growth Tier` pada kolom Plan Name untuk membuka Plan Detail `Growth Tier`
15. Verifikasi SectionCard `Fixed Asset Module` tampil dengan baris TAG Features bernilai `All TAGs`
16. Verifikasi baris Asset cap tidak muncul untuk custom plan

### TC-AC-PF-35: Tab Overview plan SAMS dan SIEM menampilkan section Supply Asset Module dan SIEM Module dengan payload fitur FAMS sebagai placeholder

17. Klik menu Plans & Licensing > Plans & Features di sidebar
18. Klik teks `Supply Pro` pada kolom Plan Name untuk membuka Plan Detail `Supply Pro`
19. Verifikasi satu SectionCard dengan nama `Supply Asset Module` tampil, bukan section gabungan FAMS dan SAMS
20. Verifikasi daftar fitur memakai payload fitur FAMS (TAG Features sampai API call quota) sebagai placeholder sampai field-set SAMS ditetapkan
21. Klik menu Plans & Licensing > Plans & Features di sidebar
22. Klik teks `SIEM` pada kolom Plan Name untuk membuka Plan Detail `SIEM`
23. Verifikasi satu SectionCard dengan nama `SIEM Module` tampil
24. Verifikasi SectionCard `SIEM Module` memuat payload fitur FAMS sebagai placeholder sampai field-set SIEM ditetapkan

## Notes

- Langkah penghubung (S-03): klik menu sidebar pada langkah 6, 12, 17, dan 21 mengembalikan layar ke list Default > Active sebelum membuka Plan Detail berikutnya; klik tab Custom pada langkah 13 mengarahkan layar ke tab yang disyaratkan TC-AC-PF-34. Langkah 2 dan 8 ("Susuri SectionCard") adalah langkah observasi TC tanpa aksi lain.
- Daftar nilai fitur pada langkah 4 dan 11 ditulis dalam satu `Verifikasi` per Expected butir b TC dan seluruh pasangan fitur dan nilai tetap diasersi (S-01, daftar komposit yang disebut utuh dalam satu butir Expected).
- Temuan untuk QA:
  - TC-AC-PF-35: Expected tidak menyebut nama fitur placeholder untuk plan SIEM selain "payload fitur FAMS"; spec mengikuti kalimat TC tanpa menambah daftar nilai.
