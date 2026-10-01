---
id: TC-GS-USER-E2E-157-empty-tab-system-log
title: Tab System Log menampilkan empty state saat kosong dan saat pencarian tanpa hasil
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-616
coverage:
  web: automated
---

# Tab System Log menampilkan empty state saat kosong dan saat pencarian tanpa hasil

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Indra Baru" baru dibuat dan belum pernah melakukan aksi admin apa pun (System Log kosong)
- User "Julia Admin" punya riwayat aksi sebagai aktor
- Spec ini hanya membaca data

## Test Steps

1. Buka User Detail "Indra Baru" > Tab System Log
2. Verifikasi ilustrasi dengan "No changelog yet" dan "Activities and changes will appear here."
3. Buka User Detail "Julia Admin" > Tab System Log
4. Ketik kata kunci yang tidak ada di kotak Search
5. Verifikasi ilustrasi dengan "No results found" dan "Try adjusting your search or filter."

## Notes

- Sumber `user.md` §7 dan §7.1. Empty state Tab User Log tidak didefinisikan PRD secara eksplisit.
