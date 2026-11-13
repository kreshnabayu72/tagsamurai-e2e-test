---
id: TC-FA-FAREG-E2E-082-approval-koreksi-diterapkan
title: "Koreksi approver: staged, diterapkan saat Approve, dan terbaca di Approver Corrections"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-07g, FAREG-LOGIC-07j, "§9.7#r16", FAREG-LOGIC-07d, T-REG-11]
smoke: [FAREG-LOGIC-07d, T-REG-11]
dependsOn: []
trace:
  FAREG-LOGIC-07g: [21, 23, 42, 44, 46, 47]
  FAREG-LOGIC-07j: 15
  "§9.7#r16": [15, 23]
  FAREG-LOGIC-07d: [8, 10]
  T-REG-11: 7
anchor: []
coverage:
  web: automated
---
# Koreksi approver: staged, diterapkan saat Approve, dan terbaca di Approver Corrections

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Koreksi {runId}` dan Group `Gudang Koreksi Sebagian {runId}`, approver). Rina W (Manage asset & TAG) adalah pengaju pengajuan.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-082-1: Group `Gudang Koreksi {runId}`, ada di entitas aktor.
  - DU-082-2: pengajuan Waiting for Approval di Group `Gudang Koreksi {runId}`, diajukan Rina W
  - DU-082-3: satu Item pada pengajuan itu: Asset Name `Laptop`, Brand `Dell`, Model `Latitude 5440`, Quantity `2`, Condition `Normal`, TAG Type `RFID`; Total Asset `2`.
  - DU-082-4: Tag RFID `RFID-082-{n}-{runId}` terpasang dengan Badge `Verified` pada setiap aset, `{n}` bernomor 1 sampai 2.
  - DU-082-5: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Koreksi {runId}` dan Group `Gudang Koreksi Sebagian {runId}`).
  - Nama singkat Budi S tampil `Budi S`.
  - DU-082-6: Model `Latitude 5540` milik Brand `Dell`, tersedia di master Model.
  - DU-082-7: koreksi yang diisi langkah: Model aset ke-1 menjadi `Latitude 5540`.
  - DU-082-8: Group `Gudang Koreksi Sebagian {runId}`, ada di entitas aktor.
  - DU-082-9: pengajuan Waiting for Approval di Group `Gudang Koreksi Sebagian {runId}`, diajukan Rina W
  - DU-082-10: satu Item pada pengajuan itu: Asset Name `Laptop`, Brand `Dell`, Model `Latitude 5440`, Quantity `2`, Condition `Normal`, TAG Type `RFID`; Total Asset `2`.
  - DU-082-11: Tag RFID `RFID-082B-{n}-{runId}` terpasang dengan Badge `Verified` pada setiap aset, `{n}` bernomor 1 sampai 2.
  - DU-082-12: Model `Latitude 7440` milik Brand `Dell`, tersedia di master Model.
  - DU-082-13: koreksi dan keputusan yang diisi langkah: Model aset ke-1 menjadi `Latitude 5540` dengan keputusan `Approve`; Model aset ke-2 menjadi `Latitude 7440` dengan keputusan `Return to Draft` dan Reason `Photo is missing`.
- Kondisi:
  - Group `Gudang Koreksi {runId}` dan Group `Gudang Koreksi Sebagian {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Koreksi Model disimpan staged dan bertahan sesudah halaman ditutup
1. Buka menu Approvals > Registration, tab `Active`
2. Ketik Search `{runId}`, tekan Enter
3. Klik ikon `Review` pada baris Group `Gudang Koreksi {runId}`
4. Klik Name aset ke-1 pada grup `Laptop` untuk membuka panel koreksi
5. Pilih Model `Latitude 5540` pada field Model panel koreksi
6. Klik `[Save correction]`
7. Verifikasi toast `Success, correction has been saved.` tampil
8. Verifikasi kolom Corrections aset ke-1 menampilkan Badge `1`
9. Klik Badge `1` pada kolom Corrections aset ke-1
10. Verifikasi dialog `Corrections` memuat Old Value `Latitude 5440` dan New Value `Latitude 5540`
11. Klik `[Close]` pada dialog `Corrections`
12. Klik `[Cancel]` pada footer halaman Approval
13. Ketik Search `{runId}`, tekan Enter
14. Klik ikon `Review` pada baris Group `Gudang Koreksi {runId}`
15. Verifikasi kolom Corrections aset ke-1 masih menampilkan Badge `1` sesudah halaman dibuka kembali

### Approve menerapkan koreksi dan terbaca di Approver Corrections
16. Klik `[Submit]`
17. Klik `[Submit]` pada dialog `Submit Approval`
18. Klik tab `History`
19. Ketik Search `{runId}`, tekan Enter
20. Klik ikon `Detail` pada baris Group `Gudang Koreksi {runId}`
21. Verifikasi ikon `Changes by approver` tampil pada header halaman Detail
22. Klik ikon `Changes by approver`
23. Verifikasi dialog `Approver Corrections` memuat baris dengan Field `Laptop (Model)`, Old Value `Latitude 5440`, New Value `Latitude 5540`, dan Modified By `Budi S`

### Koreksi pada pengajuan Partially Approved hanya memuat aset yang di-approve
24. Klik ikon `✕` pada dialog Approver Corrections
25. Buka menu Approvals > Registration, tab `Active`
26. Ketik Search `{runId}`, tekan Enter
27. Klik ikon `Review` pada baris Group `Gudang Koreksi Sebagian {runId}`
28. Klik Name aset ke-1 pada grup `Laptop` untuk membuka panel koreksi
29. Pilih Model `Latitude 5540` pada field Model panel koreksi
30. Klik `[Save correction]`
31. Klik Name aset ke-2 pada grup `Laptop` untuk membuka panel koreksi
32. Pilih Model `Latitude 7440` pada field Model panel koreksi
33. Klik `[Save correction]`
34. Centang aset ke-2 pada grup `Laptop`
35. Pilih `Return to Draft` pada Bulk Action
36. Isi Reason `Photo is missing`
37. Klik `[Apply]`
38. Klik `[Submit]`
39. Klik `[Submit]` pada dialog `Submit Approval`
40. Klik tab `History`
41. Ketik Search `{runId}`, tekan Enter
42. Verifikasi baris pengajuan Group `Gudang Koreksi Sebagian {runId}` tampil di tab `History` dengan Status `Partially Approved`
43. Klik ikon `Detail` pada baris Group `Gudang Koreksi Sebagian {runId}`
44. Verifikasi ikon `Changes by approver` tampil pada header halaman Detail
45. Klik ikon `Changes by approver`
46. Verifikasi dialog `Approver Corrections` memuat baris dengan Field `Laptop (Model)`, Old Value `Latitude 5440`, New Value `Latitude 5540`, dan Modified By `Budi S`
47. Verifikasi dialog `Approver Corrections` tidak memuat baris dengan New Value `Latitude 7440`
