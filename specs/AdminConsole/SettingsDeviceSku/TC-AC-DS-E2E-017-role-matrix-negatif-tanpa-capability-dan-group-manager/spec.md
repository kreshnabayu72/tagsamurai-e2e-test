---
id: TC-AC-DS-E2E-017-role-matrix-negatif-tanpa-capability-dan-group-manager
title: "Role Matrix Negatif: Principal Tanpa Capability dan Group Manager Tidak Melihat Menu serta URL Langsung Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-56
  - TC-AC-DS-57
  - TC-AC-DS-58
coverage:
  web: automated
---

# Role Matrix Negatif: Principal Tanpa Capability dan Group Manager Tidak Melihat Menu serta URL Langsung Ditolak

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun pertama login di hook `before` spec ini; akun kedua diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-56, TC-AC-DS-57 | Principal PT Arunika Prima tanpa capability Manage device master data (Pre-setup #8) | `noCapabilitySku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_NOCAP_PASSWORD` |
| 2 | TC-AC-DS-58 | Group Manager Principal PT Arunika Prima (Pre-setup #9) | `groupManagerSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_GM_PASSWORD` |

- Halaman dibuka hook `beforeEach` suite; untuk akun tanpa capability halaman itu ditolak (lihat Temuan untuk QA), sehingga langkah spec tidak bergantung pada halaman yang terbuka.
- Data Pre-setup: tidak ada data SKU yang dibutuhkan; tidak ada seeding. URL halaman Device SKU dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_NOCAP_PASSWORD` dan `AC_DS_GM_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada state global yang diubah.

## Test Steps

### Blok 1: Principal tanpa capability (TC-AC-DS-56 dan TC-AC-DS-57)

1. Buka menu Settings pada sidebar
2. Verifikasi item Settings lain yang menjadi hak role tetap tampil
3. Verifikasi item Device dan sub-tab Device SKU tidak tampil pada sidebar
4. Ketik URL halaman `Settings > Device > Device SKU` pada address bar lalu tekan Enter
5. Verifikasi toast error: "You don't have permission to do this."
6. Verifikasi tidak ada redirect
7. Verifikasi tidak ada baris SKU yang tampil

### Blok 2: Group Manager (TC-AC-DS-58)

8. Ganti akun: Logout dari akun Principal tanpa capability
9. Login sebagai Group Manager Principal `groupManagerSku_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_GM_PASSWORD`
10. Buka menu Settings pada sidebar
11. Verifikasi sedikitnya satu item submenu Settings tampil
12. Verifikasi menu Device dan sub-tab Device SKU tidak tampil
13. Ketik URL halaman `Settings > Device > Device SKU` pada address bar lalu tekan Enter
14. Verifikasi toast error: "You don't have permission to do this."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-56, TC-57, TC-58.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 4, 10, 13 (membuka menu atau mengetik URL; hasilnya diasersi pada langkah berikutnya), 8 dan 9 (ganti akun).
- Asersi absence langkah 3 didahului langkah 2 (item Settings lain tampil); langkah 12 didahului langkah 11; langkah 7 didahului langkah 5 (toast penolakan sebagai anchor).
- TC-58 Expected a menyebut alasan "Peran Global tidak tersentuh scope Group Manager"; alasan ini bukan keadaan yang teramati sehingga tidak diasersi terpisah.
- Temuan untuk QA:
  - S-12: tidak ada nama literal data SKU yang diasersi; email akun mengikuti Pre-setup #8 dan #9.
  - Fixture rancangan: ketersediaan Pre-setup #8 dan #9 di environment belum diverifikasi.
  - Hook `beforeEach` suite membuka Settings > Device > Device SKU; untuk akun tanpa capability halaman itu ditolak 403. Perilaku hook untuk akun tanpa akses perlu ditetapkan tim FE.
  - TC-57 Expected b ("tidak ada redirect") tidak menyebut cara mengamati; spec mengasersi halaman tidak berpindah ke halaman unauthorized.
  - TC-58 tidak menyebut path URL; URL disediakan tim FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
