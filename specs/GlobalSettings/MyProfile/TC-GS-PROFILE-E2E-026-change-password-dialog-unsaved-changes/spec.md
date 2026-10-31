---
id: TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes
title: "Change Password: Dialog Unsaved Changes saat Menutup Modal Terisi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-144
  - TC-GS-PROFILE-145
  - TC-GS-PROFILE-146
  - TC-GS-PROFILE-147
  - TC-GS-PROFILE-148
  - TC-GS-PROFILE-149
  - TC-GS-PROFILE-151
coverage:
  web: automated
---

# Change Password: Dialog Unsaved Changes saat Menutup Modal Terisi

## Prerequisites

- Mode: FE+BE (tanpa submit; tidak ada perubahan state backend).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_PROFILE_PWD_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Spec berakhir dengan modal tertutup dan kosong (langkah 34); tidak ada form dirty yang tersisa.

## Test Steps

### Persiapan form dirty

1. Klik [Change Password]
2. Isi Current Password "abc"

### TC-GS-PROFILE-144: Menutup modal terisi lewat [✕]

3. Klik [✕]
4. Verifikasi dialog "Unsaved Changes" tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" serta tombol [Cancel] dan [Leave]
5. Verifikasi modal Change Password masih terbuka di belakang dialog

### TC-GS-PROFILE-148: [Cancel] pada dialog mempertahankan isian

6. Klik [Cancel] pada dialog
7. Verifikasi dialog Unsaved Changes tertutup
8. Verifikasi modal Change Password tetap terbuka
9. Verifikasi Current Password tetap terisi

### TC-GS-PROFILE-145: Menutup modal terisi lewat [Cancel]

10. Klik [Cancel] pada modal Change Password
11. Verifikasi dialog "Unsaved Changes" tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" serta tombol [Cancel] dan [Leave]
12. Verifikasi modal Change Password masih terbuka di belakang dialog

### TC-GS-PROFILE-149: Esc pada dialog setara [Cancel]

13. Tekan Esc
14. Verifikasi dialog Unsaved Changes tertutup
15. Verifikasi modal Change Password tetap terbuka
16. Verifikasi Current Password tetap terisi

### TC-GS-PROFILE-151: Klik backdrop pada modal terisi

17. Klik area backdrop di luar modal
18. Verifikasi modal Change Password tetap terbuka
19. Verifikasi Current Password tetap terisi
20. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-PROFILE-146: Menutup modal terisi lewat Esc

21. Tekan Esc
22. Verifikasi dialog "Unsaved Changes" tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" serta tombol [Cancel] dan [Leave]
23. Verifikasi modal Change Password masih terbuka di belakang dialog
24. Klik [Cancel] pada dialog

### TC-GS-PROFILE-147: [Leave] menutup modal dan membuang isian

25. Klik [✕]
26. Verifikasi dialog Unsaved Changes tampil
27. Klik [Leave]
28. Verifikasi dialog Unsaved Changes tertutup
29. Verifikasi modal Change Password tertutup
30. Klik [Change Password]
31. Verifikasi Current Password kosong
32. Verifikasi New Password kosong
33. Verifikasi Confirm New Password kosong
34. Klik [✕]

## Notes

- Kelas harness: fungsional (menutup form). Satu pembukaan modal dengan form dirty dipakai ulang oleh seluruh kasus (langkah 1 sampai 2); modal dibuka lagi hanya di langkah 30 karena TC-GS-PROFILE-147 mengasersi modal yang dibuka kembali kosong.
- Urutan kasus di spec (144, 148, 145, 149, 151, 146, 147) mengikuti keadaan form dirty dan dialog, bukan urutan nomor TC (S-05); isi tiap kasus tidak berubah.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 24 (menutup dialog hasil TC-GS-PROFILE-146 agar modal tetap terbuka untuk kasus berikutnya) dan langkah 34 (menutup modal kosong di akhir spec). Langkah 26 (`Verifikasi` dialog sebelum [Leave]) dituntut S-08.
- Anchor absence: langkah 18 (modal masih tampil) mendahului langkah 20.
- Temuan untuk QA:
  - TC-GS-PROFILE-147 tidak menyebut apakah dialog tampil setelah [✕] (hanya Expected sesudah [Leave]); spec memakai Verifikasi dialog dari S-08.
