---
id: TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide
title: "Change Password: layar modal, masked input, dan kontrol show/hide password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-73
  - TC-GS-PROFILE-74
  - TC-GS-PROFILE-316
  - TC-GS-PROFILE-317
coverage:
  web: automated
---

# Change Password: layar modal, masked input, dan kontrol show/hide password

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun Pre-setup #7 di hook `before` spec). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang tidak dikirim, bukan kredensial): `abc` (TC-GS-PROFILE-74), `Ab1!xyzw` (TC-GS-PROFILE-316 dan TC-GS-PROFILE-317).
- Kemampuan teknis: hover pada ikon toggle untuk membaca tooltip.
- Spec ini tidak mengirim [Save] dan tidak mengubah state global. Modal dibuka sekali untuk keempat TC (halaman yang sama dipakai berulang) dan ditutup di akhir lewat `✕`, dialog `Unsaved Changes`, lalu `[Leave]` (S-08).

## Test Steps

### Screening modal (TC-GS-PROFILE-73)
1. Klik [Change Password]
2. Verifikasi header modal: judul "Change Password" dan tombol close [✕]
3. Verifikasi label "Current Password*" dengan placeholder "Enter current password"
4. Verifikasi label "New Password*" dengan placeholder "Enter new password"
5. Verifikasi label "Confirm New Password*" dengan placeholder "Enter new password again"
6. Verifikasi footer [Cancel] dan [Save] tampil
7. Verifikasi [Save] Enabled
8. Verifikasi tidak ada tombol [Clear Field]
### Masked input (TC-GS-PROFILE-74)
9. Ketik `abc` di Current Password
10. Ketik `abc` di New Password
11. Ketik `abc` di Confirm New Password
12. Verifikasi karakter yang diketik pada Current Password, New Password, dan Confirm New Password tersamarkan (masked) dan tidak tampil sebagai teks biasa selama kontrol show/hide tidak diaktifkan
### Kontrol show/hide: keadaan awal dan tooltip (TC-GS-PROFILE-316)
13. Ganti isi Current Password dengan `Ab1!xyzw`
14. Ganti isi New Password dengan `Ab1!xyzw`
15. Ganti isi Confirm New Password dengan `Ab1!xyzw`
16. Verifikasi Current Password tersamarkan (masked) secara default dengan ikon toggle `EyeLine`
17. Verifikasi New Password tersamarkan (masked) secara default dengan ikon toggle `EyeLine`
18. Verifikasi Confirm New Password tersamarkan (masked) secara default dengan ikon toggle `EyeLine`
19. Hover ikon toggle pada Current Password
20. Verifikasi tooltip ikon Current Password: "Show password"
21. Hover ikon toggle pada New Password
22. Verifikasi tooltip ikon New Password: "Show password"
23. Hover ikon toggle pada Confirm New Password
24. Verifikasi tooltip ikon Confirm New Password: "Show password"
### Kontrol show/hide: toggle independen per field (TC-GS-PROFILE-317)
25. Klik ikon toggle pada New Password
26. Verifikasi New Password tampil sebagai teks `Ab1!xyzw`
27. Verifikasi ikon toggle New Password berganti `EyeOffLine`
28. Verifikasi Current Password dan Confirm New Password tetap tersamarkan dengan ikon `EyeLine`
29. Hover ikon toggle pada New Password
30. Verifikasi tooltip ikon New Password: "Hide password"
31. Klik ikon toggle pada New Password lagi
32. Verifikasi New Password tersamarkan kembali dengan ikon `EyeLine`
33. Klik ikon toggle pada Current Password
34. Hover ikon toggle pada Current Password
35. Verifikasi Current Password tampil sebagai teks `Ab1!xyzw` dengan ikon `EyeOffLine`
36. Verifikasi tooltip ikon Current Password: "Hide password"
37. Verifikasi New Password dan Confirm New Password tetap tersamarkan
38. Klik ikon toggle pada Confirm New Password
39. Hover ikon toggle pada Confirm New Password
40. Verifikasi Confirm New Password tampil sebagai teks `Ab1!xyzw` dengan ikon `EyeOffLine`
41. Verifikasi tooltip ikon Confirm New Password: "Hide password"
42. Verifikasi Current Password tetap tampil sebagai teks
43. Klik ikon toggle pada Current Password
44. Klik ikon toggle pada Confirm New Password
45. Verifikasi Current Password dan Confirm New Password tersamarkan kembali dengan ikon `EyeLine`
### Menutup modal yang terisi
46. Klik [✕]
47. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
48. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-73, 74, 316, dan 317 berada di spec ini; tidak ada TC yang terbelah ke spec lain.
- Langkah penghubung (S-03): "Ganti isi ... dengan `Ab1!xyzw`" mengganti nilai `abc` milik TC-GS-PROFILE-74 dengan nilai TC-GS-PROFILE-316; langkah uji ke-2 TC-GS-PROFILE-317 identik dengan langkah uji ke-2 TC-GS-PROFILE-316 dan ketiga field masih terisi `Ab1!xyzw`, jadi tidak diketik ulang. Ketiga ikon toggle belum diklik sebelum blok TC-GS-PROFILE-317 sehingga keadaan awalnya sama dengan TC. Tiga langkah penutup di akhir spec adalah pemulihan form dirty (S-08, S-09) dan tidak masuk Expected TC.
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok adalah screening satu modal Change Password tanpa submit dan berbagi satu pembukaan modal; jumlah langkah berasal dari satu `Verifikasi` per klausa Expected (S-01) pada tiga field, enam tooltip, dan tiga keadaan ikon, bukan dari aksi. Satu kelas harness, satu akun, tanpa state global; blok sesudahnya tetap bermakna walau blok sebelumnya gagal karena asersi bersifat soft.
- Temuan untuk QA: tidak ada temuan.
