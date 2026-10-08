---
id: TC-AUTH-LP-E2E-012-handoff-ke-mfa
title: Handoff ke layar MFA untuk device baru dan anomali lokasi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-71
  - TC-AUTH-LP-72
  - TC-AUTH-LP-73
  - TC-AUTH-LP-74
  - TC-AUTH-LP-142
  - TC-AUTH-LP-155
  - TC-AUTH-LP-158
coverage:
  web: automated
---

# Handoff ke layar MFA untuk device baru dan anomali lokasi

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `watihandayani@qwertysystem.net` aktif; browser yang digunakan merupakan perangkat baru (fingerprint belum tersimpan).
- User `bayunugroho@qwertysystem.net` aktif; simulasi IP / koordinat lokasi berjarak >100 km dari login terakhir.
- User `citradewi@qwertysystem.net` aktif; simulasi IP / geo-location dari negara berbeda dari login terakhir.
- User `gilangramadhan@qwertysystem.net` aktif; bukan login pertama dan tidak idle; login terakhir dari lokasi A; koneksi uji dari lokasi B berjarak >100 km; geo-IP service dimatikan (failure injection).
- User `bagaspermana@qwertysystem.net` aktif; bukan login pertama dan tidak idle; login terakhir dari negara A; pasangan negara A–B sudah trusted untuk user ini (fixture modul MFA); koneksi uji dari negara B berjarak <100 km dari lokasi login terakhir.
- Akses ke mock mailbox atau service inspeksi email untuk verifikasi alert login tak biasa.

## Test Steps

### Handoff ke MFA karena device baru

1. Buka halaman Login with Password di browser web
2. Masukkan email `watihandayani@qwertysystem.net` pada field Email
3. Masukkan password `QaLogin#2026` pada field Password
4. Selesaikan reCAPTCHA
5. Klik tombol [Log in]
6. Verifikasi browser dialihkan ke halaman MFA
7. Verifikasi layar Confirm to Continue tidak tampil
8. Verifikasi sesi penuh belum dibuat dan browser tidak langsung menuju Portal — Product Hub

### Verifikasi pengiriman email alert login tak biasa

9. Buka mailbox atau lakukan pengecekan pada service notifikasi email untuk `watihandayani@qwertysystem.net`
10. Verifikasi terdapat email alert notifikasi login dari perangkat baru / lokasi tidak dikenal yang dikirimkan bersamaan dengan pemicuan MFA

### Handoff ke MFA karena perubahan lokasi >100 km

11. Buka kembali halaman Login with Password
12. Masukkan email `bayunugroho@qwertysystem.net` dan password `QaLogin#2026` dengan IP/lokasi >100 km dari riwayat login sebelumnya
13. Selesaikan reCAPTCHA lalu klik tombol [Log in]
14. Verifikasi browser dialihkan ke halaman MFA dan tidak langsung menuju Portal

### Handoff ke MFA karena perubahan negara

15. Buka kembali halaman Login with Password
16. Masukkan email `citradewi@qwertysystem.net` dan password `QaLogin#2026` dengan IP/lokasi negara berbeda dari riwayat login sebelumnya
17. Selesaikan reCAPTCHA lalu klik tombol [Log in]
18. Verifikasi browser dialihkan ke halaman MFA

### Geo-IP service tidak tersedia: trigger lokasi dilewati (fail-open)

19. Buka kembali halaman Login with Password dengan koneksi dari lokasi B yang berjarak >100 km dari login terakhir, sementara geo-IP service dimatikan (failure injection)
20. Masukkan email `gilangramadhan@qwertysystem.net` dan password `QaLogin#2026`
21. Selesaikan reCAPTCHA lalu klik tombol [Log in]
22. Verifikasi browser menuju Portal — Product Hub tanpa halaman MFA
23. Verifikasi tidak ada error atau toast gagal

### Pasangan negara trusted tidak memicu MFA

24. Buka kembali halaman Login with Password dengan koneksi dari negara B (pasangan negara A–B sudah trusted untuk user ini lewat fixture modul MFA), berjarak <100 km dari lokasi login terakhir
25. Masukkan email `bagaspermana@qwertysystem.net` dan password `QaLogin#2026`
26. Selesaikan reCAPTCHA lalu klik tombol [Log in]
27. Verifikasi browser menuju Portal — Product Hub tanpa halaman MFA
28. Buka kotak masuk email `bagaspermana@qwertysystem.net`
29. Verifikasi tidak ada email alert login tak biasa yang dikirimkan

### Sesi penuh diblokir sebelum verifikasi MFA tuntas (Security)

30. Saat browser berada di halaman MFA untuk `watihandayani@qwertysystem.net`, buka tab baru atau ganti URL langsung ke Portal — Product Hub
31. Tekan Enter
32. Verifikasi sistem menolak akses ke Portal dan mengembalikan browser ke halaman Login karena tahapan MFA belum diselesaikan

## Notes

- Modul Login with Password hanya bertanggung jawab sampai handoff ke MFA (URL redirection) beserta pre-auth token; proses verifikasi OTP / Authenticator diuji di modul MFA.
- Pemicu MFA pada akun terpercaya dipisah antara trigger jarak (>100 km) dan trigger negara berbeda; pasangan negara yang sudah trusted bolak-balik tidak memicu MFA (PRD F-AUTHLP-06, §9.4.2, `auth-foundation.md` §5).
- Bila geo-IP service tidak tersedia, trigger lokasi dilewati (fail-open): login lanjut tanpa MFA tanpa error (`TC-AUTH-LP-155`, PRD §9.2 F-AUTHLP-06, §9.4.2).
