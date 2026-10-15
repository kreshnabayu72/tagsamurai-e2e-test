---
id: TC-GS-USER-E2E-024-edit-user-screening-form-dan-validasi-field
title: "Edit User: Screening modal Edit, pemuatan data awal, dan validasi field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-160
  - TC-GS-USER-161
  - TC-GS-USER-162
  - TC-GS-USER-163
  - TC-GS-USER-164
  - TC-GS-USER-165
  - TC-GS-USER-166
  - TC-GS-USER-167
  - TC-GS-USER-168
  - TC-GS-USER-169
  - TC-GS-USER-170
  - TC-GS-USER-171
  - TC-GS-USER-172
  - TC-GS-USER-173
  - TC-GS-USER-174
  - TC-GS-USER-175
  - TC-GS-USER-176
  - TC-GS-USER-1007
coverage:
  web: automated
---

# Edit User: Screening modal Edit, pemuatan data awal, dan validasi field

## Prerequisites

- Login sebagai Role: Total Control
- User target Dewi Lestari tersedia di User List

## Test Steps

### Screening Modal Edit

1. Klik ikon menu (⋯) pada baris Dewi Lestari, pilih opsi 'Edit'
2. Verifikasi modal terbuka dengan title 'Edit User', tombol [✕] di header, dan tombol footer '[Clear Field]' serta '[Save]'
3. Verifikasi field terisi data awal Dewi Lestari secara tepat
4. Kosongkan First Name, klik '[Save]', verifikasi pesan error inline muncul

## Notes

- Menggabungkan 18 test case granular (TC-GS-USER-160 s.d. TC-GS-USER-1007).
