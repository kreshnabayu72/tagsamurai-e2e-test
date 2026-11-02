---
id: TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda
title: "Change Password: field kosong dan Confirm tidak sama diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-84
  - TC-GS-PROFILE-85
  - TC-GS-PROFILE-86
  - TC-GS-PROFILE-87
  - TC-GS-PROFILE-90
  - TC-GS-PROFILE-91
  - TC-GS-PROFILE-92
coverage:
  web: automated
---

# Change Password: field kosong dan Confirm tidak sama diblokir

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar), `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3, New Password dan Confirm New Password). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial): `Wr0ngPass!` (Current Password salah) dan `Different1!` (Confirm New Password tidak sama).
- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah sesi aktif akun Pre-setup #7. Nilainya dicatat sebagai baseline di langkah pertama dan dibandingkan di setiap `Verifikasi` "tidak ada sesi yang di-invalidate".
- Tidak ada [Save] yang berhasil di spec ini; hanya TC-GS-PROFILE-92 mengirim Current Password salah ke server (counter Change Password menjadi 1), dan tidak ada password yang berubah. Counter direset hook `after` suite (Hook suite 7). Satu pembukaan modal untuk ketujuh TC; field diubah di antara kasus.

## Test Steps

1. Catat jumlah sesi aktif akun Pre-setup #7 lewat kemampuan baca state BE sebagai baseline
2. Klik [Change Password]
### Current Password kosong (TC-GS-PROFILE-84)
3. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
4. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
5. Klik [Save]
6. Verifikasi inline error di bawah Current Password: "Password must not be empty"
7. Verifikasi modal Change Password tetap terbuka
8. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline (tidak ada sesi lain yang di-invalidate)
9. Verifikasi tidak ada toast
### New Password kosong (TC-GS-PROFILE-85)
10. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
11. Kosongkan isi New Password
12. Klik [Save]
13. Verifikasi inline error di bawah New Password: "Password must not be empty"
14. Verifikasi modal Change Password tetap terbuka
15. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline
### Confirm New Password kosong (TC-GS-PROFILE-86)
16. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
17. Kosongkan isi Confirm New Password
18. Klik [Save]
19. Verifikasi inline error di bawah Confirm New Password: "Confirm password must not be empty"
20. Verifikasi modal Change Password tetap terbuka
21. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline
### Ketiga field kosong (TC-GS-PROFILE-87)
22. Klik [✕]
23. Klik [Leave] pada dialog "Unsaved Changes"
24. Klik [Change Password]
25. Klik [Save]
26. Verifikasi inline error di bawah Current Password: "Password must not be empty"
27. Verifikasi inline error di bawah New Password: "Password must not be empty"
28. Verifikasi inline error di bawah Confirm New Password: "Confirm password must not be empty"
29. Verifikasi submit diblokir: jumlah sesi aktif akun #7 sama dengan baseline
### Confirm tidak sama (TC-GS-PROFILE-90)
30. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
31. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
32. Ketik `Different1!` di Confirm New Password
33. Klik [Save]
34. Verifikasi inline error di bawah Confirm New Password: "Passwords do not match"
35. Verifikasi modal Change Password tetap terbuka
36. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline
### Confirm tidak sama diperiksa sebelum Current Password (TC-GS-PROFILE-91)
37. Ganti isi Current Password dengan `Wr0ngPass!`
38. Kosongkan isi Confirm New Password lalu ketik ulang `Different1!`
39. Klik [Save]
40. Verifikasi hanya inline error "Passwords do not match" yang tampil di bawah Confirm New Password
41. Verifikasi tidak ada inline error "Current password is incorrect"
### Tiga submit Confirm tidak sama tidak mengunci (TC-GS-PROFILE-92)
42. Kosongkan isi Confirm New Password lalu ketik ulang `Different1!`
43. Klik [Save]
44. Verifikasi submit pertama hanya menampilkan inline error "Passwords do not match"
45. Klik [Save]
46. Verifikasi submit kedua hanya menampilkan inline error "Passwords do not match"
47. Klik [Save]
48. Verifikasi submit ketiga hanya menampilkan inline error "Passwords do not match"
49. Ganti isi Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
50. Klik [Save]
51. Verifikasi submit keempat menampilkan inline error "Current password is incorrect" di bawah Current Password (percobaan salah ke-1)
52. Verifikasi [Save] tetap Enabled
53. Verifikasi tidak ada toast terkunci
### Menutup modal yang terisi
54. Klik [✕]
55. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
56. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-84 sampai 87, 90, 91, dan 92 berada di spec ini. TC-GS-PROFILE-88 dan 89 ada di spec 019.
- Langkah penghubung (S-03): "Kosongkan isi ... lalu ketik ulang" pada TC-GS-PROFILE-91 dan 92 membersihkan inline error "Passwords do not match" sebelumnya agar asersi berikutnya tidak membaca error lama (R-12). Langkah 22 sampai 24 menutup modal yang terisi (`✕`, [Leave], S-08) lalu membukanya kembali: ketiga field kosong dan inline error "Confirm password must not be empty" dari TC-GS-PROFILE-86 hilang, sehingga `Verifikasi` TC-GS-PROFILE-87 hanya lulus dari submit baru (R-12). Langkah "Ganti isi ..." dan "Kosongkan isi ..." di antara kasus mengubah field ke keadaan precondition kasus berikutnya. Tiga langkah penutup di akhir spec memulihkan form dirty (S-08, S-09).
- Urutan: kasus yang mengirim Current Password salah ke server (TC-GS-PROFILE-92 submit keempat) diletakkan terakhir karena menaikkan counter.
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok adalah validasi negatif satu modal Change Password, satu kelas harness dan satu akun; jumlah langkah berasal dari tiga `Verifikasi` per kasus (S-01) dan satu pembukaan modal dipakai berulang (bagian 3). Blok sesudahnya tetap bermakna walau blok sebelumnya gagal karena asersi bersifat soft.
- Temuan untuk QA:
  - TC-GS-PROFILE-84 sampai 87, 90: Expected "Tidak ada sesi lain yang di-invalidate" tidak memberi cara memeriksa. Spec memakai kemampuan baca jumlah sesi aktif akun #7 yang disediakan tim FE/BE dan membandingkannya dengan baseline.
  - TC-GS-PROFILE-90, 91, 92: Post Condition counter Change Password ("tetap 0" dan "menjadi 1") tidak punya langkah observasi di TC, jadi tidak diasersi.
