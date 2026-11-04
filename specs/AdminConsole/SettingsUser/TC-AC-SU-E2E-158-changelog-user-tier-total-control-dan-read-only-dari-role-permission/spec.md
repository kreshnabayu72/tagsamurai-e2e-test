---
id: TC-AC-SU-E2E-158-changelog-user-tier-total-control-dan-read-only-dari-role-permission
title: "Popup Changelog User Mencatat Assign dan Remove Total Control serta Assign Read Only yang Dipicu dari Settings > Role & Permission"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-541
  - TC-AC-SU-542
  - TC-AC-SU-543
coverage:
  web: automated
---

# Popup Changelog User Mencatat Assign dan Remove Total Control serta Assign Read Only yang Dipicu dari Settings > Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Rina Putri {runId}-158A` | `rinaputri+{runId}-158a@qwertysystem.net` | Activated, tanpa tier |
| U2 | `Rina Putri {runId}-158B` | `rinaputri+{runId}-158b@qwertysystem.net` | Activated, bertier Total Control (dibutuhkan agar Remove Total Control bermakna, lihat Temuan untuk QA) |
| U3 | `Budi Santoso {runId}-158C` | `budisantoso+{runId}-158c@qwertysystem.net` | Activated, tanpa tier |

- Kemampuan teknis: Fixture BE (seeding user dan tier). Tanpa intercept, klien HTTP, dan jam server. Modified By yang diasersi adalah `Default U` (format `[First Name] [Last Initial]` dari nama tampil akun aktor Default User, seperti tertulis di Expected TC).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-541: Assign Total Control dari Settings > Role & Permission
1. Klik menu Settings > Role & Permission di sidebar, lalu klik Tab Total Control
2. Assign U1 (`Rina Putri {runId}-158A`) ke Total Control
3. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
4. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
5. Ketik Search `Rina Putri {runId}-158A` pada Popup Changelog: User, tekan Enter
6. Verifikasi tepat 1 baris untuk U1: Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Default U`
7. Verifikasi tidak ada baris cascade dengan Action `Assign (via Total Control)` atau `Assign (via Read Only)` untuk U1
### TC-AC-SU-542: Remove Total Control dari Settings > Role & Permission
8. Tutup Popup Changelog: User, klik menu Settings > Role & Permission di sidebar, lalu klik Tab Total Control
9. Remove U2 (`Rina Putri {runId}-158B`) dari Total Control
10. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
11. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
12. Ketik Search `Rina Putri {runId}-158B` pada Popup Changelog: User, tekan Enter
13. Verifikasi tepat 1 baris untuk U2: Action `Remove`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Default U`
14. Verifikasi tidak ada baris cascade dengan Action `Remove (via Total Control)` atau `Remove (via Read Only)` untuk U2
### TC-AC-SU-543: Assign Read Only dari Settings > Role & Permission
15. Tutup Popup Changelog: User, klik menu Settings > Role & Permission di sidebar, lalu klik Tab Read Only
16. Assign U3 (`Budi Santoso {runId}-158C`) ke Read Only
17. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
18. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
19. Ketik Search `Budi Santoso {runId}-158C` pada Popup Changelog: User, tekan Enter
20. Verifikasi tepat 1 baris untuk U3: Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Default U`
21. Verifikasi tidak ada baris cascade dengan Action `Assign (via Total Control)` atau `Assign (via Read Only)` untuk U3

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar dan pindah tab, menutup popup, dan Search nama user di Popup Changelog: User (langkah 5, 12, 19, R-16) untuk menemukan baris target; user bernama unik sehingga baseline entri nol dan "tepat 1 baris" menjadi asersi jumlah (bukan absence kelas g). Verifikasi tiadanya baris cascade didahului Verifikasi baris Access Level yang tampil pada Search yang sama (anchor, bagian 8b butir 2).
- Pemicu berada di Settings > Role & Permission (modul lain) oleh aktor yang sama; ketiga blok TC independen dan berpola sama, sehingga 21 langkah wajar.
- Temuan untuk QA:
  - TC-542 menulis precondition "Target user tersedia tanpa tier" tetapi aksinya Remove Total Control; spec men-seed U2 bertier Total Control agar Expected `Old Value Total Control` terpenuhi.
  - Post Condition TC-541 sampai TC-543 (Tab System Log Default User dan Activity Log) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC tidak menyatakan Search tersedia di Popup Changelog: User (langkah 3 TC hanya "klik icon Changelog"); spec memakai Search nama user sebagai langkah penghubung.
  - TC memakai nama literal `Rina Putri` dan `Budi Santoso` yang dipakai ulang antar TC dengan state berbeda; spec memakai user bersuffix per blok (S-12).
