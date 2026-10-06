---
id: TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3
title: "Setup Column Tab Total Control: Screening Overlay, Popup Modal Visibilitas, Urutan, Pin Kolom, dan Reset/Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-183
  - TC-GS-ROLE-201
  - TC-GS-ROLE-202
  - TC-GS-ROLE-203
  - TC-GS-ROLE-250
  - TC-GS-ROLE-251
  - TC-GS-ROLE-252
  - TC-GS-ROLE-253
  - TC-GS-ROLE-254
  - TC-GS-ROLE-255
  - TC-GS-ROLE-256
  - TC-GS-ROLE-258
  - TC-GS-ROLE-259
  - TC-GS-ROLE-260
  - TC-GS-ROLE-261
  - TC-GS-ROLE-263
  - TC-GS-ROLE-264
  - TC-GS-ROLE-265
  - TC-GS-ROLE-266
  - TC-GS-ROLE-267
  - TC-GS-ROLE-268
  - TC-GS-ROLE-270
  - TC-GS-ROLE-271
  - TC-GS-ROLE-272
  - TC-GS-ROLE-273
  - TC-GS-ROLE-275
  - TC-GS-ROLE-276
  - TC-GS-ROLE-277
  - TC-GS-ROLE-278
  - TC-GS-ROLE-279
  - TC-GS-ROLE-280
  - TC-GS-ROLE-282
  - TC-GS-ROLE-283
  - TC-GS-ROLE-284
  - TC-GS-ROLE-285
  - TC-GS-ROLE-287
  - TC-GS-ROLE-288
coverage:
  web: automated
---

# Setup Column Tab Total Control: Screening Overlay, Popup Modal Visibilitas, Urutan, Pin Kolom, dan Reset/Cancel

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka Tab Total Control
2. Klik icon Setup Column pada toolbar untuk membuka Quick Overlay (Fase 1)
3. Verifikasi daftar kolom tampil dengan toggle checkbox dan handle drag
4. Klik link 'More Options' untuk membuka Modal Penuh Setup Column (Fase 2)
5. Verifikasi modal menampilkan 10 baris kolom data yang dapat diatur
6. Uncheck kolom Division pada modal
7. Verifikasi pada live preview tabel kolom Division disembunyikan
8. Tarik (drag) kolom Status ke urutan paling atas
9. Verifikasi urutan kolom ter-update pada live preview tabel
10. Klik icon pin pada kolom Name untuk mengunci posisinya
11. Verifikasi kolom Name terkunci (pinned) di sisi kiri tabel
12. Coba uncheck seluruh kolom hingga tersisa 1 kolom
13. Verifikasi guard minimal 1 kolom terlihat: checkbox kolom terakhir dinonaktifkan (disabled)
14. Klik tombol [Reset to Default] (Fase 3)
15. Verifikasi seluruh pengaturan kolom kembali ke posisi dan visibilitas default bawaan sistem
16. Ubah kembali salah satu kolom lalu klik tombol [Cancel]
17. Verifikasi modal tertutup dan perubahan terakhir dibatalkan tanpa tersimpan

## Notes

- Setup Column menerapkan model Hideable-only dengan guard minimal 1 kolom terlihat (prd-conventions §9.3).
