---
id: TC-AC-LCS-E2E-016-guided-tooltip-penutupan-dan-mulai-ulang
title: "Guided Tooltip: Penutupan lewat Overlay dan Esc, Mulai Ulang lewat [?], dan Navigasi Keluar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-53
  - TC-AC-LCS-54
  - TC-AC-LCS-55
  - TC-AC-LCS-56
coverage:
  web: automated
---

# Guided Tooltip: Penutupan lewat Overlay dan Esc, Mulai Ulang lewat [?], dan Navigasi Keluar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini (`guided_tooltip_seen_<page_key>`, page_key `ac-plans-licensing-lifecycle-settings`) untuk akun aktor: hook `before` suite menyetelnya true; spec ini menguji flag itu sendiri sehingga mengaturnya sendiri sesudah hook (pengecualian suite): langkah "Hapus flag seen" menghapus flag lewat kemampuan yang disediakan tim FE/BE; hook `after` suite memulihkannya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); pengaturan dan penghapusan flag Guided Tooltip akun aktor (disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-53: Klik area overlay gelap menutup walkthrough dan men-set flag seen

1. Hapus flag seen untuk akun aktor (flag belum ada)
2. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
3. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
4. Klik `[Next]`
5. Klik area overlay gelap di luar spotlight
6. Verifikasi Walkthrough tertutup
7. Muat ulang halaman dengan F5
8. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings" tampil
9. Verifikasi Walkthrough tidak tampil lagi

### TC-AC-LCS-54: Tombol Esc menutup walkthrough sebagai Skip dan keyboard Enter serta panah berpindah step

10. Hapus flag seen untuk akun aktor (flag belum ada)
11. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
12. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
13. Tekan Enter
14. Verifikasi Step 2 tampil
15. Tekan panah kanan
16. Verifikasi Step 3 tampil
17. Tekan panah kiri
18. Verifikasi Step 2 tampil
19. Tekan Esc
20. Verifikasi Walkthrough tertutup
21. Muat ulang halaman dengan F5
22. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings" tampil
23. Verifikasi Walkthrough tidak tampil lagi setelah F5

### TC-AC-LCS-55: Tombol [?] di sebelah kanan Breadcrumb memulai ulang walkthrough dari Step 1

24. Atur flag seen terisi untuk akun aktor (walkthrough sudah pernah diselesaikan)
25. Hover tombol `[?]` di sebelah kanan Breadcrumb
26. Verifikasi Tooltip "Show guide" tampil
27. Klik tombol `[?]`
28. Verifikasi Walkthrough dimulai dari Step 1 of 5
29. Klik `[Next]` empat kali
30. Klik `[Done]` pada Step 5
31. Muat ulang halaman dengan F5
32. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings" tampil
33. Verifikasi Walkthrough tidak tampil otomatis

### TC-AC-LCS-56: Navigasi keluar halaman di tengah walkthrough tidak men-set flag seen

34. Hapus flag seen untuk akun aktor (flag belum ada)
35. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
36. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
37. Klik `[Next]`
38. Klik menu Plans & Features di sidebar tanpa menyelesaikan walkthrough
39. Verifikasi Walkthrough tertutup
40. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
41. Verifikasi Walkthrough tampil lagi dari Step 1 of 5

## Notes

- Pengecualian suite: spec ini mengatur flag Guided Tooltip sendiri (bagian 4 konvensi, KEPUTUSAN 2026-10-22).
- Langkah penghubung (S-03, S-09): "Hapus flag seen" di awal tiap blok yang membutuhkan flag belum ada; "Klik menu Plans & Features" lalu klik menu Lifecycle Settings memulai walkthrough dari Step 1; "Klik `[Next]`" pada TC 53 dan TC 56 membawa walkthrough ke Step 2 sesuai Precondition (hasilnya tidak diasersi karena bukan Expected TC). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: pada TC 53 dan TC 54 butir "tidak tampil lagi" adalah absence sesudah F5; spec menambah `Verifikasi` Breadcrumb tampil sebagai anchor positif halaman (bagian 8b butir 2, S-03). TC 55 langkah 3 "klik `[Done]` setelah melewati lima step" ditulis sebagai klik `[Next]` empat kali lalu klik `[Done]`.
- Alasan di atas sekitar 35 langkah: seluruh blok memuat TC fungsional kelas yang sama (Guided Tooltip), tiap blok mengatur flag seen sendiri dan memulai walkthrough dari awal, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
