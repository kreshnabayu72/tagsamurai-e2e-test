---
id: TC-AUTH-OTP-E2E-020-agreement-gate-pemicu-dan-tautan-modal
title: "Agreement Gate: Screening Confirm to Continue, Pemicu Tiga Kondisi, dan Tautan Modal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-09
  - TC-AUTH-OTP-97
  - TC-AUTH-OTP-98
  - TC-AUTH-OTP-99
  - TC-AUTH-OTP-104
  - TC-AUTH-OTP-142
coverage:
  web: automated
---

# Agreement Gate: Screening Confirm to Continue, Pemicu Tiga Kondisi, dan Tautan Modal

## Prerequisites

- Belum login dan session kosong.
- User `Nur Wibowo` (`nurwibowo@qwertysystem.net`) profil FIRST (login pertama kali di platform web).
- User `Idle Tester` (`idletester@qwertysystem.net`) profil IDLE (terakhir login > 30 hari lalu).
- User `Policy Tester` (`policytester@qwertysystem.net`) profil POLICY (ada versi Privacy Policy baru dari Principal).
- Mail-catcher aktif.

## Test Steps

### Screening UI layar Confirm to Continue (profil FIRST)

1. Buka Request OTP untuk `nurwibowo@qwertysystem.net` (profil FIRST)
2. Selesaikan reCAPTCHA dan klik [Request OTP]
3. Masukkan 6 digit kode OTP yang benar dari email
4. Verifikasi sistem TIDAK langsung mengarahkan ke Product Hub, melainkan menampilkan layar "Confirm to Continue"
5. Verifikasi title halaman adalah "Confirm to Continue"
6. Verifikasi terdapat checkbox dengan label persis: "I have read and agree to the Privacy Policy *" dalam keadaan unchecked
7. Verifikasi teks "Privacy Policy" berformat link tautan berwarna interaktif
8. Verifikasi button [Continue ➔] tampil melebar penuh (variant solid, severity primary) dalam keadaan enabled
9. Verifikasi tidak ada elemen kotak digit OTP, field email, tombol Resend, maupun reCAPTCHA di layar ini

### Pemicu 2: Pengguna idle lebih dari 30 hari (profil IDLE)

10. Buka Request OTP untuk `idletester@qwertysystem.net` (profil IDLE)
11. Masukkan kode OTP yang benar
12. Verifikasi sistem mendeteksi masa idle > 30 hari dan menampilkan layar Confirm to Continue

### Pemicu 3: Pembaruan versi Privacy Policy (profil POLICY)

13. Buka Request OTP untuk `policytester@qwertysystem.net` (profil POLICY)
14. Masukkan kode OTP yang benar
15. Verifikasi sistem mendeteksi adanya versi kebijakan baru yang belum disetujui dan menampilkan layar Confirm to Continue

### Buka tautan Privacy Policy tanpa memutus sesi

16. Pada layar Confirm to Continue, klik teks tautan "Privacy Policy"
17. Verifikasi dokumen atau modal Privacy Policy terbuka di browser
18. Tutup dokumen / kembali ke tab form Confirm to Continue
19. Verifikasi state pra-autentikasi tetap bertahan utuh dan form checkbox tetap dapat diisi

### Paritas persetujuan bersama dengan Login with Password

20. Pada layar Confirm to Continue untuk salah satu user uji di atas, centang checkbox "I have read and agree to the Privacy Policy *"
21. Klik button [Continue ➔]
22. Verifikasi user berhasil masuk ke Portal — Product Hub dan persetujuan tersimpan
23. Logout dari sistem, lalu login ulang menggunakan metode `Auth > Login with Password` untuk user yang sama
24. Verifikasi setelah submit password benar, layar Confirm to Continue TIDAK muncul kembali karena persetujuan telah tersimpan permanen di level profil akun

## Notes

- Layar "Confirm to Continue" (Agreement Gate) adalah gerbang persetujuan legal yang dipicu oleh 3 kondisi wajib: (1) Login pertama di web, (2) User idle / tidak login > 30 hari, (3) Principal mempublikasikan versi kebijakan privasi yang lebih tinggi dari versi yang pernah disetujui.
- Status persetujuan bersifat cross-auth: sekali disetujui via OTP, user tidak akan ditanya lagi saat login via Password, dan sebaliknya.
