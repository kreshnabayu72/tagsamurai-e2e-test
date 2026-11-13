---
id: TC-FA-FAREG-E2E-044-draft-setup-column-tersimpan
title: "Sub tab Draft: konfigurasi Setup Column bertahan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-KOL-2@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "EB-KOL-2@tabel-draft": [1, 6, 8, 13]
coverage:
  web: automated
---

# Sub tab Draft: konfigurasi Setup Column bertahan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - Tanpa data uji: yang diasersi hanya konfigurasi kolom tabel Draft, dan kolom `Group` dan `Progress` tampil secara bawaan.

## Test Steps

### Konfigurasi kolom tersimpan dan bertahan sesudah muat ulang
1. Verifikasi tabel sub tab Draft memuat kolom `Group` dan kolom `Progress`
2. Klik header kolom Actions `⋯`
3. Klik `Setup Column...`
4. Hilangkan centang `Progress` pada modal `Setup Column`
5. Klik `[Save]`
6. Verifikasi tabel sub tab Draft tidak memuat kolom `Progress` dan memuat kolom `Group`
7. Muat ulang halaman
8. Verifikasi tabel sub tab Draft tetap tidak memuat kolom `Progress` dan tetap memuat kolom `Group` sesudah muat ulang halaman

### Konfigurasi dikembalikan ke bawaan
9. Klik header kolom Actions `⋯`
10. Klik `Setup Column...`
11. Klik `[Reset to Default]`
12. Klik `[Save]`
13. Verifikasi tabel sub tab Draft memuat kembali kolom `Progress`
