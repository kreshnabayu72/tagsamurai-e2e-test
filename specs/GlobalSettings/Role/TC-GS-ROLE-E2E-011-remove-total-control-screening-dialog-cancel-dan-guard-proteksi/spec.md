---
id: TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi
title: "Screening Dialog Konfirmasi Remove Total Control, Pembatalan Cancel, dan Guard Default User serta Self-Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-21
  - TC-GS-ROLE-23
  - TC-GS-ROLE-24
  - TC-GS-ROLE-26
coverage:
  web: automated
---

# Screening Dialog Konfirmasi Remove Total Control, Pembatalan Cancel, dan Guard Default User serta Self-Edit

## Prerequisites

- Login sebagai Role: Total Control (menggunakan akun totalControl2, bukan Default User)
- Tersedia Default User dan Siti Rahmawati ter-assign di Tab Total Control

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Amati baris Default User pada tabel
3. Verifikasi row action [⋯] Remove berada dalam status Disabled dengan tooltip "Default User must always have Total Control."
4. Amati baris akun sendiri (totalControl2) pada tabel
5. Verifikasi row action [⋯] Remove berada dalam status Disabled dengan tooltip "You cannot change your own access level."
6. Klik row action [⋯] pada baris Siti Rahmawati lalu pilih 'Remove'
7. Verifikasi dialog konfirmasi terbuka menampilkan teks bullet nama: "• Siti Rahmawati"
8. Verifikasi deskripsi dialog memuat: "This will remove Total Control from this user. Their individual permissions will be reset and they will have no access assigned. Are you sure you want to remove it?"
9. Verifikasi dialog menyediakan tombol [Cancel] dan tombol [Remove]
10. Klik tombol [Cancel] pada dialog konfirmasi
11. Verifikasi dialog konfirmasi tertutup seketika
12. Verifikasi Siti Rahmawati tetap berada di Tab Total Control dan tidak ada toast yang muncul

## Notes

- Default User tidak pernah bisa di-remove Total Control-nya sebagai jaminan struktural keamanan sistem (ROLE-LOGIC-02).
