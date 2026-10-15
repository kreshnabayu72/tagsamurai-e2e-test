---
id: TC-AUTH-SES-E2E-007-dialog-lifecycle-lintas-role-dan-entitas
title: "Dialog Lifecycle Sesi Tampil Sama untuk Role Read Only, Entitas Distributor, dan Entitas Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-17
  - TC-AUTH-SES-18
  - TC-AUTH-SES-19
coverage:
  web: automated
---

# Dialog Lifecycle Sesi Tampil Sama untuk Role Read Only, Entitas Distributor, dan Entitas Partner

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-17: `Bayu Nugroho` (`bayunugroho+{runId}-007@qwertysystem.net`), milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5) dengan role Read Only (Tabel Data Uji Pre-setup #3); user Activated, Active ON. Sesi web aktif di Browser A (Chrome on Windows), status Active, dibuat di hook `before` lewat login API.
  - TC-AUTH-SES-19: `Joko Wijaya` (`jokowijaya+{runId}-007@qwertysystem.net`), user entitas Partner (staff, Tabel Data Uji Pre-setup #20); Activated, Active ON. Sesi web aktif di Browser A, status Active, dibuat di hook `before` lewat login API.
  - TC-AUTH-SES-18: `Intan Maulana` (`intanmaulana+{runId}-007@qwertysystem.net`), user entitas Distributor (staff, Tabel Data Uji Pre-setup #20) dengan batas idle entitas Distributor 15 menit; Activated, Active ON. Sesi web dibuat oleh langkah login di `## Test Steps` (alasan di Notes).
- Browser A dan Browser B adalah konteks terpisah per user uji. Browser B untuk TC-AUTH-SES-17 dan 19 adalah konteks baru yang belum login; TC berikutnya menutup konteks TC sebelumnya dan membuka konteks baru di langkah pembukanya.
- Hook `after`: kembalikan jam server uji dan jam browser ke waktu nyata, akhiri semua sesi uji, tutup Browser A dan B, hapus ketiga user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser (diatur bersama, TC-AUTH-SES-18), dipulihkan di hook `after`. Batas idle entitas Distributor (15 menit) dibaca, tidak diubah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel untuk TC-AUTH-SES-18): jam server dan jam browser/perangkat diatur bersama dan dapat dimajukan dengan presisi menit (Tabel Data Uji Pre-setup #18), sehingga diteruskan ke timer idle web; dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows untuk Browser A); push dialog lifecycle lewat SSE ke Browser A yang membuka Portal — Product Hub dengan sesi seed (TC-AUTH-SES-19); reCAPTCHA mode uji di environment (halaman Login with Password); seeding user entitas Distributor dan Partner yang dapat login lewat halaman Login with Password.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan B.

## Test Steps

### TC-AUTH-SES-17: Dialog Duplicate Login Attempt tampil sama untuk user dengan role Read Only

1. Di Browser B buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik email `bayunugroho+{runId}-007@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog muncul
3. Verifikasi Dialog "Duplicate Login Attempt" tampil
4. Verifikasi Title "Duplicate Login Attempt"
5. Verifikasi Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
6. Verifikasi [Confirm] (variant solid, severity warning) tampil
7. Verifikasi [Cancel] (variant text, severity contrast) tampil
8. Verifikasi Dialog identik dengan Dialog pada TC-AUTH-SES-1 (Title, Body, [Confirm], dan [Cancel] sama; teks Body, label, dan variant tombol tidak berbeda karena role)
9. Verifikasi Tidak ada elemen yang tersembunyi atau disabled karena role (Title, Body, [Confirm], dan [Cancel] semuanya tampil dan [Confirm] serta [Cancel] enabled)

### TC-AUTH-SES-19: Dialog Logged Out tampil sama untuk user entitas Partner

10. Tutup konteks Browser A dan B TC sebelumnya, lalu buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `jokowijaya+{runId}-007@qwertysystem.net`, lalu pastikan Browser A menampilkan Portal — Product Hub → halaman Portal — Product Hub tampil
11. Di Browser B buka halaman `Auth > Login with Password` dalam konteks baru yang belum login → halaman Login with Password tampil
12. Login sebagai `jokowijaya+{runId}-007@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → Dialog Duplicate Login Attempt muncul
13. Klik [Confirm] pada Dialog Duplicate Login Attempt
14. Pindah ke Browser A → Dialog muncul
15. Verifikasi Dialog "Logged Out" tampil di Browser A
16. Verifikasi Body "You have been logged out because another session was started on a different device."
17. Verifikasi [OK] sebagai satu-satunya tombol
18. Verifikasi Dialog sama dengan Dialog Logged Out pada TC-AUTH-SES-2 (Title, Body, dan [OK] sebagai satu-satunya tombol)

### TC-AUTH-SES-18: Dialog Session Expired tampil sama untuk user entitas Distributor

19. Tutup konteks Browser A dan B TC sebelumnya, buka konteks Browser A baru (Chrome on Windows, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
20. Login web sebagai `intanmaulana+{runId}-007@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → halaman Portal — Product Hub tampil
21. Biarkan Browser A tanpa aktivitas
22. Majukan jam server uji dan jam browser bersama 16 menit → Dialog muncul
23. Verifikasi Dialog "Session Expired" tampil
24. Verifikasi Body "Your session has expired due to inactivity."
25. Verifikasi Satu tombol [Refresh] sebagai satu-satunya tombol
26. Verifikasi Dialog identik dengan Dialog Session Expired untuk user Client
27. Verifikasi Tidak ada perbedaan tampilan Dialog karena jenis entitas

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (jam server) hanya pada TC-AUTH-SES-18.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-17, 19, lalu 18 (urutan TC sumber 17, 18, 19). TC-AUTH-SES-18 memajukan jam server uji 16 menit sehingga ditaruh paling akhir; sesi Browser A TC-AUTH-SES-17 dan 19 di-seed di hook `before` dan tidak boleh menua oleh pergeseran jam sebelum dipakai. Sesi TC-AUTH-SES-18 dibuat oleh langkah 19-20 (langkah TC dependensi TC-AUTH-SES-3 disalin sebagai langkah, S-04).
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-17 dari TC-AUTH-SES-1 (login di Browser B hingga Dialog Duplicate Login Attempt tampil; langkah 1-2); TC-AUTH-SES-19 dari TC-AUTH-SES-2 (login di Browser B, klik [Confirm], pindah ke Browser A; langkah 12-14); TC-AUTH-SES-18 dari TC-AUTH-SES-3 (login web dan masuk Portal — Product Hub, idle, majukan jam; langkah 20-22). Asersi screening penuh (severity, modal, tombol silang) pada dialog sumber diuji di spec `TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out` dan `TC-AUTH-SES-E2E-004-screening-session-expired-dan-idle-warning-web`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks TC sebelumnya dan membuka konteks browser bersih (langkah 10, 11, dan 19); memastikan Browser A menampilkan Portal — Product Hub sebelum Browser B login (langkah 10), karena Dialog Logged Out harus tiba lewat push SSE ke halaman app yang terbuka dan Browser A hasil seeding API belum membuka halaman app; perpindahan antar Browser A dan B.
- Asersi pencatatan sesi untuk ketiga kejadian tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-17 menyebut user `Bayu Nugroho` dengan role Read Only (Tabel Data Uji Pre-setup #3 adalah akun aktor Read Only Global Settings), sementara Tabel Data Uji Dinamis memberi profil BASE; spec men-seed user baru dengan role Read Only. (2) TC-AUTH-SES-17 Expected a menyebut dialog "identik dengan screening Dialog untuk role lain" tanpa merinci; spec memverifikasi Title, Body, [Confirm], dan [Cancel] per elemen dengan teks dan variant dari TC-AUTH-SES-1, lalu satu `Verifikasi` untuk kesimpulan dialog identik. (3) TC-AUTH-SES-18 menyebut batas idle entitas Distributor 15 menit tanpa mengatakan cara men-seed-nya; spec menganggapnya kondisi BE yang di-seed. (4) TC-AUTH-SES-18 dan 19 tidak menyebut cara membuat user Distributor dan Partner (staff) dapat login dengan Login with Password; ditulis sebagai kebutuhan seeding di Prerequisites. (5) TC-AUTH-SES-17, 18, dan 19 tidak menyebut reCAPTCHA; spec mengikuti TC.
