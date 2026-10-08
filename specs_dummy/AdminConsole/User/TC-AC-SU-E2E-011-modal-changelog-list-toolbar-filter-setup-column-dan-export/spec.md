---
id: TC-AC-SU-E2E-011-modal-changelog-list-toolbar-filter-setup-column-dan-export
title: "Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-23
  - TC-AC-SU-24
  - TC-AC-SU-25
  - TC-AC-SU-227
coverage:
  web: automated
---

# Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat riwayat log mutasi aktivitas pengguna di tingkat modul

## Test Steps

### Membuka Modal Changelog dan Screening Struktur

1. Buka halaman User List dan klik icon `[📋 Changelog]` di toolbar
2. Verifikasi modal terbuka dengan judul `"Changelog: User"`
3. Verifikasi tabel modal memuat 7 kolom: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`

### Search, Filter, dan Populasi Dropdown Modal Changelog

1. Ketik nama pengguna di kotak Search modal Changelog, verifikasi pencocokan pada kolom teks
2. Klik tombol Filter di dalam modal Changelog
3. Verifikasi dropdown Action memuat opsi hardcode aksi (Activate, Deactivate, Assign Group Role, Resend Activation Email)
4. Verifikasi dropdown User Name dan Modified By terisi DISTINCT dari riwayat log yang ada
5. Pilih Action `"Activate"` dan User Name tertentu lalu klik `[Apply]`, verifikasi tabel modal tersaring sesuai logika AND

### Column Visibility dan Download Export

1. Klik header kolom `⋯` di modal Changelog lalu buka Column Visibility
2. Sembunyikan kolom `Old Value` dan munculkan kembali, verifikasi cache pengaturan kolom terisolasi dari tabel User List utama
3. Klik tombol `[Download]` di dalam modal Changelog dan pilih CSV
4. Verifikasi file terunduh dengan nama `Changelog-User.csv`

## Notes

- Modal Changelog di tingkat List merangkum seluruh mutasi pengguna pada modul User.
