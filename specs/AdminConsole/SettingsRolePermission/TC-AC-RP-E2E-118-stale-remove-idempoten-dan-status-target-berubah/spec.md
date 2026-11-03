---
id: TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah
title: "Target Berubah sejak Render: Remove Idempoten, Approver Sudah Hilang, dan Status Target Berubah menjadi Total Control"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-398
  - TC-AC-RP-399
  - TC-AC-RP-400
  - TC-AC-RP-401
coverage:
  web: automated
---

# Target Berubah sejak Render: Remove Idempoten, Approver Sudah Hilang, dan Status Target Berubah menjadi Total Control

## Prerequisites

- Mode: FE+BE (backend nyata; Sesi A lewat UI, Sesi B lewat sesi API)
- Akun aktor Sesi A (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat langkah Ganti akun):

| Urutan | Aktor | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | `Siti Nurhaliza` (Total Control Principal, Pre-setup #1) | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` | TC-AC-RP-398, 399, 401 |
| 2 | `Hendra Wijaya` (Manage user and role R+U, Pre-setup #4) | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` | TC-AC-RP-400 |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Pelaku kedua (Sesi B, Total Control; Pre-setup #24): sesi API untuk akun `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`); hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`John Dohan`), #15 (peran individual `Manage device master data`: `John Dohan` C/R/U), #17 (approver `Manage TAG stock`: `Sarah Kimura`), #18 (Riwayat Changelog seed), dan #24 (dua sesi). Target aksi adalah data Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-118` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): sesi API aktor (dinyatakan di `suite.md`); kemampuan membaca state data lewat fixture BE (tingkat akses `John Dohan`); kemampuan baca jumlah entri Changelog lewat modal Changelog `Manage device master data` (Table Tools) di UI. Jumlah entri dibaca sebelum aksi sebagai baseline karena Changelog adalah audit trail permanen (S-12), tanpa angka absolut.
- Pemulihan baseline: data Pre-setup yang diubah spec ini (peran `John Dohan`, tingkat akses `John Dohan`, approver `Sarah Kimura`) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama), dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_MUR_U_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-398: Remove baris peran yang sudah hilang tetap sukses idempoten

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove peran `John Dohan` pada `Manage device master data` hingga tersimpan
4. Tunggu aksi selesai (Sesi B tersimpan)
5. Sesi A: buka modal Changelog `Manage device master data` melalui Table Tools
6. Catat jumlah entri Changelog sebagai baseline
7. Tutup modal Changelog
8. Sesi A: klik `⋯` baris `John Dohan` lalu klik `Remove`
9. Klik `[Remove]`
10. Verifikasi toast "Success, user has been removed."
11. Buka modal Changelog `Manage device master data` melalui Table Tools
12. Verifikasi jumlah entri Changelog sama dengan baseline langkah 6 (tanpa entri log tambahan)
13. Tutup modal Changelog
14. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` C/R/U lewat kemampuan reset FE/BE

### TC-AC-RP-399: Remove Approver yang sudah hilang tetap sukses

15. Buka halaman `Settings > Role & Permission`
16. Klik tab `System`
17. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
18. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove approver `Sarah Kimura` pada `Manage TAG stock` hingga tersimpan
19. Tunggu aksi selesai (Sesi B tersimpan)
20. Sesi A: klik `⋯` baris approver `Sarah Kimura` pada Approvers Section lalu klik `Remove`
21. Klik `[Remove]`
22. Verifikasi toast "Success, approver has been removed."
23. Pulihkan baseline: `Sarah Kimura` kembali menjadi approver `Manage TAG stock` lewat kemampuan reset FE/BE

### TC-AC-RP-401: Status target berubah TC antara render dan submit bagi Total Control

24. Buka halaman `Settings > Role & Permission`
25. Klik tab `System`
26. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
27. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Total Control ke `John Dohan` hingga tersimpan
28. Tunggu aksi selesai (Sesi B tersimpan)
29. Sesi A: hapus centang C baris `John Dohan`
30. Verifikasi aksi diproses terhadap status saat submit: checkbox C baris `John Dohan` kembali tercentang (auto-revert mengikuti status Total Control)
31. Verifikasi lewat fixture BE bahwa tingkat akses `John Dohan` tetap Total Control
32. Pulihkan baseline: `John Dohan` kembali user Standard dengan peran `Manage device master data` C/R/U lewat kemampuan reset FE/BE

33. Ganti akun: logout, lalu login sebagai `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
34. Buka halaman `Settings > Role & Permission`

### TC-AC-RP-400: Status target berubah TC antara render dan submit bagi Manage user and role

35. Klik tab `System`
36. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
37. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Total Control ke `John Dohan` hingga tersimpan
38. Tunggu aksi selesai (Sesi B tersimpan)
39. Sesi A (`Hendra Wijaya`): centang D baris `John Dohan`
40. Verifikasi permintaan perubahan dari Sesi A ditolak dengan status 403 berdasarkan status `John Dohan` saat submit
41. Verifikasi checkbox D baris `John Dohan` kembali ke nilai semula
42. Verifikasi data Role Detail di-refresh dan `John Dohan` tampil sebagai Total Control
43. Pulihkan baseline: `John Dohan` kembali user Standard dengan peran `Manage device master data` C/R/U lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Aktor: Sesi A pada TC-AC-RP-398, 399, 401 adalah `Siti Nurhaliza` dan pada TC-AC-RP-400 adalah `Hendra Wijaya`; Sesi B dijalankan lewat sesi API `Siti Nurhaliza` sesuai keputusan pelaku kedua memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (S-03, S-07, S-09): langkah 3, 18, 27, 37 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 4, 19, 28, 38 ("Tunggu aksi selesai", bagian 8b butir 8), langkah 5, 7, dan 11 (membuka dan menutup modal Changelog untuk pencatatan baseline, S-12), langkah 6 dan 13 (baseline dan penutupan modal Changelog), langkah 14, 23, 32, 43 (pemulihan baseline), langkah 15, 24, 34 (membuka halaman), langkah 33 (Ganti akun eksplisit, S-07).
- Ganti akun eksplisit pada langkah 33: TC-AC-RP-400 mensyaratkan aktor Manage user and role sedangkan TC-AC-RP-398, 399, dan 401 mensyaratkan Total Control; TC-AC-RP-400 ditaruh di akhir agar ganti akun hanya sekali (S-10). Login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun.
- Alasan di atas sekitar 35 langkah (43 langkah): spec memakai Step Ganti akun eksplisit dan bagian sesudah ganti akun (TC-AC-RP-400) tetap bermakna walau bagian sebelumnya gagal keras; semua blok berada dalam satu topik "target berubah antara render dan submit" tanpa kelas harness lain, tiap blok membuka halaman dari awal dan memulihkan datanya sendiri.
- P-1: asersi "tanpa entri log tambahan" pada TC-AC-RP-398 ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state peran yang baru diubah Sesi B; spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05). Baseline: jumlah entri Changelog `Manage device master data` sebelum aksi Sesi A.
- Temuan untuk QA:
  - TC-AC-RP-398 sampai 401 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua (spec dipindah ke kelas c).
  - TC-AC-RP-398 sampai 401 tidak menyebut akun Sesi B; spec memakai sesi API akun `Siti Nurhaliza` (Pre-setup #24 hanya menyebut "dua sesi paralel Total Control", S-13).
  - TC-AC-RP-398: Expected "tanpa entri log tambahan" tidak menyebut surface log; spec memakai modal Changelog `Manage device master data` (Catatan TC menyebut modal Changelog per role). Entri yang ditambah Sesi B sebelum baseline tidak dihitung.
  - TC-AC-RP-399: langkah TC "Sesi A Remove baris yang sama dan konfirmasi" tidak menyebut aksi baris di Approvers Section; spec menulis `Remove` pada menu `⋯` baris approver. Mohon konfirmasi label aksi baris approver.
  - TC-AC-RP-401: Expected "Aksi diproses terhadap status saat submit; auto-revert berlaku mengikuti status Total Control `John Dohan` saat submit" tidak menyebut hal yang teramati; spec mengasersi checkbox C kembali tercentang dan tingkat akses `John Dohan` tetap Total Control.
  - TC-AC-RP-400: Expected "Perubahan ditolak 403 ... data di-refresh" tidak menyebut pesan atau toast; spec mengasersi status respons permintaan perubahan yang diamati di browser, nilai checkbox, dan data Role Detail.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
