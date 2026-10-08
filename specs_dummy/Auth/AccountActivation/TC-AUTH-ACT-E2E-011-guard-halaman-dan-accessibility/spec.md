---
id: TC-AUTH-ACT-E2E-011-guard-halaman-dan-accessibility
title: "Guard halaman Set Password (tanpa dialog Unsaved Changes) dan accessibility"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-58
  - TC-AUTH-ACT-59
  - TC-AUTH-ACT-60
  - TC-AUTH-ACT-61
  - TC-AUTH-ACT-62
coverage:
  web: automated
---

# Guard halaman Set Password (tanpa dialog Unsaved Changes) dan accessibility

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run); token tidak pernah dikonsumsi selama spec berjalan.
- Kemampuan memeriksa atribut aksesibilitas (inspeksi DOM atau screen reader) untuk verifikasi keterhubungan inline error ke field.
- Akses API read-only untuk memverifikasi token tetap Active setelah meninggalkan halaman.

## Test Steps

### Reload setelah mengisi field tanpa dialog Unsaved Changes (TC-AUTH-ACT-58)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Ketik `Aman#Sandi8` pada field Password dan Confirm Password.
3. Reload halaman (F5).
4. Verifikasi tidak ada dialog Unsaved Changes maupun dialog native browser sebelum reload.
5. Verifikasi halaman memuat ulang dan halaman Set Password tampil kembali dengan field Password dan Confirm Password kosong.

### Meninggalkan halaman setelah mengisi field (TC-AUTH-ACT-59)

6. Ketik `Aman#Sandi8` pada field Password dan Confirm Password.
7. Navigasi ke halaman lain pada tab yang sama.
8. Verifikasi tidak ada dialog konfirmasi (Unsaved Changes) dan navigasi berlangsung langsung.
9. Buka kembali link aktivasi yang sama.
10. Verifikasi halaman Set Password tampil kembali dengan kedua field kosong (token tetap valid, tidak ada data yang tersimpan).
11. Verifikasi token user seeding tetap berstatus Active.

### Ikon toggle dapat difokuskan dengan keyboard (TC-AUTH-ACT-60)

12. Pada halaman Set Password, tekan Tab berulang sampai fokus mencapai ikon toggle di field Password.
13. Verifikasi ikon toggle field Password menerima fokus keyboard dan menampilkan tooltip "Show password".
14. Tekan Tab sampai fokus mencapai ikon toggle di field Confirm Password.
15. Verifikasi ikon toggle field Confirm Password menerima fokus keyboard dan menampilkan tooltip "Show password".

### Inline error berupa teks dan terhubung ke field (TC-AUTH-ACT-61)

16. Klik button "Set Password" dengan kedua field kosong.
17. Verifikasi pesan error tampil sebagai teks (bukan hanya perubahan warna): "Password must not be empty" dan "Confirm password must not be empty".
18. Verifikasi field Password terhubung ke pesan "Password must not be empty" dan field Confirm Password terhubung ke pesan "Confirm password must not be empty" (dibacakan pembaca layar saat field fokus).

### Status checklist dibedakan dengan ikon (TC-AUTH-ACT-62)

19. Kosongkan kedua field, lalu ketik `Abcdefg1` pada field Password.
20. Amati ikon pada setiap baris checklist.
21. Verifikasi baris yang terpenuhi menampilkan ikon ✓ dan baris yang belum terpenuhi menampilkan ikon ○ (status terbaca tanpa bergantung warna).

## Notes

- Guard halaman diuji pada form dirty (sudah terisi) sesuai aturan bahwa kasus menutup/meninggalkan form ditempatkan setelah validasi yang memform dirty; seluruh kasus berbagi satu user karena tidak ada submit yang diterima server.
- Kebutuhan inspeksi atribut aksesibilitas dicatat di Prerequisites.
