---
id: TC-FA-TDC-E2E-043-create-stay-on-form-checkbox-default-dan-dipertahankan
title: "Create dengan Checkbox Stay on This Form - Form Kosong dan Status Checkbox"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-111
  - TC-FA-TDC-112
sourceRules: ["T-01", "FI-10", "ST-02", "F-FATDC-01.k13", "§9.5#r5", "§9.5#r7", "§12#r11", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "T-01": 5
  "FI-10": [6, 8, 15]
  "ST-02": 7
  "F-FATDC-01.k13": [8, 16, 26]
  "§9.5#r5": [9, 10, 11, 12, 13, 14]
  "§9.5#r7": [16, 19, 22, 26, 31]
  "§12#r11": 28
  "§4.2c#b1": 29
coverage:
  web: automated
---

# Create dengan Checkbox Stay on This Form - Form Kosong dan Status Checkbox

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; setelah dua Create tabel berisi 9 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-05` dan `KHS-06` belum ada. Form valid: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok khusus uji 5` dan `Kelompok khusus uji 6`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line` dan `Declining Balance`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Pemulihan: hook `after` menghapus `KHS-05` dan `KHS-06` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-111: Create berhasil dengan checkbox Stay dicentang, Drawer tetap mode Create dengan form kosong

1. Klik `+ Class` di toolbar
2. Centang checkbox "Stay on this form after submitting"
3. Isi form valid dengan Class Code `KHS-05` (Non-building, Useful Life `8`, Straight Line dan Declining Balance)
4. Klik `[Submit]`
5. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
6. Verifikasi tabel di belakang Drawer diperbarui: baris `KHS-05` tampil
7. Verifikasi baris `KHS-05` di-highlight sesaat
8. Verifikasi Drawer tetap terbuka dalam mode Create (judul "Add Tax Depreciation Class")
9. Verifikasi field Regulation Reference kosong pada nilai awal
10. Verifikasi field Class Code kosong pada nilai awal
11. Verifikasi field Class Name kosong pada nilai awal
12. Verifikasi Asset Type belum terpilih
13. Verifikasi field Useful Life kosong pada nilai awal
14. Verifikasi Allowed Methods kosong pada nilai awal
15. Verifikasi fokus kursor berada di field Regulation Reference
16. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
17. Tutup Drawer dengan klik ikon ✕

### TC-FA-TDC-112: Checkbox Stay default tidak dicentang pada tiap pembukaan Drawer Create dan dipertahankan selama Drawer yang sama terbuka

18. Klik `+ Class` di toolbar
19. Verifikasi checkbox "Stay on this form after submitting" tidak dicentang
20. Centang checkbox "Stay on this form after submitting"
21. Klik `[Clear Field]`
22. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang setelah Clear Field
23. Isi form valid dengan Class Code `KHS-06` (Non-building, Useful Life `8`, Straight Line dan Declining Balance)
24. Klik `[Submit]`
25. Tunggu aksi selesai (semua field kembali kosong)
26. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang setelah Submit berhasil
27. Klik ikon ✕ pada Drawer
28. Verifikasi Drawer tertutup
29. Verifikasi dialog Unsaved Changes tidak muncul (form kosong)
30. Klik `+ Class` lagi
31. Verifikasi checkbox "Stay on this form after submitting" tidak dicentang
32. Tutup Drawer dengan klik ikon ✕

## Notes

- Langkah penghubung (S-03): langkah 17 dan 32 (menutup Drawer Create yang bersih; langkah 17 juga membuat langkah 18 membuka Drawer baru), langkah 25 (tunggu aksi selesai, 8b.8).
- Urutan Expected TC-FA-TDC-111 diasersi mengikuti urutan state (8b.5): baris `KHS-05` dan highlight sesaat (langkah 6 dan 7) lebih dulu, sebelum keadaan form (langkah 8 sampai 16).
- Field yang kosong sesudah Submit dengan Stay dicentang diasersi satu per satu karena kosong akibat aksi (S-01); Asset Type "belum terpilih" ditulis terpisah.
- Pembagian TC lintas spec: TC-FA-TDC-113 (Clear Field mengosongkan semua field) ada di spec `TC-FA-TDC-E2E-234-create-tombol-clear-field-mengosongkan-semua-field-tanpa-menutup-drawer`.
- Temuan untuk QA:
  - Langkah 3 dan 23 mengikuti TC ("Isi form valid"); nilai Regulation Reference dan Class Name tidak ditulis TC, spec memakai nilai dasar TC-FA-TDC-105.
  - Post Condition TC-FA-TDC-111 ("Class `KHS-05` tersimpan Active") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01).
  - TC-FA-TDC-112 Expected d ("Drawer tertutup tanpa dialog (form kosong)") bergantung pada form kosong sesudah Submit dengan Stay; spec menunggu aksi selesai (langkah 25) sebelum menutup Drawer.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
