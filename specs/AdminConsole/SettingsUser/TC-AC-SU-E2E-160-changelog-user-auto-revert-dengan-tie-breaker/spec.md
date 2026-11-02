---
id: TC-AC-SU-E2E-160-changelog-user-auto-revert-dengan-tie-breaker
title: "Popup Changelog User Mencatat Pasangan Edit dan Auto-Revert Total Control, Read Only, dan Group Manager dengan Urutan Tie-Breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-547
  - TC-AC-SU-548
  - TC-AC-SU-549
coverage:
  web: automated
---

# Popup Changelog User Mencatat Pasangan Edit dan Auto-Revert Total Control, Read Only, dan Group Manager dengan Urutan Tie-Breaker

## Prerequisites

- Mode: FE+BE.
- Akun aktor blok TC-547 dan TC-548: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Akun aktor blok TC-549: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login Default User di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; ganti akun ke Total Control dilakukan eksplisit pada langkah 26; hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Rina Putri {runId}-160A` | `rinaputri+{runId}-160a@qwertysystem.net` | Activated, bertier Total Control |
| U2 | `Budi Santoso {runId}-160B` | `budisantoso+{runId}-160b@qwertysystem.net` | Activated, bertier Read Only |
| U3 | `Dedi Kurnia {runId}-160C` | `dedikurnia+{runId}-160c@qwertysystem.net` | Activated, Group Manager di Region A dengan full CRUD pada "Manage distributor" (Region A dari Group Tree Pre-setup, tidak diubah) |

- Kemampuan teknis: Fixture BE (seeding user, tier, dan Group Manager). Modified By aktor Total Control (blok TC-549) dibaca dari `Fixture.settingsUser.totalControlActor.modifiedBy` (disediakan tim FE). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-547: Auto-Revert Total Control
1. Ketik Search `Rina Putri {runId}-160A`, tekan Enter
2. Klik Name baris U1 untuk membuka Detail
3. Klik Tab Role, lalu sub-tab Global Role
4. Uncheck Delete pada "Manage group"
5. Klik `[Remove]` pada dialog Remove Total Control
6. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
7. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
8. Ketik Search `Rina Putri {runId}-160A` pada Popup Changelog: User, tekan Enter
9. Verifikasi tepat 2 baris untuk U1 dengan Date dan Modified By `Default User` identik
10. Verifikasi baris Auto-Revert: Field `Access Level`, Old Value `Total Control`, New Value `—`
11. Verifikasi baris Edit: Field `Manage group — Delete`
12. Verifikasi pada sort default Newest First, baris Auto-Revert tampil di atas baris Edit pemicunya
13. Verifikasi Modified By baris Auto-Revert bukan `by system`
### TC-AC-SU-548: Auto-Revert Read Only
14. Tutup Popup Changelog: User, ketik Search `Budi Santoso {runId}-160B`, tekan Enter
15. Klik Name baris U2 untuk membuka Detail
16. Klik Tab Role, lalu sub-tab Global Role
17. Centang Create pada "Manage group"
18. Klik `[Remove]` pada dialog Remove Read Only
19. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
20. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
21. Ketik Search `Budi Santoso {runId}-160B` pada Popup Changelog: User, tekan Enter
22. Verifikasi tepat 2 baris untuk U2 dengan Date dan Modified By `Default User` identik
23. Verifikasi baris Auto-Revert: Field `Access Level`, Old Value `Read Only`, New Value `—`
24. Verifikasi baris Edit: Field `Manage group — Create`
25. Verifikasi pada sort default Newest First, baris Auto-Revert tampil di atas baris Edit pemicunya
### TC-AC-SU-549: Auto-Revert Group Manager
26. Tutup Popup Changelog: User, lakukan Logout dari akun Default User
27. Login sebagai Total Control, lalu klik menu Settings > User di sidebar
28. Ketik Search `Dedi Kurnia {runId}-160C`, tekan Enter
29. Klik Name baris U3 untuk membuka Detail
30. Klik Tab Role, lalu sub-tab Group Role
31. Klik `[Assign Group]` pada baris "Manage distributor"
32. Uncheck Delete pada baris Region A, lalu klik `[Save]`
33. Klik `[Remove]` pada dialog Remove Group Manager
34. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
35. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
36. Ketik Search `Dedi Kurnia {runId}-160C` pada Popup Changelog: User, tekan Enter
37. Verifikasi baris Auto-Revert: Field `Group Manager — Region A`, Old Value `Assigned`, New Value `—`, Modified By nama aktor Total Control format singkat
38. Verifikasi baris Edit: Field `Manage distributor — Region A — Delete`, Old Value `Active`, New Value `Inactive`, dengan Date identik dengan baris Auto-Revert

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search dan pembukaan Detail (langkah 1, 14, 28, R-16), Search nama user di Popup Changelog: User (langkah 8, 21, 36) untuk menemukan baris target (user bernama unik, baseline entri nol), menutup popup, dan navigasi sidebar. Ganti akun eksplisit pada langkah 26 karena TC-549 mensyaratkan aktor Total Control sedangkan TC-547 dan TC-548 mensyaratkan Default User.
- Tiga blok independen dan berpola sama; 38 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC-547 sampai TC-549 (Tab System Log aktor dan Activity Log) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC tidak menyatakan Search tersedia di Popup Changelog: User; spec memakai Search nama user sebagai langkah penghubung.
  - TC memakai nama literal `Rina Putri`, `Budi Santoso`, `Dedi Kurnia`; spec memakai user bersuffix (S-12).
