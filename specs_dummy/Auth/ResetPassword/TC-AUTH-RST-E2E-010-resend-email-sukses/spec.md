---
id: TC-AUTH-RST-E2E-010-resend-email-sukses
title: "Resend email reset setelah cooldown: pembatalan token lama, penerbitan token baru, dan toast sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-42
  - TC-AUTH-RST-43
  - TC-AUTH-RST-44
  - TC-AUTH-RST-57
  - TC-AUTH-RST-125
coverage:
  web: automated
---

# Resend email reset setelah cooldown: pembatalan token lama, penerbitan token baru, dan toast sukses

## Prerequisites

- User belum login (guest); telah melakukan request reset untuk `budisantoso@qwertysystem.net`.
- Halaman Email Sent! terbuka dengan konteks email aktif.
- Token reset pertama (Token A) telah tercatat di database dan tautannya tertangkap di mail-catcher.
- Durasi cooldown 60 detik telah berakhir sehingga tombol [Resend email] berstatus enabled.

## Test Steps

### Eksekusi Resend dan Toast konfirmasi

1. Pada halaman Email Sent!, klik tombol [Resend email] yang telah enabled
2. Verifikasi toast notifikasi sukses muncul di kanan bawah dengan pesan: "Success, email has been sent to budisantoso@qwertysystem.net."
3. Verifikasi tombol [Resend email] kembali disabled dan countdown timer me-restart hitungan mundur dari "Resend in 1:00"
4. Buka database token reset
5. Verifikasi Token A (token lama) berubah status menjadi `invalidated`
6. Verifikasi diterbitkan Token B (token baru) dengan status `active` dan masa berlaku 24 jam ke depan

### Pembuktian tautan lama (Token A) menjadi tidak berlaku

7. Salin tautan reset lama yang memuat Token A dari mail-catcher
8. Buka tautan lama tersebut pada tab browser baru
9. Verifikasi browser menampilkan Halaman 404 varian Expired dengan title "Reset Link Expired"
10. Verifikasi form Setup New Password tidak dirender untuk Token A

### Pembuktian tautan baru (Token B) berfungsi dengan baik

11. Buka email reset kedua yang baru saja masuk di mail-catcher
12. Salin tautan reset baru yang memuat Token B
13. Buka tautan baru tersebut pada browser
14. Verifikasi halaman Setup New Password berhasil terbuka dengan normal (`/setup-new-password?token=...`)

### Penegakan aturan Cooldown di server (Bypass UI Prevention)

15. Sebelum 60 detik berlalu dari Resend sebelumnya, kirimkan HTTP POST request langsung ke endpoint `/resend` untuk email Budi Santoso
16. Verifikasi server menolak request dengan status HTTP 429 atau 400 dan tidak menerbitkan token ketiga
17. Verifikasi Token B tetap aktif dan masa cooldown tetap dihormati

## Notes

- Sesuai PRD §9.2 F-AUTHRST-02, §9.7 baris 2, dan `RSTPWD-LOGIC-01c`, aksi Resend meng-invalidate token aktif sebelumnya dan menerbitkan token aktif baru; tautan sebelumnya otomatis kadaluwarsa.
- Sesuai keputusan NC-08, teks toast sukses Resend mengikuti pola: `"Success, email has been sent to [alamat email]."` dengan target spesifik penerima email.
