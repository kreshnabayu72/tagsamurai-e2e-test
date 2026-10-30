---
id: TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi
title: "Guided Tooltip: otomatis kunjungan pertama, isi Step 1-3, Next/Back/Done"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-30
  - TC-GS-PROFILE-31
  - TC-GS-PROFILE-32
  - TC-GS-PROFILE-33
  - TC-GS-PROFILE-34
coverage:
  web: automated
---

# Guided Tooltip: otomatis kunjungan pertama, isi Step 1-3, Next/Back/Done

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #20 Tono Prasetyo (`freshGuideProfile_automated_{namaCompany}@qwertysystem.net`), Total Control, flag `guided_tooltip_seen_gs-my-profile` belum ada sebelum spec; password `Spectra.env.GS_PROFILE_FRESHGUIDE_PASSWORD`.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #20) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Pengecualian Hook suite 3: spec ini menguji flag `guided_tooltip_seen_gs-my-profile` sendiri. Hook `before` spec menyetel flag akun Pre-setup #20 menjadi true sesudah hook suite supaya pembukaan awal oleh `beforeEach` tidak memunculkan walkthrough; langkah 1 menghapus flag itu (menjadi belum ada) sebelum My Profile dibuka dari account menu. Hook `after` spec memulihkan flag ke keadaan awal (belum ada). Mekanisme menyetel, menghapus, dan membaca flag disediakan tim FE/BE.
- Data Dinamis: tidak ada.

## Test Steps

### Kunjungan pertama: walkthrough otomatis dan Step 1 (TC-GS-PROFILE-30, TC-GS-PROFILE-31)

1. Hapus flag `guided_tooltip_seen_gs-my-profile` akun Pre-setup #20
2. Buka My Profile dari account menu navbar
3. Verifikasi walkthrough muncul otomatis dimulai dari Step 1
4. Verifikasi elemen yang disorot pada Step 1: Product Selector
5. Verifikasi Title Step 1: `Switch product view`
6. Verifikasi Description Step 1: `See your access and status in each product you use — this only changes what's shown here, it won't navigate you away.`
7. Verifikasi tombol [Back] Hidden pada Step 1

### Step 2 (TC-GS-PROFILE-32)

8. Klik [Next]
9. Verifikasi elemen yang disorot pada Step 2: [Change Password]
10. Verifikasi Title Step 2: `Manage your password`
11. Verifikasi Description Step 2: `Update your password anytime. Other active sessions will be signed out for security when you do.`

### Step 3 dan navigasi (TC-GS-PROFILE-33, TC-GS-PROFILE-34)

12. Klik [Next]
13. Verifikasi elemen yang disorot pada Step 3: Avatar
14. Verifikasi Title Step 3: `Update your photo`
15. Verifikasi Description Step 3: `Hover your photo to replace or remove it.`
16. Verifikasi tombol maju pada Step 3 berlabel [Done] (bukan [Next])
17. Klik [Back]
18. Verifikasi walkthrough kembali ke Step 2
19. Klik [Next]
20. Klik [Done]
21. Verifikasi walkthrough tertutup
22. Verifikasi flag `guided_tooltip_seen_gs-my-profile` tersimpan true

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-30, 31, 32, 33, 34).
- Satu kunjungan pertama dipakai bersama oleh kelima TC: kelimanya berprecondition sama (flag belum ada) dan langkahnya berurutan Step 1, Step 2, lalu Step 3 (variasi dari topik yang sama berurutan, bagian 3 prinsip 4). Akibatnya Next dari Step 1 ke Step 2 (langkah 8) dan dari Step 2 ke Step 3 (langkah 12) dipakai bersama oleh TC-GS-PROFILE-32, 33, dan 34. Expected a TC-GS-PROFILE-30 ("target Product Selector") dan butir a TC-GS-PROFILE-31 menjadi satu `Verifikasi` (langkah 4) karena isinya sama.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 menghapus flag (precondition TC) dan langkah 2 membuka ulang My Profile dari account menu navbar sehingga kunjungan pertama dimulai.
- Langkah 22 memakai kemampuan baca flag yang disediakan tim FE/BE (S-11), karena flag hanya teramati di sisi server atau penyimpanan.
- Temuan untuk QA:
  - TC-GS-PROFILE-34 menulis "Flag ... tersimpan true" tanpa cara memeriksanya dari UI; spec memakai kemampuan baca flag yang disediakan tim FE/BE.
