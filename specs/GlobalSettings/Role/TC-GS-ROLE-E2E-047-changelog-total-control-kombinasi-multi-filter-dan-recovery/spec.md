---
id: TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery
title: "Kombinasi Search dan Multi-Filter Modal Changelog Total Control Serta Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-193
  - TC-GS-ROLE-194
  - TC-GS-ROLE-195
  - TC-GS-ROLE-196
  - TC-GS-ROLE-197
  - TC-GS-ROLE-198
  - TC-GS-ROLE-199
  - TC-GS-ROLE-200
coverage:
  web: automated
---

# Kombinasi Search dan Multi-Filter Modal Changelog Total Control Serta Pemulihan Empty State

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia log di modal Changelog Total Control

## Test Steps

1. Buka Modal Changelog Total Control
2. Terapkan pencarian Search box dan beberapa filter sekaligus pada Filter Panel
3. Verifikasi tabel Changelog menampilkan irisan data log yang cocok
4. Lakukan sorting kolom Date saat Search dan Filter aktif dan verifikasi pengurutan data filtered
5. Klik [Clear All] pada Filter Panel dan verifikasi query Search box tetap aktif
6. Ketik kata kunci pencarian yang tidak menghasilkan log apa pun
7. Verifikasi ilustrasi kosong "No results found" tampil di modal Changelog
8. Klik tombol [Clear Search/Filter] untuk memulihkan tampilan data log

## Notes

- Pengujian multi-filter dan pemulihan menjamin transparansi riwayat audit pada modal Changelog (role.md §9.8).
