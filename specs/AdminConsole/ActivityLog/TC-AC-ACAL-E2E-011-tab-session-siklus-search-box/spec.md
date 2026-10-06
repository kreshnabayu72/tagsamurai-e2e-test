---
id: TC-AC-ACAL-E2E-011-tab-session-siklus-search-box
title: "Tab Session — Siklus interaksi Search Box (reveal, clear, submit, collapse)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-45
coverage:
  web: automated
---

# Tab Session — Siklus interaksi Search Box (reveal, clear, submit, collapse)

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data riwayat aktivitas

## Test Steps

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik icon Search `[🔍]` di toolbar
3. Verifikasi kotak input search terbuka (reveal) dan kursor otomatis fokus (auto-focus)
4. Ketik keyword `"john"` ke dalam kotak input
5. Verifikasi icon `✕` (Clear) muncul di dalam kotak input, dan tabel belum langsung tersaring sebelum Enter ditekan
6. Tekan tombol Enter pada keyboard
7. Verifikasi tabel tersaring menampilkan hasil pencarian `"john"`
8. Klik icon `✕` di dalam kotak input
9. Verifikasi teks `"john"` terhapus, namun tabel belum otomatis mereset hasil pencarian
10. Tekan Enter pada kotak input yang kosong
11. Verifikasi tabel mereset hasil dan kembali menampilkan seluruh data
12. Masukkan kembali keyword `"john"` dan tekan Enter
13. Klik icon panah runtuh `[←]` (Collapse Search)
14. Verifikasi kotak search tertutup (collapse) dan tabel otomatis mereset penyaringan kembali ke tampilan penuh

## Notes

- Memverifikasi siklus lengkap keyboard and mouse event pada komponen toolbar Search TAG Samurai.
