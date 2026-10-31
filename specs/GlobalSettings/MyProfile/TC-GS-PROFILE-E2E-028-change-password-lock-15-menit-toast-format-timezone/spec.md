---
id: TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone
title: "Change Password: Lock 15 Menit (Toast, Format 12 Jam, Timezone, Note User Log, Time Format Berubah)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-115
  - TC-GS-PROFILE-117
  - TC-GS-PROFILE-118
  - TC-GS-PROFILE-119
  - TC-GS-PROFILE-251
coverage:
  web: automated
---

# Change Password: Lock 15 Menit (Toast, Format 12 Jam, Timezone, Note User Log, Time Format Berubah)

## Prerequisites

- Mode: FE+BE (state lock, counter, jam server, dan User Log dibaca dari backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (jam server dan jam browser, counter Change Password, timezone dan Time Format).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Passw0rd!Old` lewat `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, timezone Asia/Jakarta). Akun lain: Pre-setup #18 (Maya Anggraini, Time Format 12 jam, `passwordProfile12h_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`) untuk TC-GS-PROFILE-117, dan Pre-setup #6 (Hendra Wijaya, Total Control, admin pembaca User Log, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) untuk TC-GS-PROFILE-119. Ganti akun memakai Step eksplisit.
- Password baru Data Dinamis #3 (`N3wPassw0rd!`) memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Current Password salah `Wr0ngPass!` ditulis literal karena submit selalu ditolak server.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; S-13): (a) mengatur counter Change Password dan mereset lock akun #7 dan #18; (b) mengatur jam server dan jam browser ke nilai absolut dan memulihkannya; (c) mengubah timezone akun #7 ke Asia/Makassar dan mengembalikannya ke Asia/Jakarta; (d) mengubah Time Format General Settings antara 24 jam dan 12 jam oleh pelaku yang tidak disebut TC-GS-PROFILE-251; (e) membaca counter Change Password akun #7; (f) membaca jumlah entri User Log akun #7; (g) menangani dialog `beforeunload` saat muat ulang dengan form dirty (S-08).
- Pemulihan di hook `after` spec: timezone #7 ke Asia/Jakarta, Time Format ke 24 jam, jam server dan jam browser ke waktu nyata, counter dan lock #7 dan #18 ke 0.
- Jam server dan jam browser diatur bersama dan dibekukan pada nilai absolut yang diset. Jam dipulihkan sebelum admin membuka User Log (S-09, langkah 39).

## Test Steps

### Persiapan TC-GS-PROFILE-115 dan TC-GS-PROFILE-119

1. Atur counter Change Password akun #7 ke 2, jam server dan jam browser ke 09:00 pada tanggal fixture Pre-setup #7
2. Catat baseline jumlah entri User Log akun #7 dengan Activity "Change Password", Status "Failed", Note "Locked 15 minutes (change password)"

### TC-GS-PROFILE-115 dan TC-GS-PROFILE-119: percobaan salah ke-3 (satu percobaan)

3. Klik [Change Password]
4. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
5. Klik [Save]
6. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 09:15."
7. Verifikasi tidak ada inline error "Current password is incorrect"
8. Verifikasi [Save] Disabled
9. Verifikasi modal Change Password tetap terbuka
10. Verifikasi Current Password, New Password, dan Confirm New Password tetap terisi
11. Verifikasi counter Change Password akun #7 menjadi 3

### TC-GS-PROFILE-118: [Time] mengikuti timezone user

12. Ubah timezone akun #7 ke Asia/Makassar (UTC+8), reset lock, atur counter Change Password ke 2, dan atur jam server dan jam browser ke 02:00 UTC
13. Muat ulang halaman (F5) dan terima konfirmasi bawaan browser
14. Klik [Change Password]
15. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
16. Klik [Save]
17. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 10:15."

### TC-GS-PROFILE-251: Time Format General Settings diubah

18. Kembalikan timezone akun #7 ke Asia/Jakarta, reset lock, atur counter Change Password ke 2, atur jam server dan jam browser ke 09:00, lalu ubah Time Format General Settings ke 12 jam hingga tersimpan
19. Muat ulang halaman (F5) dan terima konfirmasi bawaan browser
20. Klik [Change Password]
21. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
22. Klik [Save]
23. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 09:15 AM."
24. Klik [✕]
25. Verifikasi dialog Unsaved Changes tampil
26. Klik [Leave]
27. Kembalikan Time Format General Settings ke 24 jam hingga tersimpan

### TC-GS-PROFILE-117: [Time] format 12 jam (akun #18)

28. Reset lock akun #18, atur counter Change Password ke 2, dan atur jam server dan jam browser ke 09:00 pada tanggal fixture Pre-setup #7
29. Klik Logout
30. Login dengan akun Pre-setup #18 (`Spectra.env.GS_PROFILE_PWD12H_PASSWORD`)
31. Buka My Profile lewat account menu navbar > My Profile
32. Klik [Change Password]
33. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
34. Klik [Save]
35. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 09:15 AM."
36. Klik [✕]
37. Verifikasi dialog Unsaved Changes tampil
38. Klik [Leave]

### TC-GS-PROFILE-119: Note lock di User Log

39. Pulihkan jam server dan jam browser ke waktu nyata
40. Klik Logout
41. Login dengan akun Pre-setup #6 (`Spectra.env.GS_PROFILE_ADMIN_PASSWORD`)
42. Buka User Detail akun #7 > Tab User Log (Global Settings > User, Search email akun #7)
43. Cari entri User Log akun #7 dengan Note "Locked 15 minutes (change password)" berdasarkan Note dan email, bukan posisi teratas
44. Verifikasi entri tersebut memuat Activity "Change Password", Status "Failed", dan Note "Locked 15 minutes (change password)"
45. Verifikasi jumlah entri User Log akun #7 dengan Note "Locked 15 minutes (change password)" lebih banyak daripada baseline pada langkah 2

## Notes

- Kelas harness: d (jam server dan time-travel, state lock). Spec melewati sekitar 35 langkah (45 langkah nominal; blok baca-log berpola dan prefix ganti akun tidak dihitung menurut bagian 3). Alasan: seluruh blok berkelas d yang sama dan memakai fixture jam, counter, dan lock yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok mengatur ulang state-nya sendiri; ganti akun (langkah 29 sampai 31 dan 40 sampai 42) memakai Step eksplisit dengan bagian sesudahnya tetap bermakna (bagian 3, pemisah nyata butir b).
- TC-GS-PROFILE-115 dan TC-GS-PROFILE-119 memiliki precondition dan aksi identik (counter 2, jam 09:00, satu submit salah); keduanya dipenuhi satu percobaan (langkah 3 sampai 11). Expected c TC-GS-PROFILE-119 (tidak ada inline error) dipenuhi langkah 7. Pembacaan User Log TC-GS-PROFILE-119 (langkah 42 sampai 45) dilakukan di akhir spec setelah jam dipulihkan (S-09).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 12, 18, 28 (mengatur state), 13 dan 19 (muat ulang agar timezone atau Time Format baru terbaca), 24 sampai 26 dan 36 sampai 38 (menutup form dirty sesuai S-08, termasuk `Verifikasi` dialog), 27, 29 sampai 31, 39, 40 dan 41 (ganti akun dan pemulihan), serta 43 (mencari entri; Search disebut dalam langkah 42).
- Baseline log (S-12): langkah 2 dicatat sebelum aksi pertama; entri log yang dibuat saat jam digeser bercap waktu tidak sama dengan waktu nyata sehingga langkah 43 mencari berdasarkan Note dan email, dan langkah 45 membandingkan jumlah entri terhadap baseline. Percobaan TC-GS-PROFILE-118 dan TC-GS-PROFILE-251 pada akun #7 juga menambah entri Note yang sama.
- Temuan untuk QA:
  - TC-GS-PROFILE-117 memakai akun Pre-setup #18 tetapi menulis "pada tanggal fixture Pre-setup #7"; spec memakai tanggal fixture #7.
  - TC-GS-PROFILE-118 mensyaratkan timezone akun #7 Asia/Makassar tanpa menyebut cara mengubah timezone; kemampuan ditulis sebagai disediakan tim FE/BE.
  - TC-GS-PROFILE-251 tidak menyebut pelaku, cakupan (per user atau per Client), dan cara mengubah Time Format; juga tidak menyebut apakah FE membaca Time Format dan timezone baru tanpa muat ulang. Spec menambah muat ulang halaman (langkah 13 dan 19) sebagai langkah penghubung.
  - Post Condition tanpa langkah observasi tidak diasersi: TC-GS-PROFILE-115 (terkunci sampai 09:15; counter 3 diasersi lewat Expected TC-GS-PROFILE-119), TC-GS-PROFILE-117 (terkunci sampai 09:15 AM), TC-GS-PROFILE-118 (terkunci sampai 02:15 UTC).
