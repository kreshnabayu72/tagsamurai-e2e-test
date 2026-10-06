---
id: TC-AC-ACAL-E2E-039-sanitasi-xss-search-dan-ip-address
title: "Keamanan & Format — Sanitasi XSS script injection pada Search toolbar dan format IP Address"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-238
  - TC-AC-ACAL-239
coverage:
  web: automated
---

# Keamanan & Format — Sanitasi XSS script injection pada Search toolbar dan format IP Address

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session dan Tab User Action terisi data riwayat log

## Test Steps

### Uji Sanitasi Input XSS Script Injection

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik icon Search `[🔍]` di toolbar
3. Masukkan payload XSS: `<script>alert('XSS')</script>` lalu tekan Enter
4. Verifikasi teks dieksekusi secara aman sebagai plain text literal tanpa memicu script execution (tidak muncul alert dialog popup JavaScript)
5. Verifikasi tampilan tabel tetap stabil atau menampilkan `No results found` tanpa error parsing DOM

### Verifikasi Format IP Address

6. Amati nilai pada kolom `IP Address` di tabel Tab Session
7. Verifikasi IP address tampil dalam format kanonik IPv4 (contoh: `192.168.1.50`) atau IPv6 tanpa masking parsial bagi peran administrator

## Notes

- Menjamin ketahanan antarmuka terhadap serangan injeksi script melalui field input pencarian.
