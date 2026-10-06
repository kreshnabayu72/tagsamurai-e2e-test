---
id: TC-GS-POS-E2E-042-pencatatan-mutasi-tiga-surface
title: Pencatatan Mutasi Position di Tiga Surface Logging
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-46
  - TC-GS-POS-48
  - TC-GS-POS-49
  - TC-GS-POS-50
  - TC-GS-POS-51
  - TC-GS-POS-52
coverage:
  web: automated
---

# Pencatatan Mutasi Position di Tiga Surface Logging

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia tiga surface audit: Changelog, System Log, Activity Log.
- Logging terikat dalam transaksi (jika relevan) untuk operasi Create/Edit/Delete.

## Test Steps

### A. Create Position

1. Catat jumlah entri log pada Changelog, System Log, Activity Log sebelum operasi.
2. Buat Position baru via `[+ Position]` (nama unik).
3. Verifikasi toast sukses muncul.
4. Verifikasi entri log bertambah pada Changelog, System Log, Activity Log (1 transaksi, detail sesuai baseline logging).
5. Verifikasi isi log Create sesuai struktur (Action=Create, Name, Field, Old/New Value, Modified By).

### B. Edit Position

6. Catat jumlah log sebelum edit.
7. Edit nama Position yang baru dibuat.
8. Verifikasi toast sukses.
9. Verifikasi entri log bertambah di ketiga surface untuk operasi Edit (Old Value/New Value terisi, Field=Name).
10. Verifikasi detail log konsisten lintas surface.

### C. Delete Position

11. Catat jumlah log sebelum delete.
12. Hapus Position tersebut (single delete).
13. Verifikasi toast sukses.
14. Verifikasi entri log bertambah di ketiga surface untuk operasi Delete (format dash `—` sesuai konvensi Changelog).
15. Verifikasi jumlah & isi log sesuai ekspektasi dan tidak ada logging partial yang terlewat.

## Notes

- Pencatatan wajib di ketiga surface untuk setiap mutasi (Create/Edit/Delete) sesuai POS-06.
- Detail lengkap mengacu TC-GS-POS-48 (baseline logging dalam 1 transaksi).
