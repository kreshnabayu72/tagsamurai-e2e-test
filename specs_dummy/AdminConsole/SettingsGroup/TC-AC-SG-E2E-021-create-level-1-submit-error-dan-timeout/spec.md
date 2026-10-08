---
id: TC-AC-SG-E2E-021-create-level-1-submit-error-dan-timeout
title: "Penanganan kegagalan submit Form Create Level 1 saat server error 5xx atau timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-40
coverage:
  web: automated
---

# Penanganan kegagalan submit Form Create Level 1 saat server error 5xx atau timeout

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept POST /groups)

## Test Steps

### Simulasi Server Error 500
1. Buka modal `[+ New Group]`
2. Isi Group Name dengan nama valid `"Region Error"`
3. Aktifkan interceptor mock respons HTTP 500 Internal Server Error pada API Create Group
4. Klik tombol `[Submit]`
5. Verifikasi muncul toast error `"Error, failed to create group."` di sudut layar
6. Verifikasi modal Create tetap terbuka dan nilai input `"Region Error"` tetap dipertahankan (tidak hilang)
7. Verifikasi tidak ada record baru yang ditambahkan ke tabel

## Notes

- Nilai form harus tetap tersimpan agar pengguna tidak perlu mengetik ulang saat jaringan pulih.
