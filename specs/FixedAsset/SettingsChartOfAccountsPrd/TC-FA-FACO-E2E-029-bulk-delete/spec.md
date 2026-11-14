---
id: TC-FA-FACO-E2E-029-bulk-delete
title: "Bulk Delete akun yang seluruhnya lolos guard"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-08", "F-FACO-05", "EB-EDG-2", "T-06"]
smoke: ["T-06"]
dependsOn: []
trace:
  "D-08": [9, 23, 35]
  "F-FACO-05": [13, 25, 37]
  "EB-EDG-2": 10
  "T-06": 12
anchor: [5, 18, 30]
coverage:
  web: automated
---

# Bulk Delete akun yang seluruhnya lolos guard

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-029-1: akun Active dengan Account Code `HS-{runId}`, Account Name `Prepaid Equipment Kantor Cabang {runId}`, Account Function `Asset Cost`, Used By `0`, Last Used in Journal `—`; Account Label `HS-{runId} – Prepaid Equipment Kantor Cabang {runId}`.
  - DU-029-2: akun Active dengan Account Code `HB1-{runId}`, Account Name `Accumulated Depreciation Gudang {runId}`, Account Function `Accumulated Depreciation`, Used By `0`, Last Used in Journal `—`; Account Label `HB1-{runId} – Accumulated Depreciation Gudang {runId}`.
  - DU-029-3: akun Active dengan Account Code `HB2-{runId}`, Account Name `Accumulated Depreciation Workshop {runId}`, Account Function `Accumulated Depreciation`, Used By `0`, Last Used in Journal `—`; Account Label `HB2-{runId} – Accumulated Depreciation Workshop {runId}`.
  - DU-029-4: akun Active dengan Account Code `HB3-{runId}`, Account Name `Accumulated Depreciation Showroom {runId}`, Account Function `Accumulated Depreciation`, Used By `0`, Last Used in Journal `—`; Account Label `HB3-{runId} – Accumulated Depreciation Showroom {runId}`.
  - DU-029-5: 12 akun Active dengan Account Code `HV{n}-{runId}`, Account Name `Depreciation Expense Cabang Pusat Distribusi Nasional Wilayah Jawa Barat Unit {n} {runId}`, `{n}` dari 1 sampai 12, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - Seluruh akun di atas belum pernah diekspor dan bukan nilai default company, sehingga lolos kedua guard Delete.

## Test Steps

### Bulk Delete satu akun memakai bentuk dialog tunggal
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon Filter pada toolbar
3. Pilih Function `Asset Cost` pada Filter Panel
4. Klik `[Apply]`
5. Verifikasi baris `HS-{runId}` tampil pada tabel
6. Centang baris `HS-{runId}`
7. Klik `Bulk Action`
8. Klik `Delete`
9. Verifikasi dialog memuat bullet `HS-{runId} – Prepaid Equipment Kantor Cabang {runId}`
10. Verifikasi dialog memakai bentuk tunggal: judul `Delete Account` dan kalimat penutup `This action cannot be undone. Are you sure you want to delete it?`
11. Klik `[Delete]`
12. Verifikasi toast `Success, account has been deleted.` tampil
13. Verifikasi baris `HS-{runId}` tidak tampil, dengan empty state `No results found` pada tabel

### Bulk Delete beberapa akun
14. Klik ikon Filter pada toolbar
15. Klik `[Clear Field]`
16. Pilih Function `Accumulated Depreciation` pada Filter Panel
17. Klik `[Apply]`
18. Verifikasi baris `HB1-{runId}`, `HB2-{runId}`, dan `HB3-{runId}` tampil
19. Centang baris `HB1-{runId}`
20. Klik `Select All (3 records)`
21. Klik `Bulk Action`
22. Klik `Delete`
23. Verifikasi dialog memuat bullet `HB1-{runId} – Accumulated Depreciation Gudang {runId}`, `HB2-{runId} – Accumulated Depreciation Workshop {runId}`, dan `HB3-{runId} – Accumulated Depreciation Showroom {runId}`
24. Klik `[Delete]`
25. Verifikasi baris `HB1-{runId}`, `HB2-{runId}`, dan `HB3-{runId}` tidak tampil, dengan empty state `No results found` pada tabel

### Daftar dialog yang melebihi tampilan tetap memuat seluruh akun
26. Klik ikon Filter pada toolbar
27. Klik `[Clear Field]`
28. Pilih Function `Depreciation Expense` pada Filter Panel
29. Klik `[Apply]`
30. Verifikasi baris `HV1-{runId}` tampil pada tabel
31. Centang baris `HV1-{runId}`
32. Klik `Select All (12 records)`
33. Klik `Bulk Action`
34. Klik `Delete`
35. Verifikasi dialog Delete memuat 12 bullet dan seluruhnya dapat dijangkau pada daftar yang bergulir
36. Klik `[Delete]`
37. Verifikasi baris `HV1-{runId}` sampai `HV12-{runId}` tidak tampil, dengan empty state `No results found` pada tabel
