---
id: TC-AUTH-OTP-E2E-047-tidak-dicatat-absence-penolakan-navigasi-dan-kegagalan
title: "Tidak Ada Pencatatan di Surface Log untuk Navigasi, Edit Email, Penolakan Cooldown, Akun Terhapus, Kegagalan Server, dan Resend"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-35
  - TC-AUTH-OTP-36
  - TC-AUTH-OTP-86
  - TC-AUTH-OTP-30
  - TC-AUTH-OTP-90
  - TC-AUTH-OTP-140
  - TC-AUTH-OTP-62
  - TC-AUTH-OTP-157
  - TC-AUTH-OTP-31
  - TC-AUTH-OTP-32
  - TC-AUTH-OTP-78
  - TC-AUTH-OTP-68
coverage:
  web: automated
---

# Tidak Ada Pencatatan di Surface Log untuk Navigasi, Edit Email, Penolakan Cooldown, Akun Terhapus, Kegagalan Server, dan Resend

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`. Akun ini juga dipakai langkah uji untuk menghapus user (TC-AUTH-OTP-140 dan TC-AUTH-OTP-62).
- Password user uji dari `Spectra.env.OTP_PASSWORD` (dipakai saat seeding user lewat API dan login password TC-AUTH-OTP-68). Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji; `Spectra.intercept()` untuk memaksa respons Request OTP server error 500 (TC-AUTH-OTP-31; intercept parsial di atas backend nyata); kemampuan memutus koneksi internet pada browser uji (mode offline) untuk TC-AUTH-OTP-32; percepatan jam server untuk melewati countdown Resend 60 detik pada TC-AUTH-OTP-78 (jam dipulihkan di hook `after`).
- Jam yang diatur (konvensi bagian 6): jam server dan jam browser (klien) dimajukan bersama, karena countdown Resend di UI berjalan di jam klien sehingga memajukan jam server saja tidak mengaktifkan [Resend code]. Hook `after` memulihkan kedua jam. Suite berjalan serial (`parallel: false`) karena jam server digeser.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-047`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian; user `Hendra Ramadhan` dan `Maya Purnama` yang dihapus langkah uji dilewati saat cleanup). Hook `before` juga mencatat baris teratas `Global Settings > Activity Log > Session` dan jumlah baris `Global Settings > User > Detail > User Log` tiap user sebagai baseline "tidak ada entri baru". Semua user profil BASE (Tabel Data Uji Pre-setup #2: Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada):
  - TC-AUTH-OTP-35: `Galih Tanjung` (`galihtanjung+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-36: `Citra Rahmawati` (`citrarahmawati+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-86: `Surya Utami` (`suryautami+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-30: `Eko Setiawan` (`ekosetiawan+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-90: `Sinta Nugroho` (`sintanugroho+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-140: `Hendra Ramadhan` (`hendraramadhan+{runId}-047@qwertysystem.net`), dihapus oleh langkah uji
  - TC-AUTH-OTP-62: `Maya Purnama` (`mayapurnama+{runId}-047@qwertysystem.net`), dihapus oleh langkah uji
  - TC-AUTH-OTP-31: `Ratna Utami` (`ratnautami+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-32: `Taufik Safitri` (`taufiksafitri+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-78: `Galih Suryani` (`galihsuryani+{runId}-047@qwertysystem.net`)
  - TC-AUTH-OTP-68: `Yoga Wibowo` (`yogawibowo+{runId}-047@qwertysystem.net`), password `Spectra.env.OTP_PASSWORD`
- TC-AUTH-OTP-157 memakai input uji `<script>alert(1)</script>@qwertysystem.net` (literal, submit-nya ditolak dan tidak ada data tercipta); tidak ada user untuk TC ini.

## Test Steps

### Bagian A: Navigasi dan Edit email tidak menulis log (TC-AUTH-OTP-35, 36, 86)

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. TC-AUTH-OTP-35: ketik `galihtanjung+{runId}-047@qwertysystem.net` pada field Email, klik tautan [Use password instead]
3. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
4. TC-AUTH-OTP-36: ketik `citrarahmawati+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
5. Pada halaman Verify OTP klik tautan [Back to Login with Password]
6. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
7. TC-AUTH-OTP-86: ketik `suryautami+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
8. Klik tautan [Edit email]
9. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan buka `Global Settings > User > Detail > User Log` untuk `Galih Tanjung`, `Citra Rahmawati`, dan `Surya Utami`
10. Verifikasi TC-AUTH-OTP-35: tidak ada entri log baru untuk klik [Use password instead] di `Global Settings > Activity Log > Session`
11. Verifikasi TC-AUTH-OTP-35: tidak ada entri log baru untuk klik [Use password instead] di `Global Settings > User > Detail > User Log` `Galih Tanjung`
12. Verifikasi TC-AUTH-OTP-36: tidak ada entri log untuk navigasi [Back to Login with Password] di `Global Settings > Activity Log > Session`
13. Verifikasi TC-AUTH-OTP-36: tidak ada entri log untuk navigasi [Back to Login with Password] di `Global Settings > User > Detail > User Log` `Citra Rahmawati`
14. Verifikasi TC-AUTH-OTP-86: tidak ada entri log baru untuk klik [Edit email] di `Global Settings > Activity Log > Session`
15. Verifikasi TC-AUTH-OTP-86: tidak ada entri log baru untuk klik [Edit email] di `Global Settings > User > Detail > User Log` `Surya Utami`

### Bagian B: Klik ganda, cooldown, akun terhapus, dan payload script tidak menulis log (TC-AUTH-OTP-30, 90, 140, 62, 157)

16. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
17. TC-AUTH-OTP-30: ketik `ekosetiawan+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA
18. Klik button [Request OTP] dua kali berturut-turut dalam waktu kurang dari 1 detik
19. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
20. TC-AUTH-OTP-90: ketik `sintanugroho+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
21. Klik tautan [Back to Login with Password]
22. Klik tautan [Log in with OTP]
23. Centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP] (ditolak karena cooldown 60 detik masih berjalan)
24. TC-AUTH-OTP-140: ganti konteks ke browser admin, buka `Global Settings > User`, hapus user `Hendra Ramadhan`
25. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
26. Ketik `hendraramadhan+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
27. TC-AUTH-OTP-62: buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
28. Ketik `mayapurnama+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
29. Ganti konteks ke browser admin, buka `Global Settings > User`, hapus user `Maya Purnama`
30. Ganti konteks ke jendela privat TC-AUTH-OTP-62, ketik 6 digit kode OTP dari email pada kotak digit
31. TC-AUTH-OTP-157: buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
32. Ketik `<script>alert(1)</script>@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
33. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan buka `Global Settings > User > Detail > User Log` untuk `Eko Setiawan` dan `Sinta Nugroho`
34. Verifikasi TC-AUTH-OTP-30: tidak ada entri log ganda untuk klik ganda [Request OTP] di `Global Settings > Activity Log > Session`
35. Verifikasi TC-AUTH-OTP-30: tidak ada entri log ganda untuk klik ganda [Request OTP] di `Global Settings > User > Detail > User Log` `Eko Setiawan`
36. Verifikasi TC-AUTH-OTP-90: tidak ada entri log untuk penolakan Request OTP karena cooldown di `Global Settings > Activity Log > Session`
37. Verifikasi TC-AUTH-OTP-90: tidak ada entri log untuk penolakan Request OTP karena cooldown di `Global Settings > User > Detail > User Log` `Sinta Nugroho`
38. Verifikasi TC-AUTH-OTP-140: tidak ada entri log baru untuk Request OTP akun yang sudah dihapus di `Global Settings > Activity Log > Session`
39. Verifikasi TC-AUTH-OTP-62: tidak ada entri log untuk Verify OTP akun yang sudah dihapus di `Global Settings > Activity Log > Session` karena tidak ada subjek user
40. Verifikasi TC-AUTH-OTP-157: tidak ada entri log baru untuk payload script pada field Email di `Global Settings > Activity Log > Session`

### Bagian C: Kegagalan server pada Request OTP dan Resend yang berhasil tidak menulis log (TC-AUTH-OTP-31, 32, 78)

41. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
42. TC-AUTH-OTP-31: ketik `ratnautami+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA
43. Atur intercept respons Request OTP menjadi server error 500
44. Klik button [Request OTP]
45. Hapus intercept respons Request OTP
46. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
47. TC-AUTH-OTP-32: ketik `taufiksafitri+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA
48. Putuskan koneksi internet pada browser uji
49. Klik button [Request OTP]
50. Tunggu sampai request timeout
51. Pulihkan koneksi internet pada browser uji
52. TC-AUTH-OTP-78: buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
53. Ketik `galihsuryani+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
54. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
55. Klik [Resend code]
56. Pulihkan jam server dan jam browser ke waktu nyata
57. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan buka `Global Settings > User > Detail > User Log` untuk `Ratna Utami`, `Taufik Safitri`, dan `Galih Suryani`
58. Verifikasi TC-AUTH-OTP-31: tidak ada entri log baru untuk Request OTP yang gagal karena server error 5xx di `Global Settings > Activity Log > Session`
59. Verifikasi TC-AUTH-OTP-31: tidak ada entri log baru untuk Request OTP yang gagal karena server error 5xx di `Global Settings > User > Detail > User Log` `Ratna Utami`
60. Verifikasi TC-AUTH-OTP-32: tidak ada entri log baru untuk Request OTP yang gagal karena timeout di `Global Settings > Activity Log > Session`
61. Verifikasi TC-AUTH-OTP-32: tidak ada entri log baru untuk Request OTP yang gagal karena timeout di `Global Settings > User > Detail > User Log` `Taufik Safitri`
62. Verifikasi TC-AUTH-OTP-78: tidak ada entri log baru untuk Resend yang berhasil di `Global Settings > Activity Log > Session`
63. Verifikasi TC-AUTH-OTP-78: tidak ada entri log baru untuk Resend yang berhasil di `Global Settings > User > Detail > User Log` `Galih Suryani`

### Bagian D: Kegagalan OTP tidak menulis entri lock Login with Password (TC-AUTH-OTP-68)

64. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
65. TC-AUTH-OTP-68: ketik `yogawibowo+{runId}-047@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
66. Ketik 5 kali 6 digit kode salah `000000` berturut-turut pada kotak digit
67. Klik tautan [Back to Login with Password]
68. Login dengan email `yogawibowo+{runId}-047@qwertysystem.net` dan password `Spectra.env.OTP_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
69. Verifikasi TC-AUTH-OTP-68 Post Condition a: lock progression password `Yoga Wibowo` tetap pada nilai awal, diamati dari login password yang berhasil pada percobaan pertama tanpa caption akun terkunci
70. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan buka `Global Settings > User > Detail > User Log` untuk `Yoga Wibowo`
71. Verifikasi TC-AUTH-OTP-68 Expected c dan Post Condition b: tidak ada entri baru `Locked 15 minutes`, `Locked 1 hour`, `Locked requires reset`, atau `Account locked` dibanding baseline hook pada log `Yoga Wibowo` di `Global Settings > Activity Log > Session`
72. Verifikasi TC-AUTH-OTP-68 Expected c dan Post Condition b: tidak ada entri baru `Locked 15 minutes`, `Locked 1 hour`, `Locked requires reset`, atau `Account locked` dibanding baseline hook pada log `Yoga Wibowo` di `Global Settings > User > Detail > User Log`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness g (asersi absence). `sourceTc` memuat TC fungsional yang asersi "tidak ada entri log" di Expected atau Post Condition-nya dipindah ke sini (S-05, prinsip 10): TC-AUTH-OTP-35 (butir c) dari E2E-001, TC-AUTH-OTP-36 (butir c) dari E2E-002, TC-AUTH-OTP-30 (butir c) dari E2E-010, TC-AUTH-OTP-86 (butir d) dari E2E-017, TC-AUTH-OTP-68 (Expected c dan Post Condition a dan b) dari E2E-015, TC-AUTH-OTP-62 (Post Condition a dan langkah 7) dari E2E-019, TC-AUTH-OTP-140 (butir c) dari E2E-020, TC-AUTH-OTP-78 (butir d) dari E2E-021, TC-AUTH-OTP-90 (butir d) dari E2E-024, TC-AUTH-OTP-31 (butir d) dan TC-AUTH-OTP-32 (butir c) dari E2E-029, TC-AUTH-OTP-157 (butir d) dari E2E-043. Asersi fungsionalnya (caption, toast, perpindahan layar, email OTP) tetap diasersi di spec asal; spec ini hanya memuat pemicu minimal dan asersi absence. Pembagian TC dicatat juga di Notes spec asal.
- Pemicu state berat tetap di spec asal: TC-AUTH-OTP-107 dan 111 (E2E-027) serta TC-AUTH-OTP-33, 34, 63, 85, dan 135 (E2E-028) tidak dipindah ke sini. Asersi absence TC fungsional lain ada di E2E-040. Penempatan ini mengikuti pengecualian P-1 (state berat tetap di spec asal).
- Pengecualian P-2 (pemicu bukan objek uji): intercept respons 500 pada TC-AUTH-OTP-31 (langkah 43 sampai 45) dan mode offline pada TC-AUTH-OTP-32 (langkah 48 sampai 51) hanya memicu kegagalan; objek asersinya ketiadaan entri log, dan intercept dilepas serta koneksi dipulihkan segera setelah pemicu.
- TC-AUTH-OTP-62 dan TC-AUTH-OTP-133 (E2E-040) memiliki pemicu yang sama (akun dihapus setelah kode diterbitkan, lalu Verify OTP). Blok TC-AUTH-OTP-62 tetap ditulis di sini karena TC-AUTH-OTP-62 tidak ada di `sourceTc` E2E-040 dan tiap TC harus punya asersi absence-nya sendiri; data user dipisah (`Maya Purnama` dan `Budi Permata`).
- Spec ini 72 langkah, di atas smell sekitar 35 langkah (prinsip 13), karena memuat 12 TC. Dipertahankan karena seluruh spec satu kelas (absence), tiap bagian (A sampai D) berdiri sendiri dengan user dan jendela privat terpisah, dan soft assertion berlaku. Log diperiksa sekali per bagian terhadap baseline yang dicatat di hook `before` (S-14).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, memuat ulang log, memasang dan menghapus intercept respons 500, memutus dan memulihkan koneksi, serta memajukan dan memulihkan jam server dan jam browser ditulis sebagai aksi tanpa `Verifikasi`. Klik ganda TC-AUTH-OTP-30 dan lima kode salah TC-AUTH-OTP-68 ditulis sebagai pemicu; hasilnya tidak diasersi di sini selain absence.
- Urutan TC mengikuti pengelompokan pemicu (navigasi, penolakan, kegagalan server, lock password), bukan nomor TC granular (S-05). TC-AUTH-OTP-140 dan TC-AUTH-OTP-62 memakai user milik spec ini yang dihapus langkah uji, bukan data Pre-setup bersama (S-06).
- Temuan untuk QA: (1) TC-AUTH-OTP-140 dan TC-AUTH-OTP-62 meminta pemeriksaan `Global Settings > User > Detail > User Log` untuk user yang sudah dihapus; User Log user terhapus tidak dapat dibuka, sehingga spec memeriksa `Global Settings > Activity Log > Session` saja untuk keduanya. (2) TC-AUTH-OTP-68 tidak menyebut reCAPTCHA pada Login with Password; spec menyelesaikan reCAPTCHA (mengikuti spec Auth lain). Surface log yang diperiksa (kedua surface, `Yoga Wibowo`) tertulis di TC pada langkah 8 dan Expected c. (3) TC-AUTH-OTP-30 butir c "tidak ada entri log ganda" tidak menyebut entri apa yang dianggap sah; karena Request OTP berhasil tidak dicatat (TC-AUTH-OTP-28), spec mengasersi tidak ada entri baru sama sekali. (4) TC-AUTH-OTP-32 meminta "putuskan koneksi internet" tanpa menyebut mekanismenya; kemampuan mode offline pada browser uji ditulis di Prerequisites. (5) TC-AUTH-OTP-157 tidak menyebut user mana yang diperiksa User Log-nya (tidak ada user untuk payload); hanya Activity Log Session yang diperiksa.
