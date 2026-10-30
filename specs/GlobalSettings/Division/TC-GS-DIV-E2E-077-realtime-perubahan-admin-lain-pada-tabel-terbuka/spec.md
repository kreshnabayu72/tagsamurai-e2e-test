---
id: TC-GS-DIV-E2E-077-realtime-perubahan-admin-lain-pada-tabel-terbuka
title: "Realtime: Create dan Rename dari Admin Lain Tampil Otomatis di Tabel Terbuka"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-277
  - TC-GS-DIV-278
coverage:
  web: automated
---

# Realtime: Create dan Rename dari Admin Lain Tampil Otomatis di Tabel Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (Admin A, pengamat tabel): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B, pelaku Create dan Rename, hanya lewat API tanpa login UI): Total Control (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Akun ini tidak tercantum di Tabel Data Uji Pre-setup Division; akun ini mengikuti suite Brand dan disediakan tim FE di entitas yang sama dengan Sesi A.
- Dua sesi (kelas multi-konteks): Sesi A adalah sesi UI di konteks browser dengan sesi login sendiri; Sesi B adalah sesi API terpisah (login lewat API dengan `Spectra.env.GS_TC2_PASSWORD`) tanpa konteks browser kedua. Sesi A login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > User > Division tanpa Search atau Filter aktif; login API Sesi B juga dilakukan di hook `before`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat spec lewat API oleh Sesi B:
  - `Realtime Unit {runId}-077` dengan Code `RTU` (D-19) pada TC-GS-DIV-277; Code `RTU` dipakai sesuai TC (pengecualian S-12: seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial).
  - Nama hasil rename pada TC-GS-DIV-278: `Realtime Unit 2 {runId}-077`.
- Cleanup (hook `after`, tidak berasumsi langkah spec berhasil penuh): hapus lewat API `Realtime Unit {runId}-077` dan `Realtime Unit 2 {runId}-077` bila ada, dan pulihkan page size Pagination Sesi A ke 10. Hook `before` menghapus lewat API sisa Division bernama `Realtime Unit {runId lama}-077` atau `Realtime Unit 2 {runId lama}-077` (nama berpola `Realtime Unit *-077` dan `Realtime Unit 2 *-077`, bukan berdasarkan Code saja) yang masih memegang Code `RTU`.
- Kemampuan teknis: satu konteks browser (Sesi A) dan satu sesi API (Sesi B) dalam satu spec; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`; Sesi B membuat dan mengganti nama Division lewat API (disediakan tim FE); mengamati tabel Sesi A tanpa memuat ulang halaman sampai pembaruan realtime tampil (auto-wait); membaca posisi scroll dan halaman aktif tabel Sesi A.
- State global yang diubah: page size Pagination Sesi A (diubah di langkah 1, dikembalikan ke 10 di langkah 12; hook `after` menjadi cadangan). Tidak ada state global lain yang diubah.
- TC-GS-DIV-277 dan 278: login sebagai Total Control (Sesi A dan Sesi B).

## Test Steps

### TC-GS-DIV-277: Division baru dari admin lain muncul otomatis di tabel yang sedang dibuka

1. [Sesi A] Ubah page size Pagination menjadi nilai terbesar yang tersedia sehingga seluruh Division tampil dalam satu halaman
2. [Sesi A] Gulir tabel ke posisi paling bawah, lalu catat posisi scroll dan halaman aktif
3. [Sesi B] Buat Division `Realtime Unit {runId}-077` dengan Code `RTU` lewat API
4. [Sesi B] Tunggu hingga Create selesai (respons sukses diterima)
5. [Sesi A] Tanpa memuat ulang halaman, verifikasi baris `Realtime Unit {runId}-077` muncul di tabel
6. [Sesi A] Verifikasi tidak ada dialog yang tampil
7. [Sesi A] Verifikasi posisi scroll sama dengan yang dicatat pada langkah 2
8. [Sesi A] Verifikasi halaman aktif sama dengan yang dicatat pada langkah 2

### TC-GS-DIV-278: Rename Division dari admin lain tampil otomatis di tabel yang sedang dibuka

9. [Sesi B] Ganti nama Division `Realtime Unit {runId}-077` menjadi `Realtime Unit 2 {runId}-077` lewat API
10. [Sesi B] Tunggu hingga Rename selesai (respons sukses diterima)
11. [Sesi A] Tanpa memuat ulang halaman, verifikasi baris pada tabel menampilkan `Realtime Unit 2 {runId}-077`
12. [Sesi A] Kembalikan page size Pagination ke 10

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas multi-konteks (prinsip 13c), jenis dua admin; objek asersi adalah tabel Sesi A yang diubah Sesi B. Butir P-2: Sesi B adalah sesi API karena hanya memicu perubahan state (Create dan Rename) dan tidak ada asersi di Sesi B; TC-GS-DIV-277 dan 278 menulis "Admin B membuat" dan "Admin B mengubah" tanpa menyebut mekanisme.
- Urutan TC sama dengan urutan sumber (277 lalu 278); Division yang dibuat pada TC-GS-DIV-277 dipakai TC-GS-DIV-278 di spec yang sama, tidak menumpang spec lain.
- Asersi state sementara tepat waktu (bagian 8b butir 5): langkah 5 sampai 8 dijalankan sebelum Sesi A melakukan aksi lain; posisi scroll dan halaman aktif dicatat sebelum Sesi B membuat Division (langkah 2).
- Langkah penghubung: langkah 1 dan 12 (mengubah dan memulihkan page size Pagination supaya baris baru terlihat pada halaman aktif Sesi A tanpa berpindah halaman); langkah 2 (mencatat posisi scroll dan halaman aktif sebagai baseline Expected Result b); langkah 4 dan 10 (menunggu aksi Sesi B selesai).
- Expected Result a TC-GS-DIV-277 ("secara diam-diam tanpa dialog") dipecah menjadi langkah 5 (baris muncul) dan langkah 6 (tidak ada dialog); Expected Result b dipecah menjadi langkah 7 (posisi scroll) dan 8 (halaman aktif).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-277: TC tidak menyebut posisi baris baru; default sort Name A-Z (PRD Division) membuat `Realtime Unit {runId}-077` bisa berada di halaman yang bukan halaman aktif Sesi A. Spec memperbesar page size agar baris terlihat, dan opsi page size terbesar tidak didefinisikan di TC atau PRD Division.
  - TC-GS-DIV-277: TC tidak menyebut batas waktu munculnya pembaruan realtime; spec memakai auto-wait.
  - TC-GS-DIV-277 dan 278: akun Admin B (`totalControlSecond_automated_qaTeam1@qwertysystem.net`, `GS_TC2_PASSWORD`) tidak ada di Tabel Data Uji Pre-setup Division; disediakan tim FE dengan nama env var mengikuti suite Brand.
  - TC-GS-DIV-277: Post Condition `Division Realtime Unit tersimpan (D-19)` tidak punya langkah observasi di TC dan tidak diasersi terpisah; penyimpanan teramati secara tidak langsung lewat tabel Sesi A.
