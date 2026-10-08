---
id: TC-AC-SU-E2E-009-user-list-sidebar-group-tree-dan-state-collapse
title: "Navigasi Sidebar Group tree hirarki, filtering user per group, dan persistensi state collapse"
priority: High
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

- Login sebagai Role: Total Control
- Entitas memiliki pohon group berjenjang (contoh: Region A -> Branch 1 -> Sub-branch 1) dengan anggota pengguna di masing-masing node

## Test Steps

### Navigasi Sidebar Group & Filtering Hierarkis
1. Buka halaman `Settings > User`
2. Amati Sidebar Group di sisi kanan halaman
3. Klik node root `"Region A"` pada pohon group
4. Verifikasi tabel User List otomatis tersaring hanya menampilkan pengguna yang berada di Region A serta seluruh descendant-nya (Branch 1 dan Sub-branch 1)
5. Klik node child `"Branch 1"`
6. Verifikasi tabel User List menyempitkan saringan hanya ke pengguna di Branch 1 dan Sub-branch 1
7. Klik opsi `"All Groups"` di puncak sidebar
8. Verifikasi seluruh pengguna entitas kembali tampil di tabel

### Persistensi State Collapse Sidebar
9. Klik tombol toggle collapse pada header Sidebar Group untuk menutup sidebar
10. Verifikasi sidebar tertutup (collapsed) dan tabel User List melebar memenuhi layar (full-width)
11. Lakukan refresh browser (F5)
12. Verifikasi setelah reload halaman selesai, sidebar tetap dalam keadaan collapsed
13. Navigasi ke menu lain (misal: `Settings > Group`), lalu kembali ke `Settings > User`
14. Verifikasi state collapsed tetap dipulihkan dari localStorage
15. Buka kembali sidebar (state Open), tutup tab browser, dan buka kembali URL di tab baru
16. Verifikasi preferensi Open tersimpan dan sidebar langsung terbuka

## Notes

- State collapse sidebar disimpan per-user per-halaman di localStorage.
