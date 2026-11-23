---
id: TC-FA-DAMAGED-E2E-036-damage-log-my-asset-dep-my-asset
title: "Pelapor umum membuka Damage Log read-only laporannya sendiri dari My Asset termasuk record selesai, dan record orang lain ditolak 403"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.2.2#p1, §4.2.2#p2, §4.2.2#p3, §9.11#r3, §Aturan Logika Modul#r18, EC-DMG-22, S-DMG-17]
smoke: []
dependsOn:
  - "My Asset: status laporan dan tautan Damage Log"
trace:
  §4.2.2#p1: 8
  §4.2.2#p2: [8, 9, 10, 11, 12, 13, 16]
  §4.2.2#p3: [1, 2, 3, 4, 5, 6]
  §9.11#r3: [1, 2, 3, 4, 5, 6]
  §Aturan Logika Modul#r18: [3, 4, 5, 6]
  EC-DMG-22: [1, 2, 3, 4, 5, 6, 8, 16]
  S-DMG-17: [8, 9, 10, 11, 12, 13, 16]
coverage:
  web: automated
---

# Pelapor umum membuka Damage Log read-only laporannya sendiri dari My Asset termasuk record selesai, dan record orang lain ditolak 403

## Prerequisites
- Aktor: pelapor umum, yaitu pengguna tanpa role Damaged yang pernah melapor kerusakan aset.
- Layar awal: halaman My Asset.
- Data:
  - DU-036-1: aset `Mesin Fotokopi {runId} Waiting`, Group `Head Office {runId}`, dipegang aktor, record Damage laporan aktor berstatus `Waiting for Confirmation`.
  - DU-036-2: aset `Mesin Fotokopi {runId} Damaged`, Group `Head Office {runId}`, dipegang aktor, record Damage laporan aktor berstatus `Damaged`.
  - DU-036-3: aset `Mesin Fotokopi {runId} Repaired`, Group `Head Office {runId}`, record Damage laporan aktor berstatus `Repaired`.
  - DU-036-4: aset `Mesin Fotokopi {runId} Disposed`, Group `Head Office {runId}`, tidak dipegang aktor (laporan lewat scan), record Damage laporan aktor berstatus `Disposed`.
  - DU-036-5: aset `Mesin Fotokopi {runId} Rejected`, Group `Head Office {runId}`, tidak dipegang aktor (laporan lewat scan), record Damage laporan aktor berstatus `Rejected`, Damaged Photo `fotokopi-rusak.jpg`, ditolak Admin B (Total Control) dengan Reason `Kerusakan akibat kelalaian pengguna`.
  - DU-036-6: aset `Mesin Fotokopi {runId} Canceled`, Group `Head Office {runId}`, tidak dipegang aktor (laporan lewat scan), record Damage laporan aktor berstatus `Canceled`.
  - DU-036-7: aset `Mesin Fotokopi {runId} Milik Lain`, Group `Head Office {runId}`, record Damage berstatus `Damaged` yang dilaporkan pengguna lain.

## Test Steps

### Status laporan sendiri tampil di My Asset termasuk record selesai
1. Verifikasi status laporan `Waiting for Confirmation` tampil untuk aset `Mesin Fotokopi {runId} Waiting`
2. Verifikasi status laporan `Damaged` tampil untuk aset `Mesin Fotokopi {runId} Damaged`
3. Verifikasi status laporan `Repaired` tampil untuk aset `Mesin Fotokopi {runId} Repaired`
4. Verifikasi status laporan `Disposed` tampil untuk aset `Mesin Fotokopi {runId} Disposed` yang tidak dipegang aktor
5. Verifikasi status laporan `Rejected` tampil untuk aset `Mesin Fotokopi {runId} Rejected` yang tidak dipegang aktor
6. Verifikasi status laporan `Canceled` tampil untuk aset `Mesin Fotokopi {runId} Canceled` yang tidak dipegang aktor

### Damage Log read-only atas laporan sendiri yang sudah selesai
7. Buka dialog Damage Log dari kartu laporan aset `Mesin Fotokopi {runId} Rejected`
8. Verifikasi dialog `Damage Log` record aset `Mesin Fotokopi {runId} Rejected` tampil
9. Verifikasi `Damaged Photo` `fotokopi-rusak.jpg` tampil pada node `Reported damaged by`
10. Verifikasi nama admin yang memutuskan tampil pada node `Report rejected by`
11. Verifikasi Reason `Kerusakan akibat kelalaian pengguna` tampil pada node `Report rejected by`
12. Verifikasi footer `[Reject]` dan `[Confirm]` tidak tampil pada dialog
13. Verifikasi nilai finansial `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tampil pada dialog
14. Klik `✕` pada dialog Damage Log

### Damage Log record pelapor lain ditolak
15. Buka tautan Damage Log record aset `Mesin Fotokopi {runId} Milik Lain`
16. Verifikasi akses ditolak `403` tampil
