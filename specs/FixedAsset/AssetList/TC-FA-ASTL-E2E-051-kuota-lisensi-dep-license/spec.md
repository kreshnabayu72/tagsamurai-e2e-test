---
id: TC-FA-ASTL-E2E-051-kuota-lisensi-dep-license
title: "Kuota lisensi tercermin di Manage"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-16i", "ASTL-LOGIC-16m", "§9.7#r12"]
smoke: []
dependsOn: ["License: kuota lisensi"]
trace:
  "ASTL-LOGIC-16i": [20, 41]
  "ASTL-LOGIC-16m": 29
  "§9.7#r12": [8, 9, 11, 31, 32]
anchor: [2, 14, 22, 34]
coverage:
  web: automated
---

# Kuota lisensi tercermin di Manage

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-051-1: aset `Kamera Mirrorless {runId} - 1`, Group `Cabang Denpasar Timur {runId}`, Unmanaged; kuota group itu Available license `2`, Reserved `0`, Used `0`.
  - DU-051-2: aset `Scanner Gudang {runId} - 1`, Group `Cabang Denpasar`, `Pending Activation`, memegang kuota Reserved `1`, tanpa penyusutan atau jurnal Posted.
  - DU-051-5: aset `Tablet Inventaris {runId} - 1`, Group `Cabang Denpasar`, `Pending Activation`, memegang kuota Reserved `1`, Custody `Available`, tanpa penyusutan atau jurnal Posted.
  - DU-051-3: aset `Printer Laser {runId} - 1`, Group `Cabang Denpasar`, Unmanaged, Custody `Available`, tanpa penyusutan atau jurnal Posted.

## Test Steps

### Manage dengan Available quota tercermin di badge dan kuota
1. Ketik Search `Kamera Mirrorless {runId}`, tekan Enter
2. Verifikasi baris `Kamera Mirrorless {runId} - 1` menampilkan badge overlay `Unmanaged`
3. Catat Available license dan Reserved Cabang Denpasar Timur `{runId}` pada modul License
4. Buka menu `⋯` baris `Kamera Mirrorless {runId} - 1`
5. Klik `Manage`
6. Pilih sumber `Available quota`
7. Klik `[Manage]`
8. Verifikasi badge overlay baris `Kamera Mirrorless {runId} - 1` berubah dari `Unmanaged` menjadi `Pending Activation`, tanpa memuat ulang halaman
9. Verifikasi modul License menampilkan Reserved Cabang Denpasar Timur `{runId}` bertambah satu dan Available license berkurang satu dari angka yang dicatat
10. Buka menu `⋯` baris `Kamera Mirrorless {runId} - 1`
11. Verifikasi aksi `Manage` tampil `Disabled` dengan tooltip `Manage is available again on` diikuti tanggal-waktu jeda yang nyata, dalam Date Format, Time Format, dan Time Zone General Settings
12. Tutup menu aksi baris

### Kuota Reserved dilepas saat aset Pending Activation dihapus
13. Ketik Search `Scanner Gudang {runId}`, tekan Enter
14. Verifikasi baris `Scanner Gudang {runId} - 1` menampilkan badge overlay `Pending Activation`
15. Catat Available license dan Reserved Cabang Denpasar pada modul License
16. Buka menu `⋯` baris `Scanner Gudang {runId} - 1`
17. Klik `Delete Asset Data`
18. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
19. Klik `[Delete]`
20. Verifikasi modul License menampilkan Reserved Cabang Denpasar berkurang satu dan Available license bertambah satu dari angka yang dicatat

### Disposal aset Unmanaged tidak memakai kuota
21. Ketik Search `Printer Laser {runId}`, tekan Enter
22. Verifikasi baris `Printer Laser {runId} - 1` menampilkan badge overlay `Unmanaged`
23. Catat Available license, Reserved, dan Used Cabang Denpasar pada modul License
24. Buka menu `⋯` baris `Printer Laser {runId} - 1`
25. Klik `Report Disposal`
26. Isi Reason `Aset sudah tidak dipakai {runId}`
27. Konfirmasi dialog Report Disposal
28. Hendra Saputra menjalankan Submit Request dan Execute atas `Printer Laser {runId} - 1` hingga aset berstatus `Disposed`
29. Verifikasi modul License menampilkan Available license, Reserved, dan Used Cabang Denpasar sama dengan angka yang dicatat

### Aktivasi selesai memindahkan kuota Reserved ke Used
30. Tunggu hingga aktivasi `Kamera Mirrorless {runId} - 1` selesai
31. Verifikasi baris `Kamera Mirrorless {runId} - 1` tidak lagi menampilkan badge overlay `Pending Activation` dan `Unmanaged`
32. Verifikasi modul License menampilkan untuk Cabang Denpasar Timur `{runId}` Reserved `0`, Used `1`, dan Available license `1`

### Kuota Reserved dilepas saat aset Pending Activation didisposal
33. Ketik Search `Tablet Inventaris {runId}`, tekan Enter
34. Verifikasi baris `Tablet Inventaris {runId} - 1` menampilkan badge overlay `Pending Activation`
35. Catat Available license dan Reserved Cabang Denpasar pada modul License
36. Buka menu `⋯` baris `Tablet Inventaris {runId} - 1`
37. Klik `Report Disposal`
38. Isi Reason `Aset sudah tidak dipakai {runId}`
39. Konfirmasi dialog Report Disposal
40. Hendra Saputra menjalankan Submit Request dan Execute atas `Tablet Inventaris {runId} - 1` hingga aset berstatus `Disposed`
41. Verifikasi modul License menampilkan Reserved Cabang Denpasar berkurang satu dan Available license bertambah satu dari angka yang dicatat
