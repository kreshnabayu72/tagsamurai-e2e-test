---
id: TC-GS-ACTLOG-E2E-012-tab-session-pola-interaksi-search-box-toolbar
title: "Tab Session: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-41
coverage:
  web: automated
---

# Tab Session: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session

## Test Steps

1. Buka Tab Session
2. Klik icon Search pada toolbar dan verifikasi input box melebar (reveal) serta fokus otomatis ke input
3. Ketik huruf "j" dan verifikasi icon `(✕)` muncul sementara tabel belum tersaring
4. Tekan tombol Enter dan verifikasi tabel mulai tersaring berdasarkan keyword "j"
5. Klik icon `(✕)` pada input search
6. Verifikasi teks terhapus bersih namun tabel tidak otomatis ter-reset
7. Tekan tombol Enter pada input yang kosong
8. Verifikasi tabel ter-reset kembali menampilkan seluruh data awal
9. Masukkan keyword "test", lalu klik icon panah kembali `(←)`
10. Verifikasi input search menutup (collapse) dan filter pencarian langsung ter-reset

## Notes

- Pola interaksi search toolbar mengikuti konvensi standar platform: submit on Enter, clear tanpa auto-reset.
