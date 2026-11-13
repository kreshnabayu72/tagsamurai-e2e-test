---
id: TC-FA-FAREG-E2E-077-registration-log-batch-draft
title: "Registration Log batch Draft: Created, Edited, dan batch kembalian"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06o, "§8.3#p1", "§8.3#r1", "§8.3#r2", "§8.3#r8"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06o: [24, 25, 26]
  "§8.3#p1": [12, 29]
  "§8.3#r1": [13, 14]
  "§8.3#r2": 21
  "§8.3#r8": [24, 25, 26]
anchor: [28]
coverage:
  web: automated
---

# Registration Log batch Draft: Created, Edited, dan batch kembalian

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Log {runId}` dan `Gudang Kembalian {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-077-1: Group `Gudang Log {runId}`, ada di entitas aktor.
  - DU-077-2: Group `Gudang Kembalian {runId}`, ada di entitas aktor.
  - DU-077-3: batch Draft kembalian milik Rina W di Group `Gudang Kembalian {runId}`, Total Asset `2`, dengan Origin berisi Registration ID pengajuan asal yang aset-nya dikembalikan ke Draft.
  - DU-077-4: input form yang dibuat langkah: Group `Gudang Log {runId}`, Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`.
  - DU-077-5: perubahan form yang dibuat langkah: Quantity `3`.
  - Node Registration Log yang diharapkan `Draft created by Rina W` dan `Draft edited by Rina W`, dari Rina W; nama singkat Rina W tampil `Rina W`.

## Test Steps

### Save draft pertama mencatat node Created
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Log {runId}` pada field Group
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Office Desk` pada Item pertama
5. Pilih Brand `Kayu Jati`
6. Pilih Model `No Model`
7. Isi Quantity `2`
8. Klik `[Save draft]`
9. Klik `[Cancel]` pada form; Draft baru saja disimpan sehingga tidak ada dialog Unsaved Changes
10. Ketik Search `{runId}`, tekan Enter
11. Klik ikon `Registration Log` pada baris Group `Gudang Log {runId}`
12. Verifikasi dialog `Registration Log` terbuka dengan Badge `Draft`
13. Verifikasi node timeline berjudul `Draft created by Rina W`
14. Verifikasi node itu memuat Total Asset `2`
15. Klik ikon `✕` pada dialog Registration Log

### Sesi edit mencatat node Edited
16. Klik ikon `Edit` pada baris Group `Gudang Log {runId}`
17. Ganti isi Quantity dengan `3`
18. Klik `[Save draft]`
19. Klik `[Cancel]` pada form; perubahan sudah disimpan sehingga tidak ada dialog Unsaved Changes
20. Klik ikon `Registration Log` pada baris Group `Gudang Log {runId}`
21. Verifikasi node timeline berjudul `Draft edited by Rina W`
22. Klik ikon `✕` pada dialog Registration Log

### Batch Draft kembalian dibuka dengan node Created by system
23. Klik ikon `Registration Log` pada baris Group `Gudang Kembalian {runId}`
24. Verifikasi node timeline berjudul `Draft created by System`
25. Verifikasi node itu memuat Total Asset `2`
26. Verifikasi node itu memuat baris `Origin:` berisi Registration ID pengajuan asal

### Registration Log tidak tersedia dari form Draft
27. Klik ikon `Edit` pada baris Group `Gudang Log {runId}`
28. Verifikasi form Edit Draft Group `Gudang Log {runId}` terbuka dengan Quantity `3`
29. Verifikasi kontrol `Registration Log` tidak tampil pada form Edit Draft
30. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
