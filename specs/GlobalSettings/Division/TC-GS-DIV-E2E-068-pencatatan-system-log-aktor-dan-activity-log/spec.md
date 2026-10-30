---
id: TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log
title: "Pencatatan Tab System Log Aktor dan Activity Log Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-247
  - TC-GS-DIV-248
  - TC-GS-DIV-297
  - TC-GS-DIV-298
  - TC-GS-DIV-299
coverage:
  web: automated
---

# Pencatatan Tab System Log Aktor dan Activity Log Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh Division milik spec ini):
  - `Metro Branch 3 {runId}-068` dengan Code `MTB` (D-15): di-seed lewat API di hook `before` (setara dependensi TC-GS-DIV-245); Code diubah menjadi `MB3` pada TC-GS-DIV-248.
  - `Syslog Edit {runId}-068` dengan Code `SLE`: Division bebas relasi, di-seed lewat API di hook `before` (setara pembuatan lewat `[+ Division]` pada Precondition c TC-GS-DIV-297); di-rename menjadi `Syslog Edit Renamed {runId}-068` pada TC-GS-DIV-297, lalu dihapus pada TC-GS-DIV-298.
  - `Syslog Smoke {runId}-068` dengan Code `SYS`: dibuat spec lewat UI pada TC-GS-DIV-247, Code diubah menjadi `SYS2`, lalu dihapus.
  - `Syslog Bulk A {runId}-068` dan `Syslog Bulk B {runId}-068`: Division bebas relasi, di-seed lewat API di hook `before`; `Syslog Bulk C {runId}-068`: Division in-use oleh Login User uji `syslogbulk+{runId}-068@qwertysystem.net` (seeding Login User lewat API di hook `before`, dengan Division `Syslog Bulk C {runId}-068`; nilai field wajib lain disediakan tim FE). Dipakai pada TC-GS-DIV-299.
- Kode literal `MTB`, `SLE`, `SYS`, dan `SYS2` mengikuti TC. Hook `before` menghapus lewat API sisa Division bersuffix `-068` dari run lama (bukan berdasarkan kode saja) sehingga kode itu bebas; Division Pre-setup dan Population D-02 tidak disentuh. Suite berjalan serial (S-12).
- Kemampuan teknis: seeding Division dan Login User lewat API, serta penghapusan keduanya lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`). Nilai field wajib Login User uji (Access dan lainnya) berasal dari fixture `fixtures/division.json` yang belum ada; tim FE menyediakannya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Login User `syslogbulk+{runId}-068@qwertysystem.net`, lalu seluruh Division bersuffix `{runId}-068` yang masih ada (`Metro Branch 3`, `Syslog Edit`, `Syslog Edit Renamed`, `Syslog Smoke`, `Syslog Bulk A`, `Syslog Bulk B`, `Syslog Bulk C`). Entri log bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Tidak ada state global yang diubah.
- TC-GS-DIV-247, 248, 297, 298, 299: login sebagai Total Control (aktor Admin Total Control) dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-248: Edit tercatat juga di Activity Log Global Settings

1. Ketik Search `Metro Branch 3 {runId}-068`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Code `MTB` menjadi `MB3`, klik [Save]
2. Tunggu aksi selesai (modal Edit tertutup)
3. Buka Global Settings > Activity Log, ketik Search `Metro Branch 3 {runId}-068`, tekan Enter
4. Verifikasi Activity Log, entri teratas: Action `Edit`, Object `Division`, Name `Metro Branch 3 {runId}-068`, Field `Code`, Old Value `MTB`, New Value `MB3`, Modified By `Sari D`

### TC-GS-DIV-297: Edit Division menulis entri Edit di Tab System Log aktor

5. Buka Global Settings > User > Division, ketik Search `Syslog Edit {runId}-068`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Syslog Edit Renamed {runId}-068`, klik [Save]
6. Tunggu aksi selesai (modal Edit tertutup)
7. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `Syslog Edit Renamed {runId}-068`, tekan Enter
8. Verifikasi System Log Sari Dewi, entri teratas: Action `Edit`, Object `Division`, Name `Syslog Edit Renamed {runId}-068`, Field `Division Name`, Old Value `Syslog Edit {runId}-068`, New Value `Syslog Edit Renamed {runId}-068`
9. Verifikasi hasil Search memuat tepat 1 entri
10. Verifikasi hasil Search tidak memuat entri Field `Code` untuk `Syslog Edit Renamed {runId}-068`

### TC-GS-DIV-247: Create, Edit, dan Delete Division menulis entri di Tab System Log aktor

11. Buka Global Settings > User > Division, klik [+ Division], isi Division Name `Syslog Smoke {runId}-068` dan Code `SYS`, klik [Submit]
12. Tunggu aksi selesai (modal Create tertutup)
13. Ketik Search `Syslog Smoke {runId}-068`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Code `SYS` menjadi `SYS2`, klik [Save]
14. Tunggu aksi selesai (modal Edit tertutup)
15. Ganti isi kotak search tabel Division dengan `Syslog Smoke {runId}-068`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog konfirmasi
16. Tunggu aksi selesai (dialog konfirmasi Delete tertutup)
17. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `Syslog Smoke {runId}-068`, tekan Enter
18. Verifikasi System Log Sari Dewi memuat tepat 3 entri untuk `Syslog Smoke {runId}-068`
19. Verifikasi entri Create: Action `Create`, Object `Division`, Name `Syslog Smoke {runId}-068`, Field `Division Name`, Old Value `—`, New Value `Syslog Smoke {runId}-068`
20. Verifikasi entri Edit: Action `Edit`, Object `Division`, Name `Syslog Smoke {runId}-068`, Field `Code`, Old Value `SYS`, New Value `SYS2`
21. Verifikasi entri Delete: Action `Delete`, Object `Division`, Name `Syslog Smoke {runId}-068`, Field `Division Name`, Old Value `Syslog Smoke {runId}-068`, New Value `—`
22. Verifikasi kolom tabel System Log: Date, Action, Object, Name, Field, Old Value, New Value
23. Verifikasi kolom Action tampil sebagai plain text

### TC-GS-DIV-298: Delete Division menulis entri Delete di Tab System Log aktor

24. Buka Global Settings > User > Division, ketik Search `Syslog Edit Renamed {runId}-068`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog konfirmasi
25. Tunggu aksi selesai (dialog konfirmasi Delete tertutup)
26. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `Syslog Edit Renamed {runId}-068`, tekan Enter
27. Verifikasi System Log Sari Dewi, entri teratas: Action `Delete`, Object `Division`, Name `Syslog Edit Renamed {runId}-068`, Field `Division Name`, Old Value `Syslog Edit Renamed {runId}-068`, New Value `—`

### TC-GS-DIV-299: Bulk Delete menulis satu entri Tab System Log aktor per Division yang berhasil dihapus

28. Buka Global Settings > User > Division, ketik Search `Syslog Bulk`, tekan Enter pada tabel Division, centang baris `Syslog Bulk A {runId}-068`, `Syslog Bulk B {runId}-068`, dan `Syslog Bulk C {runId}-068`
29. Klik aksi [Delete] pada Bulk Action Bar
30. Klik [Continue] pada dialog Delete Division
31. Tunggu aksi selesai (dialog Delete Division tertutup)
32. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `Syslog Bulk`, tekan Enter
33. Verifikasi System Log Sari Dewi memuat tepat 2 entri dengan Action `Delete` (entri Action lain, mis. Create hasil seeding, tidak dihitung), Object `Division`, Name `Syslog Bulk A {runId}-068` dan `Syslog Bulk B {runId}-068`, masing-masing Old Value nama Division dan New Value `—`
34. Verifikasi System Log Sari Dewi tidak memuat entri Action `Delete` untuk `Syslog Bulk C {runId}-068`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Urutan TC di spec: 248, 297, 247, 298, 299. Edit (248, 297) lebih dulu; aksi yang menghapus data (247 sampai 299) kemudian, dengan 299 paling akhir karena Bulk Delete menghapus tiga Division. TC-GS-DIV-247 menghapus `Syslog Smoke` miliknya sendiri di akhir TC dan tidak dipakai TC lain, sehingga ditaruh sebelum 298 dan 299.
- Dependensi TC-GS-DIV-245 (Division `Metro Branch 3`), TC-GS-DIV-297 (dipakai sebagai dependensi TC-GS-DIV-298), dan Division pada TC-GS-DIV-299 dijalankan lewat seeding API di hook `before` atau sebagai langkah di spec ini, bukan bergantung pada spec lain.
- Entri log dikenali lewat nama bersuffix `{runId}-068`; entri milik run lain diabaikan. "Entri teratas" pada langkah 4, 8, 27 berarti entri teratas pada hasil Search nama bersuffix itu (urutan default Newest First).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search nama Division pada tabel Division sebelum Edit, Delete, atau centang (langkah 1, 5, 13, 15, 24, 28; tabel A-Z memiliki lebih dari satu halaman), membuka Detail Sari Dewi > Tab System Log atau Activity Log (langkah 3, 7, 17, 26, 32), kembali ke tab Division (langkah 5, 11, 24, 28), langkah 2, 6, 12, 14, 16, dan 25 (menunggu aksi Submit, Save, atau Delete selesai sebelum aksi berikutnya, 8b butir 8), dan langkah 31 (menunggu aksi selesai).
- Pengecualian P-1 dan S-05: TC-GS-DIV-299 Expected Result b ("Tidak ada entri untuk `Syslog Bulk C`", dibatasi spec ke entri Delete) ditulis di spec ini sebagai langkah 34 dengan nama bersuffix `{runId}-068` yang unik per run dan dibatasi ke Action `Delete` (entri Create seeding `Syslog Bulk C` mungkin ada pada hasil Search dan tidak diasersi), dengan anchor positif langkah 33 (dua entri Delete `Syslog Bulk A` dan `Syslog Bulk B` pada hasil Search yang sama), karena spec absence `TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use` tidak memuat TC-GS-DIV-299. Butir P-1: Division in-use `Syslog Bulk C` (dengan Login User hasil seeding) adalah seeding berat yang sama dengan aksi Bulk Delete TC-GS-DIV-299 Expected Result a, sehingga Expected Result b memakai state itu di spec ini.
- Spec `TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit` dan `TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete` memuat padanan pencatatan di Modal Changelog.
- Langkah 22 dan 23 memverifikasi klausa d TC-GS-DIV-247 (kolom tabel dan Action plain text) pada tabel System Log yang sama dengan langkah 18 sampai 21.
- Temuan untuk QA:
  - TC-GS-DIV-299 Precondition c menyatakan `Syslog Bulk C` "dipakai user" tanpa menyebut user atau cara memakainya; spec men-seed Login User uji lewat API (mekanisme tidak didefinisikan TC).
  - TC-GS-DIV-299 Expected Result b adalah asersi absence tetapi TC ini tidak berada di spec absence.
  - TC-GS-DIV-248 Expected Result menyebut Old Value "kode lama" tanpa nilai; spec memakai `MTB` dari seeding.
  - TC-GS-DIV-297 Precondition c menyebut Division `Syslog Edit` "dibuat lewat `[+ Division]`", sedangkan spec men-seed lewat API karena pembuatan bukan objek uji TC itu.
  - TC-GS-DIV-247 Post Condition ("Tiga entri Division tercatat di Tab System Log aktor") punya langkah observasi (Langkah Uji 4) dan diasersi pada langkah 18.
