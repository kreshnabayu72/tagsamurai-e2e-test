---
id: TC-FA-FAREG-UI-029-dialog-approver-corrections
title: "Dialog Approver Corrections: toolbar, kolom, dan empty state"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-REG-26, FAREG-LOGIC-07g, S-REG-31, §4.1#r19, §7.1#p1]
smoke: []
dependsOn: []
trace:
  D-REG-26: 2
  FAREG-LOGIC-07g: [3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 18, 20, 22, 27, 29, 30, 32, 33, 34, 35]
  S-REG-31: [29, 30]
  §4.1#r19: 2
  §7.1#p1: [29, 30]
anchor: [14, 25]
coverage:
  web: automated
---

# Dialog Approver Corrections: toolbar, kolom, dan empty state

## Prerequisites
- Aktor: Hadi K (pengaju pengajuan, role Manage asset & TAG, cakupan Group terkelola).
- Layar awal: dialog `Approver Corrections` yang terbuka dari ikon `Changes by approver` pada Detail pengajuan Approved atau Partially Approved.
- Komponen: Dialog `Approver Corrections` (`D-REG-26`)
- Data:
  - DU-029-1: koreksi approver Asset `Laptop`, Field `Model`, Old Value `Latitude 5440`, New Value `Latitude 5450`, Modified By `Agus P.`, Date `08/11/26, 14:02`.
  - Field yang diharapkan `Laptop (Model)`, dari Asset `Laptop` dan Field `Model`.
- Kondisi:
  - K1: pengajuan memiliki koreksi approver DU-029-1, dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam.
  - K2: pengajuan tidak memiliki koreksi approver.

## Test Steps

### Toolbar dan kolom dialog dengan koreksi
1. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
2. Verifikasi judul dialog `Approver Corrections`
3. Verifikasi toolbar memuat `Search`
4. Verifikasi toolbar memuat `Filter`
5. Verifikasi toolbar memuat `Download`[^drift-1]
6. Verifikasi tabel koreksi memuat kolom `Date`
7. Verifikasi tabel koreksi memuat kolom `Field`
8. Verifikasi tabel koreksi memuat kolom `Old Value`
9. Verifikasi tabel koreksi memuat kolom `New Value`
10. Verifikasi tabel koreksi memuat kolom `Modified By`
11. Verifikasi sel Field pada baris DU-029-1 menampilkan `Laptop (Model)`

### Kolom Date, Field, Old Value, dan New Value dapat disembunyikan
12. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
13. Klik `Column Visibility`
14. Verifikasi tabel koreksi memuat kolom `Modified By`
15. Hilangkan centang `Date` pada daftar kolom
16. Verifikasi kolom `Date` tidak tampil di tabel koreksi
17. Hilangkan centang `Field` pada daftar kolom
18. Verifikasi kolom `Field` tidak tampil di tabel koreksi
19. Hilangkan centang `Old Value` pada daftar kolom
20. Verifikasi kolom `Old Value` tidak tampil di tabel koreksi
21. Hilangkan centang `New Value` pada daftar kolom
22. Verifikasi kolom `New Value` tidak tampil di tabel koreksi

### Kolom Modified By dapat disembunyikan
23. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
24. Klik `Column Visibility`
25. Verifikasi tabel koreksi memuat kolom `Date`
26. Hilangkan centang `Modified By` pada daftar kolom
27. Verifikasi kolom `Modified By` tidak tampil di tabel koreksi

### Empty state dialog tanpa koreksi
28. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K2
29. Verifikasi empty state memuat judul `No changes yet`
30. Verifikasi empty state memuat deskripsi `Corrections made by the approver will appear here.`

### Nilai sel baris koreksi
31. Tampilkan Dialog `Approver Corrections` (`D-REG-26`) dengan kondisi K1
32. Verifikasi sel Date pada baris DU-029-1 menampilkan `08/11/26, 14:02`
33. Verifikasi sel Old Value pada baris DU-029-1 menampilkan `Latitude 5440`
34. Verifikasi sel New Value pada baris DU-029-1 menampilkan `Latitude 5450`
35. Verifikasi sel Modified By pada baris DU-029-1 menampilkan `Agus P.` (approver pengajuan)[^drift-2]

[^drift-1]: Drift PRD vs foundation. PRD `FAREG-LOGIC-07g`: toolbar dialog `Search · Filter · Export`. foundation `prd-conventions.md` §9.1 (Global Table Rules, toolbar): `Search (icon) | Filter | Download`; kontrak wangs-ui `Tooltip#26` dan `DataTable#81`: ExportButton bertooltip dan beraria-label `Download`. Diasersi: foundation, karena tombol unduh toolbar tabel adalah komponen bersama (SB-4).

[^drift-2]: Drift PRD vs override. PRD `FAREG-LOGIC-07g`: Modified By (= approver); PRD §8.3 contoh Activity Log: `Agus P.`; `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]` tanpa titik (`John L`). Baris O-4: nama singkat mengakhiri inisial dengan titik (`John L.`). Diasersi: override O-4 (SB-6), sehingga `Agus P.`.
