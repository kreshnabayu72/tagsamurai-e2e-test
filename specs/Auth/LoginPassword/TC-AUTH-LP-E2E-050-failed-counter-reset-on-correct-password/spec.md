---
id: TC-AUTH-LP-E2E-050-failed-counter-reset-on-correct-password
title: "Aturan Hitungan Gagal: Diatur Ulang saat Password Benar"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-68
  - TC-AUTH-LP-152
coverage:
  web: automated
---

# Aturan Hitungan Gagal: Diatur Ulang saat Password Benar

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. Kedua user dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: reCAPTCHA mode uji; device terpercaya dan tanpa MFA untuk kedua user; fixture BE yang menaruh versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui untuk user TC-AUTH-LP-152; membuka dan menutup tab browser.
- TC-AUTH-LP-68: Tanpa login (guest, browser web)
- TC-AUTH-LP-68: User `Zainal Abidin` (`zainalabidin+{runId}-050@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 hari ini (web), device terpercaya, tanpa gate Agreement dan MFA (di-seed lewat API di hook `before`)
- TC-AUTH-LP-68 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`; password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-152: Tanpa login (guest, browser web)
- TC-AUTH-LP-152: User `Salman Farisi` (`salmanfarisi+{runId}-050@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 hari ini (web), versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui, device terpercaya, tidak memicu MFA (di-seed oleh fixture BE)
- TC-AUTH-LP-152 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`; password benar `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-68: Login berhasil mengatur ulang hitungan gagal pada hari yang sama

1. Buka halaman Login with Password
2. Isi Email `zainalabidin+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in] (salah ke-1)
5. Isi Email `zainalabidin+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
6. Selesaikan reCAPTCHA
7. Klik [Log in] (salah ke-2)
8. Isi Password `Spectra.env.LP_PASSWORD`
9. Selesaikan reCAPTCHA
10. Klik [Log in] sampai Portal — Product Hub tampil
11. Logout
12. Buka halaman Login with Password
13. Isi Email `zainalabidin+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
14. Selesaikan reCAPTCHA
15. Klik [Log in] (salah baru ke-1)
16. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
17. Verifikasi Caption lock tidak tampil
18. Isi Email `zainalabidin+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
19. Selesaikan reCAPTCHA
20. Klik [Log in] (salah baru ke-2)
21. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
22. Verifikasi Caption lock tidak tampil
23. Isi Email `zainalabidin+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
24. Selesaikan reCAPTCHA
25. Klik [Log in] (salah baru ke-3)
26. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil ({time} = jam berakhirnya lock)
27. Verifikasi Salah baru ke-3 memicu lock 15 menit, bukan tahap yang lebih tinggi: hitungan gagal dan tahap lock harian hari itu kembali ke awal setelah login berhasil

### TC-AUTH-LP-152: Password benar yang berujung layar Confirm to Continue mengatur ulang hitungan gagal

28. Buka halaman Login with Password
29. Isi Email `salmanfarisi+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
30. Selesaikan reCAPTCHA
31. Klik [Log in] (salah ke-1)
32. Isi Email `salmanfarisi+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
33. Selesaikan reCAPTCHA
34. Klik [Log in] (salah ke-2)
35. Isi Password `Spectra.env.LP_PASSWORD`
36. Selesaikan reCAPTCHA
37. Klik [Log in] sampai layar Confirm to Continue tampil
38. Verifikasi Layar Confirm to Continue tampil
39. Tutup tab tanpa [Continue ➔]
40. Buka tab baru dan buka halaman Login with Password
41. Isi Email `salmanfarisi+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
42. Selesaikan reCAPTCHA
43. Klik [Log in] (salah baru ke-1)
44. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
45. Verifikasi Caption lock tidak tampil
46. Isi Email `salmanfarisi+{runId}-050@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
47. Selesaikan reCAPTCHA
48. Klik [Log in] (salah baru ke-2)
49. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
50. Verifikasi Caption lock tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian spec: TC-AUTH-LP-66 dan TC-AUTH-LP-67 (percobaan yang tidak dihitung) ada di spec `TC-AUTH-LP-E2E-016-failed-counter-rules`; spec ini memuat TC-AUTH-LP-68 dan 152. Kedua kelompok independen (user seeding berbeda) dan bagian sesudahnya tidak bermakna bila yang sebelumnya gagal keras; spec ini membutuhkan login berhasil atau layar Confirm to Continue.
- Spec ini berisi 50 langkah (melewati batas tinjau sekitar 35 langkah) karena dua skenario yang masing-masing mengulang tiga percobaan salah sebelum dan sesudah password benar; tiap TC memakai user seeding sendiri.
- Email diisi bersama Password pada tiap percobaan sebagaimana TC; hanya langkah 8 dan 35 (Langkah Uji 4 kedua TC) mengisi Password saja, sesuai TC, dan di sana Email masih terisi dari percobaan sebelumnya.
- Langkah penghubung (S-03): logout (langkah 11) dan menutup tab lalu membuka tab baru (langkah 39 dan 40) mengembalikan sesi ke guest; pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Hitungan gagal di sisi server tidak punya cara baca lewat UI sehingga tiap TC memverifikasi hitungan lewat perilaku Alert (lock 15 menit pada percobaan ke-3 atau tidak munculnya caption lock).
- Temuan untuk QA (TC-AUTH-LP-68): Expected Result (c) ("hitungan gagal dan tahap lock harian hari itu kembali ke awal setelah langkah 4") adalah penjelasan, bukan keadaan yang dapat dibaca di UI; spec menulisnya sebagai Verifikasi atas perilaku lock 15 menit pada salah baru ke-3 (bukan tahap yang lebih tinggi).
- Temuan untuk QA (TC-AUTH-LP-152): Langkah Uji 5 "Tutup tab" menyiratkan sesi pra-autentikasi dibuang; spec tidak menambah asersi untuk itu.
- Temuan untuk QA (TC-AUTH-LP-68 dan TC-AUTH-LP-152): langkah 4 kedua TC ("Isi Password ... lalu klik [Log in]") tidak menyebut reCAPTCHA, padahal widget kembali Unsolved setelah tiap respons (TC-AUTH-LP-31 Expected b); spec menyelesaikan reCAPTCHA sebelum tiap submit. Langkah 6 dan 7 TC-AUTH-LP-152 ("salah baru") juga tidak memberi Post Condition untuk hitungan gagal; hitungan hanya diamati lewat Alert.
