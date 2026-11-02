---
id: TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes
title: "Alert Group Consolidation Popup: Tutup via (X) dan Esc, Klik Backdrop Tidak Menutup, serta Dialog Unsaved Changes Saat Ada Perubahan Centang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1116
  - TC-FA-GRP-1124
  - TC-FA-GRP-1125
  - TC-FA-GRP-1126
coverage:
  web: automated
---

# Alert Group Consolidation Popup: Tutup via (X) dan Esc, Klik Backdrop Tidak Menutup, serta Dialog Unsaved Changes Saat Ada Perubahan Centang

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Alert (plan Growth; client punya 5 group dengan status Excess sesuai blok; email dan `Spectra.env.FA_ALERT_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed ulang oleh fixture BE di `before`): cap plan berlaku 3, client punya 5 group (2 berstatus Excess), Alert Group Consolidation tampil.
- State tenant (kelas h): cap plan dan status Excess diatur per blok oleh fixture BE (disediakan tim FE/BE); plan, cap, dan status Excess dipulihkan di hook `after`. Suite berjalan serial.
- Cleanup di `after`: pulihkan keadaan lewat fixture BE.

## Test Steps

### TC-FA-GRP-1124: Tutup lewat [X] dan Esc tanpa perubahan centang

1. Klik [Choose Groups]
2. Klik [X] di header popup
3. Verifikasi popup tertutup tanpa dialog Unsaved changes
4. Klik [Choose Groups] lagi
5. Tekan Esc
6. Verifikasi popup tertutup tanpa dialog Unsaved changes
7. Verifikasi status Excess tidak berubah
8. Verifikasi Alert Group Consolidation tetap tampil

### TC-FA-GRP-1126: Klik backdrop tidak menutup popup

9. Klik [Choose Groups]
10. Verifikasi popup terbuka
11. Klik backdrop di luar popup
12. Verifikasi popup tetap terbuka
13. Verifikasi tidak ada dialog Unsaved changes
14. Centang 2 group
15. Klik backdrop di luar popup
16. Verifikasi popup tetap terbuka
17. Verifikasi tidak ada dialog Unsaved changes
18. Verifikasi 2 centang tetap dipertahankan

### TC-FA-GRP-1116: [Cancel] setelah mengubah centang memunculkan dialog Unsaved changes

19. Klik [Cancel] (popup masih terbuka dengan 2 centang dari TC-1126)
20. Verifikasi dialog tanpa title "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
21. Klik [Cancel] pada dialog
22. Verifikasi dialog tertutup dan popup tetap terbuka dengan 2 centang dipertahankan
23. Klik [Cancel] lagi
24. Klik [Leave]
25. Verifikasi popup tertutup
26. Verifikasi status Excess tidak berubah
27. Verifikasi Alert Group Consolidation tetap tampil

### TC-FA-GRP-1125: [X] dan Esc setelah mengubah centang memunculkan dialog Unsaved changes

28. Klik [Choose Groups]
29. Centang 2 group
30. Klik [X] di header popup
31. Verifikasi dialog tanpa title "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
32. Klik [Cancel] pada dialog
33. Verifikasi popup tetap terbuka dengan 2 centang dipertahankan
34. Tekan Esc pada popup
35. Verifikasi dialog tanpa title "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
36. Klik [Leave] pada dialog
37. Verifikasi popup tertutup dan centang dibuang
38. Verifikasi status Excess tidak berubah
39. Verifikasi Alert Group Consolidation tetap tampil

## Notes

- Urutan: tutup tanpa perubahan (TC-1124), backdrop (TC-1126) yang menyisakan popup terbuka dengan 2 centang, lalu TC-1116 yang melanjutkan keadaan itu (tanpa mengulang membuka popup dan mencentang), lalu TC-1125. Asersi popup tetap terbuka pada TC-1126 didahului verifikasi popup terbuka (anchor, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: empat TC satu surface (popup Alert Group Consolidation) dan satu dataset, tiap blok berdiri sendiri dan menutup popup lewat jalur berbeda; `Verifikasi` dialog dan status dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-1116 Langkah 3 mencentang 2 group; spec melanjutkan 2 centang dari TC-1126 yang sama dengan langkah TC-1116 (state popup terbuka tidak berubah), sehingga langkah "Centang 2 group" TC-1116 tidak diulang.
  - TC-1125 Expected c menyebut centang dibuang tanpa langkah observasi di TC; spec mengasersi pada satu `Verifikasi` bersama popup tertutup.
