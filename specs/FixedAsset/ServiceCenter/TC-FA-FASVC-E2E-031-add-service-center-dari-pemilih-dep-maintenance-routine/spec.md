---
id: TC-FA-FASVC-E2E-031-add-service-center-dari-pemilih-dep-maintenance-routine
title: "Link Add service center dari Pemilih: Form Terisi, Langsung Terpilih atau Toast Tidak Cocok"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [F-FASVC-05.k3, EC-FASVC-25a, EC-FASVC-25b, EC-FASVC-25c, EC-FASVC-25d, TS-FASVC-09, "§4.2.4#b4", "§4.2.4#b5"]
smoke: []
dependsOn: ["Maintenance Routine: form Schedule dan Task"]
trace:
  F-FASVC-05.k3: [20, 22]
  EC-FASVC-25a: [9, 10, 11, 12]
  EC-FASVC-25b: 17
  EC-FASVC-25c: [37, 40]
  EC-FASVC-25d: 34
  TS-FASVC-09: [34, 35, 36]
  "§4.2.4#b4": [5, 6, 8, 9, 10, 11, 12, 17, 26, 34, 37, 44, 45]
  "§4.2.4#b5": [47, 48, 49, 50, 52, 54, 56, 58]
anchor: []
coverage:
  web: automated
---

# Link Add service center dari Pemilih: Form Terisi, Langsung Terpilih atau Toast Tidak Cocok

## Prerequisites
- Aktor: Total Control entitas `Klien Tautan Vendor {runId}`.
- Layar awal: Maintenance Routine.
- Data:
  - Spec ini memakai entitas khusus `Klien Tautan Vendor {runId}` yang tidak dipakai spec lain.
  - DU-031-15: Entitas `Klien Tautan Vendor {runId}`, lisensi addon Maintenance `Active`.
  - DU-031-1: Group `Cabang Bekasi {runId}`.
  - DU-031-2: Group `Cabang Cikarang {runId}`.
  - DU-031-3: Category `Kompresor {runId}`.
  - DU-031-4: Category `Pembangkit {runId}`.
  - DU-031-5: Category `Pompa {runId}`.
  - DU-031-6: Brand `Atlas {runId}`.
  - DU-031-7: Brand `Perkins {runId}`.
  - DU-031-8: Brand `Grundfos {runId}`.
  - DU-031-9: Aset `Kompresor Utama {runId}`, Group `Cabang Bekasi {runId}`, Category `Kompresor {runId}`, Brand `Atlas {runId}`.
  - DU-031-10: Aset `Genset Darurat {runId}`, Group `Cabang Bekasi {runId}`, Category `Pembangkit {runId}`, Brand `Perkins {runId}`.
  - DU-031-11: Aset `Pompa Transfer {runId}`, Group `Cabang Cikarang {runId}`, Category `Pompa {runId}`, Brand `Grundfos {runId}`.
  - DU-031-12: Aset `Pompa Cadangan {runId}`, Group `Cabang Cikarang {runId}`, Category `Pompa {runId}`, tanpa Brand.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Master Data Count Limit bernilai `1000`.
  - Entitas `Klien Tautan Vendor {runId}` tidak berisi Service Center selain yang dibuat spec ini.

## Test Steps

### Pemilih satu aset tanpa vendor yang cocok menawarkan link Add service center
1. Catat entri teratas System Log pada Detail User aktor
2. Buka form Create Schedule di Maintenance Routine
3. Pilih aset `Kompresor Utama {runId}` saja
4. Klik pemilih `Select service center`
5. Verifikasi pesan `No service centers match this asset (Cabang Bekasi {runId} · Kompresor {runId} · Atlas {runId}).` tampil
6. Verifikasi link `Add service center` tampil

### Link Add service center membuka form terisi dan vendor langsung terpilih
7. Klik link `Add service center`
8. Verifikasi form `Add Service Center` terbuka
9. Verifikasi Service type `Routine` terisi sesuai pemanggil
10. Verifikasi Available to terisi `Cabang Bekasi {runId}`
11. Verifikasi Specialization terisi `Kompresor {runId}`
12. Verifikasi Brands terisi `Atlas {runId}`
13. Isi Name `Bengkel Kompresor Bekasi {runId}`
14. Isi City `Bekasi`
15. Isi Company phone dengan Dial Code `+62` dan nomor `218550311`
16. Klik `[Submit]`
17. Verifikasi pemilih `Select service center` menampilkan `Bengkel Kompresor Bekasi {runId}` sebagai nilai terpilih

### Add service center dari pemilih tercatat di Changelog dan System Log
18. Buka Add-ons > Service Center
19. Klik `[Changelog]`
20. Verifikasi baris Changelog dengan Action `Created` dan Service Center Name `Bengkel Kompresor Bekasi {runId}` tampil
21. Buka System Log pada Detail User aktor
22. Verifikasi entri teratas System Log berAction `Created` dan berbeda dari entri teratas yang dicatat sebelumnya

### Cakupan diubah sehingga tidak cocok: tersimpan tetapi tidak terpilih
23. Buka form Create Schedule di Maintenance Routine
24. Pilih aset `Genset Darurat {runId}` saja
25. Klik pemilih `Select service center`
26. Verifikasi pesan `No service centers match this asset (Cabang Bekasi {runId} · Pembangkit {runId} · Perkins {runId}).` tampil
27. Klik link `Add service center`
28. Pilih Specialization `Kompresor {runId}`
29. Lepas Specialization `Pembangkit {runId}`
30. Isi Name `Servis Kompresor Alternatif {runId}`
31. Isi City `Bekasi`
32. Isi Company phone dengan Dial Code `+62` dan nomor `218550312`
33. Klik `[Submit]`
34. Verifikasi toast `Servis Kompresor Alternatif {runId} was added but doesn't cover this asset, so it was not selected.` tampil
35. Verifikasi toast tersebut bersifat Info (netral), bukan toast sukses maupun error
36. Verifikasi toast `Success, Servis Kompresor Alternatif {runId} has been added.` tidak tampil
37. Verifikasi pemilih `Select service center` tidak memuat `Servis Kompresor Alternatif {runId}` sebagai nilai terpilih
38. Buka Add-ons > Service Center
39. Ketik Search `Servis Kompresor Alternatif {runId}`, tekan Enter
40. Verifikasi baris `Servis Kompresor Alternatif {runId}` tampil di tabel Service Center

### Pemilih banyak aset: form terisi dengan gabungan semua aset
41. Buka form Create Schedule di Maintenance Routine
42. Pilih aset `Kompresor Utama {runId}`, `Pompa Transfer {runId}`, dan `Pompa Cadangan {runId}`
43. Klik pemilih `Select service center`
44. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil
45. Verifikasi link `Add service center` tampil
46. Klik link `Add service center`
47. Verifikasi Service type `Routine` terisi sesuai pemanggil
48. Verifikasi Available to terisi `Cabang Bekasi {runId}` dan `Cabang Cikarang {runId}`
49. Verifikasi Specialization terisi `Kompresor {runId}` dan `Pompa {runId}`
50. Verifikasi Brands terisi `Atlas {runId}` dan `Grundfos {runId}`, tanpa nilai tambahan dari aset `Pompa Cadangan {runId}` yang tidak punya merek
51. Lepas Specialization `Pompa {runId}`
52. Verifikasi Specialization terisi `Kompresor {runId}` dan tidak lagi memuat `Pompa {runId}`
53. Lepas Brands `Grundfos {runId}`
54. Verifikasi Brands terisi `Atlas {runId}` dan tidak lagi memuat `Grundfos {runId}`
55. Lepas Available to `Cabang Cikarang {runId}`
56. Verifikasi Available to terisi `Cabang Bekasi {runId}` dan tidak lagi memuat `Cabang Cikarang {runId}`
57. Centang Service type `Repair`
58. Verifikasi Service type terisi `Routine` dan `Repair`
59. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
