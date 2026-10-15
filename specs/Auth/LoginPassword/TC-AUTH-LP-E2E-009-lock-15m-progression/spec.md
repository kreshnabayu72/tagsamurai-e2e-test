---
id: TC-AUTH-LP-E2E-009-lock-15m-progression
title: "Progresi Lock 15 Menit pada Kegagalan Password"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-29
  - TC-AUTH-LP-30
  - TC-AUTH-LP-38
  - TC-AUTH-LP-39
  - TC-AUTH-LP-40
  - TC-AUTH-LP-41
coverage:
  web: automated
---

# Progresi Lock 15 Menit pada Kegagalan Password

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: reCAPTCHA mode uji di environment (dapat diselesaikan otomatis); jam server uji dan jam browser/klien dapat diatur bersama (dimajukan 70 detik pada TC-AUTH-LP-41, tanpa menunggu waktu nyata; bila batas waktu penting, diset absolut ke waktu terbit Alert + 70 detik); General Settings entitas memakai Time Zone dan Time Format default (`HH:mm`).
- State global: suite berjalan serial (`parallel: false`); jam server uji dan jam browser diubah pada TC-AUTH-LP-41 dan dipulihkan ke waktu nyata di hook `after` (tetap jalan walau spec gagal di tengah).
- TC-AUTH-LP-29: Tanpa login (guest, browser web)
- TC-AUTH-LP-29: User `Rina Putri` (`rinaputri+{runId}-009@qwertysystem.net`) berstatus Activated dan Active, password `Spectra.env.LP_PASSWORD`, hitungan gagal hari ini (web) = 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-29 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-30: Tanpa login (guest); user yang sama sudah 1 kali salah password hari ini (hasil TC-AUTH-LP-29 dalam spec ini, dijalankan berurutan)
- TC-AUTH-LP-38: Tanpa login (guest); user yang sama sudah 2 kali salah password hari ini (hasil TC-AUTH-LP-29 dan TC-AUTH-LP-30 dalam spec ini)
- TC-AUTH-LP-39: Tanpa login (guest); user yang sama sedang terkunci 15 menit di web (hasil TC-AUTH-LP-38 dalam spec ini)
- TC-AUTH-LP-40: Tanpa login (guest); user yang sama sedang terkunci 15 menit di web dengan password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-41: Tanpa login (guest); user yang sama sedang terkunci 15 menit di web

## Test Steps

### TC-AUTH-LP-29: Login dengan password salah (percobaan ke-1)

1. Buka halaman Login with Password
2. Isi Email `rinaputri+{runId}-009@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
6. Verifikasi Alert tidak memuat caption lock
7. Verifikasi field Email tetap berisi "rinaputri+{runId}-009@qwertysystem.net"
8. Verifikasi field Password dikosongkan
9. Verifikasi widget reCAPTCHA kembali Unsolved
10. Verifikasi field Email enabled
11. Verifikasi field Password enabled
12. Verifikasi Button [Log in] enabled

### TC-AUTH-LP-30: Login dengan password salah (percobaan ke-2)

13. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
14. Selesaikan reCAPTCHA
15. Klik [Log in]
16. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
17. Verifikasi Alert tidak memuat caption lock
18. Verifikasi Button [Log in] enabled

### TC-AUTH-LP-38: Password salah ke-3 pada hari yang sama memicu lock 15 menit

19. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
20. Selesaikan reCAPTCHA
21. Klik [Log in]
22. Verifikasi Alert Danger di atas Button [Log in]: "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." ({time} = jam berakhirnya lock dalam Time Format General Settings dan Time Zone entitas, hanya jam tanpa tanggal)
23. Catat nilai {time} pada Alert
24. Verifikasi Alert tidak memuat tautan [Reset password]
25. Verifikasi Link "Forgot your password? " [Reset here] di footer tetap tampil
26. Verifikasi field Email tetap enabled
27. Verifikasi field Password tetap enabled
28. Verifikasi Button [Log in] tetap enabled
29. Verifikasi field Password dikosongkan
30. Verifikasi widget reCAPTCHA kembali Unsolved

### TC-AUTH-LP-39: Submit password salah selama lock 15 menit aktif menampilkan caption lock yang sama

31. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
32. Selesaikan reCAPTCHA
33. Klik [Log in]
34. Catat nilai {time} pada Alert (percobaan pertama saat lock aktif)
35. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil pada percobaan pertama saat lock aktif
36. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
37. Selesaikan reCAPTCHA
38. Klik [Log in]
39. Catat nilai {time} pada Alert (percobaan kedua saat lock aktif)
40. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil pada percobaan kedua saat lock aktif
41. Verifikasi nilai {time} percobaan kedua identik dengan nilai {time} percobaan pertama
42. Verifikasi nilai {time} percobaan kedua identik dengan nilai {time} saat lock terpicu (langkah 23), tidak dihitung ulang
43. Verifikasi Alert "Incorrect email or password" tidak tampil

### TC-AUTH-LP-40: Submit password benar selama lock 15 menit aktif tetap ditolak

44. Isi Password `Spectra.env.LP_PASSWORD`
45. Selesaikan reCAPTCHA
46. Klik [Log in]
47. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil
48. Verifikasi browser tetap di halaman Login with Password
49. Verifikasi tidak ada sesi dibuat
50. Verifikasi browser tidak menuju Portal — Product Hub

### TC-AUTH-LP-41: Caption lock tidak berubah seiring waktu berjalan (tanpa countdown)

51. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
52. Selesaikan reCAPTCHA
53. Klik [Log in]
54. Catat teks Alert
55. Majukan jam server uji dan jam browser bersama 70 detik (tanpa menunggu waktu nyata)
56. Catat teks Alert lagi
57. Verifikasi teks Alert pada langkah 56 identik dengan langkah 54 (nilai {time} sama persis)
58. Verifikasi tidak ada hitung mundur pada Alert

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Rantai dependensi di TC sumber (kolom Dependensi): TC-AUTH-LP-30 bergantung pada TC-AUTH-LP-29; TC-AUTH-LP-38 pada TC-AUTH-LP-30; TC-AUTH-LP-39, TC-AUTH-LP-40, dan TC-AUTH-LP-41 pada TC-AUTH-LP-38. Di spec ini dependensi dipenuhi dengan menjalankan langkah tiap TC berurutan pada user yang sama (S-04), bukan dirujuk.
- Langkah penghubung (S-03): halaman Login with Password tidak dibuka ulang antar TC karena setelah tiap respons gagal form tetap berisi Email dan Password dikosongkan; pengisian Password dan penyelesaian reCAPTCHA diulang sebelum tiap submit (reCAPTCHA kembali Unsolved setelah respons). Tidak ada asersi tambahan di luar TC.
- Pemisahan lock 15 menit (spec ini) dari urutan evaluasi lock terhadap Password kosong dan reCAPTCHA (`TC-AUTH-LP-42`, `TC-AUTH-LP-43`, spec `TC-AUTH-LP-E2E-010-lock-15m-evaluation-order`) mengikuti prinsip bagian 3 konvensi: kasus yang butuh state lock dipisah dari alur yang membangun state lock.
- TC-AUTH-LP-41 tidak menunggu 70 detik nyata: jam server uji dan jam browser dimajukan bersama 70 detik (bagian 6 konvensi), dipulihkan di hook `after`. Suite serial karena jam adalah state global.
- Jumlah langkah melewati ~35 (smell): satu topik (progresi lock 15 menit pada satu user berantai TC-AUTH-LP-29 sampai 41), dan bagian sesudahnya bergantung pada state yang dibangun bagian sebelumnya sehingga tidak bisa dipecah tanpa seeding ulang.
- Temuan untuk QA: Post Condition "Hitungan gagal hari ini = …" pada TC-AUTH-LP-29 (= 1) dan TC-AUTH-LP-30 (= 2), serta Post Condition TC-AUTH-LP-38 (akun terkunci 15 menit), tidak punya langkah observasi di TC (UI tidak menampilkan hitungan) sehingga tidak diasersi; hitungan hanya teramati tidak langsung lewat Alert percobaan berikutnya.
