---
id: TC-AUTH-LP-E2E-020-concurrency-dan-race-condition
title: Concurrency dan race condition submit kredensial salah
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-146
  - TC-AUTH-LP-147
  - TC-AUTH-LP-150
coverage:
  web: automated
---

# Concurrency dan race condition submit kredensial salah

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `fitrihandayani@qwertysystem.net` berstatus aktif dengan hitungan gagal 0 (web).
- User `galihpratama@qwertysystem.net` berstatus aktif dengan hitungan gagal 0 (web).
- User `intanpermata@qwertysystem.net` berstatus aktif dengan hitungan gagal 0 (web).
- Kemampuan membuka multi-tab atau multi-context browser dalam sesi otomasi.

## Test Steps

### Akumulasi counter kegagalan konsisten lintas dua tab browser

1. Buka halaman Login with Password pada dua tab terpisah (Tab A dan Tab B)
2. Pada Tab A: Masukkan email `fitrihandayani@qwertysystem.net` dan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (gagal ke-1)
3. Verifikasi Alert Danger "Incorrect email or password" tampil pada Tab A
4. Pada Tab B: Masukkan email `fitrihandayani@qwertysystem.net` dan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (gagal ke-2)
5. Verifikasi Alert Danger "Incorrect email or password" tampil pada Tab B
6. Kembali ke Tab A: Masukkan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (gagal ke-3)
7. Verifikasi Tab A menampilkan Alert Danger: "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}."
8. Pada Tab B: Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
9. Verifikasi Tab B langsung menampilkan Alert Danger lock 15 menit dan menolak login, membuktikan counter kegagalan terakumulasi konsisten di sisi server lintas tab

### Tiga submit salah bersamaan dari tiga tab menghasilkan tepat satu lock

10. Buka halaman Login with Password pada tiga tab (Tab 1, Tab 2, dan Tab 3)
11. Pada setiap tab, masukkan email `galihpratama@qwertysystem.net`, password salah `SalahPass#1`, dan selesaikan reCAPTCHA
12. Kirimkan klik tombol [Log in] pada ketiga tab secara bersamaan (selisih waktu kurang dari 1 detik)
13. Periksa respons pada setiap tab:
    - Verifikasi tepat 1 tab menampilkan Alert Danger lock 15 menit ("Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}.")
    - Verifikasi 2 tab lainnya menampilkan Alert Danger "Incorrect email or password"
14. Pada salah satu tab, coba masukkan password yang benar `QaLogin#2026`
15. Verifikasi login ditolak dengan pesan lock 15 menit aktif dan sistem tidak menghasilkan multi-lock atau lock tingkat 1 jam

### Klik ganda cepat pada tombol [Log in] dengan password salah

16. Buka kembali halaman Login with Password
17. Masukkan email `intanpermata@qwertysystem.net` dan password salah `SalahPass#1`, selesaikan reCAPTCHA
18. Lakukan klik ganda cepat (double-click) pada tombol [Log in]
19. Verifikasi satu Alert Danger "Incorrect email or password" tampil
20. Lakukan submit password salah berikutnya (percobaan ke-2)
21. Verifikasi Alert Danger "Incorrect email or password" tampil dan akun belum terkunci
22. Lakukan submit password salah berikutnya (percobaan ke-3)
23. Verifikasi akun baru terkunci 15 menit pada percobaan ini, membuktikan double-click sebelumnya hanya dihitung sebagai 1 kali percobaan gagal

## Notes

- Sesuai PRD §9.4.2 D6 dan §9.6, atomisitas transaksi counter menjamin race condition antar request tidak menyebabkan lonjakan counter ganda yang tidak sah.
- Double-submit guard pada tombol login mencegah pengiriman request paralel dari satu interaksi pengguna.
