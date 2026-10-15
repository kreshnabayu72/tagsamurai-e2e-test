---
id: TC-AUTH-ACT-E2E-029-absence-pencatatan-aksi-admin
title: "Tidak Ada Pencatatan oleh Auth Account Activation dari Aksi Admin dan Login"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-96
  - TC-AUTH-ACT-97
coverage:
  web: automated
---

# Tidak Ada Pencatatan oleh Auth Account Activation dari Aksi Admin dan Login

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.ACT_PASSWORD` (hanya TC-AUTH-ACT-98). Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-029` beserta link aktivasinya, semuanya Pending Activation dengan token Active kecuali disebut lain:
  - TC-AUTH-ACT-97: `Hendra Hidayat` (`hendrahidayat+{runId}-029@qwertysystem.net`), cooldown Resend Activation Email untuk user ini ditunggu eksplisit di langkah sebelum Resend.
  - TC-AUTH-ACT-98 (absence): `Maya Ramadhan` (`mayaramadhan+{runId}-029@qwertysystem.net`)
- TC-AUTH-ACT-96 membuat user `Rina Puspita` (`rinapuspita+{runId}-029@qwertysystem.net`) lewat UI.
- Hook `after` menghapus semua user di atas, termasuk `Rina Puspita` (tetap jalan walau seeding atau langkah gagal sebagian).
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik untuk login TC-AUTH-ACT-98); reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-ACT-98 (absence): Penolakan login user belum aktivasi tidak menulis entri dari Auth Account Activation

1. Di jendela privat, buka `Auth > Login > Login with Password`, isi Email `mayaramadhan+{runId}-029@qwertysystem.net`, isi Password `Spectra.env.ACT_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
2. Verifikasi Pesan "Your account has not been activated" tampil
3. Pada browser admin, buka `Global Settings > Activity Log > Session` dan cari entri untuk email `mayaramadhan+{runId}-029@qwertysystem.net`
4. Verifikasi Activity Log (Session) memuat entri Failed dengan Note `Account is not activated` yang berasal dari modul Login (jangkar: entri sudah terindeks dan pencarian benar)
5. Verifikasi Tidak ada entri bertanda aktivasi atau Set Password dari Auth Account Activation untuk user `Maya Ramadhan`
6. Verifikasi Status user `Maya Ramadhan` tetap Pending Activation

### TC-AUTH-ACT-96: Pembuatan user dan pengiriman Activation Email tidak menambah entri pencatatan dari Auth

7. Buka `Global Settings > User > Login User > Popup Create User` sebagai admin, buat user `Rina Puspita` dengan Email `rinapuspita+{runId}-029@qwertysystem.net`, lalu klik [Submit]
8. Buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Rina Puspita`
9. Verifikasi Changelog dan surface log Global Settings > User memuat entri pembuatan user milik modul Global Settings > User (jangkar)
10. Verifikasi Tidak ada entri dari Auth yang mencatat pembuatan token aktivasi atau pengiriman Activation Email pada Activity Log (Session), User Log, System Log, maupun Changelog
11. Verifikasi Token aktivasi user `Rina Puspita` Active; status user Pending Activation

### TC-AUTH-ACT-97: Resend Activation Email yang men-supersede token lama tidak menambah entri pencatatan dari Auth

12. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Hendra Hidayat`
13. Pada browser admin, lakukan Resend Activation Email untuk user `Hendra Hidayat` dari `Global Settings > User > Login User`
14. Buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Hendra Hidayat`
15. Verifikasi Hanya entri Resend Activation Email milik modul pemicu (Global Settings > User) yang muncul
16. Verifikasi Tidak ada entri token superseded atau invalidated dari Auth pada Activity Log (Session), User Log, System Log, maupun Changelog
17. Verifikasi Token lama user `Hendra Hidayat` Superseded dan token baru Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness g (asersi absence), pemicu dari aksi admin dan penolakan login. Absence untuk pemicu halaman publik aktivasi ada di E2E-017.
- TC terbelah lintas spec (prinsip 10): asersi absence TC-AUTH-ACT-98 (Expected c) diuji di spec ini beserta anchor positifnya (pesan penolakan, entri Failed dari modul Login, status tetap Pending Activation) supaya absence tidak lolos hanya karena log belum terindeks; bagian fungsional lain TC-98 ada di E2E-010. Asersi absence TC-AUTH-ACT-11 (pembuatan user di Global Settings dan pengiriman Activation Email) dicakup oleh bagian TC-AUTH-ACT-96 di spec ini; bagian fungsionalnya ada di E2E-023. `sourceTc` tidak mencantumkan TC-98 dan TC-11 supaya tiap TC tetap terpetakan ke satu spec utama di `docs/coverage`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
