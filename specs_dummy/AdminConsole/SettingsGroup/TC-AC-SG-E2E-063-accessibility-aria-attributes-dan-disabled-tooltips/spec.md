---
id: TC-AC-SG-E2E-063-accessibility-aria-attributes-dan-disabled-tooltips
title: "Aksesibilitas A11y: atribut aria-required/aria-describedby dan tooltip penjelasan pada setiap elemen disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-139
  - TC-AC-SG-140
coverage:
  web: automated
---

# Aksesibilitas A11y: atribut aria-required/aria-describedby dan tooltip penjelasan pada setiap elemen disabled

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

### Inspeksi DOM Form Input
1. Buka modal `[+ New Group]` di sidebar
2. Inspeksi elemen DOM pada input field Group Name
3. Verifikasi atribut `aria-required="true"` terpasang pada elemen input
4. Picu error validasi (submit kosong)
5. Verifikasi elemen input memiliki atribut `aria-describedby` yang mengaitkan ID teks pesan error
### Tooltip pada Elemen Disabled
6. Amati seluruh tombol aksi pada modul ini, verifikasi semuanya memiliki atribut `aria-label` yang representatif
7. Kondisikan kemunculan elemen disabled (contoh: checkbox Setup Column kolom terakhir, tombol form disabled saat suspended)
8. Hover pada elemen disabled tersebut
9. Verifikasi muncul tooltip 🔖 yang menjelaskan alasan penonaktifan elemen tersebut (prd-conventions.md §18.5)

## Notes

- Menegakkan kepatuhan standar aksesibilitas WCAG dan konvensi UI.
