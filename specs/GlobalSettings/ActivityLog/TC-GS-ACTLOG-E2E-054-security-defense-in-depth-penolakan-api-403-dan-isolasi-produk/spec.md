---
id: TC-GS-ACTLOG-E2E-054-security-defense-in-depth-penolakan-api-403-dan-isolasi-produk
title: "Security & Defense-in-Depth: Penolakan Akses Langsung Endpoint API 403 dan Isolasi Parameter Multi-Produk"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-215
  - TC-GS-ACTLOG-216
  - TC-GS-ACTLOG-217
coverage:
  web: automated
---

# Security & Defense-in-Depth: Penolakan Akses Langsung Endpoint API 403 dan Isolasi Parameter Multi-Produk

## Prerequisites

- Kredensial akun peran 'Create-Only Brand' (tanpa hak Activity Log)
- Kredensial akun peran 'Admin Console See-All'
- Kredensial akun peran 'Total Control Global Settings'

## Test Steps

### Direct API Endpoint Guard (Create-Only Role)
1. Kirim request HTTP GET langsung ke endpoint API list Session, list User Action, opsi filter, dan export menggunakan token sesi 'Create-Only Brand'.
2. Verifikasi backend menolak seluruh permintaan dengan status HTTP 403 Forbidden.
### Direct API Endpoint Guard (Admin Console Role)
3. Kirim request HTTP GET ke endpoint Activity Log GS menggunakan token sesi 'Admin Console See-All'.
4. Verifikasi backend menolak permintaan dengan status HTTP 403 Forbidden (izin Admin Console tidak berlaku di GS).
### Parameter Tampering & Isolasi Produk
5. Kirim request HTTP GET ke endpoint list Session dengan token Total Control GS sambil menyisipkan query parameter produk lain (misal: '?product=fams').
6. Verifikasi server mengabaikan parameter tampering tersebut dan hanya mengembalikan log entitas Global Settings tanpa membocorkan log produk Fixed Asset.

## Notes

- Verifikasi pertahanan berlapis (defense-in-depth) di level API backend independen dari validasi antarmuka peramban.
