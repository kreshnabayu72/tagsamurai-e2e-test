---
id: TC-AUTH-OTP-E2E-028-rate-limit-ip-429
title: "Penolakan IP Rate Limit pada Request OTP, Verify OTP, dan Resend"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-33
  - TC-AUTH-OTP-135
  - TC-AUTH-OTP-63
  - TC-AUTH-OTP-85
  - TC-AUTH-OTP-34
coverage:
  web: automated
---

# Penolakan IP Rate Limit pada Request OTP, Verify OTP, dan Resend

## Prerequisites

- Mode: FE+BE (flood nyata ke server dari IP browser uji; bukan mock, sesuai bagian 6 konvensi).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah state global: counter IP rate limit (direset sebelum tiap TC dan di hook `after`) serta jam server dan jam browser (digeser pada TC-AUTH-OTP-85, dipulihkan di langkah 43 dan di hook `after`).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Dipakai untuk membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tanpa login (halaman publik, tidak ada sesi aktif di browser) untuk semua langkah publik. reCAPTCHA memakai mode uji environment.
- Ambang: 20 request per menit per IP, jendela tetap 1 menit, counter terpisah per endpoint (`request`, `verify`); Resend OTP memakai endpoint Request OTP sehingga dihitung ke counter `request`; semua request yang mencapai limiter dihitung apa pun hasilnya (NC-15, `AUTHOTP-LOGIC-04c`). Request ke-21 dalam jendela yang sama ditolak.
- Kemampuan teknis:
  - Klien HTTP yang mengirim request beruntun dari IP yang sama dengan browser uji untuk mencapai 20 request ke endpoint `request` atau `verify` dalam 1 menit.
  - Isi 20 request flood pada TC-AUTH-OTP-33, TC-AUTH-OTP-135, dan TC-AUTH-OTP-85: 20 Request OTP dengan 20 email tak terdaftar yang berbeda, `floodtakterdaftar01@qwertysystem.net` sampai `floodtakterdaftar20@qwertysystem.net` (alamat literal dari TC, tanpa suffix `{runId}`; tidak di-seed), tiap request dihitung dalam batas IP apa pun hasilnya, bukan email user uji, supaya tidak ada kode terkirim ke user uji dan tidak ada cooldown aktif pada user uji (asersi tidak ada email OTP, langkah 8 dan 42). Token reCAPTCHA mode uji disertakan bila endpoint mewajibkannya.
  - 20 Request OTP sukses pada TC-AUTH-OTP-34: dikirim lewat UI otomatis (isi Email, centang widget reCAPTCHA mode uji, klik [Request OTP]) satu per satu untuk 20 email berbeda tanpa jeda tunggu, seluruhnya selesai dalam 60 detik; toast sukses "Success, the code has been sent." diamati langsung di UI pada tiap request sebelum request berikutnya. Request ke-21 dikirim dengan cara yang sama.
  - Akses untuk mereset counter IP rate limit environment (sebelum tiap TC, supaya request TC sebelumnya tidak ikut terhitung).
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Pengaturan jam server uji dan jam browser uji untuk langkah "Tunggu countdown 60 detik selesai" pada TC-AUTH-OTP-85 (konvensi bagian 6): countdown Resend berjalan di jam browser, sehingga kedua jam dimajukan 60 detik bersama. Kedua jam dimajukan sebelum pengiriman 20 request dan tidak dimajukan lagi di antara pengiriman 20 request dan request ke-21.
  - Dua konteks browser: jendela privat publik dan browser admin.
- Hook `before`: reset counter IP rate limit; login akun aktor Total Control (Global Settings) di browser admin; lalu (seeding API, email bersuffix per run) buat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2):
  - TC-AUTH-OTP-33: `Wulan Hakim` (`wulanhakim+{runId}-028@qwertysystem.net`).
  - TC-AUTH-OTP-135: `Andi Susanti` (`andisusanti+{runId}-028@qwertysystem.net`).
  - TC-AUTH-OTP-63: `Fajar Harahap` (`fajarharahap+{runId}-028@qwertysystem.net`).
  - TC-AUTH-OTP-85: `Mega Setiawan` (`megasetiawan+{runId}-028@qwertysystem.net`).
  - TC-AUTH-OTP-34: 21 user BASE bernama `Pengguna Flood 01` sampai `Pengguna Flood 21` dengan email `penggunaflood01+{runId}-028@qwertysystem.net` sampai `penggunaflood21+{runId}-028@qwertysystem.net` (user ke-1 sampai ke-20 untuk request sukses, user ke-21 untuk request ke-21 yang ditolak dan dipakai untuk membuka User Log).
- Baseline log: hook `before` mencatat jumlah baris `Wulan Hakim`, `Andi Susanti`, `Fajar Harahap`, `Mega Setiawan`, dan `Pengguna Flood 21` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tidak ada entri log baru" pada tiap TC dihitung terhadap baseline itu (S-12).
- Hook `after`: reset counter IP rate limit, kembalikan jam server uji dan jam browser uji ke waktu nyata, dan hapus semua user yang dibuat. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-33: Request OTP ditolak karena batas request IP terlampaui

1. Reset counter IP rate limit
2. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
3. Ketik `wulanhakim+{runId}-028@qwertysystem.net` pada field Email
4. Centang widget reCAPTCHA "I'm not a robot"
5. Kirim 20 Request OTP dari IP browser uji dalam 1 menit dengan 20 email tak terdaftar yang berbeda, `floodtakterdaftar01@qwertysystem.net` sampai `floodtakterdaftar20@qwertysystem.net` (hasil tiap request tidak berpengaruh; semua dihitung)
6. Dalam jendela 1 menit yang sama, klik button [Request OTP] (request ke-21)
7. Verifikasi Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
8. Verifikasi tidak ada email OTP terkirim ke `wulanhakim+{runId}-028@qwertysystem.net` di mail-catcher
9. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`)
10. Buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Wulan Hakim`
11. Verifikasi tidak ada entri log baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

### TC-AUTH-OTP-135: Penolakan karena batas request IP tidak dicatat

12. Reset counter IP rate limit
13. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
14. Ketik `andisusanti+{runId}-028@qwertysystem.net` pada field Email
15. Centang widget reCAPTCHA "I'm not a robot"
16. Kirim 20 Request OTP dari IP browser uji dalam 1 menit dengan 20 email tak terdaftar yang berbeda, `floodtakterdaftar01@qwertysystem.net` sampai `floodtakterdaftar20@qwertysystem.net` (hasil tiap request tidak berpengaruh; semua dihitung)
17. Dalam jendela 1 menit yang sama, klik button [Request OTP] (request ke-21)
18. Verifikasi request ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
19. Ganti konteks ke browser admin dan buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Andi Susanti`
20. Verifikasi tidak ada entri log baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

### TC-AUTH-OTP-63: Verify OTP ditolak karena batas request IP terlampaui

21. Reset counter IP rate limit
22. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
23. Ketik `fajarharahap+{runId}-028@qwertysystem.net` pada field Email
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Kirim 20 request Verify OTP dari IP browser uji dalam 1 menit (hasil tiap request tidak berpengaruh; semua dihitung)
27. Dalam jendela 1 menit yang sama, ketik 6 digit kode OTP dari email pada kotak digit (request ke-21)
28. Verifikasi Alert inline di atas area Resend dan button [Verify] pada layar Verify OTP: "Too many requests. Please try again later."
29. Verifikasi 6 digit tetap terisi untuk percobaan ulang
30. Verifikasi tidak ada sesi yang dibuat (layar tetap Verify OTP)
31. Ganti konteks ke browser admin dan buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Fajar Harahap`
32. Verifikasi tidak ada entri log baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

### TC-AUTH-OTP-85: Resend ditolak karena batas request IP terlampaui

33. Reset counter IP rate limit
34. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
35. Ketik `megasetiawan+{runId}-028@qwertysystem.net` pada field Email
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Request OTP]
38. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
39. Kirim 20 request ke endpoint Request OTP dari IP browser uji dalam 1 menit dengan 20 email tak terdaftar yang berbeda, `floodtakterdaftar01@qwertysystem.net` sampai `floodtakterdaftar20@qwertysystem.net` (batas 20 request per menit per IP; semua dihitung)
40. Dalam jendela 1 menit yang sama, klik [Resend code] (request ke-21)
41. Verifikasi Alert inline di atas area Resend dan button [Verify] pada layar Verify OTP: "Too many requests. Please try again later."
42. Verifikasi tidak ada email OTP baru terkirim ke `megasetiawan+{runId}-028@qwertysystem.net` di mail-catcher selain email dari langkah 37
43. Pulihkan jam server dan jam browser ke waktu nyata
44. Ganti konteks ke browser admin dan buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Mega Setiawan`
45. Verifikasi tidak ada entri log baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

### TC-AUTH-OTP-34: Request OTP yang sukses ikut dihitung dalam batas request IP

46. Reset counter IP rate limit
47. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
48. Kirim 20 Request OTP yang sukses untuk email berbeda (`penggunaflood01+{runId}-028@qwertysystem.net` sampai `penggunaflood20+{runId}-028@qwertysystem.net`) satu per satu dari IP yang sama dalam 1 menit, dengan mencentang widget reCAPTCHA pada tiap permintaan (cara pengiriman dan pengamatan toast: lihat Prerequisites)
49. Verifikasi request ke-1 sampai ke-20 berhasil: toast sukses "Success, the code has been sent." pada tiap permintaan
50. Kirim satu Request OTP lagi dengan email `penggunaflood21+{runId}-028@qwertysystem.net` (terdaftar dan aktif) dalam jendela 1 menit yang sama (request ke-21)
51. Verifikasi request ke-21 ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
52. Verifikasi tidak ada email OTP untuk request yang ditolak di mail-catcher untuk `penggunaflood21+{runId}-028@qwertysystem.net`
53. Ganti konteks ke browser admin dan buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Pengguna Flood 21`
54. Verifikasi tidak ada entri log baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini memuat dua kelas harness sekaligus: kelas c (flood rate limit, objek uji) dan kelas d (mail-catcher untuk asersi tidak ada email OTP, serta pengaturan jam untuk menunggu countdown 60 detik pada TC-AUTH-OTP-85). Kelas d di sini hanya langkah rutin yang bukan objek uji (konvensi bagian 3 butir 13 d dan bagian 6), sehingga tidak memicu pemisahan spec; TC-85 memerlukan Resend, yang hanya mungkin sesudah countdown selesai, di jendela flood yang sama.
- Kelas harness c. Suite berjalan serial (lihat Prerequisites), jadi flood tidak mengganggu spec lain; counter direset di awal tiap TC dan di `after`. TC-34 ditaruh paling akhir karena membuat paling banyak state (21 request dan kode aktif).
- Pengecualian P-1 (state berat): Expected "tidak ada entri log baru" pada TC-33, 34, 63, 85, dan TC-135 (seluruhnya asersi absence yang bergantung pada penolakan IP rate limit hasil flood) tetap di spec ini dan tidak dipindah ke spec absence E2E-040, karena memerlukan state flood yang baru dibangun. Pembagian ini dicatat juga di Notes E2E-040.
- Langkah penghubung (S-03): langkah 1, 12, 21, 33, 46 (reset counter), langkah 43 (memulihkan jam), serta langkah 9, 13, 19, 22, 31, 34, 44, 47, 53 (ganti konteks). Pengiriman 20 request pada TC-33 dan TC-135 dilakukan setelah email dan reCAPTCHA terisi (urutan prasyarat "IP sudah mengirim 20 request" digeser tepat sebelum klik [Request OTP]) supaya request ke-21 jatuh dalam jendela 1 menit yang sama.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan periksa mail-catcher berbeda dari TC sumber: TC-AUTH-OTP-33 langkah 6, TC-AUTH-OTP-85 langkah 9, dan TC-AUTH-OTP-34 langkah 5 menaruh "Periksa mail-catcher" sesudah membuka log di sesi admin. Spec memeriksa mail-catcher (langkah 8, 42, 52) sebelum ganti konteks ke browser admin, supaya asersi email dibaca pada konteks publik yang sama dengan request yang ditolak tanpa kembali dari browser admin; tidak ada Expected yang bergantung pada urutan ini.
- Aturan suffix `{runId}-028` tidak berlaku untuk email flood: TC menetapkan alamat literal `floodtakterdaftar01@qwertysystem.net` sampai `floodtakterdaftar20@qwertysystem.net` (tak terdaftar, tidak di-seed), dan spec mengikuti TC. Karena suite berjalan serial dan counter IP direset di awal tiap TC, alamat yang sama dipakai ulang pada TC-33, TC-135, dan TC-85.
- Temuan untuk QA:
  - TC-63 langkah 5 ("Kirim 20 request Verify OTP") tidak menyebut isi kode yang dikirim. Bila 20 request memakai kode salah, lima kali salah pada kode yang sama meng-invalidate kode (TC-65); spec tidak menentukan isi request flood dan hanya mengasersi akibat pada request ke-21.
  - TC-34 langkah 2 tidak menyebut cara 20 Request OTP dikirim dan toast diamati dalam 1 menit dengan reCAPTCHA per request, atau cara form Request OTP dipakai ulang sesudah request sukses; spec memakai pengiriman UI otomatis (lihat Prerequisites).
  - TC-33 dan TC-135 hampir identik (request ke-21 ditolak dan tidak dicatat); keduanya dipertahankan karena sumbernya terpisah di Section 3b dan 5c.
  - TC-85 langkah 5 ("Tunggu countdown 60 detik selesai") tidak menyebut cara jam diatur. NC-11 (keputusan user 2026-10-06) menetapkan countdown dihitung dari timestamp server dan bertahan setelah refresh, tetapi tidak menyatakan jam yang dibaca penghitung mundur di UI; spec memajukan jam server dan jam browser bersama agar hasil tidak bergantung pada jawabannya. Mohon QA memastikan jam yang dipakai penghitung mundur.
