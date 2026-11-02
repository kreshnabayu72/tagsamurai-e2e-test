---
id: TC-AC-SU-E2E-163-modal-changelog-group-role-mencatat-aksi
title: "Modal Changelog User > Group Role Mencatat Assign, Edit, dan Remove per Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-557
  - TC-AC-SU-558
  - TC-AC-SU-559
coverage:
  web: automated
---

# Modal Changelog User > Group Role Mencatat Assign, Edit, dan Remove per Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (seeding murah, sehingga state tiap blok tidak bergantung pada blok lain). Region A dan Region B dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-163A` | `miketan+{runId}-163a@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A (TC-557) |
| U2 | `Mike Tan {runId}-163B` | `miketan+{runId}-163b@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A dengan Create Inactive (TC-558) |
| U3 | `Mike Tan {runId}-163C` | `miketan+{runId}-163c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A dan Region B (TC-559) |

- Kemampuan teknis: Fixture BE (seeding user, role, dan assignment). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-557: Assign per group
1. Ketik Search `Mike Tan {runId}-163A`, tekan Enter, klik Name baris U1, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
2. Catat jumlah baris Modal Changelog: User > Group Role sebagai N0, lalu tutup modal
3. Klik `[Assign Group]` pada baris "Manage partner", klik `[+ Assign Group]`, centang Region B, klik `[Select]`, lalu klik `[Save]`
4. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
5. Verifikasi baris teratas modal: Action `Assign`, Role Name — Group Name `Manage partner — Region B`, Field `Access`, Old Value `—`, New Value `Assigned`
6. Verifikasi jumlah baris modal bertambah tepat 1 dari N0 (1 baris per group yang berubah)
### TC-AC-SU-558: Edit per group
7. Tutup modal, klik menu Settings > User di sidebar, ketik Search `Mike Tan {runId}-163B`, tekan Enter, klik Name baris U2, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
8. Catat jumlah baris Modal Changelog: User > Group Role sebagai N1, lalu tutup modal
9. Klik `[Assign Group]` pada baris "Manage partner", centang Create pada baris Region A, lalu klik `[Save]`
10. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
11. Verifikasi baris teratas modal: Action `Edit`, Role Name — Group Name `Manage partner — Region A`, Field `Create`, Old Value `Inactive`, New Value `Active`
12. Verifikasi jumlah baris modal bertambah tepat 1 dari N1 (1 baris per group yang berubah)
### TC-AC-SU-559: Remove per group
13. Tutup modal, klik menu Settings > User di sidebar, ketik Search `Mike Tan {runId}-163C`, tekan Enter, klik Name baris U3, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
14. Catat jumlah baris Modal Changelog: User > Group Role sebagai N2, lalu tutup modal
15. Klik `[Assign Group]` pada baris "Manage partner", klik `[🗑]` pada baris Region B, lalu klik `[Save]`
16. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
17. Verifikasi baris teratas modal: Action `Remove`, Role Name — Group Name `Manage partner — Region B`, Field `Access`, Old Value `Assigned`, New Value `—`
18. Verifikasi jumlah baris modal bertambah tepat 1 dari N2 (1 baris per group yang berubah)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama user dan pembukaan Detail (langkah 1 dan langkah serupa, R-16), pencatatan jumlah baris awal N0, N1, dan N2 (langkah 2, 8, dan 14), serta menutup modal. Baris target adalah baris teratas (Newest First) karena aksi baru saja dilakukan (S-14).
- Tiga blok TC berpola sama pada satu aktor, masing-masing dengan user seed sendiri dan baseline jumlah baris sendiri; kegagalan satu blok tidak mengubah precondition blok lain; 18 langkah.
- Pembagian TC lintas spec: TC-560, TC-561, TC-562, dan TC-563 (cascade Total Control dan Read Only) ada di spec 209.
- Temuan untuk QA:
  - TC-557 sampai TC-559 butir b ("1 baris per group yang berubah") tidak menyebut baseline; spec mencatat jumlah baris sebelum aksi tiap blok.
  - Precondition TC-557 sampai TC-559 menyebut "Manage partner" aktif di Region A; TC-558 mengubah Create Region A (Old `Inactive`) dan TC-559 menghapus Region B tanpa menyebut bahwa Region B sudah di-assign. Spec memakai user seed per TC dengan state yang dibutuhkan Expected tiap TC.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
