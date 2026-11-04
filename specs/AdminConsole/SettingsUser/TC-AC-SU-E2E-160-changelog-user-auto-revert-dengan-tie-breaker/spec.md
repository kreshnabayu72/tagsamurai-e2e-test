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
- Akun aktor blok TC-547 dan TC-548: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Akun aktor blok TC-549: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login Default User di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; ganti akun ke Total Control dilakukan eksplisit pada langkah 30; hook `after` memulihkan sesi ke Default User.
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
9. Verifikasi tepat 2 baris untuk U1
10. Verifikasi Date kedua baris identik
11. Verifikasi Modified By kedua baris identik `Default U`
12. Verifikasi baris Auto-Revert: Field `Access Level`, Old Value `Total Control`, New Value `—`
13. Verifikasi baris Edit: Field `Manage group — Delete`
14. Verifikasi pada sort default Newest First, baris Auto-Revert tampil di atas baris Edit pemicunya
15. Verifikasi Modified By baris Auto-Revert bukan `by system`
### TC-AC-SU-548: Auto-Revert Read Only
16. Tutup Popup Changelog: User, ketik Search `Budi Santoso {runId}-160B`, tekan Enter
17. Klik Name baris U2 untuk membuka Detail
18. Klik Tab Role, lalu sub-tab Global Role
19. Centang Create pada "Manage group"
20. Klik `[Remove]` pada dialog Remove Read Only
21. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
22. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
23. Ketik Search `Budi Santoso {runId}-160B` pada Popup Changelog: User, tekan Enter
24. Verifikasi tepat 2 baris untuk U2
25. Verifikasi Date kedua baris identik
26. Verifikasi Modified By kedua baris identik `Default U`
27. Verifikasi baris Auto-Revert: Field `Access Level`, Old Value `Read Only`, New Value `—`
28. Verifikasi baris Edit: Field `Manage group — Create`
29. Verifikasi pada sort default Newest First, baris Auto-Revert tampil di atas baris Edit pemicunya
### TC-AC-SU-549: Auto-Revert Group Manager
30. Tutup Popup Changelog: User, lakukan Logout dari akun Default User
31. Login sebagai Total Control, lalu klik menu Settings > User di sidebar
32. Ketik Search `Dedi Kurnia {runId}-160C`, tekan Enter
33. Klik Name baris U3 untuk membuka Detail
34. Klik Tab Role, lalu sub-tab Group Role
35. Klik `[Assign Group]` pada baris "Manage distributor"
36. Uncheck Delete pada baris Region A, lalu klik `[Save]`
37. Klik `[Remove]` pada dialog Remove Group Manager
38. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
39. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
40. Ketik Search `Dedi Kurnia {runId}-160C` pada Popup Changelog: User, tekan Enter
41. Verifikasi baris Auto-Revert: Field `Group Manager — Region A`, Old Value `Assigned`, New Value `—`, Modified By nama aktor Total Control format singkat
42. Verifikasi baris Edit: Field `Manage distributor — Region A — Delete`, Old Value `Active`, New Value `Inactive`
43. Verifikasi Date baris Edit identik dengan baris Auto-Revert

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search dan pembukaan Detail (langkah 1, 16, 32, R-16), Search nama user di Popup Changelog: User (langkah 8, 23, 40) untuk menemukan baris target (user bernama unik, baseline entri nol), menutup popup, dan navigasi sidebar. Ganti akun eksplisit pada langkah 30 karena TC-549 mensyaratkan aktor Total Control sedangkan TC-547 dan TC-548 mensyaratkan Default User.
- Tiga blok independen dan berpola sama; 43 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC-547 sampai TC-549 (Tab System Log aktor dan Activity Log) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC tidak menyatakan Search tersedia di Popup Changelog: User; spec memakai Search nama user sebagai langkah penghubung.
  - TC memakai nama literal `Rina Putri`, `Budi Santoso`, `Dedi Kurnia`; spec memakai user bersuffix (S-12).
