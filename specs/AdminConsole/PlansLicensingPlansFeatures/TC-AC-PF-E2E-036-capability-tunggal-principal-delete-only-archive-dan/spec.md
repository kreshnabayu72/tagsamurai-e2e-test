---
id: TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan
title: Capability Tunggal Principal Delete-Only - Archive dan Delete Custom Plan dan Default Plan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-82
  - TC-AC-PF-83
  - TC-AC-PF-86
  - TC-AC-PF-87
coverage:
  web: automated
---

# Capability Tunggal Principal Delete-Only - Archive dan Delete Custom Plan dan Default Plan

## Prerequisites

- Mode: FE+BE
- Akun aktor: #5 `deleteOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (Delete-Only, Principal: Manage plans & licensing Read dan Delete; password dari env `AC_PF_DO_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup yang diubah (pengecualian S-06/S-12 butir A-14): custom plan `Paket Tanpa Client` aktif tanpa subscription (Dataset Plan G, di-archive), default `Enterprise` aktif tanpa subscription (Dataset Plan Y, di-archive), custom archived `Arsip Custom Satu` tidak pernah dipakai (Dataset Plan C, dihapus permanen), default archived `Plan Arsip Lama` tidak pernah dipakai (Dataset Plan R, dihapus permanen). Pemulihan semua Dataset ke keadaan awal dijamin fixture backend (disediakan tim FE/BE, idempoten, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 8, 16, dan 24). Efek di Pre-setup: Last Updated dan entri Changelog (Default dan Custom) bertambah permanen dan tidak dipulihkan. Aksi Delete dijalankan sesudah aksi Archive.
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk pemulihan Dataset Plan C, G, R, dan Y. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: status archived dan keberadaan record plan Pre-setup serta slot default plan FAMS; suite berjalan serial (`parallel: false`); dipulihkan di hook `after`.

## Test Steps

### TC-AC-PF-82: Archive custom plan

1. Klik tab Custom.
2. Buka Overlay Row Action pada `Paket Tanpa Client`.
3. Klik `Archive`.
4. Klik `[Archive]` pada dialog `Archive Plan`.
5. Verifikasi muncul toast sukses: "Success, plan has been archived."
6. Klik sub-tab Archive.
7. Verifikasi `Paket Tanpa Client` tampil di sub-tab Archive.
8. Pulihkan `Paket Tanpa Client` ke status aktif lewat fixture BE.

### TC-AC-PF-86: Archive default plan

9. Klik tab Default.
10. Buka Overlay Row Action pada `Enterprise`.
11. Klik `Archive`.
12. Klik `[Archive]` pada dialog `Archive Plan`.
13. Verifikasi muncul toast sukses: "Success, plan has been archived."
14. Klik sub-tab Archive.
15. Verifikasi `Enterprise` tampil di Default > Archive.
16. Pulihkan `Enterprise` ke status aktif lewat fixture BE.

### TC-AC-PF-83: Delete custom plan archived

17. Klik tab Custom.
18. Klik sub-tab Archive.
19. Buka Overlay Row Action pada `Arsip Custom Satu`.
20. Klik `Delete`.
21. Klik `[Delete]` pada dialog `Delete Plan`.
22. Verifikasi muncul toast sukses: "Success, plan has been permanently deleted."
23. Verifikasi `Arsip Custom Satu` tidak ada lagi di sub-tab Archive.
24. Pulihkan `Arsip Custom Satu` lewat fixture BE.

### TC-AC-PF-87: Delete default plan archived

25. Klik tab Default.
26. Klik sub-tab Archive.
27. Buka Overlay Row Action pada `Plan Arsip Lama`.
28. Klik `Delete`.
29. Klik `[Delete]` pada dialog `Delete Plan`.
30. Verifikasi muncul toast sukses: "Success, plan has been permanently deleted."
31. Verifikasi `Plan Arsip Lama` tidak ada lagi di Default > Archive.

## Notes

- Langkah penghubung (S-03): langkah 1, 6, 9, 14, 17, 18, 25, 26 (pindah tab dan sub-tab), langkah 8, 16, 24 (pemulihan Dataset lewat fixture BE, A-6).
- Urutan TC: TC-AC-PF-86 dijalankan sebelum TC-AC-PF-83 dan TC-AC-PF-87 agar aksi Delete berada di akhir (S-10).
- Langkah 5 dan 13 adalah anchor positif (toast sukses) untuk langkah 7 dan 15; langkah 22 dan 30 adalah anchor untuk langkah 23 dan 31 (absence baris sesudah Delete).
- Temuan untuk QA:
  - TC-AC-PF-82 dan TC-AC-PF-86 sama-sama mengubah slot default plan dan custom plan Pre-setup yang dipakai spec lain; pemulihan memakai fixture BE (kemampuannya tidak tertulis di TC, PRD, atau LLD).
  - Post Condition status archived dan record terhapus (TC-AC-PF-82, 83, 86, 87) sudah punya padanan Expected; Post Condition lain tanpa langkah observasi tidak diasersi (S-01).
