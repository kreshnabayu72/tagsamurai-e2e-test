---
id: TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping
title: "Ekspor Data Tabel Utama: Popover Download CSV dan XLSX, Nama Berkas Default Division, Filter Aktif Terfleksi, dan Format Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-178
  - TC-GS-DIV-179
  - TC-GS-DIV-180
  - TC-GS-DIV-181
  - TC-GS-DIV-182
  - TC-GS-DIV-185
  - TC-GS-DIV-187
coverage:
  web: automated
---

# Ekspor Data Tabel Utama: Popover Download CSV dan XLSX, Nama Berkas Default Division, Filter Aktif Terfleksi, dan Format Tanggal

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)
- General Settings Date Format `DD/MM/YY` (default)

## Test Steps

### Setup Column: kolom visible terakhir tidak dapat di-uncheck (TC-GS-DIV-178)

1. Buka Popup Setup Column
2. Hilangkan centang `Code` dan `Last Updated`
3. Hover checkbox `Name`
4. Verifikasi Checkbox `Name` disabled dan tidak dapat di-uncheck
5. Verifikasi Tooltip: `At least one column must remain visible.`

### Konfigurasi kolom tabel Division tidak memengaruhi tabel Changelog (TC-GS-DIV-179)

6. Sembunyikan kolom `Code` pada tabel Division lalu Save
7. Buka Modal Changelog dan perhatikan kolomnya
8. Verifikasi Modal Changelog tetap menampilkan seluruh 7 kolomnya (cache per tabel independen)

### Screening menu Download tabel Division (TC-GS-DIV-180)

9. Klik icon Download
10. Verifikasi Popover menampilkan opsi `Download CSV` dan `Download XLSX`

### Download tanpa Search dan Filter mengekspor seluruh baris (TC-GS-DIV-181)

11. Klik icon Download lalu `Download CSV`
12. Buka file hasil unduhan
13. Verifikasi File bernama `Division.csv` terunduh
14. Verifikasi File memuat seluruh 32 baris (bukan hanya halaman yang tampil)
15. Verifikasi Tidak ada toast sukses

### Download dengan Search dan Filter aktif hanya mengekspor baris yang cocok (TC-GS-DIV-182)

16. Cari `a` lalu Enter dan terapkan Filter rentang tanggal pre-setup
17. Klik Download lalu `Download XLSX`
18. Buka file hasil unduhan
19. Verifikasi File bernama `Division.xlsx` terunduh
20. Verifikasi File hanya memuat baris yang cocok dengan Search dan Filter aktif

### Download berhasil tidak menampilkan toast sukses (TC-GS-DIV-185)

21. Klik Download lalu `Download CSV`
22. Perhatikan layar sampai file terunduh
23. Verifikasi File langsung terunduh
24. Verifikasi Tidak ada toast sukses

### Isi file ekspor memakai format tanggal General Settings dan nilai kosong tidak ada (TC-GS-DIV-187)

25. Klik Download lalu `Download CSV`
26. Buka file hasil unduhan dan lihat kolom `Last Updated`, `Name`, `Code`
27. Verifikasi Kolom `Last Updated` memakai format tanggal dan jam General Settings
28. Verifikasi Kolom `Name` dan `Code` terisi pada seluruh baris (tidak ada sel `-`)

## Notes

- Memvalidasi menu download toolbar, pemilihan format CSV dan XLSX, nama berkas default "Division", data terunduh mencakup filter/search yang sedang aktif, ketiadaan toast sukses palsu, dan format tanggal General Settings dalam file (PRD §4.1 #13, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-178, TC-GS-DIV-179, TC-GS-DIV-180, TC-GS-DIV-181, TC-GS-DIV-182, TC-GS-DIV-185, TC-GS-DIV-187.
