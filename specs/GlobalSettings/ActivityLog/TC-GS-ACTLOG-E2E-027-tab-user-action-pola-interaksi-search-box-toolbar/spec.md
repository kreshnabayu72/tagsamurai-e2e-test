---
id: TC-GS-ACTLOG-E2E-027-tab-user-action-pola-interaksi-search-box-toolbar
title: "Tab User Action: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-132
coverage:
  web: automated
---

# Tab User Action: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action

## Test Steps

1. Buka Tab User Action
2. Klik icon Search pada toolbar dan verifikasi input box melebar serta fokus otomatis
3. Ketik sebagian teks dan verifikasi icon `(✕)` muncul tanpa menyaring tabel seketika
4. Tekan Enter dan verifikasi tabel tersaring berdasarkan keyword
5. Klik icon `(✕)` dan verifikasi input kosong namun tabel tidak auto-reset
6. Tekan Enter pada input kosong dan verifikasi tabel ter-reset menampilkan semua data
7. Masukkan keyword lalu klik icon panah kembali `(←)`
8. Verifikasi input search menutup (collapse) dan saringan pencarian langsung ter-reset

## Notes

- Pola interaksi toolbar search konsisten di kedua tab.
