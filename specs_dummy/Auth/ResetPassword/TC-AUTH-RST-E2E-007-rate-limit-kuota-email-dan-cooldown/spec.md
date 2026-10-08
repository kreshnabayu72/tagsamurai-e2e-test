---
id: TC-AUTH-RST-E2E-007-rate-limit-kuota-email-dan-cooldown
title: "Pembatasan laju reset per email: cooldown 60 detik, kuota 5 kali per 24 jam, penyamaran respons, dan sliding window"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-29
  - TC-AUTH-RST-30
  - TC-AUTH-RST-31
  - TC-AUTH-RST-32
  - TC-AUTH-RST-34
  - TC-AUTH-RST-38
  - TC-AUTH-RST-139
coverage:
  web: automated
---

# Pembatasan laju reset per email: cooldown 60 detik, kuota 5 kali per 24 jam, penyamaran respons, dan sliding window

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan akses mail-catcher.
- Akun uji terkonfigurasi:
  - `dewilestari@qwertysystem.net` (riwayat 0 request).
  - `fajarnugroho@qwertysystem.net` (fixture disetel memiliki 4 atau 5 request dalam 24 jam terakhir).
  - `sitirahmawati@qwertysystem.net` (tanpa riwayat request).
  - `tonokurniawan@qwertysystem.net` (fixture dapat diubah status aktif/inaktif dan riwayat request).
- Admin pemantau log `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` dapat melihat Activity Log Session dan User Log.

## Test Steps

### Perilaku Request ulang di dalam cooldown 60 detik (No-Op)

1. Buka halaman Reset Password di browser web
2. Masukkan email "dewilestari@qwertysystem.net" lalu selesaikan reCAPTCHA
3. Klik tombol [Reset Password]
4. Verifikasi browser menuju halaman Email Sent! dan email reset pertama masuk ke mail-catcher
5. Buka tab browser baru dan langsung akses kembali URL `/reset-password` sebelum 60 detik berlalu
6. Masukkan kembali email "dewilestari@qwertysystem.net", selesaikan reCAPTCHA, lalu klik [Reset Password]
7. Verifikasi browser tetap menampilkan halaman Email Sent! seperti biasa
8. Verifikasi pada mail-catcher tidak ada email reset baru yang dikirimkan (email kedua tidak terbit)
9. Verifikasi token reset pertama tetap aktif dan tidak berubah
10. Verifikasi counter percobaan per email tidak bertambah akibat request di dalam cooldown

### Batas maksimal 5 kali dalam 24 jam (Request ke-5 berhasil)

11. Lakukan request reset secara bertahap setelah cooldown hingga mencapai request ke-5 untuk akun `dewilestari@qwertysystem.net`
12. Verifikasi request ke-5 berhasil diproses, token baru terbit, dan email ke-5 terkirim ke mail-catcher

### Request ke-6 melebihi batas 5 kali dalam 24 jam (Penyamaran respons)

13. Gunakan akun `fajarnugroho@qwertysystem.net` yang telah disetel mencapai 5 kali percobaan dalam 24 jam
14. Buka halaman Reset Password dan masukkan email "fajarnugroho@qwertysystem.net"
15. Selesaikan reCAPTCHA lalu klik [Reset Password]
16. Verifikasi UI menampilkan respons yang persis identik dengan sukses: browser dialihkan ke halaman Email Sent! dengan subtitle memuat email Fajar Nugroho
17. Verifikasi pada mail-catcher tidak ada email reset baru yang dikirimkan
18. Buka Activity Log Session dan User Log menggunakan sesi admin
19. Verifikasi tercatat entri log baru dengan Activity "Reset Password", Status "Failed", dan Note "Too many reset attempts"

### Evaluasi kuota per email pada akun Inactive

20. Setel akun Inactive `tonokurniawan@qwertysystem.net` telah melampaui kuota 5 request dalam 24 jam
21. Kirimkan request reset untuk email Tono Kurniawan
22. Verifikasi evaluasi kuota per email mendahului evaluasi inactive: UI tetap menampilkan Email Sent! (disamarkan) dan log mencatat Note "Too many reset attempts", bukan "Account is inactive"

### Isolasi kuota per email antar user

23. Buka halaman Reset Password dan masukkan email "sitirahmawati@qwertysystem.net" (user tanpa riwayat request)
24. Selesaikan reCAPTCHA lalu klik [Reset Password]
25. Verifikasi request Siti Rahmawati berhasil diproses normal dan email reset terkirim, membuktikan kuota rate limit per email terisolasi penuh antar akun

### Pemulihan kuota dengan mekanisme Sliding Window 24 jam

26. Amati akun `fajarnugroho@qwertysystem.net` saat percobaan tertua melewati usia 24 jam
27. Kirimkan request reset baru untuk Fajar Nugroho
28. Verifikasi request berhasil diproses, email reset terkirim, dan token aktif baru diterbitkan

### Precedence pengecekan status akun terhadap cooldown (TC-139)

29. Setel ulang akun `tonokurniawan@qwertysystem.net` berstatus Active dengan Request reset berhasil kurang dari 60 detik lalu sehingga cooldown 60 detik masih berjalan (fixture BE)
30. Melalui sesi admin, nonaktifkan akun Tono (ubah status menjadi Inactive, fixture BE)
31. Buka halaman Reset Password, masukkan "tonokurniawan@qwertysystem.net", selesaikan reCAPTCHA, lalu klik [Reset Password] (Request berada di dalam cooldown)
32. Verifikasi caption inline "Your account is inactive" tampil di bawah field Email dan browser tetap di halaman Reset Password (bukan Email Sent!)
33. Verifikasi tidak ada email reset baru di mail-catcher dan tercatat entri log baru dengan Status Failed dan Note "Account is inactive"
34. Pada kondisi yang sama (akun Inactive, cooldown belum lewat), picu kembali Resend untuk email yang sama
35. Verifikasi toast sukses tampil tanpa token/email baru serta tercatat entri log Failed / "Account is inactive", membuktikan pengecekan status akun mendahului cooldown

## Notes

- Sesuai PRD §9.2 F-AUTHRST-06, `RSTPWD-LOGIC-04b`, dan `RSTPWD-LOGIC-04c`, saat batas 5 request per 24 jam terlampaui, sistem menyamarkan respons di UI agar identik dengan alur sukses untuk mencegah enumerasi batas akun, namun mencatat status Failed dengan Note "Too many reset attempts".
- Sesuai keputusan NC-01, request di dalam cooldown 60 detik merupakan no-op yang tidak menerbitkan token baru, tidak mengirim email baru, dan tidak menambah counter.
- Sesuai PRD §9.4.2 baris 38 (`TC-AUTH-RST-139`), pengecekan status akun (Inactive) dilakukan lebih dulu daripada cooldown: akun Inactive tetap ditolak dengan caption dan log "Account is inactive" meskipun berada di dalam cooldown.
- Tambahan `TC-AUTH-RST-139` menutup gap coverage yang sebelumnya belum tercakup spec (GAP-RST-E2E-001).