---
id: TC-AC-ACAL-E2E-029-tab-user-action-kombinasi-multi-filter-dan-recovery
title: "Tab User Action — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-168
  - TC-AC-ACAL-169
  - TC-AC-ACAL-170
  - TC-AC-ACAL-171
  - TC-AC-ACAL-172
coverage:
  web: automated
---

# Tab User Action — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data yang banyak dan beragam

## Test Steps

### Kombinasi Harmonis 4 Kontrol

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Masukkan keyword `"Client"` pada kotak Search lalu tekan Enter
3. Buka Filter Panel, pilih Action `"Create"` dan Object `"Client"`, lalu klik `[Apply]`
4. Klik sort pada kolom `Date` (descending)
5. Ubah baris per halaman ke `25`
6. Verifikasi seluruh 4 kontrol berlaku harmonis bersamaan menyaring tabel tanpa bentrok

### Pelepasan Parsial Kontrol

7. Buka kembali Filter Panel, klik tombol `[Clear Field]`, lalu klik `[Apply]`
8. Verifikasi filter Action dan Object lepas, sementara keyword Search dan arah Sort Date tetap aktif
9. Klik icon `✕` pada Search box dan tekan Enter pada input kosong
10. Verifikasi Search ter-reset sementara arah Sort Date tetap aktif

### Transisi Target Sort & Recovery

11. Klik header kolom `Action` untuk mengaktifkan sort pada kolom Action
12. Verifikasi sort berpindah ke kolom Action tanpa merusak filter aktif
13. Terapkan kombinasi search dan filter yang menghasilkan state `"No results found"`
14. Hapus keyword search
15. Verifikasi tabel otomatis pulih (recovery) menampilkan data yang sesuai dengan kriteria filter yang tersisa

## Notes

- Memverifikasi independensi state antar kontrol toolbar di Tab User Action.
