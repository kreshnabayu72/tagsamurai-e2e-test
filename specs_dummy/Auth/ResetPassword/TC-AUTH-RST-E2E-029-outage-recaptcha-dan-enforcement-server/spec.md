---
id: TC-AUTH-RST-E2E-029-outage-recaptcha-dan-enforcement-server
title: "Kegagalan layanan reCAPTCHA provider dan penegakan token reCAPTCHA oleh server (Defense-in-Depth)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-21
  - TC-AUTH-RST-120
  - TC-AUTH-RST-121
coverage:
  web: automated
---

# Kegagalan layanan reCAPTCHA provider dan penegakan token reCAPTCHA oleh server (Defense-in-Depth)

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan kemampuan mock network intercept (`Mode: mock`).
- Kemampuan pengiriman HTTP request langsung ke endpoint backend.

## Test Steps

### Kegagalan layanan reCAPTCHA provider (Outage)

1. Intercept permintaan verifikasi reCAPTCHA dengan kegagalan koneksi atau error 5xx dari server reCAPTCHA
2. Klik tombol [Reset Password]
3. Verifikasi toast error "Error, failed to send reset link." tampil di layar (T-AUTHRST-02, D12)
4. Verifikasi form tidak mengirimkan request reset ke endpoint internal TAG Samurai

### Penegakan keamanan server (Defense-in-Depth)

5. Kirimkan HTTP request langsung ke endpoint `/request` tanpa parameter token reCAPTCHA dan tanpa header mobile client
6. Verifikasi server mendeteksi request berasal dari web client dan menolak request dengan status HTTP 400
7. Kirimkan HTTP request langsung ke endpoint `/request` dengan token reCAPTCHA palsu atau invalid
8. Verifikasi server menolak request dengan status HTTP 400 atau 422 dan tidak ada token reset atau email yang diterbitkan

## Notes

- Sesuai PRD §9.2 F-AUTHRST-01 langkah 2 dan §9.4.2 baris 6, client web wajib menyertakan token reCAPTCHA yang valid; request tanpa captcha atau ber-token invalid akan ditolak tegas oleh server.
- Layanan reCAPTCHA tidak terjangkau (D12, §9.4.2) menampilkan toast failed Request Reset (§7 `T-AUTHRST-02`), bukan caption field.
- Spec ini hasil dekomposisi dari `TC-AUTH-RST-E2E-003` (gap GAP-RST-E2E-001): uji outage dan defense-in-depth reCAPTCHA dipisah dari uji gate evaluasi widget.