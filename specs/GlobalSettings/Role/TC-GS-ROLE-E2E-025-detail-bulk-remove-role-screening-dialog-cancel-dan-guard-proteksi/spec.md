---
id: TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi
title: "Screening Dialog Bulk Remove Role (Varian Homogen vs Campuran TC/RO), Pembatalan Cancel, dan Guard Self-Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-46
  - TC-GS-ROLE-47
  - TC-GS-ROLE-49
  - TC-GS-ROLE-50
  - TC-GS-ROLE-356
coverage:
  web: automated
---

# Screening Dialog Bulk Remove Role (Varian Homogen vs Campuran TC/RO), Pembatalan Cancel, dan Guard Self-Edit

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia beberapa user target reguler dan target user berstatus Total Control pada Detail role

## Test Steps

1. Buka Detail role pada Tab System
2. Centang 2 user target reguler (tanpa status TC/RO)
3. Klik tombol [Remove] pada Bulk Action Bar
4. Verifikasi dialog varian homogen muncul dengan judul "2 users selected"
5. Verifikasi pesan dialog memuat: "This will remove [Role Name] access from the selected users. Are you sure you want to remove them?" dengan tombol [Cancel] dan [Remove]
6. Klik tombol [Cancel] pada dialog dan verifikasi seleksi tidak dihapus
7. Centang tambahan 1 user yang berstatus Total Control sehingga seleksi menjadi campuran reguler dan TC
8. Klik tombol [Remove] pada Bulk Action Bar
9. Verifikasi dialog varian campuran muncul menampilkan peringatan bahwa user berstatus Total Control akan kehilangan akses Total Control sebagai akibatnya
10. Verifikasi tombol konfirmasi pada varian campuran adalah [Cancel] dan [Continue]
11. Klik tombol [Cancel] untuk membatalkan aksi

## Notes

- Dialog bulk remove membedakan secara tegas alur homogen (semua reguler) dengan alur campuran yang berdampak mencabut access_level (role.md §3).
