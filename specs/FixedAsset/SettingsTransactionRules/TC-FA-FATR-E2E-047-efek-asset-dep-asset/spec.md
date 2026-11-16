---
id: TC-FA-FATR-E2E-047-efek-asset-dep-asset
title: "Override dan aturan transaksi mengikuti perubahan aset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r246", "§4.1#r247", "§9.2#b122", "§9.2#b124", "§9.2#b141", "§9.2#b147", "§9.4.2#r34", "§9.7#r7", "§9.7#r14", "§9.7#r17", "§9.7#r30", "§11#r14", "EB-XM-2@asset-detail"]
smoke: []
dependsOn:
  - "Asset: Asset Detail dan penghapusan aset"
trace:
  "§4.1#r246": 40
  "§4.1#r247": [41, 42]
  "§9.2#b122": 37
  "§9.2#b124": 40
  "§9.2#b141": [11, 15]
  "§9.2#b147": 37
  "§9.4.2#r34": [37, 41]
  "§9.7#r7": 32
  "§9.7#r14": [11, 15]
  "§9.7#r17": [21, 26]
  "§9.7#r30": [45, 47]
  "§11#r14": [11, 12]
  "EB-XM-2@asset-detail": [11, 12, 21, 22, 32]
anchor: [3, 4, 25]
coverage:
  web: automated
---

# Override dan aturan transaksi mengikuti perubahan aset

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan akses penuh ke Asset.
- Layar awal: Fixed Asset > Asset List
- Data:
  - DU-047-1: Group Name `Yard Operations {runId}`; Group tanpa Division.
  - DU-047-2: Category Name `Heavy Machinery {runId}`, Max duration `14 Days`; Category leaf dengan Max duration Borrow nilai sendiri.
  - DU-047-3: Asset Name `Skid Steer SS60 {runId}`, Category `Heavy Machinery {runId}`, Group `Yard Operations {runId}`, Status `Available`; aset tanpa override yang dipakai siklus override.
  - DU-047-4: Asset Name `Hydraulic Excavator HX210 {runId}`, Category `Heavy Machinery {runId}`, Group `Yard Operations {runId}`, Status `Available`; aset yang dihapus sesudah punya override.
  - DU-047-5: Asset Name `Scissor Lift SL30 {runId}`, Category `Heavy Machinery {runId}`, Group `Yard Operations {runId}`, Status `Waiting for Approval`; aset dengan pengajuan yang sudah melewati batas Transaction timeout.
  - DU-047-6: Override Target `Hydraulic Excavator HX210 {runId}`, Scope `Asset`, Category `Heavy Machinery {runId}`, Transaction `Borrow`, Max duration `10 Days`; override Asset untuk aset yang akan dihapus.
  - DU-047-7: Override Target `Scissor Lift SL30 {runId}`, Scope `Asset`, Category `Heavy Machinery {runId}`, Transaction `Borrow`, Max duration `10 Days`; override Asset untuk aset yang tetap ada.
  - DU-047-8: Borrow Asset `Scissor Lift SL30 {runId}`, Status `Waiting for Approval`, Diajukan `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.

## Test Steps
### Override aktif memberi penanda di halaman detail aset dan filter di Asset List
1. Ketik Search `Skid Steer SS60 {runId}`, tekan Enter
2. Buka halaman detail aset `Skid Steer SS60 {runId}`
3. Verifikasi Transaction rules aset `Skid Steer SS60 {runId}` menampilkan Max duration `14` dari Category `Heavy Machinery {runId}`
4. Verifikasi header halaman detail aset aset `Skid Steer SS60 {runId}` tidak memuat penanda override
5. Buka tab `Borrow` pada node Category `Heavy Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
6. Klik `[+ Override]` pada bagian Overrides
7. Isi Scope `Asset` dengan Target `Skid Steer SS60 {runId}`
8. Pilih Field `Max duration` dengan Value `10`
9. Klik `[Submit]`
10. Buka halaman detail aset `Skid Steer SS60 {runId}`
11. Verifikasi penanda override aktif tampil di header halaman detail aset aset `Skid Steer SS60 {runId}`
12. Verifikasi Transaction rules aset `Skid Steer SS60 {runId}` menampilkan Max duration `10` dari override
13. Buka Asset List
14. Terapkan filter aset yang terkena override aktif
15. Verifikasi aset `Skid Steer SS60 {runId}` tampil pada hasil filter override aktif

### Penghapusan override menghilangkan penanda di halaman detail aset dan Asset List
16. Buka tab `Borrow` pada node Category `Heavy Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
17. Buka menu ⋯ pada baris override untuk `Skid Steer SS60 {runId}`
18. Klik `Delete`
19. Klik `[Delete]` pada dialog Delete Override
20. Buka halaman detail aset `Skid Steer SS60 {runId}`
21. Verifikasi penanda override tidak tampil lagi di header halaman detail aset aset `Skid Steer SS60 {runId}`
22. Verifikasi Transaction rules aset `Skid Steer SS60 {runId}` kembali menampilkan Max duration `14` dari Category `Heavy Machinery {runId}`
23. Buka Asset List
24. Terapkan filter aset yang terkena override aktif
25. Verifikasi aset `Hydraulic Excavator HX210 {runId}` tampil pada hasil filter override aktif
26. Verifikasi aset `Skid Steer SS60 {runId}` tidak tampil pada hasil filter override aktif

### Perubahan nilai Category tercermin di Transaction rules per aset
27. Buka tab `Borrow` pada node Category `Heavy Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
28. Isi Max duration dengan `21`
29. Klik `[Save]`
30. Klik `[Save]` pada dialog Save Changes
31. Buka halaman detail aset `Skid Steer SS60 {runId}`
32. Verifikasi Transaction rules aset `Skid Steer SS60 {runId}` menampilkan Max duration `21` dari Category `Heavy Machinery {runId}`

### Override tetap tampil dan tidak berlaku sesudah aset dihapus
33. Ketik Search `Hydraulic Excavator HX210 {runId}`, tekan Enter
34. Buka halaman detail aset `Hydraulic Excavator HX210 {runId}`
35. Hapus aset `Hydraulic Excavator HX210 {runId}` dari halaman detail aset
36. Buka tab `Borrow` pada node Category `Heavy Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
37. Verifikasi override untuk target `Hydraulic Excavator HX210 {runId}` tetap tersimpan dan tampil di tabel Overrides
38. Klik header kolom Actions pada tabel Overrides
39. Centang kolom `Category`
40. Verifikasi nama terakhir target `Hydraulic Excavator HX210 {runId}` dan Category `Heavy Machinery {runId}` tetap tampil pada baris override itu
41. Verifikasi `Not applied` tampil pada sel Target baris override untuk `Hydraulic Excavator HX210 {runId}`
42. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target

### Transaction timeout memulihkan status aset di Asset List dan halaman detail aset
43. Job Transaction timeout berjalan
44. Ketik Search `Scissor Lift SL30 {runId}`, tekan Enter
45. Verifikasi status aset `Scissor Lift SL30 {runId}` di Asset List adalah `Available`
46. Buka halaman detail aset `Scissor Lift SL30 {runId}`
47. Verifikasi status aset `Scissor Lift SL30 {runId}` di halaman detail aset adalah `Available`
