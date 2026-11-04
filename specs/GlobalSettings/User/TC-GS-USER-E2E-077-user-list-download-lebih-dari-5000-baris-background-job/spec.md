---
id: TC-GS-USER-E2E-077-user-list-download-lebih-dari-5000-baris-background-job
title: "User List: Download Lebih dari 5.000 Baris Menampilkan Loading Screen sampai Berkas Siap (Berkas Langsung Terunduh, Tanpa Notifikasi)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-462
coverage:
  web: automated
---

# User List: Download Lebih dari 5.000 Baris Menampilkan Loading Screen sampai Berkas Siap (Berkas Langsung Terunduh, Tanpa Notifikasi)

## Prerequisites

- Mode: FE+BE. Spec berjalan paling akhir di antara spec User List dan serial: data volume mengubah jumlah baris tabel Login User yang diasumsikan spec lain.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): user Pre-setup di tabel Login User ikut dihitung dalam total baris.
- Data Dinamis (volume), di-seed lewat API di hook `before`: 5.001 user Login milik spec (`Volume User <n> {runId}-077`, `n` = 1 sampai 5.001; Email `volumeuser<n>+{runId}-077@qwertysystem.net`; Division `Finance`; Access `Fixed Asset`; Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) `🇮🇩 +62` `81234567890`), sehingga tabel Login User memuat lebih dari 5.000 baris tanpa bergantung pada Pre-setup. Kemampuan seeding massal lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD); TC menyebut kondisi ini sebagai data uji BE.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus seluruh 5.001 user volume lewat API.
- Jendela tunggu: 5 detik tanpa memuat ulang halaman (langkah 7), antara berkas terunduh (langkah 6) dan pembukaan Notification Center (langkah 8), agar notifikasi `[Download]` yang seharusnya tidak ada punya waktu muncul (asersi absence langkah 9 tidak lolos hanya karena dibaca terlalu dini). Nilai 5 detik adalah keputusan spec, bukan nilai dari TC atau PRD.
- Kemampuan teknis: membaca jumlah notifikasi berisi tombol `[Download]` di Notification Center (baseline sebelum aksi) dan mendeteksi berkas yang terunduh; nama endpoint tidak dibutuhkan karena tidak ada intercept.
- State yang diubah dan dipulihkan: jumlah user di environment (volume dihapus di hook `after`). Hook `after` mengembalikan sesi ke akun default suite.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-462: Download lebih dari 5.000 baris menampilkan loading screen sampai berkas siap

1. Buka Notification Center dan catat jumlah notifikasi yang berisi tombol `[Download]` sebagai baseline
2. Tutup Notification Center
3. Klik icon Download
4. Klik `Download as CSV`
5. Verifikasi loading screen tampil sampai berkas siap
6. Verifikasi berkas CSV langsung terunduh
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Buka Notification Center
9. Verifikasi tidak ada notifikasi `[Download]` baru (jumlah notifikasi berisi `[Download]` sama dengan baseline)

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`, `TC-GS-USER-462`. Kelas harness volume data (prinsip 13e): kuota data lebih dari N record dipisah dari spec fungsional. Satu TC berdiri sendiri dengan data seed volume dan cleanup sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (mencatat baseline jumlah notifikasi berisi `[Download]` sebelum aksi pemicu, S-12) langkah 7 (`Tunggu 5 detik tanpa memuat ulang halaman`, jendela 5 detik di Prerequisites), dan langkah 8 (membuka Notification Center). Asersi absence langkah 9 memakai baseline jumlah dan ditempatkan sesudah anchor positif langkah 6 (berkas terunduh) dan jendela tunggu langkah 7. Spec memiliki 9 langkah.
- Spec berjalan paling akhir di antara spec User List karena 5.001 user volume mengubah ukuran tabel (jumlah halaman, total Select All); volume dihapus di `after`.
- Seeding dan penghapusan 5.001 user volume menambah entri pencatatan perubahan User (Changelog, System Log); spec yang membaca log memakai baseline jumlah baris (selisih terhadap jumlah awal, S-12), bukan penanda waktu, dan tidak mengandalkan posisi teratas.
- Pembagian TC lintas spec: Download tabel dengan isi berkas di spec 076; Download gagal di spec 069.
- Temuan untuk QA:
  - TC-GS-USER-462: teks loading screen tidak disebut literal; spec mengasersi loading screen tampil tanpa teks.
  - TC-GS-USER-462: Automation `Manual Only` dan precondition "data uji BE"; spec tetap ditulis karena hambatan data bukan alasan mengeluarkan TC (bagian 2 konvensi); seeding massal 5.001 user disediakan tim FE/BE.
  - TC-GS-USER-462: tidak ada langkah observasi isi berkas hasil unduh; spec tidak mengasersi isi berkas.
