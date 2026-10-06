---
id: TC-AUTH-RST-E2E-016-validasi-form-setup-new-password
title: "Validasi form Setup New Password: field wajib diisi, konfirmasi cocok, penolakan policy server, dan spasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-71
  - TC-AUTH-RST-72
  - TC-AUTH-RST-73
  - TC-AUTH-RST-74
  - TC-AUTH-RST-75
  - TC-AUTH-RST-76
  - TC-AUTH-RST-77
  - TC-AUTH-RST-78
  - TC-AUTH-RST-122
  - TC-AUTH-RST-124
coverage:
  web: automated
---

# Validasi form Setup New Password: field wajib diisi, konfirmasi cocok, penolakan policy server, dan spasi

## Prerequisites

- User belum login (guest); form Setup New Password terbuka dengan token valid.
- Environment uji terisolasi khusus pengujian otomatis.

## Test Steps

### Field Password kosong dan Confirm Password terisi

1. Buka halaman Setup New Password di browser web
2. Biarkan field Password kosong
3. Masukkan "QaBaru!2027" pada field Confirm Password
4. Klik tombol [Reset Password]
5. Verifikasi caption inline "Password must not be empty" tampil di bawah field Password
6. Verifikasi tidak ada permintaan submit yang dikirim ke server

### Field Password terisi dan Confirm Password kosong

7. Masukkan "QaBaru!2027" pada field Password
8. Kosongkan field Confirm Password
9. Klik tombol [Reset Password]
10. Verifikasi caption inline "Confirm Password must not be empty" tampil di bawah field Confirm Password

### Field Password dan Confirm Password kosong sekaligus

11. Kosongkan kedua field Password dan Confirm Password
12. Klik tombol [Reset Password]
13. Verifikasi caption inline "Password must not be empty" tampil di bawah field Password
14. Verifikasi caption inline "Confirm Password must not be empty" tampil di bawah field Confirm Password
15. Verifikasi kedua caption error tampil bersamaan di layar

### Konfirmasi password tidak cocok (Mismatch)

16. Masukkan "QaBaru!2027" pada field Password
17. Masukkan "QaBeda!2028" pada field Confirm Password
18. Klik tombol [Reset Password]
19. Verifikasi caption inline "Password and Confirm Password must match" tampil di bawah field Confirm Password
20. Verifikasi submit diblokir di sisi client

### Penolakan server terhadap pelanggaran policy dan retensi token

21. Simulasikan pengiriman password yang melanggar kebijakan (misal tanpa simbol) langsung ke server
22. Verifikasi server menolak dengan status HTTP 422
23. Verifikasi pada UI checklist policy tetap menunjukkan butir yang belum terpenuhi
24. Verifikasi token reset di database TIDAK dikonsumsi (tetap `active`)
25. Lakukan submit ulang pada form yang sama dengan password yang memenuhi policy
26. Verifikasi submit berikutnya berhasil diproses, membuktikan token tidak hangus akibat submit gagal

### Penolakan password 73 karakter di sisi server

27. Kirimkan submit password dengan panjang 73 karakter melewati validasi client
28. Verifikasi server menolak dengan status HTTP 422 dan tidak menyimpan password tersebut

### Penolakan password dengan spasi di awal atau akhir (No-Trim)

29. Masukkan password yang diawali spasi " QaBaru!2027" pada field Password dan Confirm Password
30. Klik tombol [Reset Password]
31. Verifikasi server tidak melakukan trim spasi dan menolak password karena mengandung karakter spasi yang dilarang

### Penegakan aturan oleh server (Defense-in-Depth)

32. Kirimkan HTTP request langsung ke endpoint `/confirm` dengan Confirm Password kosong atau tidak cocok
33. Verifikasi server menolak request dengan status HTTP 400 atau 422
34. Kirimkan HTTP request langsung dengan password yang melanggar policy
35. Verifikasi server menegakkan Password Policy secara independen dari validasi browser

## Notes

- Sesuai keputusan NC-15, saat kedua field password kosong, kedua caption error ditampilkan bersamaan pada field masing-masing.
- Sesuai PRD §9.4.3 Must NOT 5, kegagalan submit akibat validasi policy tidak boleh mengonsumsi token reset.
- Sesuai PRD §6 V-AUTHRST-04 s/d V-AUTHRST-07, konfirmasi password harus identik dan password tidak boleh mengandung spasi pada posisi mana pun.
