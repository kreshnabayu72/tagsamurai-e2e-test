---
id: TC-FA-FATR-E2E-022-changelog-sort
title: "Sort tabel Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r398", "§4.1#r399", "§4.1#r402", "§4.1#r403", "§4.1#r400", "§4.1#r401", "§4.1#r404", "§5#r4", "§9.5#r9", "EB-SRT-3@changelog"]
smoke: ["EB-SRT-3@changelog"]
dependsOn: []
trace:
  "§4.1#r398": [3, 7, 9]
  "§4.1#r399": 50
  "§4.1#r402": [30, 32]
  "§4.1#r403": [37, 39]
  "§4.1#r400": [14, 16]
  "§4.1#r401": [21, 23]
  "§4.1#r404": [44, 46]
  "§5#r4": 3
  "§9.5#r9": 3
  "EB-SRT-3@changelog": 25
anchor: [2, 12, 19, 28, 35, 42]
coverage:
  web: automated
---
# Sort tabel Changelog

## Prerequisites
- Aktor: Total Control `Rina Wulandari`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, DU-022-7. Changelog entitas ini hanya memuat DU-022-1 sampai DU-022-6, dibuat berurutan dari DU-022-1 paling awal sampai DU-022-6 paling akhir.
  - DU-022-1: Changelog Category `Alat Berat {runId} > Ekskavator {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `7 days`, Action `Edit`, Modified By `Rina W`, dari Name `Rina Wulandari`.
  - DU-022-2: Changelog Category `Kendaraan {runId} > Truk {runId}`, Field `Transfer (In-transit overdue after)`, Old Value `3 days`, New Value `5 days`, Action `Edit`, Modified By `Budi S`, dari Name `Budi Santoso`.
  - DU-022-3: Changelog Category `Elektronik {runId} > Laptop {runId}`, Field `Transfer (Approval type)`, Old Value `Any one approver`, New Value `All approvers (AND)`, Action `Edit`, Modified By `Citra D`, dari Name `Citra Dewi`.
  - DU-022-4: Changelog Category `Kendaraan {runId} > Mobil {runId}`, Field `Borrow (Allow Borrow)`, Old Value `Allow`, New Value `Deny`, Action `Edit`, Modified By `Dimas P`, dari Name `Dimas Pratama`.
  - DU-022-5: Changelog Category `All categories`, Field `Damaged & Missing (Long missing after)`, Old Value `45 days`, New Value `Off`, Action `Edit`, Modified By `Eko W`, dari Name `Eko Wibowo`.
  - DU-022-6: Changelog Category `Alat Berat {runId} > Buldoser {runId}`, Field `Borrow (Max extensions)`, Old Value `No extension`, New Value `2`, Action `Edit`, Modified By `Fajar N`, dari Name `Fajar Nugroho`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Urutan awal Changelog adalah Date Newest First
1. Klik ikon Changelog di header
2. Verifikasi tabel memuat keenam entri data uji
3. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Transfer (In-transit overdue after)`, `Borrow (Max duration)`
4. Klik `✕` pada dialog Changelog

### Sort kolom Date mengikuti Oldest First lalu Newest First
5. Klik ikon Changelog di header
6. Klik header kolom Date
7. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max duration)`, `Transfer (In-transit overdue after)`, `Transfer (Approval type)`, `Borrow (Allow Borrow)`, `Damaged & Missing (Long missing after)`, `Borrow (Max extensions)` sebagai Oldest First
8. Klik header kolom Date
9. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Transfer (In-transit overdue after)`, `Borrow (Max duration)` sebagai Newest First
10. Klik `✕` pada dialog Changelog

### Sort kolom Category ascending dan descending
11. Klik ikon Changelog di header
12. Verifikasi tabel memuat keenam entri data uji
13. Klik header kolom Category
14. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Borrow (Max duration)`, `Damaged & Missing (Long missing after)`, `Transfer (Approval type)`, `Borrow (Allow Borrow)`, `Transfer (In-transit overdue after)` secara ascending
15. Klik header kolom Category
16. Verifikasi urutan baris dari atas ke bawah menurut Field: `Transfer (In-transit overdue after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Damaged & Missing (Long missing after)`, `Borrow (Max duration)`, `Borrow (Max extensions)` secara descending
17. Klik `✕` pada dialog Changelog

### Sort kolom Field ascending dan descending
18. Klik ikon Changelog di header
19. Verifikasi tabel memuat keenam entri data uji
20. Klik header kolom Field
21. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Allow Borrow)`, `Borrow (Max duration)`, `Borrow (Max extensions)`, `Damaged & Missing (Long missing after)`, `Transfer (Approval type)`, `Transfer (In-transit overdue after)` secara ascending
22. Klik header kolom Field
23. Verifikasi urutan baris dari atas ke bawah menurut Field: `Transfer (In-transit overdue after)`, `Transfer (Approval type)`, `Damaged & Missing (Long missing after)`, `Borrow (Max extensions)`, `Borrow (Max duration)`, `Borrow (Allow Borrow)` secara descending
24. Klik header kolom Field
25. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Transfer (In-transit overdue after)`, `Borrow (Max duration)` sesudah klik ketiga kembali ke urutan default
26. Klik `✕` pada dialog Changelog

### Sort kolom Old Value ascending dan descending
27. Klik ikon Changelog di header
28. Verifikasi tabel memuat keenam entri data uji
29. Klik header kolom Old Value
30. Verifikasi urutan baris dari atas ke bawah menurut Field: `Transfer (In-transit overdue after)`, `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Borrow (Max duration)`, `Borrow (Max extensions)` secara ascending
31. Klik header kolom Old Value
32. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Borrow (Max duration)`, `Transfer (Approval type)`, `Borrow (Allow Borrow)`, `Damaged & Missing (Long missing after)`, `Transfer (In-transit overdue after)` secara descending
33. Klik `✕` pada dialog Changelog

### Sort kolom New Value ascending dan descending
34. Klik ikon Changelog di header
35. Verifikasi tabel memuat keenam entri data uji
36. Klik header kolom New Value
37. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max extensions)`, `Transfer (In-transit overdue after)`, `Borrow (Max duration)`, `Transfer (Approval type)`, `Borrow (Allow Borrow)`, `Damaged & Missing (Long missing after)` secara ascending
38. Klik header kolom New Value
39. Verifikasi urutan baris dari atas ke bawah menurut Field: `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Borrow (Max duration)`, `Transfer (In-transit overdue after)`, `Borrow (Max extensions)` secara descending
40. Klik `✕` pada dialog Changelog

### Sort kolom Modified By ascending dan descending
41. Klik ikon Changelog di header
42. Verifikasi tabel memuat keenam entri data uji
43. Klik header kolom Modified By
44. Verifikasi urutan baris dari atas ke bawah menurut Field: `Transfer (In-transit overdue after)`, `Transfer (Approval type)`, `Borrow (Allow Borrow)`, `Damaged & Missing (Long missing after)`, `Borrow (Max extensions)`, `Borrow (Max duration)` secara ascending
45. Klik header kolom Modified By
46. Verifikasi urutan baris dari atas ke bawah menurut Field: `Borrow (Max duration)`, `Borrow (Max extensions)`, `Damaged & Missing (Long missing after)`, `Borrow (Allow Borrow)`, `Transfer (Approval type)`, `Transfer (In-transit overdue after)` secara descending
47. Klik `✕` pada dialog Changelog

### Sort kolom Action pada nilai yang seragam
48. Klik ikon Changelog di header
49. Klik header kolom Action
50. Verifikasi keenam entri data uji tetap tampil dengan Action `Edit`
51. Klik `✕` pada dialog Changelog
