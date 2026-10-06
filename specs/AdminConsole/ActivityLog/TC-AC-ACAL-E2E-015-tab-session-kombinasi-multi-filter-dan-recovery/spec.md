---
id: TC-AC-ACAL-E2E-015-tab-session-kombinasi-multi-filter-dan-recovery
title: "Tab Session — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-77
  - TC-AC-ACAL-78
  - TC-AC-ACAL-79
  - TC-AC-ACAL-80
  - TC-AC-ACAL-81
coverage:
  web: automated
---

# Tab Session — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data yang banyak dan beragam

## Test Steps

### Kombinasi Harmonis 4 Kontrol

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Masukkan keyword `"admin"` pada kotak Search lalu tekan Enter
3. Buka Filter Panel, pilih filter Position dan Division tertentu, lalu klik `[Apply]`
4. Klik sort pada kolom `Date` (descending)
5. Ubah baris per halaman (rows-per-page) menjadi `25`
6. Verifikasi seluruh 4 kontrol berlaku harmonis bersamaan menyaring tabel tanpa konflik

### Pelepasan Parsial Kontrol

7. Buka kembali Filter Panel, klik tombol `[Clear Field]`, lalu klik `[Apply]`
8. Verifikasi filter Division lepas, sementara keyword Search `"admin"` dan arah Sort Date tetap aktif menyaring tabel
9. Klik icon `✕` pada Search box dan tekan Enter pada input kosong
10. Verifikasi Search ter-reset sementara arah Sort Date tetap aktif

### Transisi Target Sort & Recovery

11. Klik header kolom `User` untuk mengaktifkan sort pada kolom User
12. Verifikasi sort berpindah ke kolom User tanpa merusak filter yang sedang aktif
13. Terapkan kombinasi search dan filter yang menghasilkan state `"No results found"`
14. Hapus keyword search
15. Verifikasi tabel otomatis pulih (recovery) menampilkan data yang sesuai dengan kriteria filter yang tersisa

## Notes

- Memverifikasi independensi state antar kontrol toolbar di Tab Session.
