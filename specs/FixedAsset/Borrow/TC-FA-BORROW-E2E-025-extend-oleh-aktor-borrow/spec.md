---
id: TC-FA-BORROW-E2E-025-extend-oleh-aktor-borrow
title: "Aktor Borrow mengajukan Extend per baris dan hasilnya berlaku langsung atau masuk pengajuan approval"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-187", "FI-BRW-188", "FI-BRW-189", "§4.4#r13"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-187": 15
  "FI-BRW-188": [31, 47]
  "FI-BRW-189": [14, 16, 30, 46]
  "§4.4#r13": [7, 8]
anchor: []
coverage:
  web: automated
---

# Aktor Borrow mengajukan Extend per baris dan hasilnya berlaku langsung atau masuk pengajuan approval

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-025-1: BRW Group `Head Office`, Borrower `Maya Sari {runId}`, berisi baris `Borrowed` aset DU-025-2, DU-025-3, dan DU-025-4.
  - DU-025-2: aset `Laptop Dell XPS {runId}`, Due date T0 + 1 hari, Approval Extend `Auto-approve`; Extend By `1`, Reason `Proyek belum selesai`; Due date baru T0 + 2 hari (dari Due date saat ini T0 + 1 hari ditambah Extend By 1 hari).
  - DU-025-3: aset `Proyektor Epson {runId}`, Due date T0 + 1 hari, Approval Extend `Needs approval`; Extend By `2`, Reason `Menunggu persetujuan klien`; New Due Date pengajuan T0 + 3 hari.
  - DU-025-4: aset `Kamera Nikon {runId}`, Due date T0 + 1 hari, dengan pengajuan Extension yang masih menunggu approval sehingga baris Extend-nya nonaktif.
  - DU-025-5: BRW Group `Head Office`, Borrower `Nanda Putra {runId}`, berisi baris `Borrowed` aset DU-025-6.
  - DU-025-6: aset `Tablet Samsung Tab {runId}`, Due date T0 + 1 hari, Approval Extend `Auto-approve`; Extend By `1`, Reason `Acara diperpanjang`; Due date baru T0 + 2 hari.
  - DU-025-7: BRW Group `Head Office`, Borrower `Nanda Putra {runId}`, berisi baris `Borrowed` aset DU-025-8.
  - DU-025-8: aset `Monitor LG UltraWide {runId}`, Due date T0 + 2 hari, Approval Extend `Auto-approve`; Extend By `1`, Reason `Presentasi diundur`; Due date baru T0 + 3 hari.
  - DU-025-9: BRW Group `Head Office`, Borrower `Oscar Wibowo {runId}`, berisi baris `Borrowed` aset DU-025-10.
  - DU-025-10: aset `Kamera Sony A6400 {runId}`, Due date T0 + 1 hari, Approval Extend `Auto-approve`; Extend By `1`, Reason `Kegiatan lapangan diperpanjang`; Due date baru T0 + 2 hari.
  - DU-025-11: BRW Group `Head Office`, Borrower `Oscar Wibowo {runId}`, berisi baris `Borrowed` aset DU-025-12.
  - DU-025-12: aset `Tripod Benro {runId}`, Due date T0 + 2 hari, Approval Extend `Auto-approve`; Extend By `1`, Reason `Pelatihan diundur`; Due date baru T0 + 3 hari.

## Test Steps

### Halaman Extend memuat baris eligible dan baris nonaktif beserta alasan
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Maya Sari {runId}`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-025-1
5. Buka Borrow Detail BRW milik DU-025-1
6. Klik `Request Extension`
7. Verifikasi halaman Extend tampil dengan baris aset DU-025-2, DU-025-3, dan DU-025-4
8. Verifikasi baris DU-025-4 nonaktif dengan alasan `An extension is already waiting for approval.`

### Submit Extend satu BRW berlaku langsung dan masuk approval kembali ke Borrow Detail
9. Isi Extend By baris DU-025-2 dengan `1`
10. Isi Reason baris DU-025-2 dengan `Proyek belum selesai`
11. Isi Extend By baris DU-025-3 dengan `2`
12. Isi Reason baris DU-025-3 dengan `Menunggu persetujuan klien`
13. Klik `[Submit Extension]`
14. Verifikasi toast `Success, due date has been changed for [Changed] of [Total] assets. [Submitted] submitted for approval.` tampil dengan [Changed] `1`, [Total] `2`, dan [Submitted] `1`
15. Verifikasi halaman kembali ke Borrow Detail BRW milik DU-025-1 karena semua baris yang diajukan berasal dari satu BRW
16. Verifikasi baris aset DU-025-2 memiliki Due date T0 + 2 hari dan baris aset DU-025-3 tetap Due date T0 + 1 hari selama menunggu approval

### Submit Extend lintas BRW berlaku langsung dan kembali ke halaman asal
17. Klik `Transactions` pada sidebar
18. Klik `Borrow`
19. Ketik Search `Nanda Putra {runId}`, tekan Enter
20. Klik menu ⋯ pada baris BRW milik DU-025-5
21. Klik `Request Extension`
22. Klik `[+ Asset]`
23. Pilih aset DU-025-8 pada dialog Select Asset
24. Klik `[Select]`
25. Isi Extend By baris DU-025-6 dengan `1`
26. Isi Reason baris DU-025-6 dengan `Acara diperpanjang`
27. Isi Extend By baris DU-025-8 dengan `1`
28. Isi Reason baris DU-025-8 dengan `Presentasi diundur`
29. Klik `[Extend]`
30. Verifikasi toast `Success, due date has been changed for [Changed] assets.` tampil dengan [Changed] `2`
31. Verifikasi halaman kembali ke tabel Transactions sebagai halaman asal karena baris yang diajukan berasal dari dua BRW

### Submit Extend lintas BRW dari tab Borrowed Assets kembali ke tab Borrowed Assets
32. Klik `Transactions` pada sidebar
33. Klik `Borrow`
34. Klik tab `Borrowed Assets`
35. Ketik Search `Oscar Wibowo {runId}`, tekan Enter
36. Klik menu ⋯ pada baris aset DU-025-10
37. Klik `Request Extension`
38. Klik `[+ Asset]`
39. Pilih aset DU-025-12 pada dialog Select Asset
40. Klik `[Select]`
41. Isi Extend By baris DU-025-10 dengan `1`
42. Isi Reason baris DU-025-10 dengan `Kegiatan lapangan diperpanjang`
43. Isi Extend By baris DU-025-12 dengan `1`
44. Isi Reason baris DU-025-12 dengan `Pelatihan diundur`
45. Klik `[Extend]`
46. Verifikasi toast `Success, due date has been changed for [Changed] assets.` tampil dengan [Changed] `2`
47. Verifikasi halaman kembali ke tab `Borrowed Assets` sebagai halaman asal karena baris yang diajukan berasal dari dua BRW
