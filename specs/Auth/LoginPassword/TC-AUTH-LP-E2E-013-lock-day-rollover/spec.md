---
id: TC-AUTH-LP-E2E-013-lock-day-rollover
title: "Pergantian Hari pada Hitungan Gagal dan Lock"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-53
  - TC-AUTH-LP-54
  - TC-AUTH-LP-55
  - TC-AUTH-LP-56
  - TC-AUTH-LP-57
coverage:
  web: automated
---

# Pergantian Hari pada Hitungan Gagal dan Lock

## Prerequisites

- Mode: FE+BE.
- Seeding: lima user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. Semua user dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: geser jam server uji maju; fixture BE yang menulis riwayat lock tiap user (tanggal kejadian lock dalam zona waktu General Settings entitas) sehingga pada saat TC berjalan percobaan terakhir berada pada hari kalender sebelumnya; reCAPTCHA mode uji; General Settings entitas memakai Time Zone dan Time Format default. Pemulihan: hook `after` mengembalikan jam server uji ke waktu nyata dan menghapus semua user.
- State global: suite berjalan serial (`parallel: false`) karena jam server uji diubah; hook `after` memulihkan jam server uji ke waktu nyata (tetap jalan walau spec gagal di tengah). Pembekuan jam server uji pada 00:05 hari berikutnya hanya dibutuhkan TC-AUTH-LP-55 (precondition-nya), dilakukan pada langkah 31, berlaku sampai langkah 36, dan dilepas pada langkah 37. TC-AUTH-LP-53, 54, 56, dan 57 tidak bergantung pada nilai jam itu, hanya pada hari kalender sekarang yang lebih baru dari tanggal riwayat lock hasil seeding.
- TC-AUTH-LP-53: Tanpa login (guest, browser web)
- TC-AUTH-LP-53: User `Hendra Wijaya` (`hendrawijaya+{runId}-013@qwertysystem.net`) berstatus Activated dan Active, pernah terkunci 15 menit pada hari kalender sebelumnya dan tidak mencapai lock 1 jam (di-seed oleh fixture BE)
- TC-AUTH-LP-53 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-54: Tanpa login (guest, browser web)
- TC-AUTH-LP-54: User `Linda Sari` (`lindasari+{runId}-013@qwertysystem.net`) berstatus Activated dan Active, pernah terkunci 1 jam pada hari kalender sebelumnya dan tidak mencapai Requires Reset (di-seed oleh fixture BE)
- TC-AUTH-LP-54 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-55: Tanpa login (guest, browser web)
- TC-AUTH-LP-55: User `Mira Lestari` (`miralestari+{runId}-013@qwertysystem.net`) berstatus Activated dan Active, terkunci 15 menit pada pukul 23:55 (zona waktu General Settings) dengan jam server uji sekarang 00:05 hari berikutnya sehingga lock belum berakhir (di-seed oleh fixture BE)
- TC-AUTH-LP-55 data: Password benar `Spectra.env.LP_PASSWORD`; password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-56: Tanpa login (guest, browser web)
- TC-AUTH-LP-56: User `Rina Putri` (`rinaputri+{runId}-013@qwertysystem.net`) berstatus Requires Reset di web dengan percobaan terakhir pada hari kalender sebelumnya (di-seed oleh fixture BE)
- TC-AUTH-LP-56 data: Password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-57: Tanpa login (guest, browser web)
- TC-AUTH-LP-57: User `Candra Bayu` (`candrabayu+{runId}-013@qwertysystem.net`) berstatus Activated dan Active, mencapai lock 1 jam pada 6 hari kalender berturut-turut lalu pada hari ke-7 hanya mencapai lock 15 menit, dan hari kalender sekarang adalah hari ke-8 (di-seed oleh fixture BE)
- TC-AUTH-LP-57 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-53: Hari berganti mereset hitungan setelah lock 15 menit

1. Buka halaman Login with Password
2. Isi Email `hendrawijaya+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
6. Verifikasi caption lock tidak tampil
7. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
8. Selesaikan reCAPTCHA
9. Klik [Log in]
10. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
11. Verifikasi caption lock tidak tampil
12. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
13. Selesaikan reCAPTCHA
14. Klik [Log in]
15. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (lock 15 menit, bukan 1 jam)

### TC-AUTH-LP-54: Hari berganti mereset hitungan setelah lock 1 jam

16. Muat ulang halaman Login with Password
17. Isi Email `lindasari+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
18. Selesaikan reCAPTCHA
19. Klik [Log in]
20. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
21. Verifikasi caption lock tidak tampil
22. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
23. Selesaikan reCAPTCHA
24. Klik [Log in]
25. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
26. Verifikasi caption lock tidak tampil
27. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
28. Selesaikan reCAPTCHA
29. Klik [Log in]
30. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (lock 15 menit, kembali ke tahap awal)

### TC-AUTH-LP-55: Lock yang masih aktif tetap berlaku melewati tengah malam

31. Bekukan jam server uji pada 00:05 hari berikutnya
32. Muat ulang halaman Login with Password
33. Isi Email `miralestari+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
34. Selesaikan reCAPTCHA
35. Klik [Log in]
36. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil meski hari sudah berganti
37. Lepas pembekuan jam server uji lalu majukan sampai lock berakhir dan melewati 00:10
38. Muat ulang halaman Login with Password
39. Isi Email `miralestari+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
40. Selesaikan reCAPTCHA
41. Klik [Log in]
42. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in] (hitungan hari baru dimulai dari percobaan ke-1)

### TC-AUTH-LP-56: Status Requires Reset tidak reset karena pergantian hari

43. Muat ulang halaman Login with Password
44. Isi Email `rinaputri+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
45. Selesaikan reCAPTCHA
46. Klik [Log in]
47. Verifikasi Alert Danger "Please reset your password" tampil
48. Verifikasi tautan [Reset password] tampil di bawah teks Alert
49. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-57: Hitungan hari berturut-turut putus bila satu hari tidak mencapai lock 1 jam

50. Muat ulang halaman Login with Password
51. Isi Email `candrabayu+{runId}-013@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
52. Selesaikan reCAPTCHA
53. Klik [Log in]
54. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
55. Verifikasi Alert lock Permanent "For security reasons, your account has been locked. Please reset your password to regain access." tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-LP-56 tergantung TC-AUTH-LP-50 di TC sumber (kolom Dependensi). State Requires Reset disiapkan lewat seeding fixture BE (S-04); progresi yang membangunnya diuji di spec `TC-AUTH-LP-E2E-012-lock-1h-expiry-requires-reset`.
- Jumlah langkah melewati ~35 (smell): satu topik (pergantian hari pada hitungan gagal dan lock); tiap TC memakai user sendiri yang di-seed, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (S-03): "Bekukan jam server uji pada 00:05 hari berikutnya" (langkah 31) menyiapkan precondition TC-AUTH-LP-55 sebelum Alert diverifikasi; tanpa asersi. "Muat ulang halaman Login with Password" memulai tiap TC dengan form bersih (Email user berbeda per TC); tidak ada asersi tambahan. Pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Temuan untuk QA (TC-AUTH-LP-53, 54, 56, 57): precondition ditulis "waktu server uji sudah dimajukan ke hari berikutnya oleh tim BE" tanpa langkah; spec menjadikannya bagian seeding fixture BE (riwayat lock bertanggal mundur) agar keempat TC itu hanya bergantung pada tanggal riwayat lock, bukan pada jam server yang dibekukan atau bergeser (pembekuan 00:05 hanya untuk TC-AUTH-LP-55, lihat Prerequisites). Bila tim BE hanya dapat menggeser jam server uji, urutan dan jam harus diatur ulang.
- Temuan untuk QA (TC-AUTH-LP-55): precondition menyebut jam server uji sekarang 00:05 hari berikutnya (lock 23:55 belum berakhir), tetapi Langkah Uji 3 menyuruh memajukan jam "sampai lock berakhir dan melewati 00:10"; spec mengikuti keduanya. Nilai {time} pada Alert langkah 36 tidak ditentukan sehingga hanya teks Alert yang diverifikasi.
