---
id: TC-GS-ACTLOG-E2E-009-role-matrix-negatif-pengguna-tanpa-akses
title: "Role Matrix Negatif: Pengguna tanpa akses tidak melihat menu Activity Log dan direct URL ditolak 403"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-28
  - TC-GS-ACTLOG-29
coverage:
  web: automated
---

# Role Matrix Negatif: Pengguna tanpa akses tidak melihat menu Activity Log dan direct URL ditolak 403

## Prerequisites

- Akun pengguna dengan capability spesifik tanpa access_level Total Control maupun Read Only (mis. Create-Only Brand)

## Test Steps

1. Login sebagai pengguna dengan capability spesifik (tanpa Total Control/Read Only)
2. Buka menu Global Settings
3. Verifikasi menu "Activity Log" tidak ditampilkan (Hidden) pada sidebar menu
4. Akses URL langsung Activity Log (`/settings/activity-log`) melalui address bar browser
5. Verifikasi navigasi diblokir dan dialihkan ke halaman Unauthorized / 403 Forbidden
6. Verifikasi tidak ada data log apa pun yang ditampilkan di layar

## Notes

- Activity Log bukan capability individual, melainkan fitur eksklusif untuk level Total Control dan Read Only.
