---
id: TC-AUTH-SES-E2E-043-manual-logout
title: "Manual Logout di Web: Akhiri Sesi, Sesi-Produk Anak, dan Logout Saat Sesi Expired"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-140
  - TC-AUTH-SES-141
  - TC-AUTH-SES-142
coverage:
  web: automated
---

# Manual Logout di Web: Akhiri Sesi, Sesi-Produk Anak, dan Logout Saat Sesi Expired

## Prerequisites

- Mode: FE+BE.
- Client uji:
  - Client Alpha `Alpha Logistik` (Tabel Data Uji Pre-setup #5): batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5.
  - Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) masing-masing Client (Client Alpha: Tabel Data Uji Pre-setup #1; Client Q2: scope Client Q2, Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-140: `Taufik Anggraini` (`taufikanggraini+{runId}-043@qwertysystem.net`), Client Alpha; sesi web Active di Browser A (Chrome on Windows).
  - TC-AUTH-SES-141: `Mega Wibowo` (`megawibowo+{runId}-043@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset; sesi platform web dan sesi-produk Fixed Asset Active di Browser A (seat terpakai 1).
  - TC-AUTH-SES-142: `Reza Nugroho` (`rezanugroho+{runId}-043@qwertysystem.net`), Client Alpha; sesi web Active di Browser A (dibuat di `before`; dikedaluwarsakan pada langkah spec).
  - Browser A tiap TC = konteks browser yang memuat sesi web user TC bersangkutan (satu konteks per user, dibuat di `before` lewat login API).
- Akun aktor lain (login di hook `before`, satu konteks browser per akun):
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License di Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) pada TC-AUTH-SES-141.
  - Browser Admin Alpha dan Browser Admin Q2: akun aktor Total Control (Global Settings) masing-masing Client (Alpha: Tabel Data Uji Pre-setup #1; Q2: scope Client Q2, Tabel Data Uji Pre-setup #26; `Spectra.env.GS_TC_PASSWORD`). Browser Admin Alpha membaca `Global Settings > Activity Log > Session` (TC-AUTH-SES-140). Browser Admin Q2 membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log` (TC-AUTH-SES-141).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): kembalikan jam server uji ke waktu nyata, lepaskan penahanan heartbeat di proxy jaringan, akhiri semua sesi seed dan sesi-produk, tutup semua konteks browser, hapus ketiga user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server (hanya pada TC-AUTH-SES-142, hanya jam server yang dimajukan dan dipulihkan sebelum Log Out; jam browser/perangkat tidak diubah) dan penahanan request heartbeat Browser A lewat proxy jaringan (Tabel Data Uji Pre-setup #18); keduanya dipulihkan lewat langkah eksplisit dan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan (Browser A, Browser License, Browser Admin Alpha, Browser Admin Q2); jam server dapat dimajukan sendiri (tanpa jam browser/perangkat) dan dipulihkan ke waktu nyata (TC-AUTH-SES-142); proxy jaringan yang dapat menahan request heartbeat Browser A supaya dialog Session Expired belum tampil (TC-AUTH-SES-142); pembacaan status sesi web dan sesi-produk milik user uji dari sisi backend, disediakan tim FE/BE; pembacaan hitungan seat aktif dan baris sesi-produk di License > Concurrent User.
- Akun yang dipakai: user uji pada Browser A; Browser License dan Browser Admin memakai akun aktor di atas.

## Test Steps

### TC-AUTH-SES-140: Manual Logout mengakhiri sesi dan mengarah ke halaman Login

1. Di Browser Admin Alpha catat baseline jumlah entri `Logged out` `Taufik Anggraini` di `Global Settings > Activity Log > Session`; di Browser A (sesi `Taufik Anggraini`) klik menu Profile di navbar lalu pilih Log Out
2. Verifikasi Browser A diarahkan ke halaman Login with Password
3. Verifikasi Sesi web `Taufik Anggraini` berstatus Logged Out
4. Di Browser Admin Alpha buka `Global Settings > Activity Log > Session`
5. Verifikasi Entri `Logged out` untuk `Taufik Anggraini` (dicari berdasarkan Note dan email) bertambah 1 dari baseline

### TC-AUTH-SES-141: Manual Logout mengakhiri sesi-produk anak dan melepas seat

6. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan catat hitungan seat aktif serta baris `Mega Wibowo`
7. Di Browser Admin Q2 buka `Global Settings > Activity Log > Session` dan catat baseline jumlah entri `Session ended` `Mega Wibowo`
8. Di Browser Admin Q2 buka `Activity Log > Session` milik Fixed Asset dan catat baseline jumlah entri `Session ended` `Mega Wibowo`
9. Di Browser Admin Q2 buka `Global Settings > User > Detail > User Log` milik `Mega Wibowo` dan catat baseline jumlah entri `Session ended (Fixed Asset)`
10. Di Browser A (sesi `Mega Wibowo`) klik menu Profile lalu pilih Log Out
11. Di Browser License muat ulang daftar License > Concurrent User
12. Verifikasi Sesi-produk Fixed Asset `Mega Wibowo` berstatus Ended
13. Verifikasi Seat dilepas
14. Verifikasi Baris `Mega Wibowo` hilang dari daftar
15. Verifikasi Hitungan seat aktif berkurang 1
16. Di Browser Admin Q2 muat ulang `Global Settings > Activity Log > Session`
17. Verifikasi Entri `Session ended` untuk `Mega Wibowo` (dicari berdasarkan Note dan email) bertambah 1 dari baseline di `Global Settings > Activity Log > Session`, per sesi-produk anak
18. Di Browser Admin Q2 muat ulang `Activity Log > Session` milik Fixed Asset
19. Verifikasi Entri `Session ended` untuk `Mega Wibowo` (dicari berdasarkan Note dan email) bertambah 1 dari baseline di `Activity Log > Session` milik Fixed Asset
20. Di Browser Admin Q2 muat ulang `Global Settings > User > Detail > User Log` milik `Mega Wibowo`
21. Verifikasi User Log `Mega Wibowo` menampilkan entri baru `Session ended (Fixed Asset)` (jumlah bertambah 1 dari baseline)

### TC-AUTH-SES-142: Logout saat sesi sudah expired bersifat idempotent dan mengarah ke Login

22. Tahan request heartbeat Browser A (sesi `Reza Nugroho`) lewat proxy jaringan
23. Majukan hanya jam server 16 menit (jam browser/perangkat tidak diubah) sehingga sesi web `Reza Nugroho` Expired sementara Browser A belum menampilkan dialog
24. Pulihkan jam server ke waktu nyata (sebelum Log Out)
25. Di Browser A klik menu Profile lalu pilih Log Out
26. Verifikasi Browser A diarahkan ke halaman Login
27. Verifikasi Status sesi web `Reza Nugroho` tetap Expired
28. Lepaskan penahanan heartbeat Browser A di proxy jaringan

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AUTH-SES-143 (kegagalan server saat Manual Logout) tidak termasuk spec ini. TC-AUTH-SES-144 ada di spec `TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile`.
- Urutan (S-10): urutan di spec ini TC-AUTH-SES-140, 141, 142, sama dengan urutan TC sumber. TC 142 memajukan jam sehingga ditaruh paling akhir; memajukan jam membuat sesi platform lain kedaluwarsa.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): memuat ulang daftar License > Concurrent User di Browser License; mencatat hitungan seat aktif sebelum Log Out (S-14); mencatat baseline jumlah entri log dan memuat ulang surface log di Browser Admin (langkah 7 s.d. 9, 16, 18, 20; S-12); langkah 22 menahan heartbeat Browser A agar kondisi "dibaca stale" TC-AUTH-SES-142 terbentuk; langkah 24 memulihkan jam server sebelum Log Out sesuai Precondition b TC-AUTH-SES-142 dan langkah 28 melepas penahanan heartbeat (hook `after` sebagai cadangan; S-09).
- Butir c TC-AUTH-SES-140 ("Dicatat `Logged out`") hanya diasersikan kemunculan entri; kolom Activity, Status, Note, dan keunikan entri diasersikan di TC-AUTH-SES-197 (spec pencatatan). Butir b TC-AUTH-SES-142 ("Tidak ada entri log baru") adalah asersi absence; tidak diasersikan di spec ini dan dirujuk ke spec absence `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin` (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-141 Langkah 3 tidak menyebut akun yang membuka `Activity Log > Session` milik Fixed Asset dan User Log; spec memakai akun Total Control Client Q2 (Pre-setup #26) di Browser Admin Q2. (2) TC-AUTH-SES-142 Precondition b ("Browser A belum menampilkan dialog, sesi dibaca stale") tidak menyebut cara membentuk kondisi itu; spec menahan heartbeat lewat proxy jaringan lalu memajukan hanya jam server (jam browser/perangkat tidak diubah, pengecualian bagian 6 untuk TC-AUTH-SES-142) dan memulihkannya sebelum Log Out (kemampuan teknis di Prerequisites). (3) TC-AUTH-SES-140, 141, 142 menulis tombol Log Out sebagai menu Profile di navbar tanpa menyebut label tombol yang sebenarnya; spec mengikuti TC. (4) Alur login pada TC modul ini tidak menyebut widget reCAPTCHA; spec ini tidak memuat langkah login user uji (sesi seed dibuat di hook), sehingga tidak terdampak.
- Baseline log (S-12): jumlah entri dicatat di langkah 1 dan 7 s.d. 9 sebelum aksi; asersi log mencari entri berdasarkan Note dan email dan mengasersi selisih jumlah. Jam baru digeser pada TC-AUTH-SES-142 (setelah bagian log) dan dipulihkan di langkah 24 serta hook `after`.
