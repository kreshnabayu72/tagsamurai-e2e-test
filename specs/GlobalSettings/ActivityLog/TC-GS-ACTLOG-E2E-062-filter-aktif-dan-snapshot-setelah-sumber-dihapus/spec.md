---
id: TC-GS-ACTLOG-E2E-062-filter-aktif-dan-snapshot-setelah-sumber-dihapus
title: "Filter Aktif dan Snapshot Setelah Sumber Dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-55
  - TC-GS-ACTLOG-80
  - TC-GS-ACTLOG-169
coverage:
  web: automated
---

# Filter Aktif dan Snapshot Setelah Sumber Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): akun aktor utama, login di hook `before`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
  - Total Control Client A admin kedua `totalControlSecond_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC2_PASSWORD`; fixture sudah terdaftar di `.env.example`): dipakai lewat sesi API hanya untuk menghapus user target pada TC-GS-ACTLOG-80 dan 169 (pemicu state target, bukan objek asersi); kemampuan sesi API admin kedua disediakan tim FE/BE.
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A (aktor utama) dan halaman `Global Settings > Activity Log` serta `Global Settings > User` (kemampuan disediakan tim FE/BE). Admin kedua dan subjek hanya dipakai lewat sesi API atau Auth tanpa membuka halaman UI, sehingga tidak perlu flag.
- Data Pre-setup: tidak ada data tetap yang diubah atau dipakai sebagai target aksi. Admin bersama `Fixture.activityLog.adminWulan` (dan `Fixture.activityLog.adminHendra`) tidak dihapus dan tidak diubah oleh spec ini.
- Data Dinamis (semua milik spec, bersuffix per run; dibuat lewat API di hook `before`; dibersihkan di hook `after` tanpa berasumsi seeding berhasil penuh):
  - Subjek TC-GS-ACTLOG-80: user `Budi Anwar {runId}-062` (First Name `Budi`, Last Name `Anwar {runId}-062`, email `budianwar+{runId}-062@qwertysystem.net`) yang sudah login lewat alur Auth sehingga entri Login tercatat di Tab Session.
  - Subjek TC-GS-ACTLOG-169: admin `Wulan` (email `wulan+{runId}-062@qwertysystem.net`) dengan System Role berkapabilitas Create Brand tanpa access level (bukan Total Control, supaya dapat dihapus oleh admin lain), yang membuat Brand `Brand Wulan {runId}-062` lewat API sehingga entri `Create` dengan Modified By `Wulan` tercatat di Tab User Action. Nama `Wulan` literal tanpa suffix karena asersi dan opsi filter Modified By memakai nilai itu; admin target hapus dibedakan dari admin bersama `Fixture.activityLog.adminWulan` lewat email bersuffix dan Brand bersuffix.
  - Subjek TC-GS-ACTLOG-55: user `Budi Anwar {runId}-062-b` (First Name `Budi`, Last Name `Anwar {runId}-062-b`, email `budianwar+{runId}-062-b@qwertysystem.net`, Employee ID `EMP002-{runId}-062`, Position `Supervisor {runId}-062`, Division `Finance {runId}-062`) yang sudah login lewat alur Auth sehingga entri Login tercatat; singkatan tampil di kolom User `Budi A`. Position dan Division di-seed lewat API di hook `before` dan dihapus di hook `after`.
  - Password uji ketiga subjek: `Spectra.env.ACTLOG_PASSWORD` (fixture baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
- Kemampuan teknis: mengaktifkan dan login-kan subjek lewat API, serta menghapus user lewat sesi API admin kedua, tanpa mengarang endpoint (disediakan tim FE/BE).
- State global: tidak ada state global yang diubah selain menghapus user subjek milik spec. Spec ini destruktif hanya terhadap data milik spec dan tidak bergantung urutan antar spec; suite serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-80: Filter aktif tetap berlaku setelah user sumbernya dihapus (Tab Session)

1. Buka Global Settings > Activity Log > Session
2. Klik icon Filter, pilih User `Budi Anwar {runId}-062`, klik [Apply]
3. Lewat sesi API admin kedua `totalControlSecond_automated_qaTeam1@qwertysystem.net`, hapus user `Budi Anwar {runId}-062` (email `budianwar+{runId}-062@qwertysystem.net`) dan tunggu respons sukses
4. Muat ulang Tab Session dengan filter User `Budi Anwar {runId}-062` masih diterapkan
5. Verifikasi entri milik `Budi Anwar {runId}-062` tetap tampil
6. Klik icon Filter, buka daftar opsi field User
7. Verifikasi opsi `Budi Anwar {runId}-062` tetap ada di daftar opsi field User

### Pemulihan state antar TC

8. Klik [Clear Field] pada field User, klik [Apply]

### TC-GS-ACTLOG-169: Filter aktif tetap berlaku setelah admin sumbernya dihapus (Tab User Action)

9. Klik tab "User Action"
10. Klik icon Filter, pilih Modified By `Wulan`, klik [Apply]
11. Lewat sesi API admin kedua `totalControlSecond_automated_qaTeam1@qwertysystem.net`, hapus admin `Wulan` dengan email `wulan+{runId}-062@qwertysystem.net` dan tunggu respons sukses
12. Muat ulang Tab User Action dengan filter Modified By `Wulan` masih diterapkan
13. Verifikasi entri Brand `Brand Wulan {runId}-062` dengan Modified By `Wulan` tetap tampil
14. Klik icon Filter, buka daftar opsi field Modified By
15. Verifikasi opsi `Wulan` tetap ada di daftar opsi field Modified By

### Pemulihan state antar TC

16. Klik [Clear Field] pada field Modified By, klik [Apply]

### TC-GS-ACTLOG-55: Snapshot beku, baris lama tetap tampil setelah user dihapus

17. Buka Global Settings > User, hapus `Budi Anwar {runId}-062-b` (Employee ID `EMP002-{runId}-062`)
18. Tunggu aksi selesai (dialog konfirmasi tertutup dan tombol aktif kembali)
19. Buka Global Settings > Activity Log > Session
20. Ketik Search `EMP002-{runId}-062`, tekan Enter
21. Verifikasi baris Login milik `Budi Anwar {runId}-062-b` tetap tampil dengan User `Budi A`, Employee ID `EMP002-{runId}-062`, Position `Supervisor {runId}-062`, dan Division `Finance {runId}-062`

### Pemulihan state akhir spec

22. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Tiga TC menghapus data sehingga ditaruh berurutan di akhir spec (konvensi bagian 3 prinsip 5); tiap TC memakai subjek miliknya sendiri karena data yang sudah dihapus tidak dapat dipakai TC berikutnya. Semua subjek milik spec dan bersuffix, admin target hapus diidentifikasi lewat email, sehingga spec tidak bergantung urutan antar spec dan tidak menghapus fixture bersama.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 16, dan 22 (membersihkan Filter dan Search); langkah 18 (menunggu penghapusan user selesai, 8b butir 8). Subjudul "Pemulihan state" bukan TC sumber.
- Penghapusan user target pada TC-GS-ACTLOG-80 dan 169 (langkah 3 dan 11) dijalankan lewat sesi API admin kedua karena hasil di sesi itu tidak diasersi; padanan langkah "Di sesi lain, hapus" pada TC sumber.
- Temuan untuk QA:
  - TC-GS-ACTLOG-55 dan 80 sama-sama memakai `Budi Anwar`, tetapi user yang sama tidak dapat dihapus dua kali; spec memakai dua subjek bersuffix (`Budi Anwar {runId}-062` untuk TC-GS-ACTLOG-80 dan `Budi Anwar {runId}-062-b` untuk TC-GS-ACTLOG-55 yang mengasersi singkatan `Budi A`).
  - TC-GS-ACTLOG-169 tidak menyebut hak akses admin `Wulan` maupun aksi yang dilakukannya; spec memakai System Role berkapabilitas Create Brand dan satu aksi Create Brand. Total Control tidak dipakai karena target Total Control tidak dapat dihapus oleh admin lain.
  - Nama `Wulan` literal tumpang dengan admin bersama `Fixture.activityLog.adminWulan`: opsi `Wulan` pada filter Modified By (langkah 15) tidak membedakan admin yang dihapus dari admin bersama, sedangkan entri subjek dibedakan lewat Brand bersuffix (langkah 13). Mohon konfirmasi bahwa singkatan Modified By admin yang dihapus tetap `Wulan`.
  - Langkah 4 dan 12 mengasumsikan filter tetap aktif setelah muat ulang; asumsi ini mengikuti retensi state PRD §27.1c dan NC-11 tetapi tidak dinyatakan di Expected TC.
  - TC-GS-ACTLOG-55 tidak menyebut cara mencari entri Login milik user yang sudah dihapus; spec memakai Search dengan Employee ID subjek.
