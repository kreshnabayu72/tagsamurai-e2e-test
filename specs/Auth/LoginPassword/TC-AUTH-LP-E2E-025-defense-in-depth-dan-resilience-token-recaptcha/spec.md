---
id: TC-AUTH-LP-E2E-025-defense-in-depth-dan-resilience-token-recaptcha
title: Defense-in-Depth dan resilience evaluasi token reCAPTCHA
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-100
  - TC-AUTH-LP-139
coverage:
  web: automated
---

# Defense-in-Depth dan resilience evaluasi token reCAPTCHA

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `jokosusilo@qwertysystem.net` berstatus Activated dan Active dengan hitungan gagal 0.
- Mode: mock untuk simulasi network intercept bypass token dan error outage server penyedia reCAPTCHA.

## Test Steps

### Bypass submit tanpa token reCAPTCHA ditolak oleh server (Defense-in-Depth)

1. Buka halaman Login with Password di browser web
2. Masukkan email `jokosusilo@qwertysystem.net` pada field Email
3. Masukkan password `QaLogin#2026` pada field Password
4. Aktifkan intersepsi jaringan pada endpoint login
5. Buat request login dengan membuang field token reCAPTCHA dari payload HTTP POST
6. Teruskan request ke backend
7. Verifikasi respons backend menolak request dengan status penolakan autentikasi
8. Verifikasi caption "Please verify that you are not a robot" tetap tampil di UI dan tidak ada sesi yang dibuat

### Penanganan outage penyedia reCAPTCHA

9. Simulasikan layanan verifikasi Google reCAPTCHA tidak dapat dihubungi oleh backend (503 Service Unavailable / Network Failure)
10. Selesaikan reCAPTCHA di UI lalu klik tombol [Log in]
11. Verifikasi toast error "Error, failed to log in." tampil di layar
12. Verifikasi login tidak berhasil dan user tidak dialihkan ke Portal

## Notes

- Penolakan reCAPTCHA kosong di sisi backend diverifikasi melalui skenario Defense-in-Depth (TC-AUTH-LP-139).
- Kegagalan server penyedia reCAPTCHA dimodelkan sebagai kegagalan sistem internal dengan toast generik (TC-AUTH-LP-100).
- Spec ini dipecah dari E2E-003 agar ciri evaluasi reCAPTCHA (submit tanpa token, token expired, urutan evaluasi) terpisah dari uji bypass server-side dan outage penyedia (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).