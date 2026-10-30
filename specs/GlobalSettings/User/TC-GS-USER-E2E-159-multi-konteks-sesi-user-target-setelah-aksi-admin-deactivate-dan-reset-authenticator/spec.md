---
id: TC-GS-USER-E2E-159-multi-konteks-sesi-user-target-setelah-aksi-admin-deactivate-dan-reset-authenticator
title: "Multi-Konteks: Sesi Browser User Target Berakhir Setelah Admin Deactivate dan Tetap Berjalan Setelah Admin Reset Authenticator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-243
  - TC-GS-USER-331
coverage:
  web: automated
---

# Multi-Konteks: Sesi Browser User Target Berakhir Setelah Admin Deactivate dan Tetap Berjalan Setelah Admin Reset Authenticator

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (sesi utama): Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Akun target di jendela browser kedua (Browser B), hasilnya diasersi: user seed milik spec (U-1 untuk TC-GS-USER-243, U-2 untuk TC-GS-USER-331), kredensial `Spectra.env.USER_PASSWORD` (memenuhi policy password). Browser B dibuka dan ditutup di dalam tiap blok TC.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai sebagai target aksi dan tidak diubah.
- Data Dinamis, di-seed lewat API di hook `before` (HK1; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD). Semua user Activated, Division `Finance`, Access `Fixed Asset`, tanpa approval, nilai field wajib lain seragam:
  - U-1: Name `Dewi Lestari {runId}-159`, email `dewilestari+{runId}-159@qwertysystem.net`, password `Spectra.env.USER_PASSWORD` (target TC-GS-USER-243).
  - U-2: Name `John Doe {runId}-159`, email `johndoe+{runId}-159@qwertysystem.net`, MFA Enrolled, password `Spectra.env.USER_PASSWORD` (target TC-GS-USER-331).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD):
  - Dua jendela browser: sesi utama dan Browser B yang login sebagai user target (satu sesi target pada satu waktu).
  - Seeding status MFA Enrolled pada U-2 lewat API; login U-2 di Browser B yang memenuhi MFA; login ulang U-2 yang menampilkan halaman enrollment authenticator sesudah di-reset.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 dan U-2 lewat API, tutup Browser B bila masih terbuka dan hapus sesi loginnya.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Pembukaan layar

1. Klik icon Search, ketik `{runId}-159`, tekan Enter

### TC-GS-USER-243: Deactivate dikonfirmasi, user Inactive dan sesi aktifnya diakhiri

2. Buka jendela Browser B dan login sebagai `Dewi Lestari {runId}-159` dengan `Spectra.env.USER_PASSWORD`
3. Kembali ke jendela akun aktor
4. Klik switch Active baris `Dewi Lestari {runId}-159`
5. Klik `[Deactivate]`
6. Verifikasi toast sukses "Success, user has been deactivated."
7. Verifikasi switch Active baris `Dewi Lestari {runId}-159` OFF
8. Beralih ke jendela Browser B (sesi `Dewi Lestari {runId}-159`)
9. Verifikasi sesi `Dewi Lestari {runId}-159` di Browser B langsung berakhir
10. Tutup jendela Browser B dan hapus sesi login terkait
11. Kembali ke jendela akun aktor

### TC-GS-USER-331: Reset Authenticator tidak memutus sesi aktif target

12. Buka jendela Browser B dan login sebagai `John Doe {runId}-159` dengan `Spectra.env.USER_PASSWORD` (memenuhi MFA)
13. Kembali ke jendela akun aktor
14. Klik Name `John Doe {runId}-159` di User List
15. Klik `Reset Authenticator` → `[Reset]`
16. Tunggu aksi selesai (Badge diganti teks muted `Not enrolled yet`)
17. Beralih ke jendela Browser B (sesi `John Doe {runId}-159`)
18. Buka halaman lain di Browser B
19. Verifikasi sesi `John Doe {runId}-159` di Browser B tetap berjalan (halaman lain tampil dan tidak diarahkan ke halaman Login)
20. Logout di Browser B lalu login lagi sebagai `John Doe {runId}-159`
21. Verifikasi login `John Doe {runId}-159` di Browser B meminta enrollment authenticator ulang
22. Tutup jendela Browser B dan hapus sesi login terkait
23. Kembali ke jendela akun aktor

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Kelas c (multi-konteks): jendela Browser B milik user target menjadi objek asersi (sesi berakhir pada TC-GS-USER-243; sesi tetap berjalan dan permintaan enrollment ulang pada TC-GS-USER-331) setelah admin bertindak di sesi utama. Karena itu bukan pemicu P-2 dan spec ini berdiri sendiri.
- Subjudul `###` memetakan langkah ke id TC sumber.
- TC-GS-USER-243 diverifikasi seluruhnya di spec ini (Expected a, b, c); TC-GS-USER-331 diverifikasi seluruhnya di spec ini (Expected a, b). TC-GS-USER-243 diverifikasi di spec 159 dan TC-GS-USER-331 diverifikasi di spec 159; spec 047 dan spec 058 memuat TC lain di layar yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search), 2 sampai 5 dan 12 sampai 15 (membuka Browser B, berpindah jendela, aksi pemicu), 10, 11, 22 dan 23 (menutup Browser B, S-09), 16 (Tunggu aksi selesai), 17, 18 dan 20 (pengamatan di Browser B).
- Dua user seed terpisah karena U-1 berstatus Inactive setelah TC-GS-USER-243 dan sesi U-1 sudah berakhir, sedangkan TC-GS-USER-331 membutuhkan user Activated MFA Enrolled dengan sesi yang masih berjalan.
- Temuan untuk QA:
  - TC-GS-USER-243 Post Condition a (toggle per-produk tidak dipaksa OFF) dan b (terdampak approver dropdown FAMS dan Auth login diblok) tanpa langkah observasi; tidak diasersi (a dicakup TC-GS-USER-250 di spec 047).
  - TC-GS-USER-243 butir c ("sesi langsung berakhir") tidak menyebut tampilan akhir sesi di browser lain; spec mengasersi sesi berakhir tanpa menyebut halaman tujuan.
  - TC-GS-USER-243 memakai user Pre-setup Dewi Lestari; spec memakai user seed milik spec agar data Pre-setup tidak berubah.
  - TC-GS-USER-331: precondition "John Doe sedang login di browser lain" dan "login berikutnya diminta enrollment ulang" tidak menyebut mekanisme login user ber-MFA di browser lain dan tampilan halaman enrollment; disediakan tim FE/BE. Kolom Automation bernilai Manual Only.
  - TC-GS-USER-331 langkah 2 ("Reset Authenticator (konfirmasi)") dan "Di browser John Doe, buka halaman lain" tidak menyebut halaman yang dibuka; spec membuka halaman lain di Browser B tanpa menyebut tujuan.
  - TC-GS-USER-331 memakai user Pre-setup John Doe; spec memakai user seed milik spec agar data Pre-setup tidak berubah.
