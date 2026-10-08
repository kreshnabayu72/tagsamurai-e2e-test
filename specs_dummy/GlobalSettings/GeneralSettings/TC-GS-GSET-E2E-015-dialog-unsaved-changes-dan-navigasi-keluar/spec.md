---
id: TC-GS-GSET-E2E-015-dialog-unsaved-changes-dan-navigasi-keluar
title: Dialog Unsaved Changes dan navigasi keluar
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-32
  - TC-GS-GSET-33
  - TC-GS-GSET-34
  - TC-GS-GSET-35
  - TC-GS-GSET-151
coverage:
  web: automated
---

# Dialog Unsaved Changes: trigger, Stay, Leave, dan Changelog dirty

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- State awal `Session Idle Timeout = 30 minutes`, nilai `existing` lainnya sesuai fixture.

## Test Steps

### Pemicu saat ada perubahan

1. Buka halaman `Global Settings > General Settings`
2. Ubah `Session Idle Timeout` menjadi `8 hours`
3. Tanpa menyimpan, coba navigasikan ke menu lain (misal klik menu lain / link keluar pada sidebar)
4. Verifikasi dialog peringatan tampil dengan judul peringatan (misal `Unsaved Changes`)
5. Verifikasi body dialog menyebutkan bahwa perubahan belum disimpan dan akan hilang

### Stay (kembali)

6. Klik tombol `[Stay]`
7. Verifikasi dialog tertutup dan halaman tetap pada General Settings
8. Verifikasi nilai `8 hours` tetap tampil dan tombol `[Save]` masih aktif

### Leave (lanjut)

9. Klik `[Save]` dulu, verifikasi toast sukses
10. Ubah `Session Idle Timeout` menjadi `15 minutes`
11. Navigasikan ke menu lain; saat dialog tampil klik `[Leave]`
12. Verifikasi halaman berpindah ke tujuan navigasi
13. Kembali ke `Global Settings > General Settings`
14. Verifikasi nilai tersimpan masih `8 hours` dan `15 minutes` tidak tersimpan

### Navigasi tanpa perubahan tidak memicu dialog

15. Dengan tidak ada perubahan, navigasikan ke menu lain
16. Verifikasi tidak muncul dialog peringatan apa pun, halaman langsung berpindah

### Refresh/tab-close dengan perubahan (guard browser)

17. Ubah `Session Idle Timeout` menjadi `4 hours`
18. Coba refresh/reload halaman (atau simulasi close) melalui mekanisme yang dapat ditangkap spec
19. Verifikasi browser/devtool menampilkan prompt konfirmasi peringatan bahwa perubahan belum disimpan

### Changelog saat form masih dirty

20. Ubah `Session Idle Timeout` menjadi `2 hours`
21. Tanpa menyimpan, buka Modal Changelog (link Changelog di halaman)
22. Verifikasi modal tetap dapat dibuka dan menampilkan riwayat tersimpan (tidak memasukkan nilai `2 hours`)
23. Tutup modal; verifikasi form masih `2 hours` dan tombol `[Save]` aktif
24. Kembalikan `Session Idle Timeout` ke `30 minutes` untuk menutup spec

## Notes

- TC-GS-GSET-151 dibuktikan langkah 20-23: modal Changelog tidak memaksa menyimpan dan tidak kehilangan
  nilai form yang masih diedit.
- Navigasi "keluar" dimaknai sebagai pindah submenu dalam aplikasi, bukan log out sesi auth (separate).