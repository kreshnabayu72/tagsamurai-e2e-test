---
id: TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi
title: "Request OTP Ulang Setelah Kuota Resend Habis: Ditolak, Edit Email, Email Berbeda, dan Batas 24 Jam"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-92
  - TC-AUTH-OTP-94
  - TC-AUTH-OTP-96
  - TC-AUTH-OTP-87
coverage:
  web: automated
---

# Request OTP Ulang Setelah Kuota Resend Habis: Ditolak, Edit Email, Email Berbeda, dan Batas 24 Jam

## Prerequisites

- Mode: FE+BE.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser). reCAPTCHA memakai mode uji environment.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Percepatan jam (§6). Langkah "Tunggu countdown 60 detik selesai" dan "Tunggu countdown 10 menit selesai" dipenuhi dengan memajukan jam server uji dan jam browser (countdown UI berjalan di jam klien) bersama sebesar durasi itu, lalu menunggu UI menyegarkan state tombol Resend. Langkah "Tunggu 24 jam 10 menit" dipenuhi dengan memajukan jam server dan jam browser bersama sebesar itu (batas 24 jam sejak kode terakhir dikirim dihitung di server, tetapi countdown "Resend code in (00:59)" pada langkah 34 diamati setelah pergeseran itu dan berjalan di jam klien); menunggu nyata tidak praktis untuk durasi ini. Jam server dan jam browser dipulihkan ke waktu nyata pada langkah 37, sebelum Bagian B, agar pergeseran 24 jam tidak terbawa. Spec ini mengubah state global (jam), sehingga suite berjalan serial (`parallel: false`).
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API, email bersuffix per run) membuat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2):
  - Bagian A (TC-AUTH-OTP-92, 94, 96, satu alur pada satu sesi email-request yang kuotanya habis): `Kartika Cahyono` (`kartikacahyono+{runId}-023@qwertysystem.net`) dan `Budi Setiawan` (`budisetiawan+{runId}-023@qwertysystem.net`).
  - Bagian B (TC-AUTH-OTP-87): `Nadia Safitri` (`nadiasafitri+{runId}-023@qwertysystem.net`).
- Hook `after`: kembalikan jam server dan jam browser uji ke waktu nyata dan hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

#### Bagian A: sesi `Kartika Cahyono` dengan kuota Resend habis

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `kartikacahyono+{runId}-023@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ulangi lima kali (Resend ke-1 sampai ke-5): tunggu countdown 60 detik selesai, lalu klik [Resend code]
6. Verifikasi area Resend menampilkan "Resend code in (09:59)" (kuota habis)
7. Verifikasi area Resend kuota habis dalam keadaan disabled
8. Tunggu countdown 10 menit selesai

### TC-AUTH-OTP-92: Request OTP ulang pada email yang sama setelah kuota resend habis ditolak

9. Klik tautan [Back to Login with Password]
10. Klik tautan [Log in with OTP]
11. Centang widget reCAPTCHA "I'm not a robot"
12. Klik button [Request OTP]
13. Verifikasi Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
14. Verifikasi layar tetap di Request OTP
15. Verifikasi tidak ada email OTP baru di mail-catcher untuk `kartikacahyono+{runId}-023@qwertysystem.net`

### TC-AUTH-OTP-94: Request OTP dengan email berbeda setelah kuota email pertama habis memulai sesi baru

16. Klik tautan [Use password instead]
17. Kosongkan field Email di Login with Password, lalu ketik `budisetiawan+{runId}-023@qwertysystem.net`
18. Klik tautan [Log in with OTP]
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Request OTP]
21. Verifikasi toast sukses: "Success, the code has been sent."
22. Verifikasi halaman Verify OTP tampil untuk `budisetiawan+{runId}-023@qwertysystem.net`
23. Verifikasi area Resend menampilkan "Resend code in (00:59)"
24. Verifikasi area Resend dalam keadaan disabled
25. Verifikasi email OTP diterima di `budisetiawan+{runId}-023@qwertysystem.net`

### TC-AUTH-OTP-96: Request OTP pada email yang sama setelah sesi email-request melewati batas 24 jam diterima sebagai sesi baru

26. Tunggu 24 jam 10 menit sejak Resend ke-5 `Kartika Cahyono` tanpa aktivitas
27. Klik tautan [Back to Login with Password]
28. Kosongkan field Email di Login with Password, lalu ketik `kartikacahyono+{runId}-023@qwertysystem.net`
29. Klik tautan [Log in with OTP]
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Request OTP]
32. Verifikasi Request OTP diterima: toast sukses "Success, the code has been sent."
33. Verifikasi halaman Verify OTP tampil
34. Verifikasi area Resend menampilkan "Resend code in (00:59)"
35. Verifikasi area Resend dalam keadaan disabled
36. Verifikasi tidak ada Alert "Too many requests. Please try again later."
37. Pulihkan jam server dan jam browser ke waktu nyata

#### Bagian B: sesi `Nadia Safitri` dengan kuota Resend habis

### TC-AUTH-OTP-87: Edit email lalu Request OTP dengan email yang sama setelah kuota habis memulai sesi baru

38. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
39. Ketik `nadiasafitri+{runId}-023@qwertysystem.net` pada field Email
40. Centang widget reCAPTCHA "I'm not a robot"
41. Klik button [Request OTP]
42. Ulangi lima kali (Resend ke-1 sampai ke-5): tunggu countdown 60 detik selesai, lalu klik [Resend code]
43. Tunggu countdown 10 menit selesai
44. Klik tautan [Edit email]
45. Biarkan email `nadiasafitri+{runId}-023@qwertysystem.net` tidak berubah dan centang widget reCAPTCHA "I'm not a robot"
46. Klik button [Request OTP]
47. Verifikasi Request OTP diterima walau kuota resend sesi sebelumnya sudah 5
48. Verifikasi tidak ada Alert "Too many requests. Please try again later."
49. Verifikasi toast sukses: "Success, the code has been sent."
50. Verifikasi halaman Verify OTP tampil
51. Verifikasi area Resend menampilkan "Resend code in (00:59)"
52. Verifikasi area Resend dalam keadaan disabled
53. Tunggu countdown 60 detik selesai
54. Klik [Resend code]
55. Verifikasi toast sukses: "Success, the code has been sent."
56. Verifikasi area Resend menampilkan "Resend code in (00:59)" (bukan State C maupun Exhausted)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Pengecualian P-3 (user berurutan) dan P-1 (state berat dibangun langkah sebelumnya) dari `docs/e2e-conventions.md` §3: TC-92, 94, 96 di sumber memakai tiga user berbeda (`Ayu Maulana`, `Kartika Cahyono`, `Andi Safitri`) masing-masing dengan 5 Resend dan tunggu 10 menit. Bagian A memakai satu user (`Kartika Cahyono`) dengan urutan 92, 94, 96: TC-92 dan TC-94 tidak mengubah sesi `Kartika Cahyono` (TC-94 memulai sesi untuk email berbeda), sehingga sesi yang kuotanya habis tetap dipakai TC-96. TC-87 dipisah sebagai Bagian B dengan user sendiri karena Edit email mengakhiri sesi yang kuotanya habis; bila ditaruh di Bagian A, TC-96 tidak lagi memiliki sesi yang habis. Spec melewati batas ±35 langkah (56 langkah) karena dua kali membangun state kuota habis; kedua bagian independen, jadi kegagalan Bagian A tidak membuat Bagian B tidak bermakna.
- Langkah 37 (memulihkan jam) adalah langkah penghubung tanpa Verifikasi (S-09).
- Langkah penghubung (S-03): langkah 6 dan 7 (menegaskan state kuota habis sebelum tunggu 10 menit, dari Expected TC-80), langkah 16 (memakai [Use password instead] di halaman Request OTP untuk menuju Login with Password karena pada urutan gabungan layar sebelumnya adalah Request OTP, bukan Verify OTP), langkah 27 (kembali ke Login with Password). Langkah 17 menulis "Kosongkan field Email ..., lalu ketik" karena field Email sudah berisi email sebelumnya; TC hanya menulis "Ketik".
- Urutan di sumber (92, 87, 94, 96) berubah menjadi 92, 94, 96, lalu 87 di Bagian B, sesuai alasan pada catatan pertama.
- Tidak ada asersi pencatatan log pada spec ini; penolakan Request OTP karena cooldown atau kuota tidak dicatat dan diasersi di spec absence E2E-040.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - Langkah 28 (mengosongkan field Email di Login with Password lalu mengetik ulang email `Kartika Cahyono`) tidak ada di TC-96, padahal field Email membawa email `Budi Setiawan` dari TC-94; spec menambahnya supaya Request OTP berikutnya memakai email yang benar. Mohon QA menambah langkah itu di TC-96 atau mengonfirmasi perilaku field Email. Penulisan "Kosongkan ..., lalu ketik" pada langkah 28 mengikuti hal yang sama.
  - TC-96 langkah 16 ("Tunggu 24 jam 10 menit sejak Resend ke-5") ambigu pada titik awal: NC-11 menetapkan TTL 24 jam sejak pengiriman kode terakhir, sedangkan TC mengukur dari Resend ke-5 (yang juga pengiriman kode terakhir). Spec mengikuti TC.
  - TC-87 Post Condition ("jumlah resend 1 setelah Resend tersebut") tidak punya butir Expected terpisah; langkah 54 hanya mengasersi tampilan State A, bukan hitungan resend sesi.
  - Urutan 92, 94, 96 pada satu user `Kartika Cahyono` mengandalkan asumsi bahwa TC-94 (Request OTP untuk email lain, `Budi Setiawan`) tidak mengakhiri sesi email-request `Kartika Cahyono` yang kuotanya habis; TC tidak menyatakannya. Bila asumsi itu salah, TC-96 tidak lagi menguji batas 24 jam pada sesi kuota-habis. Spec mempertahankan perilaku TC (peleburan user sesuai P-3) dan tidak memisahkan TC-96 ke user sendiri; QA mohon konfirmasi atau tambahkan pernyataan di TC.
  - TC-94 dan TC-96 Post Condition a (sesi email-request baru dimulai dengan jumlah resend 0) tidak punya langkah observasi di TC; spec tidak mengasersinya, dan hanya mengasersi State A "Resend code in (00:59)" (langkah 23 dan 34). Mohon QA menambah langkah observasi bila jumlah resend 0 perlu dibuktikan.
  - TC-94 langkah 17 mengetik email kedua di Login with Password tanpa menyebut email pertama yang terbawa harus diganti; spec menulis "Kosongkan field Email ..., lalu ketik" pada langkah 17 supaya email pertama tidak terbawa; TC hanya menulis "Ketik".
