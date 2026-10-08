---
id: TC-GS-USER-E2E-061-responsibilities-empty-state
title: 'Empty state per sub-tab Responsibilities dan hasil pencarian tanpa kecocokan'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-102
  - TC-GS-USER-547
  - TC-GS-USER-548
  - TC-GS-USER-549
coverage:
  web: automated
---

# Empty state per sub-tab Responsibilities dan hasil pencarian tanpa kecocokan

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client dengan FAMS aktif
- User "Gita Sebagian" hanya punya baris di Pending Tasks, sedangkan Borrowed Assets, Assigned Assets, dan Pending Approvals kosong
- User "Hadi Sebagian" hanya punya baris di Borrowed Assets, sedangkan Pending Tasks kosong
- Spec ini tidak mengubah data

## Test Steps

### Client

1. Buka User Detail "Gita Sebagian" > Tab Responsibilities > sub-tab Borrowed Assets
2. Verifikasi sub-tab tetap muncul dan menampilkan "No borrowed assets" dengan deskripsi "This user has no borrowed assets currently."
3. Buka sub-tab Assigned Assets dan verifikasi "No assigned assets" dengan deskripsi "This user has no assigned assets currently."
4. Buka sub-tab Pending Approvals dan verifikasi "No pending approvals" dengan deskripsi "You have no pending approval requests at this moment."
5. Buka User Detail "Hadi Sebagian" > sub-tab Pending Tasks dan verifikasi "No pending tasks" dengan deskripsi "This user has no pending confirmation tasks."

### Pencarian tanpa kecocokan

6. Pada "Hadi Sebagian" > Borrowed Assets, cari `zzznotfound`
7. Verifikasi "No results found" dengan deskripsi "Try adjusting your search or filter." tampil, berbeda dari empty state genuinely empty

## Notes

- Sumber `user.md` bagian 4.2a, 7, dan 7.1. Empty state per sub-tab hanya bisa dilihat pada user yang punya data di sub-tab lain. Bila semua sub-tab kosong, yang tampil adalah empty state global (`TC-GS-USER-E2E-059-responsibilities-gating-subscription`).
- Bagian Principal dari `TC-GS-USER-548` (entity Principal dengan nol approval) tidak masuk spec ini. PRD ambigu antara empty state sub-tab dan global, dicatat di `GAP-282`.
