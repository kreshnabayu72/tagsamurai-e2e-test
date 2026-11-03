---
id: TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push
title: Capability Tunggal Principal Update-Only - Edit Custom Plan, Rename Default Plan, Push Update, dan Save Global Settings
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-81
  - TC-AC-PF-85
  - TC-AC-PF-88
  - TC-AC-PF-89
coverage:
  web: automated
---

# Capability Tunggal Principal Update-Only - Edit Custom Plan, Rename Default Plan, Push Update, dan Save Global Settings

## Prerequisites

- Mode: FE+BE
- Akun aktor: #4 `updateOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (Update-Only, Principal: Manage plans & licensing Read dan Update; Group Role Manage active client CRUD; password dari env `AC_PF_UO_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup yang diubah (pengecualian S-06/S-12 butir A-14): Dataset Plan A (`Growth Tier` v20 dengan Group count 25 diedit menjadi 3 sehingga menjadi v21; default `Enterprise` v1 di-rename menjadi `Enterprise Plus`), Dataset Plan P (`Paket Push` v3 dengan client `PT Push Satu` Active v1 dan aktor memiliki Update pada group client target), Global Settings (Max custom fields per asset name 5 dan Max depreciation methods 2, diubah menjadi 8). Pemulihan semua Dataset ke keadaan awal dijamin fixture backend (disediakan tim FE/BE, idempoten, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 8, 17, 28, dan 34). Efek di Pre-setup: Last Updated dan entri Changelog (Default, Custom, Global Settings) bertambah permanen dan tidak dipulihkan.
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk pemulihan Dataset Plan A, Dataset Plan P, dan Global Settings. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: Global FAMS Settings (singleton) dan versi plan Pre-setup; suite berjalan serial (`parallel: false`); dipulihkan di hook `after`.

## Test Steps

### TC-AC-PF-81: Edit nilai fitur custom plan

1. Klik tab Custom.
2. Buka Overlay Row Action pada `Growth Tier`.
3. Klik `Edit`.
4. Ubah Group count dari `25` ke `3`.
5. Klik `[Save]`.
6. Verifikasi muncul toast sukses: "Success, plan has been updated."
7. Verifikasi Plan Detail `Growth Tier` menampilkan `Growth Tier – v21`.
8. Pulihkan `Growth Tier` ke v20 lewat fixture BE.

### TC-AC-PF-85: Rename default plan

9. Kembali ke list lewat Breadcrumb.
10. Klik tab Default.
11. Buka Overlay Row Action pada `Enterprise`.
12. Klik `Edit`.
13. Ubah Plan Name menjadi `Enterprise Plus`.
14. Klik `[Save]`.
15. Verifikasi muncul toast sukses: "Success, plan has been updated."
16. Verifikasi judul Plan Detail `Enterprise Plus – v1` (versi tidak naik).
17. Pulihkan Plan Name `Enterprise` lewat fixture BE.

### TC-AC-PF-88: Push Update ke client eligible

18. Kembali ke list lewat Breadcrumb.
19. Klik tab Custom.
20. Buka Plan Detail `Paket Push`.
21. Klik Tab Assigned Clients.
22. Buka Overlay Row Action pada `PT Push Satu`.
23. Klik `Push Update`.
24. Klik `[Push Update]` pada dialog `Push Plan Update`.
25. Verifikasi muncul toast sukses: "Success, plan update has been pushed."
26. Verifikasi kolom Plan Version `PT Push Satu` menampilkan versi terbaru.
27. Verifikasi kolom Plan Version `PT Push Satu` tanpa badge `Outdated`.
28. Pulihkan `PT Push Satu` ke v1 lewat fixture BE.

### TC-AC-PF-89: Save Global Settings

29. Kembali ke list lewat Breadcrumb.
30. Klik tab Global Settings.
31. Ubah Max custom fields per asset name dari `5` menjadi `8`.
32. Klik `[Save]`.
33. Verifikasi muncul toast sukses: "Success, global FAMS settings has been saved."
34. Pulihkan Max custom fields per asset name ke `5` lewat fixture BE.

## Notes

- Langkah penghubung (S-03): langkah 1, 10, 19, 30 (pindah tab), langkah 9, 18, 29 (kembali ke list), langkah 8, 17, 28, 34 (pemulihan Dataset lewat fixture BE, A-6).
- Langkah 23 dan 24 menjalankan Push Update yang diakses dari baris client; hasil di Changelog tidak diasersi karena TC tidak memintanya.
- Temuan untuk QA:
  - TC-AC-PF-81 Expected b menyebut versi `v21` untuk `Growth Tier`, dan Pre-setup #21 menyebut `Growth Tier` v20; nilai Group count awal `25` tidak tertulis di Pre-setup #21 maupun #23. Spec mengikuti TC (langkah 4).
  - Post Condition TC-AC-PF-81, 85, 88, dan 89 yang tidak punya padanan Expected (entri Changelog Edit, Plan Name, versi plan term live, nilai Max custom fields) tanpa langkah observasi tidak diasersi (S-01).
