---
id: TC-AC-SU-E2E-182-defense-in-depth-request-tulis-ditolak-server-isolasi-entitas-dan-proteksi-target
title: "Defense-in-Depth Request Langsung ke Server Ditolak untuk Isolasi Entitas, Mutasi Default User, Mutasi Role Diri Sendiri, Target Total Control, Group di Group Manager, dan Target Nonaktif Global Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-614
  - TC-AC-SU-615
  - TC-AC-SU-616
  - TC-AC-SU-617
  - TC-AC-SU-618
  - TC-AC-SU-619
coverage:
  web: automated
---

# Defense-in-Depth Request Langsung ke Server Ditolak untuk Isolasi Entitas, Mutasi Default User, Mutasi Role Diri Sendiri, Target Total Control, Group di Group Manager, dan Target Nonaktif Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun UI aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`, login di hook `before` spec ini hanya sebagai kondisi awal suite; tidak ada langkah yang memakai UI, seluruh langkah mengirim request langsung ke server atas nama aktor sesi API. Hook `after` memulihkan sesi ke akun default suite.
- Sesi API tiap aktor request (login API password; token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE):

| Blok | Aktor request | Akun | Password |
|---|---|---|---|
| TC-614 | Manage user and role (Update), entitas Distributor Nusantara | email tidak tertulis di Pre-setup TC (disediakan tim FE) | `Spectra.env.AC_DIST_MUR_PASSWORD` |
| TC-615 | Total Control | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-616, TC-617, TC-618 | Manage user and role (Update) | `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MUR_UPDATE_PASSWORD` |
| TC-619 | Total Control | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Data milik spec (target yang diuji ditolak server; kecuali target Pre-setup yang tidak dapat dimiliki spec dan hanya dibaca):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Jane Smith {runId}-182A` | `janesmith+{runId}-182a@qwertysystem.net` | Activated, Active, entitas Principal (TC-614, ID dibaca dari Fixture BE) |
| U2 | `Dewi Lestari {runId}-182B` | `dewilestari+{runId}-182b@qwertysystem.net` | Activated, Active, bertier Total Control (TC-617) |
| U3 | `Dedi Kurnia {runId}-182C` | `dedikurnia+{runId}-182c@qwertysystem.net` | Activated, Group Manager di Region A, "Manage distributor" full CRUD di Region A (TC-618; Region A dari Group Tree Pre-setup, tidak diubah) |
| U4 | `Jane Smith {runId}-182D` | `janesmith+{runId}-182d@qwertysystem.net` | Inactive di Admin Console dan nonaktif di Global Settings (TC-619) |
| Pre-setup | Default User Principal (#1), akun Manage user and role (Update) (#4) | - | hanya dibaca (state target ditolak, tidak diubah); tidak dapat dimiliki spec (TC-615, TC-616) |

- Kemampuan teknis (kelas a): klien HTTP yang mengirim request langsung ke server atas nama aktor tiap blok; pola request (path dan body) disediakan tim FE/BE tanpa endpoint karangan di spec; Fixture BE untuk membaca state data (status user, role, tier, assignment). Tanpa intercept dan tanpa jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-614: Isolasi entitas
1. Kirim request langsung untuk membaca detail user milik entitas Principal (U1, lewat ID dari Fixture BE) atas nama aktor Manage user and role (Update) Distributor Nusantara
2. Verifikasi respons server berupa penolakan (bukan 2xx)
3. Verifikasi respons tidak memuat data user U1 (nama dan email)
### TC-AC-SU-615: Mutasi Default User
4. Kirim request langsung untuk menonaktifkan Default User Principal atas nama aktor Total Control
5. Verifikasi respons server berupa penolakan (bukan 2xx)
6. Verifikasi Fixture BE: Default User tetap Active
### TC-AC-SU-616: Mutasi role diri sendiri
7. Kirim request langsung untuk mematikan role "Manage user and role" pada akun aktor sendiri atas nama aktor Manage user and role (Update)
8. Verifikasi respons server berupa penolakan (bukan 2xx)
9. Verifikasi Fixture BE: role "Manage user and role" akun aktor tetap aktif
### TC-AC-SU-617: Edit role target Total Control
10. Kirim request langsung untuk mengedit CRUD role U2 (`Dewi Lestari {runId}-182B`) atas nama aktor Manage user and role (Update)
11. Verifikasi respons server berupa penolakan (bukan 2xx)
12. Verifikasi Fixture BE: tier U2 tetap Total Control
### TC-AC-SU-618: Edit Group Role di group Group Manager target
13. Kirim request langsung untuk menyimpan assignment Region A pada "Manage distributor" milik U3 (`Dedi Kurnia {runId}-182C`) atas nama aktor Manage user and role (Update)
14. Verifikasi respons server berupa penolakan (bukan 2xx)
15. Verifikasi Fixture BE: assignment "Manage distributor" U3 di Region A tidak berubah dan status Group Manager U3 tetap
### TC-AC-SU-619: Perubahan status target nonaktif Global Settings
16. Kirim request langsung untuk mengaktifkan U4 (`Jane Smith {runId}-182D`) atas nama aktor Total Control
17. Verifikasi respons server berupa penolakan (bukan 2xx)
18. Verifikasi Fixture BE: status U4 tetap Inactive

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-user-backend.md`; tiap TC tepat satu spec, dan BE mencatatnya pada tingkat endpoint.
- Seluruh langkah adalah request langsung ke server (bagian 8b butir 1): asersi hanya respons server dan state data lewat Fixture BE. Toast, refresh UI, dan state kontrol yang disebut Expected TC (TC-614 `"You don't have permission to do this."`; TC-615 `"Default User cannot be modified."`; TC-616 `"You can't manage your own account from here."`; TC-617 dan TC-618 `"You don't have permission to edit."`; TC-619 `"This user is inactive in Global Settings. Contact a Global Settings admin to reactivate."`; kontrol edit Disabled; switch di-refresh) tidak diasersi di spec ini karena request tidak melewati browser; perilaku FE untuk respons yang sama diasersi di spec jalur UI.
- Asersi "tidak ada entri baru di Changelog: User" (TC-615 sampai TC-617) tidak ditulis di spec ini: asersi absence atas penolakan request langsung masuk spec absence (kelas g, S-05); TC-615, TC-616, dan TC-617 ada juga di `sourceTc` spec 207 yang memuat request langsung, baseline, dan asersi absence-nya (pembagian TC lintas spec, S-05: spec ini mengasersi respons server dan state data).
- Enam blok kelas a berpola sama (satu request, satu respons, satu state data) pada aktor berbeda lewat sesi API; 18 langkah wajar.
- Temuan untuk QA:
  - Expected TC-614 sampai TC-619 tidak menyebut status HTTP penolakan; spec mengasersi respons bukan 2xx. Kode status tepat (mis. 403 atau 422) perlu ditetapkan.
  - TC-615 dan TC-616 memakai target Pre-setup (Default User dan akun Manage user and role) yang tidak dapat dimiliki spec; targetnya hanya dibaca (S-06).
  - TC-614 menyebut "user milik Partner lain" tanpa menyebut entitas; spec memakai user entitas Principal bagi aktor Distributor Nusantara. Email akun aktor Distributor Nusantara selain Default User tidak tertulis di Pre-setup TC.
  - TC-617 sampai TC-619 menyebut hasil UI (kontrol Disabled, switch posisi terakhir) bersama request langsung; asersi UI tersebut perlu TC jalur UI tersendiri bila belum ada.
  - TC memakai nama literal (`Jane Smith`, `Dewi Lestari`, `Dedi Kurnia`); spec memakai nama bersuffix (S-12).
