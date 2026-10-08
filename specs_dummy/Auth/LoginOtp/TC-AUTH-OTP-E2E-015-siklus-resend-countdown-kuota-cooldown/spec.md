---
id: TC-AUTH-OTP-E2E-015-siklus-resend-countdown-kuota-cooldown
title: "Siklus Resend Code: Countdown 60s, Kuota 5 Kali, Cooldown 10 Menit, dan State Exhausted"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-77
  - TC-AUTH-OTP-78
  - TC-AUTH-OTP-79
  - TC-AUTH-OTP-80
  - TC-AUTH-OTP-81
  - TC-AUTH-OTP-82
  - TC-AUTH-OTP-83
  - TC-AUTH-OTP-84
  - TC-AUTH-OTP-130
  - TC-AUTH-OTP-181
  - TC-AUTH-OTP-183
coverage:
  web: automated
---

# Siklus Resend Code: Countdown 60s, Kuota 5 Kali, Cooldown 10 Menit, dan State Exhausted

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Wulan Lubis` (`wulanlubis@qwertysystem.net`) profil BASE.
- User `Galih Suryani` (`galihsuryani@qwertysystem.net`) profil BASE.
- User `Citra Hidayati` (`citrahidayati@qwertysystem.net`) profil BASE.
- User `Joko Anggraini` (`jokoanggraini@qwertysystem.net`) profil BASE.
- User `Anisa Gunawan` (`anisagunawan@qwertysystem.net`) profil BASE.
- User `Bagas Ramadhan` (`bagasramadhan@qwertysystem.net`) profil BASE.
- User `Tiara Simanjuntak` (`tiarasimanjuntak@qwertysystem.net`) profil BASE.
- User `Rafi Mulyadi` (`rafimulyadi@qwertysystem.net`) profil BASE.
- Mail-catcher aktif.
- Helper manipulasi waktu server atau mock timer aktif untuk mempercepat uji interval 60 detik dan 10 menit.

## Test Steps

### State A: Countdown 60 detik awal dan format MM:SS

1. Buka halaman Request OTP, masukkan `wulanlubis@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
2. Verifikasi halaman Verify OTP tampil
3. Verifikasi teks Resend berstatus disabled dengan format countdown: "Resend code in (00:59)"
4. Perhatikan penurunan timer detik demi detik terformat rapi dua digit menit dan dua digit detik
5. Simulasikan atau tunggu hingga timer mencapai (00:00)
6. Verifikasi teks berubah menjadi button aktif [Resend code] (State B)

### Eksekusi Resend dan reset countdown

7. Klik button [Resend code]
8. Verifikasi toast banner sukses muncul: "Success, the code has been resent."
9. Verifikasi kode baru diterima di mail-catcher untuk `wulanlubis@qwertysystem.net`
10. Verifikasi tombol seketika kembali ke State A disabled: "Resend code in (00:59)"

### Kuota 5 kali Resend dan transisi ke Cooldown 10 Menit

11. Buka Verify OTP untuk user `jokoanggraini@qwertysystem.net`
12. Lakukan siklus resend ke-1, ke-2, ke-3, dan ke-4 (setiap kali menunggu jeda 60 detik)
13. Verifikasi setiap resend ke-1 hingga ke-4 berhasil dan memicu timer 60 detik baru
14. Pada pembukaan timer setelah resend ke-4, klik button [Resend code] untuk ke-5 kalinya (resend ke-5, menghabiskan kuota maksimum)
15. Verifikasi resend ke-5 berhasil mengirim kode terakhir
16. Verifikasi setelah resend ke-5, teks bertransisi ke mode cooldown 10 menit: "Resend code in (09:59)"
17. Verifikasi tombol dikunci (disabled) selama masa cooldown 10 menit

### Transisi ke State Exhausted setelah Cooldown berakhir

18. Simulasikan pergeseran waktu server melewati masa cooldown 10 menit
19. Verifikasi tombol Resend TIDAK menjadi aktif kembali, melainkan berstatus permanen disabled dengan label "Exhausted"
20. Verifikasi tautan [Edit email] di bawah Subtitle tetap aktif dan dapat diklik sebagai jalan keluar bagi pengguna

### Kegagalan server 5xx tidak memotong kuota Resend

21. Buka Verify OTP untuk `tiarasimanjuntak@qwertysystem.net`, tunggu hingga button [Resend code] aktif
22. Pasang mock intercept status 500 pada endpoint resend
23. Klik button [Resend code]
24. Verifikasi muncul toast error server
25. Verifikasi counter resend server-side tidak bertambah dan pengguna tidak diarahkan ke mode cooldown

### Penolakan direct API request sebelum timer selesai

26. Buka Verify OTP untuk `rafimulyadi@qwertysystem.net` saat countdown masih berjalan (misal di detik 40)
27. Kirim langsung HTTP POST ke endpoint resend tanpa menunggu tombol di UI aktif
28. Verifikasi server menolak dengan HTTP 429 / error kuota
29. Verifikasi di log tercatat penolakan "Resend limit exceeded"

### Preservasi waktu berbasis server vs manipulasi jam lokal browser

30. Pada saat countdown 60 detik sedang berjalan di Verify OTP, ubah jam sistem operasi perangkat/klien 10 menit ke masa depan
31. Muat ulang halaman (refresh) atau amati respons UI
32. Verifikasi penghitungan waktu countdown tetap didasarkan pada sisa waktu server-side dan tidak dapat di-bypass dengan manipulasi clock lokal browser

## Notes

- Arsitektur Resend: Maksimum 5 kali pengiriman ulang per sesi. Jeda antar-resend adalah 60 detik. Setelah resend ke-5, tombol memasuki cooldown 10 menit, setelah itu terkunci permanen pada status "Exhausted" untuk mencegah abuse email.
- Tautan [Edit email] sengaja selalu dipertahankan aktif agar pengguna yang salah memasukkan alamat email atau tidak menerima kode tetap memiliki alur pemulihan.
