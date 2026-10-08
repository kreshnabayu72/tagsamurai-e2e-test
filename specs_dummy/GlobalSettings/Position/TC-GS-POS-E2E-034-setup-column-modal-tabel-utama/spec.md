---
id: TC-GS-POS-E2E-034-setup-column-modal-tabel-utama
title: "Popup Setup Column tabel utama: search, hide/unhide, drag reorder, pin, Reset to Default, dan independensi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-181
  - TC-GS-POS-182
  - TC-GS-POS-183
  - TC-GS-POS-184
  - TC-GS-POS-185
  - TC-GS-POS-186
  - TC-GS-POS-187
  - TC-GS-POS-188
  - TC-GS-POS-189
  - TC-GS-POS-190
  - TC-GS-POS-191
coverage:
  web: automated
---

# Popup Setup Column tabel utama: search, hide/unhide, drag reorder, pin, Reset to Default, dan independensi

## Prerequisites

- Login sebagai Total Control
- Buka Overlay Column Visibility pada header tabel

## Test Steps

### Screening Popup Setup Column & Footer

1. Klik opsi "Setup Column..." di bagian bawah Overlay Column Visibility
2. Verifikasi modal "Setup Column" terbuka
3. Verifikasi footer hanya memuat tombol "[Reset to Default]" dan tombol "[Save]" (tidak ada tombol [Cancel] per keputusan NC-09)
4. Verifikasi terdapat input pencarian kolom di dalam modal

### Pencarian Kolom, Pin, dan Drag Reorder

5. Ketik "Last" pada input cari kolom, verifikasi hanya kolom "Last Updated" yang tersaring
6. Klik ikon pin pada kolom "Name" untuk mengunci posisi kolom
7. Lakukan drag reorder posisi kolom di dalam list
8. Klik tombol `[✕]` di header modal, verifikasi perubahan dibuang dan susunan kolom tabel tidak berubah

### Save Perubahan & Reset to Default

9. Buka kembali modal Setup Column, sembunyikan kolom "Last Updated", lalu klik "[Save]"
10. Verifikasi perubahan tersimpan dan kolom Last Updated tersembunyi
11. Buka kembali Setup Column lalu klik tombol "[Reset to Default]"
12. Klik "[Save]", verifikasi susunan kolom tabel kembali ke default awal (Name, Last Updated)
13. Verifikasi preferensi kolom tabel utama tidak memengaruhi preferensi kolom Popup Changelog dan sebaliknya

## Notes

- Menggabungkan fitur modal Setup Column dari TC-GS-POS-181 s.d. 191.
