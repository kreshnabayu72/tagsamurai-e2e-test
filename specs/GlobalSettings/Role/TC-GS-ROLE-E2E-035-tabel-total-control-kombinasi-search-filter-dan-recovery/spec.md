---
id: TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery
title: "Kombinasi Penuh Search dan Multi-Filter Tab Total Control Serta Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-145
  - TC-GS-ROLE-146
  - TC-GS-ROLE-147
  - TC-GS-ROLE-148
  - TC-GS-ROLE-149
  - TC-GS-ROLE-150
  - TC-GS-ROLE-151
  - TC-GS-ROLE-152
  - TC-GS-ROLE-153
coverage:
  web: automated
---

# Kombinasi Penuh Search dan Multi-Filter Tab Total Control Serta Pemulihan Empty State

## Prerequisites

- Login sebagai Role: Total Control
- Data user lengkap di Tab Total Control

## Test Steps

1. Buka Tab Total Control
2. Masukkan keyword pencarian nama pada Search box (mis. 'total') lalu tekan Enter
3. Buka Filter Panel dan pilih filter Division tertentu, lalu klik [Apply]
4. Verifikasi tabel menampilkan irisan (AND logic) yang memenuhi kriteria Search dan Filter
5. Klik header kolom Name untuk melakukan sorting saat Search dan Filter aktif
6. Verifikasi data terurut dengan benar hanya di antara subset data yang terfilter
7. Buka Filter Panel dan klik [Clear All]
8. Verifikasi filter terhapus namun query pencarian Search tetap bertahan aktif
9. Ketik keyword pencarian kombinasi yang menghasilkan 0 hasil cocok
10. Verifikasi tabel menampilkan empty state "No results found" beserta tombol pemulihan [Clear Filter/Search]
11. Klik tombol pemulihan [Clear Filter/Search]
12. Verifikasi seluruh data tabel pulih kembali seperti semula

## Notes

- Pengujian kombinasi 4 kontrol membuktikan independensi state pencarian, filter, dan sorting (role.md §9.8).
