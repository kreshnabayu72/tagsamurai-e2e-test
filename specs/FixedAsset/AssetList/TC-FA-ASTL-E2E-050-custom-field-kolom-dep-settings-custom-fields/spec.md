---
id: TC-FA-ASTL-E2E-050-custom-field-kolom-dep-settings-custom-fields
title: "Custom field tercermin di kolom"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#r10"]
smoke: []
dependsOn: ["Settings Custom Fields: custom field"]
trace:
  "§9.7#r10": [6, 8, 10, 12]
anchor: [3]
coverage:
  web: automated
---

# Custom field tercermin di kolom

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-050-1: aset `Printer Laser {runId} - 1`, Group `GA`, custom field General `Nomor Kontrak {runId}` bernilai `KTR-01-{runId}`.
  - DU-050-3: nilai custom field hasil ubah `KTR-02-{runId}` pada aset `Printer Laser {runId} - 1`.

## Test Steps

### Custom field tercermin sebagai kolom
1. Ketik Search `Printer Laser {runId}`, tekan Enter
2. Buka Setup Column
3. Verifikasi Setup Column memuat opsi kolom `Nomor Kontrak {runId}`
4. Centang `Nomor Kontrak {runId}`
5. Tutup Setup Column
6. Verifikasi kolom `Nomor Kontrak {runId}` baris `Printer Laser {runId} - 1` menampilkan `KTR-01-{runId}`
7. Pada Settings Custom Fields, Hendra Saputra mengubah nama custom field `Nomor Kontrak {runId}` menjadi `Nomor Kontrak Baru {runId}`, tanpa memuat ulang halaman Fixed Asset > Assets
8. Verifikasi header kolom custom field berubah menjadi `Nomor Kontrak Baru {runId}` dan baris `Printer Laser {runId} - 1` tetap menampilkan `KTR-01-{runId}`

### Nilai custom field dan field yang tidak tersedia tercermin di kolom
9. Pada Settings Custom Fields, Hendra Saputra mengubah nilai custom field `Nomor Kontrak Baru {runId}` pada aset `Printer Laser {runId} - 1` menjadi `KTR-02-{runId}`, tanpa memuat ulang halaman Fixed Asset > Assets
10. Verifikasi header kolom tetap `Nomor Kontrak Baru {runId}` dan kolom itu baris `Printer Laser {runId} - 1` menampilkan `KTR-02-{runId}`
11. Pada Settings Custom Fields, Hendra Saputra menghapus custom field `Nomor Kontrak Baru {runId}`, tanpa memuat ulang halaman Fixed Asset > Assets
12. Verifikasi kolom `Nomor Kontrak Baru {runId}` tidak tampil pada tabel dan tidak ada sebagai opsi di Setup Column
