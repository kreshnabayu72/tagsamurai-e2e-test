---
id: TC-GS-USER-E2E-099-list-badge-pending-mutually-exclusive
title: 'Badge Pending Activation dan Pending Email Confirmation tidak tampil bersamaan'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-338
  - TC-GS-USER-4
coverage:
  web: automated
---

# Badge Pending Activation dan Pending Email Confirmation tidak tampil bersamaan

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User A berstatus Pending Activation
- User B berstatus Activated dengan email pending
- User C berstatus Activated tanpa pending apa pun
- Spec ini tidak mengubah data

## Test Steps

1. Amati kolom Name pada baris User A, B, dan C di User List
2. Verifikasi User A menampilkan badge "Pending Activation"
3. Verifikasi User B menampilkan badge "Pending Email Confirmation" (bukan "Pending Activation")
4. Verifikasi User C tidak menampilkan badge sama sekali
5. Verifikasi tidak ada baris yang menampilkan dua badge sekaligus

## Notes

- Sumber `user.md` bagian 3 dan 4.2a. Kedua badge memakai severity warning dan mutually exclusive. Teks "Pending Email Confirmation" mengikuti keputusan sementara `GAP-279`.
- `TC-GS-USER-4` (peralihan badge Pending Activation, hilang setelah Activated, lalu Pending Email Confirmation setelah ganti email) diverifikasi bertahap di `TC-GS-USER-E2E-049-aktivasi-akun-dampak-user` dan `025-edit-email-pending-change`. Spec ini memverifikasi tampilan statis ketiga keadaan.
