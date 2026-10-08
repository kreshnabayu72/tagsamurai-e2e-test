---
id: TC-AUTH-RST-E2E-015-evaluasi-password-policy
title: "Evaluasi reaktif Password Policy checklist, batas karakter 8-72, dan karakter spesial"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-67
  - TC-AUTH-RST-68
  - TC-AUTH-RST-69
  - TC-AUTH-RST-80
coverage:
  web: automated
---

# Evaluasi reaktif Password Policy checklist, batas karakter 8-72, dan karakter spesial

## Prerequisites

- User belum login (guest); form Setup New Password terbuka dengan token valid.
- Environment uji terisolasi khusus pengujian otomatis.

## Test Steps

### Evaluasi reaktif per-keystroke pada checklist Password Policy

1. Buka halaman Setup New Password
2. Ketik huruf besar "A" pada field Password
3. Verifikasi item "At least 1 uppercase letter (A-Z)" seketika berubah warna hijau dengan ikon centang
4. Verifikasi 4 butir lainnya tetap berwarna abu-abu
5. Tambahkan huruf kecil "b" (menjadi "Ab")
6. Verifikasi item "At least 1 lowercase letter (a-z)" berubah hijau dengan ikon centang
7. Tambahkan angka "1" (menjadi "Ab1")
8. Verifikasi item "At least 1 number (0-9)" berubah hijau dengan ikon centang
9. Tambahkan karakter simbol "!" (menjadi "Ab1!")
10. Verifikasi item "At least 1 special character (!@?&)" berubah hijau dengan ikon centang
11. Verifikasi item "Minimum 8 characters" masih berwarna abu-abu karena panjang baru 4 karakter
12. Tambahkan karakter "cde" sehingga panjang menjadi 7 karakter ("Ab1!cde")
13. Verifikasi item "Minimum 8 characters" tetap berwarna abu-abu
14. Tambahkan karakter ke-8 "f" sehingga menjadi "Ab1!cdef"
15. Verifikasi seluruh 5 butir checklist Password Policy kini berwarna hijau dan tercentang penuh

### Larangan karakter spasi di dalam password

16. Hapus karakter terakhir lalu sisipkan spasi di tengah: "Ab1! cdef"
17. Verifikasi sistem mendeteksi keberadaan spasi
18. Verifikasi indikator aturan spasi menunjukkan pelanggaran (item checklist terkait atau caption penolakan spasi aktif)
19. Hapus spasi tersebut sehingga checklist kembali valid

### Batas panjang karakter (8 s/d 72 karakter)

20. Kosongkan field Password lalu ketik 72 karakter yang memenuhi seluruh kombinasi aturan (huruf besar, huruf kecil, angka, simbol)
21. Verifikasi seluruh checklist tercentang hijau dan caption "Max. 72 characters" tidak tampil
22. Ketik 1 karakter tambahan sehingga total panjang password menjadi 73 karakter
23. Verifikasi caption inline "Max. 72 characters" langsung muncul secara real-time tepat di bawah field Password
24. Hapus karakter ke-73 tersebut sehingga kembali ke 72 karakter
25. Verifikasi caption "Max. 72 characters" seketika hilang

### Pengujian himpunan karakter spesial ASCII yang didukung

26. Masukkan password dasar "Aa1" diikuti karakter spesial ASCII yang berbeda:
    - Simbol `@`: `Aa1@bcde` -> verifikasi centang spesial karakter hijau
    - Simbol `?`: `Aa1?bcde` -> verifikasi centang spesial karakter hijau
    - Simbol `&`: `Aa1&bcde` -> verifikasi centang spesial karakter hijau
    - Simbol `#`, `$`, `%`, `*`, `_`, `-`: verifikasi semua karakter ASCII non-alfanumerik printable diterima sebagai karakter spesial yang valid

## Notes

- Sesuai PRD §4.3 FI-AUTHRST-01, evaluasi checklist terjadi secara instan pada setiap ketukan keyboard pengguna (keystroke reactive).
- Sesuai keputusan NC-17, karakter spesial yang didukung mencakup seluruh karakter ASCII non-alfanumerik yang dapat dicetak selain spasi (huruf non-ASCII dan emoji tidak dihitung).
- Sesuai PRD §6 V-AUTHRST-07 dan §9.9 FLD-AUTHRST-03, panjang password dibatasi minimal 8 karakter dan maksimal 72 karakter.
