---
id: TC-AUTH-OTP-E2E-025-sesi-email-request-menghitung-resend
title: "Sesi Email-Request: Request OTP Setelah Cooldown Dihitung sebagai Resend dan Penolakan Tidak Menambah Hitungan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-91
  - TC-AUTH-OTP-182
coverage:
  web: automated
---

# Sesi Email-Request: Request OTP Setelah Cooldown Dihitung sebagai Resend dan Penolakan Tidak Menambah Hitungan

## Prerequisites

- Mode: FE+BE.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser). reCAPTCHA memakai mode uji environment.
- Kemampuan teknis:
  - Pengaturan jam server uji dan jam browser uji (konvensi bagian 6). Countdown Resend di UI berjalan di jam browser, sehingga setiap langkah "Tunggu countdown 60 detik selesai" dipenuhi dengan memajukan jam server dan jam browser 60 detik bersama, lalu menunggu UI menyegarkan state tombol Resend. Pada TC-AUTH-OTP-182, Request OTP kedua harus dikirim sebelum cooldown 60 detik pertama selesai (kedua jam tidak dimajukan di antara langkah 21 dan langkah 25).
- State global: jam server dan jam browser. Suite berjalan serial (`parallel: false`) karena kedua jam digeser. Kedua jam dipulihkan ke waktu nyata di langkah 17 dan di hook `after`.
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API, email bersuffix per run) membuat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2):
  - TC-AUTH-OTP-91: `Doni Aditya` (`doniaditya+{runId}-025@qwertysystem.net`).
  - TC-AUTH-OTP-182: `Agus Wulandari` (`aguswulandari+{runId}-025@qwertysystem.net`).
- Hook `after`: kembalikan jam server uji dan jam browser uji ke waktu nyata dan hapus kedua user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-91: Request OTP ulang pada email yang sama setelah cooldown selesai diterima dan dihitung sebagai resend

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `doniaditya+{runId}-025@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Tunggu countdown 60 detik selesai
6. Klik tautan [Back to Login with Password]
7. Klik tautan [Log in with OTP]
8. Centang widget reCAPTCHA "I'm not a robot"
9. Klik button [Request OTP]
10. Verifikasi toast sukses: "Success, the code has been sent."
11. Verifikasi halaman Verify OTP tampil
12. Verifikasi area Resend menampilkan "Resend code in (00:59)"
13. Verifikasi area Resend dalam keadaan disabled
14. Ulangi empat kali (Resend ke-2 sampai ke-5 menurut hitungan sesi): tunggu countdown 60 detik selesai, lalu klik [Resend code]
15. Verifikasi area Resend menampilkan "Resend code in (09:59)", karena Request OTP kedua dihitung sebagai resend ke-1 dan keempat Resend sebagai resend ke-2 sampai ke-5
16. Verifikasi area Resend dalam keadaan disabled (State C)
17. Pulihkan jam server dan jam browser ke waktu nyata

### TC-AUTH-OTP-182: Penolakan Request OTP saat cooldown tidak menambah jumlah resend

18. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
19. Ketik `aguswulandari+{runId}-025@qwertysystem.net` pada field Email
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Request OTP]
22. Klik tautan [Back to Login with Password]
23. Klik tautan [Log in with OTP]
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Verifikasi Request OTP kedua ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
27. Tekan tombol Back browser sampai layar Verify OTP tampil
28. Ulangi empat kali (Resend ke-1 sampai ke-4), pada tiap pengulangan: tunggu countdown 60 detik selesai, lalu klik [Resend code]
29. Verifikasi area Resend menampilkan "Resend code in (00:59)" setelah Resend ke-4
30. Tunggu countdown 60 detik selesai
31. Klik [Resend code] (Resend ke-5)
32. Verifikasi area Resend menampilkan "Resend code in (09:59)" setelah Resend ke-5; penolakan sebelumnya tidak dihitung

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Langkah penghubung (S-03): langkah 27 memakai Back browser untuk kembali ke layar Verify OTP, mengikuti TC-182 langkah 9; langkah 17 memulihkan kedua jam sebelum TC-182 dimulai.
- Post Condition TC-91 ("jumlah resend sesi menjadi 5") tidak punya langkah observasi sendiri dan tercakup oleh Expected b (langkah 14 dan verifikasi sesudahnya), sehingga tidak diasersi terpisah (S-01). Spec ini tidak membaca email, jadi mail-catcher tidak dicantumkan di Prerequisites (S-11).
- Langkah "Ulangi empat kali" pada langkah 14 dan 28 menuliskan ulang loop Resend dari TC sumber (TC-91 langkah 10 sampai 17, TC-182 langkah 10 sampai 19) sebagai satu langkah teks; tiap Resend dalam loop tidak punya Expected sendiri di TC sumber.
- Tidak ada asersi pencatatan log pada spec ini; Request OTP yang ditolak karena cooldown tidak dicatat dan diasersi di spec absence E2E-040.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - NC-11 (keputusan user 2026-10-06) menetapkan countdown dihitung dari timestamp server dan bertahan setelah refresh. TC tidak menyatakan jam mana yang dibaca penghitung mundur di UI (jam server atau jam browser), sehingga spec memajukan jam server dan jam browser bersama (konvensi bagian 6) agar hasil tidak bergantung pada jawabannya. Mohon QA memastikan jam yang dipakai penghitung mundur.
  - TC-91 langkah 5 menunggu 60 detik sebelum kembali ke Login with Password; spec mempertahankannya, sehingga Request OTP kedua terjadi tepat setelah cooldown selesai.
  - TC-182 langkah 9 menyebut Back browser sampai layar Verify OTP tampil tanpa memverifikasi layar itu; spec tidak menambah `Verifikasi` untuk layar Verify OTP di sini.
