---
id: TC-GS-USER-E2E-078-hapus-foto-gagal-server
title: 'Hapus foto profil dari Avatar gagal karena error server'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-576
coverage:
  web: automated
---

# Hapus foto profil dari Avatar gagal karena error server

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan hapus foto profil
- User "Budi Santoso" punya foto profil

## Test Steps

1. Buka User Detail "Budi Santoso" lalu hover Avatar di Header
2. Klik `[Delete]` dan konfirmasi di dialog saat server membalas `500`
3. Verifikasi toast "Error, failed to remove photo." muncul
4. Verifikasi Avatar tetap menampilkan foto yang sama dan `profile_picture_file_id` tidak berubah

## Notes

- Sumber `user.md` bagian 4.1 dan 7. Alur hapus foto yang berhasil dicakup `TC-GS-USER-E2E-039-foto-profil`.
