---
id: TC-AC-LCS-E2E-015-guided-tooltip-alur-walkthrough
title: "Guided Tooltip: Kunjungan Pertama dan Walkthrough Next, Back, serta Skip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-49
  - TC-AC-LCS-50
  - TC-AC-LCS-51
  - TC-AC-LCS-52
coverage:
  web: automated
---

# Guided Tooltip: Kunjungan Pertama dan Walkthrough Next, Back, serta Skip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`).
- Flag Guided Tooltip halaman ini (`guided_tooltip_seen_<page_key>`, page_key `ac-plans-licensing-lifecycle-settings`) untuk akun aktor: hook `before` suite menyetelnya true; spec ini menguji flag itu sendiri sehingga mengaturnya sendiri sesudah hook (pengecualian suite): langkah "Hapus flag seen" menghapus flag lewat kemampuan yang disediakan tim FE/BE; hook `after` suite memulihkannya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); pengaturan dan penghapusan flag Guided Tooltip akun aktor (disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-49: Guided Tooltip tampil otomatis pada kunjungan pertama ke Lifecycle Settings

1. Hapus flag seen untuk akun aktor (flag belum ada)
2. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
3. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
4. Verifikasi Overlay gelap tampil dengan spotlight pada tab bar
5. Verifikasi Step 1 of 5: Title "Seven Independent Config Areas", Description "Each tab is its own domain config — switching tabs never discards unsaved changes on the tabs you leave behind."
6. Verifikasi Tombol navigasi `[Skip]` dan `[Next]` tampil pada Step 1
7. Verifikasi Tombol `[Back]` tidak tampil pada Step 1

### TC-AC-LCS-50: Walkthrough 5 step dijalankan dengan Next sampai Done

8. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
9. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
10. Verifikasi Step 1 of 5: spotlight pada Tab bar; Title "Seven Independent Config Areas", Description "Each tab is its own domain config — switching tabs never discards unsaved changes on the tabs you leave behind."
11. Klik `[Next]`
12. Verifikasi Step 2 of 5: spotlight pada Field label — 🔖 icon; Title "Hover for Field Help"; Description "Every field has a tooltip explaining exactly what it controls and how it affects the platform — hover or focus the label to see it."
13. Klik `[Next]`
14. Verifikasi Step 3 of 5: spotlight pada [Reset to Default] button; Title "Reset to Platform Default"; Description "Restores this tab's fields to their original platform defaults. Independent per tab — resetting one tab never touches the others."
15. Klik `[Next]`
16. Verifikasi Step 4 of 5: spotlight pada [Save] button; Title "Save Is Per-Tab"; Description "Save only applies to the tab you're on. It stays disabled until you change a value, and editing one tab never enables Save on another."
17. Klik `[Next]`
18. Verifikasi Step 5 of 5: spotlight pada Changelog icon [📋]; Title "Each Tab Keeps Its Own Changelog"; Description "This icon opens the changelog for the tab you're currently on. Switch tabs, and it opens a different history — the other six tabs each have their own."
19. Verifikasi Pada Step 5 tombol `[Next]` berganti menjadi `[Done]`
20. Klik `[Done]`
21. Verifikasi Walkthrough tertutup

### TC-AC-LCS-51: Tombol Back pada walkthrough kembali ke step sebelumnya

22. Hapus flag seen untuk akun aktor (flag belum ada)
23. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
24. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
25. Klik `[Next]`
26. Klik `[Back]`
27. Verifikasi Step 1 of 5 "Seven Independent Config Areas" tampil kembali
28. Verifikasi Tombol `[Back]` tidak tampil pada Step 1

### TC-AC-LCS-52: Klik [Skip] menutup walkthrough dan walkthrough tidak muncul lagi pada kunjungan berikutnya

29. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
30. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
31. Klik `[Skip]` pada Step 1
32. Verifikasi Walkthrough dan overlay gelap tertutup
33. Muat ulang halaman dengan F5
34. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings" tampil
35. Verifikasi Walkthrough tidak tampil lagi

## Notes

- Pengecualian suite: spec ini mengatur flag Guided Tooltip sendiri (bagian 4 konvensi, KEPUTUSAN 2026-10-22).
- Langkah penghubung (S-03, S-09): "Hapus flag seen" di awal blok yang membutuhkan flag belum ada (TC 49 dan TC 51; TC 50 dan TC 52 memakai flag yang masih belum ada dari blok sebelumnya); pada TC 49 flag dihapus sesudah hook `beforeEach` suite memuat halaman, sehingga langkah 2 meninggalkan halaman dan langkah 3 membukanya kembali agar walkthrough dimuat ulang dengan flag belum ada; "Klik menu Plans & Features" lalu klik menu Lifecycle Settings memulai walkthrough dari Step 1 dan mengosongkan walkthrough blok sebelumnya (TC 56 menunjukkan klik sidebar saat walkthrough tidak men-set flag). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: TC 50 butir b dan e menulis teks target spotlight "Field label — 🔖 icon" dan "Changelog icon [📋]" dengan emoji; spec menyalin apa adanya. TC 51 langkah 1 menyebut "→ Step 2 tampil" tanpa butir Expected; tidak diasersi (hanya Step 1 setelah Back yang diasersi).
- Temuan untuk QA: pada TC 52 butir b ("walkthrough tidak tampil lagi") adalah absence sesudah F5; spec menambah `Verifikasi` Breadcrumb tampil sebagai anchor positif halaman (bagian 8b butir 2, S-03).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
