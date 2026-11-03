---
id: TC-AC-SU-E2E-159-changelog-user-tier-read-only-dan-group-manager-dari-role-permission
title: "Popup Changelog User Mencatat Remove Read Only serta Assign dan Remove Group Manager yang Dipicu dari Settings > Role & Permission"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-544
  - TC-AC-SU-545
  - TC-AC-SU-650
coverage:
  web: automated
---

# Popup Changelog User Mencatat Remove Read Only serta Assign dan Remove Group Manager yang Dipicu dari Settings > Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (Region A dari Group Tree Pre-setup hanya menjadi target assignment Group Manager dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Budi Santoso {runId}-159A` | `budisantoso+{runId}-159a@qwertysystem.net` | Activated, bertier Read Only |
| U2 | `Dedi Kurnia {runId}-159B` | `dedikurnia+{runId}-159b@qwertysystem.net` | Activated, tanpa tier |
| U3 | `Dedi Kurnia {runId}-159C` | `dedikurnia+{runId}-159c@qwertysystem.net` | Activated, Group Manager di Region A |

- Kemampuan teknis: Fixture BE (seeding user, tier, dan Group Manager). Tanpa intercept, klien HTTP, dan jam server. Modified By yang diasersi adalah `Default User`.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-544: Remove Read Only dari Settings > Role & Permission
1. Klik menu Settings > Role & Permission di sidebar, lalu klik Tab Read Only
2. Remove U1 (`Budi Santoso {runId}-159A`) dari Read Only
3. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
4. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
5. Ketik Search `Budi Santoso {runId}-159A` pada Popup Changelog: User, tekan Enter
6. Verifikasi tepat 1 baris untuk U1: Action `Remove`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Default User`
7. Verifikasi tidak ada baris cascade dengan Action `Remove (via Total Control)` atau `Remove (via Read Only)` untuk U1
### TC-AC-SU-545: Assign Group Manager dari Settings > Role & Permission
8. Tutup Popup Changelog: User, klik menu Settings > Role & Permission di sidebar, lalu klik Tab Group Manager
9. Assign Group Manager Region A ke U2 (`Dedi Kurnia {runId}-159B`)
10. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
11. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
12. Ketik Search `Dedi Kurnia {runId}-159B` pada Popup Changelog: User, tekan Enter
13. Verifikasi tepat 1 baris untuk U2: Action `Assign`, Field `Group Manager — Region A`, Old Value `—`, New Value `Assigned`, Modified By `Default User`
14. Verifikasi Field memuat nama group `Region A` dan bukan `Access Level`
### TC-AC-SU-650: Remove Group Manager manual dari Settings > Role & Permission
15. Tutup Popup Changelog: User, klik menu Settings > Role & Permission di sidebar, lalu klik Tab Group Manager
16. Remove U3 (`Dedi Kurnia {runId}-159C`) dari Region A
17. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
18. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
19. Ketik Search `Dedi Kurnia {runId}-159C` pada Popup Changelog: User, tekan Enter
20. Verifikasi tepat 1 baris untuk U3: Action `Remove`, Field `Group Manager — Region A`, Old Value `Assigned`, New Value `—`, Modified By `Default User`
21. Verifikasi Action baris itu bukan `Remove (Group Deleted)` dan bukan `Auto-Revert`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar dan pindah tab, menutup popup, dan Search nama user di Popup Changelog: User (langkah 5, 12, 19, R-16); user bernama unik sehingga baseline entri nol dan "tepat 1 baris" menjadi asersi jumlah. Verifikasi tiadanya baris cascade pada TC-544 didahului Verifikasi baris Access Level pada Search yang sama (anchor, bagian 8b butir 2).
- Pemicu berada di Settings > Role & Permission (modul lain) oleh aktor yang sama; ketiga blok independen dan berpola sama, sehingga 21 langkah wajar. TC-650 ditempatkan di spec ini karena topiknya sama (pemicu manual dari Role & Permission).
- Temuan untuk QA:
  - Post Condition TC-544, TC-545, dan TC-650 (Tab System Log Default User dan Activity Log) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC tidak menyatakan Search tersedia di Popup Changelog: User; spec memakai Search nama user sebagai langkah penghubung.
  - TC memakai nama literal `Budi Santoso` dan `Dedi Kurnia` yang dipakai ulang dengan state berbeda; spec memakai user bersuffix per blok (S-12).
