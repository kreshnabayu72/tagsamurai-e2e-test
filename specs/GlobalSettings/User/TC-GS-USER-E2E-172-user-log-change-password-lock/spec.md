---
id: TC-GS-USER-E2E-172-user-log-change-password-lock
title: Tab User Log menampilkan Note lock Change Password
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-632
coverage:
  web: automated
---

# Tab User Log menampilkan Note lock Change Password

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Doni Pratama" punya riwayat Change Password gagal pada tiap tingkat lock, disediakan tim FE lewat seeding
- Spec ini hanya membaca data

## Test Steps

1. Buka User Detail "Doni Pratama" > Tab User Log
2. Filter Activity "Change Password" dan Status "Failed"
3. Verifikasi Note "Locked 15 minutes (change password)" ada
4. Verifikasi Note "Locked 1 hour (change password)" ada
5. Verifikasi Note "Locked requires reset (change password)" ada
6. Verifikasi Note "Account locked (change password)" ada
7. Verifikasi tidak ada Note yang bersuffix nama produk

## Notes

- Sumber `auth-foundation.md` §9.1 Tabel G. Pasangan `TC-GS-USER-E2E-171`.
- Selisih dengan `user.md` §8.4 dicatat `GAP-306`.
