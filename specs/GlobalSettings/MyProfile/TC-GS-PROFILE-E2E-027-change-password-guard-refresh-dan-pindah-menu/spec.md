---
id: TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu
title: "Change Password: Guard Refresh Browser dan Pindah Menu Navbar saat Modal Terisi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-153
  - TC-GS-PROFILE-154
  - TC-GS-PROFILE-155
  - TC-GS-PROFILE-309
coverage:
  web: automated
---

# Change Password: Guard Refresh Browser dan Pindah Menu Navbar saat Modal Terisi

## Prerequisites

- Mode: FE+BE (tanpa submit; tidak ada perubahan state backend).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_PROFILE_PWD_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Kemampuan teknis: menangani dialog `beforeunload` browser pada langkah muat ulang (mengamati kemunculannya, lalu menerima atau menolaknya); disediakan tim FE (S-08).
- Spec berakhir dengan modal tertutup dan kosong (langkah 27); tidak ada form dirty yang tersisa.

## Test Steps

### TC-GS-PROFILE-154: Refresh browser saat modal kosong

1. Klik [Change Password]
2. Muat ulang halaman (F5)
3. Verifikasi halaman My Profile dimuat ulang dan tombol [Change Password] tampil
4. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul

### TC-GS-PROFILE-153: Refresh browser saat modal terisi

5. Klik [Change Password]
6. Isi Current Password "abc"
7. Muat ulang halaman (F5)
8. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
9. Tolak konfirmasi bawaan browser sehingga halaman tidak dimuat ulang

### TC-GS-PROFILE-155: Pindah menu navbar saat modal terisi, [Cancel]

10. Klik logo di navbar
11. Verifikasi dialog "Unsaved Changes" tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" serta tombol [Cancel] dan [Leave]
12. Klik [Cancel] pada dialog
13. Verifikasi dialog Unsaved Changes tertutup
14. Verifikasi navigasi dibatalkan dan halaman My Profile tetap terbuka
15. Verifikasi modal Change Password tetap terbuka
16. Verifikasi Current Password tetap terisi

### TC-GS-PROFILE-309: Pindah menu navbar saat modal terisi, [Leave]

17. Klik logo di navbar
18. Verifikasi dialog "Unsaved Changes" tampil dengan tombol [Cancel] dan [Leave]
19. Klik [Leave]
20. Verifikasi dialog Unsaved Changes tertutup
21. Verifikasi halaman tujuan logo navbar terbuka
22. Buka My Profile lewat account menu navbar > My Profile
23. Klik [Change Password]
24. Verifikasi Current Password kosong
25. Verifikasi New Password kosong
26. Verifikasi Confirm New Password kosong
27. Klik [✕]

## Notes

- Kelas harness: fungsional (guard navigasi). TC-GS-PROFILE-154 ditaruh pertama karena memakai modal kosong; kasus form dirty memakai satu isian yang dipakai ulang dari langkah 6 sampai 17 (langkah 9 menolak konfirmasi `beforeunload` sehingga form tetap dirty, dengan kemampuan penanganan dialog di Prerequisites sesuai S-08).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 9, 22 (kembali ke My Profile), dan 27 (menutup modal kosong di akhir spec).
- Anchor absence: langkah 3 mendahului langkah 4.
- Urutan kasus 154, 153, 155, 309 mengikuti keadaan form (kosong sebelum dirty), bukan urutan nomor TC (S-05).
- Temuan untuk QA:
  - TC-GS-PROFILE-155 dan TC-GS-PROFILE-309 menulis "logo atau item navigasi in-app di navbar" tanpa menyebut elemen dan halaman tujuan persisnya; spec memakai logo navbar dan mengasersi "halaman tujuan logo navbar terbuka" (langkah 21) tanpa nama halaman.
