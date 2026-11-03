---
id: TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan
title: "Keunikan Plan Name Create Custom Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-117
  - TC-AC-PF-118
  - TC-AC-PF-119
  - TC-AC-PF-120
coverage:
  web: automated
---

# Keunikan Plan Name Create Custom Plan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A (custom plan Principal `Growth Tier` aktif; custom plan archived `Enterprise Reseller`; default plan FAMS `Growth` aktif) dan Dataset Plan X (Distributor memiliki custom plan `Plan Distributor Satu`). Dataset disediakan fixture backend dan dipulihkan.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth Tier`, `Enterprise Reseller`, `Plan Distributor Satu`, `Growth`) dipakai apa adanya, sebagai nama yang dicek keunikannya; dua custom plan Principal literal `Plan Distributor Satu` dan `Growth` dibuat TC-AC-PF-120 sehingga seeding idempoten dan cleanup menghapus keduanya; pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada nama bersuffix; dua plan yang dibuat TC-AC-PF-120 bernama literal sesuai TC karena asersi bergantung pada nama yang sama dengan custom plan entitas lain dan default plan.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `before` dan `after` menghapus custom plan Principal `Plan Distributor Satu` dan `Growth` yang dibuat spec ini lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Cek keunikan saat mengetik (TC-AC-PF-117)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Ketik `Growth Tier` pada field Plan Name lalu berhenti mengetik tanpa pindah fokus dan tunggu 1 detik
5. Verifikasi pesan inline `Plan name already exists` muncul tanpa perlu blur
6. Klik `[Submit]`
7. Verifikasi Submit ditolak dan form tetap terbuka tanpa berpindah ke Plan Detail (tidak ada plan baru)

### Tidak peka huruf besar-kecil (TC-AC-PF-118)

8. Klik `[Clear Field]` agar pesan `Plan name already exists` hilang
9. Pilih Product `FAMS` dan Template `Growth`
10. Ketik `  growth tier  ` pada field Plan Name dan tunggu 1 detik
11. Verifikasi pesan inline `Plan name already exists` muncul

### Plan archived (TC-AC-PF-119)

12. Klik `[Clear Field]` agar pesan `Plan name already exists` hilang
13. Pilih Product `FAMS` dan Template `Growth`
14. Ketik `Enterprise Reseller` pada field Plan Name dan tunggu 1 detik
15. Verifikasi pesan inline `Plan name already exists` muncul walau plan itu berstatus archived

### Scope entitas (TC-AC-PF-120)

16. Klik `[Clear Field]` agar pesan `Plan name already exists` hilang
17. Pilih Product `FAMS` dan Template `Growth`
18. Isi Plan Name `Plan Distributor Satu` dan klik `[Submit]`
19. Verifikasi toast sukses: "Success, custom plan has been created."
20. Verifikasi tidak ada pesan `Plan name already exists` pada pembuatan pertama
21. Klik breadcrumb sub-tab `Active`
22. Klik `+ Custom Plan` pada toolbar
23. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Growth`, lalu klik `[Submit]`
24. Verifikasi toast sukses: "Success, custom plan has been created." pada pembuatan kedua
25. Verifikasi tidak ada pesan `Plan name already exists` pada pembuatan kedua
26. Verifikasi keunikan hanya dalam scope custom plan entitas Principal: kedua pembuatan berhasil walau nama sama dengan custom plan Distributor dan default plan

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 8, 12, 16, 21.
- Langkah `[Clear Field]` di antara TC mengosongkan pesan inline identik (R-12) dan mengembalikan form ke kondisi awal; TC berikutnya tidak bergantung pada pesan TC sebelumnya.
- "Tidak ada plan baru" diamati lewat form yang tetap terbuka tanpa berpindah ke Plan Detail, karena TC tidak memberi langkah observasi daftar.
- Temuan untuk QA: (1) Expected b TC-AC-PF-120 ("Keunikan hanya dalam scope custom plan entitas Principal") adalah kesimpulan dari kedua pembuatan berhasil; spec menulisnya sebagai satu `Verifikasi` (S-03). (2) Post Condition TC-AC-PF-120 (kedua plan tersimpan milik Principal) tidak punya langkah observasi di TC; tidak diasersi terpisah.
