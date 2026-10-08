---
id: TC-AC-SG-E2E-024-create-subgroup-guard-hierarchy-depth-limit
title: "Pencegahan penambahan subgroup melebihi batas Hierarchy Depth Limit platform"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-45
  - TC-AC-SG-46
coverage:
  web: automated
---

# Pencegahan penambahan subgroup melebihi batas Hierarchy Depth Limit platform

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia node cabang yang berada pada kedalaman sama dengan batas limit platform (depth = 50)

## Test Steps

### Evaluasi Kedalaman Subgroup
1. Cari dan navigasi ke node grup yang berada pada tingkat kedalaman limit
2. Amati tombol `+ Add Subgroup` pada baris tabel maupun elipsis sidebar
3. Verifikasi tombol `+ Add Subgroup` TETAP SHOW DAN ENABLED sebelum diklik (tidak di-disable secara preemptive)
4. Klik tombol `[+ Add Subgroup]` pada node tersebut
5. Verifikasi muncul dialog blokir `"Cannot Add Group"`
6. Verifikasi body dialog menampilkan teks `"You've reached the platform limit of 50 levels. Contact support if you need a higher limit."` dengan tombol tunggal `[OK]`
7. Verifikasi modal formulir Create TIDAK PERNAH DIBUKA
8. Klik `[OK]` dan verifikasi dialog tertutup tanpa ada data baru

## Notes

- Hierarchy Depth Limit adalah batas keselamatan teknis platform-wide, bukan plan gating (ACSG-02).
