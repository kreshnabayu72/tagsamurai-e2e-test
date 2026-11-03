---
id: TC-AC-DN-E2E-103-filter-screening-dan-opsi
title: "Filter Panel List: Screening, Tooltip Ikon, dan Opsi Dropdown dari Data Tabel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-288
  - TC-AC-DN-289
  - TC-AC-DN-290
  - TC-AC-DN-291
  - TC-AC-DN-292
  - TC-AC-DN-602
coverage:
  web: automated
---

# Filter Panel List: Screening, Tooltip Ikon, dan Opsi Dropdown dari Data Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #15 Brand `Brand A`, `Brand B`, `Brand C`, `Brand D`, `International Scanner Solutions`; #16 Device Name inti beserta SKU-nya (Model `Model G1`, `Model G2`, `Model L1`, `Model N1`, `Model R1`, `Model R2`, `Model R3`, `Industrial Barcode Station Series Alpha`); #17 seed 120 baris; #24 Measurement master `Liter` (ada di master, belum dipakai Device Name mana pun). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Filter Panel ditutup di akhir spec tanpa Apply. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-288: Screening Filter Panel

1. Klik ikon Filter di toolbar
2. Verifikasi ikon Filter berubah gelap karena panel terbuka
3. Verifikasi empat field berurutan: `Brand`, `Model/Type`, `Measurement`, `Last Modified`
4. Verifikasi placeholder field `Brand` "All brands", `Model/Type` "All models/types", `Measurement` "All measurements", `Last Modified` "Select date"
5. Verifikasi tipe kontrol: `Brand`, `Model/Type`, dan `Measurement` dropdown multi-select searchable; `Last Modified` date range picker
6. Verifikasi tidak ada field `Category` dan tidak ada field `Device Name` di panel
7. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan pada footer

### TC-AC-DN-289: Ikon Filter, tooltip dan status gelap

8. Klik ikon Filter (menutup panel)
9. Arahkan kursor ke ikon Filter
10. Verifikasi tooltip `Filter` tampil
11. Klik ikon Filter
12. Verifikasi ikon Filter berwarna gelap saat panel terbuka
13. Klik ikon Filter lagi
14. Verifikasi ikon Filter kembali ke warna normal setelah panel ditutup

### TC-AC-DN-290: Opsi dropdown Brand berasal dari data tabel

15. Klik ikon Filter
16. Klik field `Brand`
17. Verifikasi daftar opsi memuat `Brand A`, `Brand B`, `Brand C`, `Brand D`, dan `International Scanner Solutions`
18. Verifikasi tiap opsi tampil dengan checkbox
19. Verifikasi daftar tidak memuat nilai di luar lima Brand yang dipakai SKU Device Name di tabel
20. Tutup dropdown `Brand`

### TC-AC-DN-291: Opsi dropdown Model/Type berasal dari data tabel

21. Klik field `Model/Type`
22. Verifikasi daftar opsi memuat `Model G1`, `Model G2`, `Model L1`, `Model N1`, `Model R1`, `Model R2`, `Model R3`, dan `Industrial Barcode Station Series Alpha`
23. Tutup dropdown `Model/Type`

### TC-AC-DN-292: Opsi dropdown Measurement berasal dari data tabel

24. Klik field `Measurement`
25. Verifikasi daftar opsi memuat tepat tiga opsi: `Box`, `Meter`, dan `Unit`
26. Tutup dropdown `Measurement`

### TC-AC-DN-602: Opsi filter Measurement hanya memuat nilai yang dipakai Device Name

27. Klik ikon Filter (menutup panel)
28. Klik ikon Filter (membuka panel)
29. Klik field Measurement
30. Verifikasi daftar opsi memuat `Box`, `Meter`, dan `Unit`
31. Verifikasi daftar opsi tidak memuat `Liter`
32. Tutup dropdown `Measurement`
33. Klik ikon Filter (menutup panel tanpa Apply)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 8, 20, 23, 26, 27, 32, dan 33 menutup dropdown dan panel supaya tiap blok TC mulai dari state yang sama; langkah 28 dan 29 membuka ulang panel dan dropdown yang dibutuhkan TC-AC-DN-602.
- Urutan: mengikuti sourceTc; screening di awal, lalu opsi per field, dan TC-AC-DN-602 (pasangan kontras opsi dengan master `Liter`) di akhir.
- Temuan untuk QA:
  - TC-AC-DN-290 Expected b ("daftar tidak memuat nilai di luar Brand yang dipakai SKU") tidak menyebut nilai pembanding; spec mengasersi bahwa daftar hanya memuat lima Brand yang disebut, dengan daftar opsi yang tampil (langkah 17) sebagai anchor.
  - TC-AC-DN-602 dan TC-AC-DN-292 mengasersi daftar opsi Measurement yang sama dari state awal yang sama; keduanya tetap satu blok sendiri karena tiap TC satu spec.
