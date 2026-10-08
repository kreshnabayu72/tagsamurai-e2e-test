---
id: TC-GS-POS-E2E-029-mobile-selection-toolbar-dan-bulk-delete
title: "Mobile: Long-press card selection mode, toolbar, menu card, dan Bulk Delete di mobile viewport"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-151
  - TC-GS-POS-298
  - TC-GS-POS-304
coverage:
  web: automated
---

# Mobile: Long-press card selection mode, toolbar, menu card, dan Bulk Delete di mobile viewport

## Prerequisites

- Login sebagai Total Control
- Emulasi Viewport Mobile (375 x 812 px)

## Test Steps

### Tampilan Mobile Toolbar & Card List

1. Atur viewport browser ke ukuran mobile (375x812)
2. Buka Global Settings > User > Position
3. Verifikasi daftar Position ditampilkan dalam format card list (bukan tabel lebar)
4. Verifikasi header toolbar mobile menampilkan tombol "[+ Position]" dan kontrol pencarian ringkas
5. Verifikasi tiap card menampilkan nama jabatan dan menu titik tiga (⋯) card

### Long-Press Selection Mode & Bulk Delete

6. Lakukan aksi touch long-press pada salah satu card Position
7. Verifikasi aplikasi masuk ke mode multi-seleksi dan checkbox pada card muncul
8. Centang card kedua
9. Verifikasi Bulk Action Bar mobile muncul di bagian bawah
10. Klik tombol "[Delete]" pada Bulk Action Bar mobile dan konfirmasi penghapusan
11. Verifikasi kedua record terhapus dan mode seleksi otomatis keluar

## Notes

- Menggabungkan aturan khusus mobile dari TC-GS-POS-151, 298, dan 304 per keputusan NC-10.
