---
id: TC-FA-MISS-E2E-010-tab-history-filter
title: "Tab History: filter Status, Group dan Category multi-select historis, Duration range, dan Resolved Date"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1b#p1, §4.1b#r9, §4.1b#r8, §4.1b#r7, §4.1b#r14, §9.5#r9]
smoke: []
dependsOn: []
trace:
  §4.1b#p1: [8, 17, 22]
  §4.1b#r9: [12, 13]
  §4.1b#r8: [8, 17, 18]
  §4.1b#r7: [22, 23]
  §4.1b#r14: [27, 28, 32, 36, 37]
  §9.5#r9: 6
anchor: [4]
coverage:
  web: automated
---

# Tab History: filter Status, Group dan Category multi-select historis, Duration range, dan Resolved Date

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-010-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-010-2: Record `Found` untuk aset `Kursi Kantor {runId}`; saat selesai Group aset `Gudang Arsip {runId}` (kini sudah dihapus dari hierarki Group) dan Category `Elektronik {runId}`; Source `Manual`, Reported Date T0 − 30 hari pukul `09:00`, Resolved Date T0 − 24 hari pukul `14:10`, Duration `6 days`, dari selisih 6 hari kalender.
  - DU-010-3: Record `Disposed` untuk aset `Lemari Besi {runId}`; saat selesai Group `Gudang Arsip {runId}` dan Category `Kendaraan {runId}`; Source `Manual`, Reported Date T0 − 70 hari pukul `08:00`, Resolved Date T0 − 8 hari pukul `00:00`, Duration `62 days`, dari selisih 62 hari kalender.
  - DU-010-4: Record `Rejected` untuk aset `Proyektor Kecil {runId}`; saat selesai Group `Gudang Aktif {runId}` dan Category `Elektronik {runId}`; Source `Reported by holder`, Reported Date T0 − 10 hari pukul `08:30`, Resolved Date T0 − 9 hari pukul `09:15`, Duration `1 day`, dari selisih 1 hari kalender.
  - DU-010-5: Record `Canceled` untuk aset `Meja Lipat {runId}`; saat selesai Group `Gudang Aktif {runId}` dan Category `Furnitur {runId}`; Source `Reported by holder`, Reported Date T0 − 14 hari pukul `13:00`, Resolved Date T0 − 11 hari pukul `08:20`, Duration `3 days`, dari selisih 3 hari kalender.
  - Reported By dan Resolved By setiap record DU-010-2 sampai DU-010-5 adalah `Rina Wijaya {runId}`.
  - DU-010-6: rentang Resolved Date dari T0 − 24 hari sampai T0 − 9 hari; DU-010-2 tepat di hari awal dan DU-010-4 tepat di hari akhir.
  - DU-010-7: rentang Duration dengan Min `6` dan Max `62`; DU-010-2 tepat di Min dan DU-010-3 tepat di Max.
  - DU-010-8: rentang Duration dengan Min `1` dan Max `3`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.

## Test Steps

### Filter Panel tanpa saringan bawaan dan opsi dari data historis
1. Klik tab `Missing` pada halaman Assets
2. Klik sub-tab `History`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi tabel memuat baris untuk `Kursi Kantor {runId}`, `Lemari Besi {runId}`, `Proyektor Kecil {runId}`, `Meja Lipat {runId}` yang berstatus `Found`, `Disposed`, `Rejected`, dan `Canceled`
5. Klik ikon Filter
6. Verifikasi tidak ada field Filter Panel yang berisi nilai ter-Apply dan ikon Filter tidak berbadge titik
7. Buka field `Group`
8. Verifikasi opsi field `Group` memuat `Gudang Arsip {runId}` dan `Gudang Aktif {runId}` sebagai nilai historis yang dicatat saat record selesai, walau `Gudang Arsip {runId}` sudah tidak ada di hierarki Group
9. Tutup daftar opsi `Group`

### Filter Status dengan OR dalam satu field
10. Pada field `Status` pilih opsi `Found` dan `Rejected`
11. Klik `[Apply]`
12. Verifikasi tabel memuat baris `Kursi Kantor {runId}`, `Proyektor Kecil {runId}` yang berstatus `Found` atau `Rejected`
13. Verifikasi baris `Lemari Besi {runId}`, `Meja Lipat {runId}` yang berstatus `Disposed` dan `Canceled` tidak tampil
14. Klik `[Clear Field]`

### Filter Group historis dengan multi-select dan nilai yang sama persis
15. Pada field `Group` pilih opsi `Gudang Arsip {runId}`
16. Klik `[Apply]`
17. Verifikasi tabel memuat baris `Kursi Kantor {runId}`, `Lemari Besi {runId}` yang Group-nya `Gudang Arsip {runId}` saat selesai
18. Verifikasi baris `Proyektor Kecil {runId}`, `Meja Lipat {runId}` yang Group-nya `Gudang Aktif {runId}` tidak tampil
19. Klik `[Clear Field]`

### Filter Category historis walau kolom Category tersembunyi
20. Pada field `Category` pilih opsi `Elektronik {runId}`
21. Klik `[Apply]`
22. Verifikasi tabel memuat baris `Kursi Kantor {runId}`, `Proyektor Kecil {runId}` yang Category-nya `Elektronik {runId}` saat selesai, walau kolom `Category` tersembunyi
23. Verifikasi baris `Lemari Besi {runId}`, `Meja Lipat {runId}` yang Category-nya `Kendaraan {runId}` dan `Furnitur {runId}` tidak tampil
24. Klik `[Clear Field]`

### Filter rentang Duration
25. Isi field `Duration` dengan Min `6` dan Max `62`
26. Klik `[Apply]`
27. Verifikasi tabel memuat baris `Kursi Kantor {runId}` yang Duration-nya tepat di Min dan baris `Lemari Besi {runId}` yang tepat di Max
28. Verifikasi baris `Proyektor Kecil {runId}`, `Meja Lipat {runId}` yang Duration-nya `1 day` dan `3 days` tidak tampil
29. Klik `[Clear Field]`
30. Isi field `Duration` dengan Min `1` dan Max `3`
31. Klik `[Apply]`
32. Verifikasi tabel memuat baris `Proyektor Kecil {runId}`, `Meja Lipat {runId}` dan tidak memuat baris `Kursi Kantor {runId}`, `Lemari Besi {runId}`
33. Klik `[Clear Field]`

### Filter rentang Resolved Date
34. Pilih rentang Resolved Date sesuai DU-010-6
35. Klik `[Apply]`
36. Verifikasi tabel memuat baris `Kursi Kantor {runId}` yang tepat di hari awal, `Meja Lipat {runId}` di antara, dan `Proyektor Kecil {runId}` yang tepat di hari akhir
37. Verifikasi baris `Lemari Besi {runId}` yang selesai sesudah hari akhir tidak tampil
38. Klik `[Clear Field]`
39. Klik `[Apply]`
