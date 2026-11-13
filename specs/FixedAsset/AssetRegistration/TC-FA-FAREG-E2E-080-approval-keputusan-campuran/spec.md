---
id: TC-FA-FAREG-E2E-080-approval-keputusan-campuran
title: "Keputusan approval: campuran Approve, Return to Draft, dan Reject"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06f, FAREG-LOGIC-06g, FAREG-LOGIC-06n, "§9.2#p24", "§9.2#p26", "§9.2#p28", "§9.2#p29", "§9.2#p30", "§9.2#p31", "§9.4.2#r21", "§9.7#r11", FAREG-LOGIC-06h, S-REG-20]
smoke: [FAREG-LOGIC-06h, S-REG-20]
dependsOn: []
trace:
  FAREG-LOGIC-06f: [31, 41]
  FAREG-LOGIC-06g: [32, 36, 37, 45]
  FAREG-LOGIC-06n: [41, 42, 44, 45, 46, 47, 48, 57, 58]
  "§9.2#p24": 9
  "§9.2#p26": [30, 31, 32]
  "§9.2#p28": 26
  "§9.2#p29": [26, 30]
  "§9.2#p30": 49
  "§9.2#p31": 27
  "§9.4.2#r21": [41, 46]
  "§9.7#r11": [41, 49]
  FAREG-LOGIC-06h: 26
  S-REG-20: 46
anchor: []
coverage:
  web: automated
---
# Keputusan approval: campuran Approve, Return to Draft, dan Reject

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Campuran {runId}`, approver dan pemegang akses Group yang sama dengan pengaju). Hadi K (Manage asset & TAG) adalah pengaju pengajuan.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-080-1: Group `Gudang Campuran {runId}` dengan batas kuota aset `50`, ada di entitas aktor.
  - DU-080-2: pengajuan Waiting for Approval di Group `Gudang Campuran {runId}`, diajukan Hadi K, Total Asset `30`.
  - DU-080-3: Item pertama pada pengajuan itu: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `23`, Condition `Normal`, TAG Type `Non-TAG`.
  - DU-080-4: Item kedua pada pengajuan itu: Asset Name `Laptop`, Brand `Dell`, Model `Latitude 5440`, Quantity `7`, Condition `Normal`, TAG Type `RFID`; setiap aset ber-Tag `Verified` dengan kode `RFID-080-{n}-{runId}`, `{n}` bernomor 1 sampai 7.
  - DU-080-5: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Campuran {runId}`).
  - DU-080-6: Hadi K (Manage asset & TAG, Group terkelola `Gudang Campuran {runId}`), pengaju.
  - DU-080-7: batch Draft pembanding milik Hadi K di Group `Gudang Campuran {runId}`, Total Asset `1`.
  - DU-080-8: keputusan yang diisi langkah: Return to Draft dengan Reason `Photo is missing` dan `Quantity is wrong`; Reject dengan Reason `Duplicate entry`.
  - Requested By yang diharapkan pada pengajuan hasil Submit Budi S atas batch kembalian `Hadi K`, dari Owner batch kembalian milik Hadi K (DU-080-6); Total Asset `5`.
- Kondisi:
  - Group `Gudang Campuran {runId}` ber-toggle `Require Approval for Registration` ON.
  - Himpunan approver eligible pada node Group `Gudang Campuran {runId}` berisi Budi S dan Total Control, sehingga pengajuan hasil Submit Budi S masuk Waiting for Approval.
  - Seluruh aset batch Draft kembalian memenuhi Tingkat 2 dan kuota Group cukup.

## Test Steps

### Mencatat sisa kuota Group lalu keputusan campuran per grup Accordion lewat Bulk Action
1. Buka Fixed Asset > Assets > Registration, sub tab `Draft`
2. Ketik Search `{runId}`, tekan Enter
3. Klik ikon `Edit` pada baris Group `Gudang Campuran {runId}`
4. Catat nilai `Remaining Quota` pada form
5. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
6. Buka menu Approvals > Registration, tab `Active`
7. Ketik Search `{runId}`, tekan Enter
8. Klik ikon `Review` pada baris Group `Gudang Campuran {runId}`
9. Verifikasi halaman Approval memuat Status `Waiting for Approval`, Requested By `Hadi K`, dan Total Asset `30`
10. Centang aset ke-1 sampai ke-3 pada grup `Office Desk`
11. Pilih `Return to Draft` pada Bulk Action
12. Isi Reason `Photo is missing`
13. Klik `[Apply]`
14. Centang aset ke-1 dan ke-2 pada grup `Laptop`
15. Pilih `Return to Draft` pada Bulk Action
16. Isi Reason `Quantity is wrong`
17. Klik `[Apply]`
18. Centang aset ke-3 sampai ke-7 pada grup `Laptop`
19. Pilih `Reject` pada Bulk Action
20. Isi Reason `Duplicate entry`
21. Klik `[Apply]`
22. Klik `[Submit]`
23. Klik `[Submit]` pada dialog `Submit Approval`

### Status pengajuan Partially Approved dan Result per aset
24. Klik tab `History`
25. Ketik Search `{runId}`, tekan Enter
26. Verifikasi baris Group `Gudang Campuran {runId}` tampil dengan Total Asset `30` dan Status `Partially Approved`
27. Verifikasi hanya satu baris yang tampil sehingga tidak ada baris berstatus `Approved` atau `Rejected`
28. Klik ikon `Detail` pada baris Group `Gudang Campuran {runId}`
29. Klik tab `Asset`
30. Verifikasi tepat 20 aset berkolom Result `Approved` pada seluruh halaman tabel
31. Verifikasi 5 aset berkolom Result `Returned` dengan Reason `Photo is missing` pada 3 aset dan `Quantity is wrong` pada 2 aset
32. Verifikasi 5 aset berkolom Result `Rejected` dengan Reason `Duplicate entry`
33. Klik `[Close]` pada footer halaman Detail

### Registration Log mencatat aset yang ditolak
34. Ketik Search `{runId}`, tekan Enter
35. Klik ikon `Registration Log` pada baris Group `Gudang Campuran {runId}`
36. Verifikasi node timeline berjudul `Partially approved by Budi S` memuat Jumlah Approved `20`, Returned `5`, dan Rejected `5`
37. Verifikasi Reason `Duplicate entry` tercatat pada node tersebut sebagai alasan aset yang ditolak
38. Klik ikon `✕` pada dialog Registration Log

### Aset Return to Draft kembali sebagai batch Draft baru milik pengaju
39. Buka Fixed Asset > Assets > Registration, sub tab `Draft`
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi baris batch Group `Gudang Campuran {runId}` dengan Total Asset `5` tampil di sub tab `Draft`
42. Verifikasi batch dengan Total Asset `5` itu memiliki Requested By `Hadi K`
43. Klik ikon `Edit` pada baris Group `Gudang Campuran {runId}` dengan Total Asset `5`
44. Verifikasi tabel Item memuat Item `Office Desk` dengan Quantity `3`
45. Verifikasi tabel Item memuat Item `Laptop` dengan Quantity `2` sehingga lima aset Laptop yang ditolak tidak ikut kembali
46. Verifikasi `Alert` Danger di atas form memuat alasan `Photo is missing` dengan jumlah aset `3`
47. Verifikasi `Alert` Danger itu memuat alasan `Quantity is wrong` dengan jumlah aset `2`
48. Verifikasi Item `Office Desk` berada sebelum Item `Laptop` pada tabel Item, mengikuti urutan Item pada pengajuan asal
49. Verifikasi `Remaining Quota` pada form bertambah `10` dari nilai yang dicatat sebelum keputusan
50. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes

### Submit batch kembalian oleh role lain tidak mengubah Owner
51. Ketik Search `{runId}`, tekan Enter
52. Klik ikon `Edit` pada baris Group `Gudang Campuran {runId}` dengan Total Asset `5`
53. Klik `[Submit]`
54. Klik `[Submit for Approval]`
55. Klik sub tab `Waiting for Approval`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi baris pengajuan Group `Gudang Campuran {runId}` dengan Total Asset `5` tampil di sub tab `Waiting for Approval`
58. Verifikasi baris pengajuan itu memiliki Requested By `Hadi K`, sehingga Owner batch kembalian tidak berubah oleh Submit Budi S
