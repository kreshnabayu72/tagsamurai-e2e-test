---
id: TC-AC-SG-E2E-003-empty-state-genuinely-kosong-nol-group
title: "Tampilan empty state genuinely-kosong ketika entitas memiliki nol group level 1"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-184
coverage:
  web: automated
---

# Tampilan empty state genuinely-kosong ketika entitas memiliki nol group level 1

## Prerequisites

- Login sebagai Role: Total Control
- Kondisi entitas mencapai 0 group level 1 (seluruh group custom terhapus di lingkungan pengujian terisolasi)

## Test Steps

### Verifikasi Genuinely Empty State
1. Buka halaman `Settings > Group` pada entitas dengan 0 group level 1
2. Verifikasi tabel utama menampilkan ilustrasi empty state kanonikal (100x100px)
3. Verifikasi judul empty state menampilkan teks `"No group yet"`
4. Verifikasi subtitle empty state menampilkan teks `"Get started by creating your first group."` (§7.1)
5. Verifikasi root "All Groups" tidak pernah muncul sebagai baris pemicu non-empty di tabel

## Notes

- Empty state genuinely-kosong berbeda copywriting-nya dari empty state hasil search/filter (TC-AC-SG-4).
