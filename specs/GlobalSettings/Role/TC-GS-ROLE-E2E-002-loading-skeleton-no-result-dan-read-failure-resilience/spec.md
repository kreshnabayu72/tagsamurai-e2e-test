---
id: TC-GS-ROLE-E2E-002-loading-skeleton-no-result-dan-read-failure-resilience
title: "Loading State, No-Result Search, dan Ketahanan Terhadap Gagal Fetch Data"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-07
coverage:
  web: automated
---

# Loading State, No-Result Search, dan Ketahanan Terhadap Gagal Fetch Data

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tersedia kemampuan intersept API list role dan access level

## Test Steps

1. Buka menu Global Settings > Role & Permission
2. Simulasikan latensi jaringan saat memuat data awal tabel
3. Verifikasi komponen Loading skeleton tampil pada area body tabel sebelum data dirender
4. Ketik keyword pencarian 'zzznotfound' pada kotak Search toolbar Tab Total Control lalu tekan Enter
5. Verifikasi ilustrasi kosong tampil dengan Title: "No results found" dan Description: "Try adjusting your search or filter."
6. Hapus kata kunci pencarian dan pulihkan tabel
7. Simulasikan kegagalan jaringan atau respons error server 500 saat me-refresh data
8. Verifikasi pesan error "Unable to load this data." tampil beserta tombol [Try Again]
9. Klik tombol [Try Again] saat respons mock dipulihkan
10. Verifikasi data tabel berhasil dimuat ulang secara normal

## Notes

- Kasus kegagalan server dan loading state diuji menggunakan mode mock untuk menjamin determinisme pengujian.
