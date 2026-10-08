---
id: TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user
title: "Kaskade Pembersihan Hak Akses Role: Pencabutan Access GS, Penghapusan User, dan Retensi Status Inactive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-233
  - TC-GS-ROLE-234
  - TC-GS-ROLE-235
  - TC-GS-ROLE-236
  - TC-GS-ROLE-291
coverage:
  web: automated
---

# Kaskade Pembersihan Hak Akses Role: Pencabutan Access GS, Penghapusan User, dan Retensi Status Inactive

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pandu Wijaya (Dinamis #10), Dewi Lestari (Pre-setup #3)
- Setup Hook: beforeEach: executeCascadeAction()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Given Pandu Wijaya (Pre-setup #18) berstatus Total Control (di-assign oleh Ahmad Fauzi sebelum TC ini) dan memiliki Access "Global Settings"
- Given Agus Salim (baris Manage TAG, tanpa access level)
- Given Wawan Setiawan punya baris role
- Given Siti Nurhaliza (Total Control) dinonaktifkan
- Given Rahmat Hidayat di-assign Read Only kembali

## Test Steps

### Given Remove Access Global Settings di modul User untuk user Total Control (TC-GS-ROLE-233)

1. Lakukan Remove Access Global Settings Pandu Wijaya di User
2. Buka Role & Permission > Total Control
3. Buka Changelog Tab Total Control
4. Buka Tab System
5. Buka Global Settings > Activity Log
6. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
7. Verifikasi Pandu Wijaya hilang dari Tab Total Control dan dari semua Detail
8. Verifikasi Changelog: 1 entry Action "Remove", Field "Access Level", Old "Total Control", New "—", Modified By "Ahmad F"
9. Verifikasi Kolom Users keenam role berkurang 1
10. Verifikasi Pandu Wijaya tidak menerima notifikasi Role & Permission
11. Verifikasi Changelog Tab System tidak memuat entry Remove per-role untuk Pandu Wijaya
12. Verifikasi Activity Log memuat 1 entry Action "Remove", Object "Total Control", Name "Pandu Wijaya", Field "Access Level", Old "Total Control", New "—", Modified By "Ahmad F" dari modul Role & Permission, di samping entry Remove Access milik modul User
13. Verifikasi System Log Ahmad Fauzi (aktor) memuat 1 entry Action "Remove", Object "Total Control", Name "Pandu Wijaya", Field "Access Level", Old "Total Control", New "—" dari modul Role & Permission, di samping entry Remove Access milik modul User

### Given Remove Access Global Settings untuk user tanpa access level (TC-GS-ROLE-234)

14. Remove Access Global Settings Agus Salim di User
15. Buka Detail "Manage TAG" dan Changelog Tab System
16. Verifikasi Baris Agus Salim hilang
17. Verifikasi Changelog Role & Permission tidak memuat entry untuk kejadian ini

### Given user dihapus di modul User (TC-GS-ROLE-235)

18. Hapus Wawan Setiawan di User
19. Buka Detail role yang dipegangnya dan Tab System
20. Verifikasi Baris Wawan Setiawan hilang dari Detail
21. Verifikasi Users berkurang
22. Verifikasi Tidak ada entry baru di Changelog Role & Permission

### Given user dinonaktifkan di modul User (TC-GS-ROLE-236)

23. Nonaktifkan Siti Nurhaliza di User
24. Buka Tab Total Control
25. Buka Detail "Manage TAG", centang/edit tidak dilakukan; buka overlay (⋯) baris
26. Verifikasi Siti Nurhaliza tetap di Tab Total Control dengan Status "Inactive"
27. Verifikasi Baris role tetap ada dan Remove tetap enabled

### Given Remove Access Global Settings untuk user Read Only (TC-GS-ROLE-291)

28. Remove Access Global Settings Rahmat Hidayat di modul User
29. Buka Changelog Tab Read Only
30. Buka Global Settings > User > Ahmad Fauzi > Tab System Log dan Global Settings > Activity Log
31. Verifikasi Rahmat Hidayat hilang dari Tab Read Only dan dari semua Detail
32. Verifikasi Changelog Tab Read Only: 1 entry Action "Remove", Field "Access Level", Old "Read Only", New "—", Modified By "Ahmad F"
33. Verifikasi Activity Log memuat 1 entry Action "Remove", Object "Read Only", Name "Rahmat Hidayat", Field "Access Level", Old "Read Only", New "—", Modified By "Ahmad F" dari modul Role & Permission, di samping entry Remove Access milik modul User
34. Verifikasi System Log Ahmad Fauzi (aktor) memuat 1 entry Action "Remove", Object "Read Only", Name "Rahmat Hidayat", Field "Access Level", Old "Read Only", New "—" dari modul Role & Permission, di samping entry Remove Access milik modul User

## Notes

- Memvalidasi alur skenario "Kaskade Pembersihan Hak Akses Role: Pencabutan Access GS, Penghapusan User, dan Retensi Status Inactive".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.7; global-settings/role/PRD/role.md §8.7 Cascade; global-settings/role/PRD/role.md §8.6; global-settings/role/PRD/role.md §8.5; global-settings/role/PRD/role.md §8.8; foundation/functions/changelog-entry.md Aturan Terkunci #1; global-settings/role/PRD/role.md ROLE-LOGIC-06a.
- Sumber pemetaan test case granular: TC-GS-ROLE-233, TC-GS-ROLE-234, TC-GS-ROLE-235, TC-GS-ROLE-236, TC-GS-ROLE-291.
