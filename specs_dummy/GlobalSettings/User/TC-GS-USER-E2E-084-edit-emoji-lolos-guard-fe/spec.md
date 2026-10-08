---
id: TC-GS-USER-E2E-084-edit-emoji-lolos-guard-fe
title: 'Edit menolak emoji yang lolos guard FE lewat manipulasi DOM'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-465
coverage:
  web: automated
---

# Edit menolak emoji yang lolos guard FE lewat manipulasi DOM

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Kemampuan menyuntikkan nilai ke input lewat manipulasi DOM (bukan mengetik) disediakan skrip
- User "Budi Santoso" ada

## Test Steps

1. Klik row action `Edit` pada baris "Budi Santoso"
2. Sisipkan emoji ke input Full Name lewat manipulasi DOM (bukan mengetik)
3. Klik `[Save]`
4. Verifikasi perubahan tidak tersimpan dan tidak ada toast "Success, user has been updated."
5. Verifikasi field Full Name ditandai invalid dengan pesan "Full Name contains invalid characters", atau bila sampai terkirim ke server, toast "Error, failed to update user." muncul
6. Tutup modal dan verifikasi data "Budi Santoso" di User List tidak berubah

## Notes

- Sumber `user.md` bagian 4.4 dan 7. Pasangan Edit dari `TC-GS-USER-E2E-083-create-emoji-lolos-guard-fe`.
- Toast `"Failed to update user."` di TC sumber (`TC-GS-USER-465`) dikoreksi ke `"Error, failed to update user."` sesuai PRD `user.md` bagian 7 (Changelog `tc-user.md` 2026-09-30 (10)).
