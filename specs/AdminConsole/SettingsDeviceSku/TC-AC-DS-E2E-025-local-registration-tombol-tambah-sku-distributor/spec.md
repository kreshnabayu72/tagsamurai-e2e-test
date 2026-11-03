---
id: TC-AC-DS-E2E-025-local-registration-tombol-tambah-sku-distributor
title: "Local Registration: Tombol [+ SKU] Distributor Tampil Saat Aktif dan Tersembunyi Saat Nonaktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-83
  - TC-AC-DS-84
coverage:
  web: automated
---

# Local Registration: Tombol [+ SKU] Distributor Tampil Saat Aktif dan Tersembunyi Saat Nonaktif

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-83 | Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Pre-setup #10) | `totalControlDist_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_PASSWORD` |
| 2 | TC-AC-DS-84 | Total Control Distributor PT Mandala Niaga, Local Registration nonaktif (Pre-setup #17) | `totalControlDistOff_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DISTOFF_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30, SKU Distributor #31 (`LOC-NOR-01` sampai `LOC-NOR-03`; `MAN-LOC-01`). Status Local Registration kedua Distributor adalah konfigurasi tetap entitas uji dan tidak diubah spec. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_DIST_PASSWORD` dan `AC_DS_DISTOFF_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### Blok 1: Distributor dengan Local Registration aktif (TC-AC-DS-83)

1. Verifikasi toolbar menampilkan `Search | Filter | Download | Changelog | [+ SKU]` dengan tombol `[+ SKU]` Show

### Blok 2: Distributor dengan Local Registration nonaktif (TC-AC-DS-84)

2. Ganti akun: Logout dari akun Total Control Distributor PT Cakra Distribusi
3. Login sebagai Total Control Distributor PT Mandala Niaga `totalControlDistOff_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DISTOFF_PASSWORD`
4. Buka halaman `Settings > Device > Device SKU`
5. Verifikasi toolbar menampilkan `Search | Filter | Download | Changelog` tanpa tombol `[+ SKU]` (Hidden)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-83, TC-84.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 2 sampai 4 (ganti akun dan membuka halaman).
- Asersi absence tombol `[+ SKU]` pada langkah 5 memakai ikon Search, Filter, Download, dan Changelog pada toolbar yang sama sebagai anchor (bagian 8b butir 2, Table Tools sebagai anchor permukaan).
- Temuan untuk QA:
  - S-12: tidak ada nama literal data SKU yang diasersi; email akun mengikuti Pre-setup #10 dan #17.
  - Fixture rancangan: ketersediaan Pre-setup #10 dan #17 di environment belum diverifikasi.
  - TC-83 dan TC-84 tidak menyebut cara memverifikasi status Local Registration entitas; status dianggap konfigurasi tetap entitas uji.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
