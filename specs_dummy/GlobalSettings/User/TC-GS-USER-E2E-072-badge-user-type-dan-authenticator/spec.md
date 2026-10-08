---
id: TC-GS-USER-E2E-072-badge-user-type-dan-authenticator
title: 'Badge User Type dan status Authenticator di General Information'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-122
  - TC-GS-USER-123
  - TC-GS-USER-124
  - TC-GS-USER-426
  - TC-GS-USER-125
coverage:
  web: automated
---

# Badge User Type dan status Authenticator di General Information

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Siti Rahmawati" berstatus Total Control
- User "Rina Readonly" berstatus Read Only
- User "Tono Individual" tanpa Access Level tetapi punya minimal satu role aktif dengan izin lihat di Global Settings
- User "Bagus Basic" tanpa Access Level dan tanpa role aktif
- User Non-Login "Rudi Hartono"
- User "Rina Wijaya" sudah enrolled Authenticator dan user "Umar Belum" belum enrolled
- Spec ini tidak mengubah data

## Test Steps

### User Type

1. Buka User Detail "Siti Rahmawati" dan verifikasi badge User Type di General Information > Access & Status adalah `Total Control`
2. Buka User Detail "Rina Readonly" dan verifikasi badge `Read Only`
3. Buka User Detail "Tono Individual" dan verifikasi badge `Admin`
4. Buka User Detail "Bagus Basic" dan verifikasi badge `Basic`
5. Buka Detail Non-Login User "Rudi Hartono" dan verifikasi badge `Non Login`

### Authenticator

6. Buka User Detail "Rina Wijaya" dan verifikasi badge `Enrolled` beserta tombol `Reset Authenticator`
7. Buka User Detail "Umar Belum" dan verifikasi teks "Not enrolled yet" tanpa tombol `Reset Authenticator`

## Notes

- Sumber `user.md` bagian 4.1. Badge User Type diturunkan dari `access_level` dan jumlah role aktif.
- TC sumber menyebut warna badge (`Total Control` success, `Admin` danger, `Basic` primary, `Read Only` warning), tetapi PRD hanya menetapkan warna `Non Login` (dark). Spec ini memverifikasi teks badge saja. Lihat `GAP-294`.
- `Non Login` ditambahkan dari PRD `user.md` bagian 4.1 sebagai pelengkap lima nilai badge.
