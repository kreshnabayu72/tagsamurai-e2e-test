---
id: TC-GS-USER-E2E-094-list-search-box-interaksi
title: 'Siklus interaksi search box di toolbar User List'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-126
coverage:
  web: automated
---

# Siklus interaksi search box di toolbar User List

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan user "Budi Santoso" (Division `Finance`) dan user di Division lain

## Test Steps

1. Hover ikon Search di toolbar
2. Verifikasi tooltip "Search" muncul
3. Klik ikon Search
4. Verifikasi search bar melebar (reveal), kursor otomatis fokus, dan placeholder tampil
5. Ketik "Finance" tanpa menekan Enter
6. Verifikasi ikon `(✕)` muncul dan tabel belum tersaring (search bukan live-as-you-type)
7. Tekan `Enter`
8. Verifikasi tabel baru menyaring baris yang cocok di kolom Name, Email, Position, Division, Access, Employee ID, dan Modified By, dan tidak mencari di kolom Toggle Active atau Last Update
9. Klik ikon `(✕)`
10. Verifikasi teks input langsung kosong, search bar tetap terbuka dengan kursor fokus, dan tabel belum reset (masih menampilkan hasil pencarian terakhir)
11. Tekan `Enter` pada input kosong
12. Verifikasi tabel baru reset ke semua data
13. Ketik "Finance" lagi, tekan `Enter`, lalu klik ikon panah kembali `(←)` di kiri search bar
14. Verifikasi search bar collapse kembali ke ikon Search

## Notes

- Sumber `user.md` bagian 4.4 (pencarian) dan 9.1a. Teks placeholder search bar di TC sumber (`"Search name or email..."`) tidak didefinisikan di PRD, jadi tidak diverifikasi di spec ini. Lihat `GAP-284`.
- Pencarian parsial, case-insensitive, dan filter kombinasi dicakup `TC-GS-USER-E2E-098-list-search-parsial-dan-filter-kombinasi`.
