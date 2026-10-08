---
id: TC-GS-ROLE-E2E-094-konkurensi-remove-row-detail-stale-dan-auto-revert
title: "Konkurensi Antar-Admin Remove Baris Detail: Penolakan 403, Idempotent 200, dan Auto-Revert Target Menjadi TC"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-274
  - TC-GS-ROLE-276
  - TC-GS-ROLE-297
coverage:
  web: automated
---

# Konkurensi Antar-Admin Remove Baris Detail: Penolakan 403, Idempotent 200, dan Auto-Revert Target Menjadi TC

## Prerequisites

- Dual session context (Sesi A dan Sesi B)
- Data Uji: Wawan Setiawan, Agus Salim, Fikri Ramadhan
- Setup Hook: dualContext: sessionA, sessionB
- Dua admin login (sesi A dan sesi B)
- Dua admin Total Control (sesi A, B)
- Dua admin Total Control (sesi A: Ahmad Fauzi, sesi B: Eko Prasetyo)
- Given: Fikri Ramadhan (Pre-setup #18) di-assign baris Manage hardware lewat Detail [+ Assign], tanpa access level

## Test Steps

### Remove baris yang target-nya menjadi Total Control sejak render (aktor non-Total Control) (TC-GS-ROLE-274)

1. Sesi A (Manage user and role Update) membuka Detail "Manage TAG"
2. Sesi B: assign Total Control ke Wawan Setiawan
3. Sesi A: Remove baris Wawan Setiawan > [Remove]
4. Verifikasi Muncul toast error: "You don't have permission to do this."
5. Verifikasi Baris Wawan Setiawan tidak terhapus dan tidak ada dialog konflik
6. Verifikasi UI di-refresh: row action Remove baris Wawan Setiawan disabled; tooltip "You don't have permission to edit."

### Remove baris yang sudah dihapus admin lain dianggap sukses (TC-GS-ROLE-276)

7. Sesi A dan B membuka Detail "Manage hardware"
8. Sesi B: Remove baris Agus Salim
9. Sesi A: Remove baris Agus Salim > [Remove]
10. Verifikasi Sesi A tidak menampilkan error atau dialog konflik
11. Verifikasi Baris Agus Salim tidak ada
12. Verifikasi Changelog hanya memuat 1 entry Remove Agus Salim

### Remove baris oleh Total Control saat target menjadi Total Control antara render dan submit (TC-GS-ROLE-297)

13. Sesi A: buka Detail "Manage hardware", klik Remove baris Fikri Ramadhan (dialog D-03 tampil)
14. Sesi B: assign Total Control ke Fikri Ramadhan
15. Sesi A: klik [Remove]
16. Sesi A: buka Tab Total Control dan Changelog Tab Total Control
17. Verifikasi Baris Fikri Ramadhan di Detail "Manage hardware" terhapus
18. Verifikasi Fikri Ramadhan tidak ada di Tab Total Control (auto-revert terhadap status saat submit)
19. Verifikasi Changelog Tab Total Control memuat entry Auto-Revert Total Control untuk Fikri Ramadhan dengan Modified By "Ahmad F"

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin Remove Baris Detail: Penolakan 403, Idempotent 200, dan Auto-Revert Target Menjadi TC".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Edit CRUD / Remove Role Assignment D6 status TC/RO target berubah; global-settings/role/PRD/role.md ROLE-LOGIC-03; foundation/process/prd-process/error-handling-convention.md §2; global-settings/role/PRD/role.md §9.2 [F-ROLE-07] Idempotent; global-settings/role/PRD/role.md §9.4.2 D6; global-settings/role/PRD/role.md ROLE-LOGIC-04.
- Sumber pemetaan test case granular: TC-GS-ROLE-274, TC-GS-ROLE-276, TC-GS-ROLE-297.
