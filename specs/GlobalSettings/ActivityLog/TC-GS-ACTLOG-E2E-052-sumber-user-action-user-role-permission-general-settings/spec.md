---
id: TC-GS-ACTLOG-E2E-052-sumber-user-action-user-role-permission-general-settings
title: "Sumber User Action: User, Role dan Permission, General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-199
  - TC-GS-ACTLOG-200
  - TC-GS-ACTLOG-201
coverage:
  web: automated
---

# Sumber User Action: User, Role dan Permission, General Settings

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture. Akun ini membaca Changelog dan Activity Log; aksi sumber tidak dijalankan olehnya.
- Akun pelaku aksi sumber: admin `Hendra Pratama` (Client A), `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), kredensial `Spectra.env.GS_HENDRA_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Semua aksi sumber (buat user, assign ke tab Total Control, ubah Time Zone, pulihkan Time Zone) dijalankan lewat sesi API admin ini; kemampuan itu dan kapabilitas Create/Edit di modul User, Role & Permission, dan General Settings disediakan tim FE/BE tanpa mengarang endpoint. Nilai Modified By yang diasersi `Hendra P`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup: Time Zone General Settings Client A bernilai `(UTC+07:00) Bangkok, Hanoi, Jakarta` (hook `before` menyetelnya bila berbeda). Spec mengubah Time Zone General Settings (Pre-setup bersama) sehingga Last Updated General Settings berubah; nilai Time Zone dipulihkan, Last Updated tidak dipulihkan.
- Data Dinamis (bersuffix per run, seed di hook `before`, dibersihkan di hook `after` tanpa berasumsi seeding berhasil penuh):
  - Division `Operations {runId}-052` dan Position `Staff {runId}-052`: di-seed lewat API; dipakai sebagai field wajib saat membuat `John Doe {runId}-052`; dihapus lewat API setelah user dihapus.
  - `John Doe {runId}-052` dengan email `johndoe+{runId}-052@qwertysystem.net`, Employee ID `EMP001-{runId}-052`, Position `Staff {runId}-052`, Division `Operations {runId}-052`: dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-199; dihapus lewat API di hook `after`.
  - `Siti Nurbaya {runId}-052` dengan email `sitinurbaya+{runId}-052@qwertysystem.net`, Division `Operations {runId}-052`: di-seed lewat API (tanpa Position, bukan anggota Total Control); dihapus lewat API di hook `after`.
- Kemampuan teknis: akses baca Changelog user di modul User, `Changelog: Role & Permission` pada tab Total Control, dan Changelog General Settings untuk menyalin baris Changelog aksi yang sama beserta kolom Date.
- State global yang diubah: keanggotaan `Siti Nurbaya {runId}-052` di tab Total Control (TC-GS-ACTLOG-200) dan Time Zone General Settings (TC-GS-ACTLOG-201). Pemulihan: langkah pemulihan terakhir mengembalikan Time Zone ke `(UTC+07:00) Bangkok, Hanoi, Jakarta`; hook `after` menjadi cadangan untuk Time Zone dan mengeluarkan `Siti Nurbaya {runId}-052` dari tab Total Control sebelum menghapus user.
- Suite serial (`parallel: false`) karena spec mengubah Time Zone General Settings dan menambah baris log.

## Test Steps

### TC-GS-ACTLOG-199: Aksi di modul User tercatat di Tab User Action

1. Lewat sesi API admin `Hendra Pratama`, buat user `John Doe {runId}-052` (email `johndoe+{runId}-052@qwertysystem.net`, Employee ID `EMP001-{runId}-052`, Position `Staff {runId}-052`, Division `Operations {runId}-052`) dan tunggu respons sukses
2. Buka Changelog user `John Doe {runId}-052` di modul User dan catat baris Changelog aksi Create (Object, Name, Field, Old Value, New Value, Date)
3. Buka Global Settings > Activity Log > User Action
4. Ketik Search `John Doe {runId}-052`, tekan Enter
5. Verifikasi entri dengan Action `Create` untuk `John Doe {runId}-052` tampil
6. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul User yang dicatat pada langkah 2
7. Verifikasi Modified By entri `Hendra P`
8. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 2

### Pemulihan state antar TC

9. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-200: Aksi di modul Role & Permission tercatat di Tab User Action

10. Lewat sesi API admin `Hendra Pratama`, tambahkan user `Siti Nurbaya {runId}-052` ke tab Total Control di Role & Permission dan tunggu respons sukses
11. Buka `Changelog: Role & Permission` pada tab Total Control dan catat baris Changelog aksi Assign untuk `Siti Nurbaya {runId}-052` (Object, Name, Field, Old Value, New Value, Date)
12. Buka Global Settings > Activity Log > User Action
13. Ketik Search `Siti Nurbaya {runId}-052`, tekan Enter
14. Verifikasi entri dengan Action `Assign` untuk `Siti Nurbaya {runId}-052` tampil
15. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog Role & Permission yang dicatat pada langkah 11
16. Verifikasi Modified By entri `Hendra P`
17. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 11

### Pemulihan state antar TC

18. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-201: Aksi di modul General Settings tercatat di Tab User Action

19. Buka Global Settings > Activity Log > User Action
20. Ketik Search `Time Zone`, tekan Enter, lalu catat jumlah entri hasil Search sebagai baseline
21. Klik `(←)` pada kotak Search
22. Lewat sesi API admin `Hendra Pratama`, ubah Time Zone General Settings dari `(UTC+07:00) Bangkok, Hanoi, Jakarta` menjadi `(UTC+08:00) Kuala Lumpur, Singapore, Makassar` dan tunggu respons sukses
23. Buka Changelog modul General Settings dan catat baris Changelog aksi Edit Time Zone (Object, Name, Field, Old Value, New Value, Date)
24. Buka Global Settings > Activity Log > User Action
25. Ketik Search `Time Zone`, tekan Enter
26. Verifikasi entri dengan Action `Edit` baru tampil (jumlah entri hasil Search bertambah dari baseline pada langkah 20)
27. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul General Settings yang dicatat pada langkah 23
28. Verifikasi Modified By entri `Hendra P`
29. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 23, keduanya dalam zona waktu tampilan `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`

### Pemulihan state akhir spec

30. Klik `(←)` pada kotak Search
31. Lewat sesi API admin `Hendra Pratama`, kembalikan Time Zone General Settings ke `(UTC+07:00) Bangkok, Hanoi, Jakarta` dan tunggu respons sukses

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 11, dan 23 (membaca baris Changelog modul sumber sebagai pembanding Expected "identik dengan baris Changelog" dan Date); langkah 20 dan 21 (baseline jumlah entri `Time Zone`, S-12); langkah 9, 18, 21, dan 30 (membersihkan Search); langkah 31 (pemulihan Time Zone). Aksi sumber lewat API menunggu respons sukses sebelum langkah berikutnya (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline TC-GS-ACTLOG-199 dan 200 adalah nol karena nama subjek bersuffix unik per run; TC-GS-ACTLOG-201 memakai baseline jumlah entri karena Search `Time Zone` tidak unik per run.
- TC-GS-ACTLOG-201 paling akhir karena mengubah Time Zone yang memengaruhi tampilan Date di Activity Log.
- Pembagian TC lintas spec: TC-GS-ACTLOG-202, 203, 204, dan 210 ada di spec 053; TC-GS-ACTLOG-205 di spec 054; TC-GS-ACTLOG-206 ada di spec 037; TC-GS-ACTLOG-207, 208, dan 209 di spec 055.
- Temuan untuk QA:
  - Email admin `Hendra Pratama` (Modified By `Hendra P`) dan cara menjalankan aksi lewat sesi API ditetapkan tim FE (fixture `Fixture.activityLog.adminHendra`).
  - Aksi Create dan Edit menghasilkan satu baris per field (TC-GS-ACTLOG-144), sedangkan Expected TC menyebut satu "entri"; spec membandingkan seluruh baris hasil aksi dengan Changelog.
  - TC tidak menyebut lokasi baris Changelog modul User, Role & Permission, dan General Settings; spec membaca Changelog user, `Changelog: Role & Permission` tab Total Control, dan Changelog General Settings.
  - TC-GS-ACTLOG-200 dan 201 tidak menyebut Name atau Field entri (Name pada Assign, Field pada Edit Time Zone); spec mencari entri lewat Search dengan nama user subjek dan `Time Zone`. Mohon konfirmasi kolom yang dicakup Search.
  - TC-GS-ACTLOG-199 tidak menentukan Position dan Division `John Doe` (Data Dinamis TC menyebut EMP001, Staff, Marketing); spec memakai Division dan Position milik spec sebagai field wajib karena nilai itu bukan objek uji.
