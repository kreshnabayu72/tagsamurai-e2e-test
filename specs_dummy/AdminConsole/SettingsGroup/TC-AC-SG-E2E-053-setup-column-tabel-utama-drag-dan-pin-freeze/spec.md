---
id: TC-AC-SG-E2E-053-setup-column-tabel-utama-drag-dan-pin-freeze
title: "Setup Column tabel utama: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-207
  - TC-AC-SG-208
coverage:
  web: automated
---

# Setup Column tabel utama: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll

## Prerequisites

- Login sebagai Role: Total Control
- Modal Setup Column tabel utama terbuka

## Test Steps

### Drag & Drop Reordering Kolom
1. Buka modal Setup Column di tabel utama
2. Lakukan aksi drag pada baris `Total User` dan drop ke posisi paling pertama (sebelum `Group`)
3. Verifikasi susunan baris pada modal dan Live Preview seketika berpindah posisi
4. Klik tombol `[Save]`
5. Verifikasi pada tabel utama, kolom `Total User` kini dirender sebelum kolom `Group`
### Freeze Pin Kolom & Horizontal Scroll
6. Buka kembali Setup Column
7. Aktifkan toggle Pin pada kolom `Total User`
8. Klik tombol `[Save]`
9. Lakukan scroll tabel utama ke arah horizontal kanan
10. Verifikasi kolom `Total User` tetap membeku (freeze/sticky) di sisi kiri, sementara kolom-kolom lainnya bergeser normal di bawahnya

## Notes

- Menguji interaksi pointer drag-and-drop dan CSS sticky layout pada tabel.
