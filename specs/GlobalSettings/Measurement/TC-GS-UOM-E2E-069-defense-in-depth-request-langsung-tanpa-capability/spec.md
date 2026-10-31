---
id: TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability
title: "Defense-in-Depth: Request Tulis dan Baca Langsung ke Server Tanpa Capability Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-235
  - TC-GS-UOM-236
  - TC-GS-UOM-237
  - TC-GS-UOM-271
  - TC-GS-UOM-411
  - TC-GS-UOM-412
coverage:
  web: automated
---

# Defense-in-Depth: Request Tulis dan Baca Langsung ke Server Tanpa Capability Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai empat akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | System Role: Read saja (Tono Hartono) | `readCapability_automated_qaTeam1@qwertysystem.net` | `GS_READ_PASSWORD` |
  | 2 | Read Only (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `GS_RO_PASSWORD` |
  | 3 | System Role: Create dan Read (Rina Marlina) | `createOnly_automated_qaTeam1@qwertysystem.net` | `GS_CREATE_PASSWORD` |
  | 4 | Tanpa Capability (Fajar Nugroho) | `noCapability_automated_qaTeam1@qwertysystem.net` | `GS_NOCAP_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_READ_PASSWORD`, `GS_RO_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`, bagian Hook suite).
- Kemampuan teknis: (a) klien HTTP yang mengirim request Measurement langsung ke server memakai token sesi aktor yang sedang login (sesi dari login UI akun tersebut); (b) membaca state data Measurement lewat fixture BE dengan sesi API aktor Total Control Client A (lihat `suite.md`, bagian Hook suite; disediakan tim FE; endpoint tidak disebut TC) untuk asersi "data tidak berubah". Asersi spec ini hanya respons server dan state data (bagian 8b butir 1).
- Data Pre-setup Client A (hanya dirujuk request yang ditolak, tidak diubah, tanpa suffix `{runId}`): `Box` (Check References, TC-GS-UOM-412) dan `Kilogram` (Detail, TC-GS-UOM-411).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): `Target {runId}-069` / `tg`, di-seed lewat API di hook `before` (target request Edit dan Delete yang ditolak; TC tidak menyebut unit target). `Rogue {runId}-069` dan `Rogue RO {runId}-069` adalah nama pada request Create yang ditolak sehingga tidak membuat data.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target`, `Rogue`, dan `Rogue RO` bersuffix `{runId}-069` bila ada.
- Tidak ada state global yang diubah.
- TC-GS-UOM-235, 236, 237: login sebagai System Role: Read saja. TC-GS-UOM-271: Read Only. TC-GS-UOM-412: System Role: Create dan Read. TC-GS-UOM-411: Tanpa Capability. Semua berada di halaman Global Settings yang termuat setelah login.

## Test Steps

### TC-GS-UOM-235, 236, 237: System Role Read saja menolak Create, Edit, dan Delete langsung

1. Kirim request Create Measurement langsung ke server dengan Unit Name `Rogue {runId}-069` dan Symbol `rg` memakai sesi aktor
2. Verifikasi server menolak `403 Forbidden`
3. Verifikasi `Target {runId}-069` ada pada data Measurement (anchor) dan `Rogue {runId}-069` tidak ada
4. Kirim request Edit Measurement langsung untuk `Target {runId}-069` dengan Symbol `tx` memakai sesi aktor
5. Verifikasi server menolak `403 Forbidden`
6. Verifikasi Symbol `Target {runId}-069` tetap `tg`
7. Kirim request Delete Measurement langsung untuk `Target {runId}-069` memakai sesi aktor
8. Verifikasi server menolak `403 Forbidden`
9. Verifikasi `Target {runId}-069` tetap ada pada data Measurement

### TC-GS-UOM-271: Read Only menolak request tulis langsung

10. Ganti akun: logout, lalu login sebagai Read Only (`readOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_RO_PASSWORD`
11. Kirim request Create Measurement langsung ke server dengan Unit Name `Rogue RO {runId}-069` dan Symbol `rr` memakai sesi aktor
12. Verifikasi server menolak `403 Forbidden`
13. Kirim request Edit Measurement langsung untuk `Target {runId}-069` dengan Symbol `tx` memakai sesi aktor
14. Verifikasi server menolak `403 Forbidden`
15. Kirim request Delete Measurement langsung untuk `Target {runId}-069` memakai sesi aktor
16. Verifikasi server menolak `403 Forbidden`
17. Verifikasi `Target {runId}-069` ada dengan Symbol `tg` dan `Rogue RO {runId}-069` tidak ada pada data Measurement

### TC-GS-UOM-412: System Role Create dan Read dapat membaca tetapi Check References membutuhkan capability Delete

18. Ganti akun: logout, lalu login sebagai System Role: Create dan Read (`createOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_CREATE_PASSWORD`
19. Kirim request List langsung ke server memakai sesi aktor
20. Verifikasi respons List `200` dengan baris Measurement
21. Kirim request Check References langsung untuk `Box` memakai sesi aktor
22. Verifikasi server menolak `403 Forbidden`

### TC-GS-UOM-411: Aktor tanpa capability membaca langsung ditolak pada seluruh route baca

23. Ganti akun: logout, lalu login sebagai Tanpa Capability (`noCapability_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_NOCAP_PASSWORD`
24. Kirim request List langsung ke server memakai sesi aktor
25. Verifikasi server menolak `403 Forbidden`
26. Kirim request Export langsung ke server memakai sesi aktor
27. Verifikasi server menolak `403 Forbidden`
28. Kirim request Dropdown langsung ke server memakai sesi aktor
29. Verifikasi server menolak `403 Forbidden`
30. Kirim request Detail untuk `Kilogram` langsung ke server memakai sesi aktor
31. Verifikasi server menolak `403 Forbidden`
32. Kirim request Check Availability langsung ke server memakai sesi aktor
33. Verifikasi server menolak `403 Forbidden`
34. Verifikasi tidak ada respons dari kelima request yang memuat data Measurement

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas defense-in-depth (prinsip 13a, direct API tampering atau 403) tanpa harness eksternal. TC-GS-UOM-235, 236, 237, 271, 411, dan 412 bertanda server langsung (FE Test `-`, PIC FE `-`) di TC sumber; sesuai konvensi 3 prinsip 13 kelas a dan preseden `TC-GS-BRAND-E2E-068`, TC itu tetap berada di spec dengan asersi hanya respons server dan state data (bagian 8b butir 1). Perilaku FE untuk capability yang sama (Tab, tombol Create, Edit, Delete) diasersi di spec Role Matrix 013 sampai 015.
- Urutan TC di spec berbeda dari urutan sumber: dikelompokkan per akun supaya ganti akun minimal (langkah 10, 18, dan 23): Read saja (235, 236, 237), Read Only (271), Create dan Read (412), lalu Tanpa Capability (411). Semua request ditolak, sehingga tidak ada data yang dihabisi.
- TC-GS-UOM-30 dan 31 (akses langsung URL dan capability bersama Brand) ada di spec 014.
- Langkah penghubung: langkah 10, 18, dan 23 (ganti akun eksplisit, S-07). Langkah 3 dan 17 menjadi anchor positif (Target ada) bagi absence `Rogue` dan `Rogue RO` (bagian 8b butir 2).
- Sumber tidak menyebut unit target request Edit dan Delete (TC-GS-UOM-236, 237, 271); spec memakai unit milik spec `Target {runId}-069` agar baris Pre-setup tidak menjadi target (S-06).
- Temuan untuk QA:
  - Precondition TC-GS-UOM-411 "User berada di Global Settings > Master Reference > Measurement" tidak dapat dipenuhi aktor Tanpa Capability (Tab Measurement tidak tampil, lihat TC-GS-UOM-23 dan 30); spec mengirim request dari halaman Global Settings yang termuat setelah login.
  - TC-GS-UOM-235 sampai 237 dan 271 tidak menyebut payload (nama, symbol, id target); TC-GS-UOM-411 tidak menyebut bentuk request Export dan Check Availability. Spec mengikuti kata TC tanpa mengarang endpoint (S-13).
  - TC-GS-UOM-235, 236, 237, 271 dan 411 butir "Data tidak berubah" atau "Tidak ada data dikembalikan" membutuhkan pembacaan state lewat fixture BE; mekanismenya tidak disebut TC dan disediakan tim FE.
  - TC-GS-UOM-412 Expected a menyebut "List `200` dengan baris Measurement (C mengimplikasikan R)"; sesuai PRD §2 dan §9.3.
