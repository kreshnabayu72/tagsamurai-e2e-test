---
id: TC-AUTH-LP-E2E-001-screening-login-page-web
title: "Screening Halaman Login with Password (Web)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-01
  - TC-AUTH-LP-02
  - TC-AUTH-LP-03
  - TC-AUTH-LP-04
coverage:
  web: automated
---

# Screening Halaman Login with Password (Web)

## Prerequisites

- Mode: mock. Spec tampilan murni: hanya halaman Login with Password yang dirender, tanpa submit dan tanpa backend nyata. Tidak ada respons API yang dipaksa; API apa pun yang dipanggil halaman saat render di-mock tim FE.
- Tanpa seeding dan tanpa login akun aktor; tidak ada data yang dibuat sehingga tidak ada cleanup.
- Environment variable: `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: penekanan tombol Tab keyboard dengan pembacaan elemen yang fokus; hover kursor pada ikon.
- TC-AUTH-LP-01: Tanpa login (guest); browser web; halaman Login with Password belum pernah diisi pada sesi browser ini
- TC-AUTH-LP-02: Tanpa login (guest); browser web
- TC-AUTH-LP-04: Tanpa login (guest); browser web
- TC-AUTH-LP-03: Tanpa login (guest); browser web
- TC-AUTH-LP-03 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-01: Screening halaman Login with Password (web)

1. Buka halaman Login with Password
2. Susuri halaman dari atas ke bawah tanpa klik apa pun
3. Verifikasi **Header**: Logo TAG Samurai tampil
4. Verifikasi **Header**: Title "Login with Password"
5. Verifikasi **Header**: Subtitle "Sign in and start managing your assets"
6. Verifikasi **Body**: field Email wajib ditandai `*`
7. Verifikasi **Body**: field Email berlabel "Email"
8. Verifikasi **Body**: field Email berplaceholder "Enter your email"
9. Verifikasi **Body**: field Password wajib ditandai `*`
10. Verifikasi **Body**: field Password berlabel "Password"
11. Verifikasi **Body**: field Password berplaceholder "Enter your password"
12. Verifikasi **Body**: field Password memiliki ikon toggle intip
13. Verifikasi **Body**: widget Google reCAPTCHA v2 belum diselesaikan
14. Verifikasi **Body**: Alert pesan server tidak tampil
15. Verifikasi **Footer**: Button [Log in] (solid, primary, lebar penuh) tampil
16. Verifikasi **Footer**: Navigation Links [Log in with OTP] dan "Forgot your password? " [Reset here] tampil
17. Verifikasi **Must NOT**: Checkbox Agreement tidak dirender di form Login
18. Verifikasi **Must NOT**: tombol [Clear Field], [Submit], [Save], dan tombol tutup [✕] tidak ada (anchor: Button [Log in] tampil)

### TC-AUTH-LP-02: State awal form Login with Password (web)

19. Buka ulang halaman Login with Password
20. Amati state awal field, tombol, widget reCAPTCHA, dan slot caption
21. Verifikasi field Email kosong menampilkan placeholder "Enter your email"
22. Verifikasi field Password kosong menampilkan placeholder "Enter your password"
23. Verifikasi field Password dalam mode masked (karakter tersembunyi) sebelum toggle intip diklik
24. Verifikasi Button [Log in] enabled
25. Verifikasi widget reCAPTCHA berstatus Unsolved
26. Verifikasi caption "Please verify that you are not a robot" tidak tampil
27. Verifikasi Alert pesan server tidak tampil
28. Verifikasi tidak ada caption error pada field Email dan field Password

### TC-AUTH-LP-04: Urutan Tab keyboard pada halaman Login with Password (web)

29. Buka ulang halaman Login with Password
30. Klik field Email
31. Verifikasi fokus berada pada field Email
32. Tekan Tab
33. Verifikasi fokus berpindah ke field Password
34. Tekan Tab
35. Verifikasi fokus berpindah ke toggle intip
36. Tekan Tab
37. Verifikasi fokus berpindah ke widget reCAPTCHA
38. Tekan Tab
39. Verifikasi fokus berpindah ke Button [Log in]
40. Tekan Tab
41. Verifikasi fokus berpindah ke link [Log in with OTP]
42. Tekan Tab
43. Verifikasi fokus berpindah ke link [Reset here]

### TC-AUTH-LP-03: Toggle intip pada field Password menampilkan dan menyembunyikan karakter

44. Buka ulang halaman Login with Password
45. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
46. Verifikasi karakter password tersembunyi (masked)
47. Klik ikon toggle intip
48. Verifikasi karakter password terlihat apa adanya sesuai nilai `Spectra.env.LP_PASSWORD`
49. Klik ikon toggle intip sekali lagi
50. Verifikasi karakter password kembali tersembunyi (masked)
51. Arahkan kursor ke ikon toggle intip
52. Verifikasi tidak ada tooltip pada ikon toggle intip

## Notes

- Mode: mock. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di dalam spec berbeda dari urutan TC sumber (01, 02, 04, 03): TC-AUTH-LP-03 mengetik di field Password sehingga ditaruh paling akhir, supaya TC-AUTH-LP-02 (state awal field kosong) dan TC-AUTH-LP-04 tidak terpengaruh isian (prinsip 2 dan 3 konvensi).
- Langkah penghubung (S-03): "Buka ulang halaman Login with Password" pada tiap TC setelah TC pertama untuk mengembalikan form ke state awal (S-09). Tidak ada `Verifikasi` pada langkah tersebut.
- Jumlah langkah (52) melebihi batas tinjau sekitar 35 karena urutan Tab keyboard diasersi per elemen (S-01); seluruh langkah adalah screening tanpa submit sehingga kegagalan satu asersi tidak membuat bagian sesudahnya kehilangan makna.
- Temuan untuk QA: tidak ada.
