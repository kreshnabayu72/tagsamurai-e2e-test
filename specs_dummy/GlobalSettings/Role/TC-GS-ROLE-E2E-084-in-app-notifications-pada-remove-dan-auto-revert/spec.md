---
id: TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert
title: "Penerbitan Notifikasi In-App pada Kejadian Pencabutan Access Level, Auto-Revert, dan Bulk Remove"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-241
  - TC-GS-ROLE-242
  - TC-GS-ROLE-243
  - TC-GS-ROLE-244
  - TC-GS-ROLE-245
coverage:
  web: automated
---

# Penerbitan Notifikasi In-App pada Kejadian Pencabutan Access Level, Auto-Revert, dan Bulk Remove

## Prerequisites

- Dual context (Admin Ahmad Fauzi dan target user penerima notifikasi)
- Data Uji: Target user akun
- Setup Hook: dualContext: sessionAdmin, sessionUser
- Target login setelah aksi
- Siti Nurhaliza dan Rina Putri login setelah Bulk Remove

## Test Steps

### Notifikasi in-app ke target untuk Remove Total Control (TC-GS-ROLE-241)

1. Target membuka Overlay Notifikasi
2. Amati notifikasi terbaru
3. Verifikasi Title "Your Total Control access was removed"
4. Verifikasi Body "Ahmad Fauzi removed your Total Control access on [date]." dengan [date] sesuai tanggal aksi (template "[Admin Name] removed your Total Control access on [date]."); [Admin Name] = nama lengkap admin aktor
5. Verifikasi [date] tampil dalam format Date Format General Settings aktif (bukan format tetap)
6. Verifikasi Hanya tombol [Mark as Read], tanpa [Detail]

### Notifikasi in-app ke target untuk Remove Read Only (TC-GS-ROLE-242)

7. Target membuka Overlay Notifikasi
8. Amati notifikasi terbaru
9. Verifikasi Title "Your Read Only access was removed"
10. Verifikasi Body "Ahmad Fauzi removed your Read Only access on [date]." dengan [date] sesuai tanggal aksi (template "[Admin Name] removed your Read Only access on [date].")
11. Verifikasi Hanya tombol [Mark as Read], tanpa [Detail]

### Notifikasi in-app ke target untuk Auto-Revert Total Control (TC-GS-ROLE-243)

12. Target membuka Overlay Notifikasi
13. Amati notifikasi terbaru
14. Verifikasi Title "Your Total Control access was removed"
15. Verifikasi Body "Your Total Control access was automatically removed after Ahmad Fauzi changed your role permissions on [date]." dengan [date] sesuai tanggal aksi (template "Your Total Control access was automatically removed after [Admin Name] changed your role permissions on [date].")
16. Verifikasi Hanya tombol [Mark as Read], tanpa [Detail]

### Notifikasi in-app ke target untuk Auto-Revert Read Only (TC-GS-ROLE-244)

17. Target membuka Overlay Notifikasi
18. Amati notifikasi terbaru
19. Verifikasi Title "Your Read Only access was removed"
20. Verifikasi Body "Your Read Only access was automatically removed after Ahmad Fauzi changed your role permissions on [date]." dengan [date] sesuai tanggal aksi (template "Your Read Only access was automatically removed after [Admin Name] changed your role permissions on [date].")
21. Verifikasi Hanya tombol [Mark as Read], tanpa [Detail]

### Bulk Remove campuran mengirim notifikasi per target tier (TC-GS-ROLE-245)

22. Masing-masing membuka Overlay Notifikasi
23. Verifikasi Siti Nurhaliza: "Your Total Control access was removed" (auto-revert)
24. Verifikasi Rina Putri: "Your Read Only access was removed" (auto-revert)
25. Verifikasi Wawan Setiawan (regular) tidak menerima notifikasi

## Notes

- Memvalidasi alur skenario "Penerbitan Notifikasi In-App pada Kejadian Pencabutan Access Level, Auto-Revert, dan Bulk Remove".
- Aturan PRD terkait: global-settings/role/PRD/role.md §8.8; foundation/process/prd-process/prd-conventions.md §32; foundation/product/business-rules/notification-system.md §3; global-settings/role/PRD/role.md §9.7.
- Sumber pemetaan test case granular: TC-GS-ROLE-241, TC-GS-ROLE-242, TC-GS-ROLE-243, TC-GS-ROLE-244, TC-GS-ROLE-245.
