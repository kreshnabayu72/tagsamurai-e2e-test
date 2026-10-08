---
id: TC-GS-USER-E2E-033-plan-gating-semua-tier
title: Create, Edit, Delete user identik di semua tier plan dan Scan TAG hanya di Growth ke atas
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-397
  - TC-GS-USER-342
coverage:
  web: automated
---

# Create, Edit, Delete user identik di semua tier plan dan Scan TAG hanya di Growth ke atas

## Prerequisites

Spec ini dijalankan untuk setiap entity pada tabel. Langkahnya identik, hanya entity dan akun login yang berbeda.

Entity yang diuji:

| Plan | Akun | Scan TAG |
|---|---|---|
| Starter | Total Control pada entity plan Starter | Tidak tampil |
| Growth | Total Control pada entity plan Growth | Tampil |
| Professional | Total Control pada entity plan Professional | Tampil |
| Enterprise | Total Control pada entity plan Enterprise | Tampil |
| Custom | Total Control pada entity plan Custom | Tampil |

- Lima entity terpisah, masing-masing dengan akun Total Control. Nama akun dan entity disiapkan tim FE
- Position dan Division valid ada di master data setiap entity
- Data user yang dibuat spec ini (nama "Tier Uji" dengan email unik per run) dihapus di akhir langkah setiap entity

## Test Steps

Lakukan langkah 1–9 untuk setiap entity pada tabel "Entity yang diuji".

1. Login sebagai Total Control pada entity yang diuji, lalu buka User List
2. Klik `[+ User]` dan verifikasi modal Create terbuka tanpa dialog upsell atau pembatasan plan
3. Verifikasi bagian User TAG (Scan TAG) tampil atau tidak sesuai kolom "Scan TAG" pada tabel
4. Isi semua field wajib untuk user "Tier Uji" dengan Access "Global Settings", lalu klik `[Submit]`
5. Verifikasi toast "User created successfully." muncul dan baris "Tier Uji" muncul di User List
6. Klik row action `Edit` pada "Tier Uji", ubah Position, lalu klik `[Save]`
7. Verifikasi toast "Success, user has been updated." muncul dan perubahan tersimpan
8. Klik row action `Delete` pada "Tier Uji" lalu konfirmasi pada dialog
9. Verifikasi toast "Success, user has been deleted." muncul, dan tidak ada perilaku atau batas yang berbeda dari entity lain

## Notes

- Modul User adalah fitur core yang tersedia penuh di semua plan. Tidak ada batas jumlah user per tier, sehingga semua entity memakai alur yang sama (PRD `user.md` bagian 9.10).
- Satu-satunya batas yang berlaku sama di semua tier adalah Master Data Count Limit, dicakup `TC-GS-USER-E2E-040-batas-kuota-master-data`.
- Pengecualian plan yang diuji di sini adalah TAG RFID: hanya tampil di Growth ke atas, sedangkan di Starter hanya QR (`TC-GS-USER-342`).
- Cara skrip menjalankan banyak entity diputuskan di tahap script.
