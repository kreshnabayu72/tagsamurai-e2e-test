---
id: TC-GS-USER-E2E-080-download-gagal-server
title: 'Download User List gagal karena error server'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-363
coverage:
  web: automated
---

# Download User List gagal karena error server

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan Download User List

## Test Steps

1. Klik ikon Download di toolbar User List dan pilih format CSV saat server membalas `500`
2. Verifikasi toast "Error, failed to download User." muncul
3. Verifikasi tidak ada berkas yang terunduh

## Notes

- Sumber `user.md` bagian 4.4 dan 7. Download yang berhasil dicakup `TC-GS-USER-E2E-100-list-download-wysiwyg` (batch berikutnya).
