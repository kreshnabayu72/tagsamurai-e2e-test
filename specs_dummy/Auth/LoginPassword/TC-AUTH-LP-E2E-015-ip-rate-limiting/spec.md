---
id: TC-AUTH-LP-E2E-015-ip-rate-limiting
title: Pembatasan laju request per IP (20 req/menit) dan pemulihan otomatis
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-101
  - TC-AUTH-LP-104
coverage:
  web: automated
---

# Pembatasan laju request per IP (20 req/menit) dan pemulihan otomatis

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- Batas laju IP Rate Limiting pada endpoint login: 20 request per menit per IP (semua request dihitung, baik valid maupun gagal).
- Email tidak terdaftar `tidakada@qwertysystem.net` dan akun `vinamelati@qwertysystem.net` (sedang dalam status terkunci 1 jam).
- Lingkungan uji yang dapat memanipulasi jendela waktu atau menghitung kuota per menit.

## Test Steps

### Pemicuan batas 20 request per menit per IP

1. Buka halaman Login with Password di browser web
2. Dari alamat IP yang sama, kirimkan 20 kali submit login berturut-turut dalam kurun waktu 1 menit menggunakan email `tidakada@qwertysystem.net` dan password `QaLogin#2026` dengan reCAPTCHA diselesaikan
3. Verifikasi pada setiap submit ke-1 sampai ke-20 sistem merespons normal dengan caption "Email is not registered yet"
4. Kirimkan submit ke-21 dalam menit kalender yang sama
5. Verifikasi Alert Danger tampil di atas tombol [Log in] dengan pesan persis: "Too many requests. Please try again later."
6. Verifikasi field Email, Password, dan tombol [Log in] tetap berstatus enabled (tidak dikunci dari UI)

### Pemulihan otomatis setelah jeda jendela 1 menit

7. Tunggu hingga jendela waktu 1 menit berlalu (cooldown habis)
8. Masukkan kembali email `tidakada@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
9. Verifikasi pembatasan berakhir secara otomatis dan sistem kembali menampilkan caption "Email is not registered yet" (Alert 429 tidak tampil lagi)

### Percobaan saat akun terkunci tetap dihitung ke kuota IP rate limit

10. Dari IP yang sama, kirimkan 20 kali submit login dalam 1 menit menggunakan akun `vinamelati@qwertysystem.net` yang sedang terkunci 1 jam
11. Verifikasi pada submit ke-1 sampai ke-20 sistem menampilkan Alert lock 1 jam
12. Kirimkan submit ke-21 dalam jendela menit yang sama
13. Verifikasi Alert Danger berubah menjadi: "Too many requests. Please try again later."
14. Verifikasi Alert pesan lock 1 jam tertimpa oleh Alert rate limit IP, membuktikan percobaan saat akun terkunci tetap memakan kuota IP rate limit

## Notes

- Sesuai NC-03 dan NC-04, batas rate limit IP adalah 20 request per menit per IP dan seluruh request (termasuk yang ditolak karena lock) dihitung ke kuota IP rate limiting (`AUTHLP-LOGIC-02k`).
