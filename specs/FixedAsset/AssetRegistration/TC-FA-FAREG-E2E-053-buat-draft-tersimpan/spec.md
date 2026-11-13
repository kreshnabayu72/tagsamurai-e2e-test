---
id: TC-FA-FAREG-E2E-053-buat-draft-tersimpan
title: "Register Asset: Save draft pertama membentuk batch Draft"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-01a, FAREG-LOGIC-01b, FAREG-LOGIC-03a, FAREG-LOGIC-03c, FAREG-LOGIC-03l, FAREG-LOGIC-10a, §4.4#r1, §4.4#r2, §4.4#r4, §9.4.2#r1, §9.7#r1, EB-FRM-1@form-register-asset, FAREG-LOGIC-01c, T-REG-01]
smoke: [FAREG-LOGIC-01c, T-REG-01]
dependsOn: []
trace:
  FAREG-LOGIC-01a: 22
  FAREG-LOGIC-01b: [14, 15]
  FAREG-LOGIC-03a: 19
  FAREG-LOGIC-03c: 15
  FAREG-LOGIC-03l: [14, 15]
  FAREG-LOGIC-10a: 25
  §4.4#r1: [17, 19]
  §4.4#r2: [8, 15]
  §4.4#r4: 15
  §9.4.2#r1: [19, 24]
  §9.7#r1: [22, 27, 28]
  EB-FRM-1@form-register-asset: [23, 27]
  FAREG-LOGIC-01c: 18
  T-REG-01: 17
anchor: []
coverage:
  web: automated
---

# Register Asset: Save draft pertama membentuk batch Draft

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Cabang {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-053-1: Group `Gudang Cabang {runId}`, node Assignable dan bukan Excess, belum memiliki batch Draft.
  - DU-053-2: Master Asset Name `Laptop`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`.
  - DU-053-3: Master Asset Name `Office Desk`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`.

## Test Steps

### Item dan aset terbentuk di Tab Asset
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Cabang {runId}`
3. Pilih Asset Name `Laptop` pada Item 1
4. Pilih Brand `Dell` pada Item 1
5. Pilih Model `Latitude 5440` pada Item 1
6. Isi Quantity Item 1 dengan `3`
7. Klik `[+ Asset Name]`
8. Verifikasi tabel Item memuat Item 2 baru yang belum memiliki Asset Name
9. Isi Quantity Item 2 dengan `2`, tanpa memilih Asset Name
10. Pilih Asset Name `Office Desk` pada Item 2
11. Pilih Brand `Kayu Jati` pada Item 2
12. Pilih Model `No Model` pada Item 2
13. Klik tab `Asset`
14. Verifikasi Item 1 memuat tiga aset terpisah, sebanyak Quantity `3`, setelah Asset Name `Laptop` dipilih
15. Verifikasi Item 2 yang ditambahkan lewat `[+ Asset Name]` dan Quantity `2`-nya sudah diisi sebelum Asset Name `Office Desk` dipilih, memuat dua aset sebanyak Quantity itu dengan Name sementara berformat `Office Desk`, tanda hubung, lalu nomor increment

### Save draft pertama membentuk batch Draft
16. Klik `[Save draft]` dua kali berturut-turut
17. Verifikasi toast `Success, draft has been saved.` tampil
18. Verifikasi judul Item 1 memuat badge `Incomplete` karena field Tingkat 2 aset belum terisi, walau Save draft berhasil
19. Verifikasi Name ketiga aset Item 1 berformat `Laptop`, tanda hubung, lalu nomor increment yang berurutan naik satu demi satu
20. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)

### Batch Draft tampil di sub tab Draft dan tercatat di Registration Log
21. Ketik Search `Gudang Cabang {runId}`, tekan Enter
22. Verifikasi baris Group `Gudang Cabang {runId}` tampil di sub tab Draft
23. Verifikasi hanya satu baris yang cocok dengan Search itu, yaitu satu batch Draft walau `[Save draft]` diklik dua kali
24. Verifikasi Total Asset batch `5`
25. Verifikasi Requested By batch `Rina W`, pembuat draft
26. Klik row action `Registration Log` pada baris
27. Verifikasi timeline memuat node `Draft created by Rina W` satu kali
28. Verifikasi node `Draft created by Rina W` memuat Total Asset `5`
