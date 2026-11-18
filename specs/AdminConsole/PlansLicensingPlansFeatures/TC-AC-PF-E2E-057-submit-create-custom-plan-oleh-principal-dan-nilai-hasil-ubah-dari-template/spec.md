---
id: TC-AC-PF-E2E-057-submit-create-custom-plan-oleh-principal-dan-nilai-hasil-ubah-dari-template
title: "Submit Create Custom Plan oleh Principal dan Nilai Hasil Ubah dari Template"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-146
  - TC-AC-PF-149
coverage:
  web: automated
---

# Submit Create Custom Plan oleh Principal dan Nilai Hasil Ubah dari Template

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` v5 (Asset Name cap 50, Group count 3, Group hierarchy depth 2, Category count 20, Category hierarchy depth 2, Scheduled reports 1, API call quota 100K/month, Asset ID Configuration ON, License allocation per group ON, Open API ON, SAMP & Document Center OFF, Custom Report Builder OFF, Approval Workflow OFF, Borrowing Basic, Assignment Basic, Transfer None, Disposal Full, Accounting & Depreciation None).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth` v5) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-057`: `Paket Principal Baru-{runId}-057` dan `Paket Override-{runId}-057`; keduanya tersimpan (v1). Tanggal Last Modified dibandingkan dengan waktu yang dicatat sesudah `[Submit]` (format `dd MMM yy`, Time Zone UTC, toleransi satu menit; jam server dan jam browser sinkron).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-057`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Submit oleh Principal (TC-AC-PF-146)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Principal Baru-{runId}-057`
4. Verifikasi form tidak memiliki checkbox `Stay on this form after submitting`
5. Klik `[Submit]`
6. Verifikasi toast sukses: "Success, custom plan has been created."
7. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active > Detail terbuka dengan judul `Paket Principal Baru-{runId}-057 – v1`
8. Verifikasi Status Badge `Active` serta badge Product `FAMS`, Type `Custom`, dan Pricing Type `Paid`
9. Verifikasi Tab Overview memuat nilai yang sama dengan Template `Growth` v5: Group count `3`, Asset Name cap `50`, Open API `Yes`, dan API call quota `100K/month`
10. Verifikasi tidak ada baris Asset cap pada Tab Overview
11. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Principal Baru-{runId}-057`, tekan Enter
12. Catat waktu sesudah `[Submit]` untuk perbandingan tanggal Last Modified
13. Verifikasi baris list `Paket Principal Baru-{runId}-057` | `FAMS` | `Paid` | `v1` | `0`
14. Verifikasi tanggal Last Modified pada baris sama dengan waktu aksi (toleransi satu menit)

### Nilai Template yang diubah (TC-AC-PF-149)

15. Klik `✕` pada Search lalu klik `+ Custom Plan` pada toolbar
16. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Override-{runId}-057`
17. Ubah Group count `3` → `25`, Open API ON → OFF, Borrowing `Basic` → `Full`
18. Klik `[Submit]`
19. Buka Tab Overview
20. Verifikasi Tab Overview: Group count `25`, Open API `No`, API call quota `—`, Borrowing `Full`
21. Verifikasi nilai lain pada Tab Overview sama dengan Template `Growth` v5: Asset Name cap `50`, Group hierarchy depth `2`, Category count `20`, Category hierarchy depth `2`, Scheduled reports `1`, Asset ID Configuration, License allocation per group, SAMP & Document Center, Custom Report Builder, Approval Workflow, Assignment, Transfer, Disposal, dan Accounting & Depreciation sesuai nilai Template
22. Buka tab `Default`, sub-tab `Active`
23. Buka Plan Detail `Growth` pada Tab Overview
24. Verifikasi Template `Growth` tidak berubah: Group count `3`

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 11, 12, 15, 22.
- Langkah penghubung: Search untuk menemukan baris target (R-16); `✕` pada Search dan klik `+ Custom Plan` untuk membuka form kedua; tab `Default` sub-tab `Active` untuk mengamati Template.
- TC-AC-PF-152 ada di spec 065 karena TC itu mengubah default plan `Growth` yang menjadi Template dua TC lain di spec ini.
- Temuan untuk QA: (1) Post Condition TC-AC-PF-146 (a: plan aktif milik entitas Principal tanpa approval; b: tidak ada relasi tersimpan ke plan Template; c: tidak terlihat oleh entitas lain) tidak punya langkah observasi di TC dan tidak diasersi. (2) Langkah 7 TC-AC-PF-146 berbunyi "Klik breadcrumb sub-tab `Active` lalu cari" tanpa menyebut kata kunci pencarian; spec memakai nama plan. (3) Expected d TC-AC-PF-146 menyebut "tanggal Last Modified saat ini" tanpa menyebut format; spec memakai format General Settings (`dd MMM yy`). (4) Expected "nilai lain sama dengan Template" TC-AC-PF-149 tidak menyebut format tampilan binary dan Feature Suites pada Tab Overview; spec menuliskannya sesuai nilai Template.
