---
id: TC-GS-POS-E2E-046-master-data-count-limit
title: Master Data Count Limit sebagai Ceiling
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-85
  - TC-GS-POS-86
  - TC-GS-POS-196
  - TC-GS-POS-238
coverage:
  web: automated
---

# Master Data Count Limit sebagai Ceiling

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Diketahui batas limit jumlah Master Data Position (ceiling) sesuai konfigurasi sistem.
- Tersedia mekanisme validasi saat Create (manual dan/atau via import/create missing) yang memblokir jika melebihi limit.

## Test Steps

### A. Validasi saat mendekati limit

1. Siapkan kondisi jumlah Position mendekati limit (atau rekam kondisi saat ini).
2. Coba buat Position baru saat jumlah < limit → berhasil (Create sukses).
3. Coba buat Position tambahan hingga mencapai/mendekati ambang limit → perilaku sesuai batasan.

### B. Blokir saat mencapai/exceed limit

4. Pada kondisi jumlah Position == limit (atau mendekati ceiling), coba Create Position baru (manual).
5. Verifikasi operasi diblokir dengan pesan validasi terkait limit Master Data Count.
6. Verifikasi tidak ada Position baru tercipta; jumlah tetap tidak bertambah.
7. Uji jalur Create Missing Positions saat akan melampaui limit → diblokir/dibatasi sesuai aturan, tanpa menciptakan partial yang inkonsisten.

### C. Konsistensi pesan & state

8. Verifikasi pesan error konsisten (sesuai TC-GS-POS-85/86/196/238).
9. Verifikasi state tabel & logging tidak berubah saat diblokir (no side effects).
10. Setelah mengurangi jumlah (hapus salah satu), Create kembali diperbolehkan.

## Notes

- Master Data Count Limit berfungsi sebagai ceiling; validasi mencegah exceed limit dan menjaga konsistensi data.
