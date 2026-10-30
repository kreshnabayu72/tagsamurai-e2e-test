---
id: TC-GS-ACTLOG-E2E-037-aksi-relasi-hardware-user-action-pair-assign-dan-add-access
title: "Aksi Relasi Hardware di User Action: Pair/Unpair TAG, Assign/Unassign Handheld, Add/Remove Access, Audit TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-145
  - TC-GS-ACTLOG-148
  - TC-GS-ACTLOG-206
coverage:
  web: automated
---

# Aksi Relasi Hardware di User Action: Pair/Unpair TAG, Assign/Unassign Handheld, Add/Remove Access, Audit TAG

## Prerequisites

- Mode: FE+BE.
- Akun pembaca log: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku aksi sumber (sesi API, fixture baru): Admin `Hendra Pratama` (`Fixture.activityLog.adminHendra`, email ditetapkan tim FE, kredensial `Spectra.env.GS_HENDRA_PASSWORD`, env baru); Modified By tampil `Hendra P`. Sesi API dibuka di hook `before` dan ditutup di hook `after`. Admin ini melakukan semua aksi relasi di modul User (TC-GS-ACTLOG-145 dan 148) dan sesi Audit TAG di All TAGs (TC-GS-ACTLOG-206).
- Data Dinamis (bersuffix `{runId}-037`):
  - User `Siti Nurbaya {runId}-037` (email `sitinurbaya+{runId}-037@qwertysystem.net`, nilai field wajib lain dari `Fixture.activityLog.userDasar`, fixture baru berisi Position, Employee ID, dan field wajib lain di luar Name, email, dan Division) di-seed lewat API di hook `before`.
  - Satu TAG, satu Handheld, dan satu akses produk milik Client A (`Fixture.activityLog.tagUji`, `Fixture.activityLog.handheldUji`, `Fixture.activityLog.aksesProdukUji`; fixture baru) disiapkan tim FE dan hanya dipakai spec ini.
  - Satu TAG untuk sesi Audit TAG (`Fixture.activityLog.tagAuditUji`, fixture baru) di-seed lewat API di hook `before` dan dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): simulasi hardware untuk memasangkan TAG (Pair TAG), meng-assign Handheld pada user, melepasnya kembali, dan menjalankan satu sesi Audit TAG di Global Settings > All TAGs; mekanisme simulasinya tidak ditulis di TC, PRD, atau LLD. Tambah dan hapus akses produk (Add Access, Remove Access) lewat modul User. Changelog modul User dan modul All TAGs dapat dibaca dari UI Total Control Client A untuk perbandingan.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: relasi TAG, Handheld, dan akses milik user uji. Hook `after` melepas relasi yang tersisa dan menghapus user dan TAG uji; pembersihan tidak berasumsi seeding berhasil penuh. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-145: Aksi relasi dibuat dari modul User, Pair TAG, Assign Handheld, Add Access

1. Sebagai admin Hendra Pratama (sesi API), pasangkan TAG, assign Handheld, dan tambah akses produk pada user `Siti Nurbaya {runId}-037` di modul User
2. Buka Global Settings > Activity Log > Tab "User Action", ketik Search `Siti Nurbaya {runId}-037`, tekan Enter
3. Verifikasi entri `Pair TAG` tampil
4. Verifikasi entri `Assign Handheld` tampil
5. Verifikasi entri `Add Access` tampil
6. Catat Object, Name, Field, Old Value, dan New Value ketiga entri, lalu buka Changelog user `Siti Nurbaya {runId}-037` di modul User dan baca baris Pair TAG, Assign Handheld, dan Add Access
7. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Pair TAG` identik dengan baris Changelog modul sumber untuk aksi yang sama
8. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Assign Handheld` identik dengan baris Changelog modul sumber untuk aksi yang sama
9. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Add Access` identik dengan baris Changelog modul sumber untuk aksi yang sama

### Pemulihan state antar TC

10. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-148: Aksi relasi dilepas dari modul User, Unpair TAG, Unassign Handheld, Remove Access

11. Sebagai admin Hendra Pratama (sesi API), lepas TAG, unassign Handheld, dan hapus akses produk dari user `Siti Nurbaya {runId}-037` di modul User
12. Ketik Search `Siti Nurbaya {runId}-037`, tekan Enter
13. Verifikasi entri `Unpair TAG` tampil
14. Verifikasi entri `Unassign Handheld` tampil
15. Verifikasi entri `Remove Access` tampil
16. Catat Object, Name, Field, Old Value, dan New Value ketiga entri, lalu buka Changelog user `Siti Nurbaya {runId}-037` di modul User dan baca baris Unpair TAG, Unassign Handheld, dan Remove Access
17. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Unpair TAG` identik dengan baris Changelog modul sumber untuk aksi yang sama
18. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Unassign Handheld` identik dengan baris Changelog modul sumber untuk aksi yang sama
19. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Remove Access` identik dengan baris Changelog modul sumber untuk aksi yang sama

### Pemulihan state antar TC

20. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-206: Aksi di modul TAG Registry tercatat di Tab User Action

21. Sebagai admin Hendra Pratama (sesi API), jalankan satu sesi Audit TAG untuk TAG `Fixture.activityLog.tagAuditUji` di Global Settings > All TAGs
22. Buka Changelog modul All TAGs dan catat baris aksi Audit TAG (Object, Name, Field, Old Value, New Value, dan Date)
23. Buka Global Settings > Activity Log > Tab "User Action", klik icon Filter, pilih Action `Audit TAG`, klik [Apply]
24. Verifikasi entri dengan Action `Audit TAG` tampil sebagai baris teratas (Date terbaru di atas)
25. Verifikasi Object, Name, Field, Old Value, dan New Value entri itu identik dengan baris Changelog modul sumber untuk aksi yang sama
26. Verifikasi Modified By entri itu `Hendra P`
27. Verifikasi Date entri itu identik dengan Date baris Changelog aksi Audit TAG yang sama

### Pemulihan state akhir

28. Klik icon Filter, klik [Clear Field], klik [Apply]

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Kelas harness d (hardware): TC-GS-ACTLOG-145 dan 148 berbagi user, TAG, dan Handheld yang sama, sehingga TC-GS-ACTLOG-148 melepas relasi yang dibuat TC-GS-ACTLOG-145; TC-GS-ACTLOG-206 memakai simulasi hardware yang sama untuk sesi Audit TAG.
- TC-GS-ACTLOG-206 ada di spec 037.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 11, dan 21 (aksi sumber oleh admin lewat sesi API), langkah 6, 16, dan 22 (mencatat nilai entri lalu membaca Changelog modul sumber sebagai pembanding), dan langkah pemulihan 10, 20, dan 28.
- Klausa Expected "entri tampil" dan "kolom identik dengan Changelog" dipisah (S-01); kolom Object, Name, Field, Old Value, New Value satu entri dijadikan satu `Verifikasi` karena daftarnya disebut utuh.
- Entri dicari lewat Search Name bersuffix (baseline nol, S-12). Entri Audit TAG tidak punya Name yang disebut TC: dicari lewat Filter Action `Audit TAG`, diambil dari baris teratas, dan Date-nya dibandingkan dengan Date baris Changelog aksi yang sama.
- Activity Log dibuka kembali lewat menu sidebar (state default) sesudah mengunjungi modul lain, dan Search diketik ulang.
- Temuan untuk QA:
  - State kotak Search saat user keluar dari halaman Activity Log lalu kembali belum ditetapkan PRD; spec tidak mengandalkannya.
  - Env baru `GS_HENDRA_PASSWORD` perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; email dan role admin Hendra Pratama ditetapkan tim FE.
  - TC menulis subjek `Siti Nurbaya` literal; spec memakai nama bersuffix.
  - TC tidak menjelaskan cara menyimulasikan hardware (Pair TAG, Assign Handheld, Audit TAG); kebutuhannya dicatat di Prerequisites dan tidak ada endpoint yang dikarang.
  - TC-206 tidak menyebut perangkat, jumlah TAG, maupun Name entri sesi Audit TAG, dan tidak menyebut lokasi Changelog modul All TAGs; bila modul tidak punya Changelog, Expected "identik dengan baris Changelog modul sumber" tidak dapat diverifikasi.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah 28 mengikuti pola TC.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
