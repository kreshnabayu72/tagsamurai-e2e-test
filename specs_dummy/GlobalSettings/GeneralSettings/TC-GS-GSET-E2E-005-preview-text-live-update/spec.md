---
id: TC-GS-GSET-E2E-005-preview-text-live-update
title: Preview text waktu & mata uang update realtime
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-12
  - TC-GS-GSET-13
coverage:
  web: automated
---

# Preview text live update

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Form dalam keadaan isi default: `Date Format` = `dd/MM/yy`, `Time Format` = `HH:mm`, `Currency` = `IDR`.
- Data contoh untuk evaluasi preview diambil dari `Fixture.globalSettingsGeneralSettings.data.preview`.

## Test Steps

### Preview waktu mengikuti Date Format dan Time Format

1. Buka halaman `Global Settings > General Settings`
2. Verifikasi teks preview waktu tampil mengikuti format saat ini, yaitu `dd/MM/yy` + `HH:mm`
   (contoh `17/04/23 14:30`)
3. Ubah `Date Format` menjadi `M/d/yy`
4. Verifikasi teks preview langsung berubah mengikuti `M/d/yy` (contoh `3/17/23 14:30`)
5. Ubah `Time Format` menjadi `hh:mm a`
6. Verifikasi teks preview langsung berubah mengikuti `hh:mm a` (contoh `3/17/23 02:30 PM`)
7. Kembalikan kedua pilihan ke nilai awal, verifikasi preview kembali ke format awal

### Preview currency mengikuti pilihan Currency

8. Verifikasi teks preview currency menampilkan nilai ber-format mata uang saat ini (misal `Rp 5.000,00`)
9. Ubah `Currency` menjadi `$ - US Dollar`
10. Verifikasi teks preview berubah menjadi `$ 5.000,00` (ganti simbol, bukan konversi nilai)
11. Verifikasi perubahan preview terjadi tanpa melakukan operasi simpan

## Notes

- Preview selalu mencerminkan nilai di dalam kontrol (live update), bukan nilai terakhir tersimpan.
- PMC-GS `FORMAT-CONTRACT` dipenuhi: mengganti `Currency` hanya mengganti simbol, tidak mengubah besaran
  angka. Verifikasi ketiadaan konversi dilengkapi di spec 039.