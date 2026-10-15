---
id: TC-AUTH-RST-E2E-039-defense-confirm-resend-endpoint
title: "Defense-in-Depth Confirm dan Resend: Request Langsung ke Endpoint"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-122
  - TC-AUTH-RST-123
  - TC-AUTH-RST-124
  - TC-AUTH-RST-126
  - TC-AUTH-RST-127
  - TC-AUTH-RST-125
  - TC-AUTH-RST-152
  - TC-AUTH-RST-156
coverage:
  web: automated
---

# Defense-in-Depth Confirm dan Resend: Request Langsung ke Endpoint

## Prerequisites

- Mode: FE+BE (kelas a: defense-in-depth; request langsung ke endpoint tanpa melalui UI).
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan password aktif `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE), kecuali dinyatakan lain (Dian Pratama berstatus Pending Activation; Linda Sari memiliki email baru pending konfirmasi). User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT`, `RST_PASSWORD_REPLAY`.
- Kemampuan teknis: klien API untuk mengirim request langsung ke POST /v2/iam/auth/reset-password/confirm dan POST /v2/iam/auth/reset-password/resend; fixture BE untuk user Pending Activation (Dian Pratama) dan email baru pending konfirmasi (Linda Sari); mail-catcher; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session dan User Log); pembekuan jam server selama bagian TC-AUTH-RST-125.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server (dibekukan pada bagian TC-AUTH-RST-125 supaya Resend langsung tetap berada di dalam cooldown 60 detik). Suite berjalan serial (`parallel: false`). Pemulihan: pembekuan jam dilepas di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-122 sampai 127, 152, 156: User belum login (guest); browser web.
- TC-AUTH-RST-122, 123, 124: User `Budi Santoso` (`budisantoso+{runId}-039a@qwertysystem.net`) Active dengan token reset aktif (tautan di mail-catcher). Data 122: Password dan confirmPassword `abc`. Data 123: Password dan confirmPassword `Spectra.env.RST_PASSWORD`. Data 124: Password `Spectra.env.RST_PASSWORD_NEW` dengan confirmPassword kosong, lalu confirmPassword `Spectra.env.RST_PASSWORD_ALT`.
- TC-AUTH-RST-126: token acak `tokentidakpernahada` dengan Password dan confirmPassword `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-127: User `Citra Dewi` (`citradewi+{runId}-039b@qwertysystem.net`) Active; Submit New Password sukses dengan token A dan password `Spectra.env.RST_PASSWORD_NEW` sudah dilakukan di hook `before` lewat API (setara TC-AUTH-RST-82); Password replay `Spectra.env.RST_PASSWORD_REPLAY`.
- TC-AUTH-RST-125: User `Dewi Lestari` (`dewilestari+{runId}-039c@qwertysystem.net`) Active tanpa Request sebelumnya; Request pertama dilakukan lewat UI di langkah spec dengan jam server dibekukan.
- TC-AUTH-RST-152: User `Dian Pratama` (`dianpratama+{runId}-039d@qwertysystem.net`) berstatus Pending Activation; counter per email di bawah batas.
- TC-AUTH-RST-156: User `Linda Sari` (`lindasari+{runId}-039e@qwertysystem.net`) Activated dengan email baru `lindasari.baru+{runId}-039e@qwertysystem.net` pending konfirmasi.

## Test Steps

### Persiapan konteks

1. Buka jendela privat admin; login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"
2. Buka jendela privat guest (tanpa sesi login)

### TC-AUTH-RST-122: Server menegakkan Password Policy walau validasi UI dilewati

3. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah baris dan entri teratas sebagai baseline B1
4. Pindah ke jendela guest, kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token milik `budisantoso+{runId}-039a@qwertysystem.net`, password "abc", dan confirmPassword "abc"
5. Verifikasi server menolak request
6. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password")
7. Verifikasi jumlah baris bertambah tepat satu dibanding baseline B1
8. Verifikasi entri baru: Activity `Reset Password`, Status Failed, Note `Password does not meet requirements`

### TC-AUTH-RST-123: Server menegakkan larangan password sama dengan password lama

9. Pindah ke jendela guest, kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token yang sama, password `Spectra.env.RST_PASSWORD`, dan confirmPassword `Spectra.env.RST_PASSWORD`
10. Verifikasi server menolak request
11. Buka tautan reset milik `budisantoso+{runId}-039a@qwertysystem.net` dari mail-catcher di jendela guest
12. Verifikasi Setup New Password tampil (token tidak dikonsumsi)

### TC-AUTH-RST-124: Server menolak Confirm Password kosong atau berbeda walau UI dilewati

13. Kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token yang sama, password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword kosong
14. Verifikasi request ditolak
15. Kirim request langsung dengan token yang sama, password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword `Spectra.env.RST_PASSWORD_ALT`
16. Verifikasi request ditolak
17. Buka halaman Login with Password lalu login dengan Email `budisantoso+{runId}-039a@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD` (selesaikan reCAPTCHA)
18. Verifikasi login berhasil (password tidak berubah oleh request yang ditolak)
19. Tutup jendela guest lalu buka jendela privat guest baru (tanpa sesi login)

### TC-AUTH-RST-126: Submit dengan token tidak dikenal ditolak tanpa mengubah password

20. Kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token acak "tokentidakpernahada", password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword `Spectra.env.RST_PASSWORD_NEW`
21. Verifikasi request ditolak
22. Buka halaman Setup New Password dengan token "tokentidakpernahada" di jendela guest
23. Verifikasi UI yang setara menampilkan Halaman 404 varian Expired
24. Buka halaman Login with Password lalu login dengan Email `budisantoso+{runId}-039a@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW`
25. Verifikasi login ditolak (password user tidak berubah)

### TC-AUTH-RST-127: Token yang sudah dipakai tidak dapat dipakai ulang oleh siapa pun

26. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah baris dan entri teratas sebagai baseline B2
27. Pindah ke jendela guest, kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token A milik `citradewi+{runId}-039b@qwertysystem.net` (sudah consumed) dan password `Spectra.env.RST_PASSWORD_REPLAY`
28. Verifikasi request ditolak
29. Buka tautan token A di jendela guest
30. Verifikasi UI yang setara menampilkan Halaman 404 varian Already Used
31. Buka halaman Login with Password lalu login dengan Email `citradewi+{runId}-039b@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_REPLAY` (selesaikan reCAPTCHA)
32. Verifikasi login dengan `Spectra.env.RST_PASSWORD_REPLAY` ditolak
33. Login dengan Email `citradewi+{runId}-039b@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW`
34. Verifikasi login berhasil
35. Tutup jendela guest lalu buka jendela privat guest baru (tanpa sesi login)
36. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
37. Verifikasi ada entri baru di atas baseline B2: Status Failed, Note `Reset link already used`

### TC-AUTH-RST-125: Server menegakkan cooldown 60 detik untuk Resend walau UI dilewati

38. Bekukan jam server
39. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `dewilestari+{runId}-039c@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
40. Periksa mail-catcher, simpan tautan dari Request pertama, dan catat jumlah email untuk `dewilestari+{runId}-039c@qwertysystem.net` sebagai baseline M1
41. Kirim request langsung ke POST /v2/iam/auth/reset-password/resend untuk `dewilestari+{runId}-039c@qwertysystem.net` (jam server masih dibekukan, di dalam cooldown 60 detik setelah Request pertama)
42. Periksa mail-catcher
43. Verifikasi tidak ada email baru di mail-catcher: jumlah email sama dengan baseline M1
44. Buka tautan dari Request pertama di jendela guest
45. Verifikasi tautan dari Request pertama masih membuka Setup New Password
46. Lepaskan pembekuan jam server

### TC-AUTH-RST-152: Resend untuk akun Pending Activation

47. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Dian Pratama", lalu catat jumlah baris dan entri teratas kedua surface sebagai baseline B3
48. Periksa mail-catcher lalu catat jumlah email untuk `dianpratama+{runId}-039d@qwertysystem.net` sebagai baseline M2
49. Picu Resend langsung ke endpoint untuk `dianpratama+{runId}-039d@qwertysystem.net` dengan counter per email di bawah batas
50. Verifikasi respons Resend sukses seperti Resend yang diproses
51. Periksa mail-catcher
52. Verifikasi tidak ada email reset baru di mail-catcher: jumlah email sama dengan baseline M2
53. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), dan muat ulang User Log user "Dian Pratama"
54. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B3
55. Verifikasi entri baru pada kedua surface: Status Failed, Note `Account is not activated`

### TC-AUTH-RST-156: Resend untuk email pending

56. Periksa mail-catcher lalu catat jumlah email untuk `lindasari.baru+{runId}-039e@qwertysystem.net` sebagai baseline M3
57. Picu Resend langsung ke endpoint untuk `lindasari.baru+{runId}-039e@qwertysystem.net`
58. Verifikasi respons Resend sukses seperti Resend yang diproses
59. Periksa mail-catcher
60. Verifikasi tidak ada email di mail-catcher untuk alamat itu: jumlah email sama dengan baseline M3

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Status HTTP penolakan tidak disebut TC sehingga tidak diasersi (S-13).
- TC-AUTH-RST-122, 123, 124 memakai satu token yang tetap active (Post Condition). Token tetap active dibuktikan langsung di langkah 11 dan 12 (Setup New Password masih tampil setelah ditolak), karena Expected TC-AUTH-RST-123 menyebut token tidak dikonsumsi; login password lama (langkah 17 dan 18) hanya membuktikan password tidak berubah, bukan status token.
- Klausa "password tidak berubah" pada Expected TC-AUTH-RST-122 (langkah 5) dan TC-AUTH-RST-123 (langkah 10) dibuktikan secara kolektif oleh login dengan password lama pada langkah 17 dan 18, karena kedua request ditolak sebelum login itu dan tidak ada perubahan password lain pada user yang sama sebelum langkah 17.
- Temuan untuk QA: Post Condition counter 24 jam tidak berubah (TC-AUTH-RST-125) dan tidak ada token reset dibuat (TC-AUTH-RST-152, TC-AUTH-RST-156) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Asersi "tidak ada entri log baru" pada TC-AUTH-RST-124, 125, 126, 156 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g), yang memicu aksi nyata yang sama dengan baseline log sendiri; id TC tetap milik spec ini di `sourceTc` (S-05).
- TC-AUTH-RST-127 butir c memuat entri log Failed `Reset link already used`; pencatatan jenis yang sama diuji juga di `TC-AUTH-RST-E2E-042-log-token-states`. Langkah 37 tidak menyatakan "tepat satu" karena membuka tautan token A (langkah 29) juga dapat tercatat.
- TC-AUTH-RST-152 dan 156 dipicu langsung ke endpoint karena halaman Email Sent! tidak dapat dicapai lewat Request untuk akun Pending Activation atau email pending (alasan di TC sumber).
- Langkah penghubung (S-03): langkah 1 dan 2 (persiapan jendela), pindah jendela admin atau guest, langkah 19 dan 35 (jendela guest baru agar sesi login dari langkah 18 dan 34 tidak terbawa; user bersesi aktif dialihkan ke Portal sesuai TC-AUTH-RST-10), serta langkah 38 dan 46 (membekukan dan melepas jam server).
- Asersi tambahan di luar Expected TC (S-03): langkah 18 (login berhasil), langkah 25 dan 32 sampai 34 (login sebagai cara observasi password), langkah 22 dan 23 (UI setara, dari Expected a TC-AUTH-RST-126), serta baseline B1 sampai B3 dan M1 sampai M3 untuk membuktikan "baru" (S-12). Langkah 11 dan 12 menambah observasi token untuk Expected TC-AUTH-RST-123.
- Langkah 39 menyalin aksi Request dari TC-AUTH-RST-12 (S-04) karena TC-AUTH-RST-125 menuntut Resend langsung di dalam 60 detik sejak Request pertama.
- Urutan TC dalam spec (122, 123, 124, 126, 127, 125, 152, 156) berbeda dari urutan di TC sumber; TC-AUTH-RST-125 dipindah sesudah 127 karena memakai jam server beku dan Request tersendiri, jadi dipisah dari kelompok Confirm (S-05).
- Jumlah langkah 60 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (24 dari 60 langkah adalah Verifikasi; 36 sisanya aksi: request langsung ke endpoint, login sebagai cara observasi password, langkah penghubung, baseline). Satu topik (defense-in-depth endpoint Confirm dan Resend). Satu kelas harness (a, request langsung ke endpoint); tiap kelompok TC memakai user dan token sendiri sehingga tidak saling bergantung. Dapat dipecah menjadi Confirm (TC-AUTH-RST-122, 123, 124, 126, 127) dan Resend (TC-AUTH-RST-125, 152, 156) bila tim FE menginginkan.
