---
id: TC-FA-FAREG-E2E-103-kuota-group-dep-license
title: "Kuota Group: pesan Quantity, Remaining Quota nyata, dan blok Activate"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: [F-FAREG-05.k1, FAREG-LOGIC-05a, FAREG-LOGIC-05g, FAREG-LOGIC-05i, §9.2#p33, §9.2#p35, §9.2#p37, §9.2#p38, §9.2#p39, §9.4.2#r3, §9.4.2#r9, §9.4.2#r11, EB-CON-4, EB-XM-2@license, FAREG-LOGIC-05n, D-REG-08, V-REG-17]
smoke: [FAREG-LOGIC-05n, D-REG-08, V-REG-17]
dependsOn: ["License: kuota Group"]
trace:
  F-FAREG-05.k1: [15, 30]
  FAREG-LOGIC-05a: 15
  FAREG-LOGIC-05g: [10, 15]
  FAREG-LOGIC-05i: [10, 20, 23, 27]
  §9.2#p33: 8
  §9.2#p35: 12
  §9.2#p37: 15
  §9.2#p38: [15, 20]
  §9.2#p39: [17, 20]
  §9.4.2#r3: [8, 10, 15]
  §9.4.2#r9: 15
  §9.4.2#r11: [15, 20]
  EB-CON-4: [30, 36]
  EB-XM-2@license: [40, 46]
  FAREG-LOGIC-05n: [12, 14]
  D-REG-08: [14, 15]
  V-REG-17: 8
anchor: []
coverage:
  web: automated
---

# Kuota Group: pesan Quantity, Remaining Quota nyata, dan blok Activate

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Kuota {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-103-1: Group `Gudang Kuota {runId}` dengan sisa kuota Group `8`, ada di entitas aktor.
  - DU-103-2: Asset Name `Meja Kuota {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-103-3: Quantity `10` pada Item `Meja Kuota {runId}`, melebihi sisa kuota Group.
  - DU-103-4: Quantity `9` pada Item `Meja Kuota {runId}`, satu di atas sisa kuota Group.
  - DU-103-5: Quantity `8` pada Item `Meja Kuota {runId}`, tepat sama dengan sisa kuota Group.
  - DU-103-6: Quantity `1` pada Item `Meja Kuota {runId}`, saat sisa kuota Group `0`.
- Kondisi:
  - approval registrasi pada Group `Gudang Kuota {runId}` bernilai OFF.
  - sisa kuota tenant lebih besar dari `8`, sehingga sisa terkecil adalah sisa kuota Group.

## Test Steps

### Quantity melebihi sisa kuota Group langsung diberi pesan
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Kuota {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Meja Kuota {runId}`
5. Pilih Brand `Ergotec`
6. Pilih Model `No Model`
7. Isi Quantity `10`
8. Verifikasi error pada Quantity `Only 8 more assets can be added to Gudang Kuota {runId}. Reduce the quantity.`

### Save draft tetap berjalan dan Activate ditolak seluruhnya
9. Klik `[Save draft]`
10. Verifikasi toast `Success, draft has been saved.`
11. Klik `[Submit]`
12. Verifikasi dialog konfirmasi tampil lebih dulu dengan `Are you sure you want to activate it?`
13. Klik `[Activate]`
14. Verifikasi judul dialog `Cannot Activate` dan tombol `[OK]` tampil
15. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
16. Klik `[OK]`
17. Verifikasi `Remaining Quota: 8` tetap tampil di samping field Group

### Draft tetap dapat dibaca dan diekspor saat kuota tidak cukup
18. Klik `[Cancel]`
19. Ketik Search `Gudang Kuota {runId}`, tekan Enter
20. Verifikasi baris batch `Gudang Kuota {runId}` tetap di sub tab Draft dengan Total Asset `10`
21. Klik `[Download]`
22. Pilih `Download as CSV`
23. Verifikasi berkas `Registration-Drafts` terunduh

### Aset ke-N diterima dan ke-N+1 ditolak
24. Klik row action `Edit` pada baris batch `Gudang Kuota {runId}`
25. Ganti Quantity menjadi `9`
26. Klik `[Save draft]`
27. Verifikasi toast `Success, draft has been saved.`
28. Klik `[Submit]`
29. Klik `[Activate]`
30. Verifikasi dialog memuat `Group quota exceeded. Available slots: 8. Please contact administrator to increase quota.`
31. Klik `[OK]`
32. Ganti Quantity menjadi `8`
33. Klik `[Save draft]`
34. Klik `[Submit]`
35. Klik `[Activate]`
36. Verifikasi toast `Success, asset has been activated.`

### Sisa kuota Group habis tercermin di form Register Asset
37. Buka Fixed Asset > Assets > Registration > Draft
38. Klik `[+ Register Asset]`
39. Pilih Group `Gudang Kuota {runId}`
40. Verifikasi `Remaining Quota: 0` tampil di samping field Group
41. Klik `[+ Asset Name]`
42. Pilih Asset Name `Meja Kuota {runId}`
43. Pilih Brand `Ergotec`
44. Pilih Model `No Model`
45. Isi Quantity `1`
46. Verifikasi error pada Quantity `No more assets can be added to Gudang Kuota {runId}.`
