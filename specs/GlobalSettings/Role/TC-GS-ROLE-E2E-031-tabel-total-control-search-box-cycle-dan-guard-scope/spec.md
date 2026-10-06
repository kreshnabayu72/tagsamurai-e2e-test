---
id: TC-GS-ROLE-E2E-031-tabel-total-control-search-box-cycle-dan-guard-scope
title: "Pola Interaksi Search Box Toolbar Tab Total Control dan Guard Kolom Non-Searchable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-127
  - TC-GS-ROLE-315
coverage:
  web: automated
---

# Pola Interaksi Search Box Toolbar Tab Total Control dan Guard Kolom Non-Searchable

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia beberapa data user Total Control dengan nama, tanggal, dan status yang berbeda

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik icon Search pada toolbar untuk membuka search box
3. Verifikasi search box terbuka dengan fokus otomatis pada input teks
4. Ketik keyword nama user tertentu (mis. 'totalControl2') lalu tekan Enter
5. Verifikasi tabel memfilter dan hanya menampilkan baris yang cocok dengan keyword
6. Klik icon silang (✕) pada sisi kanan search box
7. Verifikasi teks terhapus dari input, namun tabel tetap menampilkan hasil pencarian sebelumnya
8. Tekan Enter pada input yang kosong
9. Verifikasi tabel kembali menampilkan seluruh data Total Control secara lengkap
10. Ketik keyword yang merupakan nilai dari kolom Last Updated atau Status lalu tekan Enter
11. Verifikasi pencarian tidak mencocokkan kolom Last Updated dan Status (guard non-searchable)
12. Klik icon panah kembali (←) di sebelah kiri search box
13. Verifikasi search box menutup (collapse) dan tabel ter-reset secara instan

## Notes

- Pola interaksi search toolbar platform TAG Samurai: Enter untuk submit, (✕) clear teks tanpa reset tabel, Enter kosong untuk reset, dan (←) untuk collapse (prd-conventions §9.4).
