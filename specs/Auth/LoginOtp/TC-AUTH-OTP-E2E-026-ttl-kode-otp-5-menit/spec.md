---
id: TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit
title: "Masa Berlaku Kode OTP 5 Menit: Expired, Batas 4:59 dan 5:00, dan Kode yang Sudah Diganti"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-50
  - TC-AUTH-OTP-123
  - TC-AUTH-OTP-194
  - TC-AUTH-OTP-55
  - TC-AUTH-OTP-51
  - TC-AUTH-OTP-193
coverage:
  web: automated
---

# Masa Berlaku Kode OTP 5 Menit: Expired, Batas 4:59 dan 5:00, dan Kode yang Sudah Diganti

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Dipakai untuk membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` pada TC-AUTH-OTP-123.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tanpa login (halaman publik, tidak ada sesi aktif di browser) untuk semua langkah publik. reCAPTCHA memakai mode uji environment.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Manipulasi jam server uji: jam server diatur ke nilai absolut lalu dibekukan sampai Verify selesai, bukan digeser relatif, karena detik nyata sejak request tidak dihitung pada batas eksak (konvensi bagian 6). Di akhir tiap TC pembekuan dilepas dan jam server dipulihkan ke waktu nyata, sehingga T0 TC berikutnya dan bagian TC-AUTH-OTP-55 berasal dari jam yang berjalan. Waktu terbit kode (T0) dibaca dari cap waktu email OTP di mail-catcher (seperti pada TC-AUTH-OTP-193 dan 194); langkah "Atur jam server ..." memakai T0 + N detik (N = 60, 330, 300, 240, atau 299; batas 5 menit eksklusif, NC-11: valid kurang dari 300 detik).
  - Umur kode (TTL 5 menit) dihitung murni di server dan tidak diamati lewat UI, sehingga pada TC-AUTH-OTP-50, 194, 51, dan 193 hanya jam server yang diatur; jam browser tidak diubah dan tidak memengaruhi hasil.
  - Pada TC-AUTH-OTP-55, countdown Resend 60 detik berjalan di jam browser, sehingga langkah "Tunggu countdown 60 detik selesai" (langkah 40) mengatur jam server absolut ke T0 + 60 detik dan memajukan jam browser 60 detik bersama; jam browser dipulihkan di langkah 42, sebelum jam server diatur ke T0 + 330 detik.
  - Dua konteks browser: jendela privat publik dan browser admin.
- State global: jam server dan jam browser. Suite berjalan serial (`parallel: false`) karena kedua jam digeser; keduanya dipulihkan di hook `after`.
- Hook `before`: login akun aktor Total Control (Global Settings) di browser admin; lalu (seeding API, email bersuffix per run) buat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2):
  - TC-AUTH-OTP-50 dan TC-AUTH-OTP-123 (satu percobaan Verify yang sama): `Ayu Prasetyo` (`ayuprasetyo+{runId}-026@qwertysystem.net`).
  - TC-AUTH-OTP-194: `Kirana Dewanti` (`kiranadewanti+{runId}-026@qwertysystem.net`).
  - TC-AUTH-OTP-55: `Andi Kartika` (`andikartika+{runId}-026@qwertysystem.net`).
  - TC-AUTH-OTP-51: `Fikri Purnama` (`fikripurnama+{runId}-026@qwertysystem.net`).
  - TC-AUTH-OTP-193: `Johan Saputra` (`johansaputra+{runId}-026@qwertysystem.net`).
- Baseline log: hook `before` mencatat jumlah baris `Ayu Prasetyo` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tepat satu baris baru" pada langkah 16 dan 19 dihitung terhadap baseline itu (S-12).
- Hook `after`: lepaskan pembekuan, kembalikan jam server uji dan jam browser uji ke waktu nyata, tutup sesi login yang terbentuk (TC-AUTH-OTP-51 dan 193), dan hapus kelima user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-50: Verify OTP dengan kode terbaru yang sudah melewati 5 menit

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `ayuprasetyo+{runId}-026@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Catat waktu terbit kode T0 dari cap waktu email OTP di mail-catcher
6. Atur jam server secara absolut ke T0 + 330 detik (5 menit 30 detik sejak kode diterbitkan) lalu bekukan
7. Ketik 6 digit kode OTP dari email pada kotak digit
8. Verifikasi kotak digit menampilkan alert tanpa shake animation
9. Verifikasi caption error di bawah kotak digit: "OTP expired"
10. Verifikasi kotak digit dikosongkan otomatis
11. Verifikasi kursor kembali ke kotak 1
12. Verifikasi tidak ada sesi yang dibuat (layar tetap Verify OTP)
13. Lepaskan pembekuan jam server dan pulihkan jam server ke waktu nyata

### TC-AUTH-OTP-123: Pencatatan OTP expired pada kode terbaru yang lewat 5 menit

14. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`)
15. Buka `Global Settings > Activity Log > Session`
16. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Ayu Prasetyo`, Activity `Login`, Status `Failed`, dan Note `OTP expired`
17. Verifikasi pada baris itu kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
18. Buka `Global Settings > User > Detail > User Log` untuk `Ayu Prasetyo`
19. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, dan Note `OTP expired`
20. Verifikasi pada baris itu IP Address dan Device / Browser sama dengan baris di Activity Log Session

### TC-AUTH-OTP-194: Verify OTP dengan kode yang berumur tepat 5 menit 00 detik ditolak sebagai expired

21. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
22. Ketik `kiranadewanti+{runId}-026@qwertysystem.net` pada field Email
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Request OTP]
25. Catat waktu terbit kode T0 dari cap waktu email OTP di mail-catcher
26. Atur jam server secara absolut ke T0 + 300 detik (tepat 5 menit 00 detik sejak kode diterbitkan) lalu bekukan jam server sampai Verify selesai; jam browser tidak diubah
27. Ketik 6 digit kode OTP dari email pada kotak digit
28. Verifikasi kotak digit menampilkan alert tanpa shake animation
29. Verifikasi caption error di bawah kotak digit: "OTP expired" (batas eksklusif: kode berumur tepat 300 detik sudah tidak valid)
30. Verifikasi kotak digit dikosongkan otomatis
31. Verifikasi kursor kembali ke kotak 1
32. Verifikasi tidak ada sesi yang dibuat (layar tetap Verify OTP)
33. Lepaskan pembekuan jam server dan pulihkan jam server ke waktu nyata

### TC-AUTH-OTP-55: Kode yang sudah diganti dan juga melewati 5 menit ditolak sebagai kode salah, bukan kedaluwarsa

34. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
35. Ketik `andikartika+{runId}-026@qwertysystem.net` pada field Email
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Request OTP]
38. Catat waktu terbit kode pertama T0 dari cap waktu email OTP di mail-catcher
39. Catat kode OTP pertama dari email
40. Tunggu countdown 60 detik selesai: atur jam server secara absolut ke T0 + 60 detik dan majukan jam browser 60 detik
41. Klik [Resend code]
42. Pulihkan jam browser ke waktu nyata
43. Atur jam server secara absolut ke T0 + 330 detik (5 menit 30 detik sejak kode pertama diterbitkan) lalu bekukan
44. Ketik kode OTP pertama pada kotak digit
45. Verifikasi kode pertama ditolak sebagai kode salah: shake animation pada kotak digit
46. Verifikasi border severity danger pada kotak digit
47. Verifikasi caption error di bawah kotak digit: "Invalid code"
48. Verifikasi caption kedaluwarsa ("OTP expired") tidak dipakai untuk kode yang sudah diganti
49. Verifikasi tidak ada sesi yang dibuat (layar tetap Verify OTP)
50. Lepaskan pembekuan jam server dan pulihkan jam server ke waktu nyata

### TC-AUTH-OTP-51: Verify OTP dengan kode yang berumur kurang dari 5 menit diterima

51. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
52. Ketik `fikripurnama+{runId}-026@qwertysystem.net` pada field Email
53. Centang widget reCAPTCHA "I'm not a robot"
54. Klik button [Request OTP]
55. Catat waktu terbit kode T0 dari cap waktu email OTP di mail-catcher
56. Atur jam server secara absolut ke T0 + 240 detik (4 menit sejak kode diterbitkan) lalu bekukan
57. Ketik 6 digit kode OTP dari email pada kotak digit
58. Verifikasi verifikasi berhasil dan browser dialihkan ke Portal — Product Hub
59. Verifikasi sesi aktif untuk `Fikri Purnama`
60. Lepaskan pembekuan jam server dan pulihkan jam server ke waktu nyata

### TC-AUTH-OTP-193: Verify OTP dengan kode yang berumur 4 menit 59 detik diterima (satu detik sebelum batas)

61. Logout dari Portal — Product Hub, lalu buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
62. Ketik `johansaputra+{runId}-026@qwertysystem.net` pada field Email
63. Centang widget reCAPTCHA "I'm not a robot"
64. Klik button [Request OTP]
65. Catat waktu terbit kode T0 dari cap waktu email OTP di mail-catcher
66. Atur jam server secara absolut ke T0 + 299 detik (4 menit 59 detik sejak kode diterbitkan) lalu bekukan jam server sampai Verify selesai; jam browser tidak diubah
67. Ketik 6 digit kode OTP dari email pada kotak digit
68. Verifikasi verifikasi berhasil dan browser dialihkan ke Portal — Product Hub (kode valid selama kurang dari 300 detik)
69. Verifikasi sesi aktif untuk `Johan Saputra`
70. Lepaskan pembekuan jam server dan pulihkan jam server ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Pengecualian P-3 (user berurutan): TC-50 dan TC-123 di sumber memakai dua user (`Ayu Prasetyo` dan `Mega Permata`) untuk alur yang sama (Request OTP, tunggu 5 menit 30 detik, ketik kode). Spec memakai satu user (`Ayu Prasetyo`) dan satu percobaan Verify: TC-123 membaca log atas percobaan Failed yang dihasilkan TC-50, sehingga satu kali tunggu 5 menit 30 detik cukup. Asersi pencatatan (Status `Failed`, Note `OTP expired`) boleh berada di spec fungsional; hanya asersi absence yang dipisah (konvensi bagian 3, kelas g).
- Urutan di sumber (50, 51, 193, 194, 55, 123) berubah menjadi 50 + 123, 194, 55, 51, 193 mengikuti bagian 3: kasus ditolak (tidak membuat sesi) lebih dulu, kasus berhasil yang membuat sesi di akhir.
- Spec melewati 35 langkah (±70) karena enam TC memakai kombinasi usia kode berbeda; tiap TC memakai user dan kode sendiri sehingga bagian sesudah tetap bermakna walau bagian sebelumnya gagal (jam server hanya dimajukan, tidak diulang). Jam server dipulihkan ke waktu nyata di akhir tiap TC; bila lingkungan menerapkan idle timeout pada sesi browser admin, login ulang akun aktor sebelum langkah 14 (hanya langkah 14 sampai 20 memakai browser admin).
- Langkah penghubung (S-03): langkah 14, 21, 34, 51, 61 (ganti konteks dan membuka jendela privat baru supaya tiap TC memulai dari konteks bersih; langkah 61 juga logout setelah login sukses TC-51).
- Langkah penghubung jam (S-03, S-11): langkah 5, 25, 38, 55, 65 (mencatat T0), langkah 13, 33, 50, 60, 70 (melepas pembekuan dan memulihkan jam server ke waktu nyata agar TC berikutnya memakai T0 dari jam yang berjalan), dan langkah 42 (memulihkan jam browser).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - NC-11 menetapkan "TC batas waktu eksak tidak ditulis; TC ditulis di sisi aman batas (4 menit vs 5 menit 30 detik)", tetapi TC-193 (4 menit 59 detik) dan TC-194 (tepat 5 menit 00 detik) menguji batas eksak. Spec mengikuti TC-193 dan TC-194; keselarasan dengan NC-11 perlu dikonfirmasi.
  - TC-50, TC-51, dan TC-55 tidak menyebut cara jam diatur ("Tunggu ..."). Spec memakai jam server absolut T0 + N detik yang dibekukan (konvensi bagian 6) dan menambah langkah mencatat T0; TC-193 dan TC-194 sudah menyebut cara jam diatur, ketiga TC itu belum.
  - NC-11 (keputusan user 2026-10-06) menetapkan countdown dihitung dari timestamp server dan bertahan setelah refresh. Pada TC-55 TC tidak menyatakan jam mana yang dibaca penghitung mundur di UI, sehingga jam browser dimajukan bersama jam server agar hasil tidak bergantung pada jawabannya. Mohon QA memastikan jam yang dipakai penghitung mundur.
  - TC-55 Expected c menyatakan caption kedaluwarsa tidak dipakai, tetapi tidak menyebut teks yang tidak boleh muncul; spec mengasersi bahwa "OTP expired" tidak tampil (teks dari NC-01).
  - TC-55 Post Condition a ("Percobaan dicatat Failed `Incorrect OTP`") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01). Mohon QA menambah langkah membuka log di TC-55.
  - TC-123 di sumber memakai user `Mega Permata` dan menjalankan Request OTP serta menunggu 5 menit 30 detik sendiri, tetapi spec melebur TC-123 ke percobaan TC-50 (P-3). Hasil TC-123 bergantung pada urutan setelah TC-50 (log yang dibaca dihasilkan Verify TC-50), dan TC tidak menyatakan ketergantungan itu. Mohon QA mengonfirmasi atau menambahkannya di TC.
