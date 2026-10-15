---
id: TC-GS-POS-E2E-050-multi-konteks-konkurensi-dua-admin-create-dan-limit
title: "Multi-Konteks: Create bersamaan nama yang sama dan create bersamaan pada slot limit terakhir oleh 2 admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-269
  - TC-GS-POS-270
coverage:
  web: automated
---

# Multi-Konteks: Create bersamaan nama yang sama dan create bersamaan pada slot limit terakhir oleh 2 admin

## Prerequisites

- Dua sesi browser simultan: Sesi 1 (Admin A) dan Sesi 2 (Admin B)
- Keduanya memiliki Role: Total Control

## Test Steps

### Create Bersamaan dengan Nama yang Sama

1. Pada Sesi 1 (Admin A), buka form Create Position dan isi "Chief Architect"
2. Pada Sesi 2 (Admin B), buka form Create Position dan isi nama yang sama persis "Chief Architect"
3. Tekan tombol "[Submit]" pada Sesi 1 dan Sesi 2 secara hampir bersamaan
4. Verifikasi salah satu admin berhasil menyimpan dan mendapatkan toast sukses
5. Verifikasi admin lainnya ditolak dengan pesan error nama duplikat "Position Name already exists"

### Create Bersamaan pada Slot Limit Terakhir

6. Atur Master Data Count Limit sehingga tersisa tepat 1 kuota kosong
7. Admin A dan Admin B membuka form Create Position dengan nama unik masing-masing
8. Keduanya menekan "[Submit]" secara serentak
9. Verifikasi salah satu submit berhasil mengisi slot kuota terakhir
10. Verifikasi admin kedua ditolak dengan pesan batas kuota limit tercapai

## Notes

- Menggabungkan TC-GS-POS-269 dan 270 dalam kelas harness Multi-Konteks.
