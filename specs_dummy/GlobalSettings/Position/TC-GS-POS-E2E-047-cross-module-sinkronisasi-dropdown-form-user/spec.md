---
id: TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user
title: "External Harness: Sinkronisasi Position baru, rename, dan terhapus ke dropdown form User, Non-Login User, dan filter User List"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-256
  - TC-GS-POS-257
  - TC-GS-POS-258
  - TC-GS-POS-281
  - TC-GS-POS-301
coverage:
  web: automated
---

# External Harness: Sinkronisasi Position baru, rename, dan terhapus ke dropdown form User, Non-Login User, dan filter User List

## Prerequisites

- Login sebagai Total Control
- Akses ke sub-tab Position, User List, dan Non-Login User

## Test Steps

### Sinkronisasi Position Baru ke Form User

1. Di tab Position, buat Position baru "Platform Architect"
2. Pindah ke sub-tab "User List", klik tombol "[+ User]"
3. Buka dropdown pilihan Position pada form Create User
4. Verifikasi "Platform Architect" langsung muncul di dalam opsi dropdown
5. Buka modul Non-Login User, buka form Create, verifikasi "Platform Architect" juga tersedia

### Sinkronisasi Rename ke Data User & Filter List

6. Buat seorang user dengan memilih Position "Platform Architect"
7. Kembali ke tab Position, edit "Platform Architect" menjadi "Principal Platform Architect"
8. Buka kembali User List, verifikasi nama jabatan pada baris user tersebut otomatis terupdate menjadi "Principal Platform Architect"
9. Buka Filter Panel di User List, verifikasi opsi filter Position mencerminkan nama baru "Principal Platform Architect"

### Sinkronisasi Penghapusan & Guard Form User

10. Kembali ke tab Position, buat position sementara "Temp Role"
11. Buka form User di tab lain dan pilih "Temp Role" (belum disimpan)
12. Hapus "Temp Role" dari tab Position
13. Kembali ke form User dan klik "[Submit]"
14. Verifikasi submit ditolak dengan pesan error field-level bahwa jabatan yang dipilih sudah tidak tersedia

## Notes

- Menggabungkan seluruh sinkronisasi lintas modul dari TC-GS-POS-256, 257, 258, 281, dan 301.
