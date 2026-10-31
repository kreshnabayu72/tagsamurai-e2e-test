---
id: TC-GS-PROFILE-E2E-009-tampilan-mobile-android
title: "Mobile Android: card satu kolom, bottom sheet Avatar, bottom sheet Change Password, dan Guided Tooltip mobile"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-45
  - TC-GS-PROFILE-46
  - TC-GS-PROFILE-47
  - TC-GS-PROFILE-48
  - TC-GS-PROFILE-49
coverage:
  web: automated
  mobile: automated
---

# Mobile Android: card satu kolom, bottom sheet Avatar, bottom sheet Change Password, dan Guided Tooltip mobile

## Prerequisites

- Mode: FE+BE.
- Perangkat: Android uji (aplikasi mobile TAG Samurai) yang dipakai bersama; suite berjalan serial (`parallel: false`), dan spec ini tidak dijalankan paralel dengan spec lain yang memakai perangkat itu (S-09).
- Akun yang diuji (urutan = urutan blok):

| Blok | Pre-setup | Akun | Kondisi data | Env var password |
|---|---|---|---|---|
| 1 | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | tanpa foto | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| 2 | #9 | Nadia Putri, `photoProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | foto profil aktif `nadia-photo.jpg` | `Spectra.env.GS_PROFILE_PHOTO_PASSWORD` |
| 3 | #10 | Fajar Nugroho, `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | tanpa foto | `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD` |
| 4 | #20 | Tono Prasetyo, `freshGuideProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | flag `guided_tooltip_seen_gs-my-profile` belum ada | `Spectra.env.GS_PROFILE_FRESHGUIDE_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) pada aplikasi Android di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2. Hook suite membuka My Profile di web; pada aplikasi Android, My Profile dibuka dengan langkah eksplisit di `## Test Steps` setelah tiap login.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3. Pengecualian: blok 4 (TC-GS-PROFILE-49) menguji walkthrough itu sendiri; flag akun Pre-setup #20 dihapus pada langkah 22 dan hook `after` memulihkannya ke keadaan awal (belum ada).
- Data Dinamis: tidak ada. Spec hanya membaca dan tidak mengubah foto Pre-setup #9 dan #10.

## Test Steps

### Susunan halaman mobile (TC-GS-PROFILE-45)

1. Buka My Profile pada aplikasi Android
2. Verifikasi tiap Section tampil sebagai card yang ditumpuk dalam satu kolom
3. Verifikasi Product Selector berupa dropdown full-width di bawah Avatar
4. Verifikasi tidak ada tabel

### Bottom sheet Change Password (TC-GS-PROFILE-48)

5. Tap [Change Password]
6. Verifikasi bottom sheet terbuka berjudul `Change Password`
7. Verifikasi bottom sheet memuat field Current Password, New Password, dan Confirm New Password
8. Verifikasi bottom sheet memuat tombol [Cancel] dan [Save]
9. Tap [Cancel]

### Bottom sheet Avatar dengan foto (TC-GS-PROFILE-46)

10. Logout dari aplikasi Android, lalu login sebagai Pre-setup #9 (Nadia Putri) dengan `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`
11. Buka My Profile pada aplikasi Android
12. Tap Avatar
13. Verifikasi bottom sheet terbuka dengan tombol [Edit] dan [Delete]
14. Tutup bottom sheet tanpa memilih aksi

### Bottom sheet Avatar tanpa foto (TC-GS-PROFILE-47)

15. Logout dari aplikasi Android, lalu login sebagai Pre-setup #10 (Fajar Nugroho) dengan `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`
16. Buka My Profile pada aplikasi Android
17. Tap Avatar
18. Verifikasi bottom sheet terbuka dengan tombol [Edit]
19. Verifikasi tidak ada tombol [Delete]
20. Tutup bottom sheet tanpa memilih aksi

### Guided Tooltip Step 3 mobile (TC-GS-PROFILE-49)

21. Logout dari aplikasi Android, lalu login sebagai Pre-setup #20 (Tono Prasetyo) dengan `Spectra.env.GS_PROFILE_FRESHGUIDE_PASSWORD`
22. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
23. Buka My Profile pada aplikasi Android
25. Tap [Next]
25. Tap [Next]
26. Verifikasi Description Step 3: `Tap your photo to replace or remove it.`

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-45, 46, 47, 48, 49). Kolom Automation di TC bertanda "Manual Only" untuk aplikasi native Android; spec tetap ditulis dengan `coverage.mobile: automated` karena kebutuhan perangkat dan aplikasi ditulis di Prerequisites (bagian 2 konvensi: hambatan teknis bukan alasan mengeluarkan TC).
- `coverage.web: automated` dan `coverage.mobile: automated` keduanya ditulis (bagian 8 konvensi) karena akun, data, dan hook suite web dipakai bersama.
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (langkah 10, 15, dan 21); tiap blok tetap bermakna walau blok sebelumnya gagal.
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-PROFILE-48 ditaruh sebelum TC-GS-PROFILE-46 dan 47 karena memakai akun Pre-setup #1 yang sama dengan TC-GS-PROFILE-45.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1, 11, 16, dan 23 membuka My Profile pada aplikasi; langkah 9, 14, dan 20 menutup bottom sheet; langkah 10, 15, dan 21 adalah Step ganti akun (langkah 22 menghapus flag precondition TC).
- Asersi absence tombol [Delete] (langkah 19) didahului `Verifikasi` tombol [Edit] pada bottom sheet yang sama tampil (langkah 18).
- Temuan untuk QA:
  - TC-GS-PROFILE-45 sampai 49 bertanda "Manual Only — (b) aplikasi native Android di luar framework otomasi web" pada kolom Automation, bertentangan dengan keputusan bagian 2 konvensi (hambatan teknis bukan alasan mengeluarkan TC); spec tetap ditulis dan kolom Automation perlu disesuaikan QA.
  - TC-GS-PROFILE-45 sampai 49 menulis Precondition "Login sbg Role: Total Control" bersama akun Pre-setup #9, #10, atau #20; spec memakai akun Pre-setup sebagai sumber.
