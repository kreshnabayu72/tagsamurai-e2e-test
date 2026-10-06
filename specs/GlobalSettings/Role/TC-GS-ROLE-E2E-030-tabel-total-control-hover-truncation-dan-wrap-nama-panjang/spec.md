---
id: TC-GS-ROLE-E2E-030-tabel-total-control-hover-truncation-dan-wrap-nama-panjang
title: "Tampilan Kolom Name Tab Total Control: Wrap Natural Nama Panjang dan Tooltip Lengkap via Hover serta Keyboard Focus"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-77
coverage:
  web: automated
---

# Tampilan Kolom Name Tab Total Control: Wrap Natural Nama Panjang dan Tooltip Lengkap via Hover serta Keyboard Focus

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tersedia user dengan nama sangat panjang ter-assign Total Control: Ahmad Fauzi Akbar Pratama Wijaya Kusuma

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Amati sel kolom Name pada baris user bernama panjang tersebut
3. Verifikasi kolom Name me-render avatar dan nama lengkap secara natural wrap (multi-baris penuh tanpa pemotongan teks terputus-putus ..)
4. Arahkan kursor mouse (hover) ke elemen nama user tersebut
5. Verifikasi tooltip muncul menampilkan nama lengkap utuh
6. Gunakan tombol navigasi keyboard (Tab) untuk memindahkan fokus ke elemen nama user tersebut
7. Verifikasi tooltip nama lengkap juga muncul melalui keyboard focus accessibility
8. Hover pada badge Status atau kolom lain yang teksnya terpotong dan verifikasi tooltip tampil sesuai konvensi

## Notes

- Kolom Name dengan avatar menerapkan pengecualian natural wrap multi-baris dan tooltip wajib dapat diakses via hover maupun focus (prd-conventions §9.13).
