---
id: TC-GS-DIV-E2E-040-tabel-utama-pola-interaksi-search-box-toolbar
title: "Pola Interaksi Search Box Toolbar: Reveal, Auto-Focus, Enter, Clear, dan Collapse"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-57
coverage:
  web: automated
---

# Pola Interaksi Search Box Toolbar: Reveal, Auto-Focus, Enter, Clear, dan Collapse

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik ikon Search pada toolbar TableTools
3. Verifikasi input search box melebar (reveal), placeholder 'Search division name...' muncul, dan kursor otomatis fokus pada input
4. Ketik 'Marketing' tanpa menekan Enter dan verifikasi tabel BELUM tersaring (search tidak bersifat live-as-you-type)
5. Tekan tombol Enter pada keyboard dan verifikasi pencarian dieksekusi
6. Klik icon clear '(✕)' di dalam input box
7. Verifikasi teks input menjadi kosong, namun tabel TIDAK langsung reset (tetap menampilkan hasil pencarian terakhir sampai Enter ditekan kembali pada input kosong)
8. Klik icon panah kembali '(←)' di samping input search box
9. Verifikasi search box menciut (collapse) kembali menjadi ikon dan filter pencarian tabel di-reset sepenuhnya

## Notes

- Pola interaksi search box toolbar mengikuti prd-conventions.md §9.1b dan §9.4.
