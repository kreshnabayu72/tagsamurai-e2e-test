---
id: TC-AC-SU-E2E-038-target-user-in-app-notifications-remove-dan-auto-revert-access
title: "Notifikasi in-app ke target user pada Remove dan Auto-Revert access, format view-only, dan guard tanpa notifikasi pada Assign"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-204
  - TC-AC-SU-205
  - TC-AC-SU-206
  - TC-AC-SU-208
  - TC-AC-SU-209
  - TC-AC-SU-210
  - TC-AC-SU-211
  - TC-AC-SU-212
  - TC-AC-SU-247
  - TC-AC-SU-248
coverage:
  web: automated
---

# Notifikasi in-app ke target user pada Remove dan Auto-Revert access, format view-only, dan guard tanpa notifikasi pada Assign

## Prerequisites

- Login sebagai Role: Principal Total Control (Aktor) dan Akun Target User (Penerima Notifikasi)
- Target user memiliki peran Total Control, Read Only, dan Group Manager

## Test Steps

### Notifikasi In-App pada Auto-Revert Total Control dan Read Only

1. Sebagai admin, ubah 1 CRUD role pada target user Total Control dari Tab Role hingga memicu Auto-Revert
2. Login sebagai target user tersebut dan buka dropdown notifikasi in-app di header
3. Verifikasi notifikasi baru muncul:
4.   - Title: `"Your Total Control access was removed"`
5.   - Body: `"Your Total Control access was automatically removed after [Admin Name] edited your role on [date]."`
6.   - Tombol aksi: `[Mark as Read]` (bertipe `view-only`, tanpa tombol `[Detail]`)
7. Ulangi skenario untuk Auto-Revert Read Only, verifikasi notifikasi muncul dengan Title `"Your Read Only access was removed"`

### Notifikasi In-App pada Auto-Revert dan Manual Remove Group Manager

1. Sebagai admin, ubah penugasan group target GM hingga memicu Auto-Revert GM untuk Group X
2. Login sebagai target user, periksa notifikasi:
3.   - Title: `"You are no longer Group Manager for [Group X]"`
4.   - Body: `"Your Group Manager status for [Group X] was automatically removed after [Admin Name] edited your role on [date]."`
5. Sebagai admin, lakukan Remove Group Manager secara manual dari Settings > Role & Permission
6. Login sebagai target user, verifikasi notifikasi muncul dengan Body `"[Admin Name] removed your Group Manager status for [Group Name] on [date]."`

### Guard Ketiadaan Notifikasi pada Assign, Deactivate, dan Group Deleted

1. Sebagai admin, lakukan Assign tier Total Control ke target user, verifikasi TIDAK ADA notifikasi baru yang terkirim (hanya kehilangan akses yang dinotifikasikan)
2. Sebagai admin, lakukan Deactivate user, verifikasi tidak ada notifikasi in-app terpisah (sudah tertangani via force-logout real-time)
3. Sebagai admin, hapus Group X dari Settings > Group, verifikasi penghapusan GM akibat group dihapus TIDAK mengirimkan notifikasi in-app ke target user

## Notes

- Notifikasi in-app memberi tahu pengguna saat hak akses administratif mereka dicabut atau mengalami auto-revert.
