---
id: TC-FA-FAREG-E2E-100-edit-setelah-active-dep-asset-list
title: "Edit setelah Active: field yang diizinkan dan field terkunci"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: [F-FAREG-10, FAREG-LOGIC-12a, FAREG-LOGIC-12b, FAREG-LOGIC-12c, FAREG-LOGIC-12d, S-REG-14, §9.2#r22, §9.2#r23, §9.2#r24, §9.2#r25, §9.4.2#r60, §9.4.2#r61, §9.4.2#r63, §9.4.3#b9, §9.6#r10, §9.7#r13]
smoke: []
dependsOn: ["Asset List: Row Action Edit aset Active"]
trace:
  F-FAREG-10: [4, 12, 22]
  FAREG-LOGIC-12a: [22, 23, 24, 25, 26, 27, 28]
  FAREG-LOGIC-12b: [4, 6, 8, 10, 12]
  FAREG-LOGIC-12c: 12
  FAREG-LOGIC-12d: [4, 6, 8, 10]
  S-REG-14: 12
  §9.2#r22: [22, 23, 24, 25, 26, 27]
  §9.2#r23: 28
  §9.2#r24: 4
  §9.2#r25: 12
  §9.4.2#r60: [4, 6, 8, 10, 12]
  §9.4.2#r61: 44
  §9.4.2#r63: [35, 38]
  §9.4.3#b9: 12
  §9.6#r10: [30, 35]
  §9.7#r13: 30
anchor: []
coverage:
  web: automated
---

# Edit setelah Active: field yang diizinkan dan field terkunci

## Prerequisites
- Aktor:
  - Dewi, role Group Manager dengan Group binaan `Gudang Edit {runId}` beserta sub-group.
  - Toni, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu perubahan.
- Layar awal: Fixed Asset > Assets > Assets.
- Data:
  - DU-100-1: Group `Gudang Edit {runId}`, ada di entitas aktor.
  - DU-100-2: aset Active `Laptop Edit {runId}`, Brand `Dell`, Model `Latitude 5440`, Alias Name `Laptop Finance {runId}`, Serial Number `SN-0100-A`, Condition `Normal`, Group `Gudang Edit {runId}`.
  - DU-100-3: Brand `Lenovo` dengan Model `ThinkPad T14`, ada di master Brand dan Model.
  - DU-100-4: Asset Label `Aset Kantor {runId}`, ada di master Asset Label.

## Test Steps

### Field terkunci tampil Disabled dengan jalur yang benar
1. Ketik Search `Laptop Edit {runId}`, tekan Enter
2. Klik row action `Edit` pada baris aset `Laptop Edit {runId}`
3. Arahkan kursor ke field Asset Name
4. Verifikasi field Asset Name Disabled dengan tooltip `Asset Name changes through Move Asset Names.`
5. Arahkan kursor ke field Condition
6. Verifikasi field Condition Disabled dengan tooltip `Condition changes through a Damaged or Missing report.`
7. Arahkan kursor ke field Tag
8. Verifikasi field Tag Disabled dengan tooltip `TAG changes through TAG replacement.`
9. Arahkan kursor ke field Asset Code
10. Verifikasi field Asset Code Disabled dengan tooltip `Asset Code is locked.`
11. Arahkan kursor ke field Group
12. Verifikasi field Group Disabled dengan tooltip `Group changes through a Transfer.`

### Field yang diizinkan tersimpan dan tercatat di log aset
13. Pilih Brand `Lenovo`
14. Pilih Model `ThinkPad T14`
15. Ganti Alias Name menjadi `Laptop Tim Keuangan {runId}`
16. Pilih Asset labels `Aset Kantor {runId}`
17. Ganti Serial Number menjadi `SN-0100-B`
18. Unggah Photo `laptop-edit.jpg`
19. Ganti Cost pada kelompok Purchase menjadi `15000000`
20. Simpan perubahan aset
21. Klik row action `Detail` pada baris aset `Laptop Edit {runId}`
22. Verifikasi Brand aset `Lenovo`
23. Verifikasi Model aset `ThinkPad T14`
24. Verifikasi Alias Name aset `Laptop Tim Keuangan {runId}`
25. Verifikasi Asset labels aset `Aset Kantor {runId}`
26. Verifikasi Serial Number aset `SN-0100-B`
27. Verifikasi Photo `laptop-edit.jpg` tampil pada aset
28. Verifikasi Cost aset `15000000`
29. Buka bagian log aset
30. Verifikasi entri log dengan Field `Alias Name`, Old Value `Laptop Finance {runId}`, dan New Value `Laptop Tim Keuangan {runId}` tampil

### Simpan tanpa perubahan tidak menambah log
31. Catat jumlah entri log aset
32. Klik row action `Edit` pada baris aset `Laptop Edit {runId}`
33. Ganti Alias Name menjadi `LAPTOP TIM KEUANGAN {runId}`
34. Simpan perubahan aset
35. Verifikasi toast `No changes to save.`
36. Klik row action `Detail` pada baris aset `Laptop Edit {runId}`
37. Buka bagian log aset
38. Verifikasi jumlah entri log aset sama dengan jumlah yang dicatat

### Dua pengguna mengedit aset yang sama
39. Dewi klik row action `Edit` pada baris aset `Laptop Edit {runId}`
40. Toni mengubah Alias Name aset menjadi `Laptop Edit B {runId}`
41. Toni menyimpan perubahan aset
42. Dewi mengganti Alias Name menjadi `Laptop Edit A {runId}`
43. Dewi menyimpan perubahan aset
44. Verifikasi Alias Name aset `Laptop Edit A {runId}` pada Detail aset
