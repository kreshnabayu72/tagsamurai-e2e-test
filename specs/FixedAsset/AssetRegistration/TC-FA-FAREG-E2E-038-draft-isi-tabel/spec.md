---
id: TC-FA-FAREG-E2E-038-draft-isi-tabel
title: "Sub tab Draft: isi tabel dari data batch dan aksi baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-11e", "FAREG-LOGIC-20b", "§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§4.1#p6"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-11e": [8, 9]
  "FAREG-LOGIC-20b": [14]
  "§4.1#r22": [2, 4, 14]
  "§4.1#r23": [5, 6]
  "§4.1#r24": [3, 7]
  "§4.1#r25": [8, 9]
  "§4.1#r26": [10]
  "§4.1#r27": [11]
  "§4.1#p6": [12, 17, 20, 23, 25]
coverage:
  web: automated
---

# Sub tab Draft: isi tabel dari data batch dan aksi baris

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-038-1: Batch Draft dengan Group `Gudang Menteng {runId}`, Origin `—`, Total Asset `12`, tanpa aset Ready sehingga Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`.
  - DU-038-2: Batch Draft dengan Group `Gudang Salemba {runId}`, Origin `REG-20261105-03801`, Total Asset `5`, dengan 3 aset Ready sehingga Progress `60%`, Requested By `Siti N.`, Last Updated `T0 − 2 hari`.
  - DU-038-3: Batch Draft dengan Group `Kantor Sudirman {runId}`, Origin `—`, Total Asset `30`, seluruh aset Ready sehingga Progress `100%`, Requested By `Agus P`, Last Updated `T0 − 3 hari`.
  - Rina W, Siti N, dan Agus P adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam.

## Test Steps

### Nilai sel tabel Draft sesuai data batch
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Draft memuat baris `Gudang Menteng {runId}`, `Gudang Salemba {runId}`, dan `Kantor Sudirman {runId}`
3. Verifikasi Total Asset baris `Gudang Menteng {runId}` bernilai `12`
4. Verifikasi Group pada baris `Gudang Salemba {runId}` tampil sebagai `Gudang Salemba {runId}`
5. Verifikasi Origin baris `Gudang Salemba {runId}` bernilai `REG-20261105-03801`
6. Verifikasi Origin baris `Gudang Menteng {runId}` bernilai `—`
7. Verifikasi Total Asset baris `Kantor Sudirman {runId}` bernilai `30`
8. Verifikasi Progress baris `Gudang Salemba {runId}` bernilai `60%` dari 3 aset Ready di antara 5 aset
9. Verifikasi Progress baris `Gudang Menteng {runId}` bernilai `0%` dan Progress baris `Kantor Sudirman {runId}` bernilai `100%`
10. Verifikasi Requested By baris `Gudang Salemba {runId}` bernilai `Siti N.`[^drift-1]
11. Verifikasi Last Updated baris `Gudang Salemba {runId}` tampil dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Ikon aksi pada baris
12. Verifikasi baris `Gudang Menteng {runId}` menampilkan ikon aksi `Edit`, `Registration Log`, dan `Delete`

### Klik Group membuka form Edit
13. Klik Group `Gudang Salemba {runId}` pada baris tabel Draft
14. Verifikasi form `Register Asset` terbuka dalam mode Edit untuk batch `Gudang Salemba {runId}`
15. Klik `[Cancel]` pada form yang belum diubah

### Aksi baris Edit
16. Klik ikon `Edit` pada baris `Gudang Menteng {runId}`
17. Verifikasi form `Register Asset` terbuka untuk batch `Gudang Menteng {runId}`
18. Klik `[Cancel]` pada form yang belum diubah

### Aksi baris Registration Log
19. Klik ikon `Registration Log` pada baris `Gudang Menteng {runId}`
20. Verifikasi dialog `Registration Log` tampil
21. Klik ikon X pada dialog `Registration Log`

### Aksi baris Delete
22. Klik ikon `Delete` pada baris `Gudang Menteng {runId}`
23. Verifikasi dialog `Delete Draft` tampil
24. Klik `[Cancel]` pada dialog `Delete Draft`

### Kolom Actions berada paling akhir
25. Verifikasi kolom `Actions` adalah kolom terakhir tabel sub tab Draft, sesudah kolom `Last Updated`

[^drift-1]: Drift PRD vs foundation vs override. PRD §4.1 kolom Requested By: `Nama singkat`. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).
