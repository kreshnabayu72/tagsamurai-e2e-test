---
id: TC-AC-SG-E2E-016-role-matrix-entity-gate-distributor-partner-dan-client
title: "Role Matrix: Entity Gate Distributor, Partner, dan Client pada Settings > Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-57
  - TC-AC-SG-58
  - TC-AC-SG-59
coverage:
  web: automated
---

# Role Matrix: Entity Gate Distributor, Partner, dan Client pada Settings > Group

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control entitas Distributor Jaringan (akun aktor pertama); halaman Settings > Group dibuka hook `beforeEach` suite untuk akun yang memiliki menu `Group`. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | Hasil |
|---|---|---|---|---|
| TC-AC-SG-57 | Total Control entitas Distributor `Distributor Jaringan` | #13 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_DIST_PASSWORD` | menu `Group` tampil; tree hanya milik entitas sendiri |
| TC-AC-SG-58 | Total Control entitas Partner `Partner Jaringan` | #14 `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_PARTNER_PASSWORD` | menu `Group` tampil; tree hanya milik entitas sendiri |
| TC-AC-SG-59 | Total Control entitas Client `Client Jaringan` | #15 `totalControlClient_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_CLIENT_PASSWORD` | menu `Group` tidak tampil; akses langsung ditolak (403) |

- Entitas Principal uji dengan `Pohon Uji Utama` (Pre-setup #16) tersedia sebagai pembanding isolasi tree (TC-AC-SG-57 dan TC-AC-SG-58); isi tree `Distributor Jaringan` dan `Partner Jaringan` tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Kemampuan teknis: membuka URL halaman Settings > Group langsung di address bar dan membaca status respons request data Group yang dipicu halaman (TC-AC-SG-59) disediakan tim FE.
- Hook `beforeEach` suite tidak dapat membuka Settings > Group lewat sidebar untuk akun Client karena menu `Group` tidak tampil; untuk blok TC-AC-SG-59 langkah dimulai dari halaman awal portal setelah login.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok akun Distributor Jaringan: TC-AC-SG-57

1. Verifikasi menu `Group` tampil di bawah menu `Settings` pada sidebar navigasi Admin Console
2. Klik menu `Group`
3. Verifikasi halaman Settings > Group terbuka
4. Verifikasi Sidebar Group Tree dan tabel hanya memuat group milik entitas Distributor Jaringan, dengan root `All Groups` miliknya sendiri
5. Verifikasi tidak ada group `Pohon Uji Utama` Principal (`Warehouse Jakarta`, `Room 301`, `Finance Dept`) pada tree dan tabel

### Blok akun Partner Jaringan: TC-AC-SG-58

6. Ganti akun: logout, lalu login sebagai Total Control entitas Partner Jaringan (`totalControlPartner_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_PARTNER_PASSWORD`)
7. Buka menu `Settings` pada sidebar navigasi Admin Console
8. Verifikasi menu `Group` tampil di bawah menu `Settings`
9. Klik menu `Group`
10. Verifikasi halaman Settings > Group terbuka
11. Verifikasi Sidebar Group Tree dan tabel hanya memuat group milik entitas Partner Jaringan, dengan root `All Groups` miliknya sendiri
12. Verifikasi tidak ada group `Pohon Uji Utama` Principal (`Warehouse Jakarta`, `Room 301`, `Finance Dept`) pada tree dan tabel

### Blok akun Client Jaringan: TC-AC-SG-59

13. Ganti akun: logout, lalu login sebagai Total Control entitas Client Jaringan (`totalControlClient_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_CLIENT_PASSWORD`)
14. Verifikasi sedikitnya satu item menu lain pada sidebar navigasi Admin Console tampil
15. Verifikasi menu `Group` tidak tampil untuk Client
16. Buka URL langsung halaman `Settings > Group`
17. Verifikasi elemen lain pada halaman tampil (sidebar navigasi Admin Console)
18. Verifikasi halaman tidak menampilkan data Group
19. Verifikasi request data Group dijawab 403 Forbidden `{ "message": "Forbidden" }`

## Notes

- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); langkah tiap role tidak identik (TC-AC-SG-59 memverifikasi absence dan 403, bukan akses).
- Langkah penghubung: langkah 7 (membuka menu `Settings` sesudah ganti akun) adalah langkah TC; pada blok TC-AC-SG-57 langkah buka halaman sudah dilakukan hook `beforeEach` sehingga langkah dimulai dari verifikasi menu dan klik `Group`.
- Temuan untuk QA:
  - Isi tree entitas `Distributor Jaringan` dan `Partner Jaringan` tidak tertulis di Pre-setup TC (hanya `All Groups` miliknya); asersi absence group Principal memakai nama group yang khas pada `Pohon Uji Utama` (`Warehouse Jakarta`, `Room 301`, `Finance Dept`) dan perlu dipastikan namanya tidak dipakai di tree kedua entitas itu.
  - TC-AC-SG-59 menyebut "request data Group dijawab 403" tanpa menyebut endpoint; spec mengasersi status respons request yang dipicu halaman tanpa menyebut endpoint (S-13).
  - Hook `beforeEach` suite membuka Settings > Group lewat sidebar sehingga tidak berlaku bagi akun tanpa menu `Group` (Client, TC-AC-SG-59; juga spec 018); pengecualiannya tercatat di `suite.md`.
