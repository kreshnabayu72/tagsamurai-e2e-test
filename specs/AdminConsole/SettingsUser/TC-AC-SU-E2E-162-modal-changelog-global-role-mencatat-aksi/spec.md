---
id: TC-AC-SU-E2E-162-modal-changelog-global-role-mencatat-aksi
title: "Modal Changelog User > Global Role Mencatat Assign, Remove, dan Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-550
  - TC-AC-SU-551
  - TC-AC-SU-552
coverage:
  web: automated
---

# Modal Changelog User > Global Role Mencatat Assign, Remove, dan Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (seeding murah, sehingga state tiap blok tidak bergantung pada blok lain):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-162A` | `miketan+{runId}-162a@qwertysystem.net` | Activated, tanpa tier, "Manage group" belum aktif (TC-550) |
| U2 | `Mike Tan {runId}-162B` | `miketan+{runId}-162b@qwertysystem.net` | Activated, tanpa tier, "Manage group" aktif (TC-551) |
| U3 | `Mike Tan {runId}-162C` | `miketan+{runId}-162c@qwertysystem.net` | Activated, tanpa tier, "Manage group" aktif dengan Update Inactive (TC-552) |

- Kemampuan teknis: Fixture BE (seeding user dan role). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-550: Assign
1. Ketik Search `Mike Tan {runId}-162A`, tekan Enter, klik Name baris U1, klik Tab Role, lalu sub-tab Global Role
2. Switch "Manage group" OFF ke ON
3. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Global Role terbuka
4. Verifikasi baris teratas modal: Action `Assign`, Role Name `Manage group`, Field `Access`, Old Value `—`, New Value `Assigned`
5. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-162A` pada Popup Changelog: User, tekan Enter
6. Verifikasi baris teratas Popup Changelog: User padanan: Action `Assign`, Field `Manage group — Access`
### TC-AC-SU-551: Remove
7. Tutup popup, ketik Search `Mike Tan {runId}-162B`, tekan Enter, klik Name baris U2, klik Tab Role, lalu sub-tab Global Role
8. Switch "Manage group" ON ke OFF
9. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Global Role terbuka
10. Verifikasi baris teratas modal: Action `Remove`, Role Name `Manage group`, Field `Access`, Old Value `Assigned`, New Value `—`
11. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-162B` pada Popup Changelog: User, tekan Enter
12. Verifikasi baris teratas Popup Changelog: User padanan: Action `Remove`, Field `Manage group — Access`
### TC-AC-SU-552: Edit
13. Tutup popup, ketik Search `Mike Tan {runId}-162C`, tekan Enter, klik Name baris U3, klik Tab Role, lalu sub-tab Global Role
14. Centang Update pada "Manage group"
15. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Global Role terbuka
16. Verifikasi baris teratas modal: Action `Edit`, Role Name `Manage group`, Field `Update`, Old Value `Inactive`, New Value `Active`
17. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-162C` pada Popup Changelog: User, tekan Enter
18. Verifikasi baris teratas Popup Changelog: User padanan: Action `Edit`, Field `Manage group — Update`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama user dan pembukaan Detail (langkah 1 dan langkah serupa, R-16), Search nama user di Popup Changelog: User (langkah 5 dan langkah serupa; user bernama unik sehingga baseline entri nol), serta menutup modal dan popup.
- Tiga blok TC berpola sama (pemicu satu aksi, satu modal, satu padanan di Popup Changelog: User) pada satu aktor, masing-masing dengan user seed sendiri; kegagalan satu blok tidak mengubah precondition blok lain. Baris target selalu baris teratas (Newest First) karena aksi baru saja dilakukan (S-14); 18 langkah.
- Pembagian TC lintas spec: TC-553, TC-554, TC-555, dan TC-556 (cascade Total Control dan Read Only) ada di spec 208.
- Temuan untuk QA:
  - TC-550 sampai TC-552 butir b ("entri padanan") hanya menyebut Field; spec mengasersi Action dan Field.
  - Precondition TC-550 sampai TC-552 menyebut satu Mike Tan dengan "Manage group" belum aktif (untuk Assign) atau aktif (untuk lainnya); spec memakai satu user seed per TC sesuai precondition itu.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
