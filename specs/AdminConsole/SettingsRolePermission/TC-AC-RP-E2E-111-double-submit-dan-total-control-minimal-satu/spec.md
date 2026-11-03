---
id: TC-AC-RP-E2E-111-double-submit-dan-total-control-minimal-satu
title: "Double Submit: Klik Assign dan Confirm Ganda Tanpa Efek Ganda, serta Total Control Selalu Minimal Satu"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-407
  - TC-AC-RP-408
  - TC-AC-RP-410
coverage:
  web: automated
---

# Double Submit: Klik Assign dan Confirm Ganda Tanpa Efek Ganda, serta Total Control Selalu Minimal Satu

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit pada langkah 25 (S-07): Default User Principal `defaultUserRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Bambang Hartono`, Pre-setup #2), password dari `Spectra.env.AC_RP_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (user Standard `Alex Tan`), #13 (pemegang Total Control), #15 (`Manage device master data` John Dohan C/R/U), #18 (Riwayat Changelog seed), dan #26 (Changelog).
- Tabel "Total Control yang dilepas" (TC-AC-RP-410, Pre-setup #13; selain `Bambang Hartono`):

| No | Nama user |
|---|---|
| 1 | `Budi Santoso` |
| 2 | `John Doe` |
| 3 | `Rina Wijaya` |
| 4 | `Sarah Kim` |
| 5 | `Siti Nurhaliza` |

- Data Dinamis: spec ini tidak membuat entitas baru; target aksi adalah user Pre-setup bernama literal sesuai TC (S-06), sehingga suffix `+{runId}-111` tidak dipakai.
- Kemampuan teknis: penghitung request Assign dan Remove lewat intercept pass-through (Pre-setup #23) yang tidak mengubah respons (disediakan tim FE; langkah 6); modal Changelog (Table Tools) untuk baseline jumlah entri audit trail permanen (S-12).
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`, `AC_RP_DU_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-407: Klik Assign ganda tidak membuat efek ganda

1. Buka modal Changelog Tab Total Control lewat Table Tools
2. Catat jumlah entri Changelog sebagai baseline
3. Tutup modal Changelog
4. Klik `+ Assign` lalu centang `Alex Tan`
5. Klik `[Assign]` dua kali berturut-turut dengan cepat
6. Verifikasi hanya satu request Assign diproses
7. Verifikasi satu toast sukses "Success, Total Control has been assigned."
8. Verifikasi `Alex Tan` tampil satu baris di Tab Total Control
9. Buka modal Changelog Tab Total Control lewat Table Tools
10. Verifikasi jumlah entri Changelog bertambah satu dibanding baseline langkah 2
11. Tutup modal Changelog
12. Pulihkan baseline: Total Control `Alex Tan` di-Remove lewat kemampuan reset FE/BE

### TC-AC-RP-408: Klik Confirm dialog Remove ganda tidak membuat efek ganda

13. Klik tab `System`
14. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
15. Buka modal Changelog `Manage device master data` lewat Table Tools
16. Catat jumlah entri Changelog sebagai baseline
17. Tutup modal Changelog
18. Klik `⋯` baris `John Dohan` lalu klik `Remove`
19. Klik `[Remove]` dua kali dengan cepat
20. Verifikasi satu toast "Success, user has been removed."
21. Buka modal Changelog `Manage device master data` lewat Table Tools
22. Verifikasi jumlah entri Changelog bertambah satu dibanding baseline langkah 16
23. Tutup modal Changelog
24. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` dengan C, R, U

### TC-AC-RP-410: Total Control selalu minimal satu lewat Default User

25. Ganti akun: logout, lalu login sebagai Default User `Bambang Hartono` (`Spectra.env.AC_RP_DU_PASSWORD`)
26. Buka halaman `Settings > Role & Permission` (Tab Total Control aktif)
27. Untuk setiap baris tabel "Total Control yang dilepas" pada Prerequisites, lakukan langkah 28 sampai 29
28. Klik `⋯` baris user lalu klik `Remove`
29. Klik `[Remove]`
30. Verifikasi `Bambang Hartono` tetap Total Control (baris tampil di Tab Total Control)
31. Verifikasi `Remove` milik `Bambang Hartono` Disabled
32. Verifikasi Tab Total Control tidak kosong
33. Pulihkan baseline: Total Control `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, dan `Siti Nurhaliza` dikembalikan lewat kemampuan reset FE/BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec melewati sekitar 35 langkah (bagian 8b butir 7: ambang dihitung dengan ekspansi; 5 iterasi langkah 28 sampai 29): ketiga blok TC berdiri sendiri dengan baseline dan pemulihan sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, S-09): langkah 2 dan 16 (baseline jumlah entri Changelog, S-12); langkah 12, 24, dan 33 (pemulihan baseline).
- Langkah berulang (bagian 8b butir 7): langkah 28 dan 29 diulang per baris tabel "Total Control yang dilepas" (lima iterasi).
- Temuan untuk QA:
  - TC-AC-RP-407 "Hanya satu request diproses" tidak menyebut cara pengamatan; spec memakai penghitung request lewat intercept pass-through yang disediakan tim FE (S-11, S-13).
  - TC-AC-RP-407 dan TC-AC-RP-408 tidak menyebut surface log; spec memakai modal Changelog (Tab Total Control untuk Assign, `Manage device master data` untuk Remove) dan mengasersi selisih satu entri terhadap baseline.
  - TC-AC-RP-410 langkah "Remove Total Control seluruh user selain `Bambang Hartono`" tidak menyebut cara (satu per satu atau massal); spec memakai Remove satu per satu atas lima user Pre-setup #13. Setiap Remove baris `Siti Nurhaliza` mencabut hak aktor default suite sampai baseline dipulihkan.
  - TC-AC-RP-410 Expected "Tab Total Control tidak pernah kosong" dibaca sebagai keadaan akhir sesudah semua Remove; keadaan antar-Remove tidak diamati.
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
