---
id: TC-AUTH-OTP-E2E-027-konkurensi-multi-tab-paralel
title: "Konkurensi Multi-Tab: Verifikasi Paralel, Resend Lintas Tab, dan Request Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-164
  - TC-AUTH-OTP-165
  - TC-AUTH-OTP-173
coverage:
  web: automated
---

# Konkurensi Multi-Tab: Verifikasi Paralel, Resend Lintas Tab, dan Request Bersamaan

## Prerequisites

- Dua konteks tab browser aktif dalam satu browser session (`Tab 1` dan `Tab 2`).
- Belum login dan session kosong.
- User `MultiTab Verifier` (`multitab1@qwertysystem.net`) profil BASE.
- User `MultiTab Resender` (`multitab2@qwertysystem.net`) profil BASE.
- User `MultiTab Requester` (`multitab3@qwertysystem.net`) profil BASE.
- Mail-catcher aktif.

## Test Steps

### Verifikasi paralel pada dua tab: Konsumsi kode secara atomik

1. Pada Tab 1, buka Request OTP untuk `multitab1@qwertysystem.net`, kirim permintaan OTP
2. Salin URL Verify OTP dari Tab 1 dan buka di Tab 2
3. Ambil kode OTP asli yang masuk ke email mail-catcher (misal: "654321")
4. Isi 6 digit kode "654321" pada Tab 1 dan Tab 2
5. Picu verifikasi kode secara hampir bersamaan (paralel) pada kedua tab
6. Verifikasi backend memproses verifikasi secara atomik (database transaction lock):
   - Tab 1 yang diproses pertama berhasil melakukan login dan masuk ke Product Hub
   - Tab 2 yang diproses sepersekian detik setelahnya ditolak dengan pesan kode salah / telah terpakai
7. Verifikasi tidak ada kondisi race condition yang menghasilkan dua sesi aktif yang inkonsisten

### Resend di Tab A meng-invalidate kode yang sedang aktif di Tab B

8. Pada Tab 1, buka Request OTP untuk `multitab2@qwertysystem.net`, catat Kode 1 yang diterima di email
9. Duplikasi layar Verify OTP ke Tab 2
10. Pada Tab 2, ketik Kode 1 ke kotak digit tetapi jangan submit terlebih dahulu
11. Pada Tab 1, tunggu tombol [Resend code] aktif, lalu klik button [Resend code] untuk menerbitkan Kode 2
12. Pada Tab 2, submit Kode 1 yang sebelumnya sudah terketik
13. Verifikasi Kode 1 ditolak seketika oleh server karena penerbitan Kode 2 di Tab 1 telah meng-invalidate Kode 1
14. Masukkan Kode 2 pada Tab 2 dan verifikasi login berhasil

### Request OTP bersamaan dari dua tab untuk email yang sama

15. Buka halaman Request OTP pada Tab 1 dan Tab 2
16. Masukkan email `multitab3@qwertysystem.net` pada kedua tab
17. Centang reCAPTCHA pada kedua tab
18. Klik button [Request OTP] secara bersamaan pada Tab 1 dan Tab 2
19. Verifikasi server menangani konkurensi dengan benar:
    - Hanya satu proses penerbitan kode yang dieksekusi atau request kedua ditangani sebagai duplicate in-flight
    - Kuota pengiriman tidak terpotong dua kali untuk aksi yang sama
    - Pengguna dapat menyelesaikan verifikasi dengan kode yang valid tanpa kegagalan sistem

## Notes

- Pengujian konkurensi multi-tab menguji ketahanan server terhadap kondisi balapan (race conditions) pada transaksi verifikasi, penerbitan kode, dan pemotongan kuota.
- Konsumsi kode OTP dilakukan dalam transaksi database terisolasi untuk memastikan prinsip Exactly-Once Execution.
