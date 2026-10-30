---
id: TC-GS-USER-E2E-077-user-list-download-lebih-dari-5000-baris-background-job
title: "User List: Download Lebih dari 5.000 Baris Berjalan sebagai Background Job (Toast Informasional dan Notifikasi dengan Tombol Download)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-462
coverage:
  web: automated
---

# User List: Download Lebih dari 5.000 Baris Berjalan sebagai Background Job (Toast Informasional dan Notifikasi dengan Tombol Download)

## Prerequisites

- Mode: FE+BE. Spec berjalan paling akhir di antara spec User List dan serial: data volume mengubah jumlah baris tabel Login User yang diasumsikan spec lain.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): user Pre-setup di tabel Login User ikut dihitung dalam total baris.
- Data Dinamis (volume), di-seed lewat API di hook `before`: 5.001 user Login milik spec (`Volume User <n> {runId}-077`, `n` = 1 sampai 5.001; Email `volumeuser<n>+{runId}-077@qwertysystem.net`; Division `Finance`; Access `Fixed Asset`; Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) `🇮🇩 +62` `81234567890`), sehingga tabel Login User memuat lebih dari 5.000 baris tanpa bergantung pada Pre-setup. Kemampuan seeding massal lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD); TC menyebut kondisi ini sebagai data uji BE.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus seluruh 5.001 user volume lewat API.
- Kemampuan teknis: membuka Notification Center dan membaca jumlah serta isi notifikasi; menunggu job background selesai dengan batas waktu yang ditetapkan tim FE (TC tidak menyebut lama job); nama endpoint tidak dibutuhkan karena tidak ada intercept.
- State yang diubah dan dipulihkan: jumlah user di environment (volume dihapus di hook `after`); notifikasi baru di Notification Center (tidak dihapus oleh spec). Hook `after` mengembalikan sesi ke akun default suite.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-462: Download lebih dari 5.000 baris berjalan sebagai background job

1. Buka Notification Center dan catat jumlah notifikasi yang berisi tombol `[Download]` sebagai baseline
2. Tutup Notification Center
3. Klik icon Download
4. Klik `Download as CSV`
5. Verifikasi toast informasional pemrosesan background tampil
6. Buka Notification Center
7. Verifikasi notifikasi baru berisi tombol `[Download]` tampil saat job selesai (jumlah notifikasi berisi `[Download]` bertambah satu dari baseline)

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`, `TC-GS-USER-462`. Kelas harness volume data (prinsip 13e): kuota data lebih dari N record dipisah dari spec fungsional. Satu TC berdiri sendiri dengan data seed volume dan cleanup sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (mencatat baseline jumlah notifikasi berisi `[Download]` sebelum aksi pemicu, S-12) dan langkah 6 (membuka Notification Center). Asersi "notifikasi berisi `[Download]`" memakai baseline, bukan posisi teratas.
- Spec berjalan paling akhir di antara spec User List karena 5.001 user volume mengubah ukuran tabel (jumlah halaman, total Select All); volume dihapus di `after`.
- Seeding dan penghapusan 5.001 user volume menambah entri pencatatan perubahan User (Changelog, System Log); spec yang membaca log memakai baseline penanda waktu (S-12) dan tidak mengandalkan posisi teratas.
- Pembagian TC lintas spec: Download tabel dengan isi berkas di spec 076; Download gagal di spec 069.
- Temuan untuk QA:
  - TC-GS-USER-462 bertentangan dengan `foundation/process/prd-process/error-handling-convention.md` §10.1 (revisi 2026-10-07): Download atau Export di atas 5.000 baris memakai loading screen sampai berkas siap lalu langsung terunduh, tanpa job background, tanpa toast informasional, dan tanpa notifikasi in-app. PRD User §5 merujuk §10.1. Spec mengikuti TC (toast informasional dan notifikasi `[Download]`); TC atau konvensi perlu diselaraskan.
  - TC-GS-USER-462: teks toast informasional tidak disebut literal (TC hanya menyebut "toast informasional pemrosesan background"); spec mengasersi toast tampil tanpa teks.
  - TC-GS-USER-462: Automation `Manual Only` dan precondition "data uji BE"; spec tetap ditulis karena hambatan data bukan alasan mengeluarkan TC (bagian 2 konvensi); seeding massal 5.001 user disediakan tim FE/BE.
  - TC-GS-USER-462: tidak ada langkah observasi isi berkas hasil unduh dari notifikasi; spec tidak mengasersi isi berkas dan tidak mengklik `[Download]`.
