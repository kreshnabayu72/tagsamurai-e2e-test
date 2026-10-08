---
id: TC-GS-USER-E2E-168-my-profile-banner-pending-email
title: My Profile menampilkan banner Pending Email Change read-only tanpa Resend atau Cancel
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-628
coverage:
  web: automated
---

# My Profile menampilkan banner Pending Email Change read-only tanpa Resend atau Cancel

## Prerequisites

- Login sebagai user "Rendi Profil" yang emailnya sedang pending change (diubah admin, belum dikonfirmasi)
- Spec ini hanya membaca data

## Test Steps

1. Buka Global Settings > My Profile
2. Verifikasi teks atau banner Pending Email Change tampil dan email lama tetap tampil sebagai email aktif
3. Verifikasi tidak ada tombol Resend Confirmation Email maupun Cancel

## Notes

- Sumber `user.md` §9.2 [F-USER-03] dan `my-profile` PROFILE-LOGIC-04. Teks banner bergantung `GAP-279`.
