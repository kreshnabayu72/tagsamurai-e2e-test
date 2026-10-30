---
id: TC-GS-ACTLOG-E2E-055-sumber-user-action-position-division-non-login-user
title: "Sumber User Action: Position, Division, Non-Login User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-207
  - TC-GS-ACTLOG-208
  - TC-GS-ACTLOG-209
coverage:
  web: automated
---

# Sumber User Action: Position, Division, Non-Login User

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture. Akun ini membaca Changelog dan Activity Log; aksi sumber tidak dijalankan olehnya.
- Akun pelaku aksi sumber: admin `Hendra Pratama` (Client A), `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), kredensial `Spectra.env.GS_HENDRA_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Semua aksi sumber (buat Position, Division, dan Non-Login User) dijalankan lewat sesi API admin ini; kemampuan itu dan kapabilitas Create Position, Division, dan Non-Login User disediakan tim FE/BE tanpa mengarang endpoint. Nilai Modified By yang diasersi `Hendra P`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup: tidak ada data tetap yang diubah atau dipakai sebagai target aksi. Login User Active `Sari Dewi` (akun pengamat) hanya dipilih sebagai Represented By pada Non-Login User dan tidak diubah.
- Data Dinamis (bersuffix per run, dibersihkan di hook `after` tanpa berasumsi seeding atau pembuatan berhasil):
  - Position `Warehouse Staff {runId}-055`: dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-207; dihapus lewat API di hook `after`. Position hanya memiliki field `Position Name`.
  - Division `Finance {runId}-055` dengan Code dikosongkan (di-generate otomatis, `DIV-LOGIC-04`): dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-208; dihapus lewat API di hook `after`.
  - Non-Login User `Budi Kurniawan {runId}-055` (First Name `Budi`, Last Name `Kurniawan {runId}-055`, email `budikurniawan+{runId}-055@qwertysystem.net`, Division `Operations {runId}-055`, Employee ID dikosongkan, bukan Temporary, Represented By `Sari Dewi`): dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-209; dihapus lewat API di hook `after`.
  - Division `Operations {runId}-055`: di-seed lewat API di hook `before` sebagai Division wajib Non-Login User; dihapus lewat API di hook `after` sesudah Non-Login User dihapus.
- Kemampuan teknis: akses baca Changelog modul Position, Division, dan Non-Login User untuk menyalin baris Changelog aksi yang sama beserta kolom Date.
- Spec hanya menambah baris log. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-207: Aksi di modul Position tercatat di Tab User Action

1. Lewat sesi API admin `Hendra Pratama`, buat Position `Warehouse Staff {runId}-055` dan tunggu respons sukses
2. Buka Changelog modul Position dan catat baris Changelog aksi Create untuk `Warehouse Staff {runId}-055` (Object, Name, Field, Old Value, New Value, Date)
3. Buka Global Settings > Activity Log > User Action
4. Ketik Search `Warehouse Staff {runId}-055`, tekan Enter
5. Verifikasi entri dengan Action `Create` untuk `Warehouse Staff {runId}-055` tampil
6. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Position yang dicatat pada langkah 2
7. Verifikasi Modified By entri `Hendra P`
8. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 2

### Pemulihan state antar TC

9. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-208: Aksi di modul Division tercatat di Tab User Action

10. Lewat sesi API admin `Hendra Pratama`, buat Division `Finance {runId}-055` dan tunggu respons sukses
11. Buka Changelog modul Division dan catat baris Changelog aksi Create untuk `Finance {runId}-055` (Object, Name, Field, Old Value, New Value, Date)
12. Buka Global Settings > Activity Log > User Action
13. Ketik Search `Finance {runId}-055`, tekan Enter
14. Verifikasi entri dengan Action `Create` untuk `Finance {runId}-055` tampil
15. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Division yang dicatat pada langkah 11
16. Verifikasi Modified By entri `Hendra P`
17. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 11

### Pemulihan state antar TC

18. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-209: Aksi di modul Non-Login User tercatat di Tab User Action

19. Lewat sesi API admin `Hendra Pratama`, buat Non-Login User `Budi Kurniawan {runId}-055` dan tunggu respons sukses
20. Buka Changelog modul Non-Login User dan catat baris Changelog aksi Create untuk `Budi Kurniawan {runId}-055` (Object, Name, Field, Old Value, New Value, Date)
21. Buka Global Settings > Activity Log > User Action
22. Ketik Search `Budi Kurniawan {runId}-055`, tekan Enter
23. Verifikasi entri dengan Action `Create` untuk `Budi Kurniawan {runId}-055` tampil
24. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Non-Login User yang dicatat pada langkah 20
25. Verifikasi Modified By entri `Hendra P`
26. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 20

### Pemulihan state akhir spec

27. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 11, dan 20 (membaca baris Changelog modul sumber sebagai pembanding Expected "identik dengan baris Changelog" dan Date); langkah 9, 18, dan 27 (membersihkan Search). Aksi sumber lewat API menunggu respons sukses sebelum langkah berikutnya (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline entri adalah nol karena nama subjek bersuffix unik per run (S-12).
- Pembagian TC lintas spec: TC-GS-ACTLOG-199, 200, dan 201 ada di spec 052; TC-GS-ACTLOG-202, 203, 204, dan 210 di spec 053; TC-GS-ACTLOG-205 di spec 054; TC-GS-ACTLOG-206 ada di spec 037.
- Temuan untuk QA:
  - Email admin `Hendra Pratama` (Modified By `Hendra P`) dan cara menjalankan aksi lewat sesi API ditetapkan tim FE (fixture `Fixture.activityLog.adminHendra`).
  - Aksi Create menghasilkan satu baris per field (TC-GS-ACTLOG-144), sedangkan Expected TC menyebut satu "entri"; spec membandingkan seluruh baris hasil aksi dengan Changelog.
  - TC-GS-ACTLOG-209 tidak menyebut nilai field wajib Non-Login User selain nama (Division, email, Represented By); spec memakai nilai yang tertulis di Data Dinamis sebagai data pendukung (PRD non-login-user `FLD-02` sampai `FLD-08`).
  - TC-GS-ACTLOG-207 dan 208 menyebut nama literal (`Warehouse Staff`, `Finance`); spec memakai nama bersuffix per run dan mengasersi nama bersuffix yang sama.
