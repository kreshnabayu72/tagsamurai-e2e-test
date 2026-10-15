---
id: TC-AUTH-LP-E2E-016-failed-counter-rules
title: "Aturan Hitungan Gagal: Percobaan yang Tidak Dihitung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-66
  - TC-AUTH-LP-67
coverage:
  web: automated
---

# Aturan Hitungan Gagal: Percobaan yang Tidak Dihitung

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. Kedua user dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: reCAPTCHA mode uji; General Settings entitas memakai Time Zone dan Time Format default.
- TC-AUTH-LP-66: Tanpa login (guest, browser web)
- TC-AUTH-LP-66: User `Kevin Hartanto` (`kevinhartanto+{runId}-016@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (web) (di-seed lewat API di hook `before`)
- TC-AUTH-LP-66 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-67: Tanpa login (guest, browser web)
- TC-AUTH-LP-67: User `Lestari Wulan` (`lestariwulan+{runId}-016@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (web) (di-seed lewat API di hook `before`)
- TC-AUTH-LP-67 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-66: Percobaan Password kosong tidak menambah hitungan gagal

1. Buka halaman Login with Password
2. Isi Email `kevinhartanto+{runId}-016@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in] (salah ke-1)
5. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
6. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
7. Selesaikan reCAPTCHA
8. Klik [Log in] (salah ke-2)
9. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
10. Kosongkan field Password
11. Selesaikan reCAPTCHA
12. Klik [Log in]
13. Verifikasi Caption "Password must not be empty" tampil di bawah field Password
14. Verifikasi Caption lock tidak tampil
15. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
16. Selesaikan reCAPTCHA
17. Klik [Log in] (salah ke-3)
18. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (lock pada kegagalan password ke-3)

### TC-AUTH-LP-67: Percobaan tanpa reCAPTCHA tidak menambah hitungan gagal

19. Buka halaman Login with Password
20. Isi Email `lestariwulan+{runId}-016@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
21. Selesaikan reCAPTCHA
22. Klik [Log in] (salah ke-1)
23. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
24. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
25. Selesaikan reCAPTCHA
26. Klik [Log in] (salah ke-2)
27. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
28. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
29. Tanpa menyelesaikan reCAPTCHA, klik [Log in]
30. Verifikasi Caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
31. Verifikasi Caption lock tidak tampil
32. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
33. Selesaikan reCAPTCHA
34. Klik [Log in] (salah ke-3)
35. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (lock pada kegagalan password ke-3)

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemisahan: TC-AUTH-LP-68 dan TC-AUTH-LP-152 (hitungan gagal diatur ulang saat password benar) diuji di spec `TC-AUTH-LP-E2E-050-failed-counter-reset-on-correct-password`. Kedua kelompok independen (user seeding berbeda) dan bagian sesudahnya tidak bermakna bila yang sebelumnya gagal keras, karena kelompok 68 dan 152 membutuhkan login berhasil atau layar Agreement.
- Spec ini berisi 35 langkah dengan dua skenario independen (TC-AUTH-LP-66 dan TC-AUTH-LP-67), masing-masing dengan user seeding sendiri.
- Langkah penghubung (S-03): pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Hitungan gagal di sisi server tidak punya cara baca lewat UI sehingga tiap TC memverifikasi hitungan lewat perilaku Alert pada percobaan ke-3 (lock 15 menit) atau tidak munculnya caption lock.
