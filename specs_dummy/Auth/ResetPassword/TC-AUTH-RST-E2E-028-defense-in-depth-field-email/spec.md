---
id: TC-AUTH-RST-E2E-028-defense-in-depth-field-email
title: "Proteksi keamanan payload injeksi dan penegakan server pada field Email (Defense-in-Depth)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-119
  - TC-AUTH-RST-128
coverage:
  web: automated
---

# Proteksi keamanan payload injeksi dan penegakan server pada field Email (Defense-in-Depth)

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi khusus pengujian otomatis.
- Widget Google reCAPTCHA v2 diselesaikan otomatis melalui test bypass token.
- Kemampuan pengiriman HTTP request langsung ke endpoint backend (`Mode: mock`).

## Test Steps

### Proteksi payload injeksi SQL dan XSS pada field Email

1. Buka halaman Reset Password di browser web
2. Masukkan payload injeksi SQL `' OR '1'='1` pada field Email
3. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
4. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
5. Verifikasi tidak ada kebocoran error SQL atau pesan 500 dari server
6. Masukkan payload injeksi XSS `<script>alert("xss")</script>` pada field Email
7. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
8. Verifikasi caption inline "Email format is incorrect" tampil dan tidak ada dialog script yang dieksekusi

### Penegakan server terhadap email tidak valid (Bypass UI)

9. Simulasikan pengiriman request bypass UI dengan email tidak valid langsung ke endpoint backend `/request`
10. Verifikasi server menolak request dengan status HTTP 400 atau 422 dan tidak menerbitkan token reset

## Notes

- Sesuai PRD §9.4.3 Must NOT 3 dan `auth-foundation.md` §4.0a, payload injeksi diperlakukan sebagai format email tidak valid (caption "Email format is incorrect") tanpa dieksekusi atau membocorkan error ke pengguna.
- Penegakan server tetap memvalidasi email secara independen dari validasi browser sehingga request langsung ke backend tanpa email valid ditolak tegas.
- Spec ini hasil dekomposisi dari `TC-AUTH-RST-E2E-002` (gap GAP-RST-E2E-001): uji security/defense-in-depth dipisah dari uji validasi fungsional field Email.