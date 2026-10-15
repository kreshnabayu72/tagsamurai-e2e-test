---
id: TC-GS-GSET-E2E-027-changelog-pagination-default-page-size-navigasi-input-dan-retensi-kriteria
title: "Pagination Changelog: default 10, page size, navigasi next/prev, input nomor halaman, dan reset ke halaman 1 saat Search/Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-102
  - TC-GS-GSET-157
  - TC-GS-GSET-180
  - TC-GS-GSET-181
coverage:
  web: automated
---

# Pagination Changelog: default 10, page size, navigasi next/prev, input nomor halaman, dan reset ke halaman 1 saat Search/Filter

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi minimal 26 baris; hasil Search "Edit" dengan Filter Modified By `Budi S` berisi ≥11 baris

## Test Steps

### Default, Page Size, dan Navigasi

1. Buka Modal Changelog dan amati pagination
2. Verifikasi default 10 baris per halaman
3. Verifikasi opsi page size 10 / 25 / 50 / 100
4. Klik halaman berikutnya lalu sebelumnya dan verifikasi navigasi menampilkan halaman yang sesuai
5. Ubah page size ke 25, lalu 50, lalu 100 dan verifikasi tiap perubahan

### Input Nomor Halaman Langsung

6. Ketik `2` pada input nomor halaman lalu tekan `Enter`
7. Verifikasi langsung berpindah ke halaman 2
8. Ketik `3` pada input nomor halaman lalu tekan `Enter`
9. Verifikasi langsung berpindah ke halaman 3

### Reset ke Halaman 1 saat Search dan Filter

10. Klik halaman 2
11. Search "Edit" lalu `Enter`
12. Verifikasi tabel kembali ke halaman 1
13. Klik halaman 2 lagi
14. Buka Filter, pilih Modified By `Budi S`, lalu klik `[Apply]`
15. Verifikasi tabel kembali ke halaman 1

### Retensi Kriteria Antar Halaman

16. Search "Edit" lalu `Enter`
17. Buka Filter, pilih Modified By `Budi S`, klik `[Apply]`
18. Klik header Field sekali (Ascending)
19. Klik halaman 2, lalu klik halaman 1
20. Verifikasi kotak Search tetap berisi "Edit", chip `Budi S` tetap di Filter Panel, dan indikator sort Field Ascending tetap aktif
21. Verifikasi halaman 2 dan halaman 1 menampilkan baris sesuai ketiga kriteria tersebut

## Notes

- Menggabungkan TC-GS-GSET-102, 157, 180, dan 181 (Pagination Changelog).
