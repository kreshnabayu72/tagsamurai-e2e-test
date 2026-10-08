---
id: TC-GS-USER-E2E-112-changelog-modal-download
title: 'Download modal Changelog User List: semua data dan hasil filter'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-249
coverage:
  web: automated
---

# Download modal Changelog User List: semua data dan hasil filter

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Riwayat Changelog banyak
- Pembacaan berkas unduhan tersedia bagi skrip

## Test Steps

1. Buka modal Changelog User List dan klik Download lalu pilih CSV
2. Verifikasi berkas berisi seluruh riwayat dan tidak ada toast sukses
3. Terapkan satu filter Action lalu klik Download dan pilih XLSX
4. Verifikasi berkas hanya berisi baris hasil filter dan tidak ada toast sukses

## Notes

- Sumber `user.md` bagian 4.2a dan 8.
