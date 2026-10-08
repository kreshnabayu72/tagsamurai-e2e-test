---
id: TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin
title: "Multi-Konteks: Edit bersamaan record sama (last-write-wins), delete race, dan bulk delete race antar 2 admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-109
  - TC-GS-POS-118
  - TC-GS-POS-119
  - TC-GS-POS-147
  - TC-GS-POS-148
  - TC-GS-POS-271
  - TC-GS-POS-300
coverage:
  web: automated
---

# Multi-Konteks: Edit bersamaan record sama (last-write-wins), delete race, dan bulk delete race antar 2 admin

## Prerequisites

- Dua sesi browser: Admin A dan Admin B (Total Control)

## Test Steps

### Edit Bersamaan Record yang Sama (Last-Write-Wins)

1. Admin A dan Admin B membuka modal Edit pada record "Finance Analyst"
2. Admin A mengubah nama menjadi "Finance Analyst Level 1" lalu klik "[Save]"
3. Admin B mengubah nama menjadi "Finance Analyst Level 2" lalu klik "[Save]"
4. Verifikasi strategi last-write-wins diterapkan: nama akhir di tabel menjadi "Finance Analyst Level 2"

### Delete Race: Record Dihapus Admin Lain Sebelum Confirm

5. Admin A membuka dialog Delete pada record "Logistics Officer"
6. Sebelum Admin A menekan konfirmasi, Admin B menghapus record tersebut terlebih dahulu
7. Admin A menekan tombol konfirmasi "[Delete]" pada dialognya yang masih terbuka
8. Verifikasi operasi bersifat idempoten (NC-01): dialog tertutup tanpa error crashing dan daftar di-refresh

### In-Use Race: Record Dipakai User Lain Sebelum Confirm Delete

9. Admin A membuka dialog Delete pada record bebas relasi "Branch Manager"
10. Sebelum Admin A klik Confirm, Admin B mengaitkan jabatan tersebut ke seorang user
11. Admin A mengonfirmasi penghapusan
12. Verifikasi sistem mengecek ulang kondisi saat confirm: penghapusan diblokir dan dialog "Cannot Delete Data" muncul

## Notes

- Menggabungkan seluruh skenario konkurensi Edit, Delete, dan Bulk Delete race dari TC-GS-POS-109, 118, 119, 147, 148, 271, dan 300.
