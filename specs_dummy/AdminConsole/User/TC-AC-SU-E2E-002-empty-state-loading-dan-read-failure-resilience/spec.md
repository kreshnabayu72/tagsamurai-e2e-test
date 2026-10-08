---
id: TC-AC-SU-E2E-002-empty-state-loading-dan-read-failure-resilience
title: "Loading state, simulasi error fetch 500, pemulihan via Try Again, dan empty state no results found"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-10
  - TC-AC-SU-11
coverage:
  web: automated
---

# Loading state, simulasi error fetch 500, pemulihan via Try Again, dan empty state no results found

## Prerequisites

- Mode: mock
- Login sebagai Role: Principal Total Control
- Simulasi mock network failure 500 pada endpoint GET users
- Simulasi mock respons kosong pada pencarian filter

## Test Steps

### Simulasi Network Failure 500 dan Pemulihan

1. Konfigurasikan mock network agar endpoint `GET /ac/users` mengembalikan status error `500 Internal Server Error`
2. Buka sidebar menu `Admin Console > Settings > User`
3. Verifikasi tabel tidak memuat data dan menampilkan ilustrasi error dengan teks `"Unable to load this data."` serta tombol `[Try Again]`
4. Hapus kondisi intercept mock failure agar endpoint mengembalikan data sukses
5. Klik tombol `[Try Again]`
6. Verifikasi skeleton loading muncul sesaat dan tabel User List berhasil dimuat dengan data lengkap

### Empty State Hasil Filter / Search

1. Masukkan kata kunci pencarian acak yang tidak cocok dengan data apa pun (contoh: `"xyznotfound999"`) pada kotak Search lalu tekan Enter
2. Verifikasi tabel menampilkan empty state dengan judul `"No results found"` dan subtitle `"Try adjusting your search or filter."`

## Notes

- Uji ketahanan UI terhadap kegagalan jaringan dan verifikasi kejelasan pesan empty state bagi pengguna.
