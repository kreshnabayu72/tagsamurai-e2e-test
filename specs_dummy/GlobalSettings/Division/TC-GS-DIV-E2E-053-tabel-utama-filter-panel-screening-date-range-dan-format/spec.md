---
id: TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format
title: "Filter Panel Tabel Utama: Screening Panel, Date Range Picker, Kepatuhan Format Tanggal, dan Reset Clear Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-149
  - TC-GS-DIV-150
  - TC-GS-DIV-151
  - TC-GS-DIV-152
coverage:
  web: automated
---

# Filter Panel Tabel Utama: Screening Panel, Date Range Picker, Kepatuhan Format Tanggal, dan Reset Clear Field

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data dengan rentang tanggal Last Updated bervariasi
- General Settings Date Format DD/MM/YY (default)
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)
- Last Updated Division Pre-setup = tanggal pre-setup; Last Updated Division Data Uji Dinamis = hari uji
- General Settings Date Format `DD/MM/YY` (default)

## Test Steps

### Screening Filter Panel Tabel Division (TC-GS-DIV-149)

1. Perhatikan tabel sebelum filter dibuka
2. Klik icon Filter
3. Verifikasi Filter Panel tersembunyi secara default dan terbuka setelah klik icon Filter
4. Verifikasi Satu-satunya field: `Last Updated` bertipe date range picker dengan placeholder `Select date`
5. Verifikasi Aksi `[Clear Field]` dan `[Apply]`
6. Verifikasi Tidak ada field `Modified By`, `Division Name`, `Field`, atau `Action`

### Filter Last Updated menyaring baris dalam rentang tanggal (TC-GS-DIV-150)

7. Klik icon Filter
8. Pilih rentang tanggal yang hanya memuat tanggal pre-setup
9. Klik `[Apply]`
10. Verifikasi Tabel hanya menampilkan 6 Division Pre-setup
11. Verifikasi Division Data Uji Dinamis (hari uji) tidak tampil
12. Verifikasi Halaman kembali ke halaman 1

### Teks tanggal pada input Date filter mengikuti format General Settings (TC-GS-DIV-151)

13. Klik icon Filter
14. Pilih rentang tanggal pre-setup
15. Perhatikan teks pada input Last Updated
16. Verifikasi Teks nilai tanggal pada input Last Updated mengikuti Date Format General Settings (`DD/MM/YY`)

### Clear Field pada Filter Panel dan Apply mengembalikan seluruh data (TC-GS-DIV-152)

17. Klik icon Filter, pilih rentang tanggal pre-setup, klik `[Apply]`
18. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
19. Verifikasi Setelah Clear Field dan Apply tabel menampilkan seluruh 32 Division
20. Verifikasi Field Last Updated kosong

## Notes

- Memvalidasi panel filter tabel utama (FI-11): toggle buka/tutup panel, Last Updated sebagai satu-satunya field filter, date range picker memfilter baris dalam rentang, teks input mengikuti format General Settings (DD/MM/YY), dan tombol [Clear Field] mengembalikan seluruh data (PRD §4.1.1, §4.2, §4.4, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-149, TC-GS-DIV-150, TC-GS-DIV-151, TC-GS-DIV-152.
