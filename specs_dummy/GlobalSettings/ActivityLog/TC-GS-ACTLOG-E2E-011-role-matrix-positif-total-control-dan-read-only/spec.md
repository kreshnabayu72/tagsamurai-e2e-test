---
id: TC-GS-ACTLOG-E2E-011-role-matrix-positif-total-control-dan-read-only
title: "Role Matrix Positif: Total Control dan Read Only Memiliki Akses Penuh Identik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-28
  - TC-GS-ACTLOG-29
coverage:
  web: automated
---

# Role Matrix Positif: Total Control dan Read Only Memiliki Akses Penuh Identik

## Prerequisites

- Tabel Role yang diuji:
| Role | Akun Uji |
| Total Control GS | totalControlGlobalSettings_automated@qwertysystem.net |
| Read Only GS | readOnlyGlobalSettings_automated@qwertysystem.net |

## Test Steps

### Eksekusi Matriks Role Positif
1. Jalankan pengujian berikut untuk setiap role pada tabel:
2. Login dengan akun uji role yang bersangkutan.
3. Verifikasi menu 'Activity Log' tampil (Show) di sidebar Global Settings.
4. Klik menu 'Activity Log'.
5. Verifikasi kedua tab 'Session' dan 'User Action' tampil (Show) dan dapat diakses.
6. Verifikasi toolbar Table Tools (Search, Filter, Download) tampil aktif tanpa state disabled.
7. Verifikasi data log dapat dibaca pada kedua tab.
8. Verifikasi antarmuka yang dilihat oleh Read Only identik 100% dengan Total Control karena seluruh fungsi modul bersifat read-only.

## Notes

- Akses ke Activity Log berbasis access level (bukan granular capability). Total Control dan Read Only memiliki hak baca identik.
