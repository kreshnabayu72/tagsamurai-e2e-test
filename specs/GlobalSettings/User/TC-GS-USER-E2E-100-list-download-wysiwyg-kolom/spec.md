---
id: TC-GS-USER-E2E-100-list-download-wysiwyg-kolom
title: 'Download User List mengikuti kolom yang sedang terlihat'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-494
coverage:
  web: automated
---

# Download User List mengikuti kolom yang sedang terlihat

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Kolom `Email` bisa disembunyikan lewat Setup Column
- Pembacaan berkas CSV yang terunduh tersedia bagi skrip
- Konfigurasi kolom dikembalikan ke default di langkah akhir

## Test Steps

1. Sembunyikan kolom `Email` lewat Setup Column
2. Klik ikon Download lalu pilih CSV
3. Verifikasi berkas CSV tidak memuat kolom `Email` dan tidak ada toast atau peringatan tambahan tentang ekspor sebagian
4. Kembalikan kolom `Email` ke tampilan lewat Setup Column

## Notes

- Sumber `user.md` bagian 4.4 dan 4.2a (`GAP-161` sudah ditutup). Cakupan kolom mengikuti kondisi terlihat saat Download diklik (WYSIWYG). Pasangan lengkap dan pembalikan unhide ada di `TC-GS-USER-496` dan `497`.
- Download yang gagal dicakup `TC-GS-USER-E2E-080-download-gagal-server`.
