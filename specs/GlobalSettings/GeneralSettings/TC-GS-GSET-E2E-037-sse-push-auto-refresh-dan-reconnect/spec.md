---
id: TC-GS-GSET-E2E-037-sse-push-auto-refresh-dan-reconnect
title: SSE push auto-refresh FAMS/SAMS dan reconnect via snapshot
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-131
  - TC-GS-GSET-132
coverage:
  web: automated
---

# SSE push: refresh multiproduk dan pemulihan koneksi

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Environment menyediakan endpoint SSE yang dapat men-trigger event refresh FAMS/SAMS secara programatik.
- Konfigurasi menjamin koneksi SSE aktif saat halaman dibuka.

## Test Steps

### Push FAMS/SAMS memicu fetch ulang

1. Buka `Global Settings > General Settings`
2. Trigger push event FAMS dari sisi server (via helper/koneksi SSE test)
3. Verifikasi aplikasi menerima push dan melakukan fetch ulang data sehingga nilai form (misal
   `Session Idle Timeout`) yang diubah server ikut termuat
4. Trigger push event SAMS
5. Verifikasi aplikasi juga menerima push SAMS dan melakukan fetch ulang (nilai form konsisten)

### Reconnect saat koneksi putus

6. Simulasikan putusnya koneksi SSE (misal helper menutup event-stream di luar aplikasi atau
    mematikan socket)
7. Verifikasi aplikasi mendeteksi koneksi SSE hilang/error
8. Verifikasi aplikasi mencoba reconnect dalam jangka waktu wajar
9. Trigger push FAMS saat koneksi baru
10. Verifikasi setelah reconnect, push kembali bekerja dan fetch ulang tetap berjalan

### Konsistensi data setelah push

11. Lakukan mutasi form (ubah `Currency` via dialog, simpan)
12. Trigger push FAMS lagi
13. Verifikasi nilai form yang tampil sesuai state server terakhir (tidak regress ke nilai lama)
14. Verifikasi Modal Changelog (bila terbuka) juga memperbarui baris log setelah push

## Notes

- PMC `SSE-REFRESH-CONTRACT` terpenuhi: aplikasi fetch ulang data setelah push FAMS/SAMS dan memulihkan
  pesan stream yang hilang lewat GET snapshot saat reconnect (libat hubungan dengan spec 038).