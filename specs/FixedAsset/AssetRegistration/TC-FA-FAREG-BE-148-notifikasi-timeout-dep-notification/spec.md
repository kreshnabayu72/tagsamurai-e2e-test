---
id: TC-FA-FAREG-BE-148-notifikasi-timeout-dep-notification
title: "Notifikasi auto-cancel dan peringatan H-24"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.8#r6", "§9.8#r7"]
smoke: []
dependsOn:
  - "Notification: notifikasi in-app"
owner: BE
trace:
  "§9.8#r6": [16, 19]
  "§9.8#r7": [3, 4, 5, 6, 9, 13]
---

# Notifikasi auto-cancel dan peringatan H-24

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Palembang {runId}`) sebagai pengaju sekaligus requester.
  - Budi dan Citra (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Palembang {runId}`) sebagai approver aktif.
  - Maya (Manage purchase, Group terkelola `Gudang Palembang {runId}`) yang bukan approver dan bukan requester.
  - Operator Admin Console yang mengubah plan entitas aktor.
- Data:
  - DU-148-1: Group `Gudang Palembang {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-148-2: Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-148`, TAG Type `Non-TAG`, Status `Active`.
  - DU-148-3: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-148-4: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-148-5: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`.
  - DU-148-6: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Palembang {runId}` berisi `1` aset `Meja Kerja {runId}`.
- Kondisi:
  - kuota Group `Gudang Palembang {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.
  - background job pemeriksa timeout berjalan berkala.

## Test Steps

### Peringatan H-24 dikirim ke approver aktif dan requester
1. Catat jumlah notifikasi `registration_almost_timeout` milik Budi, Citra, Rina W, dan Maya
2. Waktu berlalu sampai sisa waktu ke batas Approval Timeout pengajuan DU-148-3 kurang dari atau sama dengan 24 jam
3. Verifikasi Budi menerima satu notifikasi baru dengan event_type `registration_almost_timeout` untuk pengajuan itu
4. Verifikasi Citra menerima satu notifikasi baru dengan event_type `registration_almost_timeout` untuk pengajuan itu
5. Verifikasi Rina W menerima satu notifikasi baru dengan event_type `registration_almost_timeout` sebagai requester
6. Verifikasi Maya tidak menerima notifikasi baru dengan event_type `registration_almost_timeout`

### Peringatan H-24 tidak dikirim berulang
7. Catat jumlah notifikasi `registration_almost_timeout` milik Budi dan Rina W
8. Background job pemeriksa timeout berjalan sekali lagi
9. Verifikasi jumlah notifikasi `registration_almost_timeout` milik Budi dan Rina W sama dengan catatan

### Pengajuan yang sudah diputuskan sebelum H-24 tidak memicu peringatan
10. Catat jumlah notifikasi `registration_almost_timeout` milik Rina W
11. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-148-4
12. Waktu berlalu sampai sisa waktu ke batas Approval Timeout pengajuan DU-148-4 kurang dari atau sama dengan 24 jam
13. Verifikasi jumlah notifikasi `registration_almost_timeout` milik Rina W sama dengan catatan

### Auto-cancel karena timeout memicu notifikasi ke requester
14. Catat jumlah notifikasi `registration_auto_canceled` milik Rina W
15. Waktu berlalu sampai Approval Timeout platform terlampaui sejak pengajuan DU-148-5 diajukan
16. Verifikasi Rina W menerima satu notifikasi baru dengan event_type `registration_auto_canceled` untuk pengajuan itu

### Auto-cancel karena plan berubah memicu notifikasi ke requester
17. Catat jumlah notifikasi `registration_auto_canceled` milik Rina W
18. Operator Admin Console mengubah plan entitas aktor sehingga kehilangan Approval Workflow, sementara pengajuan DU-148-6 berstatus `Waiting for Approval`
19. Verifikasi Rina W menerima satu notifikasi baru dengan event_type `registration_auto_canceled` untuk pengajuan itu
