---
id: TC-GS-USER-E2E-076-edit-save-state-loading
title: 'Tombol Save di modal Edit loading dan tidak bisa diklik ganda'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-194
coverage:
  web: automated
---

# Tombol Save di modal Edit loading dan tidak bisa diklik ganda

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `PATCH` simpan Edit User ditunda beberapa detik supaya state loading bisa diamati, lalu dibalas sukses
- User "Budi Santoso" ada

## Test Steps

1. Klik row action `Edit` pada baris "Budi Santoso" lalu ubah Position ke nilai lain
2. Klik `[Save]`
3. Verifikasi tombol `[Save]` menampilkan loading dan Disabled selama respons belum kembali
4. Klik `[Save]` sekali lagi selagi loading
5. Verifikasi tidak ada permintaan simpan kedua yang terkirim
6. Tunggu respons sukses
7. Verifikasi modal tertutup dan toast "Success, user has been updated." muncul

## Notes

- Sumber `user.md` bagian 4.4 (Saving State). Alur Edit yang berhasil dicakup `TC-GS-USER-E2E-024-edit-user-success`.
