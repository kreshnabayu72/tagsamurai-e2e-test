---
id: TC-GS-ROLE-E2E-097-konkurensi-assign-concurrent-rebutan-kandidat-user
title: "Konkurensi Antar-Admin: Rebutan Kandidat User Simultan pada Assign Role dan Assign Total Control"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-279
  - TC-GS-ROLE-280
coverage:
  web: automated
---

# Konkurensi Antar-Admin: Rebutan Kandidat User Simultan pada Assign Role dan Assign Total Control

## Prerequisites

- Dual session context (Sesi A dan Sesi B submit bersamaan)
- Data Uji: Zahra Nabila (Dinamis #13), Nina Kartika (Dinamis #6)
- Setup Hook: dualContext: sessionA, sessionB
- Dua admin (sesi A, B) membuka Popup Assign Role Detail "Manage hardware"
- Dua admin Total Control membuka Popup Assign Total Control

## Test Steps

### Assign Role concurrent ke user yang sama oleh dua admin (TC-GS-ROLE-279)

1. Kedua sesi mencentang Zahra Nabila
2. Sesi A klik [Assign]
3. Sesi B klik [Assign]
4. Verifikasi Sesi A: toast sukses "Success, role has been assigned."
5. Verifikasi Sesi B: alert inline "Zahra Nabila is no longer eligible. Please select another."; centangan Zahra Nabila hilang
6. Verifikasi Detail hanya memuat 1 baris Zahra Nabila

### Assign Total Control concurrent ke user yang sama oleh dua admin (TC-GS-ROLE-280)

7. Kedua sesi mencentang Nina Kartika
8. Sesi A klik [Assign]
9. Sesi B klik [Assign]
10. Verifikasi Sesi A: toast sukses "Success, Total Control has been assigned."
11. Verifikasi Sesi B: alert inline "Nina Kartika is no longer eligible. Please select another."; popup tetap terbuka
12. Verifikasi Changelog Tab Total Control hanya 1 entry Assign untuk Nina Kartika

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin: Rebutan Kandidat User Simultan pada Assign Role dan Assign Total Control".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 D7; global-settings/role/PRD/role.md §9.4.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-279, TC-GS-ROLE-280.
