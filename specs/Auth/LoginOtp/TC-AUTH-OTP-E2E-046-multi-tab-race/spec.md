---
id: TC-AUTH-OTP-E2E-046-multi-tab-race
title: "Multi-Tab dan Multi-Browser: Cooldown Lintas Konteks, Resend, Request, dan Verify Bersamaan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-170
  - TC-AUTH-OTP-165
  - TC-AUTH-OTP-173
  - TC-AUTH-OTP-164
coverage:
  web: automated
---

# Multi-Tab dan Multi-Browser: Cooldown Lintas Konteks, Resend, Request, dan Verify Bersamaan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`; dipakai membaca log pada TC-AUTH-OTP-164.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua tab pada satu jendela privat (duplikasi tab) dan profil browser lain (browser atau perangkat berbeda) yang dikendalikan bersamaan; aksi pada dua tab "hampir bersamaan" dengan jeda antar-klik di bawah 100 ms; mail-catcher lingkungan uji untuk membaca dan menghitung email OTP; klien HTTP untuk mengirim Verify OTP langsung ke server (`/v2/iam/auth/otp/verify` di `auth/login-otp/API/openapi.yaml`) pada TC-AUTH-OTP-164 langkah 8; percepatan jam server untuk melewati countdown Resend 60 detik (TC-AUTH-OTP-165, lima kali) dengan jam dipulihkan di hook `after`; reCAPTCHA mode uji.
- Jam yang diatur (konvensi bagian 6): jam server dan jam browser (klien) dimajukan bersama, karena countdown Resend di UI berjalan di jam klien sehingga memajukan jam server saja tidak mengaktifkan [Resend code]. Hook `after` memulihkan kedua jam. Suite berjalan serial (`parallel: false`) karena jam server digeser.
- Hook `before` (seeding API) membuat user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) dengan suffix per run `+{runId}-046`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal Activity Log Session dan User Log tiap user dicatat di hook:
  - TC-AUTH-OTP-170: `Irfan Lestari` (`irfanlestari+{runId}-046@qwertysystem.net`)
  - TC-AUTH-OTP-165: `Nadia Purnama` (`nadiapurnama+{runId}-046@qwertysystem.net`)
  - TC-AUTH-OTP-173: `Ayu Damayanti` (`ayudamayanti+{runId}-046@qwertysystem.net`)
  - TC-AUTH-OTP-164: `Surya Prasetyo` (`suryaprasetyo+{runId}-046@qwertysystem.net`)
- Tanpa login pada langkah publik: halaman Login with OTP adalah halaman publik, tidak ada sesi aktif di browser. Pengecualian: langkah 41 dan 50 mengamati sesi aktif hasil login sukses, dan langkah 53 sampai 58 memakai browser admin.

## Test Steps

### TC-AUTH-OTP-170: Request OTP email yang sama dari tab baru dan browser lain saat cooldown berjalan ditolak

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `irfanlestari+{runId}-046@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Buka tab baru pada browser yang sama, buka halaman Request OTP, ketik `irfanlestari+{runId}-046@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
6. Verifikasi pada tab baru muncul Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
7. Verifikasi tab baru tidak berpindah ke Verify OTP
8. Buka profil browser lain (browser atau perangkat berbeda), buka halaman Request OTP, ketik `irfanlestari+{runId}-046@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
9. Verifikasi pada browser lain muncul Alert yang sama
10. Verifikasi sesi email-request tidak terikat device atau browser
11. Verifikasi tidak ada email OTP baru terkirim di mail-catcher untuk `irfanlestari+{runId}-046@qwertysystem.net`

### TC-AUTH-OTP-165: Dua tab menekan Resend bersamaan hanya menerbitkan satu kode baru

12. Tutup jendela privat dan profil browser lain sebelumnya, buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `nadiapurnama+{runId}-046@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Duplikasi tab pada halaman Verify OTP (tab A dan tab B)
17. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
18. Klik [Resend code] pada tab A dan tab B hampir bersamaan
19. Verifikasi tepat satu email OTP baru diterima di `nadiapurnama+{runId}-046@qwertysystem.net`
20. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
21. Klik [Resend code]
22. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
23. Klik [Resend code]
24. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
25. Klik [Resend code]
26. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
27. Klik [Resend code]
28. Verifikasi area Resend menampilkan "Resend code in (09:59)" disabled setelah Resend terakhir (Resend ke-5 karena Resend bersamaan dihitung satu), bukan lebih awal
29. Pulihkan jam server dan jam browser ke waktu nyata

### TC-AUTH-OTP-173: Dua tab meminta OTP untuk email yang sama bersamaan menyisakan satu kode aktif

30. Tutup jendela privat sebelumnya, buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
31. Ketik `ayudamayanti+{runId}-046@qwertysystem.net` pada field Email
32. Centang widget reCAPTCHA "I'm not a robot"
33. Duplikasi tab, centang widget reCAPTCHA "I'm not a robot" pada tab B
34. Klik [Request OTP] pada tab A dan tab B hampir bersamaan
35. Baca kedua email OTP yang masuk di mail-catcher `ayudamayanti+{runId}-046@qwertysystem.net`; kode lama = email yang diterbitkan lebih dulu, kode baru = email yang diterbitkan terakhir
36. Ketik kode lama pada layar Verify OTP yang terbuka
37. Verifikasi kode lama ditolak dengan caption "Invalid code"
38. Ketik kode baru pada layar Verify OTP yang sama
39. Verifikasi kode baru diterima sekali
40. Verifikasi browser dialihkan ke Portal — Product Hub
41. Verifikasi sesi aktif untuk `Ayu Damayanti`
42. Verifikasi hanya kode terbitan terakhir yang dapat dipakai login (kode lama ditolak pada langkah 37, kode baru diterima pada langkah 39)

### TC-AUTH-OTP-164: Dua tab memverifikasi kode yang sama bersamaan hanya membuat satu sesi

43. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
44. Ketik `suryaprasetyo+{runId}-046@qwertysystem.net` pada field Email
45. Centang widget reCAPTCHA "I'm not a robot"
46. Klik button [Request OTP]
47. Duplikasi tab pada halaman Verify OTP (tab A dan tab B)
48. Ketik kode OTP dari email pada tab A dan tab B hampir bersamaan
49. Verifikasi tepat satu tab berhasil dan browser dialihkan ke Portal — Product Hub
50. Verifikasi sesi aktif untuk `Surya Prasetyo`
51. Verifikasi tab yang kalah ditolak tanpa membuat sesi kedua: shake animation
52. Verifikasi tab yang kalah ditolak tanpa membuat sesi kedua: caption "Invalid code"
53. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session` untuk `Surya Prasetyo`
54. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` untuk `Surya Prasetyo` di `Global Settings > Activity Log > Session`
55. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Failed `Incorrect OTP` untuk `Surya Prasetyo` di `Global Settings > Activity Log > Session`
56. Buka `Global Settings > User > Detail > User Log` untuk `Surya Prasetyo`
57. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` untuk `Surya Prasetyo` di User Log
58. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Failed `Incorrect OTP` untuk `Surya Prasetyo` di User Log
59. Kirim permintaan Verify OTP langsung ke server dengan email `suryaprasetyo+{runId}-046@qwertysystem.net` dan kode OTP yang sudah dipakai tadi
60. Verifikasi permintaan ditolak server
61. Verifikasi tidak ada sesi baru yang dibuat untuk `Surya Prasetyo`
62. Verifikasi kode OTP berstatus terpakai sekali (diamati dari penolakan pada langkah 60)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness c (multi-konteks: multi-tab, multi-browser, race antar-sesi). Spec ini 62 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena keempat TC memakai harness yang sama (dua tab atau browser bersamaan), user dan jendela privat terpisah per blok, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC di dalam spec berbeda dari nomor TC: TC-AUTH-OTP-170 dan 165 (tanpa login) lebih dulu, lalu TC-AUTH-OTP-173 dan 164 yang menyelesaikan login (S-05, S-10).
- Langkah penghubung (S-03): menutup dan membuka jendela privat, duplikasi tab, dan mengganti konteks ke browser admin ditulis sebagai aksi tanpa `Verifikasi`. Pada TC-AUTH-OTP-165 langkah 20 sampai 27 mengulang "majukan jam lalu Resend" empat kali karena tiap Resend butuh countdown 60 detik.
- Asersi pada log di TC-AUTH-OTP-164 adalah asersi jumlah ("tepat satu baris Success dan tepat satu baris Failed"), bukan absence, sehingga tetap di spec ini (kelas g tidak berlaku); tiap surface log dibuka dan diasersi sendiri (langkah 54, 55, 57, dan 58).
- Pengecualian P-2 (pemicu bukan objek uji): memutar ulang kode yang sudah terpakai langsung ke server pada TC-AUTH-OTP-164 (langkah 59 sampai 60; langkah 8 TC) adalah langkah observasi Expected d dan Post Condition a, bukan objek uji spec ini.
- Pembacaan "Resend code in (09:59)" pada TC-AUTH-OTP-165 (langkah 28) memakai pergeseran jam relatif (majukan 60 detik), bukan jam yang dibekukan absolut; polanya sama dengan spec 018, 022, dan 023.
- Percepatan jam server dan jam browser pada TC-AUTH-OTP-165 aman bagi blok lain karena kedua jam dipulihkan pada langkah 29 (hook `after` tetap menjadi cadangan) dan suite berjalan serial.
- Temuan untuk QA: (1) Langkah 9 TC-AUTH-OTP-165 berbunyi "ulangi menunggu dan klik [Resend code] sampai total 4 kali setelah Resend bersamaan" dan Expected menyebut "Resend ke-5 bila Resend bersamaan dihitung satu"; spec membaca ini sebagai satu Resend bersamaan ditambah empat Resend berurutan. (2) Syarat "hampir bersamaan" pada TC-AUTH-OTP-164, 165, dan 173 tidak menyebut batas selang waktu antar-klik; spec memakai kemampuan teknis di bawah 100 ms sebagai asumsi. (3) Expected d TC-AUTH-OTP-164 ("tidak ada sesi baru yang dibuat" pada langkah 8) tidak menyebut cara mengamati sesi; spec tidak menambah kemampuan baca sesi dan hanya mengasersi penolakan server serta mengikuti kalimat TC pada langkah 61. Post Condition a ("kode OTP berstatus terpakai sekali") diamati TC dari penolakan pada langkah 8, sehingga langkah 62 tidak punya mekanisme baca status kode tersendiri.
