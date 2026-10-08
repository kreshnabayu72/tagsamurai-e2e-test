---
id: TC-AC-SU-E2E-016-row-action-deactivate-user-dual-session-real-time-force-logout
title: "Terminasi Sesi Real-Time dan Force Logout Saat Deaktivasi User Target"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-27
coverage:
  web: automated
---

# Terminasi Sesi Real-Time dan Force Logout Saat Deaktivasi User Target

## Prerequisites

- Sesi Context A: Login sebagai Admin Console Total Control
- Sesi Context B: Login sebagai User Target yang sedang aktif beroperasi di sistem

## Test Steps

### Deaktivasi dari Sesi Admin (Context A)
1. Buka `Admin Console > Settings > User` di Context A
2. Cari User Target pada tabel daftar pengguna
3. Buka menu aksi baris `[...]` dan pilih `Deactivate User`
4. Pada dialog konfirmasi bahaya, klik `[Deactivate]`
5. Verifikasi toast sukses muncul: `"The user has been deactivated."`

### Verifikasi Force-Logout Real-Time di Sesi Target (Context B)
6. Di Context B (sesi User Target), lakukan interaksi klik atau navigasi halaman
7. Verifikasi request API mengembalikan status `401 Unauthorized`
8. Verifikasi sistem secara otomatis mencabut token sesi dan me-redirect browser Context B ke halaman `Login`
9. Verifikasi muncul banner notifikasi: `"Your account has been deactivated. Please contact your administrator."`

## Notes

Memvalidasi harness dual-session multi-context untuk memastikan sesi segera terminasi tanpa menunggu browser refresh manual.
