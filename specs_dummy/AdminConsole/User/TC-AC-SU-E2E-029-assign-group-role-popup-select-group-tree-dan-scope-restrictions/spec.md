---
id: TC-AC-SU-E2E-029-assign-group-role-popup-select-group-tree-dan-scope-restrictions
title: "Popup Assign Group Role: hierarki tree Select Group, scope restriction already-assigned disabled, dan proteksi duplikat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-86
  - TC-AC-SU-87
  - TC-AC-SU-90
  - TC-AC-SU-91
  - TC-AC-SU-93
  - TC-AC-SU-256
coverage:
  web: automated
---

# Popup Assign Group Role: hierarki tree Select Group, scope restriction already-assigned disabled, dan proteksi duplikat

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat hierarki group tree dan group yang telah ter-assign ke role target

## Test Steps

### Buka Tree Select Group dan Penambahan Group ke Tabel Popup

1. Buka halaman Detail User > Tab Role > Sub-tab Group Role
2. Klik tombol `[Assign Group]` pada salah satu Group Role
3. Verifikasi popup Assign Group Role terbuka
4. Klik tombol `[+ Assign Group]` di dalam popup
5. Verifikasi popup sekunder `Select Group` terbuka memuat struktur hierarki tree group dengan checkbox multi-select

### Scope Restriction Kondisi Already-Assigned dan Proteksi Duplikat

1. Amati node Group X yang sudah ter-assign sebelumnya pada role ini
2. Verifikasi node Group X berstatus Disabled dengan tooltip `"[Group Name] is already assigned to this role."` sehingga tidak dapat dipilih ulang
3. Centang node Group Y yang belum ter-assign lalu klik tombol `[Select]`
4. Verifikasi Group Y masuk ke dalam tabel popup Assign Group Role dengan opsi CRUD default unchecked (R akan otomatis aktif saat disimpan)
5. Klik kembali tombol `[+ Assign Group]` di sesi popup yang sama (sebelum disimpan)
6. Verifikasi node Group Y kini juga berstatus Disabled dengan tooltip already-assigned
7. Verifikasi sistem secara proaktif mencegah penambahan group duplikat pada tabel penugasan

## Notes

- Pencegahan duplikat assignment dilakukan langsung di tingkat UI tree selection.
