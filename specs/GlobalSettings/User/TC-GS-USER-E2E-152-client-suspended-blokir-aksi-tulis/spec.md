---
id: TC-GS-USER-E2E-152-client-suspended-blokir-aksi-tulis
title: Client suspended atau expired memblokir semua aksi tulis di modul User
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-611
coverage:
  web: automated
---

# Client suspended atau expired memblokir semua aksi tulis di modul User

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, dengan status client dipaksa suspended lalu expired (diulang untuk keduanya)
- Target "Gilang Hartono" adalah User Basic biasa

## Test Steps

1. Buka sub-tab "Login User" di User List
2. Coba `[+ User]`, isi field wajib, lalu `[Submit]`
3. Coba Edit pada target, Delete, Toggle Active, Resend, dan Pair TAG
4. Verifikasi semua aksi tulis diblokir dan data target tidak berubah
5. Verifikasi aksi baca (List, User Detail, Changelog) tetap berfungsi
6. Ulangi langkah 2–5 untuk status client expired

## Notes

- Sumber `user.md` §9.4.2 baris "Semua aksi tulis" (D1). Pasangan `TC-GS-BRAND-136` dan `TC-GS-ROLE-110`.
- Copy penolakan belum didefinisikan PRD, jadi spec ini hanya memverifikasi aksi diblokir, bukan teksnya.
- Mode mock dipakai karena status client tidak bisa diubah dari UI.
