---
id: TC-GS-USER-E2E-086-foto-hover-overlay-detail-dan-edit
title: 'Overlay hover Avatar di User Detail dan modal Edit'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-370
  - TC-GS-USER-540
coverage:
  web: automated
---

# Overlay hover Avatar di User Detail dan modal Edit

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- User "Budi Santoso" punya foto profil dan user "Umar Belum" belum punya foto profil

## Test Steps

1. Buka User Detail "Budi Santoso" lalu hover Avatar di Header
2. Verifikasi overlay muncul dengan tombol `[Edit]` dan `[Delete]`
3. Buka User Detail "Umar Belum" lalu hover Avatar
4. Verifikasi overlay muncul dengan tombol `[Edit]` saja, tanpa `[Delete]`
5. Klik row action `Edit` pada baris "Budi Santoso" di User List lalu hover field Photo
6. Verifikasi overlay `[Edit]` dan `[Delete]` tampil identik dengan langkah 2, dan hover saja tidak memicu permintaan apa pun

## Notes

- Sumber `user.md` bagian 4.1 dan 4.3. Hapus dan ganti foto yang berhasil dicakup `TC-GS-USER-E2E-039-foto-profil`.
