---
id: TC-GS-USER-E2E-155-empty-modal-changelog-list
title: Modal Changelog List-level menampilkan empty state saat pencarian tanpa hasil
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-614
coverage:
  web: automated
---

# Modal Changelog List-level menampilkan empty state saat pencarian tanpa hasil

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Riwayat Changelog sudah ada
- Spec ini hanya membaca data

## Test Steps

1. Klik icon Changelog di toolbar User List
2. Ketik kata kunci yang tidak ada di kotak Search
3. Verifikasi ilustrasi dengan "No results found" dan "Try adjusting your search or filter."
4. Hapus kata kunci dan verifikasi baris riwayat kembali tampil

## Notes

- Pasangan `TC-GS-USER-E2E-109` sampai `116` untuk modal Role. Sumber `user.md` §7 dan §7.1.
