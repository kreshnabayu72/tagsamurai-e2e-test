---
id: TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard
title: "Guided Tooltip File Manager: Konten Step, Siklus Back, Next, Done, Skip, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-34
  - TC-GS-FILEMGR-37
  - TC-GS-FILEMGR-39
coverage:
  web: automated
---

# Guided Tooltip File Manager: Konten Step, Siklus Back, Next, Done, Skip, dan Keyboard

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor yang dimodelkan lewat payload izin mock: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD`.
- Kebutuhan mock (respons yang dipaksa):
  - Respons sesi/profil dan payload izin: Total Control (semua aksi File Manager); disediakan tim FE (S-13).
  - Daftar file aktif: `GET /v2/file-manager/{type}/files/list` (openapi baris 16); skema respons mengikuti openapi (baris 16). Sedikitnya satu halaman baris sehingga toolbar dan tabel utama ter-render, termasuk tombol Recycle Bin di toolbar.
  - Daftar Recycle Bin: `GET /v2/file-manager/{type}/files/recycle-bin/list` (openapi baris 334); skema respons mengikuti openapi (baris 334). Dimuat saat halaman dibuka bila halaman memuatnya; isi minimal.
  - Storage Usage: `GET /v2/file-manager/storage-usage` (openapi baris 579); skema respons mengikuti openapi (baris 579). Skenario S1 (Tabel A5) agar halaman termuat penuh.
  - Daftar Changelog: endpoint baca Changelog tidak ada di `openapi.yaml` maupun `low-level-design.md` modul; disediakan tim FE (S-13), hanya bila halaman memuatnya saat dibuka.
  - Respons preferensi Guided Tooltip untuk flag `guided_tooltip_seen_gs-file-manager`: true (walkthrough tidak muncul otomatis; hanya terbuka lewat tombol [?]). API pendukung di luar sumber modul (identitas pengguna, sesi, menu, preferensi Guided Tooltip) disediakan tim FE (S-13). Penyimpanan flag oleh [Done] dan overlay direkam sebagai permintaan pada mock.
- Tidak ada data backend atau state global yang diubah, sehingga tidak ada cleanup selain melepas mock di hook `after`.

## Test Steps

### TC-GS-FILEMGR-34: Konten walkthrough

1. Terapkan mock sesi Total Control dengan flag `guided_tooltip_seen_gs-file-manager` true, lalu buka Global Settings > File Manager
2. Klik tombol bantuan [?] di sebelah kanan Breadcrumb
3. Verifikasi Step 1 menampilkan indikator `Step 1 of 2`
4. Verifikasi Step 1 menyorot tabel utama
5. Verifikasi Step 1 Title "File Manager"
6. Verifikasi Step 1 Description "View and manage all uploaded user profile pictures stored in your organization's storage."
7. Klik [Next]
8. Verifikasi Step 2 menampilkan indikator `Step 2 of 2`
9. Verifikasi Step 2 menyorot tombol Recycle Bin di toolbar
10. Verifikasi Step 2 Title "Recycle Bin"
11. Verifikasi Step 2 Description "Access soft-deleted files with auto-purge retention before permanent deletion."
12. Verifikasi tombol di Step 2 berlabel [Done]
13. Klik [Done] untuk menutup walkthrough

### TC-GS-FILEMGR-37: Siklus navigasi Back, Next, Done, dan Skip lewat klik overlay

14. Klik tombol [?] di sebelah kanan Breadcrumb
15. Verifikasi Step 1 tidak menampilkan tombol [Back] (Hidden)
16. Klik [Next]
17. Verifikasi Step 2 menampilkan tombol [Back]
18. Verifikasi Step 2 menampilkan tombol [Done]
19. Klik [Back]
20. Verifikasi [Back] kembali ke Step 1
21. Klik [Next]
22. Klik [Done]
23. Verifikasi [Done] menutup walkthrough
24. Verifikasi [Done] menetapkan flag seen (permintaan simpan flag `guided_tooltip_seen_gs-file-manager` terekam pada mock)
25. Klik tombol [?] lagi
26. Klik area overlay gelap
27. Verifikasi klik overlay gelap menutup walkthrough (setara [Skip])

### TC-GS-FILEMGR-39: Aksesibilitas lewat fokus keyboard dan tombol Esc, Enter, panah

28. Klik tombol [?] di sebelah kanan Breadcrumb
29. Verifikasi kotak tooltip mendapat fokus keyboard saat aktif
30. Tekan Enter
31. Verifikasi Enter memajukan ke Step 2
32. Tekan panah kiri
33. Verifikasi panah kiri kembali ke Step 1
34. Tekan panah kanan
35. Verifikasi panah kanan memajukan ke Step 2
36. Tekan Esc
37. Verifikasi Esc menutup walkthrough (setara Skip)

## Notes

- Mode: mock. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas guided tooltip (konten dan navigasi); flag seen dan navigasi keluar diuji di spec `TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar` (FE+BE).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec berjumlah 37 langkah nominal, sedikit di atas sekitar 35 langkah. Semua blok satu kelas (guided tooltip), seluruhnya mock, berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain; langkah per blok pendek karena tiap Step butuh `Verifikasi` per klausa (indikator, spotlight, judul, deskripsi).
- TC-34, TC-37, dan TC-39 tidak menyebut kondisi flag; spec memakai flag true agar walkthrough hanya muncul lewat tombol [?] (pola yang sama dengan Guided Tooltip modul lain). Step otomatis pada kunjungan pertama diuji di spec 070.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (mock sesi dan flag), langkah 13 (Done menutup walkthrough sebelum TC berikutnya), langkah 21 dan 22 (TC-37 langkah 4), langkah 25 (TC-37 langkah 5).
- Temuan untuk QA:
  - Endpoint baca Changelog tidak ada di `openapi.yaml` maupun `low-level-design.md` modul (Changelog ditulis lintas-service oleh Analytics Reporting); owner: API/LLD. Sampai dilengkapi, disediakan tim FE (S-13).
  - TC-37 butir d ("menetapkan flag seen") diasersi lewat rekaman permintaan simpan pada mock; TC tidak menyebut cara cek flag.
  - TC-34, TC-37, dan TC-39 tidak menyebut kondisi flag.
