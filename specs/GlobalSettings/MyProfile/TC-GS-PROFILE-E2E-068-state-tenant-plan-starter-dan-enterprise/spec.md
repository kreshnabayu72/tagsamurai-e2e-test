---
id: TC-GS-PROFILE-E2E-068-state-tenant-plan-starter-dan-enterprise
title: "State Tenant: Plan Starter dan Enterprise Tanpa Gating pada Change Password dan Edit Photo"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-303
  - TC-GS-PROFILE-304
coverage:
  web: automated
---

# State Tenant: Plan Starter dan Enterprise Tanpa Gating pada Change Password dan Edit Photo

## Prerequisites

- Mode: FE+BE.
- Akun aktor (ganti akun eksplisit): Total Control Pre-setup #14 (Client plan Starter) `totalControlStarter_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_STARTER_PASSWORD`), login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Total Control Pre-setup #15 (Client plan Enterprise) `totalControlEnterprise_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_ENTERPRISE_PASSWORD`). Password baru `N3wPassw0rd!` (Data Dinamis #3, `Spectra.env.PROFILE_PASSWORD_NEW`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup: #14 (plan Starter), #15 (plan Enterprise), file uji Pre-setup #17 `valid-photo.png`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE yang memulihkan password akun #14 dan #15 ke nilai awal dan foto akun #14 dan #15 ke keadaan awal (pemulihan akun #14 dan #15 tidak tercakup hook `after` suite, lihat Temuan untuk QA).
- State global yang diubah: password dan foto profil akun #14 dan #15. Dipulihkan oleh langkah pemulihan antar blok dan di akhir spec. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-303: Plan Starter, Change Password dan Edit Photo tanpa gating tier

1. Klik [Change Password]
2. Isi Current Password `Spectra.env.GS_PROFILE_STARTER_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
3. Verifikasi toast sukses `Success, your password has been updated.` tampil
4. Hover Avatar, klik [Edit], pilih file `valid-photo.png`
5. Verifikasi toast sukses `Success, photo has been updated.` tampil
6. Verifikasi tidak ada upsell, batasan, atau pesan gating plan
7. Fixture BE memulihkan password dan foto akun #14 ke nilai awal hingga tersimpan

### TC-GS-PROFILE-304: Plan Enterprise, Change Password dan Edit Photo tanpa gating tier

8. Ganti akun: klik Logout, lalu login sebagai Pre-setup #15 dengan `Spectra.env.GS_PROFILE_ENTERPRISE_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile
9. Klik [Change Password]
10. Isi Current Password `Spectra.env.GS_PROFILE_ENTERPRISE_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
11. Verifikasi toast sukses `Success, your password has been updated.` tampil
12. Hover Avatar, klik [Edit], pilih file `valid-photo.png`
13. Verifikasi toast sukses `Success, photo has been updated.` tampil
14. Verifikasi tidak ada upsell, batasan, atau pesan gating plan

### Pemulihan state

15. Fixture BE memulihkan password dan foto akun #15 ke nilai awal hingga tersimpan

## Notes

- Kelas h (perubahan plan tier) dengan dua blok identik yang berdiri sendiri; ganti akun memakai Step eksplisit (langkah 8) dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. TC write-lockdown (Client Suspended dan Expired) berada di spec 069 karena kondisi data dan fixture status Client berbeda.
- Langkah penghubung (S-03): langkah 7 dan 15 memulihkan password dan foto antar blok (S-09); langkah 8 mengganti akun dan membuka My Profile.
- Temuan untuk QA:
  - Hook `after` suite hanya memulihkan password #7, #18, dan #24; Change Password sukses pada akun #14 dan #15 mengubah password keduanya sehingga pemulihan ditulis spec sendiri (R-08) lewat fixture BE yang disediakan tim FE/BE.
  - TC-GS-PROFILE-303 dan 304 mengharapkan "tidak ada upsell, batasan, atau pesan gating plan" tanpa menyebut elemen yang diperiksa; spec mengasersi satu klausa tanpa elemen spesifik.
  - Pre-setup #14 dan #15 tidak menyebut keadaan foto dan password awal; spec memulihkan "ke nilai awal" lewat fixture BE.
