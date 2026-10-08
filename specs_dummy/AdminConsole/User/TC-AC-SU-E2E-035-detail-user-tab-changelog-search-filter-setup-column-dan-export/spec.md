---
id: TC-AC-SU-E2E-035-detail-user-tab-changelog-search-filter-setup-column-dan-export
title: "Detail User Tab Changelog per-user: 6 kolom, Search, Filter Panel date range, Setup Column terpisah, dan export CSV"
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

# Detail User Tab Changelog per-user: 6 kolom, Search, Filter Panel date range, Setup Column terpisah, dan export CSV

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna memiliki riwayat mutasi changelog dan target lain tanpa riwayat

## Test Steps

### Screening Tab Changelog Per-User dan Struktur Kolom

1. Buka halaman Detail User > Tab `Changelog`
2. Verifikasi tabel memuat 6 kolom data: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` (tanpa kolom User Name karena sudah scoped 1 user)
3. Verifikasi urutan default tabel adalah kolom `Date` Descending (terbaru di atas)

### Search, Filter Date Range, dan Setup Column

1. Ketik kata kunci pada kotak Search, verifikasi pencocokan pada kolom Action dan Field (mengabaikan Date)
2. Buka Filter Panel, pilih Action `"Activate"`, pilih Modified By, dan tentukan rentang tanggal pada Date Range Picker lalu klik `[Apply]`
3. Verifikasi tabel hanya menampilkan entri log yang sesuai dengan filter
4. Buka Setup Column, sembunyikan kolom `New Value`, verifikasi pengaturan kolom tersimpan terpisah dari modal Changelog tingkat List
5. Klik tombol `[Download]`, verifikasi file terunduh dengan nama `Changelog-User-[User Name].csv`

### Verifikasi Empty State

1. Buka Tab Changelog pada pengguna baru yang belum memiliki riwayat mutasi
2. Verifikasi tabel menampilkan empty state dengan Title `"No changelog yet"` dan Description `"Activities and changes will appear here."`

## Notes

- Tab Changelog menyajikan jejak audit terfokus khusus untuk satu record user.
