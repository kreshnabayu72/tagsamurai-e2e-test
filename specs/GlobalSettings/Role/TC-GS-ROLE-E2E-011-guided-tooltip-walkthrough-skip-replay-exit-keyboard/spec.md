---
id: TC-GS-ROLE-E2E-011-guided-tooltip-walkthrough-skip-replay-exit-keyboard
title: "Guided Tooltip Walkthrough: Tombol Skip, Replay via [?], Pembatalan Exit Interruption, dan Navigasi Keyboard"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-29
  - TC-GS-ROLE-30
  - TC-GS-ROLE-31
coverage:
  web: automated
---

# Guided Tooltip Walkthrough: Tombol Skip, Replay via [?], Pembatalan Exit Interruption, dan Navigasi Keyboard

## Prerequisites

- Login sebagai Total Control
- Data Uji: User tour state
- Setup Hook: beforeEach: navigateTo(Role & Permission)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Flag guided tooltip belum diset

## Test Steps

### Guided tooltip Skip, Back, dan replay via [?] (TC-GS-ROLE-29)

1. Buka Role & Permission
2. Klik [Next] lalu [Back]
3. Klik [Skip]
4. Reload
5. Klik [?] di header
6. Verifikasi [Back] kembali ke Step 1
7. Verifikasi [Skip] menutup walkthrough
8. Verifikasi Setelah reload walkthrough tidak muncul otomatis
9. Verifikasi [?] memulai walkthrough dari Step 1

### Guided tooltip ditutup tanpa selesai saat navigasi keluar (TC-GS-ROLE-30)

10. Buka Role & Permission
11. Saat Step 2 tampil, klik menu sidebar User
12. Kembali ke Role & Permission
13. Verifikasi Walkthrough tertutup saat navigasi keluar
14. Verifikasi Saat kembali walkthrough muncul otomatis lagi dari Step 1

### Guided tooltip dapat dikendalikan dengan keyboard (TC-GS-ROLE-31)

15. Buka Role & Permission
16. Tekan Enter
17. Tekan ←
18. Tekan Esc
19. Verifikasi Enter ke Step 2
20. Verifikasi ← kembali ke Step 1
21. Verifikasi Esc menutup walkthrough (setara Skip)

## Notes

- Memvalidasi alur skenario "Guided Tooltip Walkthrough: Tombol Skip, Replay via [?], Pembatalan Exit Interruption, dan Navigasi Keyboard".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.7; foundation/functions/guided-tooltip.md.
- Sumber pemetaan test case granular: TC-GS-ROLE-29, TC-GS-ROLE-30, TC-GS-ROLE-31.
