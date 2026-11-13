---
id: TC-FA-FAREG-E2E-095-guided-tooltip-flag
title: "Guided Tooltip: flag bertahan antar sesi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-10": [3, 9, 13, 17]
anchor: [8, 12, 16]
coverage:
  web: automated
---

# Guided Tooltip: flag bertahan antar sesi

## Prerequisites
- Aktor: Tia R, lalu Uli S, lalu Vera T (masing-masing Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-095-1: Tia R (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` belum disetel.
  - DU-095-2: Uli S (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel.
  - DU-095-3: Vera T (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), flag `guided_tooltip_seen_fa-registration` sudah disetel dari perangkat lain sebelum sesi ini.

## Test Steps

### Kunjungan pertama menampilkan tur dan Skip menyetel flag
1. Masuk sebagai Tia R
2. Klik tab `Registration`
3. Verifikasi tur Guided Tooltip `fa-registration` tampil otomatis dengan Title `See what's missing` bagi Tia R
4. Klik `[Skip]`
5. Keluar dari aplikasi
6. Masuk kembali sebagai Tia R
7. Klik tab `Registration`
8. Verifikasi sub tab `Draft` tampil bagi Tia R sesudah masuk kembali
9. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Tia R sesudah masuk kembali

### Flag yang sudah disetel membuat tur tidak tampil
10. Masuk sebagai Uli S
11. Klik tab `Registration`
12. Verifikasi sub tab `Draft` tampil bagi Uli S
13. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Uli S

### Flag yang disetel dari perangkat lain berlaku di perangkat ini
14. Masuk sebagai Vera T dari perangkat yang belum pernah dipakai Vera T
15. Klik tab `Registration`
16. Verifikasi sub tab `Draft` tampil bagi Vera T
17. Verifikasi tur Guided Tooltip `fa-registration` tidak tampil bagi Vera T
