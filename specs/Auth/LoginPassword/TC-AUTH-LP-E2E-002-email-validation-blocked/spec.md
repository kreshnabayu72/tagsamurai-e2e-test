---
id: TC-AUTH-LP-E2E-002-email-validation-blocked
title: "Validasi Field Email: Submit Diblokir dan Batas Format serta Panjang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-10
  - TC-AUTH-LP-11
  - TC-AUTH-LP-12
  - TC-AUTH-LP-13
  - TC-AUTH-LP-14
  - TC-AUTH-LP-15
  - TC-AUTH-LP-16
  - TC-AUTH-LP-17
  - TC-AUTH-LP-161
coverage:
  web: automated
---

# Validasi Field Email: Submit Diblokir dan Batas Format serta Panjang

## Prerequisites

- Mode: FE+BE. Dua kasus terakhir (TC-AUTH-LP-15 dan TC-AUTH-LP-16) memerlukan pengecekan Email terdaftar oleh backend nyata.
- Tanpa seeding dan tanpa login akun aktor: seluruh email adalah nilai uji yang sengaja salah format atau tidak terdaftar, sehingga tidak ada data yang dibuat dan tidak ada cleanup. Tidak ada percobaan yang menambah hitungan gagal user mana pun.
- Environment variable: `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: reCAPTCHA mode uji di environment (dapat diselesaikan otomatis); pengamatan caption inline dan perpindahan fokus (blur).
- TC-AUTH-LP-14: Tanpa login (guest); browser web
- TC-AUTH-LP-14 data: Email: `budisantoso@`
- TC-AUTH-LP-10: Tanpa login (guest); browser web
- TC-AUTH-LP-10 data: Email: (kosong); Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-11: Tanpa login (guest); browser web
- TC-AUTH-LP-11 data: Email: `budisantoso.qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-12: Tanpa login (guest); browser web
- TC-AUTH-LP-12 data: Email: `budisantoso@qwertysystem.n`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-13: Tanpa login (guest); browser web
- TC-AUTH-LP-13 data: Email: `budisantoso@qwertysystem`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-17: Tanpa login (guest); browser web
- TC-AUTH-LP-17 data: Email: 104 × `a` + `@qwertysystem.net` (121 karakter); Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-161: Tanpa login (guest); browser web
- TC-AUTH-LP-161 data: Email: 121 × `a` (tanpa `@`); Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-15: Tanpa login (guest); browser web; Email `budisantoso@qwertysystem.id` belum terdaftar di Global Settings > User
- TC-AUTH-LP-15 data: Email: `budisantoso@qwertysystem.id`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-16: Tanpa login (guest); browser web; Email 120 karakter yang dipakai belum terdaftar
- TC-AUTH-LP-16 data: Email: 103 × `a` + `@qwertysystem.net` (120 karakter); Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-14: Caption format Email muncul saat field Email kehilangan fokus

1. Buka halaman Login with Password
2. Ketik "budisantoso@" di field Email
3. Klik field Password (field Email kehilangan fokus) tanpa klik [Log in]
4. Verifikasi caption "Email format is incorrect" tampil di bawah field Email sebelum Button [Log in] diklik

### TC-AUTH-LP-10: Submit dengan Email kosong

5. Muat ulang halaman Login with Password
6. Kosongkan field Email dan isi field Password dengan nilai `Spectra.env.LP_PASSWORD`
7. Selesaikan reCAPTCHA
8. Klik [Log in]
9. Verifikasi caption "Email must not be empty" tampil di bawah field Email
10. Verifikasi Alert pesan server tidak tampil
11. Verifikasi tidak ada sesi dibuat
12. Verifikasi halaman tetap di Login with Password

### TC-AUTH-LP-11: Submit dengan Email tanpa karakter @

13. Muat ulang halaman Login with Password
14. Isi field Email dengan "budisantoso.qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
18. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-12: Submit dengan Email yang karakter setelah titik terakhir kurang dari 2

19. Muat ulang halaman Login with Password
20. Isi field Email dengan "budisantoso@qwertysystem.n" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
21. Selesaikan reCAPTCHA
22. Klik [Log in]
23. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
24. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-13: Submit dengan Email tanpa titik pada bagian domain

25. Muat ulang halaman Login with Password
26. Isi field Email dengan "budisantoso@qwertysystem" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
27. Selesaikan reCAPTCHA
28. Klik [Log in]
29. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
30. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-17: Email 121 karakter menampilkan caption batas panjang

31. Muat ulang halaman Login with Password
32. Ketik Email dengan 104 karakter "a" diikuti "@qwertysystem.net" (total 121 karakter) di field Email
33. Amati area di bawah field Email
34. Verifikasi field Email menerima seluruh 121 karakter
35. Verifikasi caption "Max. 120 characters" tampil di bawah field Email saat mengetik
36. Isi field Password dengan nilai `Spectra.env.LP_PASSWORD`
37. Selesaikan reCAPTCHA
38. Klik [Log in]
39. Verifikasi caption "Max. 120 characters" tetap tampil di bawah field Email
40. Verifikasi caption "Email is not registered yet" tidak tampil
41. Verifikasi Alert pesan server tidak tampil
42. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-161: Email 121 karakter tanpa tanda @ menampilkan caption format, bukan caption batas panjang

43. Muat ulang halaman Login with Password
44. Ketik Email dengan 121 karakter "a" tanpa tanda @ di field Email
45. Pindahkan fokus ke field Password (blur)
46. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
47. Verifikasi caption "Max. 120 characters" tidak tampil
48. Isi field Password dengan nilai `Spectra.env.LP_PASSWORD`
49. Selesaikan reCAPTCHA
50. Klik [Log in]
51. Verifikasi caption "Email format is incorrect" tetap tampil
52. Verifikasi caption "Max. 120 characters" tidak tampil
53. Verifikasi caption "Email is not registered yet" tidak tampil
54. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-15: Email dengan 2 karakter setelah titik terakhir lolos validasi format

55. Muat ulang halaman Login with Password
56. Isi field Email dengan "budisantoso@qwertysystem.id" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
57. Selesaikan reCAPTCHA
58. Klik [Log in]
59. Verifikasi caption "Email format is incorrect" tidak tampil
60. Verifikasi caption "Email is not registered yet" tampil di bawah field Email

### TC-AUTH-LP-16: Email tepat 120 karakter tidak ditolak karena panjang

61. Muat ulang halaman Login with Password
62. Isi field Email dengan 103 karakter "a" diikuti "@qwertysystem.net" (total 120 karakter) dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
63. Selesaikan reCAPTCHA
64. Klik [Log in]
65. Verifikasi caption "Max. 120 characters" tidak tampil
66. Verifikasi caption "Email is not registered yet" tampil di bawah field Email

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Screening tanpa submit (TC-AUTH-LP-14, blur) ditaruh paling awal; validasi yang diblokir di sisi form (TC-AUTH-LP-10 sampai 13 dan 161) serta TC-AUTH-LP-17 (jalur submit tidak dinyatakan TC, lihat Temuan untuk QA; diperlakukan sebagai validasi Email yang tidak menghasilkan caption "Email is not registered yet") mendahului dua kasus yang diteruskan ke backend (TC-AUTH-LP-15 dan 16), sesuai prinsip 3. Urutan spec berbeda dari urutan TC sumber.
- Langkah penghubung (S-03): "Muat ulang halaman Login with Password" sebelum tiap TC setelah yang pertama untuk mengembalikan form ke state bersih (S-09); tanpa `Verifikasi`.
- TC-AUTH-LP-161 terbagi lintas spec: asersi "Tidak ada entri log baru untuk percobaan ini" (Expected butir c) diuji di spec `TC-AUTH-LP-E2E-042-absence-input-rejections` (kelas g, S-05).
- Temuan untuk QA: TC-AUTH-LP-17 langkah 4 menyebut "klik [Log in]" tanpa menjelaskan apakah submit dikirim ke server atau diblokir di sisi form; Expected hanya menyebut tidak ada caption "Email is not registered yet" dan tidak ada sesi. Spec mengikuti Expected tanpa mengasumsikan jalur tertentu.
- Jumlah langkah melewati ~35 (smell): satu topik (validasi Email pada form Login with Password), seluruh TC memakai form yang sama dengan user sendiri dan form dimuat ulang tiap TC, sehingga kegagalan satu TC tidak membuat TC sesudahnya kehilangan makna.
