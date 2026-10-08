---
id: TC-GS-ROLE-E2E-026-assign-total-control-happy-path-single-dan-multi-user
title: "Penugasan Total Control Berhasil untuk User Tunggal dan Multi-User Serta Refleksi Rename User Sesi B"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-58
  - TC-GS-ROLE-59
  - TC-GS-ROLE-67
coverage:
  web: automated
---

# Penugasan Total Control Berhasil untuk User Tunggal dan Multi-User Serta Refleksi Rename User Sesi B

## Prerequisites

- Login sebagai Total Control
- Data Uji: Sari Wulandari (Dinamis #1), Maya Anggraini & Rudi Hartono (Dinamis #2), Olivia Rahma (Dinamis #11)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Sari Wulandari tanpa access level dan tanpa baris role
- Eko Prasetyo login di sesi B

## Test Steps

### Assign Total Control ke satu user (TC-GS-ROLE-58)

1. Klik [+ Assign]
2. Centang Sari Wulandari
3. Klik [Assign]
4. Buka Tab System
5. Buka Detail "Manage TAG" dan "Import data"
6. Verifikasi Muncul toast sukses: "Success, Total Control has been assigned."
7. Verifikasi Popup tertutup; baris Sari Wulandari tampil di Tab Total Control dengan Modified By "Ahmad F" dan Last Updated = waktu assign
8. Verifikasi Tidak ada dialog konfirmasi sebelum assign
9. Verifikasi Tab System: kolom Users keenam role bertambah 1
10. Verifikasi Detail "Manage TAG": baris Sari Wulandari Read dan Update checked
11. Verifikasi Detail "Import data": baris Sari Wulandari Create dan Read checked

### Assign Total Control ke beberapa user sekaligus termasuk Inactive dan Pending Activation (TC-GS-ROLE-59)

12. Klik [+ Assign]
13. Centang Maya Anggraini dan Rudi Hartono
14. Klik [Assign]
15. Verifikasi Muncul toast sukses: "Success, Total Control has been assigned."
16. Verifikasi Maya Anggraini tampil di Tab Total Control dengan Status "Inactive"
17. Verifikasi Rudi Hartono tampil dengan badge "Pending Activation" di sebelah Name

### Assign Total Control saat user terpilih di-rename sebelum submit (TC-GS-ROLE-67)

18. Sesi A: [+ Assign] > centang Olivia Rahma
19. Sesi B: rename Olivia Rahma menjadi Olivia Rahmawati di modul User
20. Sesi A: klik [Assign]
21. Verifikasi Toast sukses: "Success, Total Control has been assigned."
22. Verifikasi Tab Total Control menampilkan "Olivia Rahmawati"
23. Verifikasi Tidak ada alert stale reference

## Notes

- Memvalidasi alur skenario "Penugasan Total Control Berhasil untuk User Tunggal dan Multi-User Serta Refleksi Rename User Sesi B".
- Aturan PRD terkait: global-settings/role/PRD/role.md §3 Alur assign; global-settings/role/PRD/role.md §9.2 [F-ROLE-04]; global-settings/role/PRD/role.md §7.1 T-02; global-settings/role/PRD/role.md ROLE-LOGIC-06a; global-settings/role/PRD/role.md §9.4.2 Assign D1; global-settings/role/PRD/role.md §6 V-13; global-settings/role/PRD/role.md §9.4.2 rename D6.
- Sumber pemetaan test case granular: TC-GS-ROLE-58, TC-GS-ROLE-59, TC-GS-ROLE-67.
