---
id: TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi
title: "Request OTP dengan Email Valid Diterima: TLD 2 Karakter, Tepat 120 Karakter, Trim Spasi, Plus-addressing, dan Kapitalisasi Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-14
  - TC-AUTH-OTP-15
  - TC-AUTH-OTP-18
  - TC-AUTH-OTP-186
  - TC-AUTH-OTP-187
coverage:
  web: automated
---

# Request OTP dengan Email Valid Diterima: TLD 2 Karakter, Tepat 120 Karakter, Trim Spasi, Plus-addressing, dan Kapitalisasi Campuran

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment.
- Environment variable: `OTP_PASSWORD` (password user uji Activated yang di-seed). Tidak ada password atau token di spec atau fixture.
- Kemampuan teknis: mail-catcher lingkungan uji dapat dibaca untuk tiap alamat yang diketik (membuktikan email OTP diterima) dan dapat menerima domain `qwertysystem.co` (TC-AUTH-OTP-14) serta subdomain dengan label panjang di bawah `qwertysystem.net` (label hingga 63 karakter, TC-AUTH-OTP-15).
- Hook `before` (seeding API) membuat user profil BASE berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-14: `Rina Permata` (`rinapermata+{runId}-007@qwertysystem.co`), domain dengan TLD tepat 2 karakter
  - TC-AUTH-OTP-15: `Hendra Fitriani`, alamat mengikuti pola TC (`hendrafitriani@` + label huruf `a` + `.` + label 44 huruf `b` + `.qwertysystem.net`, tepat 120 karakter) dengan suffix `+{runId}-007` disisipkan di akhir local-part (`hendrafitriani+{runId}-007@...`); jumlah huruf `a` pada label pertama (43 pada TC) dikurangi sepanjang suffix `+{runId}-007` dan dihitung saat seeding sehingga total alamat tepat 120 karakter, local-part tetap maksimal 64 karakter, dan tiap label domain maksimal 63 karakter
  - TC-AUTH-OTP-18: `Maya Susanti` (`mayasusanti+{runId}-007@qwertysystem.net`)
  - TC-AUTH-OTP-186: `Wawan Setiadi` (`wawansetiadi+otp-{runId}-007@qwertysystem.net`), bentuk plus-addressing
  - TC-AUTH-OTP-187: `Gita Permatasari` (`gitapermatasari+{runId}-007@qwertysystem.net`, disimpan dalam huruf kecil)
- Tidak ada state global yang diubah. Kode OTP yang diterbitkan dibiarkan tidak dipakai (tidak ada login selesai); user dihapus di hook `after`.

## Test Steps

### TC-AUTH-OTP-14: Request OTP dengan email yang memiliki tepat 2 karakter setelah titik diterima

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Ketik `rinapermata+{runId}-007@qwertysystem.co` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi tidak ada caption error format email
6. Verifikasi toast sukses "Success, the code has been sent." tampil
7. Verifikasi halaman Verify OTP tampil
8. Verifikasi Subtitle "Enter the 6-digit code sent to: rinapermata+{runId}-007@qwertysystem.co"

### TC-AUTH-OTP-15: Request OTP dengan email tepat 120 karakter diterima tanpa caption batas panjang

9. Buka halaman `Auth > Login with OTP > Request OTP` di browser
10. Ketik alamat email milik `Hendra Fitriani` yang tepat 120 karakter pada field Email
11. Centang widget reCAPTCHA "I'm not a robot"
12. Klik button [Request OTP]
13. Verifikasi tidak ada caption "Max. 120 characters"
14. Verifikasi toast sukses "Success, the code has been sent." tampil
15. Verifikasi halaman Verify OTP tampil

### TC-AUTH-OTP-18: Request OTP dengan email berspasi di awal dan akhir diproses setelah di-trim

16. Buka halaman `Auth > Login with OTP > Request OTP` di browser
17. Ketik spasi, lalu `mayasusanti+{runId}-007@qwertysystem.net`, lalu spasi pada field Email
18. Centang widget reCAPTCHA "I'm not a robot"
19. Klik button [Request OTP]
20. Verifikasi toast sukses "Success, the code has been sent." tampil
21. Verifikasi halaman Verify OTP tampil
22. Verifikasi email OTP diterima di `mayasusanti+{runId}-007@qwertysystem.net` di mail-catcher

### TC-AUTH-OTP-186: Request OTP dengan email plus-addressing diterima

23. Buka halaman `Auth > Login with OTP > Request OTP` di browser
24. Ketik `wawansetiadi+otp-{runId}-007@qwertysystem.net` pada field Email
25. Centang widget reCAPTCHA "I'm not a robot"
26. Klik button [Request OTP]
27. Verifikasi tidak ada caption "Email format is incorrect"
28. Verifikasi toast sukses "Success, the code has been sent." tampil
29. Verifikasi browser berpindah ke halaman Verify OTP
30. Verifikasi email OTP berisi kode 6 digit diterima di `wawansetiadi+otp-{runId}-007@qwertysystem.net` di mail-catcher

### TC-AUTH-OTP-187: Request OTP dengan kapitalisasi email campuran menemukan akun yang sama

31. Buka halaman `Auth > Login with OTP > Request OTP` di browser
32. Ketik `GitaPermatasari+{runId}-007@QwertySystem.net` pada field Email
33. Centang widget reCAPTCHA "I'm not a robot"
34. Klik button [Request OTP]
35. Verifikasi caption "Email is not registered yet" tidak tampil
36. Verifikasi browser berpindah ke halaman Verify OTP
37. Verifikasi email OTP berisi kode 6 digit diterima di `gitapermatasari+{runId}-007@qwertysystem.net` (akun yang sama dalam bentuk huruf kecil) di mail-catcher

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 14, 15, 18, 186, 187 (semua alur sukses; tidak ada alur diblokir di spec ini karena validasi yang diblokir ada di E2E-006). Urutan sama dengan urutan bagian 3a sumber.
- Langkah 9, 16, 23, dan 31 membuka ulang halaman Request OTP agar tiap TC mulai dari field kosong dan widget reCAPTCHA belum dicentang; langkah penghubung tanpa asersi (S-03). Tiap TC memakai email berbeda sehingga sesi email-request antar TC tidak saling menolak.
- Spec ini 37 langkah (melewati smell sekitar 35) karena lima TC alur sukses yang masing-masing berdiri sendiri lewat buka ulang halaman dengan email berbeda; semuanya satu topik (email valid diterima), satu akun tanpa login, tanpa harness selain mail-catcher, dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Tidak ada pengecualian P-1, P-2, atau P-3 yang dipakai.
- Temuan untuk QA:
  - TC-AUTH-OTP-14 memakai domain `qwertysystem.co` (berbeda dari `qwertysystem.net` pada TC lain) tanpa menyebut bahwa domain itu menerima email di mail-catcher; spec mensyaratkan (lihat Prerequisites) mail-catcher dapat menerima domain itu atau seeding memakai domain yang setara dengan TLD 2 karakter.
  - TC-AUTH-OTP-15 menyebut alamat literal tanpa suffix `{runId}`; spec menyisipkan suffix `+{runId}-007` agar user unik per run dan mengurangi jumlah huruf `a` pada label pertama agar total tetap 120 karakter. Bila QA menghendaki alamat literal persis TC, user harus di-seed dengan alamat itu dan run paralel tidak boleh memakainya bersamaan.
  - TC-AUTH-OTP-14 dan 15 tidak membaca email di mail-catcher walau precondition-nya menyebut; spec mengikuti Expected TC (tidak ada Verifikasi email di dua TC itu).
