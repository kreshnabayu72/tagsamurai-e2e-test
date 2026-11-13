---
id: TC-FA-FAREG-BE-148-notifikasi-timeout-dep-notification
title: "Notifikasi auto-cancel dan peringatan H-24"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.8#r6", "§9.8#r7"]
smoke: []
dependsOn:
  - "Notification: notifikasi in-app"
owner: BE
trace:
  "§9.8#r6": 12
  "§9.8#r7": [3, 4, 5, 6, 9, 16]
---

# Notifikasi auto-cancel dan peringatan H-24

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Palembang {runId}`) sebagai pengaju sekaligus requester.
  - Budi dan Citra (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Palembang {runId}`) sebagai approver aktif.
  - Maya (Manage purchase, Group terkelola `Gudang Palembang {runId}`) yang bukan approver dan bukan requester.
- Data:
  - DU-148-1: Group `Gudang Palembang {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-148-2: Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-148`, TAG Type `Non-TAG`, Status `Active`.
  - DU-148-3: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`, diajukan pada `T0 - 47 jam`, sehingga batas Approval Timeout-nya `T0 + 25 jam`.
  - DU-148-4: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`, diajukan pada `T0`, sehingga batas Approval Timeout-nya `T0 + 72 jam`.
- Kondisi:
  - kuota Group `Gudang Palembang {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.
  - `T0` adalah waktu spec dimulai.
  - Approval Timeout platform bernilai `3` hari.
  - background job pemeriksa timeout berjalan berkala.

## Test Steps

### Peringatan H-24 dikirim ke approver aktif dan requester
1. Catat jumlah notifikasi `registration_almost_timeout` yang menyebut pengajuan DU-148-3 milik Budi, Citra, Rina W, dan Maya
2. Waktu berlalu sampai `T0 + 2 jam`, ketika sisa waktu ke batas Approval Timeout pengajuan DU-148-3 tinggal `23` jam
3. Verifikasi Budi menerima satu notifikasi baru dengan event_type `registration_almost_timeout` yang menyebut pengajuan DU-148-3
4. Verifikasi Citra menerima satu notifikasi baru dengan event_type `registration_almost_timeout` yang menyebut pengajuan DU-148-3
5. Verifikasi Rina W menerima satu notifikasi baru dengan event_type `registration_almost_timeout` yang menyebut pengajuan DU-148-3 sebagai requester
6. Verifikasi Maya tidak menerima notifikasi baru dengan event_type `registration_almost_timeout` yang menyebut pengajuan DU-148-3

### Peringatan H-24 tidak dikirim berulang
7. Catat jumlah notifikasi `registration_almost_timeout` yang menyebut pengajuan DU-148-3 milik Budi dan Rina W
8. Background job pemeriksa timeout berjalan sekali lagi
9. Verifikasi jumlah notifikasi `registration_almost_timeout` yang menyebut pengajuan DU-148-3 milik Budi dan Rina W sama dengan catatan

### Auto-cancel karena timeout memicu notifikasi ke requester
10. Catat jumlah notifikasi `registration_auto_canceled` yang menyebut pengajuan DU-148-3 milik Rina W
11. Waktu berlalu sampai `T0 + 26 jam`, ketika batas Approval Timeout pengajuan DU-148-3 telah terlampaui
12. Verifikasi Rina W menerima satu notifikasi baru dengan event_type `registration_auto_canceled` yang menyebut pengajuan DU-148-3

### Pengajuan yang sudah diputuskan sebelum H-24 tidak memicu peringatan
13. Catat jumlah notifikasi `registration_almost_timeout` yang menyebut pengajuan DU-148-4 milik Rina W
14. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-148-4
15. Waktu berlalu sampai `T0 + 49 jam`, ketika sisa waktu ke batas Approval Timeout pengajuan DU-148-4 tinggal `23` jam
16. Verifikasi jumlah notifikasi `registration_almost_timeout` yang menyebut pengajuan DU-148-4 milik Rina W sama dengan catatan
