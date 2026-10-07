---
id: TC-GS-ACTLOG-E2E-015-tab-session-entri-dasar-login-logout-dan-status-dash
title: "Tab Session: Entri Dasar Login Berhasil, Logout Normal dengan Status Dash, Sesi GS, dan Format Sel Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-41
  - TC-GS-ACTLOG-45
  - TC-GS-ACTLOG-51
  - TC-GS-ACTLOG-52
  - TC-GS-ACTLOG-53
  - TC-GS-ACTLOG-226
coverage:
  web: automated
---

# Tab Session: Entri Dasar Login Berhasil, Logout Normal dengan Status Dash, Sesi GS, dan Format Sel Kosong

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat aktivitas Login, Logout, dan Sesi modul Global Settings di entitas aktif

## Test Steps

### Entri Login Berhasil
1. Buka Tab Session di menu Global Settings > Activity Log.
2. Cari entri aktivitas Login milik pengguna 'Budi Santoso'.
3. Verifikasi baris memuat: Date, User 'Budi Santoso', Employee ID, Position, Division, Activity 'Login', Status 'Success', IP Address, dan Device / Browser.
4. Verifikasi sel Date berformat plain text tanpa tautan atau clickable cursor.
### Entri Logout Normal & Status Dash
5. Cari entri aktivitas Logout normal pengguna 'Budi Santoso'.
6. Verifikasi kolom Activity menampilkan 'Logout'.
7. Verifikasi kolom Status menampilkan tanda pisah em-dash '—' (tidak ada status Success maupun Failed untuk logout normal).
### Sesi Modul Global Settings & Sel Kosong
8. Cari entri sesi pengguna yang beraktivitas di dalam modul Global Settings.
9. Verifikasi tercatat di Tab Session dengan detail sesi yang valid.
10. Periksa entri dengan nilai Note, IP Address, atau Device yang tidak tercatat.
11. Verifikasi sel yang kosong dirender sebagai tanda pisah em-dash '—' secara konsisten.

## Notes

- Aktivitas Logout tidak memiliki konsep status berhasil/gagal sehingga selalu berstatus '—'. Sel tanpa nilai dirender '—'.
