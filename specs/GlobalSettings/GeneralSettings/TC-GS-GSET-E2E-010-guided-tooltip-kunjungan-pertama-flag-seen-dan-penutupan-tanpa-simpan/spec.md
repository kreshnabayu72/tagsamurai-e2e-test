---
id: TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan
title: "Trigger, flag, penutupan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-14
  - TC-GS-GSET-17
  - TC-GS-GSET-146
  - TC-GS-GSET-147
coverage:
  web: automated
---

# Trigger, flag, penutupan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Pre-setup No 8 menyebut Total Control baru tanpa flag; email akun itu tidak tertulis di Pre-setup TC, sehingga spec memakai akun No 1 dengan flag dihapus.
- Guided Tooltip: spec ini mengecualikan hook suite untuk flag `guided_tooltip_seen_gs-general-settings` (page_key `gs-general-settings`, PRD §4.7). Hook `before` spec mencatat nilai awal flag akun aktor lalu menyetelnya true (agar pembukaan halaman di `beforeEach` suite tidak memunculkan walkthrough); hook `after` memulihkan nilai awal walau spec gagal di tengah. Flag dihapus ("belum ada") oleh langkah eksplisit sebelum tiap TC. Kemampuan menghapus dan membaca flag lewat API disediakan tim FE/BE (nama endpoint tidak disebut di TC, PRD, atau LLD).
- Kemampuan teknis: mengubah ukuran viewport browser saat walkthrough berjalan (TC-GS-GSET-147): lebar awal 1280 px diubah menjadi 1024 px dan dipulihkan di langkah 36 (hook `after` sebagai cadangan); klik area overlay gelap; muat ulang halaman (F5).
- Data Pre-setup No 10 (record Client A, hanya dibaca). Spec tidak menekan `[Save]`.
- State global yang diubah: flag Guided Tooltip akun aktor dan ukuran viewport (dipulihkan seperti di atas).

## Test Steps

### TC-GS-GSET-14: Trigger kunjungan pertama dan flag seen setelah Skip

1. Hapus flag `guided_tooltip_seen_gs-general-settings` akun aktor lewat API sehingga flag belum ada
2. Muat ulang halaman Global Settings > General Settings (F5) untuk kunjungan pertama
3. Verifikasi walkthrough otomatis muncul dari Step 1
4. Klik `[Skip]`
5. Verifikasi walkthrough tertutup
6. Verifikasi flag `guided_tooltip_seen_gs-general-settings` tersimpan (true, dibaca lewat API)
7. Keluar ke Global Settings > Activity Log
8. Buka kembali Global Settings > General Settings
9. Verifikasi Select "Currency Code" tampil
10. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-GSET-17: Penutupan saat navigasi keluar tanpa menyimpan flag

11. Hapus flag `guided_tooltip_seen_gs-general-settings` akun aktor lewat API sehingga flag belum ada
12. Muat ulang halaman Global Settings > General Settings (F5)
13. Verifikasi walkthrough Step 1 tampil
14. Navigasi ke Global Settings > Activity Log
15. Verifikasi halaman Activity Log tampil
16. Verifikasi walkthrough tertutup
17. Verifikasi flag `guided_tooltip_seen_gs-general-settings` belum tersimpan (dibaca lewat API)
18. Kembali ke Global Settings > General Settings
19. Verifikasi walkthrough muncul lagi otomatis dari Step 1

### TC-GS-GSET-146: Klik overlay gelap setara Skip

20. Klik area overlay gelap di luar tooltip (walkthrough Step 1 dari langkah 19 masih tampil)
21. Verifikasi walkthrough tertutup
22. Verifikasi flag `guided_tooltip_seen_gs-general-settings` tersimpan (true, dibaca lewat API)
23. Keluar ke Global Settings > Activity Log
24. Buka kembali Global Settings > General Settings
25. Verifikasi Select "Currency Code" tampil
26. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-GSET-147: Penutupan saat viewport di-resize tanpa menyimpan flag

27. Hapus flag `guided_tooltip_seen_gs-general-settings` akun aktor lewat API sehingga flag belum ada
28. Muat ulang halaman Global Settings > General Settings (F5)
29. Verifikasi walkthrough Step 1 tampil
30. Ubah lebar viewport browser dari 1280 px menjadi 1024 px
31. Verifikasi walkthrough tertutup
32. Verifikasi flag `guided_tooltip_seen_gs-general-settings` belum tersimpan (dibaca lewat API)
33. Keluar ke Global Settings > Activity Log
34. Buka kembali Global Settings > General Settings
35. Verifikasi walkthrough muncul lagi otomatis dari Step 1
36. Pulihkan lebar viewport browser menjadi 1280 px

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 36 langkah, hampir pada batas sekitar 35 langkah; alasan: satu kelas (Guided Tooltip trigger dan penutupan), empat blok berdiri sendiri yang masing-masing menghapus flag di awal, dan tiap blok memuat siklus "keluar lalu buka kembali" yang diwajibkan TC.
- Dipisah dari spec 009 karena gabungan langkahnya melewati batas ukuran jauh (36 + 35 = 71 langkah, tanpa langkah berulang sehingga ekspansi sama); spec ini memuat TC-GS-GSET-14, 17, 146, dan 147 (trigger kunjungan pertama dan penutupan tanpa menyimpan flag), spec 009 memuat TC-GS-GSET-15, 16, dan 18 (konten, navigasi, dan keyboard walkthrough).
- Pecahan Expected: TC-GS-GSET-14 a menjadi langkah 3, b menjadi langkah 5 dan 6, c menjadi langkah 10; TC-GS-GSET-17 a menjadi langkah 16 dan 17, b menjadi langkah 19; TC-GS-GSET-146 a menjadi langkah 21 dan 22, b menjadi langkah 26; TC-GS-GSET-147 a menjadi langkah 31 dan 32, b menjadi langkah 35.
- TC-GS-GSET-146 langkah 1 dan 2 (Buka General Settings, tunggu Step 1) dipenuhi langkah 19 (walkthrough Step 1 dari TC-GS-GSET-17 tampil dan flag belum ada); precondition "flag belum ada" TC-GS-GSET-146 terpenuhi oleh langkah 17.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 11, 27 (reset flag) dan langkah 36 (memulihkan viewport).
- Anchor `Verifikasi` (bukan langkah penghubung): langkah 9 dan 25 (Select "Currency Code" tampil, anchor halaman termuat sebelum asersi absence walkthrough langkah 10 dan 26) dan langkah 15 (halaman Activity Log tampil, anchor sebelum asersi walkthrough tertutup langkah 16).
- Asersi tambahan di luar Expected (S-03): langkah 15 mengasersi halaman Activity Log tampil; Expected TC-GS-GSET-17 hanya menyebut walkthrough tertutup dan flag belum tersimpan, dan asersi ini dipakai sebagai anchor positif absence.
- Verifikasi flag lewat API (langkah 6, 17, 22, dan 32) dipakai karena Expected menyatakan flag `seen` tersimpan atau tidak tersimpan; kemampuan membacanya disediakan tim FE/BE.
- Temuan untuk QA:
  - Mekanisme menghapus dan membaca flag `seen` tidak ada di TC, PRD, atau LLD (Q-10); ditulis sebagai kemampuan "disediakan tim FE/BE" tanpa endpoint.
  - TC-GS-GSET-147 langkah 2 ("ubah ukuran viewport browser") tidak menyebut ukuran. Spec memakai 1280 px ke 1024 px (data uji, bukan aturan PRD); QA perlu menegaskan.
  - TC-GS-GSET-14 langkah 4 menyebut "Keluar ke menu lain" tanpa menyebut menu; spec memakai Global Settings > Activity Log, sama dengan TC-GS-GSET-17.
  - Email akun Total Control baru (Pre-setup No 8) tidak tertulis; spec memakai akun No 1 dengan flag dihapus.
