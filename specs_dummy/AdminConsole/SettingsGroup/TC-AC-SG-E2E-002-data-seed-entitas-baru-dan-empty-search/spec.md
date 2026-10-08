---
id: TC-AC-SG-E2E-002-data-seed-entitas-baru-dan-empty-search
title: "Inisialisasi data seed entitas baru dan tampilan empty state hasil search/filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-2
  - TC-AC-SG-4
coverage:
  web: automated
---

# Inisialisasi data seed entitas baru dan tampilan empty state hasil search/filter

## Prerequisites

- Akun entitas baru yang baru di-onboard (belum memiliki custom group)
- Akun entitas aktif dengan data group untuk pengujian filter

## Test Steps

### Data Seed Entitas Baru
1. Login sebagai Total Control pada entitas baru yang baru selesai di-onboard
2. Buka halaman `Settings > Group`
3. Verifikasi tabel utama merender 1 baris record biasa bernama `"Default Group"` dengan parent root virtual All Groups
4. Verifikasi halaman tidak menampilkan empty state pada entitas baru karena data seed otomatis terbentuk
### Empty State Hasil Search / Filter
5. Login sebagai Total Control pada entitas yang memiliki kumpulan group
6. Buka halaman `Settings > Group`
7. Klik icon `[🔍 Search]` pada toolbar dan ketik keyword non-existent `"zzz-notfound"` lalu tekan Enter
8. Verifikasi tabel beralih ke tampilan empty state pencarian
9. Verifikasi judul empty state menampilkan `"No results found"`
10. Verifikasi subtitle empty state menampilkan `"Try adjusting your search or filter."`

## Notes

- Root "All Groups" tidak pernah dirender sebagai baris data di tabel utama (ACSG-LOGIC-07).
- Entitas baru secara deterministik di-seed dengan 1 Default Group.
