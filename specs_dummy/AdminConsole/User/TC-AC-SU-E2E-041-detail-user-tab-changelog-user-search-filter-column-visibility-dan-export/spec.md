---
id: TC-AC-SU-E2E-041-detail-user-tab-changelog-user-search-filter-column-visibility-dan-export
title: "Detail User Tab Changelog: Riwayat Mutasi User, Search, Filter Rentang Tanggal, dan Export"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-124
  - TC-AC-SU-126
  - TC-AC-SU-127
  - TC-AC-SU-128
  - TC-AC-SU-129
  - TC-AC-SU-130
  - TC-AC-SU-131
  - TC-AC-SU-132
  - TC-AC-SU-133
coverage:
  web: automated
---

# Detail User Tab Changelog: Riwayat Mutasi User, Search, Filter Rentang Tanggal, dan Export

## Prerequisites

- Login sebagai Total Control
- Target user memiliki riwayat mutasi identitas dan perubahan peran

## Test Steps

### Screening Struktur Kolom Tab Changelog
1. Buka Detail User target > klik tab `Changelog`
2. Verifikasi tabel memuat 6 kolom baku: `Date & Time`, `Field / Module`, `Action`, `Before`, `After`, `Modified By`

### Pencarian Toolbar dan Filter Rentang Tanggal
3. Masukkan kata kunci pencarian pada toolbar (misal: `"Role"`)
4. Verifikasi baris tabel tersaring menampilkan perubahan terkait role
5. Buka panel `[Filter]` dan atur filter rentang tanggal mutasi
6. Verifikasi data tersaring mematuhi batasan tanggal yang dipilih

### Setup Column dan Ekspor CSV
7. Buka modal `[Setup Column]` tab Changelog dan sesuaikan kolom yang aktif
8. Klik tombol `[Download]` untuk mengekspor rekaman riwayat perubahan
9. Verifikasi berkas CSV memuat rekaman mutasi lengkap dalam format UTF-8

## Notes

Memastikan auditabilitas seluruh riwayat modifikasi akun pengguna.
