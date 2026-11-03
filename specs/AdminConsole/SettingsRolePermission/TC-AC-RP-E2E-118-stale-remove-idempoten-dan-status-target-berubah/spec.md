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
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`John Dohan`), #15 (peran individual `Manage device master data`: `John Dohan` C/R/U), #17 (approver `Manage TAG stock`: `Sarah Kimura`), dan #24 (dua sesi). Target aksi adalah data Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-118` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): sesi API aktor (dinyatakan di `suite.md`); kemampuan membaca state data lewat fixture BE (tingkat akses `John Dohan`); kemampuan baca jumlah entri audit trail pelaku (Detail User `Siti Nurhaliza` > Tab System Log dan Activity Log Admin Console, 8b butir 10), dipakai tanpa berpindah halaman supaya Sesi A tetap berada di Role Detail. Jumlah entri dibaca sebelum aksi sebagai baseline karena audit trail permanen (S-12), tanpa angka absolut.
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
5. Catat baseline jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console pelaku
6. Sesi A: klik `⋯` baris `John Dohan` lalu klik `Remove`
7. Klik `[Remove]`
8. Verifikasi toast "Success, user has been removed."
9. Verifikasi jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log sama dengan baseline langkah 5 (selisih 0, tanpa entri log tambahan)
10. Verifikasi jumlah entri Activity Log Admin Console pelaku sama dengan baseline langkah 5 (selisih 0, tanpa entri log tambahan)
11. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` C/R/U lewat kemampuan reset FE/BE

### TC-AC-RP-399: Remove Approver yang sudah hilang tetap sukses

12. Buka halaman `Settings > Role & Permission`
13. Klik tab `System`
14. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
15. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove approver `Sarah Kimura` pada `Manage TAG stock` hingga tersimpan
16. Tunggu aksi selesai (Sesi B tersimpan)
17. Sesi A: klik `⋯` baris approver `Sarah Kimura` pada Approvers Section lalu klik `Remove`
18. Klik `[Remove]`
19. Verifikasi toast "Success, approver has been removed."
20. Pulihkan baseline: `Sarah Kimura` kembali menjadi approver `Manage TAG stock` lewat kemampuan reset FE/BE

### TC-AC-RP-401: Status target berubah TC antara render dan submit bagi Total Control

21. Buka halaman `Settings > Role & Permission`
22. Klik tab `System`
23. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
24. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Total Control ke `John Dohan` hingga tersimpan
25. Tunggu aksi selesai (Sesi B tersimpan)
26. Sesi A: hapus centang C baris `John Dohan`
27. Verifikasi aksi diproses terhadap status saat submit: checkbox C baris `John Dohan` kembali tercentang (auto-revert mengikuti status Total Control)
28. Verifikasi lewat fixture BE bahwa tingkat akses `John Dohan` tetap Total Control
29. Pulihkan baseline: `John Dohan` kembali user Standard dengan peran `Manage device master data` C/R/U lewat kemampuan reset FE/BE

30. Ganti akun: logout, lalu login sebagai `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
31. Buka halaman `Settings > Role & Permission`

### TC-AC-RP-400: Status target berubah TC antara render dan submit bagi Manage user and role

32. Klik tab `System`
33. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
34. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Total Control ke `John Dohan` hingga tersimpan
35. Tunggu aksi selesai (Sesi B tersimpan)
36. Sesi A (`Hendra Wijaya`): centang D baris `John Dohan`
37. Verifikasi permintaan perubahan dari Sesi A ditolak dengan status 403 berdasarkan status `John Dohan` saat submit
38. Verifikasi checkbox D baris `John Dohan` kembali ke nilai semula
39. Verifikasi data Role Detail di-refresh dan `John Dohan` tampil sebagai Total Control
40. Pulihkan baseline: `John Dohan` kembali user Standard dengan peran `Manage device master data` C/R/U lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Aktor: Sesi A pada TC-AC-RP-398, 399, 401 adalah `Siti Nurhaliza` dan pada TC-AC-RP-400 adalah `Hendra Wijaya`; Sesi B dijalankan lewat sesi API `Siti Nurhaliza` sesuai keputusan pelaku kedua memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (S-03, S-07, S-09): langkah 3, 15, 24, 34 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 4, 16, 25, 35 ("Tunggu aksi selesai", bagian 8b butir 8), langkah 5 (baseline jumlah entri audit trail pelaku, S-12), langkah 11, 20, 29, 40 (pemulihan baseline), langkah 12, 21, 31 (membuka halaman), langkah 30 (Ganti akun eksplisit, S-07).
- Ganti akun eksplisit pada langkah 30: TC-AC-RP-400 mensyaratkan aktor Manage user and role sedangkan TC-AC-RP-398, 399, dan 401 mensyaratkan Total Control; TC-AC-RP-400 ditaruh di akhir agar ganti akun hanya sekali (S-10). Login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun.
- Alasan di atas sekitar 35 langkah (40 langkah): spec memakai Step Ganti akun eksplisit dan bagian sesudah ganti akun (TC-AC-RP-400) tetap bermakna walau bagian sebelumnya gagal keras; semua blok berada dalam satu topik "target berubah antara render dan submit" tanpa kelas harness lain, tiap blok membuka halaman dari awal dan memulihkan datanya sendiri.
- P-1: asersi "tanpa entri log tambahan" pada TC-AC-RP-398 ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state peran yang baru diubah Sesi B; spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05). Baseline: jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console pelaku (langkah 5) sebelum aksi Sesi A, dibaca lewat kemampuan baca yang disediakan tim FE/BE; asersi di langkah 9 dan 10.
- Temuan untuk QA:
  - TC-AC-RP-398 sampai 401 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua (spec dipindah ke kelas c).
  - TC-AC-RP-398 sampai 401 tidak menyebut akun Sesi B; spec memakai sesi API akun `Siti Nurhaliza` (Pre-setup #24 hanya menyebut "dua sesi paralel Total Control", S-13).
  - TC-AC-RP-398: Expected menyebut surface Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console dengan selisih 0; spec mengasersi keduanya (langkah 9 dan 10) terhadap baseline langkah 5, yang dicatat sesudah pemicu Sesi B sehingga entri Sesi B tidak dihitung.
  - TC-AC-RP-399: langkah TC "Sesi A Remove baris yang sama dan konfirmasi" tidak menyebut aksi baris di Approvers Section; spec menulis `Remove` pada menu `⋯` baris approver. Mohon konfirmasi label aksi baris approver.
  - TC-AC-RP-401: Expected "Aksi diproses terhadap status saat submit; auto-revert berlaku mengikuti status Total Control `John Dohan` saat submit" tidak menyebut hal yang teramati; spec mengasersi checkbox C kembali tercentang dan tingkat akses `John Dohan` tetap Total Control.
  - TC-AC-RP-400: Expected "Perubahan ditolak 403 ... data di-refresh" tidak menyebut pesan atau toast; spec mengasersi status respons permintaan perubahan yang diamati di browser, nilai checkbox, dan data Role Detail.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
