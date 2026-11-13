---
id: TC-FA-FAREG-E2E-040-draft-sort
title: "Sub tab Draft: urutan default dan hasil sort"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§5#r4", "§9.5#r4", "EB-SRT-3@tabel-draft", "EB-SRT-1"]
smoke: ["EB-SRT-1"]
dependsOn: []
trace:
  "§4.1#r22": [5, 7]
  "§4.1#r23": [11, 13]
  "§4.1#r24": [15, 17]
  "§4.1#r25": [19, 21]
  "§4.1#r26": [23, 25]
  "§4.1#r27": [27, 29, 3]
  "§5#r4": [3]
  "§9.5#r4": [3]
  "EB-SRT-3@tabel-draft": [9]
  "EB-SRT-1": [5, 15, 27]
anchor: [2]
coverage:
  web: automated
---

# Sub tab Draft: urutan default dan hasil sort

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-040-1: Batch Draft dengan Group `Gudang Mawar {runId}`, Origin `—`, Total Asset `12`, Progress `60%`, Requested By `Siti N`, Last Updated `T0 − 1 hari`.
  - DU-040-2: Batch Draft dengan Group `Gudang Anggrek {runId}`, Origin `REG-20261105-04002`, Total Asset `5`, Progress `100%`, Requested By `Agus P`, Last Updated `T0 − 2 hari`.
  - DU-040-3: Batch Draft dengan Group `Gudang Melati {runId}`, Origin `REG-20261103-04001`, Total Asset `30`, Progress `0%`, Requested By `Budi S`, Last Updated `T0 − 3 hari`.
  - DU-040-4: Batch Draft dengan Group `Gudang Cempaka {runId}`, Origin `REG-20261104-04003`, Total Asset `12`, Progress `40%`, Requested By `Rina W`, Last Updated `T0 − 4 hari`.
  - Siti N, Agus P, Budi S, dan Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.

## Test Steps

### Urutan default Last Updated terbaru di atas
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Draft memuat keempat baris data uji: `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`, `Gudang Melati {runId}`, `Gudang Cempaka {runId}`
3. Verifikasi urutan baris dari atas ke bawah: `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`, `Gudang Melati {runId}`, `Gudang Cempaka {runId}` (Last Updated terbaru di atas)

### Sort kolom Group dan kembali ke urutan default
4. Klik ikon sort pada header kolom `Group`
5. Verifikasi urutan baris kolom `Group` naik: `Gudang Anggrek {runId}`, `Gudang Cempaka {runId}`, `Gudang Mawar {runId}`, `Gudang Melati {runId}`
6. Klik ikon sort pada header kolom `Group` sekali lagi
7. Verifikasi urutan baris kolom `Group` turun: `Gudang Melati {runId}`, `Gudang Mawar {runId}`, `Gudang Cempaka {runId}`, `Gudang Anggrek {runId}`
8. Klik ikon sort pada header kolom `Group` untuk ketiga kalinya
9. Verifikasi urutan baris kembali ke urutan default: `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`, `Gudang Melati {runId}`, `Gudang Cempaka {runId}`

### Sort kolom Origin dengan nilai kosong
10. Klik ikon sort pada header kolom `Origin`
11. Verifikasi urutan baris kolom `Origin` naik: `Gudang Melati {runId}`, `Gudang Cempaka {runId}`, `Gudang Anggrek {runId}`, `Gudang Mawar {runId}` dengan Origin `—` di akhir
12. Klik ikon sort pada header kolom `Origin` sekali lagi
13. Verifikasi urutan baris kolom `Origin` turun: `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`, `Gudang Cempaka {runId}`, `Gudang Melati {runId}` dengan Origin `—` di awal

### Sort kolom Total Asset secara numerik
14. Klik ikon sort pada header kolom `Total Asset`
15. Verifikasi urutan baris kolom `Total Asset` naik: `Gudang Anggrek {runId}`, `Gudang Mawar {runId}`, `Gudang Cempaka {runId}`, `Gudang Melati {runId}`; baris `Gudang Mawar {runId}` dan `Gudang Cempaka {runId}` yang sama-sama bernilai `12` berurutan menurut Last Updated terbaru di atas
16. Klik ikon sort pada header kolom `Total Asset` sekali lagi
17. Verifikasi urutan baris kolom `Total Asset` turun: `Gudang Melati {runId}`, `Gudang Mawar {runId}`, `Gudang Cempaka {runId}`, `Gudang Anggrek {runId}`; baris `Gudang Mawar {runId}` dan `Gudang Cempaka {runId}` yang sama-sama bernilai `12` tetap berurutan menurut Last Updated terbaru di atas

### Sort kolom Progress secara numerik
18. Klik ikon sort pada header kolom `Progress`
19. Verifikasi urutan baris kolom `Progress` naik: `Gudang Melati {runId}`, `Gudang Cempaka {runId}`, `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`
20. Klik ikon sort pada header kolom `Progress` sekali lagi
21. Verifikasi urutan baris kolom `Progress` turun: `Gudang Anggrek {runId}`, `Gudang Mawar {runId}`, `Gudang Cempaka {runId}`, `Gudang Melati {runId}`

### Sort kolom Requested By
22. Klik ikon sort pada header kolom `Requested By`
23. Verifikasi urutan baris kolom `Requested By` naik: `Gudang Anggrek {runId}`, `Gudang Melati {runId}`, `Gudang Cempaka {runId}`, `Gudang Mawar {runId}`
24. Klik ikon sort pada header kolom `Requested By` sekali lagi
25. Verifikasi urutan baris kolom `Requested By` turun: `Gudang Mawar {runId}`, `Gudang Cempaka {runId}`, `Gudang Melati {runId}`, `Gudang Anggrek {runId}`

### Sort kolom Last Updated
26. Klik ikon sort pada header kolom `Last Updated`
27. Verifikasi urutan baris kolom `Last Updated` naik: `Gudang Cempaka {runId}`, `Gudang Melati {runId}`, `Gudang Anggrek {runId}`, `Gudang Mawar {runId}` (Oldest First)
28. Klik ikon sort pada header kolom `Last Updated` sekali lagi
29. Verifikasi urutan baris kolom `Last Updated` turun: `Gudang Mawar {runId}`, `Gudang Anggrek {runId}`, `Gudang Melati {runId}`, `Gudang Cempaka {runId}` (Newest First)
