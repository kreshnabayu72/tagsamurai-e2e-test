---
id: TC-AUTH-OTP-E2E-009-recaptcha-gate-web
title: "Proteksi reCAPTCHA Web pada Request OTP: Blokir Submit, Urutan Evaluasi, Reset Widget, dan Caption"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-22
  - TC-AUTH-OTP-23
  - TC-AUTH-OTP-24
  - TC-AUTH-OTP-25
  - TC-AUTH-OTP-26
  - TC-AUTH-OTP-27
coverage:
  web: automated
---

# Proteksi reCAPTCHA Web pada Request OTP: Blokir Submit, Urutan Evaluasi, Reset Widget, dan Caption

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment; widget dapat dibiarkan tidak dicentang atau dicentang sesuai langkah.
- Environment variable: `OTP_PASSWORD` (password user uji yang sudah Activated). Tidak ada password atau token di spec atau fixture.
- Kemampuan teknis: mail-catcher lingkungan uji dapat dibaca untuk alamat yang diketik (membuktikan tidak ada email OTP terkirim).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-22: `Dimas Hidayati` (`dimashidayati+{runId}-009@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-25: `Lestari Anggraini` (`lestarianggraini+{runId}-009@qwertysystem.net`), profil PENDING (Pending Activation, Active ON)
  - TC-AUTH-OTP-26: `Bayu Gunawan` (`bayugunawan+{runId}-009@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-27: `Intan Ramadhan` (`intanramadhan+{runId}-009@qwertysystem.net`), profil BASE
- TC-AUTH-OTP-24 memakai `belumada.user@qwertysystem.net` dan TC-AUTH-OTP-26 memakai `tidakterdaftar.baru@qwertysystem.net`; keduanya tidak ada di Global Settings > User, ditulis literal karena submit-nya ditolak dan tidak ada data tercipta.
- Tidak ada state global yang diubah. Kode OTP tidak diterbitkan oleh satu pun TC di spec ini.

## Test Steps

### TC-AUTH-OTP-22: Request OTP tanpa mencentang reCAPTCHA di web

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Ketik `dimashidayati+{runId}-009@qwertysystem.net` pada field Email
3. Biarkan widget reCAPTCHA tidak dicentang
4. Klik button [Request OTP]
5. Verifikasi caption error di bawah widget reCAPTCHA: "Please verify that you are not a robot"
6. Verifikasi tidak ada email OTP terkirim
7. Verifikasi halaman tetap di Request OTP

### TC-AUTH-OTP-23: Email kosong dan reCAPTCHA kosong: hanya caption Email kosong yang tampil

8. Buka ulang halaman `Auth > Login with OTP > Request OTP`
9. Biarkan field Email kosong dan widget reCAPTCHA tidak dicentang
10. Klik button [Request OTP]
11. Verifikasi caption error di bawah field Email: "Email must not be empty"
12. Verifikasi caption "Please verify that you are not a robot" tidak tampil

### TC-AUTH-OTP-24: Email belum terdaftar dan reCAPTCHA kosong: caption Email belum terdaftar lebih dulu

13. Buka ulang halaman `Auth > Login with OTP > Request OTP`
14. Ketik `belumada.user@qwertysystem.net` pada field Email
15. Biarkan widget reCAPTCHA tidak dicentang
16. Klik button [Request OTP]
17. Verifikasi caption error di bawah field Email: "Email is not registered yet"
18. Verifikasi caption "Please verify that you are not a robot" tidak tampil

### TC-AUTH-OTP-25: reCAPTCHA kosong pada akun belum aktivasi: caption reCAPTCHA lebih dulu

19. Buka ulang halaman `Auth > Login with OTP > Request OTP`
20. Ketik `lestarianggraini+{runId}-009@qwertysystem.net` pada field Email
21. Biarkan widget reCAPTCHA tidak dicentang
22. Klik button [Request OTP]
23. Verifikasi caption error di bawah widget reCAPTCHA: "Please verify that you are not a robot"
24. Verifikasi caption "Your account has not been activated" tidak tampil

### TC-AUTH-OTP-26: Widget reCAPTCHA kembali belum dicentang setelah Request OTP ditolak sehingga wajib dicentang ulang

25. Buka ulang halaman `Auth > Login with OTP > Request OTP`
26. Ketik `tidakterdaftar.baru@qwertysystem.net` pada field Email
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Request OTP]
29. Verifikasi caption "Email is not registered yet" tampil di bawah field Email
30. Verifikasi widget reCAPTCHA kembali ke keadaan belum dicentang
31. Ganti isi field Email menjadi `bayugunawan+{runId}-009@qwertysystem.net`
32. Klik button [Request OTP] tanpa mencentang ulang widget reCAPTCHA
33. Verifikasi caption "Please verify that you are not a robot" tampil di bawah widget reCAPTCHA
34. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-27: Caption reCAPTCHA setelah widget dicentang

35. Buka ulang halaman `Auth > Login with OTP > Request OTP`
36. Ketik `intanramadhan+{runId}-009@qwertysystem.net` pada field Email
37. Biarkan widget reCAPTCHA tidak dicentang
38. Klik button [Request OTP]
39. Verifikasi caption "Please verify that you are not a robot" tampil di bawah widget
40. Centang widget reCAPTCHA "I'm not a robot"
41. Verifikasi caption "Please verify that you are not a robot" hilang

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 22, 23, 24, 25, 26, 27 (sama dengan nomor TC sumber; semua TC adalah alur yang diblokir, TC-AUTH-OTP-27 tanpa submit sukses di akhir).
- Spec ini melewati sekitar 35 langkah (41 langkah) karena enam TC; tiap TC berdiri sendiri lewat buka ulang halaman sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal (batas ukuran bagian 3).
- Langkah 8, 13, 19, 25, dan 35 adalah langkah penghubung (membuka ulang halaman Request OTP agar tiap TC mulai dari field kosong dan widget reCAPTCHA belum dicentang), tanpa asersi (S-03).
- Asersi absence TC-AUTH-OTP-23 butir c dan TC-AUTH-OTP-24 butir c ("tidak ada entri log baru di `Global Settings > Activity Log > Session`"; tidak ada user yang terdampak sehingga tidak ada User Log) dipindah ke E2E-040 (kelas g). Pembagian TC dicatat juga di Notes E2E-040.
- Spec ini tidak membuka Activity Log sehingga akun admin Total Control tidak dipakai. Pencatatan Failed `Captcha not completed` untuk TC-AUTH-OTP-22, 25, dan 26 dicakup oleh E2E-036 lewat TC-AUTH-OTP-116.
- Temuan untuk QA:
  - TC-AUTH-OTP-22, 25, dan 26 punya Post Condition "percobaan dicatat Failed `Captcha not completed`, detail pada TC Logging" tanpa langkah observasi di TC ini; spec tidak mengasersikannya (S-01). Pencatatan itu hanya teramati lewat TC-AUTH-OTP-116 di E2E-036; mohon QA mengonfirmasi rujukan itu sebagai padanannya.
  - TC-AUTH-OTP-23 dan 24 menulis langkah "Biarkan ... widget reCAPTCHA tidak dicentang" lalu klik [Request OTP], sedangkan klaim urutan evaluasi (Email lebih dulu daripada reCAPTCHA) hanya diasersi lewat tidak tampilnya caption reCAPTCHA; spec mengikuti Expected TC.
  - TC-AUTH-OTP-26 Expected a dan b memuat dua kejadian di satu butir (penolakan server lalu klik kedua tanpa centang); spec memisahkannya menjadi dua kelompok `Verifikasi` sesuai langkah masing-masing.
