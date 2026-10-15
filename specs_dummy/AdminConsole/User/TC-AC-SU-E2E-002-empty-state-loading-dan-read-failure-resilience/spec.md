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
- Mode: mock
- Login sebagai Role: Total Control
- Mock endpoint `POST /v2/iam/products/admin_console/users/list` untuk simulasi kegagalan server dan hasil kosong

## Test Steps

### Simulasi Error Fetch 500 & Pemulihan
1. Intercept request `POST /v2/iam/products/admin_console/users/list` dan kembalikan response HTTP 500 Internal Server Error
2. Buka menu navigasi `Admin Console > Settings > User`
3. Verifikasi tabel User List menampilkan error state dengan pesan literal `"Unable to load this data."` beserta tombol `[Try Again]`
4. Hapus mock error dan kembalikan response sukses 200 dengan data pengguna valid
5. Klik tombol `[Try Again]`
6. Verifikasi indikator loading muncul dan tabel berhasil memuat daftar data pengguna secara normal

### Empty State Filter & Pencarian
7. Ketik kata kunci acak pada Search input yang tidak cocok dengan data pengguna manapun (misal: `"xyznonexistentquery999"`)
8. Tekan Enter untuk menerapkan pencarian
9. Verifikasi tabel menampilkan empty state dengan judul literal `"No results found"` dan subjudul `"Try adjusting your search or filter."`
10. Kosongkan kembali Search input dan verifikasi seluruh baris data pengguna kembali tampil di tabel

## Notes

- Menguji ketahanan UI saat terjadi gangguan backend dan kejelasan pesan feedback saat query pencarian tidak menghasilkan data.
