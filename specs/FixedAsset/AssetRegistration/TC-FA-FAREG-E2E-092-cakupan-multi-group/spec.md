---
id: TC-FA-FAREG-E2E-092-cakupan-multi-group
title: "Cakupan Group: pengguna dengan beberapa Group melihat gabungan draft"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-02e", "§9.2#p66", "§9.2#p68", "§9.2#p70", "§9.2#p71", "§9.5#r9"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-02e": [3, 4, 14]
  "§9.2#p66": [3, 4]
  "§9.2#p68": [3, 4]
  "§9.2#p70": [3, 4]
  "§9.2#p71": [3, 4, 13, 14]
  "§9.5#r9": [7, 17, 18, 26, 27]
coverage:
  web: automated
---

# Cakupan Group: pengguna dengan beberapa Group melihat gabungan draft

## Prerequisites
- Aktor: Lina M (Manage asset & TAG, Group terkelola `Gudang 1 {runId}` dan `Gudang 2 {runId}`), lalu Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}` saja).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-092-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-092-2: Batch Draft dengan Group `Gudang 2 {runId}`, Origin `—`, Total Asset `5`, Progress `0%`, Requested By `Lina M`, Last Updated `T0 − 2 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `5`.
  - DU-092-3: Lina M (Manage asset & TAG, Group terkelola `Gudang 1 {runId}` dan `Gudang 2 {runId}`).
  - DU-092-4: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-092-5: Group `Kantor Induk {runId}`, induk dari Group `Gudang 1 {runId}` dan `Gudang 2 {runId}`, di luar Group terkelola Lina M dan Rina W.
  - DU-092-6: Group `Gudang 1 Rak {runId}`, sub-group dari Group `Gudang 1 {runId}`.
- Kondisi:
  - Group `Gudang 1 {runId}` dan `Gudang 2 {runId}` adalah sub-group dari Group `Kantor Induk {runId}`.
  - Group `Gudang 1 Rak {runId}` adalah sub-group dari Group `Gudang 1 {runId}`, dan tidak disebut sendiri sebagai Group terkelola Lina M.

## Test Steps

### Lina M melihat gabungan batch Draft Gudang 1 dan Gudang 2
1. Klik tab `Registration`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` tampil di sub tab `Draft` bagi Lina M
4. Verifikasi baris Group `Gudang 2 {runId}` dengan Requested By `Lina M` tampil di sub tab `Draft` bagi Lina M

### Selector Group pada form Register Asset memuat Group dalam scope Lina M
5. Klik `[+ Register Asset]`
6. Buka field Group
7. Verifikasi pilihan Group memuat `Gudang 1 {runId}` dan `Gudang 2 {runId}` bagi Lina M
8. Tutup daftar pilihan Group tanpa memilih
9. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes

### Rina W hanya melihat batch Draft Gudang 1
10. Masuk sebagai Rina W
11. Klik tab `Registration`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` tampil di sub tab `Draft` bagi Rina W
14. Verifikasi tidak ada baris Group `Gudang 2 {runId}` di sub tab `Draft` bagi Rina W

### Selector Group pada form Register Asset memuat Group dalam scope Rina W
15. Klik `[+ Register Asset]`
16. Buka field Group
17. Verifikasi pilihan Group memuat `Gudang 1 {runId}` bagi Rina W
18. Verifikasi pilihan Group tidak memuat `Gudang 2 {runId}` bagi Rina W
19. Tutup daftar pilihan Group tanpa memilih
20. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes

### Selector Group menampilkan hierarki Group dalam scope Lina M
21. Masuk sebagai Lina M
22. Klik tab `Registration`
23. Klik `[+ Register Asset]`
24. Buka field Group
25. Perluas node `Gudang 1 {runId}` pada pilihan Group
26. Verifikasi `Gudang 1 Rak {runId}` tampil sebagai anak node `Gudang 1 {runId}` bagi Lina M
27. Verifikasi `Kantor Induk {runId}` tidak tampil pada pilihan Group bagi Lina M
28. Tutup daftar pilihan Group tanpa memilih
29. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes
