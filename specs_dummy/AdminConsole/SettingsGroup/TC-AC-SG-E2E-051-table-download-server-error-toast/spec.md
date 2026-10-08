---
id: TC-AC-SG-E2E-051-table-download-server-error-toast
title: "Penanganan error saat download tabel utama gagal (500 server error)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-98
coverage:
  web: automated
---

# Penanganan error saat download tabel utama gagal (500 server error)

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept POST /groups/export dengan status 500)

## Test Steps

### Simulasi Download Gagal
1. Buka halaman `Settings > Group`
2. Pasang interceptor mock respons 500 Server Error pada request download
3. Klik icon `[⬇ Download]` lalu pilih salah satu format ekspor
4. Verifikasi toast error muncul dengan pesan `"Error, failed to download Groups."`
5. Verifikasi tabel utama tetap responsif dan tidak mengalami crash

## Notes

- Diisolasi untuk pengujian ketahanan interaksi ekspor jaringan.
