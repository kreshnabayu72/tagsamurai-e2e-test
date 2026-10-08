---
id: TC-GS-ACTLOG-E2E-031-pagination-kedua-tab-page-size-navigasi-dan-persistensi
title: "Paginasi Kedua Tab: Pilihan Page Size 10/25/50/100, Navigasi Halaman, dan Persistensi State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-118
  - TC-GS-ACTLOG-119
  - TC-GS-ACTLOG-120
  - TC-GS-ACTLOG-121
coverage:
  web: automated
---

# Paginasi Kedua Tab: Pilihan Page Size 10/25/50/100, Navigasi Halaman, dan Persistensi State

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat sekurang-kurangnya 100 baris entri log pada kedua tab

## Test Steps

### Pemilihan Page Size
1. Buka Tab Session, ubah page size ke 25, verifikasi tepat 25 baris data tampil.
2. Ubah page size ke 50, verifikasi tepat 50 baris data tampil.
3. Ubah page size ke 100, verifikasi tepat 100 baris data tampil.
4. Verifikasi tidak tersedia opsi 'All'.
5. Uji pergantian page size yang sama pada Tab User Action, verifikasi jumlah baris sesuai.
### Navigasi Halaman & Reset ke Halaman 1
6. Pada page size 10, klik tombol Next (halaman berikutnya), verifikasi halaman 2 tampil.
7. Klik tombol Previous, verifikasi kembali ke halaman 1.
8. Masukkan angka '3' di input nomor halaman lalu tekan Enter, verifikasi halaman 3 tampil.
9. Saat berada di halaman 3, masukkan kata kunci pencarian baru atau klik [Apply] pada filter.
10. Verifikasi sistem otomatis mereset posisi navigasi kembali ke halaman 1.
### Persistensi Refresh F5 vs Sidebar Reset
11. Atur Search, Filter, Sort, page size 25, dan buka halaman 2, lalu lakukan refresh browser (F5).
12. Verifikasi seluruh state paginasi dan filter tetap bertahan setelah refresh.
13. Klik ulang menu 'Activity Log' di sidebar navigasi.
14. Verifikasi seluruh search, filter, sort, dan paginasi otomatis kembali ke default (halaman 1, 10 baris per halaman, Date desc).

## Notes

- Paginasi mendukung navigasi cepat dan mematuhi konvensi reset ke halaman 1 saat filter diperbarui.
