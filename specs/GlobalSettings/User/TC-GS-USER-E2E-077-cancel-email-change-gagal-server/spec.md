---
id: TC-GS-USER-E2E-077-cancel-email-change-gagal-server
title: 'Batalkan perubahan email gagal karena error server'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-559
coverage:
  web: automated
---

# Batalkan perubahan email gagal karena error server

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan batalkan perubahan email
- User "Rudi Reset" berstatus Activated dengan email pending

## Test Steps

1. Klik row action `Edit` pada baris "Rudi Reset"
2. Verifikasi label "Pending email change to [email baru]" dan tombol `[Cancel]` tampil di bawah field Email
3. Klik `[Cancel]` lalu konfirmasi pembatalan di dialog saat server membalas `500`
4. Verifikasi toast "Error, failed to cancel email change." muncul
5. Verifikasi label "Pending email change to [email baru]" dan tombol `[Cancel]` tetap tampil dan pending state tidak berubah
6. Tutup modal dan buka Changelog "Rudi Reset"
7. Verifikasi tidak ada baris "Cancel Email Change"

## Notes

- Sumber `user.md` bagian 4.1, 7, dan 8.2. Alur batal yang berhasil dicakup `TC-GS-USER-E2E-025-edit-email-pending-change`.
