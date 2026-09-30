---
id: TC-GS-USER-E2E-056-tab-role-auto-revert-notifikasi
title: 'Target menerima notifikasi saat Total Control atau Read Only dicabut otomatis lewat Tab Role'
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-252
  - TC-GS-USER-253
coverage:
  web: automated
---

# Target menerima notifikasi saat Total Control atau Read Only dicabut otomatis lewat Tab Role

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi admin
- Sesi target dengan akun "Siti Rahmawati" (Total Control) dan sesi target lain dengan akun "Rina Readonly" (Read Only), masing-masing bisa dibuka skrip dan membuka panel notifikasi in-app
- Kedua target belum punya notifikasi Auto-Revert
- Spec ini mencabut akses Total Control dan Read Only kedua target, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya. Jalankan sendirian

## Test Steps

### Total Control

1. Di sesi admin, buka User Detail "Siti Rahmawati" > Tab Role, hapus centang satu checkbox CRUD lalu klik `[Continue]` di dialog
2. Di sesi target "Siti Rahmawati", buka panel notifikasi
3. Verifikasi ada notifikasi baru berjudul "Your Total Control access was removed" dengan isi "Your Total Control access was automatically removed after [nama admin] edited your role on [tanggal]." dan bersifat view-only (tanpa aksi lanjutan)

### Read Only

4. Di sesi admin, buka User Detail "Rina Readonly" > Tab Role, hapus centang satu checkbox CRUD lalu klik `[Continue]` di dialog
5. Di sesi target "Rina Readonly", buka panel notifikasi
6. Verifikasi ada notifikasi baru berjudul "Your Read Only access was removed" dengan isi "Your Read Only access was automatically removed after [nama admin] edited your role on [tanggal]." dan bersifat view-only

## Notes

- Event dan mekanisme notifikasi dimiliki `role/PRD/role.md` bagian 8.8, dan modul User hanya memicunya dari Tab Role. Teks lengkap diambil dari PRD Role. Sumber TC hanya mengutip sebagian teks.
- Panel notifikasi in-app adalah kebutuhan Prerequisites untuk tim FE (cara membuka dan membaca notifikasi target).
