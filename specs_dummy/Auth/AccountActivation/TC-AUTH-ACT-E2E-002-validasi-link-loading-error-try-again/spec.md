---
id: TC-AUTH-ACT-E2E-002-validasi-link-loading-error-try-again
title: "Validasi link: full-page loading, server error 5xx/429/timeout, dan pemulihan [Try Again]"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-02
  - TC-AUTH-ACT-03
  - TC-AUTH-ACT-04
  - TC-AUTH-ACT-05
  - TC-AUTH-ACT-06
  - TC-AUTH-ACT-133
coverage:
  web: automated
---

# Validasi link: full-page loading, server error 5xx/429/timeout, dan pemulihan [Try Again]

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run); token tidak pernah dikonsumsi selama spec berjalan sehingga satu user cukup untuk seluruh blok.
- Mode: mock. Kemampuan `Spectra.intercept()` pada endpoint validasi link (GET validate) untuk memaksa: delay 5 detik, respons HTTP 500, respons timeout tanpa body, dan respons HTTP 429 (IP rate limit) — termasuk mengembalikan respons ke normal di tengah sesi.
- Akses API read-only untuk memverifikasi token tetap Active dan tidak ada entri pencatatan baru.

## Test Steps

### Full-page loading saat token divalidasi (TC-AUTH-ACT-02)

1. Atur intercept sehingga respons validasi link tertahan selama 5 detik.
2. Buka link aktivasi user seeding.
3. Verifikasi full-page loading tampil selama 5 detik; field Password, field Confirm Password, dan button "Set Password" belum dirender (tidak ada form kosong tanpa indikator).
4. Lepaskan respons validasi sehingga halaman selesai dimuat.
5. Verifikasi halaman Set Password tampil dengan subtitle "Set a password to log in for <email user seeding>.".

### Server error 5xx menampilkan error state, bukan 404 (TC-AUTH-ACT-03)

6. Atur respons validasi link menjadi HTTP 500.
7. Buka link aktivasi.
8. Verifikasi error state "Unable to load this data." tampil dengan button [Try Again].
9. Verifikasi halaman Invalid Link tidak tampil dan form Set Password tidak dirender.

### Timeout tanpa respons jaringan menampilkan error state (TC-AUTH-ACT-04)

10. Atur respons validasi link menjadi timeout tanpa respons.
11. Buka link aktivasi lalu tunggu sampai timeout terjadi.
12. Verifikasi error state "Unable to load this data." tampil dengan button [Try Again].
13. Verifikasi halaman Invalid Link tidak tampil dan form Set Password tidak dirender.

### [Try Again] saat server masih error (TC-AUTH-ACT-06)

14. Dengan respons validasi tetap 500, klik [Try Again].
15. Verifikasi error state "Unable to load this data." dengan button [Try Again] tetap tampil.
16. Verifikasi tidak ada redirect ke halaman Invalid Link dan form Set Password tidak dirender.

### [Try Again] setelah server pulih (TC-AUTH-ACT-05)

17. Pulihkan respons validasi ke kondisi normal.
18. Klik [Try Again].
19. Verifikasi loading tampil sesaat lalu halaman Set Password tampil dengan subtitle "Set a password to log in for <email user seeding>.".
20. Verifikasi error state "Unable to load this data." tidak tampil lagi.

### Rate limit 429 menampilkan error state, bukan 404 (TC-AUTH-ACT-133)

21. Atur respons validasi link menjadi HTTP 429 (simulasi IP rate limit pada endpoint aktivasi).
22. Buka link aktivasi.
23. Verifikasi error state "Unable to load this data." dengan button [Try Again] tampil, bukan halaman Invalid Link.
24. Verifikasi token user seeding tetap Active dan tidak ada entri pencatatan baru dari Auth.

## Notes

- Seluruh kondisi dalam spec ini dipicu lewat intercept sehingga spec berstatus hanya-FE (`Mode: mock`); kebutuhan mock ditulis eksplisit di Prerequisites.
- Karena tidak ada aksi yang mengubah data (link hanya dibuka, tidak disubmit), satu user seeding dipakai berurutan untuk seluruh blok dan token dijamin tetap Active.
- Blok [Try Again] disusun dari kondisi masih-error ke kondisi pulih agar sesi tidak perlu membuka ulang halaman.
