---
id: TC-GS-PROFILE-E2E-003-screening-variasi-data-akun
title: "Screening halaman: variasi tampilan per akun (tanpa Employee ID, foto, TAG, plan Starter, Authenticator, Temporary User)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-7
  - TC-GS-PROFILE-8
  - TC-GS-PROFILE-13
  - TC-GS-PROFILE-14
  - TC-GS-PROFILE-16
  - TC-GS-PROFILE-26
coverage:
  web: automated
---

# Screening halaman: variasi tampilan per akun (tanpa Employee ID, foto, TAG, plan Starter, Authenticator, Temporary User)

## Prerequisites

- Mode: FE+BE.
- Spec membaca lima akun berbeda secara berurutan; tiap blok mandiri dan dimulai dengan Step ganti akun eksplisit (langkah 9, 12, 16, dan 23). Akun pertama login di hook `before` spec ini.
- Akun yang diuji (urutan = urutan blok):

| Blok | Pre-setup | Akun | Kondisi data | Env var password |
|---|---|---|---|---|
| 1 | #10 | Fajar Nugroho, `noPhotoProfile_automated_{namaCompany}@qwertysystem.net` | Total Control, tanpa foto, tanpa Employee ID, tanpa TAG, plan Growth | `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD` |
| 2 | #9 | Nadia Putri, `photoProfile_automated_{namaCompany}@qwertysystem.net` | Total Control, foto profil aktif `nadia-photo.jpg` | `Spectra.env.GS_PROFILE_PHOTO_PASSWORD` |
| 3 | #14 | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | Total Control, Client plan Starter | `Spectra.env.GS_PROFILE_STARTER_PASSWORD` |
| 4 | #19 | Gita Savitri, `notEnrolledProfile_automated_{namaCompany}@qwertysystem.net` | Total Control, Authenticator belum enroll | `Spectra.env.GS_PROFILE_NOTENROLLED_PASSWORD` |
| 5 | #21 | Wulan Sari, `temporaryProfile_automated_{namaCompany}@qwertysystem.net` | Temporary User sampai 31/12/26; Date Format General Settings `dd/MM/yy` (kondisi Pre-setup #21 di environment, tidak diubah spec) | `Spectra.env.GS_PROFILE_TEMP_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #10) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Data Dinamis: tidak ada. Spec hanya membaca; foto Pre-setup #9 dan #10 tidak diubah.

## Test Steps

### Akun Fajar Nugroho tanpa Employee ID, tanpa foto, tanpa TAG (TC-GS-PROFILE-7, TC-GS-PROFILE-8, TC-GS-PROFILE-13)

1. Amati subtitle di bawah Full Name pada Header
2. Verifikasi subtitle Employee ID menampilkan `—`
3. Amati Avatar
4. Verifikasi Avatar Fajar Nugroho menampilkan inisial `FN`
5. Amati sub-section User TAG pada Section Identity
6. Verifikasi Badge `Unverified` tampil pada sub-section User TAG
7. Verifikasi teks `No TAG paired` tampil pada sub-section User TAG
8. Verifikasi tidak ada tombol Scan TAG

### Akun Nadia Putri dengan foto (TC-GS-PROFILE-8)

9. Logout, lalu login sebagai Pre-setup #9 (Nadia Putri) dengan `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`
10. Buka My Profile dari account menu navbar
11. Verifikasi Avatar Nadia Putri menampilkan foto `nadia-photo.jpg` dalam lingkaran

### Akun client plan Starter (TC-GS-PROFILE-14)

12. Logout, lalu login sebagai Pre-setup #14 dengan `Spectra.env.GS_PROFILE_STARTER_PASSWORD`
13. Buka My Profile dari account menu navbar
14. Verifikasi Section Identity tampil
15. Verifikasi sub-section User TAG tidak tampil di Section Identity

### Akun Gita Savitri belum enroll Authenticator (TC-GS-PROFILE-16)

16. Logout, lalu login sebagai Pre-setup #19 (Gita Savitri) dengan `Spectra.env.GS_PROFILE_NOTENROLLED_PASSWORD`
17. Buka My Profile dari account menu navbar
18. Amati sub-section Authenticator
19. Verifikasi teks muted `Not enrolled yet` tampil
20. Verifikasi tidak ada Badge `Enrolled`
21. Verifikasi tidak ada teks `Lost your device? Contact your administrator.`
22. Verifikasi tidak ada tombol maupun tautan enrollment

### Akun Wulan Sari Temporary User (TC-GS-PROFILE-26)

23. Logout, lalu login sebagai Pre-setup #21 (Wulan Sari) dengan `Spectra.env.GS_PROFILE_TEMP_PASSWORD`
24. Buka My Profile dari account menu navbar
25. Amati Section Access & Status konteks Global Settings
26. Verifikasi info Temporary User `Temporary until 31/12/26`

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-7, 8, 13, 14, 16, 26).
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); tiap blok tetap bermakna walau blok sebelumnya gagal (bagian 3 butir "Beda akun, role, atau entity" kasus b).
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-PROFILE-8 terbelah menjadi dua blok akun (Fajar Nugroho di blok 1 bersama TC-GS-PROFILE-7 dan TC-GS-PROFILE-13 yang memakai akun yang sama; Nadia Putri di blok 2), supaya ganti akun minimal. Urutan Nadia lalu Fajar pada langkah TC tidak mempengaruhi hasil.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1, 3, 5, 18, dan 25 adalah aksi amati TC; langkah 9, 12, 16, dan 23 adalah Step ganti akun; langkah 10, 13, 17, dan 24 membuka My Profile untuk akun baru (hook `beforeEach` hanya membuka halaman untuk akun hook).
- Asersi absence pada langkah 8, 15, 20, 21, dan 22 didahului `Verifikasi` elemen lain pada halaman yang sama sudah tampil (langkah 6 dan 7 untuk langkah 8; langkah 14 untuk langkah 15; langkah 19 untuk langkah 20 sampai 22).
- Temuan untuk QA:
  - TC-GS-PROFILE-8 memakai langkah login Nadia Putri lalu Fajar Nugroho dengan Precondition "Login sbg Role: Total Control" tanpa menyebut akun aktor awal; spec memakai akun Pre-setup #9 dan #10 sebagai sumber.
