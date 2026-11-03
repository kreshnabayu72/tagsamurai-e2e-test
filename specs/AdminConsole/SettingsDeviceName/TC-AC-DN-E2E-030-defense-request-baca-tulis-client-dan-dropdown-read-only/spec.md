---
id: TC-AC-DN-E2E-030-defense-request-baca-tulis-client-dan-dropdown-read-only
title: "Defense-in-Depth: Request Baca dan Tulis oleh Client Ditolak Server, serta Dropdown Read-only Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-543
  - TC-AC-DN-544
  - TC-AC-DN-655
coverage:
  web: automated
---

# Defense-in-Depth: Request Baca dan Tulis oleh Client Ditolak Server, serta Dropdown Read-only Client

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #11 | Total Control pada entitas Client `Client Jaringan` | (tanpa nama di TC) | `totalControlClient_automated_{namaCompany}@qwertysystem.net` | `akunClient` | `Spectra.env.AC_DN_CLIENT_PASSWORD` | TC-AC-DN-543, TC-AC-DN-544, TC-AC-DN-655 |
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-544, TC-AC-DN-655 (pengamat List) |

- Env var password: `Spectra.env.AC_DN_CLIENT_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_CLIENT_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan login API (password) tiap akun; token tidak dihitung sebagai sesi web (`suite.md`). Request langsung hanya mengasersi respons server (status); state data diamati lewat List pada sesi Total Control UI (hook `before`) dan fixture backend (bagian 8b butir 1).
- Penghapusan record milik spec dan pemulihan dilakukan fixture backend di hook `after`.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before`: `Cable Tester {runId}-030` (Category `Accessory`, Measurement `Unit`) dan `Door Antenna {runId}-030` (Category `Antenna`, Measurement `Unit`) sebagai target Edit dan Delete yang ditolak server; `Direct Create Test {runId}-030` adalah nama request Create yang ditolak. `Gate Antenna` (Pre-setup #16) hanya dibaca.
- Data tambahan TC-AC-DN-655: `Gate Antenna` (Category `Antenna`) dan `Field Radio` (Category `Accessory`) dari Device Name inti (#16) hanya dibaca; nama request Create yang ditolak `Direct Create Test {runId}-030-B`.

## Test Steps

### TC-AC-DN-543: Request baca oleh Client ditolak server

1. Kirim request daftar Device Name memakai klien HTTP dengan sesi akun Client Jaringan
2. Verifikasi server menolak request daftar dengan 403 Forbidden (error-handling-convention.md §2)
3. Kirim request detail Device Name `Gate Antenna` dengan sesi akun Client Jaringan
4. Verifikasi server menolak request detail dengan 403 Forbidden (error-handling-convention.md §2)
5. Kirim request download daftar Device Name format CSV dengan sesi akun Client Jaringan
6. Verifikasi server menolak request download CSV dengan 403 Forbidden (error-handling-convention.md §2)
7. Kirim request daftar Changelog Device Name dengan sesi akun Client Jaringan
8. Verifikasi server menolak request Changelog dengan 403 Forbidden (error-handling-convention.md §2)
9. Verifikasi respons keempat request tidak memuat data Device Name
10. Verifikasi tidak ada data Device Name yang dikembalikan oleh keempat request

### TC-AC-DN-544: Request tulis oleh Client ditolak server

11. Kirim request Create Device Name `Direct Create Test {runId}-030` (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi akun Client Jaringan
12. Verifikasi server menolak request Create dengan 403 Forbidden (error-handling-convention.md §2)
13. Kirim request Edit Device Name `Cable Tester {runId}-030` menjadi `Direct Edit Test {runId}-030` dengan sesi akun Client Jaringan
14. Verifikasi server menolak request Edit dengan 403 Forbidden (error-handling-convention.md §2)
15. Kirim request Delete Device Name `Door Antenna {runId}-030` dengan sesi akun Client Jaringan
16. Verifikasi server menolak request Delete dengan 403 Forbidden (error-handling-convention.md §2)
17. Verifikasi respons ketiga request tidak memuat data Device Name
18. Verifikasi data Device Name tidak berubah
19. Buka halaman `Settings > Device > Device Name`
20. Ketik Search `{runId}-030`, tekan Enter
21. Verifikasi Device Name `Cable Tester {runId}-030` tetap bernama `Cable Tester {runId}-030`
22. Verifikasi Device Name `Door Antenna {runId}-030` tetap ada
23. Verifikasi Device Name `Direct Create Test {runId}-030` tidak ada
24. Klik `(←)` pada kotak Search

### TC-AC-DN-655: Client membaca opsi Device Name lewat endpoint dropdown read-only sedangkan list dan endpoint tulis tetap ditolak server

25. Kirim request GET daftar opsi dropdown Device Name memakai klien HTTP dengan sesi akun Client Jaringan untuk konteks Category `Antenna`
26. Verifikasi request dropdown berhasil (200 OK)
27. Verifikasi respons dropdown memuat opsi "Gate Antenna" (Category Antenna)
28. Verifikasi respons dropdown tidak memuat opsi "Field Radio" (Category Accessory, di luar konteks)
29. Verifikasi daftar opsi dropdown bersifat hanya baca
30. Kirim request daftar Device Name dengan sesi akun Client Jaringan
31. Verifikasi server menolak request daftar dengan 403 Forbidden (error-handling-convention.md §2)
32. Verifikasi respons request daftar tidak memuat data Device Name
33. Kirim request Create Device Name `Direct Create Test {runId}-030-B` (Measurement `Unit`, Category `Antenna`) dengan sesi akun Client Jaringan
34. Verifikasi server menolak request Create dengan 403 Forbidden (error-handling-convention.md §2)
35. Verifikasi respons request Create tidak memuat data Device Name
36. Buka halaman `Settings > Device > Device Name`
37. Ketik Search `Direct Create Test {runId}-030-B`, tekan Enter
38. Verifikasi empty state "No results found" tampil
39. Verifikasi List Principal tidak memuat `Direct Create Test {runId}-030-B`
40. Klik `(←)` pada kotak Search

## Notes

- Spec defense-in-depth (kelas a): request langsung ke server oleh entitas Client. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-DN-543, 544, dan 655 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap FE+BE walau tumpang tindih dengan `tc-settings-device-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Penyimpangan data (S-06): target Edit dan Delete diganti record milik spec bersuffix; request ditolak sehingga record tidak berubah. Pada TC-AC-DN-655 pengamatan List memakai empty state Search "No results found" sebagai anchor positif asersi absence (bagian 8b butir 2).
- Langkah penghubung (S-03): `Buka halaman` dan Search pada pengamatan List (R-16) serta mengosongkan Search lewat `(←)`. Verifikasi "data Device Name tidak berubah" (Expected c TC-AC-DN-544) dipenuhi rincian pengamatan List sesudahnya.
- Pembagian TC lintas spec: TC-AC-DN-545 dan 546 (Principal tanpa capability) ada di spec 041.
- Ukuran spec (40 langkah, di atas 35 langkah): seluruh blok satu kelas harness (a) dengan klien HTTP yang sama dan akun Client yang sama; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-DN-655 Expected a menyebut daftar "hanya baca" tanpa cara mengamatinya; spec memverifikasinya sebagai klausa sendiri dan keterbacaannya hanya teramati lewat ditolaknya request tulis (Verifikasi 403 Create).
  - Expected b dan c pada TC baca bermakna sama (respons tanpa data); keduanya tetap diasersi terpisah.
  - Post Condition tiap TC defense request tulis sama dengan butir Expected c; hanya Expected c yang diasersi (tidak ada Verifikasi ganda).
