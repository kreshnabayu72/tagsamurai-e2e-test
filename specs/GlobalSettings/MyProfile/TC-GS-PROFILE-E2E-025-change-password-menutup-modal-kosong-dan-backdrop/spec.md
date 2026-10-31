---
id: TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop
title: "Change Password: Menutup Modal Kosong (X, Cancel, Esc), Klik Backdrop, dan Isian Dikosongkan Kembali"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-141
  - TC-GS-PROFILE-142
  - TC-GS-PROFILE-143
  - TC-GS-PROFILE-150
  - TC-GS-PROFILE-152
coverage:
  web: automated
---

# Change Password: Menutup Modal Kosong (X, Cancel, Esc), Klik Backdrop, dan Isian Dikosongkan Kembali

## Prerequisites

- Mode: FE+BE (tanpa submit; tidak ada perubahan state backend).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_PROFILE_PWD_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Spec tidak mengirim form; modal ditutup di akhir tiap kasus sehingga tidak ada form dirty di akhir spec.

## Test Steps

### TC-GS-PROFILE-141: Menutup modal kosong lewat [✕]

1. Klik [Change Password]
2. Klik [✕]
3. Verifikasi modal Change Password tertutup langsung
4. Verifikasi tombol [Change Password] tampil di halaman My Profile
5. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-PROFILE-142: Menutup modal kosong lewat [Cancel]

6. Klik [Change Password]
7. Klik [Cancel]
8. Verifikasi modal Change Password tertutup langsung
9. Verifikasi tombol [Change Password] tampil di halaman My Profile
10. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-PROFILE-143: Menutup modal kosong lewat Esc

11. Klik [Change Password]
12. Tekan Esc
13. Verifikasi modal Change Password tertutup langsung
14. Verifikasi tombol [Change Password] tampil di halaman My Profile
15. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-PROFILE-150: Klik backdrop pada modal kosong

16. Klik [Change Password]
17. Klik area backdrop di luar modal
18. Verifikasi modal Change Password tetap terbuka
19. Verifikasi Current Password, New Password, dan Confirm New Password tetap kosong
20. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-PROFILE-152: Isian diisi lalu dikosongkan kembali

21. Isi Current Password "abc" pada modal yang masih terbuka dari langkah 16
22. Hapus seluruh isi Current Password
23. Klik [✕]
24. Verifikasi modal Change Password tertutup langsung
25. Verifikasi tombol [Change Password] tampil di halaman My Profile
26. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Kelas harness: fungsional (menutup form). Empat kejadian menutup modal (langkah 2, 7, 12, 23) memakai empat pembukaan modal (langkah 1, 6, 11, 16); modal dari langkah 16 dipakai ulang di TC-GS-PROFILE-152 karena belum pernah diisi (prinsip 6).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Anchor absence (bagian 8b butir 2): langkah 4, 9, 14, 25 (tombol [Change Password] tampil kembali) mendahului asersi dialog Unsaved Changes tidak muncul; langkah 18 (modal masih tampil) menjadi anchor langkah 20.
- Langkah 22 mengosongkan field yang diisi di langkah 21; TC-GS-PROFILE-152 menguji pengosongan itu sendiri sehingga pengecualian prinsip 6 berlaku.
- Temuan untuk QA:
  - TC-GS-PROFILE-150 menulis "isian dipertahankan" padahal modal belum diisi; spec mengasersi ketiga field tetap kosong (langkah 19).
  - TC-GS-PROFILE-152 hanya menyebut Current Password; New Password dan Confirm New Password tidak diisi.
