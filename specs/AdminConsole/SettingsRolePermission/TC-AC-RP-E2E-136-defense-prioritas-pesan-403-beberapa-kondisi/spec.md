---
id: TC-AC-RP-E2E-136-defense-prioritas-pesan-403-beberapa-kondisi
title: "Defense-in-depth: Prioritas Pesan 403 saat Beberapa Kondisi Penolakan Berlaku Sekaligus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-418
coverage:
  web: automated
---

# Defense-in-depth: Prioritas Pesan 403 saat Beberapa Kondisi Penolakan Berlaku Sekaligus

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP, tanpa browser)
- Akun aktor (urutan eksekusi sesuai langkah TC-AC-RP-418; aktor pertama login di hook `before` spec ini, sisanya lewat langkah Ganti akun):

| Urutan | Aktor | Akun | Env password |
|---|---|---|---|
| 1 | `Dewi Anggraini` (Read Only Principal, Pre-setup #3) | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| 2 | `Yoga Pratama` (Total Control `Distributor Suspended`, Pre-setup #20) | `totalControlSuspRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_SUSP_TC_PASSWORD` |
| 3 | `Hendra Wijaya` (Manage user and role R+U Principal, Pre-setup #4) | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #2 dan #13 (`Bambang Hartono`, Default User sekaligus pemegang Total Control), #11 (tree group Principal; `Region A`), #14 (penugasan Group Manager), #15 (`Manage device master data`), #20 (entitas `Distributor Suspended` berstatus Suspended dengan Total Control `Yoga Pratama`; status Suspended dipakai sebagai kondisi penolakan, tidak diubah spec ini), dan #25 (klien HTTP). Target aksi adalah data Pre-setup bernama literal sesuai TC; tidak ada Data Dinamis bersuffix `+{runId}-136` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung (Pre-setup #25); sesi API aktor (dinyatakan di `suite.md`) untuk ketiga akun, termasuk akun entitas `Distributor Suspended`; kemampuan membaca state data lewat fixture BE (peran individual `Bambang Hartono`, data Default User entitas `Distributor Suspended`, penugasan Group Manager `Bambang Hartono`).
- Pemulihan baseline: seluruh request ditolak sehingga data Pre-setup tidak diubah; kemampuan reset data Pre-setup yang disediakan tim FE/BE (dinyatakan di `suite.md`) dijalankan di hook `before` dan `after` spec ini sebagai jaring pengaman. Last Updated dan Modified By data Pre-setup tidak berubah.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_RP_RO_PASSWORD`, `AC_RP_SUSP_TC_PASSWORD`, dan `AC_RP_MUR_U_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Catat lewat fixture BE sebagai baseline: peran individual `Bambang Hartono` pada `Manage device master data`, data Default User entitas `Distributor Suspended`, dan penugasan Group Manager `Bambang Hartono`

### TC-AC-RP-418: Prioritas pesan 403

2. Sesi API `Dewi Anggraini`: kirim request Edit CRUD Create=true untuk `Bambang Hartono` (Default User) pada `Manage device master data`
3. Verifikasi respons request ditolak dengan status 403
4. Verifikasi pesan respons "You don't have permission to do this."
5. Verifikasi pesan respons bukan "Default User cannot be modified."
6. Verifikasi pesan respons bukan "Read Only access cannot modify data."
7. Ganti akun: login sesi API sebagai `Yoga Pratama` (`Spectra.env.AC_RP_SUSP_TC_PASSWORD`)
8. Sesi API `Yoga Pratama`: kirim request Edit CRUD untuk Default User entitas `Distributor Suspended`
9. Verifikasi respons request ditolak dengan status 403
10. Verifikasi pesan respons "Changes can't be saved while this workspace is suspended or expired."
11. Verifikasi pesan respons bukan "Default User cannot be modified."
12. Ganti akun: login sesi API sebagai `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
13. Sesi API `Hendra Wijaya`: kirim request Assign GM untuk `Bambang Hartono` (Default User) di `Region A`
14. Verifikasi respons request ditolak dengan status 403
15. Verifikasi pesan respons "Only Default User or Total Control can assign Group Manager."
16. Verifikasi pesan respons bukan "You don't have permission to do this."
17. Verifikasi pesan respons bukan "Default User cannot be modified."
18. Verifikasi lewat fixture BE bahwa peran individual `Bambang Hartono`, data Default User entitas `Distributor Suspended`, dan penugasan Group Manager `Bambang Hartono` sama dengan baseline langkah 1

## Notes

- K-1: TC-AC-RP-418 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap berada di spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec, walau isinya tumpang tindih dengan `tc-settings-role-permission-backend.md`; BE mencatatnya pada tingkat endpoint.
- Asersi hanya status respons, pesan respons, dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (S-03, S-07): langkah 1 (baseline state), langkah 7 dan 12 (Ganti akun sesi API; TC mensyaratkan tiga akun berurutan dalam satu TC). Sesi aktor `Yoga Pratama` adalah akun entitas `Distributor Suspended` yang dipakai sebagai kondisi penolakan (kelas h) dan bukan objek uji; objek uji adalah urutan prioritas pesan (P-5 butir b: satu TC objek-uji ringan).
- Temuan untuk QA:
  - TC-AC-RP-418: Expected request sesi `Yoga Pratama` menyebut "toast" "Changes can't be saved while this workspace is suspended or expired." untuk request langsung; sesuai bagian 8b butir 1, spec mengasersi teks itu sebagai pesan respons server, bukan toast UI.
  - TC-AC-RP-418: Default User entitas `Distributor Suspended` tidak diidentifikasi (nama atau email) di Pre-setup #20; spec menulis "Default User entitas `Distributor Suspended`" apa adanya (S-11, S-13).
  - TC-AC-RP-418: Expected request sesi `Dewi Anggraini` dan `Hendra Wijaya` memuat "(bukan ... dan bukan ...)"; spec memecahnya satu `Verifikasi` per negasi (S-01); tiap negasi didahului pesan persis yang diharapkan sebagai anchor.
  - TC-AC-RP-418 tidak menyebut endpoint, method, atau body request; spec menulis aksi seperti di TC tanpa mengarang endpoint (S-13).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
