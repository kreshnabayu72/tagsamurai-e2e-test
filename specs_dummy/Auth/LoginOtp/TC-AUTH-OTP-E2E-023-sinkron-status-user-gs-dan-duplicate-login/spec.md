---
id: TC-AUTH-OTP-E2E-023-sinkron-status-user-gs-dan-duplicate-login
title: "Sinkronisasi Status User Global Settings dan Deteksi Duplicate Login Attempt"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-138
  - TC-AUTH-OTP-139
  - TC-AUTH-OTP-140
  - TC-AUTH-OTP-143
  - TC-AUTH-OTP-175
  - TC-AUTH-OTP-176
coverage:
  web: automated
---

# Sinkronisasi Status User Global Settings dan Deteksi Duplicate Login Attempt

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Inactive Recovery` (`inactiverecover@qwertysystem.net`) awalnya profil INACTIVE.
- User `Pending Activation` (`pendingactivation@qwertysystem.net`) awalnya profil PENDING.
- User `Email Change Tester` (`emailchange@qwertysystem.net`) profil BASE.
- User `Concurrent Tester` (`concurrent@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings aktif untuk memanipulasi entitas User.

## Test Steps

### Pemulihan instan saat akun diaktifkan kembali di Global Settings

1. Pada Global Settings > User via sesi admin, ubah status user `Inactive Recovery` dari Inactive menjadi Active (Toggle ON)
2. Buka halaman Request OTP di browser klien uji
3. Masukkan email `inactiverecover@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
4. Verifikasi request diterima seketika tanpa jeda delay atau caching yang menghambat
5. Verifikasi toast sukses pengiriman kode tampil dan halaman Verify OTP terbuka

### Akun baru diaktivasi langsung dapat menggunakan Login with OTP

6. Pada Global Settings > User, ubah status user `Pending Activation` menjadi Activated
7. Masukkan email `pendingactivation@qwertysystem.net` ke Request OTP
8. Verifikasi sistem tidak lagi menampilkan "Your account has not been activated yet", melainkan langsung menerbitkan kode OTP

### Sinkronisasi perubahan alamat email user di Global Settings

9. Pada Global Settings > User, ganti alamat email user dari `emailchange@qwertysystem.net` menjadi `emailnew@qwertysystem.net`
10. Pada halaman Request OTP, coba masukkan alamat email lama `emailchange@qwertysystem.net`
11. Verifikasi submit ditolak dengan caption "Email is not registered yet"
12. Masukkan alamat email baru `emailnew@qwertysystem.net`
13. Verifikasi request diterima dan kode OTP dikirimkan ke alamat email baru

### Deteksi percobaan login ganda dan integrasi Session Management (EC-50, TC-175, TC-176)

14. Login sebagai `concurrent@qwertysystem.net` di Peramban A hingga masuk ke Product Hub
15. Di Peramban B, buka Request OTP dan masukkan kode OTP 6 digit yang valid untuk `concurrent@qwertysystem.net`
16. Verifikasi sistem menampilkan dialog "Duplicate Login Attempt" sebelum sesi baru dibuat (karena sesi aktif sudah ada pada platform yang sama)
17. Di sesi admin Total Control: buka `Global Settings > Activity Log > Session`
18. Verifikasi TIDAK ADA entri log baru yang ditulis saat dialog Duplicate Login Attempt ditampilkan (sesuai PRD §9.8)
19. Pada Peramban B, klik tombol [Cancel] pada dialog Duplicate Login Attempt
20. Verifikasi dialog tertutup, tidak ada sesi baru yang dibuat, dan tetap TIDAK ADA entri log baru yang ditulis
21. Buka kembali alur verifikasi kode di Peramban B hingga dialog "Duplicate Login Attempt" muncul kembali
22. Pada Peramban B, klik tombol [Confirm] pada dialog Duplicate Login Attempt
23. Verifikasi sesi aktif di Peramban A seketika berakhir (terputus) saat melakukan aksi berikutnya
24. Verifikasi Peramban B berhasil membuat sesi baru dan dialihkan ke Product Hub
25. Di sesi admin Total Control: periksa `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail (Concurrent Tester) > User Log`
26. Verifikasi tercatat tepat SATU entri baru dengan Activity "Login", Status "Success", dan Method/Note "Login with OTP"

### Pencabutan sesi seketika saat akun dinonaktifkan oleh Admin (Real-time termination)

27. Pada sesi login aktif milik `concurrent@qwertysystem.net`, buka halaman modul di dalam portal
28. Melalui akun admin Total Control di tab lain, matikan Toggle Active user tersebut menjadi OFF
29. Pada browser user aktif, lakukan aksi klik atau refresh halaman
30. Verifikasi sesi user seketika dicabut (terminated), token dinyatakan invalid, dan user diarahkan kembali ke halaman login

## Notes

- Status akun (Active/Inactive, Activated, Email) bersumber langsung dari database otoritatif Global Settings tanpa stale-caching berdurasi panjang pada lapisan autentikasi.
- Kebijakan penanganan sesi ganda dikelola secara terpusat oleh layanan `session-management` platform.
