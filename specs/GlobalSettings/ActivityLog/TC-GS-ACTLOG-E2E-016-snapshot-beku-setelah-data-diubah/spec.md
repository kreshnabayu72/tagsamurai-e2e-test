---
id: TC-GS-ACTLOG-E2E-016-snapshot-beku-setelah-data-diubah
title: "Snapshot Beku Setelah Data Diubah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-54
  - TC-GS-ACTLOG-213
coverage:
  web: automated
---

# Snapshot Beku Setelah Data Diubah

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman Global Settings > User (flag `gs-user`) serta Global Settings > Activity Log (kemampuan disediakan tim FE/BE)
- Akun aktor: Total Control Client A (Sari Dewi), `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Activity Log.
- Admin `Wulan Sari` (Client A; pelaku aksi sumber, tampil Modified By `Wulan S`): `Fixture.activityLog.adminWulanSari` (email ditetapkan tim FE), password `Spectra.env.GS_WULANSARI_PASSWORD`, capability Create Brand (disediakan tim FE). Dipakai di hook `before` lewat sesi API untuk membuat Brand `Acme Corp {runId}-016`.
- Environment variable: `GS_TC_PASSWORD`, `GS_WULANSARI_PASSWORD`, `ACTLOG_PASSWORD` (password uji yang dipasang ke user dinamis modul Activity Log). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- State global yang diubah: Last Name admin `Wulan Sari` menjadi `Sari Dewi` pada langkah 15; hook `after` memulihkannya ke `Sari` walau spec gagal di tengah. Akun ini dipakai bersama spec lain sebagai pelaku aksi sumber, sehingga suite berjalan serial (`parallel: false`, lihat suite.md).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat API di hook `before`:
  - User `John Doe {runId}-016` (First Name `John`, Last Name `Doe {runId}-016`), Employee ID `EMP001-{runId}-016`, Position `Staff {runId}-016`, Division `Marketing {runId}-016`, dengan entri Login lama lewat alur Auth (password `Spectra.env.ACTLOG_PASSWORD`). Nilai bersuffix dipakai sebagai pengganti `John Doe`, `EMP001`, `Staff`, dan `Marketing` di TC agar tidak bentrok dengan spec lain; singkatan User mengikuti TC (`John Doe` tampil `John D`).
  - Position `Manager {runId}-016` dan Division `Finance {runId}-016` sebagai nilai tujuan perubahan.
  - Brand `Acme Corp {runId}-016`, dibuat oleh admin `Wulan Sari` lewat sesi API sehingga entri User Action `Create` `Brand` `Acme Corp {runId}-016` bercatat atas nama `Wulan Sari` (setara precondition TC-GS-ACTLOG-213).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `John Doe {runId}-016` (atau nama tampil hasil edit `Johnny Doe {runId}-016`), Brand `Acme Corp {runId}-016`, Position `Staff {runId}-016` dan `Manager {runId}-016`, serta Division `Marketing {runId}-016` dan `Finance {runId}-016`, bila masih ada; pulihkan Last Name admin `Wulan Sari` ke `Sari`. Aksi Edit user pada John Doe hanya mengubah data milik spec ini (bagian 5 konvensi, S-06).

## Test Steps

### TC-GS-ACTLOG-54: Snapshot beku nama, Employee ID, Position, dan Division di baris lama

1. Buka Global Settings > User, ketik Search `John Doe {runId}-016`, tekan Enter, buka Edit pada baris `John Doe {runId}-016`
2. Ubah First Name menjadi `Johnny`, Employee ID menjadi `EMP101-{runId}-016`, Position menjadi `Manager {runId}-016`, Division menjadi `Finance {runId}-016`
3. Klik [Save]
4. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
5. Buka Global Settings > Activity Log > Session
6. Ketik Search `John Doe {runId}-016`, tekan Enter
7. Verifikasi kolom User pada baris Login lama tetap `John D`
8. Arahkan kursor ke sel User pada baris Login lama
9. Verifikasi hover menampilkan `John Doe {runId}-016`
10. Verifikasi kolom Employee ID pada baris Login lama tetap `EMP001-{runId}-016`
11. Verifikasi kolom Position pada baris Login lama tetap `Staff {runId}-016`
12. Verifikasi kolom Division pada baris Login lama tetap `Marketing {runId}-016`

### TC-GS-ACTLOG-213: Snapshot Modified By beku setelah admin diubah namanya

13. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
14. Buka Global Settings > User, ketik Search `Wulan Sari`, tekan Enter, buka Edit pada baris `Wulan Sari`
15. Ubah Last Name menjadi `Sari Dewi`
16. Klik [Save]
17. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
18. Buka Global Settings > Activity Log > User Action
19. Ketik Search `Acme Corp {runId}-016`, tekan Enter
20. Verifikasi kolom Modified By pada entri lama tetap `Wulan S`
21. Arahkan kursor ke sel Modified By pada entri lama
22. Verifikasi hover menampilkan `Wulan Sari`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-54, 213).
- Langkah penghubung (tanpa awalan `Verifikasi`): mencari user di daftar User lewat Search sebelum membuka Edit (langkah 1 dan 14), membuka Tab Session dan User Action serta mengetik Search nama subjek bersuffix (langkah 5, 6, 18, 19), mengarahkan kursor ke sel (langkah 8 dan 21), dan menunggu [Save] selesai sebelum berpindah halaman (langkah 4 dan 17, bagian 8b butir 8). Langkah 13 menutup Search tab Session sebagai pemulihan state antar TC. Langkah 15 mengubah Last Name `Sari` menjadi `Sari Dewi`, yaitu perubahan nama `Wulan Sari` menjadi `Wulan Sari Dewi` pada TC.
- Search pada langkah 6 memakai nama lama `John Doe {runId}-016` untuk menemukan baris lama; ini mengikuti TC ("cari entri Login lama tersebut").
- Edit user (langkah 1 sampai 3 dan 14 sampai 16) adalah aksi nyata di modul sumber User dan menghasilkan entri User Action baru; entri itu tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-GS-ACTLOG-54 tidak menyebut cara mencari baris lama setelah nama berubah (Search dengan nama lama atau baru); spec memakai nama lama bersuffix.
  - TC-GS-ACTLOG-213 memuat entri `Create` `Brand` `Acme Corp` oleh admin `Wulan Sari` sebagai precondition tanpa menyebut capability admin; spec memakai admin dengan capability Create Brand yang disediakan tim FE/BE.
  - TC memakai `John Doe`, `EMP001`, `Staff`, `Marketing`, dan `Acme Corp` literal; spec memakai nilai bersuffix untuk data John Doe dan Brand. QA konfirmasi bahwa singkatan User (`John D`) tidak terpengaruh suffix pada Last Name.
  - TC-GS-ACTLOG-54 Expected a berisi dua klausa (User tetap `John D`, hover tetap `John Doe`); spec memisahkannya menjadi langkah 7 dan 9.
  - TC-GS-ACTLOG-213 mengubah nama admin `Wulan Sari`, akun yang juga dipakai sebagai pelaku aksi sumber oleh spec lain (Tabel Dinamis TC baris 4); pemulihan nama di hook `after` mengandalkan akun tidak dipakai spec lain bersamaan.
