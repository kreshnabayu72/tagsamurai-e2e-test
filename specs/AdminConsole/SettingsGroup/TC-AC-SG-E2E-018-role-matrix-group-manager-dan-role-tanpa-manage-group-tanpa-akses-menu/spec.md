---
id: TC-AC-SG-E2E-018-role-matrix-group-manager-dan-role-tanpa-manage-group-tanpa-akses-menu
title: "Role Matrix: Group Manager dan Role Lain tanpa Manage group Tidak Punya Akses Menu Settings > Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-63
  - TC-AC-SG-64
coverage:
  web: automated
---

# Role Matrix: Group Manager dan Role Lain tanpa Manage group Tidak Punya Akses Menu Settings > Group

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (akun aktor pertama). Hook `beforeEach` suite tidak dapat membuka Settings > Group lewat sidebar untuk kedua akun ini karena menu `Group` tidak tampil; langkah spec dimulai dari halaman awal portal setelah login. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password |
|---|---|---|---|
| TC-AC-SG-63 | Group Manager (`Maya Kusuma`, node `Warehouse Jakarta`) | #11 `groupManagerGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_GM_PASSWORD` |
| TC-AC-SG-64 | Global Role Manage language saja | #12 `manageLanguageGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_ML_PASSWORD` |

- Kemampuan teknis: membuka URL halaman Settings > Group langsung di address bar dan membaca status respons request data Group yang dipicu halaman disediakan tim FE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok akun Group Manager: TC-AC-SG-63

1. Verifikasi sedikitnya satu item menu lain pada sidebar navigasi Admin Console tampil
2. Verifikasi menu `Group` tidak tampil
3. Buka URL langsung `Settings > Group`
4. Verifikasi elemen lain pada halaman tampil (sidebar navigasi Admin Console)
5. Verifikasi akses langsung ditolak tanpa data Group
6. Verifikasi request data Group dijawab 403 Forbidden `{ "message": "Forbidden" }`

### Blok akun Manage language: TC-AC-SG-64

7. Ganti akun: logout, lalu login sebagai Role Manage language saja (`manageLanguageGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_ML_PASSWORD`)
8. Verifikasi sedikitnya satu item menu lain pada sidebar navigasi Admin Console tampil
9. Verifikasi menu `Group` tidak tampil
10. Buka URL langsung `Settings > Group`
11. Verifikasi elemen lain pada halaman tampil (sidebar navigasi Admin Console)
12. Verifikasi akses langsung ditolak tanpa data Group
13. Verifikasi request data Group dijawab 403 Forbidden `{ "message": "Forbidden" }`

## Notes

- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka Settings > Group lewat sidebar sehingga tidak berlaku bagi akun tanpa menu `Group` (spec ini dan blok Client di spec 016); perlu pengecualian di hook suite.
  - TC-AC-SG-63 dan TC-AC-SG-64 menyebut "request data Group dijawab 403" tanpa endpoint; spec mengasersi status respons request yang dipicu halaman tanpa menyebut endpoint (S-13).
