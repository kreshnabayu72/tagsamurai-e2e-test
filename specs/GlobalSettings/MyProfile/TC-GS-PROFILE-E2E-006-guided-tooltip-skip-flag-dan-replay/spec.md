---
id: TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay
title: "Guided Tooltip: Skip, klik overlay, flag seen, kunjungan berikutnya, dan tombol replay"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-35
  - TC-GS-PROFILE-36
  - TC-GS-PROFILE-37
  - TC-GS-PROFILE-38
coverage:
  web: automated
---

# Guided Tooltip: Skip, klik overlay, flag seen, kunjungan berikutnya, dan tombol replay

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan = urutan blok):

| Blok | Pre-setup | Akun | Kondisi flag | Env var password |
|---|---|---|---|---|
| 1 | #20 | Tono Prasetyo, `freshGuideProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | `guided_tooltip_seen_gs-my-profile` belum ada sebelum tiap TC | `Spectra.env.GS_PROFILE_FRESHGUIDE_PASSWORD` |
| 2 | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | flag sudah true | `Spectra.env.GS_PROFILE_TC_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #20) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Pengecualian Hook suite 3: spec ini menguji flag `guided_tooltip_seen_gs-my-profile` sendiri. Untuk akun Pre-setup #20, hook `before` spec menyetel flag menjadi true sesudah hook suite supaya pembukaan awal oleh `beforeEach` tidak memunculkan walkthrough; langkah 1 dan 7 menghapus flag itu sebelum tiap TC. Hook `after` spec memulihkan flag akun Pre-setup #20 ke keadaan awal (belum ada). Untuk akun Pre-setup #1, flag true berasal dari Hook suite 3. Mekanisme menyetel dan menghapus flag disediakan tim FE/BE.
- Data Dinamis: tidak ada.

## Test Steps

### Skip menyimpan flag seen (TC-GS-PROFILE-35)

1. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
2. Buka My Profile dari account menu navbar
3. Klik [Skip]
4. Verifikasi walkthrough tertutup setelah [Skip]
5. Buka ulang My Profile dari account menu navbar
6. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### Klik overlay setara Skip (TC-GS-PROFILE-36)

7. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
8. Buka My Profile dari account menu navbar
9. Klik [Next]
10. Klik area overlay gelap di luar tooltip
11. Verifikasi walkthrough tertutup
12. Buka ulang My Profile dari account menu navbar
13. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### Ganti akun ke Pre-setup #1

14. Logout, lalu login sebagai Pre-setup #1 dengan `Spectra.env.GS_PROFILE_TC_PASSWORD`

### Flag seen true: tidak ada walkthrough otomatis (TC-GS-PROFILE-37)

15. Buka My Profile dari account menu navbar
16. Verifikasi halaman My Profile termuat: Breadcrumb `My Profile` tampil
17. Verifikasi walkthrough tidak muncul otomatis

### Tombol replay (TC-GS-PROFILE-38)

18. Klik tombol [?] di kanan Breadcrumb
19. Verifikasi walkthrough muncul dari Step 1
20. Klik [Skip]
21. Muat ulang halaman
22. Verifikasi Breadcrumb `My Profile` tampil
23. Verifikasi walkthrough tidak muncul otomatis (flag tetap true)

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-35, 36, 37, 38).
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (langkah 14); blok 2 tetap bermakna walau blok 1 gagal.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 dan 7 menghapus flag akun Pre-setup #20 (precondition TC) dan langkah 14 adalah Step ganti akun. Langkah 16 dan 22 membuktikan halaman sudah termuat sebelum asersi absence walkthrough (anchor positif).
- Asersi "flag seen tersimpan" pada judul TC-GS-PROFILE-35 dan TC-GS-PROFILE-36 diamati lewat walkthrough yang tidak muncul pada kunjungan berikutnya (Expected b TC); spec tidak membaca flag langsung.
- Temuan untuk QA: tidak ada.
