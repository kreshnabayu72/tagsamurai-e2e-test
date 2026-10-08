---
name: Auth Reset Password
id: suite-auth-reset-password
description: Test cases derived from tc-reset-password.md for Auth > Reset Password
executionOrder: 1.0
parallel: false
---

# Suite: Auth Reset Password

Suite ini mencakup alur Reset Password secara menyeluruh:
1. Screening form Request Reset Password (Halaman 1), state awal, urutan keyboard Tab, dan navigasi bolak-balik dengan halaman Login with Password.
2. Validasi field Email: wajib diisi, format email valid, batas panjang 120/121 karakter, trim spasi, serta proteksi sanitasi injeksi SQL dan XSS.
3. Evaluasi widget Google reCAPTCHA v2 (web): token belum diselesaikan, token expired, dan penanganan kegagalan layanan captcha.
4. Evaluasi status akun saat Request: email tidak terdaftar (zero-logging), akun dihapus, akun nonaktif (Inactive), status client suspended, dan plan Starter.
5. Alur sukses Request Reset (Happy Path): loading spinner, penerbitan token baru, pengiriman email notifikasi reset dengan tautan aktif 24 jam, dan navigasi ke halaman Email Sent!.
6. Pembatasan laju request (Rate Limiting): proteksi IP rate limit (20 req/jam) dengan penolakan 429 inline alert, kuota 5 kali per email dalam 24 jam dengan penyamaran respons sukses, sliding window, serta cooldown 60 detik.
7. Screening halaman Email Sent! (Halaman 2), countdown timer 60 detik, tombol [Resend email], navigasi kembali, dan penanganan akses tanpa konteks email (fallback text dan section Resend tersembunyi).
8. Alur Resend email: penerbitan token baru, invalidasi otomatis token lama (404 Expired), toast sukses, dan variasi penolakan Resend pada akun yang dimatikan/dihapus/kuota habis.
9. Validasi tautan token reset: pembukaan berulang idempotent tanpa konsumsi token, penolakan token tidak dikenal, token kosong, tautan kedaluwarsa (>24 jam), serta akun yang dinonaktifkan/dihapus (Halaman 404 varian Expired).
10. Screening form Setup New Password (Halaman 3), state awal, atribut aksesibilitas ARIA, urutan keyboard Tab, dan toggle intip independen.
11. Evaluasi reaktif Password Policy checklist 5 butir (panjang 8-72 karakter, kombinasi karakter, larangan spasi, simbol spesial).
12. Validasi form Setup New Password: field wajib diisi, konfirmasi password cocok, penolakan server terhadap pelanggaran policy dan spasi, serta penolakan password baru yang sama dengan password aktif saat ini.
13. Alur sukses Submit New Password: loading spinner, penyimpanan password baru secara atomik, konsumsi token sekali pakai, navigasi ke Halaman Password Reset Successful (Halaman 4), tombol [Go to Login Page], dan pembuktian token consumed membuka Halaman 404 varian Already Used.
14. Verifikasi login pasca-reset: login sukses dengan password baru, penolakan password lama, sifat case-sensitive password baru, dan pengakhiran (terminasi) otomatis semua sesi aktif user di seluruh perangkat.
15. Pemulihan akun terkunci (Account Lock Recovery): pembersihan lock 15 menit, lock 1 jam, lock Requires Reset, dan lock permanen (eskalasi 7 hari) secara langsung setelah reset password berhasil, serta pembersihan counter percobaan gagal dan counter reset per email.
16. Ketahanan terhadap kegagalan (Resilience & Error Handling): penanganan server error 500 dan network timeout pada alur Request, Resend, Validate Link (ErrorState dengan [Try Again]), dan Submit New Password, serta atomicity database rollback.
17. Concurrency dan race condition: pencegahan double-submit pada Request dan Submit, penanganan pembukaan tautan pada 2 tab bersamaan, dan Resend di tab lain saat form Setup New Password terbuka.
18. Perubahan state user di tengah alur: konfirmasi ubah email di Global Settings > User meng-invalidate token aktif email lama, akun dinonaktifkan saat form terbuka, dan token expired saat form terbuka.
19. Pencatatan audit log di dua surface (Activity Log > Session dan User Log): event sukses, event gagal, format atribut IP Address dan Device / Browser, atomicity logging, serta verifikasi kondisi yang tidak dicatat (anti-enumerasi privasi dan zero-logging non-event).
20. Akses halaman reset oleh user yang sudah login (redirect ke Portal untuk form request/email-sent, tetap membuka Setup New Password untuk tautan token).
21. Perilaku khusus aplikasi Android native: form tanpa widget reCAPTCHA, request reset sukses native, dan penanganan App Link.

`parallel: false` karena alasan berikut:
- IP Rate Limiting (E2E-006) membatasi 20 request per jam per IP address; eksekusi paralel dari IP yang sama akan memicu blokir 429 dan merusak spec lainnya.
- Rate Limiting per email (E2E-007, E2E-011) membatasi maksimal 5 request per 24 jam per alamat email.
- Spec pemulihan account lock (E2E-020) memanipulasi lock level, status requires-reset, dan counter login user tertentu.
- Spec audit log (E2E-024, E2E-025) memverifikasi delta jumlah baris dan urutan entri di Activity Log > Session dan User Log; eksekusi paralel akan mencemari log.
- Spec perubahan state user (E2E-023) mengubah email dan status aktif user di Global Settings > User.
- Concurrency spec (E2E-022) menguji persaingan multi-tab untuk akun yang sama sehingga membutuhkan isolasi lingkungan.
