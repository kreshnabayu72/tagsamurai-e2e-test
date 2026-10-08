---
id: TC-AUTH-LP-E2E-028-kondisi-audit-log-yang-tidak-dicatat
title: Verifikasi kondisi yang TIDAK dicatat di kedua surface log
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-90
  - TC-AUTH-LP-117
  - TC-AUTH-LP-118
  - TC-AUTH-LP-119
  - TC-AUTH-LP-120
  - TC-AUTH-LP-121
  - TC-AUTH-LP-122
  - TC-AUTH-LP-123
coverage:
  web: automated
---

# Verifikasi kondisi yang TIDAK dicatat di kedua surface log

## Prerequisites

- Pengujian memerlukan dua sesi browser:
  - Sesi 1: Form Login with Password untuk submit skenario uji.
  - Sesi 2: Administrator Total Control (Global Settings) yang memantau `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- User `jokosusilo@qwertysystem.net` aktif; email `tidakada@qwertysystem.net` tidak terdaftar.
- User `nuraini@qwertysystem.net` dalam status lock 15 menit.
- User `jonoiskandar@qwertysystem.net` berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA.
- Akun Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` tersedia untuk mempublikasikan versi Privacy Policy baru di tengah skenario.
- Kemampuan mengirim lebih dari 20 request login per menit dari satu IP untuk memicu batas rate limit.

## Test Steps

### Verifikasi kondisi yang TIDAK dicatat pada surface log mana pun

1. Pada Sesi 2: Catat jumlah baris log pada Activity Log > Session dan User Log
2. Pada Sesi 1: Kosongkan field Email, isi password, selesaikan reCAPTCHA, lalu klik [Log in]
3. Pada Sesi 2: Muat ulang kedua surface dan verifikasi tidak ada baris log baru bertambah (email kosong tidak punya subjek user)
4. Pada Sesi 1: Masukkan email dengan format salah `jokosusilo@qwertysystem`, selesaikan reCAPTCHA, lalu klik [Log in]
5. Pada Sesi 2: Verifikasi tidak ada baris log baru bertambah
6. Pada Sesi 1: Masukkan email belum terdaftar `tidakada@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Log in]
7. Pada Sesi 2: Verifikasi tidak ada baris log baru bertambah
8. Pada Sesi 1: Pada akun `nuraini@qwertysystem.net` yang sedang terkunci 15 menit, kirimkan submit tambahan selama lock aktif
9. Pada Sesi 2: Verifikasi tidak ada baris log baru bertambah untuk percobaan selama masa lock aktif
10. Pada Sesi 1: Klik link navigasi [Log in with OTP] dan [Reset here]
11. Pada Sesi 2: Verifikasi aksi navigasi tidak menghasilkan baris log
12. Pada Sesi 1: Lakukan penolakan confirm agreement akibat versi Privacy Policy berubah di tengah jalan
13. Pada Sesi 2: Verifikasi reload layar akibat perubahan versi policy tidak menghasilkan baris log
14. Pada Sesi 1: Kirim submit yang melampaui batas rate limit IP 20 request/menit
15. Pada Sesi 2: Verifikasi penolakan IP rate limit tidak menghasilkan baris log pada kedua surface

### Meninggalkan layar Confirm to Continue tanpa Continue tidak dicatat

16. Pada Sesi 1: Login dengan email `jonoiskandar@qwertysystem.net` dan password `QaLogin#2026` sampai layar Confirm to Continue tampil
17. Tutup tab tanpa mencentang checkbox atau klik tombol [Continue ➔]
18. Buka halaman Login with Password di tab baru dan verifikasi halaman Login tampil normal tanpa sesi aktif
19. Login lagi dengan email dan password yang sama sampai layar Confirm to Continue tampil kembali
20. Pada Sesi 2: Muat ulang `Global Settings > Activity Log > Session` dan cari baris untuk user "Jono I"
21. Pada Sesi 2: Buka `Global Settings > User > Detail > User Log` untuk user "Jono I"
22. Verifikasi tidak ada baris baru dengan Note `Consent not given` maupun `Login with password` di kedua surface (baris sebelumnya tetap tampil sebagai anchor)

## Notes

- Sesuai PRD §9.8, hanya attempt dengan subjek user valid dan resolved yang dicatat (`TC-AUTH-LP-117` s/d `TC-AUTH-LP-119`); percobaan selama akun terkunci tidak menambah baris log agar tidak mencemari audit trail (`AUTHLP-LOGIC-02k`, `TC-AUTH-LP-120`).
- Aksi navigasi, reload akibat perubahan versi policy, dan penolakan IP rate limit tidak menghasilkan baris log (`TC-AUTH-LP-121`, `TC-AUTH-LP-122`, `TC-AUTH-LP-123`).
- Meninggalkan layar Confirm to Continue tanpa Continue tidak mencatat `Consent not given` maupun `Login with password` (PRD §9.2 F-AUTHLP-05 butir terakhir; `TC-AUTH-LP-90`).
- Spec ini dipecah dari E2E-017 dan E2E-011 agar verifikasi absence log terpisah dari uji pencatatan kegagalan dan dari uji konfirmasi Agreement (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).