---
id: TC-AC-SG-E2E-007-sidebar-search-toggle-dan-persistensi
title: "Pencarian sidebar, hierarchy toggle expand/collapse all, dan persistensi state sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-9
  - TC-AC-SG-10
  - TC-AC-SG-223
coverage:
  web: automated
---

# Pencarian sidebar, hierarchy toggle expand/collapse all, dan persistensi state sidebar

## Prerequisites

- Login sebagai Role: Total Control
- Pohon hierarki grup ≥ 3 level

## Test Steps

### Pencarian Sidebar
1. Buka halaman `Settings > Group` dengan sidebar terbuka
2. Ketik nama subgroup level terdalam (contoh: `"sub branch"`) pada kotak pencarian di toolbar sidebar
3. Verifikasi pohon grup di sidebar secara otomatis meng-expand cabang menuju node yang cocok dan memberikan highlight visual
4. Bersihkan kata kunci pencarian sidebar
### Hierarchy Toggle (Expand/Collapse All)
5. Klik icon hierarchy toggle di toolbar sidebar
6. Verifikasi seluruh cabang pohon di sidebar ter-collapse (hanya menampilkan level 1)
7. Klik kembali icon hierarchy toggle
8. Verifikasi seluruh cabang pohon di sidebar kembali ter-expand penuh
### Persistensi State Collapse Sidebar
9. Klik tombol collapse sidebar (sidebar tertutup, tabel melebar full-width)
10. Refresh halaman (F5)
11. Verifikasi sidebar tetap berada dalam status collapsed
12. Navigasi ke menu lain lalu kembali ke `Settings > Group`
13. Verifikasi sidebar tetap collapsed
14. Buka kembali sidebar (klik tombol expand sidebar)
15. Tutup tab dan buka kembali di sesi baru, verifikasi state Open berhasil dipulihkan

## Notes

- State terbuka/tertutupnya sidebar disimpan per user di localStorage (prd-conventions.md §31.3).
