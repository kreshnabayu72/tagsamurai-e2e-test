---
id: TC-AUTH-SES-E2E-008-dialog-lifecycle-di-dalam-produk-lain
title: "Dialog Lifecycle Sesi Tampil di Dalam Admin Console, Supply Asset, dan Fixed Asset"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-290
  - TC-AUTH-SES-291
  - TC-AUTH-SES-292
coverage:
  web: automated
---

# Dialog Lifecycle Sesi Tampil di Dalam Admin Console, Supply Asset, dan Fixed Asset

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-291: `Mega Santoso` (`megasantoso+{runId}-008@qwertysystem.net`), user Principal staff (profil PRINC, Tabel Data Uji Pre-setup #20) dengan sesi Admin Console Active di Browser A (dibuat di hook `before` lewat login API).
  - TC-AUTH-SES-292: `Reza Kusuma` (`rezakusuma+{runId}-008@qwertysystem.net`), profil BASE milik Client Suspend (Tabel Data Uji Pre-setup #16; di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend, Tabel Data Uji Pre-setup #32) dengan sesi-produk Supply Asset Active di Browser A (dibuat di hook `before` lewat login API dan masuk Supply Asset).
  - TC-AUTH-SES-290: `Taufik Setiawan` (`taufiksetiawan+{runId}-008@qwertysystem.net`), profil BASE milik Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota 2) dengan App Access Fixed Asset dan Supply Asset, batas idle Client Q2 15 menit (diatur di `Global Settings > General Settings` oleh akun aktor Total Control dengan scope Client Q2, Tabel Data Uji Pre-setup #26, di hook `before`), sesi-produk Fixed Asset Active di Browser A pada halaman di dalam Fixed Asset (dibuat di hook `before` lewat login API dan masuk Fixed Asset).
- Browser A adalah konteks terpisah per user uji; TC berikutnya menutup konteks TC sebelumnya dan membuka konteks Browser A baru dengan sesi seed milik user TC itu di langkah pembukanya.
- Browser Admin: konteks terpisah dari Browser A, login oleh akun aktor Total Control (Global Settings) di hook `before` (TC-AUTH-SES-291). Untuk TC-AUTH-SES-292 konteks Browser Admin ditutup dan konteks baru dibuka lewat langkah eksplisit dengan akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Principal staff Admin Console, Tabel Data Uji Pre-setup #4, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`).
- Hook `after`: kembalikan jam server uji dan jam browser ke waktu nyata, pulihkan batas idle Client Q2 ke nilai awal; pulihkan status Client Suspend ke Active (Unsuspend oleh akun aktor Principal Admin Console); kembalikan sesi Browser Admin ke akun default (Total Control Global Settings); akhiri semua sesi uji; tutup Browser A dan Browser Admin; hapus ketiga user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Toggle Active `Mega Santoso`, status Client Suspend (Suspended), batas idle Client Q2 (15 menit), serta jam server uji dan jam browser (diatur bersama), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel untuk TC-AUTH-SES-290): jam server dan jam browser/perangkat diatur bersama dan dapat dimajukan dengan presisi menit (Tabel Data Uji Pre-setup #18), sehingga diteruskan ke timer idle web; dua konteks browser bersamaan; push dialog lifecycle lewat SSE ke Browser A pada halaman Admin Console, Supply Asset, dan Fixed Asset; observasi Browser A tanpa interaksi selama 10 detik; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A; akun aktor pada Browser Admin.

## Test Steps

### TC-AUTH-SES-291: Dialog Account Deactivated tampil saat user berada di dalam Admin Console

1. Di Browser A pastikan halaman Admin Console tampil untuk `megasantoso+{runId}-008@qwertysystem.net` → halaman Admin Console tampil
2. Di Browser Admin buka `Global Settings > User` dan cari `Mega Santoso` (`megasantoso+{runId}-008@qwertysystem.net`)
3. Nonaktifkan Toggle Active `Mega Santoso` → Toggle Active OFF
4. Amati Browser A tanpa interaksi selama 10 detik
5. Verifikasi Dialog "Account Deactivated" tampil di atas halaman Admin Console
6. Verifikasi Body "Your account has been deactivated. You will be logged out."
7. Verifikasi Tombol [OK]

### TC-AUTH-SES-292: Dialog Access Restricted tampil saat user berada di dalam Supply Asset

8. Tutup konteks Browser A TC sebelumnya, buka konteks Browser A baru dengan sesi seed milik `rezakusuma+{runId}-008@qwertysystem.net`, lalu pastikan halaman Supply Asset tampil untuk `rezakusuma+{runId}-008@qwertysystem.net` → halaman Supply Asset tampil
9. Tutup konteks Browser Admin akun Total Control (Global Settings), buka konteks Browser Admin baru, lalu login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD` → halaman beranda akun Principal Admin Console tampil
10. Di Browser Admin buka `Admin Console > Client` → halaman daftar Client tampil
11. Buka menu elipsis Client Suspend (Tabel Data Uji Pre-setup #16) dan pilih Suspend, lalu konfirmasi sampai Client berstatus Suspended
12. Amati Browser A tanpa interaksi selama 10 detik
13. Verifikasi Dialog "Access Restricted" tampil di atas halaman Supply Asset
14. Verifikasi Body "Your organization's access has been suspended. You can still view data, but write actions are disabled until access is restored."
15. Verifikasi Tombol [OK]

### TC-AUTH-SES-290: Dialog Session Expired tampil saat user berada di halaman dalam Fixed Asset

16. Tutup konteks Browser A TC sebelumnya, buka konteks Browser A baru dengan sesi seed milik `taufiksetiawan+{runId}-008@qwertysystem.net`, lalu pastikan halaman di dalam Fixed Asset tampil untuk `taufiksetiawan+{runId}-008@qwertysystem.net` → halaman Fixed Asset tampil
17. Biarkan Browser A tanpa aktivitas
18. Majukan jam server uji dan jam browser bersama 16 menit
19. Verifikasi Dialog "Session Expired" tampil di atas halaman Fixed Asset
20. Verifikasi Body "Your session has expired due to inactivity."
21. Verifikasi Tombol [Refresh]

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (jam server) hanya pada TC-AUTH-SES-290.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-291, 292, lalu 290 (urutan TC sumber 290, 291, 292). TC-AUTH-SES-290 memajukan jam server uji 16 menit sehingga ditaruh paling akhir agar sesi Browser A TC-AUTH-SES-291 dan 292 yang di-seed di hook `before` tidak menua oleh pergeseran jam. TC-AUTH-SES-291 memakai akun Total Control yang sudah login di Browser Admin dari hook, lalu ganti akun ke Principal untuk TC-AUTH-SES-292.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): memastikan halaman produk tampil di Browser A (langkah 1, 8, 16), menutup konteks Browser A TC sebelumnya dan membuka konteks Browser A baru (langkah 8 dan 16), serta mengganti konteks Browser Admin ke akun Principal (langkah 9).
- Asersi pencatatan sesi untuk ketiga kejadian tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) Tabel Data Uji Dinamis baris 294 menamai skenario TC-AUTH-SES-291 "Dialog Log Out tampil saat user berada di dalam Admin Console", sedangkan skenario dan Expected TC-AUTH-SES-291 adalah Account Deactivated; spec mengikuti Skenario dan Expected TC. (2) TC-AUTH-SES-290, 291, dan 292 tidak menyebut cara user dibawa ke halaman di dalam produk (Admin Console, Supply Asset, Fixed Asset) dan tidak menyebut login; spec men-seed sesi di hook `before` dan memakai langkah penghubung "pastikan halaman tampil". (3) TC-AUTH-SES-291 tidak menyebut Client user Principal staff dan batas idle; spec mengikuti Tabel Data Uji Pre-setup #20. (4) TC-AUTH-SES-290 tidak menyebut waktu tunggu setelah memajukan jam; spec memverifikasi dialog langsung setelah pergeseran jam (bila perlu penyesuaian jeda polling/timer klien, dicatat sebagai kebutuhan teknis di Prerequisites). (5) TC-AUTH-SES-292 menyebut Browser Admin untuk aksi akun Principal, sedangkan Tabel Data Uji Pre-setup #1 mendefinisikan Browser Admin sebagai konteks akun Total Control; spec membuka konteks Browser Admin baru dengan akun Principal. (6) TC-AUTH-SES-291 dan 292 menyebut "tombol [OK]" tanpa variant dan severity dialog; spec tidak menambahnya.
