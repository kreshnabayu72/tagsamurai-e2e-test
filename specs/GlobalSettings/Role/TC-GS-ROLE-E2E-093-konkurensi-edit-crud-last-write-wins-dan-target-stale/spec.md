---
id: TC-GS-ROLE-E2E-093-konkurensi-edit-crud-last-write-wins-dan-target-stale
title: "Konkurensi Antar-Admin pada Edit CRUD: Mekanisme Last-Write-Wins, Penolakan 403, dan 404 Netral"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-272
  - TC-GS-ROLE-273
  - TC-GS-ROLE-284
coverage:
  web: automated
---

# Konkurensi Antar-Admin pada Edit CRUD: Mekanisme Last-Write-Wins, Penolakan 403, dan 404 Netral

## Prerequisites

- Dual session context (Sesi A dan Sesi B)
- Data Uji: Doni Pratama, Wawan Setiawan
- Setup Hook: dualContext: sessionA, sessionB
- Dua admin login (sesi A dan sesi B)
- Dua admin Total Control (sesi A, B)

## Test Steps

### Edit CRUD pada nilai baris yang sudah diubah admin lain sejak render — last-write-wins (TC-GS-ROLE-272)

1. Sesi A dan B membuka Detail "Manage TAG"
2. Sesi B: centang Update Doni Pratama
3. Sesi A (tanpa reload): centang Update Doni Pratama
4. Verifikasi Tidak ada dialog konflik
5. Verifikasi Sesi A: toast sukses "Success, permissions have been updated."
6. Verifikasi Checkbox Update Doni Pratama tetap checked (nilai akhir = Save terakhir yang diterima server)

### Edit CRUD target yang status Total Control-nya berubah sejak render (aktor non-Total Control) (TC-GS-ROLE-273)

7. Sesi A (Manage user and role Update) membuka Detail "Manage TAG"
8. Sesi B (Total Control): assign Total Control ke Wawan Setiawan
9. Sesi A: centang Update baris Wawan Setiawan
10. Verifikasi Muncul toast error: "You don't have permission to do this."
11. Verifikasi Perubahan sesi A tidak tersimpan dan tidak ada dialog konflik
12. Verifikasi UI di-refresh: checkbox Update baris Wawan Setiawan disabled; tooltip "You don't have permission to edit."

### Edit CRUD pada baris yang sudah dihapus admin lain (TC-GS-ROLE-284)

13. Sesi A dan B membuka Detail "Manage TAG"
14. Sesi B: Remove baris Wawan Setiawan
15. Sesi A (tanpa reload): centang Update baris Wawan Setiawan
16. Verifikasi Muncul toast netral: "This permission is no longer available."
17. Verifikasi Detail di-refresh, baris Wawan Setiawan tidak ada
18. Verifikasi Tidak ada dialog dan tidak ada toast sukses

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin pada Edit CRUD: Mekanisme Last-Write-Wins, Penolakan 403, dan 404 Netral".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Edit CRUD / Remove Role Assignment / Remove access level D6 nilai baris diubah admin lain (last-write-wins); global-settings/role/PRD/role.md §9.6; foundation/process/prd-process/error-handling-convention.md §5.7; global-settings/role/PRD/role.md §9.4.2 Edit CRUD / Remove Role Assignment D6 status TC/RO target berubah; global-settings/role/PRD/role.md ROLE-LOGIC-03; foundation/process/prd-process/error-handling-convention.md §2; global-settings/role/PRD/role.md §9.4.2 Edit CRUD / Remove access level D6 baris sudah dihapus admin lain; global-settings/role/PRD/role.md §4.4 Target sudah tidak tersedia (404).
- Sumber pemetaan test case granular: TC-GS-ROLE-272, TC-GS-ROLE-273, TC-GS-ROLE-284.
