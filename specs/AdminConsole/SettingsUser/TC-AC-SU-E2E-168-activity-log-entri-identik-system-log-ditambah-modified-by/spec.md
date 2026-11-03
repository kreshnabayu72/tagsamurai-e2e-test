---
id: TC-AC-SU-E2E-168-activity-log-entri-identik-system-log-ditambah-modified-by
title: "Activity Log Memuat Entri Identik Tab System Log Aktor untuk Tiap Kelas Object Ditambah Kolom Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-571
  - TC-AC-SU-642
coverage:
  web: automated
---

# Activity Log Memuat Entri Identik Tab System Log Aktor untuk Tiap Kelas Object Ditambah Kolom Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per kebutuhan state (nama berprefix `Mike Tan {runId}-168`, kecuali U0). Pelaku seluruh pemicu adalah Default User lewat sesi API aktor (login API password `Spectra.env.AC_DU_PASSWORD`, token tidak dihitung sebagai sesi web). Region A dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah.

| Kode | Name | State awal | Pemicu (sesi API Default User) |
|---|---|---|---|
| U0 | `John Doe {runId}-168` | Activated, Active | Deactivate (blok TC-571) |
| A | `Mike Tan {runId}-168A` | Activated, Inactive | Activate |
| B | `Mike Tan {runId}-168B` | Pending Activation, di luar cooldown Resend | Resend Activation Email |
| C | `Mike Tan {runId}-168C` | tanpa tier, "Manage group" OFF | Assign, Edit (Update), Remove "Manage group" |
| D | `Mike Tan {runId}-168D` | tanpa tier, "Manage partner" aktif di Region A | Assign Region B, Edit Create Region A, Remove Region B pada "Manage partner" |
| E | `Mike Tan {runId}-168E` | tanpa tier | Assign Total Control, edit role hingga menyimpang dan konfirmasi Remove (Auto-Revert), Assign Total Control, Remove Total Control |
| F | `Mike Tan {runId}-168F` | tanpa tier | Assign Read Only, edit role hingga menyimpang dan konfirmasi Remove (Auto-Revert), Assign Read Only, Remove Read Only |
| G | `Mike Tan {runId}-168G` | tanpa tier | Assign Group Manager Region A, edit CRUD hingga menyimpang dan konfirmasi Remove (Auto-Revert), Assign Group Manager Region A, Remove Group Manager Region A |

- Kemampuan teknis: Fixture BE (seeding user, tier, role, dan assignment); sesi API aktor Default User (kemampuan disediakan tim BE/FE tanpa endpoint karangan di spec); nama tampil akun Default User dari `Fixture.settingsUser.defaultUserActor.displayName` (disediakan tim FE; tidak tertulis di Pre-setup TC). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-571: Entri Deactivate di Activity Log
1. Jalankan pemicu U0 (Deactivate `John Doe {runId}-168`) lewat sesi API Default User hingga entri tersimpan
2. Klik menu Admin Console > Activity Log di sidebar, lalu ketik Search `John Doe {runId}-168`, tekan Enter
3. Verifikasi kolom tabel Activity Log berurutan: Date, Action, Object, Name, Field, Old Value, New Value, Modified By
4. Verifikasi baris Action `Deactivate`: Object `User`, Name `John Doe {runId}-168`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Default User`
### TC-AC-SU-642: Entri tiap kelas Object di Activity Log
5. Jalankan pemicu A sampai G (tabel Prerequisites) lewat sesi API Default User hingga seluruh entri tersimpan
6. Ketik Search `Mike Tan {runId}-168` pada Activity Log, tekan Enter
7. Verifikasi Object `User`: baris Activate untuk A, dan Resend Activation Email untuk B, dengan Modified By `Default User`
8. Verifikasi Object `Global Role`: baris Assign, Edit, dan Remove untuk C dengan Modified By `Default User`
9. Verifikasi Object `Group Role`: baris Assign, Edit, dan Remove untuk D dengan Modified By `Default User`
10. Verifikasi Object `Total Control`: baris Assign, Remove, dan Auto-Revert untuk E dengan Modified By aktor
11. Verifikasi Object `Read Only`: baris Assign, Remove, dan Auto-Revert untuk F dengan Modified By aktor
12. Verifikasi Object `Group Manager`: baris Assign, Remove, dan Auto-Revert untuk G dengan Modified By aktor
13. Buka Detail Default User (Search nama tampil Default User, klik Name baris), klik Tab System Log, lalu ketik Search `Mike Tan {runId}-168` pada tab, tekan Enter
14. Verifikasi Field, Old Value, dan New Value tiap baris Activity Log pada keenam kelas Object identik dengan baris yang sama di Tab System Log aktor

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemicu lewat sesi API (langkah 1 dan serupa; R-20), Search nama target di Activity Log dan Tab System Log (langkah 2, 6, 13, R-16; user bernama unik sehingga baseline entri nol), dan pembukaan Detail aktor.
- Kolom Modified By diasersi `Default User` sesuai Expected TC; format `[First Name] [Last Initial]` (R-14) tidak diterapkan karena TC menyebut nama aktor tanpa inisial.
- Temuan untuk QA:
  - TC-642 mengharapkan "Filter Name `Mike Tan`"; spec memakai Search nama berprefix karena target dibuat per State dengan nama bersuffix, dan keberadaan Search di Activity Log tidak ditegaskan TC.
  - TC-642 mensyaratkan aksi Default User untuk tiap kelas Object terhadap satu target `Mike Tan` tanpa menyebut Dependensi; spec men-seed pemicu lewat sesi API aktor dengan user terpisah per state (S-04).
  - TC-642 butir d sampai f menyebut "Modified By aktor" tanpa nama; spec memakai nama aktor (Default User) yang sama dengan butir a sampai c.
  - TC-642 butir g ("identik") tidak menyebut baris yang dibandingkan; spec membandingkan Field, Old Value, dan New Value tiap baris pada keenam kelas Object.
  - Nama tampil akun Default User tidak tertulis di Pre-setup TC (hanya email). TC memakai nama literal `John Doe` dan `Mike Tan`; spec memakai nama bersuffix (S-12).
