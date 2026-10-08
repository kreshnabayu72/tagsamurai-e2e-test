---
id: TC-GS-ROLE-E2E-039-remove-access-level-tier-berbeda-toast-404-netral
title: "Pencabutan Access Level Saat Tier Target Berubah dari Tab yang Dirender: Toast 404 Netral dan Refresh Data"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-298
coverage:
  web: automated
---

# Pencabutan Access Level Saat Tier Target Berubah dari Tab yang Dirender: Toast 404 Netral dan Refresh Data

## Prerequisites

- Dual session context (Sesi A membuka Tab RO; Sesi B meng-upgrade target ke TC)
- Data Uji: Rizal Hakim (Pre-setup #18 / Dinamis #15)
- Setup Hook: dualContext: sessionA, sessionB
- Dua admin Total Control (sesi A: Ahmad Fauzi, sesi B: Eko Prasetyo)
- Rizal Hakim (Pre-setup #18) Read Only (Given: di-assign Read Only oleh Ahmad Fauzi; baris keenam role hasil bulk-write)

## Test Steps

### Remove access level saat tier target berbeda dari tab yang dirender (TC-GS-ROLE-298)

1. Sesi A: buka Tab Read Only (baris Rizal Hakim tampil)
2. Sesi B: Tab Total Control > [+ Assign] > centang Rizal Hakim > [Assign] (upgrade Read Only ke Total Control)
3. Sesi A: buka (⋯) baris Rizal Hakim > Remove > klik [Remove] pada dialog Remove Read Only
4. Sesi A: buka Tab Total Control, lalu Detail "Manage TAG"
5. Sesi A: buka Changelog Tab Total Control dan Changelog Tab Read Only
6. Verifikasi Muncul toast netral: "This access level is no longer available."
7. Verifikasi Tab Read Only di-refresh dan Rizal Hakim tidak ada
8. Verifikasi Rizal Hakim tetap Total Control di Tab Total Control (access level tidak dicabut)
9. Verifikasi Baris role Rizal Hakim tetap ada di Detail "Manage TAG" (tidak dihapus)
10. Verifikasi Tidak ada toast sukses dan tidak ada dialog konflik
11. Verifikasi Changelog Tab Total Control hanya memuat entry Assign upgrade dari sesi B (Old "Read Only", New "Total Control"); tidak ada entry Remove dari sesi A di Changelog Tab Total Control maupun Tab Read Only

## Notes

- Memvalidasi alur skenario "Pencabutan Access Level Saat Tier Target Berubah dari Tab yang Dirender: Toast 404 Netral dan Refresh Data".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Remove access level D6 tier berbeda dari tab yang dirender; global-settings/role/PRD/role.md §4.4 Target sudah tidak tersedia (404); global-settings/role/PRD/role.md §9.2 [F-ROLE-05]; foundation/process/prd-process/error-handling-convention.md §2.
- Sumber pemetaan test case granular: TC-GS-ROLE-298.
