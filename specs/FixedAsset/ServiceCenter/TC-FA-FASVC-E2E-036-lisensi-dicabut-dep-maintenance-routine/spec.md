---
id: TC-FA-FASVC-E2E-036-lisensi-dicabut-dep-maintenance-routine
title: "Lisensi Dicabut: Task dan Schedule oleh System, Wind-down 30 Hari, Data Tetap"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-10g, "§9.11#r2"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-10g: [3, 5, 7, 9, 12, 14, 18]
  "§9.11#r2": [3, 5, 7, 9, 12, 14, 18]
anchor: []
coverage:
  web: automated
---

# Lisensi Dicabut: Task dan Schedule oleh System, Wind-down 30 Hari, Data Tetap

## Prerequisites
- Aktor: Total Control entitas `Klien Lisensi {runId}`. Aktor kedua: Operator Admin Console yang mengelola lisensi addon entitas.
- Layar awal: Maintenance Routine.
- Data:
  - Spec ini memakai entitas khusus `Klien Lisensi {runId}` yang tidak dipakai spec lain.
  - DU-036-1: Entitas `Klien Lisensi {runId}`, lisensi addon Maintenance `Active`.
  - DU-036-2: User `Hendra Gunawan {runId}`, Role Total Control di entitas `Klien Lisensi {runId}`.
  - DU-036-3: Group `Cabang Utama Lisensi {runId}`.
  - DU-036-4: Service Center `Teknik Lisensi Prima {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Utama Lisensi {runId}`, City `Medan`.
  - DU-036-5: Schedule `Servis Lisensi Bulanan {runId}`, Status `Active`, pelaksana default `Teknik Lisensi Prima {runId}`.
  - DU-036-6: Task aset `Mesin Lisensi Satu {runId}`, Status `To Do`, pelaksana `Teknik Lisensi Prima {runId}`.
  - DU-036-7: Task aset `Mesin Lisensi Dua {runId}`, Status `In Progress`, pelaksana `Teknik Lisensi Prima {runId}`.
  - DU-036-8: Task aset `Mesin Lisensi Tiga {runId}`, Status `Waiting for Approval`, pelaksana `Teknik Lisensi Prima {runId}`.
- Kondisi:
  - Lisensi addon Maintenance entitas `Klien Lisensi {runId}` aktif sampai langkah pertama dijalankan.

## Test Steps

### Lisensi dicabut: Task dan Schedule oleh System, wind-down 30 hari, data tetap
1. Operator Admin Console mencabut lisensi addon Maintenance dari entitas `Klien Lisensi {runId}`
2. Buka Task aset `Mesin Lisensi Satu {runId}` di Maintenance Routine
3. Verifikasi Task berstatus `Canceled` oleh `System`
4. Buka Schedule `Servis Lisensi Bulanan {runId}` di Maintenance Routine
5. Verifikasi Schedule berstatus `Paused` oleh `System`
6. Buka Task aset `Mesin Lisensi Dua {runId}` di Maintenance Routine
7. Verifikasi Task berstatus `In Progress` dengan pelaksana `Teknik Lisensi Prima {runId}` tetap terbaca
8. Buka Task aset `Mesin Lisensi Tiga {runId}` di Maintenance Routine
9. Verifikasi Task berstatus `Waiting for Approval` dengan pelaksana `Teknik Lisensi Prima {runId}` tetap terbaca
10. Waktu berlalu sampai 30 hari sejak lisensi dicabut
11. Buka Task aset `Mesin Lisensi Dua {runId}` di Maintenance Routine
12. Verifikasi Task berstatus `Canceled` oleh `System`
13. Buka Task aset `Mesin Lisensi Tiga {runId}` di Maintenance Routine
14. Verifikasi Task berstatus `Canceled` oleh `System`
15. Operator Admin Console mengaktifkan kembali lisensi addon Maintenance entitas `Klien Lisensi {runId}`
16. Buka Add-ons > Service Center
17. Ketik Search `Teknik Lisensi Prima {runId}`, tekan Enter
18. Verifikasi baris `Teknik Lisensi Prima {runId}` tampil karena data Service Center tetap tersimpan
