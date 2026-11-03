---
id: TC-FA-RP-E2E-302-bulk-remove-hasil-parsial-dan-diblok-oleh-admin-lain
title: "Bulk Remove: hasil parsial dan diblok oleh admin lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-299
  - TC-FA-RP-300
coverage:
  web: automated
---

# Bulk Remove: hasil parsial dan diblok oleh admin lain

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Manage global user & role (Update) Hendra Wijaya (Pre-setup #6), `murGlobal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_MUR_GLOBAL_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Pelaku kedua (Sesi 2): Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, lewat sesi API (hanya memicu perubahan state, bukan konteks UI kedua).
- Data Pre-setup: pool #15 (Ahmad Fauzi, Budi Santoso, Budi Setiawan) dan #6 (Hendra Wijaya). Ahmad Fauzi, Budi Santoso, dan Budi Setiawan memegang Global Role `Manage Open API` tanpa tingkat akses; disiapkan lewat seed API di hook `before` dan sebagai langkah penghubung (langkah 12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan `Manage Open API` pool #15 dan tingkat akses yang diberikan Sesi 2 (Ahmad Fauzi, Budi Santoso, Budi Setiawan kembali Standard)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-299: Bulk Remove sebagian baris ditolak per baris: toast sukses parsial

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Centang baris Ahmad Fauzi, Budi Santoso, dan Budi Setiawan
3. Klik `Bulk Action` > `Remove` hingga dialog Bulk Remove terbuka
4. Sesi 2 (sesi API Total Control Siti Rahmawati) meng-Assign Total Control ke Ahmad Fauzi hingga penugasan tersimpan
5. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
6. Di Sesi 1, klik `[Remove]`
7. Verifikasi muncul toast sukses parsial: `Success, user has been removed. Some items were skipped.`
8. Verifikasi baris Budi Santoso dan Budi Setiawan terhapus
9. Verifikasi baris Ahmad Fauzi tetap ada
10. Verifikasi Bulk Action Bar tertutup
11. Verifikasi seleksi di-reset ke 0 termasuk baris yang gagal

### TC-FA-RP-300: Bulk Remove tanpa satu baris pun berhasil: dialog blok tanpa toast

12. Pulihkan state lewat seed API: Budi Santoso dan Budi Setiawan memegang `Manage Open API` tanpa tingkat akses, lalu muat ulang halaman
13. Centang baris Budi Santoso dan Budi Setiawan
14. Klik `Bulk Action` > `Remove` hingga dialog Bulk Remove terbuka
15. Sesi 2 (sesi API Total Control Siti Rahmawati) meng-Assign Total Control ke Budi Santoso dan Budi Setiawan hingga penugasan tersimpan
16. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
17. Di Sesi 1, klik `[Remove]`
18. Verifikasi tidak muncul toast sukses maupun toast parsial
19. Verifikasi tampil dialog blok severity warning: Title `Cannot Remove`; Body `None of the selected users could be removed.`; satu tombol `[OK]`
20. Verifikasi tidak ada baris yang terhapus: baris Budi Santoso dan Budi Setiawan tetap ada
21. Klik `[OK]`
22. Verifikasi Bulk Action Bar dan seleksi dipertahankan

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-299, TC-FA-RP-300).
- Langkah penghubung (S-03): membuka Detail Role; berpindah sesi; pemulihan state seed (langkah 12); "Tunggu aksi selesai" pada langkah 5 dan 16 karena aktor berpindah sesi sesudah aksi tanpa asersi (bagian 8b butir 8).
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected b TC-FA-RP-300 diasersi di spec 291 (kelas g, absence log) dengan aksi nyata dan baseline sendiri; spec ini mengasersi klausa lain TC-FA-RP-300 (S-05).
- Asersi "tidak muncul toast sukses maupun toast parsial" (langkah 18) diletakkan segera setelah pemicu `[Remove]` dan sebelum asersi dialog blok (bagian 8b butir 11); dialog blok yang tampil menjadi anchor positif sesudahnya.
- Temuan untuk QA:
  - TC-FA-RP-299 dan TC-FA-RP-300 menyebut "Dua sesi; Sesi 2 Total Control" tanpa akun; spec memakai Total Control Siti Rahmawati (Pre-setup #2, aktor utama suite) lewat sesi API karena Sesi 2 hanya memicu perubahan state. Akun aktor Sesi 1 adalah Pre-setup #6 (Hendra Wijaya).
  - Expected c TC-FA-RP-300 menyebut seleksi "tetap dipertahankan" setelah `[OK]` tanpa angka; spec mengasersi Bulk Action Bar dan seleksi tampil.
