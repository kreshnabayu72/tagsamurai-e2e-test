---
id: TC-GS-GSET-E2E-021-pola-interaksi-search-box-dan-kolom-hidden
title: Pola interaksi search box dan pencarian saat kolom hidden
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-50
  - TC-GS-GSET-154
coverage:
  web: automated
---

# Pola interaksi search box dan search tetap berlaku pada kolom hidden

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data changelog dikenal: baris dengan `Action=Edit` dan `Field=Time Zone`.

## Test Steps

### Pola interaksi search box (fokus, debounce, clear)

1. Buka Modal Changelog
2. Klik ikon/tombol `Search`
3. Verifikasi input pencarian tampil dengan placeholder yang sesuai (misal
   `Search action, field, or value...`)
4. Ketik `Time` dan berhenti sejenak
5. Verifikasi hasil pencarian muncul (mendukung debounce)
6. Verifikasi tombol/X untuk menghapus pencarian tersedia di dalam search box
7. Klik tombol hapus
8. Verifikasi seluruh baris tampil kembali dan input pencarian kosong
9. Klik di luar search box / tekan `Esc`; verifikasi search box tertutup (kolaps) dan hasil kembali penuh

### Pencarian tetap berlaku saat kolom di-hide

10. Pilih data yang memiliki `Field=Time Zone`
11. Buka Setup Column, sembunyikan kolom `Field` (lihat spec 029 untuk langkah teknis yang telah diuji)
12. Tutup Setup Column dan pastikan kolom `Field` tidak tampil pada tabel
13. Masukkan pencarian `Time Zone`
14. Verifikasi baris dengan `Field=Time Zone` tetap tampil meskipun kolom `Field` tersembunyi
15. Masukkan pencarian nilai yang hanya ada di kolom tersembunyi (`Field`)
16. Verifikasi tetap menemukan baris; search tidak bergantung pada visibilitas kolom
17. Kembalikan kolom `Field` ke tampil lewat Setup Column (guard layer spec 032)

## Notes

- Perilaku "search working on hidden columns" membuktikan logika pencarian berjalan pada seluruh kolom
  yang diizinkan, bukan hanya kolom yang terlihat. Interaksi ini berdiri sendiri dari interaksi
  filter/sort yang diuji pada spec 025.