---
id: TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5
title: "Tab User Action: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-179
  - TC-GS-ACTLOG-180
  - TC-GS-ACTLOG-181
  - TC-GS-ACTLOG-182
  - TC-GS-ACTLOG-183
  - TC-GS-ACTLOG-184
  - TC-GS-ACTLOG-185
  - TC-GS-ACTLOG-186
coverage:
  web: automated
---

# Tab User Action: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab User Action
2. Drag baris kolom Date ke urutan ketiga
3. Drag baris kolom Action ke urutan pertama
4. Drag baris kolom Object, Name, Field, Old Value, New Value, dan Modified By ke posisi kustom
5. Verifikasi urutan kolom pada Live Preview langsung berubah mengikuti hasil drag
6. Klik tombol `[Save]`
7. Verifikasi urutan kolom pada tabel utama Tab User Action berubah sesuai susunan baru
8. Lakukan refresh halaman browser (F5)
9. Verifikasi urutan kolom kustom tetap bertahan (persist) setelah refresh

## Notes

- Pengaturan urutan kolom disimpan di local storage per sub-modul tab.
