---
id: TC-AUTH-RST-E2E-014-screening-setup-new-password
title: "Screening halaman Setup New Password, state awal form, aksesibilitas ARIA, dan urutan keyboard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-63
  - TC-AUTH-RST-64
  - TC-AUTH-RST-65
  - TC-AUTH-RST-66
  - TC-AUTH-RST-70
coverage:
  web: automated
---

# Screening halaman Setup New Password, state awal form, aksesibilitas ARIA, dan urutan keyboard

## Prerequisites

- User belum login (guest); membuka tautan reset valid milik `budisantoso@qwertysystem.net`.
- Halaman Setup New Password (`/setup-new-password?token=...`) berhasil dimuat di browser web.

## Test Steps

### Screening elemen halaman dan state awal

1. Amati form Setup New Password dari atas ke bawah
2. Verifikasi logo TAG Samurai tampil di bagian tengah atas
3. Verifikasi title halaman adalah "Setup New Password"
4. Verifikasi subtitle halaman adalah "Please enter a new password for budisantoso@qwertysystem.net"
5. Verifikasi field Password tampil dengan label "Password", placeholder "Enter your password", dan karakter dalam keadaan masked (tersembunyi)
6. Verifikasi field Confirm Password tampil dengan label "Confirm Password", placeholder "Confirm your password", dan karakter dalam keadaan masked
7. Verifikasi kedua field memiliki ikon toggle intip (eye icon) di sisi kanan
8. Verifikasi bagian checklist Password Policy menampilkan 5 butir persyaratan dengan warna netral abu-abu (belum terpenuhi):
   - "Minimum 8 characters"
   - "At least 1 uppercase letter (A-Z)"
   - "At least 1 lowercase letter (a-z)"
   - "At least 1 number (0-9)"
   - "At least 1 special character (!@?&)"
9. Verifikasi tombol [Reset Password] tampil dengan styling solid primary dan dalam keadaan enabled

### Aksesibilitas keyboard dan urutan Tab

10. Klik field Password untuk menempatkan fokus keyboard
11. Tekan tombol Tab pada keyboard lalu verifikasi fokus berpindah ke ikon toggle intip field Password
12. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke field Confirm Password
13. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke ikon toggle intip field Confirm Password
14. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke tombol [Reset Password]

### Kelengkapan atribut ARIA untuk Screen Reader

15. Periksa atribut DOM pada field Password
16. Verifikasi field Password memiliki atribut `aria-describedby` yang mereferensikan kontainer checklist Password Policy
17. Verifikasi kontainer checklist memiliki atribut `role="list"` dan setiap item memiliki `role="listitem"`
18. Verifikasi status pemenuhan checklist diperbarui secara dinamis pada atribut ARIA bagi pembaca layar

### Independensi toggle intip password (Show/Hide)

19. Masukkan teks "Rahasia123!" pada field Password dan field Confirm Password
20. Klik ikon toggle intip pada field Password saja
21. Verifikasi karakter pada field Password menjadi terlihat (unmasked / type="text")
22. Verifikasi karakter pada field Confirm Password tetap tersembunyi (masked / type="password")
23. Klik ikon toggle intip pada field Confirm Password
24. Verifikasi karakter pada field Confirm Password kini terlihat tanpa memengaruhi status field Password
25. Klik kembali kedua ikon toggle intip untuk menyembunyikan karakter kembali

## Notes

- Sesuai PRD §4.1 S-AUTHRST-03, §4.2 Halaman 3, §4.3 FI-AUTHRST-02, dan §4.5 Keyboard Focus, toggle intip pada kedua field bekerja secara independen satu sama lain dan form dapat dinavigasikan secara penuh menggunakan keyboard.
