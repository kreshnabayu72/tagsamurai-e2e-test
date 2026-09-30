---
id: TC-GS-USER-E2E-123-bulk-delete-sebagian-gagal
title: 'Bulk Delete sebagian gagal karena satu user sudah dihapus'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-39
coverage:
  web: automated
---

# Bulk Delete sebagian gagal karena satu user sudah dihapus

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: dari tiga permintaan Delete, satu dibalas `404` dan dua dibalas sukses
- Tiga user "Target Satu", "Target Dua", dan "Target Tiga" ada

## Test Steps

1. Pilih ketiga baris lalu klik bulk action `Delete` dan konfirmasi saat salah satu dibalas `404`
2. Verifikasi toast "Success, user has been deleted. Some items failed." muncul
3. Verifikasi baris yang berhasil dihapus hilang dari tabel dan baris yang gagal tetap tampil

## Notes

- Sumber `user.md` bagian 7 (toast partial). Bulk Delete yang berhasil dicakup `TC-GS-USER-E2E-005-delete-user`.
