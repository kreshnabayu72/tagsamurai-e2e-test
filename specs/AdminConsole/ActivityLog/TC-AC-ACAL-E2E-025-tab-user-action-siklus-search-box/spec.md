---
id: TC-AC-ACAL-E2E-025-tab-user-action-siklus-search-box
title: "Tab User Action — Siklus interaksi Search Box (reveal, clear, submit, collapse)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-137
coverage:
  web: automated
---

# Tab User Action — Siklus interaksi Search Box (reveal, clear, submit, collapse)

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data riwayat aktivitas

## Test Steps

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik icon Search `[🔍]` di toolbar
3. Verifikasi kotak search terbuka (reveal) dan kursor otomatis fokus
4. Ketik keyword `"Create"` ke dalam input box
5. Verifikasi icon `✕` muncul dan tabel belum menyaring sebelum tombol Enter ditekan
6. Tekan tombol Enter
7. Verifikasi tabel menyaring baris yang cocok dengan keyword `"Create"`
8. Klik icon `✕` di dalam kotak search
9. Verifikasi teks terhapus sementara tabel tetap menampilkan hasil filter sebelumnya
10. Tekan Enter pada kotak input yang kosong
11. Verifikasi tabel mereset hasil dan kembali menampilkan seluruh data
12. Masukkan kembali keyword `"Create"` dan tekan Enter
13. Klik icon panah runtuh `[←]` (Collapse Search)
14. Verifikasi kotak search tertutup dan tabel otomatis mereset pencarian

## Notes

- Memverifikasi konsistensi perilaku komponen Search Box pada Tab User Action.
