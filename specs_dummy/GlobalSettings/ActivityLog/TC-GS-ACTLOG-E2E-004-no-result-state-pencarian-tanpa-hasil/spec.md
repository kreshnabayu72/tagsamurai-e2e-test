---
id: TC-GS-ACTLOG-E2E-004-no-result-state-pencarian-tanpa-hasil
title: "Tampilan No-Result State Akibat Pencarian dan Filter Tanpa Hasil serta Pemulihan Data"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-06
  - TC-GS-ACTLOG-07
  - TC-GS-ACTLOG-108
coverage:
  web: automated
---

# Tampilan No-Result State Akibat Pencarian dan Filter Tanpa Hasil serta Pemulihan Data

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log aktivitas Session dan User Action

## Test Steps

### No-Result State via Search
1. Buka Tab Session, klik icon Search, ketik kata kunci non-existent 'zzznotfound', lalu tekan Enter.
2. Verifikasi area tabel menampilkan ilustrasi No-Result dengan Title 'No results found' dan Description 'Try adjusting your search or filter.'.
3. Klik tab 'User Action', ketik kata kunci 'zzznotfound' di kotak Search lalu tekan Enter.
4. Verifikasi Tab User Action menampilkan ilustrasi 'No results found' dengan Description 'Try adjusting your search or filter.'.
### No-Result State via Filter
5. Kosongkan kotak Search di Tab Session, buka Filter Panel, pilih rentang tanggal masa lalu yang tidak memiliki data (misal 1 Jan 2020), lalu klik [Apply].
6. Verifikasi area tabel Tab Session menampilkan ilustrasi 'No results found'.
7. Terapkan filter tanggal yang sama pada Tab User Action, verifikasi ilustrasi 'No results found' muncul.
### Pemulihan Data (Recovery)
8. Pada Tab Session dengan kondisi filter dan search menghasilkan 0 baris (misal Search 'Budi' dan Filter User 'John Doe'), kosongkan kata kunci pencarian lalu tekan Enter.
9. Verifikasi tabel Tab Session pulih menampilkan baris milik 'John Doe' sesuai filter yang tersisa.
10. Pada Tab User Action (Search 'Acme' dan Filter Action 'Create'), kosongkan pencarian lalu tekan Enter.
11. Verifikasi tabel Tab User Action pulih menampilkan baris Action 'Create'.

## Notes

- No-result state memberikan petunjuk jelas bagi pengguna untuk menyesuaikan kembali filter atau kata kunci pencarian.
