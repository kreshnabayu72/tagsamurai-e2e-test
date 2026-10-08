---
id: TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path
title: "Pencabutan Massal User Regular Berhasil: Dialog D-05, Pembatalan Cancel, dan Eksekusi oleh Aktor MUR"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-126
  - TC-GS-ROLE-127
  - TC-GS-ROLE-128
  - TC-GS-ROLE-132
coverage:
  web: automated
---

# Pencabutan Massal User Regular Berhasil: Dialog D-05, Pembatalan Cancel, dan Eksekusi oleh Aktor MUR

## Prerequisites

- Login sebagai Total Control lalu Hendra Wijaya
- Data Uji: Wawan Setiawan & Nina Kartika (Dinamis #5)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Nina Kartika dan Agus Salim punya baris Manage hardware, tanpa access level
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"

## Test Steps

### Screening dialog Bulk Remove tanpa baris Total Control/Read Only (TC-GS-ROLE-126)

1. Centang Nina Kartika dan Agus Salim
2. Klik Bulk Action > Remove
3. Screening dialog
4. Verifikasi Overlay Bulk Action berisi `Remove` (DeleteBin6Line, danger)
5. Verifikasi Title "Remove Access"
6. Verifikasi Body "• Nina Kartika", "• Agus Salim" + "Are you sure you want to remove them? This action cannot be undone."
7. Verifikasi Tombol `[Cancel]` | `[Remove]` (danger)

### Cancel dialog Bulk Remove mempertahankan seleksi (TC-GS-ROLE-127)

8. Centang Nina Kartika dan Agus Salim
9. Klik Bulk Action > Remove
10. Klik [Cancel]
11. Verifikasi Tidak ada baris terhapus, tidak ada toast
12. Verifikasi Kedua baris tetap tercentang dan Bulk Action Bar tetap tampil

### Bulk Remove baris regular (TC-GS-ROLE-128)

13. Centang Nina Kartika dan Agus Salim
14. Klik Bulk Action > Remove
15. Klik [Remove]
16. Buka Tab System
17. Verifikasi Muncul toast sukses: "Success, user has been removed."
18. Verifikasi Kedua baris hilang; Bulk Action Bar tertutup
19. Verifikasi Users "Manage hardware" berkurang 2

### Bulk Remove oleh aktor Manage user and role dengan Update (TC-GS-ROLE-132)

20. Centang Wawan Setiawan dan Nina Kartika
21. Klik Bulk Action > Remove > [Remove]
22. Verifikasi Dialog varian tanpa baris TC/RO
23. Verifikasi Toast sukses: "Success, user has been removed."

## Notes

- Memvalidasi alur skenario "Pencabutan Massal User Regular Berhasil: Dialog D-05, Pembatalan Cancel, dan Eksekusi oleh Aktor MUR".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-05; global-settings/role/PRD/role.md §9.2 [F-ROLE-07] Bulk; global-settings/role/PRD/role.md §7.1 T-10; global-settings/role/PRD/role.md §4.8 Bulk.
- Sumber pemetaan test case granular: TC-GS-ROLE-126, TC-GS-ROLE-127, TC-GS-ROLE-128, TC-GS-ROLE-132.
