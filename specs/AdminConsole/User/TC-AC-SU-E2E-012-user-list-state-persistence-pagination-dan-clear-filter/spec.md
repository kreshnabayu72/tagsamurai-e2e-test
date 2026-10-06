---
id: TC-AC-SU-E2E-012-user-list-state-persistence-pagination-dan-clear-filter
title: "Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-232
  - TC-AC-SU-233
  - TC-AC-SU-281
  - TC-AC-SU-282
  - TC-AC-SU-283
  - TC-AC-SU-284
coverage:
  web: automated
---

# Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat dataset ≥50 data pengguna untuk pengujian pagination

## Test Steps

### Persistensi State Pencarian dan Filter

1. Buka halaman User List, masukkan kata kunci Search, pilih filter Status, dan terapkan pengurutan
2. Klik nama salah satu pengguna untuk masuk ke halaman Detail User
3. Kembali ke halaman User List, verifikasi kata kunci Search, saringan Filter, dan arah Sort tetap aktif
4. Muat ulang halaman browser (F5), verifikasi state Search dan Filter tetap dipulihkan dan tidak tereset

### Pengujian Clear Filter dan Clear Search

1. Buka Filter Panel, klik tombol `[Clear Field]` lalu klik `[Apply]`
2. Verifikasi kriteria Filter terlepas kembali ke default, sementara kata kunci Search dan arah Sort TETAP aktif
3. Klik icon `✕` pada input Search lalu tekan Enter
4. Verifikasi kata kunci Search terhapus dan tabel menampilkan data sesuai saringan Sort

### Pengujian Pagination dan Persistensi Halaman

1. Ubah pilihan page size dari 10 menjadi 25 lalu 50 pada pagination bar
2. Verifikasi jumlah baris yang tampil pada halaman mengikuti pilihan page size secara tepat
3. Navigasi ke halaman ke-2 pagination
4. Muat ulang halaman browser (F5)
5. Verifikasi nomor halaman aktif tetap berada di halaman ke-2 (tidak tereset ke halaman 1)

## Notes

- State filter dan pagination disimpan pada sessionStorage untuk kenyamanan navigasi admin.
