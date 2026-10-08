---
id: TC-GS-USER-E2E-109-changelog-modal-struktur-search
title: 'Modal Changelog User List: struktur, kolom, dan Search'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-232
  - TC-GS-USER-233
  - TC-GS-USER-250
  - TC-GS-USER-558
coverage:
  web: automated
---

# Modal Changelog User List: struktur, kolom, dan Search

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Riwayat perubahan beberapa user dengan Field beragam (Name, Position, Email, App Access, TAG) dan nilai Old/New bertipe berbeda
- Spec ini tidak mengubah data

## Test Steps

1. Klik ikon Changelog di toolbar User List
2. Verifikasi header "Changelog: User" dan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
3. Verifikasi placeholder Search "Search action, name, field, or value..."
4. Cari kata yang cocok dengan Field, Old Value, atau New Value
5. Verifikasi baris yang cocok tampil
6. Tutup modal lalu buka User Detail salah satu user > Tab Changelog
7. Verifikasi struktur identik (kolom, Filter Panel, Sort, Setup Column, Download) kecuali tidak ada kolom Name dan filter Name karena scope sudah satu user
8. Verifikasi data untuk user itu identik dengan yang tampil di modal Changelog List

## Notes

- Sumber `user.md` bagian 4.2, 4.2a, 8. Filter Field dicakup `TC-GS-USER-E2E-110-changelog-modal-filter`.
