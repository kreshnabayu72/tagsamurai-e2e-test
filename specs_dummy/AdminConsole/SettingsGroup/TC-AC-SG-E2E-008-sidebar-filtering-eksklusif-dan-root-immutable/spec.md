---
id: TC-AC-SG-E2E-008-sidebar-filtering-eksklusif-dan-root-immutable
title: "Filtering eksklusif rekursif via klik node sidebar, toggle off, dan immutabilitas root All Groups"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-11
  - TC-AC-SG-12
  - TC-AC-SG-13
  - TC-AC-SG-187
coverage:
  web: automated
---

# Filtering eksklusif rekursif via klik node sidebar, toggle off, dan immutabilitas root All Groups

## Prerequisites

- Login sebagai Role: Total Control
- Pohon hierarki: `"Region A"` (level 1) membawahi `"Branch 1"` (level 2) > `"Sub Branch 1"` (level 3), dan `"Branch 2"` (level 2)

## Test Steps

### Exclusive Filtering via Klik Node
1. Buka `Settings > Group`
2. Klik node `"Region A"` pada pohon sidebar
3. Verifikasi node `"Region A"` di sidebar memiliki highlight visual aktif yang jelas beda dari node lain
4. Verifikasi Group Context Header berganti menampilkan `"Region A"` beserta Total User dan Total Member miliknya
5. Verifikasi baris tabel utama hanya menampilkan seluruh descendant secara rekursif (`"Branch 1"`, `"Branch 2"`, dan `"Sub Branch 1"`)
6. Verifikasi `"Region A"` sendiri TIDAK muncul sebagai baris data di tabel
### Toggle Off Node Aktif
7. Klik kembali node `"Region A"` yang sedang terpilih di sidebar
8. Verifikasi seleksi ter-deselect (toggle off)
9. Verifikasi Group Context Header dan tabel kembali ke state default `"All Groups"` (seluruh tree flat)
### Immutabilitas Root All Groups
10. Amati node root virtual `"All Groups"` di baris paling atas sidebar
11. Verifikasi root `"All Groups"` tidak memiliki tombol elipsis `[⋯]` dan tidak memiliki jalur interaksi Edit, Delete, maupun `+ Add Subgroup`

## Notes

- Root All Groups murni struktural dan tidak dapat dimutasi (ACSG-LOGIC-07).
- TC-AC-SG-14 (agregasi distinct backend) dikecualikan sbg uji BE.
