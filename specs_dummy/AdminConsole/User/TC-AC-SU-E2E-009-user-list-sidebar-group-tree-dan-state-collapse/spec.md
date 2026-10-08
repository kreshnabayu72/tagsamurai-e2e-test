---
id: TC-AC-SU-E2E-009-user-list-sidebar-group-tree-dan-state-collapse
title: "Navigasi Sidebar Group tree hirarki, filtering user per group, dan persistensi state collapse"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-20
  - TC-AC-SU-293
coverage:
  web: automated
---

# Navigasi Sidebar Group tree hirarki, filtering user per group, dan persistensi state collapse

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat hierarki Group (Parent Group dan Child Group) dengan penugasan user

## Test Steps

### Navigasi dan Filtering via Sidebar Group

1. Buka halaman User List
2. Verifikasi Sidebar Group tampil di sisi kiri dengan struktur hirarki tree group
3. Klik salah satu node Parent Group
4. Verifikasi tabel User List otomatis tersaring menampilkan seluruh pengguna yang berada di dalam group tersebut beserta seluruh descendant group-nya

### Toggle Collapse Sidebar dan Persistensi State

1. Klik tombol toggle collapse pada Sidebar Group
2. Verifikasi Sidebar Group tertutup dan area tabel User List melebar menjadi full-width
3. Muat ulang halaman browser (F5)
4. Verifikasi state Sidebar Group tetap tertutup (collapsed)
5. Buka menu lain di aplikasi lalu kembali ke `Settings > User`
6. Verifikasi state Sidebar Group tetap dipertahankan sesuai preferensi tersimpan di localStorage
7. Klik tombol toggle untuk membuka kembali Sidebar Group, verifikasi sidebar terbuka normal

## Notes

- State collapse sidebar disimpan per-user per-halaman.
