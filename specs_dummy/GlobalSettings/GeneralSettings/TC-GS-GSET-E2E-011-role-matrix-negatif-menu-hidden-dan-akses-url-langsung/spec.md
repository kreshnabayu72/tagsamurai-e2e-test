---
id: TC-GS-GSET-E2E-011-role-matrix-negatif-menu-hidden-dan-akses-url-langsung
title: "Role Matrix Negatif: menu General Settings Hidden dan akses URL langsung ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-24
  - TC-GS-GSET-25
  - TC-GS-GSET-26
  - TC-GS-GSET-27
coverage:
  web: automated
---

# Role Matrix Negatif: menu General Settings Hidden dan akses URL langsung ditolak 403

## Prerequisites

- Akun Role System Role (tanpa Access Level Total Control/Read Only)
- Akun Capability Individual (tanpa Access Level Total Control/Read Only)
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Menu Hidden di Sidebar

1. Login sebagai Role System Role, buka Global Settings
2. Verifikasi menu General Settings Hidden (tidak muncul di sidebar)
3. Login sebagai Capability Individual, buka Global Settings
4. Verifikasi menu General Settings Hidden (tidak muncul di sidebar)

### Akses URL Langsung Ditolak Server

5. Sebagai Role System Role, ketik URL halaman General Settings langsung di address bar
6. Verifikasi akses ditolak server (403): muncul toast error "You don't have permission to do this." dan elemen halaman tidak ditampilkan, tanpa redirect ke halaman unauthorized terpisah
7. Login sebagai Capability Individual, ketik URL halaman General Settings langsung di address bar
8. Verifikasi akses ditolak server (403): muncul toast error "You don't have permission to do this." dan elemen halaman tidak ditampilkan, tanpa redirect ke halaman unauthorized terpisah

## Notes

- Menggabungkan TC-GS-GSET-24 dan 25 (menu Hidden) serta TC-GS-GSET-26 dan 27 (akses URL langsung ditolak). Penolakan 403 adalah keputusan server; langkah 6 dan 8 mengasersi respons server dan tidak menampilkan elemen halaman.
