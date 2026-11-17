---
id: TC-FA-FAAC-E2E-080-duplicate-asset-class
title: "Duplicate Asset Class: Pre-fill Mode Create dan Submit dengan Class Code Baru"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-263
  - TC-FA-FAAC-264
sourceRules: ["§4.2b#p1", "§3.8#p1", "R-07", "§[F-FAAC-06] Duplicate Asset Class#b3", "§[F-FAAC-06] Duplicate Asset Class#b2", "§[F-FAAC-06] Duplicate Asset Class#p2", "T-01", "§[F-FAAC-01] Create Asset Class#b3", "L-01", "§[F-FAAC-01] Create Asset Class#b4"]
smoke: []
dependsOn: []
trace:
  "§4.2b#p1": 3
  "§3.8#p1": 3
  "R-07": 4
  "§[F-FAAC-06] Duplicate Asset Class#b3": 4
  "§[F-FAAC-06] Duplicate Asset Class#b2": [5, 6, 10, 12, 20]
  "§[F-FAAC-06] Duplicate Asset Class#p2": [8, 20]
  "T-01": 16
  "§[F-FAAC-01] Create Asset Class#b3": [18, 19]
  "L-01": 22
  "§[F-FAAC-01] Create Asset Class#b4": 22
coverage:
  web: automated
---

# Duplicate Asset Class: Pre-fill Mode Create dan Submit dengan Class Code Baru

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class `B-ANCHOR` (Active; Class Name "Anchor Heavy Equipment"; Description "Asset class fixture group B"; tab Depreciation dan Accounts terisi sesuai seed; tanpa Asset Name). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Data Dinamis: Class Code hasil Duplicate `B-DUP-080` (literal, maks 15 karakter); Class Name `Duplicate Class {runId}-080`; dihapus di hook `before` bila sisa run sebelumnya dan di hook `after` lewat API.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk jumlah Asset Class, nilai Depreciation dan Accounts Asset Class, dan jumlah entri Changelog (audit trail permanen, S-12).
- State global: tidak ada yang diubah selain Asset Class `B-DUP-080` yang dibuat spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-263: Duplicate membuka Detail mode Create terisi dari sumber

1. Baca jumlah Asset Class sebagai baseline
2. Klik ikon "⋯" pada baris B-ANCHOR lalu pilih "Duplicate"
3. Verifikasi halaman Detail mode Create terbuka dengan judul "Add Asset Class"
4. Verifikasi jumlah Asset Class sama dengan baseline langkah 1 (tanpa mutasi data)
5. Verifikasi tab General: Class Code kosong
6. Verifikasi tab General: Class Name "Anchor Heavy Equipment" dan Description "Asset class fixture group B" disalin
7. Klik tab "Depreciation"
8. Verifikasi tab Depreciation terisi sama dengan B-ANCHOR
9. Klik tab "Accounts"
10. Verifikasi tab Accounts terisi sama dengan B-ANCHOR
11. Klik tab "Asset Names"
12. Verifikasi tab Asset Names tidak menyalin Asset Name (daftar draft kosong)

### TC-FA-FAAC-264: Submit hasil Duplicate dengan Class Code baru

13. Klik tab "General", isi Class Code `B-DUP-080` dan Class Name `Duplicate Class {runId}-080`
14. Baca jumlah entri Changelog sebagai baseline
15. Klik "Submit"
16. Verifikasi muncul toast sukses: "Success, asset class has been created."
17. Klik breadcrumb "Asset Class" (kembali ke tabel Asset Class)
18. Verifikasi Asset Class `B-DUP-080` dibuat Active di tabel
19. Verifikasi Asset Names `B-DUP-080` bernilai 0
20. Verifikasi nilai Depreciation dan Accounts `B-DUP-080` sama dengan B-ANCHOR
21. Klik ikon Changelog
22. Verifikasi selisih jumlah entri Changelog terhadap baseline langkah 14 adalah 1, yaitu satu baris Action "Create" Field "Class Code" Old Value "—" New Value `B-DUP-080`

## Notes

- Class Code `B-DUP-080` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98) sehingga suffix itu tidak muat; `{runId}-080` dipindah ke Class Name agar unik per run (S-12; pola spec 066 sampai 069 dan 047/048); cleanup di hook `before` dan `after`.
- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 263 lalu 264; TC-264 melanjutkan form Duplicate hasil TC-263 (langkah Duplicate TC-264 sama dengan langkah 2 dan tidak diulang).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-ANCHOR` adalah seed bertanda `B-*` per TC, dipakai apa adanya sebagai sumber salinan (tidak diubah). Class Code hasil Duplicate memakai literal `B-DUP-080`; `{runId}-080` dipindah ke Class Name (lihat butir Class Code 15 karakter).
- Langkah penghubung (S-03): langkah 1 dan 14 (baseline), 7, 9, 11, dan 13 (berpindah tab), 17 (halaman Create tetap di mode Edit setelah Submit, lihat Expected TC-259 butir b, sehingga tabel dibuka lewat breadcrumb).
- Langkah 8 dan 10 membandingkan dengan nilai B-ANCHOR dari fixture; spesifikasi nilai tidak tertulis di TC (Temuan untuk QA).
- Temuan untuk QA: TC-263 butir "tanpa mutasi data" tidak punya cara observasi di UI; spec memakai jumlah Asset Class dari kemampuan baca BE. TC-264 memakai Class Code literal "B-DUP"; spec memakai `B-DUP-080` dan Class Name ber-{runId}.
