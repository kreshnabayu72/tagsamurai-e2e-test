---
id: TC-GS-USER-E2E-156-empty-tab-changelog-detail
title: Tab Changelog di User Detail menampilkan empty state saat pencarian tanpa hasil
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-615
coverage:
  web: automated
---

# Tab Changelog di User Detail menampilkan empty state saat pencarian tanpa hasil

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Hendra Wijaya" punya riwayat Changelog
- Spec ini hanya membaca data

## Test Steps

1. Buka User Detail "Hendra Wijaya" > Tab Changelog
2. Ketik kata kunci yang tidak ada di kotak Search
3. Verifikasi ilustrasi dengan "No results found" dan "Try adjusting your search or filter." sementara kolom dan toolbar tetap tampil
4. Hapus kata kunci dan verifikasi baris kembali tampil

## Notes

- Sumber `user.md` §7 dan §7.1.
