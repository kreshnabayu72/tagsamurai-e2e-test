---
id: TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save
title: "Validasi nama duplikat saat edit, pengecualian nama sendiri, dan guard double-click Save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-85
  - TC-GS-POS-86
  - TC-GS-POS-87
  - TC-GS-POS-104
  - TC-GS-POS-105
coverage:
  web: automated
---

# Validasi nama duplikat saat edit, pengecualian nama sendiri, dan guard double-click Save

## Prerequisites

- Login sebagai Role: Total Control
- Record "IT Manager" dan "Finance Analyst" sudah ada di database

## Test Steps

### Validasi Nama Duplikat Record Lain

1. Buka menu ⋯ pada baris "Finance Analyst", klik "Edit"
2. Ubah Position Name menjadi "it manager" (sama dengan nama record lain)
3. Tunggu debounce, verifikasi inline error "Position Name already exists" langsung muncul
4. Tambahkan spasi ("  it manager  ") lalu klik "[Save]"
5. Verifikasi simpan diblokir dan data tidak terkirim

### Pengecualian Nama Sendiri (Self-Name Exception)

6. Kembalikan teks ke nama aslinya "Finance Analyst"
7. Verifikasi tidak ada error duplikat yang muncul (nama milik record itu sendiri tidak dianggap bentrok)

### Saving State & Guard Double-Click

8. Ubah nama menjadi "Lead Finance Analyst"
9. Klik tombol "[Save]" secara cepat dua kali (double-click)
10. Verifikasi tombol menampilkan state "Saving..." dan permintaan hanya dieksekusi satu kali

## Notes

- Menggabungkan TC-GS-POS-85, 86, 87, 104, dan 105.
