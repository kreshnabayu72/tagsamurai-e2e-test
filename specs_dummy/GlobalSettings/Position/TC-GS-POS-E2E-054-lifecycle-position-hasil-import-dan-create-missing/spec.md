---
id: TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing
title: "Lifecycle & Parity: Position hasil Import Type Position (Edit, Delete in-use guard, Delete sukses) dan Create Missing Positions"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-275
  - TC-GS-POS-276
  - TC-GS-POS-277
  - TC-GS-POS-295
coverage:
  web: automated
---

# Lifecycle & Parity: Position hasil Import Type Position (Edit, Delete in-use guard, Delete sukses) dan Create Missing Positions

## Prerequisites

- Record hasil Import Type Position tersedia di database: "Sales Coordinator" (dipakai user Hendra Gunawan) dan "Field Technician" (bebas relasi)

## Test Steps

### Parity Operasional Record Hasil Import

1. Buka tab Position
2. Buka menu ⋯ pada record "Field Technician" (hasil import), klik "Edit"
3. Ubah nama menjadi "Senior Field Technician", simpan, verifikasi update berhasil identik record manual
4. Buka menu ⋯ pada "Sales Coordinator" (hasil import yang dipakai user Hendra Gunawan), klik "Delete"
5. Verifikasi guard in-use tetap ditegakkan: muncul dialog "Cannot Delete Data"
6. Buka menu ⋯ pada "Senior Field Technician" (bebas relasi), klik "Delete"
7. Konfirmasi penghapusan, verifikasi record berhasil dihapus

### Perilaku Fitur [Create Missing Positions]

8. Jalankan simulasi alur [Create Missing Positions] saat import user mendeteksi jabatan belum ada
9. Verifikasi jabatan yang belum ada otomatis ditambahkan ke master data Position
10. Coba jalankan [Create Missing Positions] dengan nama jabatan yang sudah ada di sistem
11. Verifikasi sistem menolak duplikasi dan tidak membuat record ganda

## Notes

- Menggabungkan lifecycle record import dan create missing positions dari TC-GS-POS-275, 276, 277, dan 295.
