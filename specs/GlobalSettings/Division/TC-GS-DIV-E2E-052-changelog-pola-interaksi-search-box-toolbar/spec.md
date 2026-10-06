---
id: TC-GS-DIV-E2E-052-changelog-pola-interaksi-search-box-toolbar
title: "Pola Interaksi Search Box Toolbar Modal Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-96
coverage:
  web: automated
---

# Pola Interaksi Search Box Toolbar Modal Changelog

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka Modal Changelog Division
2. Klik ikon Search pada toolbar Changelog
3. Verifikasi input search box reveal dan kursor auto-focus
4. Ketik keyword tanpa menekan Enter dan verifikasi tabel tidak reaktif
5. Tekan Enter dan verifikasi pencarian dieksekusi
6. Klik icon clear '(✕)' dan verifikasi teks terhapus sementara hasil pencarian tetap tampil hingga Enter ditekan ulang
7. Klik icon collapse '(←)' dan verifikasi search box menutup dan filter pencarian ter-reset

## Notes

- Pola interaksi search toolbar pada modal changelog identik dengan tabel utama.
