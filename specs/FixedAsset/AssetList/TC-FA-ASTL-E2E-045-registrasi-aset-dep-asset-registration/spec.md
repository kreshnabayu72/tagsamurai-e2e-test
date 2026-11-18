---
id: TC-FA-ASTL-E2E-045-registrasi-aset-dep-asset-registration
title: "Aset hasil registrasi muncul di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-01a", "§9.4.3#p2", "§9.7#r4"]
smoke: []
dependsOn: ["Asset Registration: registrasi aset"]
trace:
  "ASTL-LOGIC-01a": [3, 4, 5, 9, 12, 20, 23]
  "§9.4.3#p2": 3
  "§9.7#r4": 17
anchor: [2, 8, 15]
coverage:
  web: automated
---

# Aset hasil registrasi muncul di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-045-1: aset `Laptop Pro 16 {runId} - 1`, Group `IT`, Lifecycle `Active`, Custody `Available`.
  - DU-045-2: aset `Mobil Operasional {runId} - 1`, Group `IT`, Lifecycle `Draft`.
  - DU-045-3: aset `Printer Laser {runId} - 1`, Group `IT`, Lifecycle `Waiting for Approval`.
  - DU-045-4: aset `Server Rack {runId} - 1`, Group `IT`, Lifecycle `Deleted`.

## Test Steps

### Draft, Waiting for Approval, dan Deleted tidak tampil di All Assets
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1` (Active) tampil pada tabel hasil Search `{runId}`
3. Verifikasi baris `Mobil Operasional {runId} - 1` (Draft) dan baris `Printer Laser {runId} - 1` (Waiting for Approval) tidak tampil di tabel All Assets
4. Verifikasi baris `Server Rack {runId} - 1` (Deleted) tidak tampil di tabel All Assets
5. Verifikasi baris `Laptop Pro 16 {runId} - 1` menampilkan `Available` saja tanpa badge status lain
6. Klik ikon Filter
7. Buka opsi Status pada panel Filter
8. Verifikasi opsi Status memuat `Borrowed` dan `Damaged`
9. Verifikasi opsi Status tidak memuat dimensi Lifecycle, yaitu tidak ada opsi `Active`, `Disposed`, `Draft`, `Waiting for Approval`, maupun `Deleted`
10. Tutup panel Filter
11. Klik tab `Registration`
12. Verifikasi tab `Registration` memuat `Mobil Operasional {runId} - 1` dan `Printer Laser {runId} - 1`

### Registrasi disetujui memunculkan aset di daftar
13. Klik tab `Assets`
14. Ketik Search `Printer Laser {runId}`, tekan Enter
15. Verifikasi tabel tidak memuat baris `Printer Laser {runId} - 1`
16. Pada modul Asset Registration, Approver menyetujui registrasi aset `Printer Laser {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
17. Verifikasi baris `Printer Laser {runId} - 1` muncul di tabel All Assets dengan Lifecycle `Active`

### Deleted tidak tampil di tab Registration dan kartu Disposed
18. Klik tab `Registration`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi tab `Registration` tidak memuat `Server Rack {runId} - 1` (Deleted)
21. Klik tab `Assets`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi angka kartu `Disposed` menjadi `0` karena aset Draft, Waiting for Approval, dan Deleted tidak dihitung sebagai Disposed
