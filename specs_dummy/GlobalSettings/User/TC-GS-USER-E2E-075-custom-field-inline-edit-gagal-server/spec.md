---
id: TC-GS-USER-E2E-075-custom-field-inline-edit-gagal-server
title: 'Inline-edit Custom Field gagal karena error server'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-577
coverage:
  web: automated
---

# Inline-edit Custom Field gagal karena error server

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan simpan inline-edit Custom Field (`PATCH` ke user "Budi Santoso") saat langkah simpan
- User "Budi Santoso" punya Custom Field aktif `Blood Type` dengan value existing

## Test Steps

1. Buka User Detail "Budi Santoso", expand Section Custom Fields, lalu klik ikon `Edit2Line` pada `Blood Type`
2. Isi value baru `O+` lalu klik `[✓ Save]` saat server membalas `500`
3. Verifikasi toast "Error, failed to update Blood Type." muncul
4. Verifikasi field tetap dalam state Active dengan value `O+` yang diketik masih ada
5. Klik `[✕ Cancel]` dan verifikasi baris kembali ke state Display dengan value lama, karena value tersimpan tidak berubah

## Notes

- Spec hanya-FE (`Mode: mock`). Sumber `user.md` bagian 6 dan 7 (Save gagal server). Alur inline-edit yang berhasil dicakup `TC-GS-USER-E2E-064-custom-field-inline-edit`.
