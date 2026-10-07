---
id: TC-AUTH-MFA-E2E-031-session-management-dan-paritas-subscription-plan
title: "Interaksi Session Management: Dialog Duplicate Login dan Paritas Subscription Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-179
  - TC-AUTH-MFA-180
  - TC-AUTH-MFA-181
  - TC-AUTH-MFA-182
  - TC-AUTH-MFA-183
  - TC-AUTH-MFA-184
  - TC-AUTH-MFA-185
  - TC-AUTH-MFA-186
  - TC-AUTH-MFA-187
coverage:
  web: automated
---
# Interaksi Session Management: Dialog Duplicate Login dan Paritas Subscription Plan

## Prerequisites

- Akun pengguna dari Client berstatus Suspended dan Expired.
- Akun pengguna dari Client bertier Starter, Growth, Professional, dan Enterprise.
- Akun pengguna dari entitas Distributor, Partner, dan Principal.
- Dua browser terpisah untuk pengujian duplikasi login.

## Test Steps

### Interaksi dengan Session Management: Dialog Duplicate Login Attempt

1. Login sebagai user pada Browser 1 hingga masuk ke Portal — Product Hub
2. Buka Browser 2 dan login dengan user yang sama hingga menyelesaikan faktor-2 MFA
3. Verifikasi setelah MFA di Browser 2 selesai, sistem Session Management memunculkan Dialog "Duplicate Login Attempt" untuk mengonfirmasi pengalihan sesi
4. Konfirmasi pengalihan sesi di Browser 2 dan verifikasi sesi di Browser 1 dicabut

### Paritas lintas Client Suspended dan Expired

5. Lakukan login untuk user dari Client berstatus Suspended yang terkena pemicu MFA
6. Verifikasi alur pemilihan metode dan verifikasi faktor-2 MFA berjalan penuh tanpa pemblokiran (pembatasan read-only dimiliki oleh Session Management pasca login)
7. Lakukan login untuk user dari Client berstatus Expired dan verifikasi MFA berjalan normal

### Paritas tanpa gating lintas paket lisensi dan jenis entitas

8. Lakukan pengujian login MFA untuk akun dari tier Starter, Growth, Professional, dan Enterprise
9. Verifikasi seluruh fungsionalitas MFA tersedia identik tanpa pembatasan fitur (MFA tidak di-gate per paket langganan)
10. Lakukan pengujian login MFA untuk akun dari entitas Distributor, Partner, dan Principal
11. Verifikasi alur verifikasi faktor kedua berjalan seragam tanpa perbedaan alur antarmuka

## Notes

- Sesuai PRD §9.10 dan §9.11, fitur keamanan MFA berlaku universal untuk seluruh paket langganan dan seluruh jenis entitas.
- Sesuai keputusan NC-10, status subscription Client tidak memblok alur verifikasi faktor kedua.
