---
id: TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi
title: "Screening Bulk Action Bar, counter realtime, Select All N records lintas halaman, Unselect All, dan retensi state"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-123
  - TC-GS-POS-124
  - TC-GS-POS-125
  - TC-GS-POS-126
  - TC-GS-POS-127
  - TC-GS-POS-128
  - TC-GS-POS-129
  - TC-GS-POS-130
  - TC-GS-POS-131
  - TC-GS-POS-132
  - TC-GS-POS-133
  - TC-GS-POS-134
coverage:
  web: automated
---

# Screening Bulk Action Bar, counter realtime, Select All N records lintas halaman, Unselect All, dan retensi state

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Position berisi ≥15 record (Pre-setup 20 s.d. 34) tersebar di minimal 2 halaman

## Test Steps

### Screening Bulk Action Bar & Counter

1. Buka Global Settings > User > Position
2. Centang 1 baris checkbox Position
3. Verifikasi Bulk Action Bar melayang (floating) muncul di bagian bawah layar menampilkan: teks counter "1 position selected", tombol aksi "[Delete]", dan ikon batal `[✕]`
4. Centang baris kedua, verifikasi counter berubah realtime menjadi "2 positions selected"
5. Klik ikon `[✕]` pada Bulk Action Bar, verifikasi seluruh centang dibatalkan dan Bulk Action Bar menghilang

### Checkbox Header & Indeterminate State

6. Centang sebagian baris pada halaman 1
7. Verifikasi checkbox di header tabel berada dalam state indeterminate (ikon strip horizontal)
8. Klik checkbox header tabel
9. Verifikasi seluruh 10 baris pada halaman aktif langsung terpilih dan checkbox header menjadi checked penuh

### Select All Lintas Halaman & Unselect All

10. Saat seluruh baris halaman 1 terpilih, verifikasi banner/tombol "Select all {N} positions" muncul
11. Klik "Select all {N} positions"
12. Verifikasi counter pada Bulk Action Bar berubah menjadi "{N} positions selected" (mencakup seluruh record lintas halaman)
13. Verifikasi tombol berubah menjadi "Unselect all"
14. Klik "Unselect all"
15. Verifikasi seluruh seleksi di seluruh halaman dibatalkan

### Retensi Seleksi Saat Navigasi

16. Centang 3 baris pada halaman 1
17. Pindah ke halaman 2 via pagination
18. Centang 2 baris pada halaman 2
19. Lakukan filter atau sort pada tabel
20. Verifikasi counter Bulk Action Bar tetap mencatat total 5 baris terpilih dan seleksi tidak hilang

## Notes

- Menggabungkan protokol seleksi tabel dan toolbar bulk action dari TC-GS-POS-123 s.d. 134.
