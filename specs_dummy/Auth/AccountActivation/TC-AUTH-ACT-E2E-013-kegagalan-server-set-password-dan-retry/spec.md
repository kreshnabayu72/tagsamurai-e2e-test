---
id: TC-AUTH-ACT-E2E-013-kegagalan-server-set-password-dan-retry
title: "Kegagalan Set Password (5xx, timeout, 429) mempertahankan input dan token sampai retry sukses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-66
  - TC-AUTH-ACT-67
  - TC-AUTH-ACT-68
  - TC-AUTH-ACT-69
  - TC-AUTH-ACT-134
coverage:
  web: automated
---

# Kegagalan Set Password (5xx, timeout, 429) mempertahankan input dan token sampai retry sukses

## Prerequisites

- Browser publik tanpa sesi login; sesi kedua (jendela privat) untuk memverifikasi link masih valid.
- `Mode: mock` — kemampuan mengatur respons submit menjadi server error 500, timeout, dan 429 Rate Limit via intercept jaringan.
- 3 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run):
  - User A untuk rantai TC-AUTH-ACT-66 → 67 → 68 (submit 500, verifikasi token, lalu retry sukses).
  - User B untuk TC-AUTH-ACT-69 (timeout).
  - User C untuk TC-AUTH-ACT-134 (rate limit), didahului fixture 20 request aktivasi dari IP yang sama dalam 1 menit terakhir sesuai precondition TC.
- Pemantauan request jaringan untuk memastikan hanya satu request per klik.
- Akses API read-only untuk memverifikasi status token dan user sebelum serta sesudah tiap kegagalan.

## Test Steps

### Screening: form Set Password siap dan token Active (TC-AUTH-ACT-66)

1. Buka link aktivasi user A → halaman `Auth > Account Activation > Set Password` tampil.
2. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.

### Server error 5xx menampilkan toast dan mempertahankan input (TC-AUTH-ACT-66)

3. Atur respons submit menjadi server error 500.
4. Klik button "Set Password".
5. Verifikasi toast error: "Error, failed to set password."
6. Verifikasi halaman tetap `Auth > Account Activation > Set Password` dan field Password serta Confirm Password tetap berisi `Aman#Sandi8`.
7. Verifikasi button "Set Password" kembali enabled (tidak Loading) dan halaman Activation Success tidak tampil.

### Token dan status user tidak berubah setelah gagal 5xx (TC-AUTH-ACT-67)

8. Buka kembali link aktivasi user A yang sama di tab/jendela baru.
9. Verifikasi halaman `Auth > Account Activation > Set Password` tampil kembali (token masih valid).
10. Buka `Global Settings > User > Login User` dengan sesi admin dan cari user A.
11. Verifikasi user A tetap berbadge Pending Activation pada tabel.
12. Verifikasi via API bahwa token user A tetap Active dan status user tetap Pending Activation.

### Retry setelah server pulih berhasil tanpa mengisi ulang (TC-AUTH-ACT-68)

13. Kembali ke tab asal, pulihkan respons submit menjadi normal.
14. Verifikasi field Password dan Confirm Password masih berisi `Aman#Sandi8` (tanpa pengisian ulang).
15. Klik button "Set Password".
16. Verifikasi halaman `Auth > Account Activation > Activation Success` tampil.
17. Verifikasi via API bahwa token user A berstatus Consumed dan status user A Activated.

### Timeout menampilkan toast dan mempertahankan input (TC-AUTH-ACT-69)

18. Buka link aktivasi user B → halaman Set Password tampil.
19. Ketik `Aman#Sandi8` pada kedua field.
20. Atur respons submit menjadi timeout (blokir respons sampai timeout).
21. Klik button "Set Password", lalu tunggu sampai timeout terjadi.
22. Verifikasi toast error: "Error, failed to set password."
23. Verifikasi halaman tetap di Set Password dengan kedua field tetap berisi `Aman#Sandi8` dan button "Set Password" enabled kembali.
24. Verifikasi via API bahwa token user B tetap Active.

### Ditolak 429 oleh IP rate limit (TC-AUTH-ACT-134)

25. Buka link aktivasi user C → halaman Set Password tampil.
26. Verifikasi fixture 20 request aktivasi dari IP yang sama sudah terkirim dalam 1 menit terakhir.
27. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password" (request ke-21 dalam 1 menit dari IP yang sama).
28. Verifikasi toast gagal tampil, form tetap terbuka, dan nilai field dipertahankan.
29. Verifikasi via API bahwa token user C tetap Active, status user C tetap Pending Activation, dan tidak ada entri pencatatan baru.

## Notes

- User A sengaja dipakai berantai (66 → 67 → 68) karena TC-67 dan TC-68 bergantung pada state gagal 5xx yang sama; retry sukses (aksi destruktif) ditempatkan terakhir dalam rantai tersebut.
- Seluruh kasus kegagalan tidak mengubah token, sehingga user B dan C bebas diuji setelah rantai user A; blok 429 diletakkan sebelum penutup sukses agar seluruh kasus gagal berurutan.
- Kebutuhan mock respons dan fixture rate limit dicatat di Prerequisites.
