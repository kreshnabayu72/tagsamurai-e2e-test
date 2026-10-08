---
id: TC-GS-USER-E2E-101-list-subtab-login-non-login
title: 'Sub-tab Login User dan Non-Login User di User List menyimpan state sendiri-sendiri'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-134
  - TC-GS-USER-135
coverage:
  web: automated
---

# Sub-tab Login User dan Non-Login User di User List menyimpan state sendiri-sendiri

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Data Login User dan Non-Login User ada
- Spec ini tidak mengubah data

## Test Steps

1. Di sub-tab Login User, cari "Finance" dan tekan `Enter`
2. Klik sub-tab Non-Login User
3. Verifikasi tabel menampilkan data Non-Login User dan kotak Search kosong (state independen)
4. Klik kembali sub-tab Login User
5. Verifikasi Search masih berisi "Finance" dan hasil pencarian dipertahankan

## Notes

- Sumber `user.md` bagian 4.2 dan 4.4. CRUD dan format kolom Non-Login User diuji di modul Non-Login User dan tidak diulang di sini.
