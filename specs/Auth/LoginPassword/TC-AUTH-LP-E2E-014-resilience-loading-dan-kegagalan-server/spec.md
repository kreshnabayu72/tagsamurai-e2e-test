---
id: TC-AUTH-LP-E2E-014-resilience-loading-dan-kegagalan-server
title: State loading submit dan penanganan kegagalan server (500, timeout)
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-92
  - TC-AUTH-LP-97
  - TC-AUTH-LP-98
  - TC-AUTH-LP-99
  - TC-AUTH-LP-102
  - TC-AUTH-LP-103
coverage:
  web: automated
---

# State loading submit dan penanganan kegagalan server (500, timeout)

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `jokosusilo@qwertysystem.net` dan `taufikhidayat@qwertysystem.net` aktif dengan password `QaLogin#2026`.
- Mode: mock untuk throttling jaringan, respons status 500, dan timeout.

## Test Steps

### State loading saat submit sedang diproses

1. Buka halaman Login with Password di browser web
2. Masukkan email `jokosusilo@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA
3. Aktifkan simulasi penundaan jaringan (throttling latency) pada endpoint login
4. Klik tombol [Log in]
5. Verifikasi tombol [Log in] menampilkan spinner loading animasi
6. Verifikasi field Email dan field Password dalam keadaan disabled selama proses pengiriman
7. Lepaskan penundaan jaringan dan biarkan respons selesai diproses

### Kesalahan server (HTTP 500) saat submit login

8. Muat ulang halaman Login with Password
9. Masukkan email `jokosusilo@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA
10. Konfigurasikan mock/intersepsi agar request login mengembalikan status HTTP 500 Internal Server Error
11. Klik tombol [Log in]
12. Verifikasi toast error muncul dengan pesan persis: "Error, failed to log in."
13. Verifikasi Alert pesan server tidak tampil di atas tombol [Log in]
14. Verifikasi field Email dan field Password tetap terisi (password tidak dikosongkan)
15. Verifikasi widget reCAPTCHA kembali ke status Unsolved
16. Verifikasi tombol [Log in] kembali enabled sehingga user dapat mencoba lagi

### Timeout jaringan saat submit login

17. Muat ulang halaman Login with Password
18. Masukkan email `jokosusilo@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA
19. Konfigurasikan mock agar request login menggantung tanpa respons hingga batas client timeout
20. Klik tombol [Log in] dan tunggu hingga timeout tercapai
21. Verifikasi toast error "Error, failed to log in." tampil di layar
22. Verifikasi field Email dan Password tetap terisi serta tombol [Log in] kembali enabled

### Kesalahan server saat konfirmasi Agreement

23. Login menggunakan `taufikhidayat@qwertysystem.net` sampai layar Confirm to Continue tampil
24. Centang checkbox persetujuan
25. Konfigurasikan intersepsi jaringan agar request konfirmasi Agreement mengembalikan status 500
26. Klik tombol [Continue ➔]
27. Verifikasi toast error "Error, failed to log in." tampil
28. Verifikasi layar Confirm to Continue tetap terbuka
29. Nonaktifkan intersepsi lalu klik tombol [Continue ➔] kembali
30. Verifikasi request berhasil dan browser menuju Portal — Product Hub

### Pembersihan Alert Danger saat transisi layar dan submit berikutnya

31. Kembali ke halaman Login with Password
32. Masukkan email `jokosusilo@qwertysystem.net` dengan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in]
33. Verifikasi Alert Danger "Incorrect email or password" tampil
34. Kosongkan field Email lalu klik tombol [Log in] (memicu caption inline Email)
35. Verifikasi Alert Danger "Incorrect email or password" langsung hilang dan hanya caption inline "Email must not be empty" yang tampil
36. Masukkan password salah kembali untuk menampilkan Alert Danger
37. Masukkan password yang benar dan selesaikan reCAPTCHA untuk berpindah ke layar Confirm to Continue / Portal
38. Verifikasi saat layar baru terbuka, Alert Danger dari form login sebelumnya tidak terbawa

## Notes

- Sesuai PRD §4.3 FI-AUTHLP-04, pada error jaringan atau kegagalan server (5xx/timeout), field Password dipertahankan dan tidak dikosongkan agar mempermudah user melakukan retry.
- Sesuai NC-14, Alert Danger server langsung hilang ketika submit berikutnya menghasilkan caption error inline.
