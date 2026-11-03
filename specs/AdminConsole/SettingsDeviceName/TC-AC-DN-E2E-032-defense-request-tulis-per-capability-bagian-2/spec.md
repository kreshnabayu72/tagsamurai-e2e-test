---
id: TC-AC-DN-E2E-032-defense-request-tulis-per-capability-bagian-2
title: "Defense-in-Depth: Request Tulis Ditolak untuk Update-Only dan Delete-Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-555
  - TC-AC-DN-556
  - TC-AC-DN-557
  - TC-AC-DN-558
coverage:
  web: automated
---

# Defense-in-Depth: Request Tulis Ditolak untuk Update-Only dan Delete-Only

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #5 | Update-Only (Manage device master data: Update + Read) | (tanpa nama di TC) | `manageDeviceU_automated_{namaCompany}@qwertysystem.net` | `akunUpdateOnly` | `Spectra.env.AC_DN_UPDATE_PASSWORD` | TC-AC-DN-555, TC-AC-DN-556 |
| #6 | Delete-Only (Manage device master data: Delete + Read) | (tanpa nama di TC) | `manageDeviceD_automated_{namaCompany}@qwertysystem.net` | `akunDeleteOnly` | `Spectra.env.AC_DN_DELETE_PASSWORD` | TC-AC-DN-557, TC-AC-DN-558 |
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | semua TC (pengamat List) |

- Env var password: `Spectra.env.AC_DN_DELETE_PASSWORD`, `Spectra.env.AC_DN_UPDATE_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_DELETE_PASSWORD`, `AC_DN_UPDATE_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan login API (password) tiap akun; token tidak dihitung sebagai sesi web (`suite.md`). Request langsung hanya mengasersi respons server (status); state data diamati lewat List pada sesi Total Control UI (hook `before`) dan fixture backend (bagian 8b butir 1).
- Penghapusan record milik spec dan pemulihan dilakukan fixture backend di hook `after`.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before`: `Cable Tester {runId}-032` (Category `Accessory`, Measurement `Unit`) dan `Door Antenna {runId}-032` (Category `Antenna`, Measurement `Unit`) sebagai target Edit dan Delete yang ditolak server; `Direct Create Test {runId}-032` adalah nama request Create yang ditolak. `Gate Antenna` (Pre-setup #16) hanya dibaca.

## Test Steps

### TC-AC-DN-555: Request Create oleh Update-Only ditolak server

1. Kirim request Create Device Name `Direct Create Test {runId}-032` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Update-Only
2. Verifikasi server menolak request dengan 403 Forbidden (error-handling-convention.md §2)
3. Verifikasi data Device Name tidak berubah
4. Buka halaman `Settings > Device > Device Name`
5. Ketik Search `Direct Create Test {runId}-032`, tekan Enter
6. Verifikasi hasil Search menampilkan empty state "No results found"
7. Verifikasi Device Name `Direct Create Test {runId}-032` tidak ada di List
8. Klik `(←)` pada kotak Search

### TC-AC-DN-556: Request Delete oleh Update-Only ditolak server

9. Kirim request Delete Device Name `Door Antenna {runId}-032` memakai klien HTTP dengan sesi akun Update-Only
10. Verifikasi server menolak request dengan 403 Forbidden (error-handling-convention.md §2)
11. Verifikasi data Device Name tidak berubah
12. Buka halaman `Settings > Device > Device Name`
13. Ketik Search `{runId}-032`, tekan Enter
14. Verifikasi Device Name `Door Antenna {runId}-032` tetap ada di List
15. Klik `(←)` pada kotak Search

### TC-AC-DN-557: Request Create oleh Delete-Only ditolak server

16. Kirim request Create Device Name `Direct Create Test {runId}-032` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Delete-Only
17. Verifikasi server menolak request dengan 403 Forbidden (error-handling-convention.md §2)
18. Verifikasi data Device Name tidak berubah
19. Buka halaman `Settings > Device > Device Name`
20. Ketik Search `Direct Create Test {runId}-032`, tekan Enter
21. Verifikasi hasil Search menampilkan empty state "No results found"
22. Verifikasi Device Name `Direct Create Test {runId}-032` tidak ada di List
23. Klik `(←)` pada kotak Search

### TC-AC-DN-558: Request Edit oleh Delete-Only ditolak server

24. Kirim request Edit Device Name `Cable Tester {runId}-032` menjadi `Direct Edit Test {runId}-032` memakai klien HTTP dengan sesi akun Delete-Only
25. Verifikasi server menolak request dengan 403 Forbidden (error-handling-convention.md §2)
26. Verifikasi data Device Name tidak berubah
27. Buka halaman `Settings > Device > Device Name`
28. Ketik Search `{runId}-032`, tekan Enter
29. Verifikasi Device Name `Cable Tester {runId}-032` tetap bernama `Cable Tester {runId}-032`
30. Klik `(←)` pada kotak Search

## Notes

- Spec defense-in-depth (kelas a): request tulis langsung ke server oleh capability tanpa hak. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-DN-555, 556, 557, dan 558 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap FE+BE walau tumpang tindih dengan `tc-settings-device-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Penyimpangan data (S-06): target Edit dan Delete diganti record milik spec bersuffix; request ditolak sehingga record tidak berubah. Asersi absence Create memakai empty state Search "No results found" sebagai anchor positif (bagian 8b butir 2).
- Langkah penghubung (S-03): `Buka halaman` dan Search pada pengamatan List (R-16) serta mengosongkan Search lewat `(←)`.
- Pembagian TC lintas spec: TC-AC-DN-550 sampai 554 (Read Only dan Create-Only) ada di spec 031.
- Temuan untuk QA:
  - Post Condition tiap TC defense request tulis sama dengan butir Expected c; hanya Expected c yang diasersi (tidak ada Verifikasi ganda).
