---
id: TC-GS-ACTLOG-E2E-056-edge-case-akses-dan-ingestion-saat-client-suspended
title: "Edge Case Bisnis: Akses Riwayat Log dan Ingestion Audit Otomatis saat Status Client Suspended/Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-222
  - TC-GS-ACTLOG-223
coverage:
  web: automated
---

# Edge Case Bisnis: Akses Riwayat Log dan Ingestion Audit Otomatis saat Status Client Suspended/Expired

## Prerequisites

- Kredensial akun Total Control pada entitas Client yang berstatus Suspended / Expired
- Terdapat aksi sistem otomatis yang berjalan pada client yang ditangguhkan

## Test Steps

### Akses Riwayat saat Client Suspended
1. Login sebagai Total Control pada Client yang berstatus Suspended/Expired.
2. Buka menu Global Settings > Activity Log pada kedua tab (Session dan User Action).
3. Verifikasi pengguna tetap dapat melihat seluruh riwayat aktivitas masa lalu tanpa blokade.
### Ingestion Aksi Sistem pada Client Suspended
4. Saat Client dalam status suspended, jalankan aksi sistem otomatis pada entitas tersebut.
5. Amati Tab User Action pada akun Client Suspended.
6. Verifikasi entri aksi sistem tetap tercatat secara normal di tabel audit trail.

## Notes

- Penangguhan akun client tidak menghilangkan hak akses ke audit trail masa lalu dan tidak menghentikan pencatatan audit sistem.
