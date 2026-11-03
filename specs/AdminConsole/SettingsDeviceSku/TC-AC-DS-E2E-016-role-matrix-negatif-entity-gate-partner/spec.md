---
id: TC-AC-DS-E2E-016-role-matrix-negatif-entity-gate-partner
title: "Role Matrix Negatif: Partner Tidak Melihat Menu Device dan Akses URL Langsung Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-54
  - TC-AC-DS-55
coverage:
  web: automated
---

# Role Matrix Negatif: Partner Tidak Melihat Menu Device dan Akses URL Langsung Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Env var |
|---|---|---|
| Total Control Partner CV Karya Mandiri (Pre-setup #15; entitas Partner tidak punya akses menu Device) | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_PARTNER_PASSWORD` |

- Login akun Partner di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite. Hook `beforeEach` suite membuka Settings > Device > Device SKU; untuk akun tanpa akses halaman itu ditolak (lihat Temuan untuk QA), sehingga langkah spec tidak bergantung pada halaman yang terbuka.
- Data Pre-setup: tidak ada data SKU yang dibutuhkan; tidak ada seeding. URL halaman Device SKU dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_PARTNER_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-54: Partner tidak melihat menu Device

1. Buka menu Settings pada sidebar
2. Verifikasi sedikitnya satu item submenu Settings tampil
3. Verifikasi menu Device tidak tampil pada submenu Settings, tab Device SKU tidak ada
4. Verifikasi tidak ada jalur navigasi dari sidebar menuju halaman Device SKU

### TC-AC-DS-55: Partner membuka URL Device SKU langsung

5. Ketik URL halaman `Settings > Device > Device SKU` pada address bar lalu tekan Enter
6. Verifikasi toast error: "You don't have permission to do this."
7. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
8. Verifikasi UI di-refresh sehingga elemen yang tak berhak tersembunyi
9. Verifikasi tidak ada data SKU yang tampil

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-54, TC-55.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (membuka menu Settings) dan langkah 5 (mengetik URL; hasilnya diasersi pada langkah 6 sampai 9).
- Asersi absence langkah 3 dan 4 didahului langkah 2 (item submenu Settings lain tampil sebagai anchor pada sidebar yang sama); langkah 9 didahului langkah 6 (toast penolakan sebagai anchor).
- Temuan untuk QA:
  - S-12: tidak ada nama literal data SKU yang diasersi; email akun Partner mengikuti Pre-setup #15.
  - Fixture rancangan: ketersediaan Pre-setup #15 di environment belum diverifikasi.
  - Hook `beforeEach` suite membuka Settings > Device > Device SKU; untuk Partner halaman itu ditolak 403. Perilaku hook untuk akun tanpa akses perlu ditetapkan tim FE (mis. pengecualian pembukaan halaman pada spec role-negatif).
  - TC-54 tidak menyebut item submenu Settings yang dimiliki Partner; langkah 2 memakai pembanding generik "sedikitnya satu item".
  - TC-55 tidak menyebut path URL atau cara membaca bahwa UI di-refresh; URL disediakan tim FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
