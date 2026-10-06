---
id: TC-AUTH-RST-E2E-025-verifikasi-kondisi-tidak-dicatat-log
title: "Verifikasi kondisi yang tidak dicatat pada audit log: email tidak terdaftar, kesalahan input field, submit token tidak dikenal, dan Resend sukses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-104
  - TC-AUTH-RST-105
  - TC-AUTH-RST-126
  - TC-AUTH-RST-137
coverage:
  web: automated
---

# Verifikasi kondisi yang tidak dicatat pada audit log: email tidak terdaftar, kesalahan input field, submit token tidak dikenal, dan Resend sukses

## Prerequisites

- User belum login (guest); alur Reset Password diuji di browser web.
- Admin `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` dapat memantau Activity Log > Session dan User Log.

## Test Steps

### Verifikasi tidak ada pencatatan untuk kesalahan input form awal

1. Lakukan submit pada form Request Reset dengan kondisi:
   - Field Email kosong
   - Field Email format salah
   - Widget Google reCAPTCHA v2 belum dicentang
2. Periksa Activity Log > Session dan User Log
3. Verifikasi tidak ada penambahan entri log baru sama sekali untuk validasi client-side tersebut

### Verifikasi proteksi Anti-Enumerasi (Email tidak terdaftar)

4. Lakukan request reset dengan email yang belum pernah terdaftar di sistem (`belumterdaftar@qwertysystem.net`)
5. Lakukan resend pada akun uji yang tidak ditemukan / dihapus
6. Periksa Activity Log > Session dan User Log
7. Verifikasi sistem TIDAK mencatat log apa pun untuk email yang tidak terdaftar, guna mencegah peretas memanfaatkan log untuk memetakan keberadaan akun

### Verifikasi tidak ada pencatatan untuk Submit dengan Token tidak dikenal

8. Kirimkan permintaan submit password langsung dengan token acak yang tidak dikenal di database
9. Periksa Activity Log > Session dan User Log
10. Verifikasi request ditolak tanpa meninggalkan entri log (zero-logging token invalid)

### Verifikasi kondisi-kondisi lain yang ditetapkan tidak dicatat

11. Lakukan aksi Resend email yang berhasil di bawah batas kuota
12. Lakukan request reset yang ditolak akibat batas IP rate limiting (429)
13. Lakukan submit pada Setup New Password dengan Password kosong, Confirm Password kosong, atau Confirm Password mismatch
14. Periksa kedua surface log (Activity Log Session dan User Log)
15. Verifikasi tidak ada entri log baru yang tercatat untuk satu pun dari kondisi-kondisi di atas

## Notes

- Sesuai PRD §9.4.3 Must NOT 1, §9.8, dan `RSTPWD-LOGIC-04h`, pencatatan log sengaja ditiadakan (zero-logging) untuk request dengan email tidak terdaftar demi melindungi privasi dan mencegah enumerasi pengguna.
- Aksi Resend yang sukses juga tidak dicatat pada audit log karena event operasional yang signifikan adalah saat Request awal dan saat Password berhasil diperbarui (`TC-AUTH-RST-137`).
