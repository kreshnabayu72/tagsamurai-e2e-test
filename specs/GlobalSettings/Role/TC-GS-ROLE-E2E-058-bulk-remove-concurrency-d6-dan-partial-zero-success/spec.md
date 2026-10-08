---
id: TC-GS-ROLE-E2E-058-bulk-remove-concurrency-d6-dan-partial-zero-success
title: "Konkurensi Pencabutan Massal: Sebagian Baris Dihapus Sesi Lain, Perubahan Status TC Parsial, dan 0 Baris Berhasil"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-134
  - TC-GS-ROLE-296
  - TC-GS-ROLE-299
coverage:
  web: automated
---

# Konkurensi Pencabutan Massal: Sebagian Baris Dihapus Sesi Lain, Perubahan Status TC Parsial, dan 0 Baris Berhasil

## Prerequisites

- Dual session context (Sesi admin A dan admin B)
- Data Uji: Wawan Setiawan, Nina Kartika, Dimas Anggara, Gita Permata
- Setup Hook: dualContext: sessionA, sessionB
- Login sbg Role: Total Control (Ahmad Fauzi)
- Eko Prasetyo login di sesi B
- Dua admin (sesi A: Hendra Wijaya, Manage user and role C/R/U/D; sesi B: Total Control)
- Wawan Setiawan dan Nina Kartika punya baris Manage TAG, tanpa access level
- Dimas Anggara dan Gita Permata (Pre-setup #18) punya baris Manage hardware, tanpa access level

## Test Steps

### Bulk Remove saat sebagian baris sudah dihapus admin lain (TC-GS-ROLE-134)

1. Sesi A: Detail "Manage hardware" > centang 2 baris
2. Sesi B: Remove salah satu baris itu
3. Sesi A: Bulk Action > Remove > [Remove]
4. Verifikasi Muncul toast sukses: "Success, user has been removed." (bukan toast parsial)
5. Verifikasi Kedua baris tidak ada di Detail
6. Verifikasi Changelog memuat 1 entry Remove dari sesi B untuk baris yang sudah dihapus dan 1 entry dari sesi A untuk baris lainnya

### Bulk Remove saat status Total Control target berubah antara render dan submit (TC-GS-ROLE-296)

7. Sesi A: Detail "Manage TAG" > centang Wawan Setiawan dan Nina Kartika
8. Sesi B: assign Total Control ke Wawan Setiawan
9. Sesi A: Bulk Action > Remove > [Remove]
10. Verifikasi Baris Nina Kartika terhapus
11. Verifikasi Baris Wawan Setiawan tetap ada (ditolak per baris, dihitung gagal)
12. Verifikasi Muncul toast sukses parsial: "Success, user has been removed. Some items were skipped."
13. Verifikasi Bulk Action Bar tertutup dan seleksi di-reset ke 0
14. Verifikasi Tidak ada dialog konflik; Changelog hanya memuat entry Remove Nina Kartika dari sesi A

### Bulk Remove saat semua baris ditolak per baris (0 berhasil) (TC-GS-ROLE-299)

15. Sesi A: Detail "Manage hardware" > centang Dimas Anggara dan Gita Permata
16. Sesi B: assign Total Control ke Dimas Anggara dan Gita Permata
17. Sesi A: Bulk Action > Remove > [Remove] pada dialog
18. Sesi A: buka Changelog Detail "Manage hardware"
19. Verifikasi Muncul toast error: "Error, failed to remove user."
20. Verifikasi Kedua baris tetap ada di Detail "Manage hardware" (keduanya ditolak per baris, tidak ada baris terhapus)
21. Verifikasi Bulk Action Bar tertutup dan seleksi di-reset ke 0
22. Verifikasi Tidak ada toast sukses maupun toast sukses parsial, dan tidak ada dialog konflik
23. Verifikasi Changelog Detail "Manage hardware" tidak memuat entry Remove untuk Dimas Anggara maupun Gita Permata

## Notes

- Memvalidasi alur skenario "Konkurensi Pencabutan Massal: Sebagian Baris Dihapus Sesi Lain, Perubahan Status TC Parsial, dan 0 Baris Berhasil".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Bulk D6; global-settings/role/PRD/role.md §9.2 [F-ROLE-07]; global-settings/role/PRD/role.md §9.4.2 Bulk D6 status TC/RO berubah; global-settings/role/PRD/role.md §9.6; global-settings/role/PRD/role.md §7.1 T-11; global-settings/role/PRD/role.md §9.4.2 Bulk D9 0 baris berhasil; global-settings/role/PRD/role.md §7.1 T-10; global-settings/role/PRD/role.md §4.4.
- Sumber pemetaan test case granular: TC-GS-ROLE-134, TC-GS-ROLE-296, TC-GS-ROLE-299.
