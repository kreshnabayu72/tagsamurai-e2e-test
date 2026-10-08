---
id: TC-GS-ROLE-E2E-044-edit-crud-detail-happy-path-dan-rapid-toggle
title: "Penyuntingan CRUD Inline pada Detail Berhasil: Auto-Save Instan, Debounce Klik Cepat, dan Aktor MUR"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-101
  - TC-GS-ROLE-102
  - TC-GS-ROLE-103
coverage:
  web: automated
---

# Penyuntingan CRUD Inline pada Detail Berhasil: Auto-Save Instan, Debounce Klik Cepat, dan Aktor MUR

## Prerequisites

- Login sebagai Total Control lalu Hendra Wijaya (MUR Update)
- Data Uji: Doni Pratama (Pre-setup #10)
- Setup Hook: beforeEach: navigateTo(Detail Manage TAG)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Doni Pratama: Manage TAG Read checked, Update unchecked
- User berada di Global Settings > Role & Permission > System > Detail "Manage files"
- Doni Pratama: Manage files Read dan Delete checked
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Wawan Setiawan punya baris Manage hardware (Read)

## Test Steps

### Edit CRUD centang Update oleh Total Control pada target biasa (TC-GS-ROLE-101)

1. Centang Update baris Doni Pratama
2. Reload halaman
3. Verifikasi Tersimpan langsung tanpa tombol Save dan tanpa dialog
4. Verifikasi Muncul toast sukses: "Success, permissions have been updated."
5. Verifikasi Setelah reload Update tetap checked; Read tetap checked

### Edit CRUD uncheck Delete oleh Total Control pada target biasa (TC-GS-ROLE-102)

6. Uncheck Delete baris Doni Pratama
7. Reload halaman
8. Verifikasi Toast sukses: "Success, permissions have been updated."
9. Verifikasi Setelah reload Delete unchecked, Read checked

### Edit CRUD oleh aktor Manage user and role dengan Update (TC-GS-ROLE-103)

10. Centang Create baris Wawan Setiawan
11. Verifikasi Toast sukses: "Success, permissions have been updated."
12. Verifikasi Create checked setelah reload

## Notes

- Memvalidasi alur skenario "Penyuntingan CRUD Inline pada Detail Berhasil: Auto-Save Instan, Debounce Klik Cepat, dan Aktor MUR".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-03]; global-settings/role/PRD/role.md §4.4 Detail; global-settings/role/PRD/role.md §7.1 T-01.
- Sumber pemetaan test case granular: TC-GS-ROLE-101, TC-GS-ROLE-102, TC-GS-ROLE-103.
