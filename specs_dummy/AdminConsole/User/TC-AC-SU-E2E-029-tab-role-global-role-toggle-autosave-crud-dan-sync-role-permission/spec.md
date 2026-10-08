---
id: TC-AC-SU-E2E-029-tab-role-global-role-toggle-autosave-crud-dan-sync-role-permission
title: "Detail User Tab Role: Global Role Toggle, Autosave CRUD per Cell, dan Sinkronisasi 2-Arah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-64
  - TC-AC-SU-65
  - TC-AC-SU-66
  - TC-AC-SU-67
  - TC-AC-SU-68
coverage:
  web: automated
---

# Detail User Tab Role: Global Role Toggle, Autosave CRUD per Cell, dan Sinkronisasi 2-Arah

## Prerequisites

- Login sebagai Total Control
- Berada pada halaman Detail User target

## Test Steps

### Interaksi Global Role dan Autosave CRUD
1. Di halaman Detail User, pilih tab `Role` lalu buka sub-tab `Global Role`
2. Verifikasi daftar katalog Global Role yang tersedia di entitas
3. Klik toggle switch pada salah satu Global Role yang belum aktif (misal `"Asset Auditor"`)
4. Verifikasi toggle berpindah ke posisi ON dan kolom hak akses `C` (Create), `R` (Read), `U` (Update), `D` (Delete) muncul
5. Centang checkbox `Create` pada baris tersebut
6. Verifikasi sistem melakukan autosave seketika (indikator auto-save spinner singkat / toast kecil `"Changes saved"` tanpa tombol submit global)

### Verifikasi Sinkronisasi 2-Arah ke Modul Role & Permission
7. Buka tab baru di browser dan akses menu `Settings > Role & Permission`
8. Buka role `Asset Auditor` dan periksa daftar user ter-assign
9. Verifikasi nama user target kini telah tercantum di daftar anggota role tsb dengan izin Create aktif

## Notes

Memvalidasi mekanisme mutasi real-time autosave tanpa tombol save form konvensional.
