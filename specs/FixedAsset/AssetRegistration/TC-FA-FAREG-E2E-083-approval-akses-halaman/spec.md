---
id: TC-FA-FAREG-E2E-083-approval-akses-halaman
title: "Halaman Approval: pengajuan sendiri, pengajuan bukan Waiting for Approval, dan keluar halaman"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [F-FAREG-06.k1, FAREG-LOGIC-06j, FAREG-LOGIC-07j, FAREG-LOGIC-20l, "§4.2.4#p1", "§4.2.4#b6", "§4.2.4#b13", "§9.4.2#r13", S-REG-13]
smoke: [S-REG-13]
dependsOn: []
trace:
  F-FAREG-06.k1: 12
  FAREG-LOGIC-06j: [4, 7, 9, 55]
  FAREG-LOGIC-07j: [29, 36, 43, 53]
  FAREG-LOGIC-20l: [22, 23]
  "§4.2.4#p1": 20
  "§4.2.4#b6": [11, 13]
  "§4.2.4#b13": [29, 43]
  "§9.4.2#r13": [11, 12, 13, 14, 58]
  S-REG-13: 16
anchor: [3, 19, 34, 51]
coverage:
  web: automated
---
# Halaman Approval: pengajuan sendiri, pengajuan bukan Waiting for Approval, dan keluar halaman

## Prerequisites
- Aktor: Hadi K (Manage asset & TAG dengan capability Update pada Group `Gudang Akses {runId}`), pengaju pengajuan DU-083-1 dan DU-083-3. Rina W (Manage asset & TAG) adalah pengaju pengajuan DU-083-2. Dewi A (Group Manager) adalah pemutus pengajuan DU-083-3.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-083-1: pengajuan Waiting for Approval di Group `Gudang Akses {runId}`, diajukan Hadi K, Total Asset `3` (Item `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`).
  - DU-083-2: pengajuan Waiting for Approval di Group `Gudang Akses {runId}`, diajukan Rina W, Total Asset `4` (Item `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `4`).
  - DU-083-3: pengajuan Approved di Group `Gudang Akses {runId}`, diajukan Hadi K dan diputuskan Dewi A, Total Asset `2` (Item `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `2`).
  - DU-083-4: Hadi K (Manage asset & TAG dengan capability Update pada Group `Gudang Akses {runId}`).
  - DU-083-5: Rina W (Manage asset & TAG, Group terkelola `Gudang Akses {runId}`).
  - DU-083-6: Dewi A (Group Manager yang menaungi Group `Gudang Akses {runId}`).
  - DU-083-7: Model `Meja Kerja 120` milik Brand `Kayu Jati`, tersedia di master Model.
  - DU-083-8: koreksi yang diisi langkah: Model aset ke-1 menjadi `Meja Kerja 120`.
- Kondisi:
  - Group `Gudang Akses {runId}` ber-toggle `Require Approval for Registration` ON.
  - Hak putus Hadi K hanya pada Group `Gudang Akses {runId}`, sehingga antrean Active Hadi K hanya memuat pengajuan Group itu.

## Test Steps

### Pengajuan sendiri tidak masuk tab Active
1. Buka menu Approvals > Registration, tab `Active`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris pengajuan Group `Gudang Akses {runId}` dengan Total Asset `4` dan Requested By `Rina W` tampil di tab `Active`
4. Verifikasi tidak ada baris pengajuan dengan Total Asset `3` milik Hadi K di tab `Active`

### Pengajuan sendiri yang sudah diputuskan tampil di History dan Detail
5. Klik tab `History`
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi baris pengajuan Group `Gudang Akses {runId}` dengan Total Asset `2`, Status `Approved`, dan Requested By `Hadi K` tampil di tab `History`
8. Klik ikon `Detail` pada baris dengan Total Asset `2`
9. Verifikasi halaman Detail pengajuan terbuka dengan Badge status `Approved`

### Halaman Approval pengajuan sendiri terkunci
10. Buka halaman Approval pengajuan dengan Total Asset `3` lewat alamat langsung (URL)
11. Verifikasi notice `You cannot decide a registration you submitted.` tampil di atas tabel aset
12. Verifikasi kontrol Decision pada seluruh aset Disabled sehingga Hadi K tidak dapat memutuskan pengajuannya sendiri
13. Verifikasi tombol `[Submit]` Disabled
14. Verifikasi row option `Edit` Disabled
15. Arahkan kursor ke tombol `[Submit]`
16. Verifikasi tooltip `You cannot decide a registration you submitted.` tampil

### Sub tab Registration tidak memiliki jalur ke halaman Approval
17. Buka Fixed Asset > Assets > Registration, sub tab `Waiting for Approval`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi baris pengajuan Total Asset `3` memiliki ikon `Detail`, `Registration Log`, dan `Cancel registration`
20. Verifikasi tidak ada ikon `Review` pada baris pengajuan Total Asset `3`

### Pengajuan yang bukan Waiting for Approval dialihkan ke Detail
21. Buka halaman Approval pengajuan dengan Total Asset `2` lewat alamat langsung (URL)
22. Verifikasi halaman Detail pengajuan terbuka dengan Badge status `Approved`
23. Verifikasi tidak ada dialog yang tampil

### Dialog Unsaved Changes hanya untuk isian yang belum dikirim
24. Buka menu Approvals > Registration, tab `Active`
25. Ketik Search `{runId}`, tekan Enter
26. Klik ikon `Review` pada baris pengajuan dengan Total Asset `4`
27. Ubah Decision aset ke-1 pada grup `Office Desk` menjadi `Reject`
28. Klik menu `Assets` pada sidebar
29. Verifikasi dialog `Unsaved Changes` tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
30. Klik `[Leave]`
31. Buka menu Approvals > Registration, tab `Active`
32. Ketik Search `{runId}`, tekan Enter
33. Klik ikon `Review` pada baris pengajuan dengan Total Asset `4`
34. Verifikasi Decision aset ke-1 pada grup `Office Desk` bernilai `Approve`
35. Klik menu `Assets` pada sidebar
36. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil

### Dialog Unsaved Changes untuk isian panel koreksi yang belum disimpan
37. Buka menu Approvals > Registration, tab `Active`
38. Ketik Search `{runId}`, tekan Enter
39. Klik ikon `Review` pada baris pengajuan dengan Total Asset `4`
40. Klik Name aset ke-1 pada grup `Office Desk` untuk membuka panel koreksi
41. Pilih Model `Meja Kerja 120` pada field Model panel koreksi
42. Klik menu `Assets` pada sidebar
43. Verifikasi dialog `Unsaved Changes` tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
44. Klik `[Leave]`

### Koreksi yang sudah disimpan staged tidak memicu dialog saat keluar
45. Buka menu Approvals > Registration, tab `Active`
46. Ketik Search `{runId}`, tekan Enter
47. Klik ikon `Review` pada baris pengajuan dengan Total Asset `4`
48. Klik Name aset ke-1 pada grup `Office Desk` untuk membuka panel koreksi
49. Pilih Model `Meja Kerja 120` pada field Model panel koreksi
50. Klik `[Save correction]`
51. Verifikasi toast `Success, correction has been saved.` tampil sebagai bukti koreksi tersimpan staged
52. Klik menu `Assets` pada sidebar
53. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil

### Hitungan tab Active tidak memuat pengajuan sendiri
54. Buka menu Approvals > Registration, tab `Active`
55. Verifikasi angka N pada tab `Active (N)` bernilai 1 karena hanya menghitung pengajuan Rina W dengan Total Asset `4`, bukan pengajuan Hadi K dengan Total Asset `3`

### Bulk Action Disabled pada halaman terkunci
56. Buka halaman Approval pengajuan dengan Total Asset `3` lewat alamat langsung (URL)
57. Centang aset ke-1 pada grup `Office Desk`
58. Verifikasi Bulk Action (trigger) pada grup `Office Desk` Disabled
