---
id: TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi
title: "Screening Dialog Remove Role Assignment Tunggal, Pembatalan Cancel, dan Guard Self-Edit serta Target TC/RO"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-41
  - TC-GS-ROLE-43
  - TC-GS-ROLE-44
  - TC-GS-ROLE-115
coverage:
  web: automated
---

# Screening Dialog Remove Role Assignment Tunggal, Pembatalan Cancel, dan Guard Self-Edit serta Target TC/RO

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user Budi Santoso ter-assign pada Detail role Manage master reference
- Tersedia baris aktor sendiri dan target TC

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage master reference'
2. Klik row action [⋯] pada baris Budi Santoso lalu pilih 'Remove'
3. Verifikasi dialog konfirmasi terbuka menampilkan bullet nama: "• Budi Santoso"
4. Verifikasi pesan dialog memuat: "This will remove Manage master reference access from this user. Are you sure you want to remove it?"
5. Verifikasi dialog menyediakan tombol [Cancel] dan [Remove]
6. Klik tombol [Cancel] pada dialog konfirmasi
7. Verifikasi dialog tertutup tanpa menghapus data Budi Santoso
8. Amati baris akun sendiri pada tabel Detail dan verifikasi row action Remove disabled dengan tooltip self-edit

## Notes

- Dialog konfirmasi pencabutan role tunggal menyebutkan nama spesifik role yang akan dicabut (role.md §3).
