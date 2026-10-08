---
id: TC-GS-GSET-E2E-014-save-gagal-timeout-dan-double-submit
title: Save gagal, timeout, dan double-submit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-31
  - TC-GS-GSET-39
  - TC-GS-GSET-40
coverage:
  web: automated
mock: true
---

# Save gagal, timeout, dan double-submit

## Prerequisites

- Spec ini dijalankan dengan `Mode: mock`. Simulasi kegagalan PUT menyimpan data tahun:
  - Mock A: PUT `settings/general` mengembalikan 500 (setelah slicing)
  - Mock B: PUT `settings/general` menggantung lebih lama dari batas waktu (delay > timeout)
  - Mock C: PUT `settings/general` sukses; script mengklik `[Save]` dua kali berturut tanpa menunggu
- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).

## Test Steps

### Save gagal 5xx

1. Buka halaman `Global Settings > General Settings` dengan mock A aktif
2. Ubah `Session Idle Timeout` menjadi `8 hours`
3. Klik `[Save]`
4. Verifikasi toast error `Error, failed to save general settings.` tampil
5. Verifikasi tab Form tetap pada halaman yang sama (tidak refresh ke data lain)
6. Verifikasi nilai form yang diedit tetap tampil (belum hilang)
7. Verifikasi tombol `[Save]` tetap aktif sehingga User dapat mencoba lagi

### Save timeout

8. Set mock B (delay > timeout); ubah `Session Idle Timeout` menjadi `15 minutes`
9. Klik `[Save]`
10. Verifikasi tombol `[Save]` menampilkan indikator proses
11. Verifikasi setelah melewati batas waktu, toast error `Error, failed to save general settings.` muncul
12. Verifikasi `[Save]` kembali aktif dan nilai form tidak hilang

### Double-submit diblokir

13. Set mock C (sukses); ubah `Session Idle Timeout` menjadi `1 hour`
14. Klik `[Save]` dua kali cepat tanpa menunggu respons pertama
15. Verifikasi tombol `[Save]` terkunci/in-progress selama permintaan pertama belum selesai sehingga
    klik kedua tidak memicu permintaan kedua
16. Verifikasi hanya satu toast sukses yang muncul (tidak ada duplikasi simpan)
17. Verifikasi halaman tidak menghasilkan perubahan data dobel (maksimal satu PUT)

## Notes

- Untuk menegakkan determinisme, script menggunakan environment/instance terisolasi per run pada
  langkah double-submit agar jumlah PUt tidak menjadi ambigu.