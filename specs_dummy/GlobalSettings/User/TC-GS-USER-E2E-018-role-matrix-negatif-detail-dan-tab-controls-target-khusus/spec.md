---
id: TC-GS-USER-E2E-018-role-matrix-negatif-detail-dan-tab-controls-target-khusus
title: "Role Matrix Negatif: Pengamanan tombol dan tab di halaman Detail untuk target khusus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-74
  - TC-GS-USER-75
  - TC-GS-USER-76
  - TC-GS-USER-77
  - TC-GS-USER-78
  - TC-GS-USER-79
  - TC-GS-USER-80
  - TC-GS-USER-81
  - TC-GS-USER-82
  - TC-GS-USER-83
  - TC-GS-USER-84
  - TC-GS-USER-996
  - TC-GS-USER-997
  - TC-GS-USER-998
  - TC-GS-USER-999
  - TC-GS-USER-1000
  - TC-GS-USER-1001
  - TC-GS-USER-1002
  - TC-GS-USER-1003
  - TC-GS-USER-1004
  - TC-GS-USER-1047
coverage:
  web: automated
---

# Role Matrix Negatif: Pengamanan tombol dan tab di halaman Detail untuk target khusus

## Prerequisites

- Pengujian pov aktor terhadap Detail Default User, Self, dan Tier Total Control

## Test Steps

### Detail Default User

1. Buka Detail Hendra Gunawan (Default User)
2. Verifikasi tombol Delete User disabled dengan tooltip Default User
3. Verifikasi Resend Email hidden bagi capability holder (TC-1047)
4. Verifikasi kontrol Tab Role terkunci disabled

### Detail Akun Sendiri dan Target Tier

5. Buka Detail akun sendiri, verifikasi tombol Deactivate dan Delete disabled
6. Buka Detail Andi Wijaya oleh aktor capability holder, verifikasi tombol header [⋯] tidak menampilkan aksi modifikasi

## Notes

- Menggabungkan 21 test case granular (TC-GS-USER-74 s.d. TC-GS-USER-1047).
