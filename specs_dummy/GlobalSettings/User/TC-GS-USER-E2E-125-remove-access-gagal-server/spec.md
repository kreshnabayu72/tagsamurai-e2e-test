---
id: TC-GS-USER-E2E-125-remove-access-gagal-server
title: 'Remove Access lewat modal Edit gagal karena error server'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-53
coverage:
  web: automated
---

# Remove Access lewat modal Edit gagal karena error server

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan simpan Edit setelah dialog peringatan dikonfirmasi
- User "Ahmad Fauzi" punya Access ke FAMS dengan aset atau approval aktif (memicu dialog peringatan)

## Test Steps

1. Klik row action `Edit` pada baris "Ahmad Fauzi" dan hapus centang produk FAMS di field Access
2. Konfirmasi dialog peringatan lalu klik `[Save]` saat server membalas `500`
3. Verifikasi toast "Error, failed to update user." muncul (Remove Access memakai toast Edit standar)
4. Verifikasi modal Edit tetap terbuka, checkbox FAMS tetap tidak tercentang, dan tombol `[Save]` kembali aktif

## Notes

- Sumber `user.md` bagian 7 dan [F-USER-03]. Remove Access yang berhasil dicakup `TC-GS-USER-E2E-009-remove-access-user`.
