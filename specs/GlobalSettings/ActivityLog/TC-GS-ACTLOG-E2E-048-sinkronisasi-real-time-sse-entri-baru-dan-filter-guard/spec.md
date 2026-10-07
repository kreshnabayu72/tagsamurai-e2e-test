---
id: TC-GS-ACTLOG-E2E-048-sinkronisasi-real-time-sse-entri-baru-dan-filter-guard
title: "Sinkronisasi Real-Time SSE: Kemunculan Otomatis Entri Baru dan Filter-Matching Guard di Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-195
  - TC-GS-ACTLOG-196
  - TC-GS-ACTLOG-197
coverage:
  web: automated
---

# Sinkronisasi Real-Time SSE: Kemunculan Otomatis Entri Baru dan Filter-Matching Guard di Kedua Tab

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Dua sesi browser aktif pada entitas Client yang sama

## Test Steps

### Realtime Streaming Tab Session
1. Buka Tab Session pada Sesi Browser 1 tanpa filter aktif.
2. Pada Sesi Browser 2, lakukan login sebagai pengguna 'Siti Nurbaya'.
3. Amati Sesi Browser 1 tanpa memuat ulang halaman secara manual.
4. Verifikasi baris login baru 'Siti Nurbaya' otomatis disisipkan di baris teratas tabel Tab Session.
### Realtime Streaming Tab User Action
5. Buka Tab User Action pada Sesi Browser 1.
6. Pada Sesi Browser 2, buat Brand baru 'Acme Corp' di modul Brand.
7. Amati Sesi Browser 1 tanpa reload manual.
8. Verifikasi baris aksi 'Create Brand Acme Corp' otomatis muncul di posisi teratas tabel.
### Filter-Matching Guard pada SSE
9. Pada Sesi Browser 1 di Tab Session, pasang filter Activity = 'Login'.
10. Pada Sesi Browser 2, lakukan Logout lalu Login kembali.
11. Verifikasi hanya event 'Login' yang otomatis disisipkan ke tabel; event 'Logout' tidak ditampilkan karena tidak lolos kriteria filter aktif.

## Notes

- Koneksi SSE memperbarui tabel secara reaktif dengan tetap menghormati aturan filter aktif.
