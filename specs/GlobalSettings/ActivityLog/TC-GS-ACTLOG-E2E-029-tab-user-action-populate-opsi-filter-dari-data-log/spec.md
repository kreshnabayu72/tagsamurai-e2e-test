---
id: TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log
title: "Tab User Action: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-138
  - TC-GS-ACTLOG-139
  - TC-GS-ACTLOG-140
  - TC-GS-ACTLOG-142
  - TC-GS-ACTLOG-143
  - TC-GS-ACTLOG-144
coverage:
  web: automated
---

# Tab User Action: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan subset data changelog aktif

## Test Steps

1. Buka Filter Panel pada Tab User Action
2. Buka dropdown Action saat opsi sedang di-fetch dan verifikasi indikator skeleton/loading tampil
3. Amati daftar opsi dropdown Action saat log entitas ini baru memuat Create, Edit, dan Delete
4. Verifikasi dropdown Action hanya memuat Create, Edit, dan Delete, sementara aksi lain (mis. Combine) tidak muncul jika belum pernah terjadi
5. Buka dropdown Object dan verifikasi hanya memuat Object yang genuinely pernah dicatat di log entitas ini
6. Buka dropdown Modified By dan verifikasi hanya admin yang pernah beraksi yang muncul di opsi
7. Terapkan filter Modified By = "Admin A", simulasikan akun "Admin A" dihapus oleh sistem
8. Verifikasi filter tetap berjalan sebagai snapshot dan entri lama milik "Admin A" tetap tampil di tabel

## Notes

- Enum Action dan Object di API berjumlah banyak, namun dropdown UI hanya menyajikan opsi yang pernah muncul di data historis entitas.
