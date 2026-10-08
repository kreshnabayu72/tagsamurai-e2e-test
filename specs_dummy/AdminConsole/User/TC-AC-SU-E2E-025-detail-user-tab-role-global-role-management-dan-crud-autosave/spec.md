---
id: TC-AC-SU-E2E-025-detail-user-tab-role-global-role-management-dan-crud-autosave
title: "Tab Role Sub-tab Global Role: toggle role ON/OFF, autosave CRUD per cell, dan sinkronisasi 2-arah ke Role & Permission"
priority: Critical
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

# Tab Role Sub-tab Global Role: toggle role ON/OFF, autosave CRUD per cell, dan sinkronisasi 2-arah ke Role & Permission

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna memiliki daftar Global Role aktif dan nonaktif

## Test Steps

### Navigasi Sub-Tab Global Role dan Toggle Switch ON/OFF

1. Buka halaman Detail User > Tab Role > Sub-tab `Global Role`
2. Verifikasi seluruh Global Role yang berlaku untuk entitas tampil pada tabel
3. Klik switch toggle pada salah satu role yang sedang OFF untuk menyalakannya (ON)
4. Verifikasi toast sukses muncul: `"Success, role has been updated."` / `"Success, role has been assigned."`
5. Verifikasi checkbox R (Read) otomatis tercentang dan berstatus Disabled (mandatory read)
6. Verifikasi checkbox C (Create), U (Update), dan D (Delete) kini terbuka (unlocked) dan dapat dicentang

### Autosave Checkbox CRUD dan Retensi Nilai saat Toggle OFF

1. Centang checkbox C (Create) pada role tersebut
2. Verifikasi perubahan tersimpan seketika (autosave) tanpa membutuhkan tombol Save terpisah
3. Klik switch toggle role tersebut menjadi OFF
4. Verifikasi seluruh checkbox CRUD terkunci (disabled) dalam keadaan switch OFF
5. Klik switch toggle role kembali menjadi ON
6. Verifikasi nilai centang CRUD sebelumnya tetap tersimpan dan tidak tereset

### Sinkronisasi Dua Arah dengan Settings > Role & Permission

1. Buka menu `Settings > Role & Permission` lalu buka detail Global Role yang baru diubah
2. Verifikasi nama pengguna tersebut dan matriks CRUD-nya tercermin sinkron di kedua modul

## Notes

- Perubahan hak akses Global Role tersimpan secara atomik dengan autosave per cell.
