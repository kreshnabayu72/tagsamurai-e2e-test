---
id: TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit
title: "Penanganan Konflik Konkurensi Antar-Pengguna: Concurrent Edit, Delete, Duplicate, dan Limit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-186
  - TC-GS-DIV-187
  - TC-GS-DIV-188
  - TC-GS-DIV-251
  - TC-GS-DIV-252
  - TC-GS-DIV-253
coverage:
  web: automated
---

# Penanganan Konflik Konkurensi Antar-Pengguna: Concurrent Edit, Delete, Duplicate, dan Limit

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mocking response konflik konkuren (HTTP 409 Conflict)

## Test Steps

1. Buka modal Edit pada divisi 'Finance'
2. Simulasikan kondisi di mana admin lain telah menghapus divisi tersebut di latar belakang
3. Klik tombol '[Save]'
4. Verifikasi sistem mengembalikan penolakan 409 / data tidak ditemukan dengan pesan 'This division is no longer available.'
5. Simulasikan 2 admin secara bersamaan membuat divisi baru dengan nama yang sama persis
6. Verifikasi transaksi kedua ditolak dengan inline error duplikasi dan modal tetap terbuka untuk input baru
7. Simulasikan race condition pada slot terakhir Master Data Count Limit
8. Verifikasi request yang datang belakangan diblokir aman oleh re-check atomik limit saat submit

## Notes

- Menguji dimensi konkurensi D6 dan Action Resilience Spec division.md §9.4 dan §9.6.
