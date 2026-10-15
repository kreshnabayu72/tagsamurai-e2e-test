---
id: TC-AC-SU-E2E-046-role-matrix-positive-access-menu-settings-user-dan-full-write-controls
title: "Role Matrix Positif: Akses Menu Settings User dan Kontrol Write Penuh"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-150
coverage:
  web: automated
---

# Role Matrix Positif: Akses Menu Settings User dan Kontrol Write Penuh

## Prerequisites

- Pengguna terdaftar dengan peran otoritas penuh: Principal Total Control, Distributor Total Control, Partner Total Control, dan peran manajerial yang memiliki hak akses "Manage user and role"

## Test Steps

### Verifikasi Akses Menu Sidebar
1. Lakukan login secara bergantian menggunakan masing-masing akun peran berwenang di atas
2. Periksa sidebar navigasi aplikasi
3. Verifikasi menu `Admin Console > Settings > User` tampil dengan jelas dan dapat diklik

### Verifikasi Kontrol Write Penuh
4. Buka halaman User List
5. Verifikasi seluruh kontrol write aktif: switch status Active dapat diubah, menu aksi baris memuat `Deactivate User` dan `Resend Activation Email`
6. Buka halaman Detail User target
7. Verifikasi Tab Role (Global Role & Group Role) dapat diedit dan disimpan secara penuh

## Notes

Memastikan aktor yang memiliki wewenang sah mendapatkan akses lengkap ke seluruh fitur modul.
