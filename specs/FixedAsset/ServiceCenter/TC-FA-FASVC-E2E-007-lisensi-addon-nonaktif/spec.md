---
id: TC-FA-FASVC-E2E-007-lisensi-addon-nonaktif
title: "Lisensi Addon Maintenance Tidak Aktif: Menu Tidak Tampil, URL Langsung, Data Kembali"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FASVC-LOGIC-10a", "FASVC-LOGIC-10b", "FASVC-LOGIC-10c", "FASVC-LOGIC-10d", "FASVC-LOGIC-10f", "EC-FASVC-27", "EC-FASVC-28", "F-FASVC-01.k3", "F-FASVC-01.k4", "§9.11#p1", "§9.11#r1", "§9.11#r3", "§9.7#r8", "§11#r10", "§Dependencies#b10"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-10a": [3, 7, 9]
  "FASVC-LOGIC-10b": [3, 7]
  "FASVC-LOGIC-10c": 7
  "FASVC-LOGIC-10d": [9, 10]
  "FASVC-LOGIC-10f": [17, 19]
  "EC-FASVC-27": [7, 9]
  "EC-FASVC-28": [14, 17, 19]
  "F-FASVC-01.k3": [7, 9]
  "F-FASVC-01.k4": [14, 17, 19]
  "§9.11#p1": [3, 7, 14]
  "§9.11#r1": [7, 9, 10]
  "§9.11#r3": [14, 17, 18, 19, 20]
  "§9.7#r8": [7, 14]
  "§11#r10": [3, 7, 14]
  "§Dependencies#b10": [3, 7, 14]
anchor: [6]
coverage:
  web: automated
---

# Lisensi Addon Maintenance Tidak Aktif: Menu Tidak Tampil, URL Langsung, Data Kembali

## Prerequisites
- Aktor: Total Control `Lena Control {runId}` pada entitas khusus `Entitas Uji Lisensi {runId}`, dan Plan Owner `Pandu PlanOwner {runId}` yang mengalokasikan lisensi addon. Spec ini memakai entitas khusus yang tidak dipakai spec lain.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-007-1: Entitas `Entitas Uji Lisensi {runId}` dengan subscription Fixed Asset Paid berstatus Active dan lisensi addon `Maintenance` dialokasikan.
  - DU-007-2: Entitas `Entitas Uji Lisensi {runId}` dengan subscription Fixed Asset Paid berstatus Active dan lisensi addon `Maintenance` tidak dialokasikan, hasil pencabutan oleh Plan Owner.
  - DU-007-3: Aktor `Lena Control {runId}` dengan Role `Total Control`, ada di entitas `Entitas Uji Lisensi {runId}`.
  - DU-007-4: Aktor `Pandu PlanOwner {runId}` sebagai Plan Owner (Principal) yang mengalokasikan lisensi addon.
  - DU-007-5: Service Center `Servis Lisensi Aktif {runId}`, Service type `Routine`, Available to `All groups`, City `Surabaya`, Company email `kontak@lisensiaktif.co.id`, Status `Active`, ada di entitas `Entitas Uji Lisensi {runId}`. Usage `0`.
  - DU-007-6: Service Center `Servis Lisensi Nonaktif {runId}`, Service type `Repair`, Available to `All groups`, City `Malang`, Company email `kontak@lisensinonaktif.co.id`, Status `Inactive`, ada di entitas `Entitas Uji Lisensi {runId}`. Usage `0`.
- Kondisi:
  - Akun `Lena Control {runId}` aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas `Entitas Uji Lisensi {runId}` berisi kurang dari 1.000 Service Center.

## Test Steps

### Lisensi addon Maintenance aktif: menu Service Center tampil
1. Masuk sebagai `Lena Control {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Verifikasi menu `Service Center` tampil di bawah `Add-ons`

### Lisensi dicabut: menu tidak tampil dan URL langsung menampilkan empty state
4. Plan Owner `Pandu PlanOwner {runId}` mencabut alokasi lisensi addon `Maintenance` dari entitas `Entitas Uji Lisensi {runId}`
5. Muat ulang halaman
6. Verifikasi menu `Dashboard` tampil pada sidebar
7. Verifikasi menu `Service Center` tidak tampil pada sidebar
8. Buka halaman daftar Service Center lewat alamat langsung
9. Verifikasi empty state `Service Center is not available.` tampil
10. Verifikasi petunjuk `Activate the Maintenance add-on (Maintenance Routine / Repair) to use it.` tampil

### Lisensi dialokasikan kembali: menu, data, dan status kembali
11. Plan Owner `Pandu PlanOwner {runId}` mengalokasikan kembali lisensi addon `Maintenance` ke entitas `Entitas Uji Lisensi {runId}`
12. Muat ulang halaman
13. Buka menu `Add-ons` pada sidebar
14. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
15. Klik `Service Center`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Servis Lisensi Aktif {runId}` tampil di tabel
18. Verifikasi kolom Status pada baris `Servis Lisensi Aktif {runId}` menampilkan `Active`
19. Verifikasi baris `Servis Lisensi Nonaktif {runId}` tampil di tabel
20. Verifikasi kolom Status pada baris `Servis Lisensi Nonaktif {runId}` menampilkan `Inactive`
