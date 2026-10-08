---
id: TC-GS-USER-E2E-170-file-manager-override-hapus-foto-profil
title: Admin override Delete foto profil di File Manager mengembalikan avatar ke inisial dan tercatat di Changelog
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-630
coverage:
  web: automated
---

# Admin override Delete foto profil di File Manager mengembalikan avatar ke inisial dan tercatat di Changelog

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Umar Foto" punya foto profil aktif yang tampil di File Manager
- Spec ini menghapus foto profil target, jadi foto di-seed ulang setelah run

## Test Steps

1. Buka Global Settings > File Manager dan hapus foto profil aktif "Umar Foto"
2. Buka User List dan User Detail "Umar Foto"
3. Verifikasi avatar kembali ke inisial di List dan Detail
4. Buka Tab Changelog dan verifikasi ada entri Action "Edit" Field "Photo" tanpa Old/New Value dengan Modified By admin yang menghapus, bukan System

## Notes

- Sumber `user.md` §8.2 (catatan Photo, trigger kedua) dan `file-manager` F-FILEMGR-02. Arah Affected dari File Manager ke modul User.
