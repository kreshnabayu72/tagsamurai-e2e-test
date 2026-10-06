---
id: TC-AUTH-OTP-E2E-013-fallback-tombol-verify-saat-gagal-auto-submit
title: "Fallback Tombol Verify saat Gagal Auto-Submit, Pemulihan Jaringan, dan Reset Tampilan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-56
  - TC-AUTH-OTP-57
  - TC-AUTH-OTP-58
  - TC-AUTH-OTP-59
  - TC-AUTH-OTP-60
  - TC-AUTH-OTP-119
  - TC-AUTH-OTP-131
  - TC-AUTH-OTP-177
coverage:
  web: automated
---

# Fallback Tombol Verify saat Gagal Auto-Submit, Pemulihan Jaringan, dan Reset Tampilan

## Prerequisites

- Mode: mock / network intercept. Digunakan intercept HTTP untuk memanipulasi respons endpoint `POST /auth/otp/verify`.
- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Dewi Firmansyah` (`dewifirmansyah@qwertysystem.net`) profil BASE.
- User `Rizky Nasution` (`rizkynasution@qwertysystem.net`) profil BASE.
- User `Nur Halim` (`nurhalim@qwertysystem.net`) profil BASE.
- User `Agus Pratama` (`aguspratama@qwertysystem.net`) profil BASE.
- User `Rina Handayani` (`rinahandayani@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings aktif untuk memeriksa Activity Log Session.

## Test Steps

### Kemunculan tombol Verify fallback akibat kegagalan server 5xx (NC-10)

1. Buka halaman Verify OTP untuk user `rizkynasution@qwertysystem.net` dengan kode OTP valid yang baru dikirim
2. Verifikasi tombol [Verify] dalam keadaan tersembunyi (Hidden secara default pada alur normal)
3. Pasang mock intercept agar endpoint `POST /auth/otp/verify` mengembalikan status `500 Internal Server Error`
4. Masukkan 6 digit kode OTP lengkap sehingga auto-submit terpanggil
5. Verifikasi auto-submit gagal dan toast error server muncul: "Internal server error. Please try again later."
6. Verifikasi nilai ke-6 kotak digit TIDAK dihapus (tetap tersimpan utuh di layar sesuai NC-10)
7. Verifikasi tombol [Verify] kini bertransisi menjadi terlihat (Visible) dan enabled di bawah kotak digit sebagai tombol cadangan (fallback)
8. Periksa log: verifikasi tercatat entri "Failed" dengan Note "Server error" pada Activity Log Session

### Tombol Verify fallback akibat network timeout / gangguan koneksi (NC-10)

9. Buka halaman Verify OTP untuk `nurhalim@qwertysystem.net`
10. Konfigurasikan mock jaringan untuk mensimulasikan kegagalan koneksi jaringan (network drop/timeout)
11. Masukkan 6 digit kode OTP lengkap
12. Verifikasi auto-submit gagal dan toast network error muncul: "Network connection failed. Please check your internet connection."
13. Verifikasi 6 digit tetap berada di dalam kotak digit
14. Verifikasi tombol [Verify] fallback muncul dalam keadaan aktif
15. Periksa log: verifikasi tercatat entri "Failed" dengan Note "Network error" pada Activity Log Session

### Validasi tombol Verify jika digit belum lengkap

16. Hapus digit terakhir (kotak 6) sehingga kotak digit hanya terisi 5 digit
17. Klik tombol [Verify] fallback
18. Verifikasi verifikasi diblokir di sisi client dan caption error inline "OTP must not be empty" muncul di bawah kotak digit

### Pemulihan sukses via tombol fallback saat server pulih

19. Buka halaman Verify OTP untuk `aguspratama@qwertysystem.net`
20. Picu error 500 sementara hingga tombol [Verify] fallback muncul
21. Hentikan mock intercept (pulihkan backend ke kondisi normal)
22. Pastikan 6 digit kode benar terisi lengkap di kotak digit
23. Klik tombol [Verify] fallback
24. Verifikasi request verifikasi berhasil dikirim ulang dan browser sukses dialihkan ke Product Hub

### Reset tampilan tombol Verify fallback pada navigasi baru

25. Buka halaman Verify OTP untuk `rinahandayani@qwertysystem.net`
26. Picu tombol [Verify] fallback tampil melalui simulasi kegagalan jaringan
27. Klik tautan [Back to Login with Password] lalu navigasikan kembali ke Request OTP dan kirim permintaan baru
28. Verifikasi pada layar Verify OTP yang baru dibuka, tombol [Verify] fallback kembali tersembunyi (Hidden)

## Notes

- Pola interaksi TAG Samurai menyembunyikan tombol [Verify] pada happy path demi mempermudah auto-submit 6 digit.
- Bila auto-submit gagal akibat kendala infrastruktur (5xx atau network error), tombol [Verify] ditampilkan agar pengguna dapat mencoba mengirim ulang tanpa harus mengetik ulang seluruh 6 digit kode (sesuai NC-10).
