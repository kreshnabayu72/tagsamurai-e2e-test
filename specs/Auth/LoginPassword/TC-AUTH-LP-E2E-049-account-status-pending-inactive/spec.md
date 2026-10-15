---
id: TC-AUTH-LP-E2E-049-account-status-pending-inactive
title: "Penolakan Login Akun Pending Activation dan Akun Inactive"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-31
  - TC-AUTH-LP-35
  - TC-AUTH-LP-36
  - TC-AUTH-LP-33
  - TC-AUTH-LP-32
  - TC-AUTH-LP-34
coverage:
  web: automated
---

# Penolakan Login Akun Pending Activation dan Akun Inactive

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-049` (contoh `dewilestari+{runId}-049@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: reCAPTCHA mode uji di environment; user berstatus Pending Activation (dibuat lewat Create User tanpa menyelesaikan aktivasi); user Activated dengan Toggle Global OFF (dibuat lewat API lalu Toggle Global dimatikan oleh aktor GS).
- TC-AUTH-LP-31: Tanpa login (guest); browser web
- TC-AUTH-LP-31: User `Dewi Lestari` (`dewilestari+{runId}-049@qwertysystem.net`) berstatus Pending Activation, hitungan gagal 0 (di-seed lewat API di hook `before`, aktivasi tidak diselesaikan)
- TC-AUTH-LP-31 data: Email: `dewilestari+{runId}-049@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-35: Tanpa login (guest); browser web; User `Dewi Lestari` (`dewilestari+{runId}-049@qwertysystem.net`) berstatus Pending Activation
- TC-AUTH-LP-35 data: Email: `dewilestari+{runId}-049@qwertysystem.net`; Password: (kosong)
- TC-AUTH-LP-36: Tanpa login (guest); browser web; User `Dewi Lestari` (`dewilestari+{runId}-049@qwertysystem.net`) berstatus Pending Activation
- TC-AUTH-LP-36 data: Email: `dewilestari+{runId}-049@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-33: Tanpa login (guest); browser web; User `Dewi Lestari` (`dewilestari+{runId}-049@qwertysystem.net`) berstatus Pending Activation, hitungan gagal 0
- TC-AUTH-LP-33 data: Email: `dewilestari+{runId}-049@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-32: Tanpa login (guest); browser web
- TC-AUTH-LP-32: User `Agus Setiawan` (`agussetiawan+{runId}-049@qwertysystem.net`) berstatus Activated dengan Toggle Global OFF di Global Settings > User, hitungan gagal 0 (di-seed lewat API di hook `before`, Toggle Global dimatikan oleh aktor GS)
- TC-AUTH-LP-32 data: Email: `agussetiawan+{runId}-049@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-34: Tanpa login (guest); browser web; User `Agus Setiawan` (`agussetiawan+{runId}-049@qwertysystem.net`) berstatus Activated dengan Toggle Global OFF, hitungan gagal 0
- TC-AUTH-LP-34 data: Email: `agussetiawan+{runId}-049@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-31: Login akun yang belum diaktivasi

1. Buka halaman Login with Password
2. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger "Your account has not been activated" tampil di atas Button [Log in]
6. Verifikasi field Email tetap berisi "dewilestari+{runId}-049@qwertysystem.net"
7. Verifikasi field Password dikosongkan
8. Verifikasi widget reCAPTCHA kembali Unsolved
9. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-35: Akun belum aktivasi dengan Password kosong menampilkan caption Password kosong

10. Muat ulang halaman Login with Password
11. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan kosongkan field Password
12. Selesaikan reCAPTCHA
13. Klik [Log in]
14. Verifikasi caption "Password must not be empty" tampil di bawah field Password
15. Verifikasi Alert "Your account has not been activated" tidak tampil

### TC-AUTH-LP-36: Akun belum aktivasi tanpa reCAPTCHA menampilkan caption reCAPTCHA

16. Muat ulang halaman Login with Password
17. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
18. Tanpa menyelesaikan reCAPTCHA, klik [Log in]
19. Verifikasi caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
20. Verifikasi Alert "Your account has not been activated" tidak tampil

### TC-AUTH-LP-33: Akun belum aktivasi dengan password salah tiga kali tidak pernah terkunci

21. Muat ulang halaman Login with Password
22. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-1)
23. Selesaikan reCAPTCHA
24. Klik [Log in]
25. Verifikasi Alert Danger "Your account has not been activated" tampil
26. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil
27. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-2)
28. Selesaikan reCAPTCHA
29. Klik [Log in]
30. Verifikasi Alert Danger "Your account has not been activated" tampil
31. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil
32. Isi field Email dengan "dewilestari+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-3)
33. Selesaikan reCAPTCHA
34. Klik [Log in]
35. Verifikasi Alert Danger "Your account has not been activated" tampil
36. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil

### TC-AUTH-LP-32: Login akun yang dinonaktifkan (Toggle Global OFF)

37. Muat ulang halaman Login with Password
38. Isi field Email dengan "agussetiawan+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
39. Selesaikan reCAPTCHA
40. Klik [Log in]
41. Verifikasi Alert Danger "Your account is inactive" tampil di atas Button [Log in]
42. Verifikasi field Email tetap berisi "agussetiawan+{runId}-049@qwertysystem.net"
43. Verifikasi field Password dikosongkan
44. Verifikasi widget reCAPTCHA kembali Unsolved
45. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-34: Akun inactive dengan password salah tiga kali tidak pernah terkunci

46. Muat ulang halaman Login with Password
47. Isi field Email dengan "agussetiawan+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-1)
48. Selesaikan reCAPTCHA
49. Klik [Log in]
50. Verifikasi Alert Danger "Your account is inactive" tampil
51. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil
52. Isi field Email dengan "agussetiawan+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-2)
53. Selesaikan reCAPTCHA
54. Klik [Log in]
55. Verifikasi Alert Danger "Your account is inactive" tampil
56. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil
57. Isi field Email dengan "agussetiawan+{runId}-049@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG` (percobaan ke-3)
58. Selesaikan reCAPTCHA
59. Klik [Log in]
60. Verifikasi Alert Danger "Your account is inactive" tampil
61. Verifikasi Alert "Incorrect email or password" dan caption lock tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian spec: spec ini memuat kasus penolakan karena kondisi data akun (Pending Activation dan Inactive) yang butuh data prasyarat khusus (prinsip 12); penolakan email tak terdaftar dan kredensial salah ada di spec `TC-AUTH-LP-E2E-006-account-status-and-unregistered-email`.
- Spec ini berisi 61 langkah, sekitar 38 setelah prefix login faktor-1 yang identik tidak dihitung (konvensi §3 smell), karena TC-AUTH-LP-33 dan TC-AUTH-LP-34 masing-masing mengulang tiga percobaan login yang ditolak (data akun berbeda, alur sama) dan tidak bermakna bila dipecah dari TC akun yang sama.
- Urutan dikelompokkan per akun (`Dewi Lestari`, lalu `Agus Setiawan`) supaya state tiap akun tidak saling mengganggu: TC-AUTH-LP-31, 35, 36, 33, 32, 34. Urutan ini berbeda dari urutan TC sumber.
- Langkah penghubung (S-03): "Muat ulang halaman Login with Password" sebelum tiap TC setelah yang pertama (S-09); tanpa `Verifikasi`. Pada TC-AUTH-LP-33 dan 34, field Email dan Password diisi pada tiap percobaan ("Ulangi langkah 2" TC mengisi Email dan Password) agar konsisten, karena Password dikosongkan setelah penolakan (Expected TC-AUTH-LP-31 butir b).
- Langkah 9 dan 45 hanya memuat Expected c ("Tidak ada sesi dibuat"); sesi web teramati sebagai halaman tetap di Login with Password. Post Condition "status akun tetap" TC-AUTH-LP-31 dan TC-AUTH-LP-32 tidak punya langkah observasi di TC sehingga tidak diasersi (dicatat di Temuan untuk QA).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC sehingga tidak diasersi (S-01): TC-AUTH-LP-31 "Status akun `dewilestari@qwertysystem.net` tetap Pending Activation" dan TC-AUTH-LP-32 "Status akun `agussetiawan@qwertysystem.net` tetap Toggle Global OFF". Spec tidak menambah langkah observasi sendiri.
  - TC-AUTH-LP-33 dan TC-AUTH-LP-34 langkah TC 4 ("Ulangi langkah 2 dua kali lagi") hanya mengulang pengisian Email dan Password, padahal reCAPTCHA kembali Unsolved setelah tiap penolakan (Expected b TC-AUTH-LP-31 dan TC-AUTH-LP-32); spec menyelesaikan reCAPTCHA pada tiap percobaan.
  - TC-AUTH-LP-33 dan TC-AUTH-LP-34 tidak punya Post Condition untuk hitungan gagal ("tidak pernah terkunci" hanya diamati lewat tidak munculnya Alert "Incorrect email or password" dan caption lock).
