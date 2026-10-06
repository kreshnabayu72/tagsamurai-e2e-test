---
id: TC-GS-DIV-E2E-002-loading-skeleton-dan-read-failure-resilience
title: "Loading State Skeleton dan Ketahanan Terhadap Gagal Fetch Data Awal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-03
  - TC-GS-DIV-05
  - TC-GS-DIV-06
coverage:
  web: automated
---

# Loading State Skeleton dan Ketahanan Terhadap Gagal Fetch Data Awal

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock network throttling untuk simulasi loading state
- Mock response endpoint POST /v2/iam/divisions/list disimulasikan gagal 500 / network error, kemudian pulih ke 200 OK

## Test Steps

1. Buka menu Global Settings > User > tab Division dengan kondisi jaringan lambat
2. Verifikasi tabel menampilkan skeleton placeholder / shimmer rows selama proses pemuatan data, bukan layar kosong atau blank
3. Kondisikan endpoint list division mengembalikan response error 500
4. Muat ulang halaman atau akses kembali tab Division
5. Verifikasi tabel menampilkan pesan kesalahan 'Unable to load this data.' beserta tombol '[Try Again]'
6. Pulihkan response endpoint list division ke kondisi normal (200 OK)
7. Klik tombol '[Try Again]'
8. Verifikasi pesan error hilang dan daftar baris data divisi berhasil dimuat normal

## Notes

- Mengikuti panduan penanganan error pembacaan tabel pada prd-conventions.md §7.
