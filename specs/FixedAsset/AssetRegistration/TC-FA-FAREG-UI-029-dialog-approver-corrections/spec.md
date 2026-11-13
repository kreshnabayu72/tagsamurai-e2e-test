---
id: TC-FA-FAREG-UI-029-dialog-approver-corrections
title: "Dialog Approver Corrections: toolbar, kolom, dan empty state"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [D-REG-26, FAREG-LOGIC-07g, S-REG-31, §4.1#r19, §7.1#p1]
smoke: []
dependsOn: []
trace:
  D-REG-26: 2
  FAREG-LOGIC-07g: [3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 20, 21]
  S-REG-31: [20, 21]
  §4.1#r19: 2
  §7.1#p1: [20, 21]
anchor: []
coverage:
  web: automated
---

# Dialog Approver Corrections: toolbar, kolom, dan empty state

## Prerequisites
- Aktor: Hadi K (pengaju pengajuan, role Manage asset & TAG, cakupan Group terkelola).
- Layar awal: dialog `Approver Corrections` yang terbuka dari ikon `Changes by approver` pada Detail pengajuan Approved atau Partially Approved.
- Komponen: Dialog `Approver Corrections` (`D-REG-26`)
- Data:
  - DU-029-1: koreksi approver Asset `Laptop`, Field `Model`, Old Value `Latitude 5440`, New Value `Latitude 5450`, Modified By `Agus P`, Date `08/11/26, 14:02`.
  - Field yang diharapkan `Laptop (Model)`, dari Asset `Laptop` dan Field `Model`.
- Kondisi:
  - K1: pengajuan memiliki koreksi approver DU-029-1.
  - K2: pengajuan tidak memiliki koreksi approver.

## Test Steps

### Toolbar dan kolom dialog dengan koreksi
1. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
2. Verifikasi judul dialog `Approver Corrections`
3. Verifikasi toolbar memuat `Search`
4. Verifikasi toolbar memuat `Filter`
5. Verifikasi toolbar memuat `Export`
6. Verifikasi tabel koreksi memuat kolom `Date`
7. Verifikasi tabel koreksi memuat kolom `Field`
8. Verifikasi tabel koreksi memuat kolom `Old Value`
9. Verifikasi tabel koreksi memuat kolom `New Value`
10. Verifikasi tabel koreksi memuat kolom `Modified By`
11. Verifikasi sel Field pada baris DU-029-1 menampilkan `Laptop (Model)`

### Semua kolom dapat disembunyikan
12. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
13. Klik kontrol column visibility pada toolbar
14. Verifikasi kolom `Date` dapat disembunyikan
15. Verifikasi kolom `Field` dapat disembunyikan
16. Verifikasi kolom `Old Value` dapat disembunyikan
17. Verifikasi kolom `New Value` dapat disembunyikan
18. Verifikasi kolom `Modified By` dapat disembunyikan

### Empty state dialog tanpa koreksi
19. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K2
20. Verifikasi empty state memuat judul `No changes yet`
21. Verifikasi empty state memuat deskripsi `Corrections made by the approver will appear here.`
