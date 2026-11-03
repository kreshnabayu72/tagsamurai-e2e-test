---
id: TC-AC-DN-E2E-041-defense-request-baca-tulis-tanpa-capability
title: "Defense-in-Depth: Request Baca dan Tulis oleh Principal Tanpa Capability Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-545
  - TC-AC-DN-546
coverage:
  web: automated
---

# Defense-in-Depth: Request Baca dan Tulis oleh Principal Tanpa Capability Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #8 | Principal tanpa capability Manage device master data | (tanpa nama di TC) | `noCapabilityDevName_automated_{namaCompany}@qwertysystem.net` | `akunTanpaCapability` | `Spectra.env.AC_DN_NOCAP_PASSWORD` | TC-AC-DN-545, TC-AC-DN-546 |
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-546 (pengamat List) |

- Env var password: `Spectra.env.AC_DN_NOCAP_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_NOCAP_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan login API (password) tiap akun; token tidak dihitung sebagai sesi web (`suite.md`). Request langsung hanya mengasersi respons server (status); state data diamati lewat List pada sesi Total Control UI (hook `before`) dan fixture backend (bagian 8b butir 1).
- Penghapusan record milik spec dan pemulihan dilakukan fixture backend di hook `after`.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before`: `Cable Tester {runId}-041` (Category `Accessory`, Measurement `Unit`) dan `Door Antenna {runId}-041` (Category `Antenna`, Measurement `Unit`) sebagai target Edit dan Delete yang ditolak server; `Direct Create Test {runId}-041` adalah nama request Create yang ditolak. `Gate Antenna` (Pre-setup #16) hanya dibaca.

## Test Steps

### TC-AC-DN-545: Request baca oleh Principal tanpa capability ditolak server

1. Kirim request daftar Device Name memakai klien HTTP dengan sesi akun Principal tanpa capability Manage device master data
2. Verifikasi server menolak request daftar dengan 403 Forbidden (error-handling-convention.md §2)
3. Kirim request detail Device Name `Gate Antenna` dengan sesi akun Principal tanpa capability Manage device master data
4. Verifikasi server menolak request detail dengan 403 Forbidden (error-handling-convention.md §2)
5. Kirim request download daftar Device Name format CSV dengan sesi akun Principal tanpa capability Manage device master data
6. Verifikasi server menolak request download CSV dengan 403 Forbidden (error-handling-convention.md §2)
7. Kirim request daftar Changelog Device Name dengan sesi akun Principal tanpa capability Manage device master data
8. Verifikasi server menolak request Changelog dengan 403 Forbidden (error-handling-convention.md §2)
9. Verifikasi respons keempat request tidak memuat data Device Name
10. Verifikasi tidak ada data Device Name yang dikembalikan oleh keempat request

### TC-AC-DN-546: Request tulis oleh Principal tanpa capability ditolak server

11. Kirim request Create Device Name `Direct Create Test {runId}-041` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Principal tanpa capability Manage device master data
12. Verifikasi server menolak request Create dengan 403 Forbidden (error-handling-convention.md §2)
13. Kirim request Edit Device Name `Cable Tester {runId}-041` menjadi `Direct Edit Test {runId}-041` dengan sesi akun Principal tanpa capability Manage device master data
14. Verifikasi server menolak request Edit dengan 403 Forbidden (error-handling-convention.md §2)
15. Kirim request Delete Device Name `Door Antenna {runId}-041` dengan sesi akun Principal tanpa capability Manage device master data
16. Verifikasi server menolak request Delete dengan 403 Forbidden (error-handling-convention.md §2)
17. Verifikasi respons ketiga request tidak memuat data Device Name
18. Verifikasi data Device Name tidak berubah
19. Buka halaman `Settings > Device > Device Name`
20. Ketik Search `{runId}-041`, tekan Enter
21. Verifikasi Device Name `Cable Tester {runId}-041` tetap bernama `Cable Tester {runId}-041`
22. Verifikasi Device Name `Door Antenna {runId}-041` tetap ada
23. Verifikasi Device Name `Direct Create Test {runId}-041` tidak ada
24. Klik `(←)` pada kotak Search

## Notes

- Spec defense-in-depth (kelas a): request langsung ke server oleh Principal tanpa capability Manage device master data. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-DN-545 dan 546 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap FE+BE walau tumpang tindih dengan `tc-settings-device-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Penyimpangan data (S-06): target Edit dan Delete diganti record milik spec bersuffix; request ditolak sehingga record tidak berubah. Search `{runId}-041` pada pengamatan List mempersempit List ke record milik spec; baris `Cable Tester {runId}-041` dan `Door Antenna {runId}-041` menjadi anchor positif asersi absence.
- Langkah penghubung (S-03): `Buka halaman` dan Search pada pengamatan List (R-16) serta mengosongkan Search lewat `(←)`.
- Pembagian TC lintas spec: TC-AC-DN-543, 544, dan 655 (Client) ada di spec 030.
- Temuan untuk QA:
  - Expected b dan c pada TC baca bermakna sama; keduanya tetap diasersi terpisah.
  - Post Condition tiap TC defense request tulis sama dengan butir Expected c; hanya Expected c yang diasersi (tidak ada Verifikasi ganda).
