---
id: TC-GS-DIV-E2E-019-edit-modal-screening-prefilled-dan-hover
title: "Screening Modal Edit Division, Nilai Terisi Awal, dan Feedback Tombol"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-31
  - TC-GS-DIV-196
coverage:
  web: automated
---

# Screening Modal Edit Division, Nilai Terisi Awal, dan Feedback Tombol

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Terdapat data divisi 'Legal' dengan Code 'LGL'

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik icon menu row action (⋯) pada baris divisi 'Legal'
3. Klik menu 'Edit'
4. Verifikasi modal dialog 'Edit Division' terbuka dengan icon close '[✕]' di kanan atas
5. Verifikasi field 'Division Name *' terisi awal (pre-filled) dengan teks 'Legal'
6. Verifikasi field 'Code' terisi awal dengan nilai eksisting 'LGL'
7. Verifikasi modal Edit TIDAK memiliki checkbox 'Stay on this form after submitting' (hanya tersedia di Create)
8. Verifikasi footer modal memuat tombol '[Clear Field]' (variant text) dan '[Save]' (variant filled primary)
9. Arahkan kursor (hover) pada tombol '[Save]' dan '[Clear Field]' lalu verifikasi feedback visual hover state
10. Tekan tombol Escape (Esc) dan verifikasi modal menutup tanpa mengubah data

## Notes

- Spesifikasi form modal Edit mengikuti division.md §4.2c.
