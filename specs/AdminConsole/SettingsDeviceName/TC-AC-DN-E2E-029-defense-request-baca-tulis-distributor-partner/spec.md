---
id: TC-AC-DN-E2E-029-defense-request-baca-tulis-distributor-partner
title: "Defense-in-Depth: Request Baca dan Tulis oleh Distributor dan Partner Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-539
  - TC-AC-DN-540
  - TC-AC-DN-541
  - TC-AC-DN-542
  - TC-AC-DN-627
coverage:
  web: automated
---

# Defense-in-Depth: Request Baca dan Tulis oleh Distributor dan Partner Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #9 | Total Control pada entitas Distributor `Distributor Jaringan` | (tanpa nama di TC) | `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `akunDistributor` | `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD` | TC-AC-DN-539, TC-AC-DN-540 |
| #10 | Total Control pada entitas Partner `Partner Jaringan` | (tanpa nama di TC) | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `akunPartner` | `Spectra.env.AC_DN_PARTNER_PASSWORD` | TC-AC-DN-541, TC-AC-DN-542, TC-AC-DN-627 |
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-540, TC-AC-DN-542 (pengamat List) |

- Env var password: `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD`, `Spectra.env.AC_DN_PARTNER_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_DISTRIBUTOR_PASSWORD`, `AC_DN_PARTNER_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan login API (password) tiap akun; token tidak dihitung sebagai sesi web (`suite.md`). Request langsung hanya mengasersi respons server (status); state data diamati lewat List pada sesi Total Control UI (hook `before`) dan fixture backend (bagian 8b butir 1).
- Penghapusan record milik spec dan pemulihan dilakukan fixture backend di hook `after`.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before`: `Cable Tester {runId}-029` (Category `Accessory`, Measurement `Unit`) dan `Door Antenna {runId}-029` (Category `Antenna`, Measurement `Unit`) sebagai target Edit dan Delete yang ditolak server; `Direct Create Test {runId}-029` adalah nama request Create yang ditolak. `Gate Antenna` (Pre-setup #16) hanya dibaca.

## Test Steps

### TC-AC-DN-539: Request baca oleh Distributor ditolak server

1. Kirim request daftar Device Name memakai klien HTTP dengan sesi akun Distributor Jaringan
2. Verifikasi server menolak request daftar dengan 403 Forbidden (error-handling-convention.md §2)
3. Kirim request detail Device Name `Gate Antenna` dengan sesi akun Distributor Jaringan
4. Verifikasi server menolak request detail dengan 403 Forbidden (error-handling-convention.md §2)
5. Kirim request download daftar Device Name format CSV dengan sesi akun Distributor Jaringan
6. Verifikasi server menolak request download CSV dengan 403 Forbidden (error-handling-convention.md §2)
7. Kirim request daftar Changelog Device Name dengan sesi akun Distributor Jaringan
8. Verifikasi server menolak request Changelog dengan 403 Forbidden (error-handling-convention.md §2)
9. Verifikasi respons keempat request tidak memuat data Device Name
10. Verifikasi tidak ada data Device Name yang dikembalikan oleh keempat request

### TC-AC-DN-540: Request tulis oleh Distributor ditolak server

11. Kirim request Create Device Name `Direct Create Test {runId}-029` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Distributor Jaringan
12. Verifikasi server menolak request Create dengan 403 Forbidden (error-handling-convention.md §2)
13. Kirim request Edit Device Name `Cable Tester {runId}-029` menjadi `Direct Edit Test {runId}-029` dengan sesi akun Distributor Jaringan
14. Verifikasi server menolak request Edit dengan 403 Forbidden (error-handling-convention.md §2)
15. Kirim request Delete Device Name `Door Antenna {runId}-029` dengan sesi akun Distributor Jaringan
16. Verifikasi server menolak request Delete dengan 403 Forbidden (error-handling-convention.md §2)
17. Verifikasi respons ketiga request tidak memuat data Device Name
18. Verifikasi data Device Name tidak berubah
19. Buka halaman `Settings > Device > Device Name`
20. Ketik Search `{runId}-029`, tekan Enter
21. Verifikasi Device Name `Cable Tester {runId}-029` tetap bernama `Cable Tester {runId}-029`
22. Verifikasi Device Name `Door Antenna {runId}-029` tetap ada
23. Verifikasi Device Name `Direct Create Test {runId}-029` tidak ada
24. Klik `(←)` pada kotak Search

### TC-AC-DN-541: Request baca oleh Partner ditolak server

25. Kirim request daftar Device Name memakai klien HTTP dengan sesi akun Partner Jaringan
26. Verifikasi server menolak request daftar dengan 403 Forbidden (error-handling-convention.md §2)
27. Kirim request detail Device Name `Gate Antenna` dengan sesi akun Partner Jaringan
28. Verifikasi server menolak request detail dengan 403 Forbidden (error-handling-convention.md §2)
29. Kirim request download daftar Device Name format CSV dengan sesi akun Partner Jaringan
30. Verifikasi server menolak request download CSV dengan 403 Forbidden (error-handling-convention.md §2)
31. Kirim request daftar Changelog Device Name dengan sesi akun Partner Jaringan
32. Verifikasi server menolak request Changelog dengan 403 Forbidden (error-handling-convention.md §2)
33. Verifikasi respons keempat request tidak memuat data Device Name
34. Verifikasi tidak ada data Device Name yang dikembalikan oleh keempat request

### TC-AC-DN-542: Request tulis oleh Partner ditolak server

35. Kirim request Create Device Name `Direct Create Test {runId}-029` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Partner Jaringan
36. Verifikasi server menolak request Create dengan 403 Forbidden (error-handling-convention.md §2)
37. Kirim request Edit Device Name `Cable Tester {runId}-029` menjadi `Direct Edit Test {runId}-029` dengan sesi akun Partner Jaringan
38. Verifikasi server menolak request Edit dengan 403 Forbidden (error-handling-convention.md §2)
39. Kirim request Delete Device Name `Door Antenna {runId}-029` dengan sesi akun Partner Jaringan
40. Verifikasi server menolak request Delete dengan 403 Forbidden (error-handling-convention.md §2)
41. Verifikasi respons ketiga request tidak memuat data Device Name
42. Verifikasi data Device Name tidak berubah
43. Buka halaman `Settings > Device > Device Name`
44. Ketik Search `{runId}-029`, tekan Enter
45. Verifikasi Device Name `Cable Tester {runId}-029` tetap bernama `Cable Tester {runId}-029`
46. Verifikasi Device Name `Door Antenna {runId}-029` tetap ada
47. Verifikasi Device Name `Direct Create Test {runId}-029` tidak ada
48. Klik `(←)` pada kotak Search

### TC-AC-DN-627: Request ke endpoint dropdown Device Name oleh Partner ditolak server

49. Kirim request GET daftar opsi dropdown Device Name memakai klien HTTP dengan sesi akun Partner Jaringan
50. Verifikasi server menolak request sesi Partner dengan 403 Forbidden (error-handling-convention.md §2)
51. Verifikasi respons tidak memuat daftar Device Name

## Notes

- Spec defense-in-depth (kelas a): request langsung ke server oleh entitas tanpa akses. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-DN-539, 540, 541, 542, dan 627 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap FE+BE walau tumpang tindih dengan `tc-settings-device-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Penyimpangan data (S-06): target Edit dan Delete (`Cable Tester`, `Door Antenna` Pre-setup #16 di TC) diganti record milik spec bersuffix; request ditolak sehingga record tidak berubah. Search `{runId}-029` pada pengamatan List mempersempit List ke record milik spec; baris `Cable Tester {runId}-029` dan `Door Antenna {runId}-029` menjadi anchor positif asersi absence `Direct Create Test {runId}-029`.
- Langkah penghubung (S-03): `Buka halaman` dan Search pada pengamatan List (R-16) serta mengosongkan Search lewat `(←)`. Verifikasi "data Device Name tidak berubah" (Expected c) dipenuhi rincian pengamatan List sesudahnya.
- Ukuran spec (51 langkah, di atas 35 langkah; alasan R3): seluruh blok satu kelas harness (a) dengan klien HTTP yang sama dan dataset milik spec yang sama; blok per entitas (Distributor lalu Partner) dan per jenis request berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Expected b ("Respons tidak memuat data Device Name") dan c ("Tidak ada data Device Name yang dikembalikan") pada TC baca bermakna sama; keduanya tetap diasersi sebagai Verifikasi terpisah.
  - Post Condition tiap TC defense request tulis sama dengan butir Expected c; hanya Expected c yang diasersi (tidak ada Verifikasi ganda).
