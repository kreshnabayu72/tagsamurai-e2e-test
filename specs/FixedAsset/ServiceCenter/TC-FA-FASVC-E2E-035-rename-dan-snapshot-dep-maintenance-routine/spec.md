---
id: TC-FA-FASVC-E2E-035-rename-dan-snapshot-dep-maintenance-routine
title: "Rename Service Center yang Dipakai: Nama Baru di Tabel, Snapshot di Log Lama"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-01d, FASVC-LOGIC-07j, FASVC-LOGIC-07k, FASVC-LOGIC-09f, FASVC-LOGIC-09g, EC-FASVC-04, F-FASVC-02.k17, "§9.7#r1", "§9.4.3#b3", "§8#r9", "§9.2#r4"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-01d: [16, 17, 22, 27, 28]
  FASVC-LOGIC-07j: [16, 17, 22, 27]
  FASVC-LOGIC-07k: 33
  FASVC-LOGIC-09f: [5, 33]
  FASVC-LOGIC-09g: [16, 17, 22]
  EC-FASVC-04: [16, 17, 19, 33]
  F-FASVC-02.k17: [36, 38]
  "§9.7#r1": [16, 17, 22, 33]
  "§9.4.3#b3": [16, 17, 22]
  "§8#r9": [5, 16, 33]
  "§9.2#r4": 33
anchor: [18, 23]
coverage:
  web: automated
---

# Rename Service Center yang Dipakai: Nama Baru di Tabel, Snapshot di Log Lama

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-035-1: Group `Cabang Merapi {runId}`.
  - DU-035-2: User `Budi Santoso {runId}`, Role Asset Admin dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Merapi {runId}`; pencatat Task `Completed`.
  - DU-035-3: Service Center `Teknik Merapi Jaya {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Merapi {runId}`, City `Yogyakarta`; Name diganti menjadi `Teknik Merapi Perkasa {runId}` di spec ini.
  - DU-035-4: Schedule `Servis Merapi Bulanan {runId}`, Status `Active`, pelaksana default `Teknik Merapi Jaya {runId}`.
  - DU-035-5: Task aset `Kompresor Merapi {runId}`, Status `Completed`, pelaksana `Teknik Merapi Jaya {runId}`, dicatat oleh `Budi Santoso {runId}`, selesai `T0 − 3 hari, pukul 10:15`; log Task memuat `Executed by Teknik Merapi Jaya {runId} · recorded by Budi Santoso {runId}`.
  - DU-035-6: Task aset `Genset Merapi {runId}`, Status `To Do`, pelaksana `Teknik Merapi Jaya {runId}`.
  - DU-035-7: Aset `Kompresor Merapi {runId}`, Group `Cabang Merapi {runId}`.
  - DU-035-8: Aset `Genset Merapi {runId}`, Group `Cabang Merapi {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.

## Test Steps

### Log Task sebelum rename memuat nama lama
1. Buka Add-ons > Service Center
2. Ketik Search `Teknik Merapi Jaya {runId}`, tekan Enter
3. Klik angka Usage pada baris `Teknik Merapi Jaya {runId}`
4. Klik Reference pada baris aset `Kompresor Merapi {runId}`
5. Verifikasi log `Executed by Teknik Merapi Jaya {runId} · recorded by Budi Santoso {runId}` tampil di popup `Maintenance Routine Log`
6. Tutup popup `Maintenance Routine Log`

### Rename Service Center yang dipakai tampil di tabel dan pemilih modul pemakai
7. Catat entri teratas System Log aktor
8. Buka Add-ons > Service Center
9. Ketik Search `Teknik Merapi Jaya {runId}`, tekan Enter
10. Klik `⋯` pada baris `Teknik Merapi Jaya {runId}`
11. Klik `Edit`
12. Ganti isi Name menjadi `Teknik Merapi Perkasa {runId}`
13. Klik `[Save]`
14. Buka daftar Task di Maintenance Routine
15. Ketik Search `Merapi {runId}`, tekan Enter
16. Verifikasi baris Task aset `Kompresor Merapi {runId}` menampilkan pelaksana `Teknik Merapi Perkasa {runId}`
17. Verifikasi baris Task aset `Genset Merapi {runId}` menampilkan pelaksana `Teknik Merapi Perkasa {runId}`
18. Verifikasi baris Task aset `Genset Merapi {runId}` tetap berstatus `To Do`
19. Verifikasi tidak ada baris Task yang menampilkan pelaksana `Teknik Merapi Jaya {runId}`
20. Buka daftar Schedule di Maintenance Routine
21. Ketik Search `Servis Merapi Bulanan {runId}`, tekan Enter
22. Verifikasi baris Schedule `Servis Merapi Bulanan {runId}` menampilkan pelaksana default `Teknik Merapi Perkasa {runId}`
23. Verifikasi baris Schedule `Servis Merapi Bulanan {runId}` tetap berstatus `Active`
24. Buka form Create Schedule di Maintenance Routine
25. Pilih aset `Kompresor Merapi {runId}` saja
26. Klik pemilih `Select service center`
27. Verifikasi opsi `Teknik Merapi Perkasa {runId}` tampil
28. Verifikasi `Teknik Merapi Jaya {runId}` tidak ada di opsi

### Log Task yang sudah tertulis tetap memuat nama lama
29. Buka Add-ons > Service Center
30. Ketik Search `Teknik Merapi Perkasa {runId}`, tekan Enter
31. Klik angka Usage pada baris `Teknik Merapi Perkasa {runId}`
32. Klik Reference pada baris aset `Kompresor Merapi {runId}`
33. Verifikasi log `Executed by Teknik Merapi Jaya {runId} · recorded by Budi Santoso {runId}` tetap tampil di popup `Maintenance Routine Log`

### Rename tercatat di Changelog dan System Log
34. Buka Add-ons > Service Center
35. Klik `[Changelog]`
36. Verifikasi baris Changelog dengan Action `Updated`, Field `Name`, Old Value `Teknik Merapi Jaya {runId}`, dan New Value `Teknik Merapi Perkasa {runId}` tampil
37. Buka System Log aktor
38. Verifikasi entri teratas System Log berAction `Updated` dan berbeda dari entri teratas yang dicatat sebelumnya
