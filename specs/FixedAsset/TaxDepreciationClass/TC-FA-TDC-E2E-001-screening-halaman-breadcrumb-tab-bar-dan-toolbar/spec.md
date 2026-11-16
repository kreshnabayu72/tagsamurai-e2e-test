---
id: TC-FA-TDC-E2E-001-screening-halaman-breadcrumb-tab-bar-dan-toolbar
title: "Screening Halaman Tax Depreciation Class: Breadcrumb, Tab Bar, dan Toolbar"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-1
  - TC-FA-TDC-2
  - TC-FA-TDC-3
  - TC-FA-TDC-4
sourceRules: ["§4.2a#p1", "§4.1#r1", "FATDC-LOGIC-02a", "§4.2a#p2", "§4.7#p1", "§4.1.1#p5", "§5#b1", "§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "§4.1.1#p4", "§4.4#r11", "§4.1.1#r11", "§4.1.1#r12", "§4.1.1#r13", "§9.5#r4", "§9.5#r1", "§4.1.1#b7", "§5#b5", "§9.5#r3"]
smoke: []
dependsOn: []
trace:
  "§4.2a#p1": [4, 5, 10, 18, 19, 23, 25]
  "§4.1#r1": [4, 24]
  "FATDC-LOGIC-02a": [6, 14]
  "§4.2a#p2": [8, 25]
  "§4.7#p1": 9
  "§4.1.1#p5": 11
  "§5#b1": 11
  "§4.1.1#r1": 12
  "§4.1.1#r2": 12
  "§4.1.1#r3": 12
  "§4.1.1#r4": 12
  "§4.1.1#r5": 12
  "§4.1.1#r6": 12
  "§4.1.1#r7": 12
  "§4.1.1#r8": 12
  "§4.1.1#r9": 12
  "§4.1.1#r10": 12
  "§4.1.1#p4": 12
  "§4.4#r11": 12
  "§4.1.1#r11": 13
  "§4.1.1#r12": 13
  "§4.1.1#r13": 13
  "§9.5#r4": 13
  "§9.5#r1": 14
  "§4.1.1#b7": 15
  "§5#b5": 16
  "§9.5#r3": 16
anchor: [21, 27, 29, 31]
coverage:
  web: automated
---

# Screening Halaman Tax Depreciation Class: Breadcrumb, Tab Bar, dan Toolbar

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset, plan Growth). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun dan email disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama usulan, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`; flag halaman ini disetel seen untuk akun aktor sehingga walkthrough tidak menutupi layar.
- Data Pre-setup (dibaca, tidak diubah; dirujuk lewat `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND dalam keadaan belum diubah; plan company Growth; tidak ada Search, Filter, atau sort manual aktif. Data Dinamis: tidak ada.
- Kemampuan teknis: seeding tujuh class seed dan plan company lewat API (disediakan tim FE/BE, `suite.md`). Spec membuka halaman utama aplikasi Fixed Asset sendiri untuk TC-FA-TDC-1 (pengecualian atas `beforeEach` suite).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-1: Buka tab Tax Depreciation Class dari sidebar Accounting

1. Buka halaman utama aplikasi Fixed Asset
2. Klik menu sidebar `Accounting`
3. Klik tab `Tax Depreciation Class`
4. Verifikasi halaman Accounting terbuka dengan tab `Tax Depreciation Class` aktif
5. Verifikasi Breadcrumb tampil `Settings > Accounting > Tax Depreciation Class`
6. Verifikasi tabel Tax Depreciation Class List tampil dengan 7 baris seed

### TC-FA-TDC-2: Screening halaman Settings > Accounting > Tax Depreciation Class

7. Klik tab `Tax Depreciation Class`
8. Verifikasi Breadcrumb `Settings > Accounting > Tax Depreciation Class` tampil tanpa Page Title terpisah di bawahnya
9. Verifikasi tombol replay Guided Tooltip `[?]` tampil tepat di sebelah kanan Breadcrumb
10. Verifikasi Tab tampil `Preferences | Chart of Accounts | Tax Depreciation Class (aktif) | Asset Class`
11. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | + Class`
12. Verifikasi kolom tabel `Checkbox seleksi baris | Active (sortable) | Class Code (sortable) | Class Name (sortable) | Asset Type (sortable) | Useful Life (years) (sortable) | Straight Line Rate (sortable) | Declining Balance Rate (sortable) | Allowed Methods (sortable) | Used By (sortable) | Effective From (sortable) | Column Visibility (⋯) (unsortable — header klik = buka Overlay Column Visibility, body per baris = row action menu)`
13. Verifikasi kolom Regulation Reference, Modified By, dan Last Updated tidak tampil (Hidden default)
14. Verifikasi 7 baris tampil berurutan Class Code A-Z: BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-3, NB-4
15. Verifikasi chip filter aktif dan `Clear all` tidak tampil karena tidak ada filter aktif
16. Verifikasi Footer menampilkan Pagination dengan page size default 10 per halaman

### TC-FA-TDC-4: Tab bar halaman Accounting: urutan tab dan tab Tax Depreciation Class aktif

17. Klik tab `Tax Depreciation Class`
18. Verifikasi tab bar menampilkan `Preferences | Chart of Accounts | Tax Depreciation Class | Asset Class`
19. Verifikasi tab ke-3 `Tax Depreciation Class` aktif
20. Amati tab bar, lalu klik tab `Asset Class`
21. Verifikasi tab aktif berpindah ke `Asset Class`
22. Klik kembali tab `Tax Depreciation Class`
23. Verifikasi tab ke-3 `Tax Depreciation Class` aktif lagi
24. Verifikasi tabel Tax Depreciation Class List tampil

### TC-FA-TDC-3: Breadcrumb halaman: teks path, segmen yang dapat diklik, dan segmen terakhir statis

25. Verifikasi teks Breadcrumb persis `Settings > Accounting > Tax Depreciation Class` tanpa Page Title terpisah di bawahnya
26. Klik segmen `Settings`
27. Verifikasi segmen `Settings` adalah label statis: klik tidak membuka halaman apa pun
28. Klik segmen `Tax Depreciation Class`
29. Verifikasi segmen terakhir `Tax Depreciation Class` adalah label statis: halaman tidak berpindah dan tab tetap `Tax Depreciation Class`
30. Klik segmen `Accounting`
31. Verifikasi halaman Accounting terbuka

## Notes

- Urutan TC dalam spec: TC-FA-TDC-1, 2, 4, 3 (bukan 1, 2, 3, 4). TC-FA-TDC-3 berakhir dengan membuka halaman Accounting lewat segmen Breadcrumb sehingga diletakkan terakhir; TC-FA-TDC-4 berakhir di tab `Tax Depreciation Class`. Screening (TC-FA-TDC-2) tetap di awal setelah navigasi TC-FA-TDC-1.
- Langkah penghubung (S-03): langkah 1 (membuka halaman utama aplikasi sebagai awal TC-FA-TDC-1), langkah 7 dan 17 (`Klik tab Tax Depreciation Class` untuk "Buka tab Tax Depreciation Class" pada TC; halaman sudah aktif dari langkah sebelumnya), dan langkah 20 (kalimat "Amati tab bar" TC-FA-TDC-4 digabung dengan aksi klik berikutnya). Tidak ada langkah penghubung lain.
- Langkah "Amati Breadcrumb" TC-FA-TDC-3 diwujudkan sebagai `Verifikasi` langkah 25 karena Expected a-nya adalah hasil pengamatan itu.
- Temuan untuk QA:
  - Email dan company akun Total Control tidak tertulis di TC (ACC hanya menyebut nama role); akun disediakan tim FE (S-11, S-13).
  - TC-FA-TDC-3 Expected b dan c tidak menyebut halaman apa yang tampil bila segmen statis diklik selain "tidak membuka halaman apa pun"; spec mengasersi hanya yang tertulis.
  - TC-FA-TDC-4 Expected a menggabungkan urutan tab dan status aktif; spec memecahnya menjadi dua `Verifikasi` (S-01).
