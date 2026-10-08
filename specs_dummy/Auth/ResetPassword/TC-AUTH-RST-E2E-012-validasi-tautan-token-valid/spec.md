---
id: TC-AUTH-RST-E2E-012-validasi-tautan-token-valid
title: "Validasi tautan token reset: pembukaan idempotent tanpa efek samping dan masa berlaku 24 jam"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-54
  - TC-AUTH-RST-56
  - TC-AUTH-RST-58
  - TC-AUTH-RST-59
coverage:
  web: automated
---

# Validasi tautan token reset: pembukaan idempotent tanpa efek samping dan masa berlaku 24 jam

## Prerequisites

- User belum login (guest); browser web siap mengakses tautan reset.
- Token reset aktif valid milik user `budisantoso@qwertysystem.net` telah diterbitkan di database.
- Tautan reset valid berformat `/setup-new-password?token={valid_token}`.

## Test Steps

### Pembukaan tautan valid pertama kali

1. Buka tautan reset valid di browser web
2. Verifikasi halaman Setup New Password berhasil dirender
3. Verifikasi title halaman adalah "Setup New Password"
4. Verifikasi subtitle memuat alamat email "Set a new password to log in for budisantoso@qwertysystem.net."

### Pembukaan berulang kali (Idempotent GET /validate)

5. Lakukan reload / refresh halaman browser yang sedang membuka Setup New Password
6. Buka kembali tautan reset yang sama pada tab browser lain
7. Verifikasi halaman Setup New Password tetap berhasil dirender dengan benar
8. Verifikasi status token di database tetap `active` (tidak dikonsumsi oleh aksi GET)
9. Buka Activity Log Session dan User Log menggunakan sesi admin
10. Verifikasi tidak ada entri log yang dicatat untuk pembukaan tautan valid (zero-logging operasi read)

### Tautan berusia kurang dari 24 jam (Batas 23 jam 59 menit)

11. Siapkan token reset yang telah berusia 23 jam 59 menit dari waktu pembuatan di database
12. Buka tautan token tersebut di browser
13. Verifikasi tautan masih diterima sebagai token aktif dan halaman Setup New Password berhasil dirender normal

### Akses dengan token tidak dikenal atau dimanipulasi

14. Ubah beberapa karakter pada parameter token di URL (misal: `/setup-new-password?token=invalid_random_string_123`)
15. Tekan Enter untuk memuat halaman
16. Verifikasi sistem menolak token dan merender Halaman 404 varian Expired ("Reset Link Expired")
17. Verifikasi tidak ada log yang dicatat untuk token tidak dikenal

### Akses URL Setup New Password tanpa parameter token

18. Akses langsung path `/setup-new-password` tanpa parameter query token atau dengan parameter kosong (`?token=`)
19. Verifikasi sistem memperlakukan ketiadaan token sama dengan token tidak dikenal
20. Verifikasi browser menampilkan Halaman 404 varian Expired ("Reset Link Expired")

## Notes

- Sesuai keputusan NC-12 dan PRD §9.9 FLD-AUTHRST-05, URL tanpa token atau dengan token kosong langsung dialihkan ke Halaman 404 varian Expired.
- Sesuai PRD §9.2 F-AUTHRST-03 dan §9.8 catatan, endpoint validasi link (`GET /validate/{token}`) bersifat read-only dan idempotent, sehingga pembukaan berkali-kali tidak mengubah status token maupun mencatat audit log.
