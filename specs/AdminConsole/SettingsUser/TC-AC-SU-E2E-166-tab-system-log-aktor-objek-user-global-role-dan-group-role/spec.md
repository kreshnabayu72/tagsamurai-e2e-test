---
id: TC-AC-SU-E2E-166-tab-system-log-aktor-objek-user-global-role-dan-group-role
title: "Tab System Log Aktor Menampilkan Entri Object User, Global Role, dan Group Role dengan Name Target dan Isi Identik Popup Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-565
  - TC-AC-SU-566
  - TC-AC-SU-567
coverage:
  web: automated
---

# Tab System Log Aktor Menampilkan Entri Object User, Global Role, dan Group Role dengan Name Target dan Isi Identik Popup Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per kebutuhan state (nama berprefix `Mike Tan {runId}-166` agar satu Search menemukan seluruh target). Pelaku seluruh pemicu adalah Default User lewat sesi API aktor (login API password `Spectra.env.AC_DU_PASSWORD`, token tidak dihitung sebagai sesi web). Region A dan Region B dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah.

| Kode | Name | Email | State awal | Pemicu (sesi API Default User) |
|---|---|---|---|---|
| A | `Mike Tan {runId}-166A` | `miketan+{runId}-166a@qwertysystem.net` | Activated, Inactive | Activate |
| B | `Mike Tan {runId}-166B` | `miketan+{runId}-166b@qwertysystem.net` | Activated, Active | Deactivate |
| C | `Mike Tan {runId}-166C` | `miketan+{runId}-166c@qwertysystem.net` | Pending Activation, di luar cooldown Resend | Resend Activation Email |
| D | `Mike Tan {runId}-166D` | email pending `miketan+{runId}-166d@qwertysystem.net` | Pending Email Confirmation, di luar cooldown Resend | Resend Confirmation Email |
| E | `Mike Tan {runId}-166E` | `miketan+{runId}-166e@qwertysystem.net` | tanpa tier, "Manage group" OFF | Assign (switch ON), Edit (Update), Remove (switch OFF) "Manage group" |
| F | `Mike Tan {runId}-166F` | `miketan+{runId}-166f@qwertysystem.net` | tanpa tier, "Manage partner" aktif di Region A | Assign Region B, Edit Create Region A, Remove Region B pada "Manage partner" |

- Kemampuan teknis: Fixture BE (seeding user, role, dan assignment); sesi API aktor Default User (kemampuan disediakan tim BE/FE tanpa endpoint karangan di spec); nama tampil akun Default User dari `Fixture.settingsUser.defaultUserActor.displayName` (disediakan tim FE; tidak tertulis di Pre-setup TC). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-565: Object `User`
1. Jalankan pemicu A, B, C, dan D (tabel Prerequisites) lewat sesi API Default User hingga keempat entri tersimpan
2. Ketik Search nama tampil Default User, tekan Enter, klik Name baris Default User untuk membuka Detail, klik Tab System Log, lalu ketik Search `Mike Tan {runId}-166` pada tab, tekan Enter
3. Verifikasi baris Action `Activate`: Object `User`, Name `Mike Tan {runId}-166A`, Field `Status`, Old Value `Inactive`, New Value `Active`
4. Verifikasi baris Action `Deactivate`: Object `User`, Name `Mike Tan {runId}-166B`, Field `Status`, Old Value `Active`, New Value `Inactive`
5. Verifikasi baris Action `Resend Activation Email`: Object `User`, Name `Mike Tan {runId}-166C`, Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-166c@qwertysystem.net`
6. Verifikasi baris Action `Resend Confirmation Email`: Object `User`, Name `Mike Tan {runId}-166D`, Field `Confirmation Email`, Old Value `—`, New Value `miketan+{runId}-166d@qwertysystem.net`
7. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
8. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-166` pada Popup Changelog: User, tekan Enter
9. Verifikasi Popup Changelog: User memuat baris `Activate` untuk A dengan Field `Status`, Old Value `Inactive`, New Value `Active` (identik dengan Tab System Log)
10. Verifikasi Popup Changelog: User memuat baris `Deactivate` untuk B dengan Field `Status`, Old Value `Active`, New Value `Inactive` (identik dengan Tab System Log)
11. Verifikasi Popup Changelog: User memuat baris `Resend Activation Email` untuk C dengan Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-166c@qwertysystem.net` (identik dengan Tab System Log)
12. Verifikasi Popup Changelog: User memuat baris `Resend Confirmation Email` untuk D dengan Field `Confirmation Email`, Old Value `—`, New Value `miketan+{runId}-166d@qwertysystem.net` (identik dengan Tab System Log)
### TC-AC-SU-566: Object `Global Role`
13. Tutup popup, jalankan pemicu E (Assign, Edit, Remove "Manage group") lewat sesi API Default User hingga ketiga entri tersimpan
14. Buka Detail Default User (Search nama tampil Default User, klik Name baris), klik Tab System Log, lalu ketik Search `Mike Tan {runId}-166E` pada tab, tekan Enter
15. Verifikasi baris Action `Assign`: Object `Global Role`, Name `Mike Tan {runId}-166E`, Field `Manage group — Access`, Old Value `—`, New Value `Assigned`
16. Verifikasi baris Action `Edit`: Object `Global Role`, Name `Mike Tan {runId}-166E`, Field `Manage group — Update`, Old Value `Inactive`, New Value `Active`
17. Verifikasi baris Action `Remove`: Object `Global Role`, Name `Mike Tan {runId}-166E`, Field `Manage group — Access`, Old Value `Assigned`, New Value `—`
18. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
19. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-166E` pada Popup Changelog: User, tekan Enter
20. Verifikasi Popup Changelog: User memuat baris `Assign` dengan Field `Manage group — Access`, Old Value `—`, New Value `Assigned` (identik dengan Tab System Log)
21. Verifikasi Popup Changelog: User memuat baris `Edit` dengan Field `Manage group — Update`, Old Value `Inactive`, New Value `Active` (identik dengan Tab System Log)
22. Verifikasi Popup Changelog: User memuat baris `Remove` dengan Field `Manage group — Access`, Old Value `Assigned`, New Value `—` (identik dengan Tab System Log)
### TC-AC-SU-567: Object `Group Role`
23. Tutup popup, jalankan pemicu F (Assign Region B, Edit Create Region A, Remove Region B pada "Manage partner") lewat sesi API Default User hingga ketiga entri tersimpan
24. Buka Detail Default User (Search nama tampil Default User, klik Name baris), klik Tab System Log, lalu ketik Search `Mike Tan {runId}-166F` pada tab, tekan Enter
25. Verifikasi baris Action `Assign`: Object `Group Role`, Name `Mike Tan {runId}-166F`, Field `Manage partner — Region B — Access`, Old Value `—`, New Value `Assigned`
26. Verifikasi baris Action `Edit`: Object `Group Role`, Name `Mike Tan {runId}-166F`, Field `Manage partner — Region A — Create`, Old Value `Inactive`, New Value `Active`
27. Verifikasi baris Action `Remove`: Object `Group Role`, Name `Mike Tan {runId}-166F`, Field `Manage partner — Region B — Access`, Old Value `Assigned`, New Value `—`
28. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
29. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-166F` pada Popup Changelog: User, tekan Enter
30. Verifikasi Popup Changelog: User memuat baris `Assign` dengan Field `Manage partner — Region B — Access`, Old Value `—`, New Value `Assigned` (identik dengan Tab System Log)
31. Verifikasi Popup Changelog: User memuat baris `Edit` dengan Field `Manage partner — Region A — Create`, Old Value `Inactive`, New Value `Active` (identik dengan Tab System Log)
32. Verifikasi Popup Changelog: User memuat baris `Remove` dengan Field `Manage partner — Region B — Access`, Old Value `Assigned`, New Value `—` (identik dengan Tab System Log)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemicu lewat sesi API (langkah 1 dan serupa; R-20), pembukaan Detail aktor, Tab System Log, dan Search nama target (langkah 2 dan langkah serupa, R-16), menutup popup, serta Search nama target pada Popup Changelog: User (langkah 8 dan langkah serupa; user bernama unik sehingga baseline entri nol).
- Tiga blok TC berpola sama (pemicu, Tab System Log aktor, padanan Popup Changelog: User) untuk kelas Object berbeda; 32 langkah wajar karena tiap blok berdiri sendiri dengan user seeding sendiri.
- Temuan untuk QA:
  - Precondition TC-565 menyebut aktor telah menjalankan keempat Action terhadap satu target `Mike Tan`, padahal Activate, Deactivate, Resend Activation Email, dan Resend Confirmation Email butuh status awal berbeda; spec memakai empat user bernama berprefix sama.
  - TC-565 sampai TC-567 menyebut "Dependensi" tanpa mengisinya; spec men-seed pemicu lewat sesi API aktor (S-04).
  - Nilai Field/Old/New TC-565 sampai TC-567 tidak ditulis di TC; spec memakai nilai dari TC-531 sampai TC-540 (Changelog: User).
  - Nama tampil akun Default User tidak tertulis di Pre-setup TC (hanya email).
