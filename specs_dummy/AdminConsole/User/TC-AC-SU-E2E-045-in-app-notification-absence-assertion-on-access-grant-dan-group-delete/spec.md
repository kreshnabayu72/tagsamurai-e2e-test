---
id: TC-AC-SU-E2E-045-in-app-notification-absence-assertion-on-access-grant-dan-group-delete
title: "Asersi Ketiadaan Notifikasi In-App pada Penugasan Akses Baru dan Penghapusan Grup"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-211
  - TC-AC-SU-212
  - TC-AC-SU-248
coverage:
  web: automated
---

# Asersi Ketiadaan Notifikasi In-App pada Penugasan Akses Baru dan Penghapusan Grup

## Prerequisites

- Context A: Login sebagai Total Control
- Context B: Login sebagai Target User

## Test Steps

### Penugasan Akses Baru di Context Admin (Context A)
1. Di Context A, berikan penugasan Global Role atau Group Role baru kepada Target User
2. Hapus salah satu grup umum di mana Target User terdaftar sebagai anggota biasa

### Asersi Ketiadaan Notifikasi di Context Target (Context B)
3. Di Context B, buka panel notifikasi in-app
4. Lakukan polling verifikasi selama 10 detik penuh
5. Verifikasi bahwa TIDAK ADA notifikasi baru yang masuk untuk event penugasan role baru (PRD §9.12 menetapkan penugasan baru tidak memicu notifikasi)
6. Verifikasi bahwa TIDAK ADA notifikasi yang masuk untuk event penghapusan grup umum
7. Pastikan integritas panel notifikasi target user bersih dari pesan redundan

## Notes

Memastikan kepatuhan aturan bisnis ketiadaan notifikasi (assertion of absence) per PRD §9.12.
