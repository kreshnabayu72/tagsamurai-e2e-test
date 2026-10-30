---
id: TC-GS-ACTLOG-E2E-036-pola-entri-user-action-create-edit-delete-dan-satu-save-banyak-field
title: "Pola Entri User Action: Create, Edit, Delete, dan Satu Save Banyak Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-141
  - TC-GS-ACTLOG-142
  - TC-GS-ACTLOG-143
  - TC-GS-ACTLOG-144
coverage:
  web: automated
---

# Pola Entri User Action: Create, Edit, Delete, dan Satu Save Banyak Field

## Prerequisites

- Mode: FE+BE.
- Akun pembaca log: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku aksi sumber (sesi API, fixture baru; email dan role ditetapkan tim FE):
  - Admin `Hendra Pratama` (`Fixture.activityLog.adminHendra`, kredensial `Spectra.env.GS_HENDRA_PASSWORD`, env baru): pelaku TC-GS-ACTLOG-141, 142, dan 144; Modified By tampil `Hendra P`.
  - Admin `Wulan` (`Fixture.activityLog.adminWulan`, kredensial `Spectra.env.GS_WULAN_PASSWORD`, env baru): pelaku TC-GS-ACTLOG-143; Modified By tampil `Wulan`.
  - Sesi API kedua admin dibuka di hook `before` dan ditutup di hook `after`.
- Data Dinamis (dibuat spec, bersuffix `{runId}-036`):
  - User `John Doe {runId}-036` (email `johndoe+{runId}-036@qwertysystem.net`, nilai field wajib lain dari `Fixture.activityLog.userDasar`, fixture baru berisi Position, Employee ID, dan field wajib lain di luar Name, email, dan Division) dibuat sebagai aksi Create pada langkah TC-GS-ACTLOG-141.
  - Division `Marketing {runId}-036` dan `Finance {runId}-036` di-seed lewat API di hook `before`.
  - User `Siti Nurbaya {runId}-036` (email `sitinurbaya+{runId}-036@qwertysystem.net`, Division `Marketing {runId}-036`) di-seed lewat API di hook `before`.
  - Brand `Acme Corp {runId}-036` di-seed lewat API di hook `before` dan dihapus oleh Wulan pada langkah TC-GS-ACTLOG-143.
  - Nama bersuffix dipakai agar asersi mengidentifikasi entri lewat Name unik (baseline nol).
- Nilai General Settings untuk TC-GS-ACTLOG-144: `Fixture.activityLog.currencyCodeBaru`, `Fixture.activityLog.timeZoneBaru`, dan `Fixture.activityLog.dateFormatBaru` (fixture baru; masing-masing berbeda dari nilai awal environment). Hook `before` mencatat nilai awal Currency Code, Time Zone, dan Date Format.
- Kemampuan teknis (disediakan tim FE/BE): sesi API admin untuk Create User, Edit Division user, Delete Brand, dan Save General Settings; Changelog modul User dan Brand dapat dibaca dari UI Total Control Client A untuk perbandingan (TC-GS-ACTLOG-141, 143).
- Guided Tooltip: hook suite before/after menyetel flag seen untuk halaman Activity Log (lihat suite.md). Hook before/after spec ini juga menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman Changelog modul User dan Brand yang dibuka pada langkah 6 dan 20 (kemampuan disediakan tim FE/BE).
- Entri awal (hook `before`, sebelum langkah 23): admin Hendra Pratama (sesi API) mengubah satu nilai General Settings (mis. Session Idle Timeout ke nilai lain yang valid, disediakan tim FE/BE) sehingga ada baris Object `General Settings` dan opsi itu ada di Filter Panel. Save dengan nilai yang sama adalah no-op tanpa baris log, sehingga tidak dipakai sebagai seed. Hook `after` memulihkan nilai itu (pemulihan menambah baris log, wajar). Entri log tidak dapat dihapus; asersi memakai selisih jumlah baris sehingga tahan baris dari run lain.
- Cara baca jumlah baris (langkah 23 dan 26): PRD tidak punya indikator total baris, sehingga yang dihitung adalah baris yang tampil. Klik menu Activity Log di sidebar mengembalikan ukuran halaman ke default 10 (PRD FI-06), sehingga langkah 23 dan 25 mengatur jumlah baris per halaman ke 100 (pilihan 10/25/50/100) sebagai aksi sebelum baris dibaca; ukuran halaman setelah [Apply] tidak ditetapkan PRD. Hasil dipersempit dengan Filter Object `General Settings`, Modified By `Hendra Pratama`, dan Date dari kemarin sampai hari ini (rentang menutupi pergeseran jendela hari akibat perubahan Time Zone di langkah 24) supaya jumlah baris hasil kurang dari satu halaman (diasumsikan di bawah 100 baris per rentang itu; jaminan tim FE/BE lewat entri log hasil run sebelumnya tetap ada karena log tidak dapat dihapus).
- State global yang diubah: Currency Code, Time Zone, Date Format, dan Session Idle Timeout di General Settings (TC-GS-ACTLOG-144 untuk tiga yang pertama; Session Idle Timeout diubah oleh entri awal hook `before` dan nilai awalnya dicatat). Hook `after` memulihkan keempatnya ke nilai awal lewat API, sehingga menambah entri Edit General Settings di log (tiga untuk Currency Code, Time Zone, Date Format, ditambah satu entri pemulihan Session Idle Timeout) dan mengubah Last Updated General Settings. Suite berjalan serial (`parallel: false`). Hook `after` menghapus User, Division, dan Brand yang tersisa milik spec ini.

## Test Steps

### TC-GS-ACTLOG-141: Entri Create, Old Value kosong dan New Value berisi nilai field

1. Sebagai admin Hendra Pratama (sesi API), buat user `John Doe {runId}-036` lewat modul User
2. Buka Global Settings > Activity Log > Tab "User Action", ketik Search `John Doe {runId}-036`, tekan Enter
3. Verifikasi baris menampilkan Action `Create`, Object `User`, dan Name `John Doe {runId}-036`
4. Verifikasi Old Value tampil `—`
5. Verifikasi Modified By tampil `Hendra P`
6. Catat Field dan New Value baris itu, lalu buka Changelog user `John Doe {runId}-036` di modul User dan baca baris Create-nya
7. Verifikasi Field dan New Value baris Activity Log identik dengan baris Changelog modul User untuk aksi Create yang sama

### Pemulihan state antar TC

8. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-142: Entri Edit, Field, Old Value, dan New Value terisi

9. Sebagai admin Hendra Pratama (sesi API), ubah Division user `Siti Nurbaya {runId}-036` dari `Marketing {runId}-036` menjadi `Finance {runId}-036` lewat modul User
10. Ketik Search `Siti Nurbaya {runId}-036`, tekan Enter
11. Verifikasi baris menampilkan Action `Edit`, Object `User`, Name `Siti Nurbaya {runId}-036`, dan Field `Division`
12. Verifikasi Old Value `Marketing {runId}-036` dan New Value `Finance {runId}-036`
13. Verifikasi Modified By tampil `Hendra P`

### Pemulihan state antar TC

14. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-143: Entri Delete, New Value kosong

15. Sebagai admin Wulan (sesi API), hapus Brand `Acme Corp {runId}-036` lewat modul Brand
16. Ketik Search `Acme Corp {runId}-036`, tekan Enter
17. Verifikasi baris menampilkan Action `Delete`, Object `Brand`, dan Name `Acme Corp {runId}-036`
18. Verifikasi New Value tampil `—`
19. Verifikasi Modified By tampil `Wulan`
20. Catat Field dan Old Value baris itu, lalu buka Changelog modul Brand dan baca baris Delete untuk `Acme Corp {runId}-036`
21. Verifikasi Field dan Old Value baris Activity Log identik dengan baris Changelog modul Brand untuk aksi Delete yang sama

### Pemulihan state antar TC

22. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-144: Satu Save yang mengubah tiga field menghasilkan tiga entri terpisah

23. Pada Tab "User Action" klik icon Filter, pilih Object `General Settings`, Modified By `Hendra Pratama`, dan Date dari kemarin sampai hari ini, klik [Apply], atur jumlah baris per halaman ke 100, lalu hitung baris yang tampil sebagai baseline B144
24. Sebagai admin Hendra Pratama (sesi API), ubah Currency Code, Time Zone, dan Date Format di Global Settings > General Settings ke `Fixture.activityLog.currencyCodeBaru`, `Fixture.activityLog.timeZoneBaru`, dan `Fixture.activityLog.dateFormatBaru` dalam satu Save
25. Klik icon Filter, klik [Apply] untuk memuat ulang hasil Filter, lalu atur jumlah baris per halaman ke 100
26. Verifikasi jumlah baris yang tampil pada hasil Filter (ukuran halaman 100) bertambah tepat tiga dari B144 dengan Action `Edit` Object `General Settings`, satu baris per field yang berubah
27. Verifikasi tiga baris pertama hasil Filter (urutan default, Date terbaru di atas) adalah baris Edit dengan Field `Currency Code` ber-New Value `Fixture.activityLog.currencyCodeBaru`, Field `Time Zone` ber-New Value `Fixture.activityLog.timeZoneBaru`, dan Field `Date Format` ber-New Value `Fixture.activityLog.dateFormatBaru` (diasersi sebagai himpunan; urutan di antara ketiga baris yang ber-Date sama tidak diasersi; baris run sebelumnya dengan Field dan New Value yang sama berada di bawah ketiga baris ini karena Date-nya lebih lama)
28. Verifikasi ketiga baris pada langkah 27 memiliki Date identik

### Pemulihan state akhir

29. Klik icon Filter, klik [Clear Field], klik [Apply]

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. TC-GS-ACTLOG-141 sampai 144 dipertahankan urutannya.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 9, 15, dan 24 (aksi sumber oleh admin lewat sesi API), langkah 23 (baseline jumlah baris sesuai S-12), langkah 25 (memuat ulang hasil Filter), langkah 6 dan 20 (mencatat nilai baris log lalu membaca Changelog modul sumber sebagai pembanding), dan langkah pemulihan 8, 14, 22, dan 29.
- Aksi sumber dijalankan spec sendiri lewat sesi API admin supaya baris log tercipta lewat aksi nyata; TC menulisnya sebagai Precondition. Save General Settings (langkah 24) lewat sesi API selesai sinkron sehingga tidak memakai langkah tunggu aksi.
- Baris dicari lewat Search Name bersuffix (baseline nol, S-12) dan baseline jumlah baris untuk General Settings (Filter Object, Modified By, dan Date dari kemarin sampai hari ini, ukuran halaman 100 diatur pada langkah 23 dan 25; baris yang tampil dihitung karena PRD tidak punya indikator total), bukan jam runner. Langkah 27 memakai posisi hanya sebagai tiga baris pertama pada urutan default (Date terbaru di atas), diasersi sebagai himpunan. Modified By diasersi sebelum membuka Changelog karena Changelog berada di modul lain.
- Activity Log dibuka kembali lewat menu sidebar (state default) sesudah mengunjungi modul lain, dan Search diketik ulang.
- Temuan untuk QA:
  - State kotak Search saat user keluar dari halaman Activity Log lalu kembali belum ditetapkan PRD; spec tidak mengandalkannya.
  - Ukuran halaman tabel sesudah [Apply] belum ditetapkan PRD (klik menu sidebar mengembalikan ke 10, FI-06); spec mengatur 100 sebagai aksi pada langkah 23 dan 25.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah 25 dan 29 yang mengklik icon Filter sesudah [Apply] mengikuti pola TC dan bergantung pada perilaku itu.
  - Env baru `GS_HENDRA_PASSWORD` dan `GS_WULAN_PASSWORD` perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; email dan role admin Hendra Pratama dan Wulan ditetapkan tim FE.
  - TC memakai subjek `John Doe`, `Siti Nurbaya`, `Acme`, Division `Marketing` dan `Finance` literal; spec memakai nama bersuffix. Data Dinamis TC menulis Division awal `Siti Nurbaya` sebagai `Operations` sedangkan TC-142 mengubahnya dari `Marketing`; spec mengikuti TC-142.
  - TC-144 dan TC-149 menulis jumlah baris tanpa menyebut cara menghitung pada tabel berpaginasi, dan PRD Activity Log tidak punya indikator total; spec menghitung baris yang tampil pada ukuran halaman 100 setelah hasil dipersempit (pilihan spec; pemilik TC dan PRD perlu menetapkan cara baca atau indikator total).
  - TC-144 tidak menyebut aktor perubah General Settings; spec memakai Admin `Hendra Pratama`.
  - TC-144 tidak menyebut nilai baru Currency Code, Time Zone, dan Date Format; spec memakai fixture baru yang harus disediakan tim FE.
  - Post Condition semua TC bernilai `-`; tidak ada yang diasersi.
