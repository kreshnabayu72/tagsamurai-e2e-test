---
id: TC-GS-USER-E2E-162-kolom-access-popup-overflow
title: Klik sel Access di List membuka popup berisi semua produk
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-622
coverage:
  web: automated
---

# Klik sel Access di List membuka popup berisi semua produk

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Oscar Multi" punya Access minimal empat produk sehingga kolom Access menampilkan "+N more"
- Spec ini hanya membaca data

## Test Steps

1. Cari "Oscar Multi" di User List
2. Klik "+N more" pada kolom Access
3. Verifikasi popup Access terbuka memuat seluruh produk user sebagai badge dark dengan nama verbatim dan urut alfabetis
4. Tutup popup dan verifikasi tidak ada perubahan pada baris atau seleksi

## Notes

- Sumber `user.md` §4.2a (kolom Access, Klik / Link).
