---
id: TC-GS-USER-E2E-119-list-loading-no-result-gagal-muat
title: 'User List: loading, hasil pencarian kosong, dan gagal memuat data'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-3
coverage:
  web: automated
---

# User List: loading, hasil pencarian kosong, dan gagal memuat data

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons daftar user ditunda beberapa detik di pemuatan pertama; pada percobaan berikutnya dibalas `500` sekali lalu sukses

## Test Steps

1. Buka Global Settings > User saat respons masih ditunda
2. Verifikasi komponen loading tampil
3. Setelah data tampil, cari "zzznotfound" dan tekan `Enter`
4. Verifikasi ilustrasi dan pesan "No results found" dengan deskripsi "Try adjusting your search or filter."
5. Muat ulang halaman saat server membalas `500`
6. Verifikasi pesan "Failed to load data" dengan deskripsi "Something went wrong while fetching data." dan tombol `[Retry]`
7. Klik `[Retry]` saat server sudah membalas sukses
8. Verifikasi data tampil kembali

## Notes

- Sumber `user.md` bagian 7 (states).
