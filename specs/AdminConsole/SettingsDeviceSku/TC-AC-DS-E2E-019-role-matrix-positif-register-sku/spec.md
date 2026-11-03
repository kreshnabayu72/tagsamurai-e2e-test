---
id: TC-AC-DS-E2E-019-role-matrix-positif-register-sku
title: "Role Matrix Positif: Create-Only Principal dan Distributor Menyelesaikan Register SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-70
  - TC-AC-DS-74
coverage:
  web: automated
---

# Role Matrix Positif: Create-Only Principal dan Distributor Menyelesaikan Register SKU

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-70 | Create-Only Principal PT Arunika Prima (Pre-setup #4) | `manageSkuC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_C_PASSWORD` |
| 2 | TC-AC-DS-74 | Create-Only Distributor PT Cakra Distribusi, Local Registration aktif (Pre-setup #12) | `manageSkuDistC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_C_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25 (`Asset TAG`), Device Name #26 (`Asset TAG`), Brand Principal #27 (`Arcturus`), Brand Distributor #28 (`Nordik`), file foto `foto-a.jpg` #37, SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data Dinamis (dibuat spec): SKU `CRE-ONLY-{runId}-019` (blok 1: Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-CRE`, foto `foto-a.jpg`) dan SKU `DIS-CRE-{runId}-019` (blok 2: Category `Asset TAG`, Device Name `Asset TAG`, Brand `Nordik`, Model/Type `T-DC1`, foto `foto-a.jpg`). Role Create-Only tidak dapat menghapus SKU, sehingga hook `after` menghapus kedua SKU lewat sesi API aktor Total Control dan fixture BE yang disediakan tim BE/FE.
- Env var `AC_DS_C_PASSWORD` dan `AC_DS_DIST_C_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada state global yang diubah.

## Test Steps

### Blok 1: Create-Only Principal (TC-AC-DS-70)

1. Klik `[+ SKU]`
2. Pilih Category `Asset TAG` lewat picker lalu klik `[Select]`
3. Pilih Device Name `Asset TAG`
4. Pilih Brand `Arcturus`
5. Ketik `T-CRE` pada Model/Type
6. Ketik `cre-only-{runId}-019` pada SKU
7. Unggah `foto-a.jpg`
8. Klik `[Submit]`
9. Verifikasi toast sukses: "Success, device SKU has been registered."
10. Verifikasi popup Register SKU tertutup
11. Ketik Search `CRE-ONLY-{runId}-019`, tekan Enter
12. Verifikasi baris `CRE-ONLY-{runId}-019` ada pada List
13. Verifikasi Current Stock baris `CRE-ONLY-{runId}-019` adalah `0`
14. Klik `(←)` pada kotak Search

### Blok 2: Create-Only Distributor (TC-AC-DS-74)

15. Ganti akun: Logout dari akun Create-Only Principal
16. Login sebagai Create-Only Distributor `manageSkuDistC_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_C_PASSWORD`
17. Buka halaman `Settings > Device > Device SKU`
18. Klik `[+ SKU]`
19. Pilih Category `Asset TAG` lewat picker lalu klik `[Select]`
20. Pilih Device Name `Asset TAG`
21. Pilih Brand `Nordik`
22. Ketik `T-DC1` pada Model/Type
23. Ketik `DIS-CRE-{runId}-019` pada SKU
24. Unggah `foto-a.jpg`
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, device SKU has been registered."
27. Ketik Search `DIS-CRE-{runId}-019`, tekan Enter
28. Verifikasi baris `DIS-CRE-{runId}-019` ada pada List Distributor
29. Klik ⋯ pada baris `DIS-CRE-{runId}-019`
30. Verifikasi menu ⋯ hanya memuat `Detail`; `Edit` dan `Delete` Hidden untuk tier Create
31. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-70, TC-74.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 sampai 8 dan 18 sampai 25 (mengisi form Register dan Submit; hasilnya diasersi pada langkah 9 dan 10, 26), 11 dan 27 (Search untuk menemukan baris target, R-16), 14 dan 31 (mengosongkan Search, S-09), 15 sampai 17 (ganti akun dan membuka halaman), 29.
- Langkah 6 dan 23 mengetik kode SKU; kolom SKU mengubah huruf kecil menjadi kapital sesuai TC-70 langkah 7, sehingga baris tampil sebagai `CRE-ONLY-{runId}-019`.
- Temuan untuk QA:
  - S-12: TC menamai SKU `CRE-ONLY-01` dan `DIS-CRE-01`; spec memakai nama bersuffix `CRE-ONLY-{runId}-019` dan `DIS-CRE-{runId}-019` (data Dinamis bersuffix per run).
  - Fixture rancangan: ketersediaan Pre-setup #4, #12, #25, #26, #28, dan #37 di environment belum diverifikasi.
  - Post Condition TC-70 dan TC-74 (SKU tersimpan, entri Create tercatat di tiga surface log, SKU tidak tampil pada List Principal) tidak punya langkah observasi di TC, sehingga tidak diasersi; pencatatan log dicakup spec lain.
  - Role Create-Only tidak dapat menghapus SKU; cleanup memakai sesi API aktor Total Control atau fixture BE yang disediakan tim BE/FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
