---
id: TC-AC-SU-E2E-044-in-app-notification-delivery-on-access-removal-dan-auto-revert
title: "Pengiriman Notifikasi In-App Saat Pencabutan Akses dan Terjadinya Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-204
  - TC-AC-SU-205
  - TC-AC-SU-206
  - TC-AC-SU-208
  - TC-AC-SU-209
  - TC-AC-SU-210
  - TC-AC-SU-247
coverage:
  web: automated
---

# Pengiriman Notifikasi In-App Saat Pencabutan Akses dan Terjadinya Auto-Revert

## Prerequisites

- Context A: Login sebagai Administrator Total Control
- Context B: Login sebagai Target User pada sesi browser terpisah

## Test Steps

### Pencabutan Akses dari Context Admin (Context A)
1. Di Context A, buka Detail User target > tab `Role`
2. Cabut salah satu penugasan Global Role atau Group Role yang dimiliki target user
3. Lakukan mutasi izin yang memicu terjadinya Auto-Revert tier Total Control target user

### Verifikasi Notifikasi Real-Time di Context Target (Context B)
4. Di Context B, perhatikan ikon lonceng notifikasi di header sistem
5. Verifikasi badge notifikasi baru (counter angka merah) muncul secara reaktif
6. Klik ikon lonceng untuk membuka panel notifikasi in-app
7. Verifikasi pesan notifikasi pencabutan akses muncul: `"Your access for [Role Name] has been revoked"`
8. Verifikasi pesan notifikasi auto-revert tier muncul: `"Your tier status has changed to Custom Role"`
9. Verifikasi seluruh notifikasi bersifat informasi `view-only` tanpa tombol aksi CTA yang ambigu

## Notes

Memvalidasi penyampaian informasi real-time kepada pengguna saat terjadi perubahan wewenang.
