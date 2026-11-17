---
id: TC-FA-FAAC-E2E-031-role-matrix-positif-manage-create-use-recommended
title: "Role Matrix Positif: Manage Accounting (Read, Create) Menjalankan Use Recommended Classes"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-77
sourceRules: ["D-21", "T-10"]
smoke: []
dependsOn: []
trace:
  "D-21": 2
  "T-10": 5
coverage:
  web: automated
---

# Role Matrix Positif: Manage Accounting (Read, Create) Menjalankan Use Recommended Classes

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Create)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-77 |

- Env var: `FA_AC_MA_RC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: client tanpa Asset Class (EmptyState tampil) dan Tax Depreciation Class Bangunan permanen berstatus Active. Client tanpa Asset Class disediakan tim FE/BE (client terpisah atau fixture BE yang mengosongkan Asset Class client uji); email akun mengikuti pola tabel dengan `{namaCompany}` client itu.
- Data yang diubah spec: Asset Class BLDG dibuat lewat dialog Recommended Classes. Fixture BE (disediakan tim FE/BE) menyiapkan kondisi tanpa Asset Class di hook `before` dan memulihkannya (menghapus BLDG dan mengembalikan data client) di hook `after`, termasuk bila spec gagal di tengah.
- State global: Master Data Count Limit tidak diubah; kondisi tanpa Asset Class dipulihkan di hook `after` (suite serial).
- Data Dinamis: tidak ada data bersuffix `{runId}`; target aksi tulis adalah baris seed literal di atas (pengecualian beralasan, lihat butir sebelumnya).
- Kemampuan teknis: dialog Recommended Classes dengan checkbox baris, fixture BE untuk client tanpa Asset Class.

## Test Steps

### TC-FA-FAAC-77

1. Klik link "Use recommended classes" pada EmptyState
2. Verifikasi dialog Recommended Classes terbuka sebelum baris dicentang
3. Centang baris BLDG – Buildings
4. Klik [Create]
5. Verifikasi toast "Success, asset class has been created." tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a): Use Recommended Classes berhasil bagi role dengan huruf Create; satu role, tanpa ganti akun.
- Post Condition TC-FA-FAAC-77 (Asset Class BLDG berstatus Active tersimpan) tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-FAAC-77 mensyaratkan client tanpa Asset Class, tetapi Pre-setup TC memuat sembilan Asset Class contoh pada client yang sama dengan spec lain; spec memakai client atau kondisi kosong yang disediakan tim FE/BE.
  - TC-FA-FAAC-77 tidak menyebut cara memastikan EmptyState tampil sebelum langkah 1; spec mengikuti precondition tanpa asersi tambahan.
