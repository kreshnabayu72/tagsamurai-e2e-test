---
id: TC-AUTH-OTP-E2E-021-agreement-gate-submit-dan-token-ttl
title: "Agreement Gate: Validasi Submit, Penolakan Tanpa Centang, TTL Token 10 Menit, dan Abandoned"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-72
  - TC-AUTH-OTP-74
  - TC-AUTH-OTP-102
  - TC-AUTH-OTP-103
  - TC-AUTH-OTP-105
  - TC-AUTH-OTP-106
  - TC-AUTH-OTP-107
  - TC-AUTH-OTP-108
  - TC-AUTH-OTP-109
  - TC-AUTH-OTP-110
  - TC-AUTH-OTP-111
  - TC-AUTH-OTP-126
  - TC-AUTH-OTP-128
  - TC-AUTH-OTP-132
coverage:
  web: automated
---

# Agreement Gate: Validasi Submit, Penolakan Tanpa Centang, TTL Token 10 Menit, dan Abandoned

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Taufik Susanti` (`taufiksusanti@qwertysystem.net`) profil POLICY (memicu Agreement Gate).
- User `Budi Agreement` (`budiagree@qwertysystem.net`) profil POLICY.
- User `Abandon Tester` (`abandontest@qwertysystem.net`) profil FIRST.
- Akun admin Total Control Global Settings aktif untuk memeriksa entri audit log.

## Test Steps

### Klik Continue tanpa mencentang checkbox

1. Selesaikan verifikasi OTP untuk `taufiksusanti@qwertysystem.net` hingga layar Confirm to Continue tampil
2. Verifikasi button [Continue ➔] dalam keadaan enabled meskipun checkbox belum dicentang
3. Klik button [Continue ➔] tanpa mencentang checkbox
4. Verifikasi aksi diblokir di sisi klien dan caption error inline muncul di bawah checkbox: "You need to agree to the Privacy Policy to continue"
5. Verifikasi tidak ada pengalihan halaman

### Submit persetujuan yang sah

6. Klik checkbox "I have read and agree to the Privacy Policy *" sehingga tanda centang aktif
7. Verifikasi caption error inline seketika hilang
8. Klik button [Continue ➔]
9. Verifikasi persetujuan berhasil dikirim ke server dan pengguna dialihkan ke Portal — Product Hub
10. Periksa audit trail: tercatat entri login "Success" di User Log dan Activity Log Session

### Refresh halaman (F5) pada layar Confirm to Continue (NC-08)

11. Buka kembali layar Confirm to Continue untuk `budiagree@qwertysystem.net`
12. Tekan tombol F5 / muat ulang browser saat token pra-autentikasi masih dalam batas 10 menit
13. Verifikasi halaman TETAP bertahan di Confirm to Continue tanpa harus mengulang verifikasi OTP

### Akses URL langsung /login/confirm-agreement tanpa token (NC-08)

14. Buka tab baru yang bersih tanpa state token
15. Masukkan langsung URL `/login/confirm-agreement`
16. Verifikasi sistem mengalihkan browser ke halaman `Auth > Login with Password` (`/login`)

### Kedaluwarsa token pra-autentikasi (TTL 10 menit) dan Abandoned (NC-08)

17. Selesaikan OTP hingga mencapai layar Confirm to Continue untuk `abandontest@qwertysystem.net`
18. Simulasikan penutupan browser atau biarkan token pra-autentikasi melewati batas TTL 10 menit
19. Bila dicoba submit setelah 10 menit, verifikasi server menolak token dan mengarahkan kembali ke login
20. Periksa audit trail di User Log / Activity Log Session: verifikasi TIDAK ada penambahan baris baru di kedua surface untuk kasus token kedaluwarsa atau layar ditinggalkan tanpa klik (sesuai PRD §9.8 dan TC-107, TC-109, TC-111); penolakan 'Consent not given' hanya dicatat saat tombol Continue diklik tanpa centang (langkah 3)

### Modifikasi token (Tampering) dan kegagalan submit

21. Buka layar Confirm to Continue, manipulasi token pra-autentikasi di storage/payload menjadi nilai acak
22. Centang checkbox dan klik [Continue ➔]
23. Verifikasi request ditolak oleh backend (HTTP 401 Unauthorized)
24. Lakukan pengujian double-click cepat pada [Continue ➔]: verifikasi tombol mematikan submit ganda
25. Simulasikan error server 500 saat submit: verifikasi toast error muncul dan checkbox tetap tercentang

## Notes

- Token pra-autentikasi (preAuthToken) untuk gerbang persetujuan memiliki masa hidup 10 menit. Sesuai PRD §9.8 dan TC-AUTH-OTP-107/109/111, jika pengguna mengabaikan layar persetujuan hingga token kedaluwarsa atau menutup halaman, sistem tidak mencatat entri log baru. Penulisan log Failed dengan Note `Consent not given` hanya terjadi saat pengguna secara eksplisit mengklik tombol [Continue ➔] tanpa mencentang checkbox (TC-AUTH-OTP-102 dan TC-AUTH-OTP-126).
- Tombol `[Continue ➔]` berstatus enabled secara visual saat form dimuat; klik tanpa centang mengirim permintaan ke server yang ditolak dengan kode 422 dan caption `You need to agree to the Privacy Policy to continue`.
