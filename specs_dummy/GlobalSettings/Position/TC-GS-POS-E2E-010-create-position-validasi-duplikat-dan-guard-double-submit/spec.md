---
id: TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit
title: "Validasi nama duplikat case-insensitive saat mengetik dan guard double-submit Save state"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-47
  - TC-GS-POS-48
  - TC-GS-POS-49
  - TC-GS-POS-65
  - TC-GS-POS-66
coverage:
  web: automated
---

# Validasi nama duplikat case-insensitive saat mengetik dan guard double-submit Save state

## Prerequisites

- Login sebagai Role: Total Control
- Record "IT Manager" sudah ada di database

## Test Steps

### Validasi Duplikat Case-Insensitive Saat Mengetik

1. Klik "[+ Position]" untuk membuka modal Create
2. Ketik "it manager" (huruf kecil) ke dalam field Position Name
3. Tunggu debounce (sekitar 500 ms), verifikasi pesan inline error "Position Name already exists" langsung muncul
4. Tambahkan spasi di depan dan belakang ("  it manager  "), verifikasi error nama duplikat tetap muncul
5. Klik "[Submit]", verifikasi submit diblokir dan data tidak terkirim

### Pemulihan Error Duplikat

6. Ubah teks menjadi nama yang unik, misalnya "IT Manager Level 2"
7. Verifikasi pesan error duplikat otomatis hilang dan border merah kembali normal

### Guard Double-Submit dan Saving State

8. Klik tombol "[Submit]" secara cepat dua kali berturut-turut (double-click)
9. Verifikasi tombol "[Submit]" menampilkan state disabled/loading ("Saving...") saat permintaan diproses
10. Verifikasi setelah proses selesai, hanya 1 record "IT Manager Level 2" yang tercipta di tabel

## Notes

- Menggabungkan TC-GS-POS-47, 48, 49, 65, dan 66.
