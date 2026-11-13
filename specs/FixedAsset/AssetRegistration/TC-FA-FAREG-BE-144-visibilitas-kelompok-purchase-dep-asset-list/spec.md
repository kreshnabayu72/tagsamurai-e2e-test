---
id: TC-FA-FAREG-BE-144-visibilitas-kelompok-purchase-dep-asset-list
title: "Visibilitas kelompok Purchase per role"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-02a, FAREG-LOGIC-02b, FAREG-LOGIC-02c, FAREG-LOGIC-02e, "§2.2#r1", "§2.2#r2", "§2.2#b1", "§9.2#p72", "§9.2#p73", "§9.4.3#b2"]
smoke: []
dependsOn:
  - "Asset List: kolom dan export kelompok Purchase"
owner: BE
trace:
  FAREG-LOGIC-02a: 2
  FAREG-LOGIC-02b: [2, 4, 6, 8, 10, 12]
  FAREG-LOGIC-02c: [2, 4, 6, 8, 10, 12]
  FAREG-LOGIC-02e: [24, 26]
  "§2.2#r1": [2, 16, 18, 20, 22]
  "§2.2#r2": [16, 18, 20, 22]
  "§2.2#b1": [2, 4, 6, 8, 10, 12, 14, 24]
  "§9.2#p72": [14, 24]
  "§9.2#p73": 26
  "§9.4.3#b2": [2, 4, 6, 8, 10, 12]
---

# Visibilitas kelompok Purchase per role

## Prerequisites
- Aktor:
  - Rina W (hanya Manage asset & TAG, Group terkelola `Gudang Semarang {runId}`).
  - Lina (hanya Manage asset & TAG, Group terkelola `Gudang Semarang {runId}` dan satu Group lain).
  - Toni (Manage asset & TAG dengan Group terkelola `Gudang Semarang {runId}` dan juga Read Only).
  - Hana T (Total Control, seluruh client).
  - Dewi S (Group Manager Group `Gudang Semarang {runId}`).
  - Maya (Manage purchase, Group terkelola `Gudang Semarang {runId}`).
  - Roni (Read Only, seluruh client).
- Data:
  - DU-144-1: Group `Gudang Semarang {runId}`, ada di entitas aktor.
  - DU-144-2: aset `Active` `Genset {runId}` di Group `Gudang Semarang {runId}`, Condition `Normal`, Alias Name `Genset Gudang {runId}`, Purchase status `Pending`.

## Test Steps

### Aktor yang hanya memegang Manage asset & TAG tidak menerima kelompok Purchase
1. Rina W meminta data aset DU-144-2 lewat form
2. Verifikasi respons form memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong
3. Rina W meminta data aset DU-144-2 lewat Asset List
4. Verifikasi respons Asset List memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong
5. Rina W meminta data aset DU-144-2 lewat export
6. Verifikasi respons export memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong
7. Rina W meminta data aset DU-144-2 lewat hasil scan
8. Verifikasi respons hasil scan memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong
9. Rina W meminta data aset DU-144-2 lewat template impor
10. Verifikasi respons template impor memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong
11. Rina W meminta data aset DU-144-2 lewat API
12. Verifikasi respons API memuat kelompok General dan tidak memuat satu pun field kelompok Purchase, termasuk Purchase status, karena field itu dihilangkan di query dan bukan ditampilkan kosong

### Aktor Manage asset & TAG di beberapa Group tetap tanpa kelompok Purchase
13. Lina meminta data aset DU-144-2 lewat Asset List
14. Verifikasi respons Asset List memuat kelompok General dan tidak memuat field kelompok Purchase

### Role dengan akses Purchase menerima kelompok General dan Purchase
15. Hana T (Total Control) meminta data aset DU-144-2 lewat Asset List
16. Verifikasi respons Asset List memuat kelompok General dan kelompok Purchase, termasuk Purchase status `Pending`
17. Dewi S (Group Manager) meminta data aset DU-144-2 lewat Asset List
18. Verifikasi respons Asset List memuat kelompok General dan kelompok Purchase, termasuk Purchase status `Pending`
19. Maya (Manage purchase) meminta data aset DU-144-2 lewat Asset List
20. Verifikasi respons Asset List memuat kelompok General dan kelompok Purchase, termasuk Purchase status `Pending`
21. Roni (Read Only) meminta data aset DU-144-2 lewat Asset List
22. Verifikasi respons Asset List memuat kelompok General dan kelompok Purchase, termasuk Purchase status `Pending`

### Pengguna multi-role mengikuti hak yang lebih luas
23. Toni meminta data aset DU-144-2 lewat Asset List
24. Verifikasi respons Asset List memuat kelompok General dan kelompok Purchase karena Toni mengikuti hak yang lebih luas dari Manage asset & TAG dan Read Only
25. Toni meminta data aset DU-144-2 lewat export
26. Verifikasi respons export memuat kelompok Purchase sehingga Toni tidak diperlakukan sebagai pemegang Manage asset & TAG saja
