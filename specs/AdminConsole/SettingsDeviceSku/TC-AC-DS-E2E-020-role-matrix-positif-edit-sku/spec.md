---
id: TC-AC-DS-E2E-020-role-matrix-positif-edit-sku
title: "Role Matrix Positif: Update-Only Principal dan Distributor Menyelesaikan Edit SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-71
  - TC-AC-DS-75
coverage:
  web: automated
---

# Role Matrix Positif: Update-Only Principal dan Distributor Menyelesaikan Edit SKU

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-71 | Update-Only Principal PT Arunika Prima (Pre-setup #5) | `manageSkuU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_U_PASSWORD` |
| 2 | TC-AC-DS-75 | Update-Only Distributor PT Cakra Distribusi (Pre-setup #13) | `manageSkuDistU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_U_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30, SKU Distributor #31. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data milik spec (hook `before`, lewat sesi API aktor Principal dan Distributor serta fixture BE yang disediakan tim BE/FE; menggantikan `HHR-ARC-200` dan `LOC-NOR-02` agar data Pre-setup tidak berubah, S-06):
  - SKU Principal `UPD-{runId}-020` (Device Name `UHF Handheld Reader`, Category `UHF Handheld`, Brand `Arcturus`, Model/Type `UP1-{runId}`, Range Type `Short Range`, stok 0, 1 foto).
  - SKU Distributor PT Cakra Distribusi `DUPD-{runId}-020` (Device Name `BLE Gateway`, Category `BLE Gateway`, Brand `Nordik`, Model/Type `DUP1-{runId}`, stok 0, 1 foto).
  - Hook `after` menghapus kedua SKU lewat fixture BE.
- Env var `AC_DS_U_PASSWORD` dan `AC_DS_DIST_U_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada state global yang diubah.

## Test Steps

### Blok 1: Update-Only Principal (TC-AC-DS-71)

1. Ketik Search `UPD-{runId}-020`, tekan Enter
2. Klik ⋯ baris `UPD-{runId}-020` lalu pilih `Edit`
3. Ubah Model/Type dari `UP1-{runId}` menjadi `UP2-{runId}`
4. Klik `[Save]`
5. Verifikasi toast sukses: "Success, device SKU has been updated."
6. Verifikasi popup Edit SKU tertutup
7. Verifikasi baris `UPD-{runId}-020` menampilkan Model/Type `UP2-{runId}`
8. Klik `(←)` pada kotak Search

### Blok 2: Update-Only Distributor (TC-AC-DS-75)

9. Ganti akun: Logout dari akun Update-Only Principal
10. Login sebagai Update-Only Distributor `manageSkuDistU_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_U_PASSWORD`
11. Buka halaman `Settings > Device > Device SKU`
12. Ketik Search `DUPD-{runId}-020`, tekan Enter
13. Klik ⋯ baris `DUPD-{runId}-020` lalu pilih `Edit`
14. Ubah Model/Type dari `DUP1-{runId}` menjadi `DUP2-{runId}`
15. Klik `[Save]`
16. Verifikasi toast sukses: "Success, device SKU has been updated."
17. Verifikasi baris `DUPD-{runId}-020` menampilkan Model/Type `DUP2-{runId}`
18. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-71, TC-75.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 12 (Search untuk menemukan baris target, R-16), 2 sampai 4 dan 13 sampai 15 (membuka Edit, mengubah, dan menyimpan; hasilnya diasersi pada langkah berikutnya), 8 dan 18 (mengosongkan Search, S-09), 9 sampai 11 (ganti akun dan membuka halaman).
- Temuan untuk QA:
  - S-12/S-06: TC mengubah `HHR-ARC-200` (Model/Type `H200` menjadi `H201`) dan `LOC-NOR-02` (`GW-N2` menjadi `GW-N3`) pada data Pre-setup; spec memakai SKU milik spec bersuffix dengan atribut setara (stok 0) dan Model/Type bersuffix.
  - Fixture rancangan: ketersediaan Pre-setup #5 dan #13 di environment belum diverifikasi; seeding SKU Principal dan Distributor bergantung pada sesi API aktor yang disediakan tim BE/FE.
  - Post Condition TC-71 dan TC-75 (nilai tersimpan, entri Edit tercatat di tiga surface log) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
