---
id: TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback
title: "Verify OTP dengan Kode Salah dan Button Verify Fallback"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-49
  - TC-AUTH-OTP-56
  - TC-AUTH-OTP-60
  - TC-AUTH-OTP-69
  - TC-AUTH-OTP-177
coverage:
  web: automated
---

# Verify OTP dengan Kode Salah dan Button Verify Fallback

## Prerequisites

- Mode: FE+BE (Verify OTP terhadap backend nyata; respons Verify OTP dipaksa `500` lewat intercept parsial hanya sebagai pemicu munculnya button [Verify] fallback pada TC-AUTH-OTP-56, TC-AUTH-OTP-60, dan TC-AUTH-OTP-177).
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-014`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-49: `Doni Handayani` (`donihandayani+{runId}-014@qwertysystem.net`)
  - TC-AUTH-OTP-69: `Sari Wijaya` (`sariwijaya+{runId}-014@qwertysystem.net`)
  - TC-AUTH-OTP-56: `Dewi Firmansyah` (`dewifirmansyah+{runId}-014@qwertysystem.net`)
  - TC-AUTH-OTP-60: `Rina Handayani` (`rinahandayani+{runId}-014@qwertysystem.net`)
  - TC-AUTH-OTP-177: `Siti Prasetyo` (`sitiprasetyo+{runId}-014@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji di environment (centang tanpa tantangan); `Spectra.intercept()` untuk memaksa respons Verify OTP menjadi server error 500 lalu memulihkannya ke normal (dipulihkan juga di hook `after` bila spec gagal di tengah).
- Kode salah yang diketik adalah `000000` (kode yang berbeda dari kode yang diterbitkan untuk user itu).
- State yang berubah: TC-AUTH-OTP-177 diakhiri dengan login sukses (sesi web aktif untuk `Siti Prasetyo`); hook `after` menutup sesi itu.

## Test Steps

### TC-AUTH-OTP-49: Verify OTP dengan kode salah

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `donihandayani+{runId}-014@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Ketik 6 digit kode yang berbeda dari kode di email (`000000`)
4. Verifikasi kotak digit menampilkan shake animation
5. Verifikasi kotak digit berborder severity danger
6. Verifikasi caption error di bawah kotak digit: "Invalid code"
7. Verifikasi kotak digit dikosongkan otomatis
8. Verifikasi kursor kembali ke kotak 1
9. Verifikasi tidak ada sesi yang dibuat
10. Verifikasi halaman tetap di Verify OTP

### TC-AUTH-OTP-69: Caption error Verify OTP saat user mulai mengetik ulang setelah kode salah

11. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
12. Ketik `sariwijaya+{runId}-014@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
13. Ketik 6 digit kode yang salah (`000000`)
14. Verifikasi kotak digit menampilkan shake animation
15. Verifikasi kotak digit berborder severity danger
16. Verifikasi kotak digit dikosongkan
17. Verifikasi kursor di kotak 1
18. Ketik digit `1` pada kotak 1
19. Verifikasi caption error hilang segera setelah digit `1` diketik
20. Verifikasi border danger hilang segera setelah digit `1` diketik
21. Verifikasi digit `1` tampil di kotak 1

### TC-AUTH-OTP-56: Klik Verify fallback sebelum 6 digit terisi menampilkan OTP must not be empty

22. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
23. Ketik `dewifirmansyah+{runId}-014@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
24. Atur respons Verify OTP menjadi server error 500
25. Ketik 6 digit kode OTP dari email (mail-catcher `dewifirmansyah+{runId}-014@qwertysystem.net`) pada kotak digit
26. Verifikasi verifikasi otomatis gagal
27. Verifikasi button [Verify] muncul
28. Hapus digit terakhir (kotak 6) sehingga hanya 5 kotak terisi
29. Pulihkan respons Verify OTP menjadi normal
30. Klik button [Verify]
31. Verifikasi caption error di bawah kotak digit: "OTP must not be empty"
32. Verifikasi tidak ada sesi yang dibuat
33. Verifikasi halaman tetap di Verify OTP

### TC-AUTH-OTP-60: Button Verify fallback hilang saat layar Verify OTP dibuka ulang

34. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
35. Ketik `rinahandayani+{runId}-014@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
36. Atur respons Verify OTP menjadi server error 500
37. Ketik 6 digit kode OTP dari email (mail-catcher `rinahandayani+{runId}-014@qwertysystem.net`) pada kotak digit
38. Verifikasi button [Verify] muncul
39. Pulihkan respons Verify OTP menjadi normal
40. Klik tautan [Edit email]
41. Biarkan email `rinahandayani+{runId}-014@qwertysystem.net` tidak berubah, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
42. Verifikasi halaman Verify OTP tampil kembali
43. Verifikasi kotak digit kosong
44. Verifikasi button [Verify] tidak tampil

### TC-AUTH-OTP-177: Verify fallback kosong berulang tidak ikut dihitung dalam batas 5 kali salah

45. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
46. Ketik `sitiprasetyo+{runId}-014@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
47. Atur respons Verify OTP menjadi server error 500
48. Ketik 6 digit kode OTP dari email (mail-catcher `sitiprasetyo+{runId}-014@qwertysystem.net`) pada kotak digit
49. Verifikasi button [Verify] muncul
50. Hapus digit terakhir sehingga hanya 5 kotak terisi
51. Pulihkan respons Verify OTP menjadi normal
52. Klik button [Verify] sebanyak 5 kali berturut-turut
53. Verifikasi setiap klik [Verify] dengan 5 digit menampilkan caption "OTP must not be empty"
54. Isi ulang 6 digit kode benar dari email pada kotak digit, lalu klik button [Verify]
55. Verifikasi kode benar tetap diterima pada percobaan berikutnya (hanya kode salah yang dihitung dalam batas 5 kali)
56. Verifikasi browser dialihkan ke Portal — Product Hub
57. Verifikasi sesi aktif untuk `Siti Prasetyo`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber (49, 56, 60, 69, 177): kode salah murni (49, 69) lebih dulu, lalu fallback (56, 60), dan TC-AUTH-OTP-177 terakhir karena diakhiri login sukses (prinsip 3).
- Pemicu server error 500 pada TC-AUTH-OTP-56, TC-AUTH-OTP-60, dan TC-AUTH-OTP-177 hanya sarana memunculkan button [Verify] fallback; kegagalan 5xx itu sendiri diuji di spec ketahanan Verify (TC-AUTH-OTP-57). Spec ini tidak mengasersi tampilan error 5xx. Pemicu 500 itu memenuhi pengecualian P-2 (`docs/e2e-conventions.md` §3: kegagalan yang dipaksa hanya sebagai pemicu state UI dan bukan objek asersi; intercept dilepas setelah pemicu selesai, S-09). Intercept dipasang pada langkah 24, 36, dan 47. Dilepas pada langkah 29 dan 51 (urutan TC: setelah digit dihapus) dan pada langkah 39 (tepat setelah button [Verify] terverifikasi muncul, sebelum langkah Edit email).
- Langkah 11, 22, 34, dan 45 (buka ulang halaman Request OTP) serta langkah 39 (memulihkan respons Verify OTP lebih awal dari urutan TC-AUTH-OTP-60) adalah langkah penghubung (S-03, S-09). Langkah 2, 12, 23, 35, dan 46 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC.
- Temuan untuk QA: (1) TC-AUTH-OTP-177 langkah 10 menyebut "Isi ulang 6 digit kode benar ... dan klik [Verify]" padahal verifikasi otomatis sudah berjalan pada digit ke-6; TC tidak menyebut apakah button [Verify] masih tampil dan perlu diklik, atau klik tersebut berlebihan. Spec mengikuti TC (langkah 54). (2) TC-AUTH-OTP-177 tidak menyebut apakah button [Verify] tetap tampil setelah klik kosong pertama. (3) TC-AUTH-OTP-60 menulis klik [Request OTP] pada Edit email dengan email tidak berubah; hasilnya (sesi baru sehingga tidak ada cooldown) mengikuti NC-03 tetapi tidak disebut di TC. (4) Post Condition TC-AUTH-OTP-49 a (Failed `Incorrect OTP`) dan TC-AUTH-OTP-56 a (Failed `Empty OTP`) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; pencatatan itu diuji di spec pencatatan Failed Verify OTP (TC-AUTH-OTP-119 dan TC-AUTH-OTP-120).
