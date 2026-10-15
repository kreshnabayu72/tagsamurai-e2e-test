---
id: TC-AUTH-RST-E2E-036-resilience-intercept
title: "Ketahanan Request, Resend, Validate Link, dan Submit terhadap 5xx dan Timeout (Intercept)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-87
  - TC-AUTH-RST-88
  - TC-AUTH-RST-50
  - TC-AUTH-RST-62
  - TC-AUTH-RST-90
  - TC-AUTH-RST-91
coverage:
  web: automated
---

# Ketahanan Request, Resend, Validate Link, dan Submit terhadap 5xx dan Timeout (Intercept)

## Prerequisites

- Mode: FE+BE dengan `Spectra.intercept` parsial di atas backend nyata (kelas b). Kegagalan dipaksa di browser pada respons endpoint; endpoint lain tetap ke backend nyata.
- Seeding: enam user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`. Untuk TC-AUTH-RST-62, 90, dan 91, satu token reset aktif per user diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: `Spectra.intercept` untuk memaksa respons 5xx dan menahan respons sampai timeout klien pada endpoint Request (POST /v2/iam/auth/reset-password/request), Resend (POST /v2/iam/auth/reset-password/resend), Confirm (POST /v2/iam/auth/reset-password/confirm), dan endpoint validasi tautan; melepas intercept di tengah langkah; mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela privat tanpa sesi login; pengaturan jam server dan jam browser bersama (cooldown ditegakkan di server, countdown [Resend email] berjalan di jam klien).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- Jeda nyata: langkah "Tunggu sampai timeout klien tercapai" (langkah 15 dan 54) menunggu timeout klien aplikasi; lama timeout klien ditetapkan tim FE pada environment automation dan tidak lebih dari ±30 detik.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: kedua jam dipulihkan dan semua intercept dilepas di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-87, 88, 50, 62, 90, 91: User belum login (guest); browser web.
- TC-AUTH-RST-87: User `Budi Santoso` (`budisantoso+{runId}-036a@qwertysystem.net`) Active.
- TC-AUTH-RST-88: User `Citra Dewi` (`citradewi+{runId}-036b@qwertysystem.net`) Active.
- TC-AUTH-RST-50: User `Dewi Lestari` (`dewilestari+{runId}-036c@qwertysystem.net`) Active; Request pertama dilakukan lewat UI di langkah spec dan cooldown dilewati dengan memajukan jam.
- TC-AUTH-RST-62: User `Eko Santoso` (`ekosantoso+{runId}-036d@qwertysystem.net`) dengan token aktif.
- TC-AUTH-RST-90: User `Fani Wulandari` (`faniwulandari+{runId}-036e@qwertysystem.net`) dengan token aktif; Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-91: User `Gita Pratama` (`gitapratama+{runId}-036f@qwertysystem.net`) dengan token aktif; Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-87: Request gagal 5xx mempertahankan form dan menampilkan toast error

1. Paksa endpoint Request mengembalikan 5xx (intercept)
2. Buka jendela privat baru lalu buka halaman Reset Password (Request)
3. Ketik `budisantoso+{runId}-036a@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
4. Amati halaman dan Button [Reset Password]
5. Verifikasi toast error muncul "Error, failed to send reset link."
6. Verifikasi toast error tetap tampil sampai ditutup manual
7. Verifikasi browser tetap di halaman Reset Password
8. Verifikasi field Email tetap berisi `budisantoso+{runId}-036a@qwertysystem.net`
9. Verifikasi Button [Reset Password] kembali enabled
10. Lepas intercept lalu klik Button [Reset Password] lagi
11. Verifikasi browser menuju halaman Email Sent!

### TC-AUTH-RST-88: Request timeout menampilkan toast koneksi dan form dapat dikirim ulang

12. Tahan respons endpoint Request sampai timeout klien (intercept)
13. Buka halaman Reset Password (Request) di jendela privat baru
14. Ketik `citradewi+{runId}-036b@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
15. Tunggu sampai timeout klien tercapai
16. Verifikasi toast error muncul: "Connection problem. Please try again."
17. Verifikasi browser tetap di halaman Reset Password
18. Verifikasi input Email dipertahankan
19. Verifikasi Button [Reset Password] kembali enabled

### TC-AUTH-RST-50: Resend gagal 5xx mempertahankan halaman dan token

20. Lepas semua intercept lalu buka halaman Reset Password (Request) di jendela privat baru
21. Ketik `dewilestari+{runId}-036c@qwertysystem.net` pada field Email, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
22. Catat jumlah email di mail-catcher untuk `dewilestari+{runId}-036c@qwertysystem.net` sebagai baseline M1 (sudah memuat email dari Request)
23. Majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
24. Paksa endpoint Resend mengembalikan 5xx (intercept) lalu klik [Resend email]
25. Verifikasi toast error muncul: "Error, failed to send email to dewilestari+{runId}-036c@qwertysystem.net."
26. Verifikasi toast error tetap tampil sampai ditutup manual
27. Verifikasi halaman tetap Email Sent!
28. Verifikasi [Resend email] tetap tersedia untuk dicoba ulang
29. Periksa mail-catcher
30. Verifikasi tidak ada email baru: jumlah email sama dengan baseline M1

### TC-AUTH-RST-62: Validasi tautan gagal 5xx menampilkan ErrorState, bukan Halaman 404

31. Lepas intercept Resend lalu paksa endpoint validasi tautan mengembalikan 5xx (intercept)
32. Buka tautan reset milik `ekosantoso+{runId}-036d@qwertysystem.net` dari mail-catcher
33. Amati halaman
34. Verifikasi ErrorState varian With Retry tampil
35. Verifikasi ErrorState menampilkan teks "Unable to load this data."
36. Verifikasi ErrorState menampilkan Button [Try Again]
37. Verifikasi Halaman 404 tidak tampil
38. Lepas intercept lalu klik [Try Again]
39. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for ekosantoso+{runId}-036d@qwertysystem.net."

### TC-AUTH-RST-90: Submit gagal 5xx mempertahankan form dan token

40. Buka tautan reset milik `faniwulandari+{runId}-036e@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
41. Paksa endpoint Confirm mengembalikan 5xx (intercept)
42. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
43. Verifikasi toast error muncul "Error, failed to reset password."
44. Verifikasi toast error tetap tampil sampai ditutup manual
45. Verifikasi form tetap terbuka
46. Verifikasi input dipertahankan
47. Verifikasi Button [Reset Password] kembali enabled
48. Verifikasi Halaman 404 tidak tampil
49. Lepas intercept lalu klik Button [Reset Password] lagi
50. Verifikasi browser menuju halaman Password Reset Successful

### TC-AUTH-RST-91: Submit timeout menampilkan toast koneksi dan token tidak dikonsumsi

51. Buka tautan reset milik `gitapratama+{runId}-036f@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
52. Tahan respons endpoint Confirm sampai timeout klien (intercept)
53. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
54. Tunggu sampai timeout klien tercapai
55. Verifikasi toast error muncul: "Connection problem. Please try again."
56. Verifikasi form tetap terbuka
57. Verifikasi input dipertahankan
58. Verifikasi Button [Reset Password] kembali enabled
59. Lepas intercept Confirm

## Notes

- Mode: FE+BE dengan intercept (konvensi bagian 6): TC sumber mengasersi state backend (token tidak dibuat atau tetap active) sehingga tidak murni mock. Kebutuhan intercept ditulis di Prerequisites.
- Temuan untuk QA: TC-AUTH-RST-87 menulis hasil percobaan ulang sebagai "Setelah langkah 5" padahal klik ulang ada di langkah 6 (S-15). Spec mengikuti urutan aksi sebenarnya.
- Temuan untuk QA: Post Condition tanpa langkah observasi di TC tidak diasersi: tautan lama masih membuka Setup New Password (TC-AUTH-RST-50), token tidak dikonsumsi (TC-AUTH-RST-91), token tidak dibuat pada percobaan 5xx (TC-AUTH-RST-87), serta password dan lock akun tidak berubah pada percobaan 5xx (TC-AUTH-RST-90) (S-01, S-15).
- Endpoint validasi tautan tidak disebut path-nya di TC sumber; spec menyebutnya generik (S-13).
- Token yang tetap active pada TC-AUTH-RST-62 dan 90 hanya terbukti tidak langsung lewat percobaan ulang yang berhasil; ini bukan asersi tambahan.
- Urutan TC dalam spec (87, 88, 50, 62, 90, 91) berbeda dari urutan di TC sumber; alasannya pengelompokan per endpoint (Request, Resend, Validate Link, Submit) agar tiap intercept dipasang lalu dilepas sebelum endpoint berikutnya (S-05, S-09).
- Langkah penghubung (S-03): membuka jendela privat baru, melepas intercept antar-TC (langkah 10, 20, 31, 38, 49), dan langkah 59 yang melepas intercept Confirm di akhir spec; hook `after` melepas semua intercept sebagai cadangan. Langkah 23 memajukan jam menggantikan menunggu 61 detik (konvensi bagian 6).
- Jumlah langkah 59 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (31 dari 59 langkah adalah Verifikasi; 28 sisanya aksi, pemasangan atau pelepasan intercept, dan langkah penghubung). Satu topik (resilience tiap endpoint), tanpa prefix login berulang (tidak ada login). Satu kelas harness (b, intercept) dan tiap TC memakai user dan token sendiri, sehingga kegagalan keras satu TC tidak menggugurkan TC sesudahnya; dipertahankan satu spec per prinsip 3.13 (kelas ringan satu spec per kelas per modul).
