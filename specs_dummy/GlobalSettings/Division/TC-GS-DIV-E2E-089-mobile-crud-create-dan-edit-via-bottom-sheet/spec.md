---
id: TC-GS-DIV-E2E-089-mobile-crud-create-dan-edit-via-bottom-sheet
title: "Eksekusi CRUD Mobile Android: Penambahan dan Pengeditan Divisi Berhasil Melalui Bottom Sheet Form"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-285
  - TC-GS-DIV-286
coverage:
  web: automated
---

# Eksekusi CRUD Mobile Android: Penambahan dan Pengeditan Divisi Berhasil Melalui Bottom Sheet Form

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (viewport emulasi Android <768px)
- Aplikasi TAG Samurai Mobile (Android)
- Aplikasi TAG Samurai Mobile (Android) terbuka sebagai Total Control

## Test Steps

### Create Division dari mobile berhasil (TC-GS-DIV-285)

1. Ketuk `[+ Division]`
2. Isi Division Name `Mobile Unit` dan Code `MBL`
3. Ketuk `[Submit]`
4. Verifikasi Muncul toast sukses: `Success, division has been created.`
5. Verifikasi Card `Mobile Unit` tampil pada card list

### Edit Division dari mobile tampil sebagai bottom sheet dan berhasil disimpan (TC-GS-DIV-286)

6. Ketuk `[⋯]` pada card `Mobile Unit` lalu `Edit`
7. Ubah Division Name menjadi `Mobile Unit 2`
8. Ketuk `[Save]`
9. Verifikasi Form Edit Division tampil sebagai bottom sheet dengan Division Name dan Code terisi
10. Verifikasi Muncul toast sukses: `Success, division has been updated.`
11. Verifikasi Card menampilkan `Mobile Unit 2`

## Notes

- Memvalidasi penambahan divisi baru via tombol [+ Division] floating dan pengeditan divisi via menu bottom sheet pada aplikasi mobile Android hingga tersimpan berhasil (PRD §4.6).
- Sumber pemetaan test case granular: TC-GS-DIV-285, TC-GS-DIV-286.
