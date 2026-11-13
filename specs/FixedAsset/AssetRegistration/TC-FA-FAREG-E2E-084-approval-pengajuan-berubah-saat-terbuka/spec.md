---
id: TC-FA-FAREG-E2E-084-approval-pengajuan-berubah-saat-terbuka
title: "Halaman Approval: pengajuan dibatalkan atau diputuskan pihak lain saat terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.2.4#b12", "§9.4.2#r15", "§9.4.2#r16", D-REG-19]
smoke: [D-REG-19]
dependsOn: []
trace:
  "§4.2.4#b12": [6, 7, 9, 16, 18]
  "§9.4.2#r15": [6, 9, 12, 39]
  "§9.4.2#r16": [16, 21, 26]
  D-REG-19: [6, 16]
anchor: [11, 20]
coverage:
  web: automated
---
# Halaman Approval: pengajuan dibatalkan atau diputuskan pihak lain saat terbuka

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Berubah {runId}`, approver). Rina W (Manage asset & TAG) membatalkan pengajuan sebagai pemicu. Dewi A (Group Manager yang menaungi Group `Gudang Berubah {runId}`) memutuskan pengajuan sebagai pemicu.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-084-1: Group `Gudang Berubah {runId}`, ada di entitas aktor.
  - DU-084-2: pengajuan Waiting for Approval pertama di Group `Gudang Berubah {runId}`, diajukan Rina W, Total Asset `3`.
  - DU-084-3: pengajuan Waiting for Approval kedua di Group `Gudang Berubah {runId}`, diajukan Rina W, Total Asset `4`.
  - DU-084-4: pengajuan Waiting for Approval pembanding di Group `Gudang Berubah {runId}`, diajukan Rina W, Total Asset `5`.
  - DU-084-5: Item pengajuan pertama: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `3`, Condition `Normal`, TAG Type `Non-TAG`.
  - DU-084-6: Item pengajuan kedua: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `4`, Condition `Normal`, TAG Type `Non-TAG`.
  - DU-084-7: Item pengajuan pembanding: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `5`, Condition `Normal`, TAG Type `Non-TAG`.
  - DU-084-8: Budi S (Manage asset & TAG dengan capability Update pada Group `Gudang Berubah {runId}`).
  - DU-084-9: Dewi A (Group Manager yang menaungi Group `Gudang Berubah {runId}`).
  - DU-084-10: pengajuan Waiting for Approval keempat di Group `Gudang Berubah {runId}`, diajukan Rina W, Total Asset `6`.
  - DU-084-11: Item pengajuan keempat: Asset Name `Office Desk`, Brand `Kayu Jati`, Model `No Model`, Quantity `6`, Condition `Normal`, TAG Type `Non-TAG`.
  - DU-084-12: Model `Meja Kerja 120` milik Brand `Kayu Jati`, tersedia di master Model.
  - DU-084-13: koreksi yang diisi langkah: Model aset ke-1 menjadi `Meja Kerja 120`.
- Kondisi:
  - Group `Gudang Berubah {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Pengajuan dibatalkan pengaju saat halaman Approval terbuka
1. Buka menu Approvals > Registration, tab `Active`
2. Ketik Search `{runId}`, tekan Enter
3. Klik ikon `Review` pada baris pengajuan dengan Total Asset `3`
4. Ubah Decision aset ke-1 pada grup `Office Desk` menjadi `Reject`
5. Rina W membatalkan pengajuan Group `Gudang Berubah {runId}` dengan Total Asset `3`
6. Verifikasi dialog `Request Canceled` terbuka seketika dengan pesan `This request was canceled by [User]. Your decisions were not saved.`, dengan [User] berisi nama pengguna yang membatalkan, yaitu Rina W
7. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil
8. Klik `[OK]`
9. Verifikasi halaman kembali ke antrean `Approvals > Registration > Active`
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris pengajuan pembanding dengan Total Asset `5` tampil di tab `Active`
12. Verifikasi tidak ada baris pengajuan dengan Total Asset `3` di tab `Active`

### Pengajuan diputuskan approver lain saat halaman Approval terbuka
13. Klik ikon `Review` pada baris pengajuan dengan Total Asset `4`
14. Ubah Decision aset ke-1 pada grup `Office Desk` menjadi `Reject`
15. Dewi A menyetujui seluruh aset pengajuan Group `Gudang Berubah {runId}` dengan Total Asset `4`
16. Verifikasi dialog `Request Already Decided` terbuka seketika dengan pesan `This request was already decided by [User]. Your decisions were not saved.`, dengan [User] berisi nama pengguna yang memutuskan, yaitu Dewi A
17. Klik `[OK]`
18. Verifikasi halaman kembali ke antrean `Approvals > Registration > Active`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi baris pengajuan pembanding dengan Total Asset `5` tampil di tab `Active`
21. Verifikasi tidak ada baris pengajuan dengan Total Asset `4` di tab `Active`
22. Klik tab `History`
23. Ketik Search `{runId}`, tekan Enter
24. Klik ikon `Detail` pada baris pengajuan dengan Total Asset `4`
25. Klik tab `Asset`
26. Verifikasi aset ke-1 berkolom Result `Approved` sehingga keputusan `Reject` yang belum terkirim tidak diterapkan

### Koreksi staged dibuang saat pengajuan dibatalkan
27. Buka menu Approvals > Registration, tab `Active`
28. Ketik Search `{runId}`, tekan Enter
29. Klik ikon `Review` pada baris pengajuan dengan Total Asset `6`
30. Klik Name aset ke-1 pada grup `Office Desk` untuk membuka panel koreksi
31. Pilih Model `Meja Kerja 120` pada field Model panel koreksi
32. Klik `[Save correction]`
33. Rina W membatalkan pengajuan Group `Gudang Berubah {runId}` dengan Total Asset `6` dengan `Save as Draft to edit` tercentang
34. Klik `[OK]` pada dialog `Request Canceled`
35. Buka Fixed Asset > Assets > Registration, sub tab `Draft`
36. Ketik Search `{runId}`, tekan Enter
37. Klik ikon `Edit` pada baris Group `Gudang Berubah {runId}` dengan Total Asset `6`
38. Klik tab `General Information`
39. Verifikasi Item `Office Desk` pada tabel Item bermodel `No Model` dan bukan `Meja Kerja 120` sehingga koreksi staged dibuang
40. Klik `[Cancel]` pada form; form belum diubah sehingga tidak ada dialog Unsaved Changes
