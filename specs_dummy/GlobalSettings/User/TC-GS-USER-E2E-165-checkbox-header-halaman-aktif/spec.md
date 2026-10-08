---
id: TC-GS-USER-E2E-165-checkbox-header-halaman-aktif
title: Checkbox header hanya memilih halaman aktif dan seleksi bertahan antar halaman
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-625
coverage:
  web: automated
---

# Checkbox header hanya memilih halaman aktif dan seleksi bertahan antar halaman

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Minimal 25 login user, page size 10
- Spec ini hanya membaca data

## Test Steps

1. Klik checkbox header di halaman 1
2. Verifikasi hanya baris di halaman 1 yang tercentang, kecuali Default User dan akun sendiri yang disabled
3. Pindah ke halaman 2 dan verifikasi baris halaman 2 tidak tercentang
4. Kembali ke halaman 1 dan verifikasi seleksi halaman 1 masih ada dan bulk bar menunjukkan jumlah terkini
5. Verifikasi tombol "Select All ({N} records)" tersedia untuk seleksi lintas halaman

## Notes

- Melengkapi `TC-GS-USER-258`. Copy tombol bergantung `GAP-304` (records atau data).
