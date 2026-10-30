---
id: TC-GS-ACTLOG-E2E-053-sumber-user-action-brand-measurement-file-manager-permanently-delete
title: "Sumber User Action: Brand, Measurement, File Manager, Permanently Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-202
  - TC-GS-ACTLOG-203
  - TC-GS-ACTLOG-204
  - TC-GS-ACTLOG-210
coverage:
  web: automated
---

# Sumber User Action: Brand, Measurement, File Manager, Permanently Delete

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture. Akun ini membaca Changelog dan Activity Log; aksi sumber tidak dijalankan olehnya.
- Akun pelaku aksi sumber: admin `Hendra Pratama` (Client A), `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), kredensial `Spectra.env.GS_HENDRA_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Semua aksi sumber (buat Brand, buat unit Measurement, hapus berkas, hapus permanen berkas) dijalankan lewat sesi API admin ini; kemampuan itu dan kapabilitas Create Brand, Create Measurement, serta Delete dan Permanently Delete File Manager disediakan tim FE/BE tanpa mengarang endpoint. Nilai Modified By yang diasersi `Hendra P`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup: tidak ada data tetap yang diubah atau dipakai sebagai target aksi.
- Data Dinamis (bersuffix per run, dibersihkan di hook `after` tanpa berasumsi seeding berhasil penuh):
  - Brand `Acme Corp {runId}-053`: dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-202; dihapus lewat API di hook `after`.
  - Unit Measurement `Pieces {runId}-053`: dibuat oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-203; dihapus lewat API di hook `after`.
  - Berkas `Panduan Penggunaan {runId}-053.png`: di-seed lewat API di hook `before` pada File Manager; dihapus oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-204 (masuk Recycle Bin), lalu dihapus permanen di hook `after` bila masih ada.
  - Berkas `Panduan Penggunaan {runId}-053-permanen.png`: di-seed lewat API di hook `before` lalu dipindah ke Recycle Bin (seeding), dihapus permanen oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-210.
- Kemampuan teknis: akses baca `Changelog: Brand`, Changelog Measurement, dan `Changelog: File Manager` untuk menyalin baris Changelog aksi yang sama beserta kolom Date.
- Spec hanya menambah baris log. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-202: Aksi di modul Brand tercatat di Tab User Action

1. Lewat sesi API admin `Hendra Pratama`, buat Brand `Acme Corp {runId}-053` dan tunggu respons sukses
2. Buka Changelog modul Brand dan catat baris Changelog aksi Create untuk `Acme Corp {runId}-053` (Object, Name, Field, Old Value, New Value, Date)
3. Buka Global Settings > Activity Log > User Action
4. Ketik Search `Acme Corp {runId}-053`, tekan Enter
5. Verifikasi entri dengan Action `Create` untuk `Acme Corp {runId}-053` tampil
6. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Brand yang dicatat pada langkah 2
7. Verifikasi Modified By entri `Hendra P`
8. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 2

### Pemulihan state antar TC

9. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-203: Aksi di modul Measurement tercatat di Tab User Action

10. Lewat sesi API admin `Hendra Pratama`, buat unit Measurement `Pieces {runId}-053` dan tunggu respons sukses
11. Buka Changelog modul Measurement dan catat baris Changelog aksi Create untuk `Pieces {runId}-053` (Object, Name, Field, Old Value, New Value, Date)
12. Buka Global Settings > Activity Log > User Action
13. Ketik Search `Pieces {runId}-053`, tekan Enter
14. Verifikasi entri dengan Action `Create` untuk `Pieces {runId}-053` tampil
15. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Measurement yang dicatat pada langkah 11
16. Verifikasi Modified By entri `Hendra P`
17. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 11

### Pemulihan state antar TC

18. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-204: Aksi di modul File Manager tercatat di Tab User Action

19. Lewat sesi API admin `Hendra Pratama`, hapus berkas `Panduan Penggunaan {runId}-053.png` di File Manager dan tunggu respons sukses
20. Buka `Changelog: File Manager` dan catat baris Changelog aksi Delete berkas tersebut (Object, Name, Field, Old Value, New Value, Date)
21. Buka Global Settings > Activity Log > User Action
22. Ketik Search `Panduan Penggunaan {runId}-053.png`, tekan Enter
23. Verifikasi entri dengan Action `Delete` untuk `Panduan Penggunaan {runId}-053.png` tampil
24. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris `Changelog: File Manager` yang dicatat pada langkah 20
25. Verifikasi Modified By entri `Hendra P`
26. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 20

### Pemulihan state antar TC

27. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-210: Hapus permanen berkas di File Manager tercatat sebagai Permanently Delete

28. Lewat sesi API admin `Hendra Pratama`, hapus permanen berkas `Panduan Penggunaan {runId}-053-permanen.png` dari Recycle Bin File Manager dan tunggu respons sukses
29. Buka `Changelog: File Manager` dan catat baris Changelog aksi Permanently Delete berkas tersebut (Object, Field, Old Value, New Value)
30. Buka Global Settings > Activity Log > User Action
31. Ketik Search `Panduan Penggunaan {runId}-053-permanen.png`, tekan Enter
32. Verifikasi entri dengan Action `Permanently Delete` dan Name `Panduan Penggunaan {runId}-053-permanen.png` tampil
33. Verifikasi Object, Field, Old Value, dan New Value entri identik dengan baris `Changelog: File Manager` yang dicatat pada langkah 29
34. Verifikasi Modified By entri `Hendra P`
35. Klik icon Filter, buka daftar opsi field Action
36. Verifikasi daftar opsi Action memuat `Permanently Delete`

### Pemulihan state akhir spec

37. Tutup Filter Panel tanpa menerapkan filter, lalu klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 11, 20, dan 29 (membaca baris Changelog modul sumber sebagai pembanding Expected "identik dengan baris Changelog" dan Date); langkah 9, 18, 27, dan 37 (membersihkan Search dan menutup Filter Panel). Aksi sumber lewat API menunggu respons sukses sebelum langkah berikutnya (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline entri adalah nol karena nama subjek bersuffix unik per run (S-12).
- Spec di atas smell 35 langkah (37). Alasan: empat blok berdiri sendiri dengan akun, tabel, dan pola baca-log yang sama (satu kelas harness); langkah baca-log yang berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung ke batas ukuran, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-GS-ACTLOG-210 memakai berkas kedua milik spec karena berkas TC-GS-ACTLOG-204 sudah dihapus pada blok sebelumnya. Urutan TC-GS-ACTLOG-204 sebelum 210 mengikuti TC sumber.
- Pembagian TC lintas spec: TC-GS-ACTLOG-199, 200, dan 201 ada di spec 052; TC-GS-ACTLOG-205 di spec 054; TC-GS-ACTLOG-206 ada di spec 037; TC-GS-ACTLOG-207, 208, dan 209 di spec 055; TC-GS-ACTLOG-211 (Modified By `System`) di spec 056.
- Temuan untuk QA:
  - Email admin `Hendra Pratama` (Modified By `Hendra P`) dan cara menjalankan aksi lewat sesi API ditetapkan tim FE (fixture `Fixture.activityLog.adminHendra`).
  - Aksi Create menghasilkan satu baris per field (TC-GS-ACTLOG-144), sedangkan Expected TC menyebut satu "entri"; spec membandingkan seluruh baris hasil aksi dengan Changelog.
  - PRD File Manager menamai surface log itu `Changelog: File Manager`; TC-GS-ACTLOG-204 dan 210 tidak menyebut lokasinya.
  - TC-GS-ACTLOG-204 dan 210 menyebut Name `Panduan Penggunaan.png` literal; spec memakai nama bersuffix per run dan mengasersi Name bersuffix yang sama.
  - TC-GS-ACTLOG-210 langkah 1 ("cari entri aksi tersebut") tidak menyebut kriteria pencarian; spec mencari lewat Search dengan nama berkas.
