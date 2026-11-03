---
id: TC-FA-RP-E2E-019-role-matrix-negatif-peran-tanpa-akses-modul
title: "Role Matrix Negatif: peran tanpa akses modul"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-75
  - TC-FA-RP-76
coverage:
  web: automated
---

# Role Matrix Negatif: peran tanpa akses modul

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Tanpa Akses (Pre-setup #10). Akun ini tidak berhak atas halaman Role & Permission, sehingga layar awal yang dibuka hook `beforeEach` suite untuk spec ini adalah layar Fixed Asset > Settings tanpa menu Role & Permission (kemampuan itu disediakan tim FE; lihat Temuan untuk QA). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix negatif, satu role):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Tanpa Akses (Tono Wibowo; tanpa tingkat akses, tanpa Group Manager, tanpa Manage user & role) | #10 | `noAccess_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.noAccess.email`) | `Spectra.env.FA_NOACCESS_PASSWORD` |

- Data: URL halaman Settings > Role & Permission dari `Fixture.fixedAssetRolePermission.url.rolePermission` (fixture belum ada; URL tidak tertulis di TC dan ditambahkan tim FE).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan URL ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah data atau state global.

## Test Steps

### TC-FA-RP-75: Menu Role & Permission Hidden bagi peran tanpa akses modul

1. Verifikasi sedikitnya satu item menu lain pada sidebar Settings tampil
2. Verifikasi item `Role & Permission` tidak muncul di sidebar sama sekali (Hidden)

### TC-FA-RP-76: Akses langsung ke halaman modul oleh peran tanpa akses ditolak

3. Ketik URL halaman Settings > Role & Permission (`Fixture.fixedAssetRolePermission.url.rolePermission`) langsung di address bar
4. Verifikasi muncul toast error `You don't have permission to do this.`
5. Verifikasi konten modul tidak tampil
6. Verifikasi sedikitnya satu item menu lain pada sidebar Settings tampil
7. Muat ulang halaman (F5)
8. Amati halaman
9. Verifikasi elemen yang tak berhak tersembunyi: item `Role & Permission` tidak ada di sidebar setelah UI di-refresh
10. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-75, 76). Spec Role Matrix negatif per topik (bagian 3a): target yang tidak berhak atas modul; tabel "Role yang diuji" memuat satu role.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik URL langsung dan memuat ulang halaman (F5, langkah 7) lalu mengamati halaman (langkah 8) pada TC-FA-RP-76 adalah langkah TC.
- Anchor absence (8b butir 2): item menu lain pada sidebar Settings menjadi anchor positif untuk absence item `Role & Permission`.
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka halaman Role & Permission untuk akun aktor; akun Tanpa Akses tidak berhak atas halaman itu. Spec ini memakai layar awal yang tidak memuat halaman modul (disediakan tim FE).
  - TC-FA-RP-76 expected b menulis "elemen yang tak berhak tersembunyi setelah UI di-refresh" tanpa menyebut elemen mana; spec memakai item `Role & Permission` pada sidebar.
  - TC-FA-RP-76 tidak menyebut URL halaman; URL disediakan tim FE lewat fixture.
  - Post Condition TC-FA-RP-75 dan 76 tidak memberi langkah observasi tambahan; tidak diasersi.
