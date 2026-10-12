---
id: TC-GS-BRAND-E2E-007-guided-tooltip-konten-navigasi-keyboard
title: "Konten dan Navigasi Keyboard Guided Tooltip Tab Brand"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-19
  - TC-GS-BRAND-22
  - TC-GS-BRAND-25
  - TC-GS-BRAND-26
coverage:
  web: automated
---

# Konten dan Navigasi Keyboard Guided Tooltip Tab Brand

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor yang dimodelkan lewat payload izin mock:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` untuk TC-GS-BRAND-19, TC-GS-BRAND-22, dan TC-GS-BRAND-25.
  - Read Only Client A (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` untuk TC-GS-BRAND-26.
  - Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD` dan `Spectra.env.GS_RO_PASSWORD`.
- Kebutuhan mock (respons yang dipaksa):
  - Respons sesi/profil dan payload izin: Total Control (semua aksi Brand) dan Read Only (hanya baca; `[+ Brand]` Hidden).
  - Respons daftar Brand: minimal 10 baris sehingga `#brand-table-toolbar` dan `#brand-table` ter-render.
  - Respons preferensi Guided Tooltip untuk flag `guided_tooltip_seen_gs-brand`: belum ada (TC-GS-BRAND-19; penyimpanan flag oleh [Skip] tidak mengubah respons selama TC itu), true (TC-GS-BRAND-22, TC-GS-BRAND-25, TC-GS-BRAND-26).
- Tidak ada data backend atau state global yang diubah, sehingga tidak ada cleanup selain melepas mock di hook `after`.

## Test Steps

### TC-GS-BRAND-19: Konten 3 step Guided Tooltip tab Brand sesuai urutan

1. Terapkan mock sesi Total Control dengan flag `guided_tooltip_seen_gs-brand` belum ada
2. Buka Global Settings > Master Reference > Brand → walkthrough otomatis tampil karena flag belum ada
3. Klik [Skip] untuk menutup walkthrough otomatis
4. Klik `[?]` di Breadcrumb
5. Baca Step 1
6. Verifikasi Step 1 menyorot `#brand-table-toolbar`
7. Verifikasi Step 1 Title `Table Tools`
8. Verifikasi Step 1 Description `Search, filter, and manage brand master data from here — available actions depend on your access level.`
9. Verifikasi `[Back]` Hidden pada Step 1
10. Klik [Next]
11. Baca Step 2
12. Verifikasi Step 2 menyorot kontainer tabel (`#brand-table`)
13. Verifikasi Step 2 Title `Used By (Items)`
14. Verifikasi Step 2 Description `Each row shows how many items use that brand. Click the number to see the details.`
15. Klik [Next]
16. Baca Step 3
17. Verifikasi Step 3 menyorot icon Changelog
18. Verifikasi Step 3 Title `Changelog Audit`
19. Verifikasi Step 3 Description `Review the history of changes made to brands.`
20. Verifikasi `[Next]` berganti `[Done]` pada Step 3
21. Klik [Done] untuk menutup walkthrough

### TC-GS-BRAND-22: Tombol [?] memulai ulang walkthrough tanpa mereset flag

22. Terapkan mock flag `guided_tooltip_seen_gs-brand` = true lalu muat ulang tab Brand
23. Klik `[?]`
24. Verifikasi walkthrough mulai dari Step 1
25. Klik [Next]
26. Klik [Back]
27. Verifikasi [Back] kembali ke Step 1
28. Klik [Next]
29. Klik [Next]
30. Klik [Done]
31. Verifikasi [Done] menutup walkthrough
32. Muat ulang halaman
33. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-GS-BRAND-25: Keyboard pada walkthrough: panah kanan, panah kiri, Enter, Esc

34. Klik `[?]`
35. Tekan panah kanan
36. Verifikasi panah kanan berpindah ke Step 2
37. Tekan panah kiri
38. Verifikasi panah kiri kembali ke Step 1
39. Tekan Enter
40. Verifikasi Enter berpindah ke Step 2
41. Tekan Esc
42. Verifikasi Esc menutup walkthrough

### TC-GS-BRAND-26: Step Guided Tooltip tetap 3 step untuk Read Only

43. Ganti mock sesi ke Read Only (flag tetap true) lalu buka Global Settings > Master Reference > Brand
44. Klik `[?]`
45. Verifikasi Step 1 menyorot Table Tools
46. Verifikasi `[+ Brand]` Hidden pada Table Tools
47. Klik [Next]
48. Verifikasi Step 2 menyorot kontainer tabel Brand
49. Klik [Next]
50. Verifikasi Step 3 tampil dengan `[Done]` sehingga total walkthrough 3 step
51. Klik [Done] untuk menutup walkthrough

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-BRAND-19 mensyaratkan flag belum ada, sehingga walkthrough otomatis muncul saat tab dibuka. Langkah 2 sampai 3 menutup walkthrough otomatis itu agar `[?]` (langkah 4) bisa diklik dan Step 1 sampai Step 3 dibaca dari awal. Perilaku walkthrough otomatis, Skip, dan penyimpanan flag diuji di spec `TC-GS-BRAND-E2E-008-guided-tooltip-flag-seen-dan-dismiss`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (mock sesi dan flag awal), 3 (Skip walkthrough otomatis), 21 dan 51 (Done menutup walkthrough), 22 (mock flag true lalu muat ulang), 43 (ganti mock sesi ke Read Only).
- TC-GS-BRAND-22, TC-GS-BRAND-25, dan TC-GS-BRAND-26 tidak menyebut kondisi flag selain TC-GS-BRAND-22 (flag seen true); untuk TC-GS-BRAND-25 dan TC-GS-BRAND-26 spec memakai flag true agar walkthrough hanya muncul lewat `[?]`.
- Pada TC-GS-BRAND-26 Step 3 hanya diverifikasi sebagai step ketiga dengan `[Done]` (total 3 step); TC sumber tidak merinci konten Step 3 untuk Read Only.
