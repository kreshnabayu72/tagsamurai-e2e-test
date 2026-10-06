---
id: TC-AC-SU-E2E-039-role-matrix-positif-akses-menu-dan-write-controls
title: "Role Matrix Positif: akses menu Settings > User dan kontrol write penuh untuk Principal TC, Distributor TC, Partner TC, dan Manage user and role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-150
coverage:
  web: automated
---

# Role Matrix Positif: akses menu Settings > User dan kontrol write penuh untuk Principal TC, Distributor TC, Partner TC, dan Manage user and role

## Prerequisites

- Terdapat akun login untuk: Principal Total Control, Distributor Total Control, Partner Total Control, dan Pengguna dengan Global Role "Manage user and role"

## Test Steps

### Eksekusi Role Matrix Positif Lintas Role Berhak

1. Lakukan langkah berikut untuk setiap role pada tabel prasyarat:
2. 1. Login menggunakan akun dengan role tersebut
3. 2. Buka sidebar menu aplikasi, verifikasi menu `Settings > User` tampil
4. 3. Klik menu `Settings > User`, verifikasi halaman User List terbuka sukses
5. 4. Verifikasi toolbar memuat kontrol lengkap dan switch Active berstatus Enabled untuk data yang memenuhi syarat
6. 5. Buka Detail User salah satu pengguna, verifikasi halaman Detail User dan Tab Role dapat diakses dengan kontrol write (toggle switch role, checkbox CRUD, tombol Assign Group) terbuka sesuai wewenang

## Notes

- Role matrix positif memvalidasi hak akses penuh bagi seluruh peran berwenang.
