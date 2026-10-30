---
id: TC-GS-FILEMGR-E2E-049-setup-column-screening-tutup-dan-guard-tiga-surface
title: "Setup Column Tiga Surface: Screening Overlay dan Popup, Tutup Tanpa Save, dan Guard Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-175
  - TC-GS-FILEMGR-176
  - TC-GS-FILEMGR-177
  - TC-GS-FILEMGR-178
  - TC-GS-FILEMGR-179
  - TC-GS-FILEMGR-180
  - TC-GS-FILEMGR-186
  - TC-GS-FILEMGR-187
coverage:
  web: automated
---

# Setup Column Tiga Surface: Screening Overlay dan Popup, Tutup Tanpa Save, dan Guard Kolom Terakhir

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (respons yang dipaksa):
  - Daftar file aktif tabel utama: `GET /v2/file-manager/{type}/files/list` (openapi baris 16); skema respons mengikuti openapi (baris 16). Mengembalikan 33 file Tabel A2 (ukuran halaman 10).
  - Daftar Recycle Bin: `GET /v2/file-manager/{type}/files/recycle-bin/list` (openapi baris 334); skema respons mengikuti openapi (baris 334). Mengembalikan 16 baris Tabel A3 (retensi 30 hari).
  - Daftar Changelog: endpoint baca Changelog tidak ada di `openapi.yaml` maupun `low-level-design.md` modul (Changelog ditulis lintas-service); endpoint dan skema responsnya disediakan tim FE (S-13). Mengembalikan 14 entri Tabel A4.
  - Storage Usage: `GET /v2/file-manager/storage-usage` (openapi baris 579), hanya bila halaman memuatnya saat dibuka; skema respons mengikuti openapi (baris 579). Tidak menjadi objek langkah spec ini.
  - Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-file-manager`: true (di-mock). API pendukung di luar modul (identitas pengguna, sesi, menu, preferensi Guided Tooltip, General Settings) disediakan tim FE (S-13).
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per tabel di browser (PRD File Manager; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya.
- Tabel "Surface yang diuji" (parameter langkah 19 sampai 37, 38 sampai 45, dan 46 sampai 52):

| Surface | Pembuka | Kolom (berurutan) | Kolom yang tidak ada di overlay | Kolom di-uncheck (langkah 41) | Cara tutup popup (langkah 42) | Kolom tersisa (langkah 48) |
|---|---|---|---|---|---|---|
| Tabel utama | tanpa aksi (layar File Manager) | `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date` | `Checkbox`, `Actions` | `Size` | ikon close (X) | `File Name` |
| Recycle Bin | klik tombol Recycle Bin di toolbar | `File Name`, `File Format`, `User Name`, `Size`, `Deleted Date`, `Deleted By`, `Auto-Purge In` | `Checkbox`, `Actions` | `Deleted By` | Esc | `File Name` |
| Changelog | klik ikon Changelog di toolbar | `Date`, `Action`, `File Name`, `Field`, `Old Value`, `New Value`, `Modified By` | `Actions` | `Field` | ikon close (X) | `Date` |

- Suite serial (`parallel: false`): konfigurasi kolom tiga tabel adalah state global browser yang dipakai spec lain.
- Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-file-manager`: true (di-mock), sehingga walkthrough tidak muncul otomatis; terdaftar di Kebutuhan mock.
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom ketiga tabel dikembalikan ke default (semua kolom tampil, urutan default, tanpa pin) lewat `[Reset to Default]` atau penghapusan penyimpanan preferensi kolom di browser.
- Kemampuan teknis: `Spectra.intercept()` untuk ketiga respons daftar; mengarahkan kursor ke checkbox disabled untuk membaca tooltip; menutup popup lewat ikon close dan Esc.

## Test Steps

### TC-GS-FILEMGR-175: Screening overlay Column Visibility tabel utama

1. Klik ikon (⋯) di header kolom Actions tabel utama
2. Verifikasi daftar overlay berurutan `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date`
3. Verifikasi setiap kolom pada daftar memiliki checkbox tercentang (enabled)
4. Verifikasi setiap kolom pada daftar memiliki handle drag
5. Verifikasi kolom Checkbox dan Actions tidak ada di daftar
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-FILEMGR-178: Screening popup Setup Column tabel utama

7. Klik item `Setup Column...`
8. Verifikasi Header: judul "Setup Column"
9. Verifikasi Header: teks "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
10. Verifikasi Header: ikon close (X) di kanan atas
11. Verifikasi Body: daftar enam kolom berurutan `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date`
12. Verifikasi setiap kolom di Body memiliki checkbox tercentang (enabled)
13. Verifikasi setiap kolom di Body memiliki handle drag
14. Verifikasi setiap kolom di Body memiliki ikon Pin
15. Verifikasi tabel di balik popup menampilkan pratinjau
16. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi tidak ada tombol `[Cancel]`
18. Klik ikon close (X) untuk menutup popup

### TC-GS-FILEMGR-176, 177, 179, 180: Screening overlay dan popup Setup Column modal Recycle Bin dan Changelog

19. Untuk setiap surface Recycle Bin dan Changelog pada tabel Prerequisites, lakukan langkah 20 sampai 37
20. Buka surface sesuai kolom Pembuka
21. Klik ikon (⋯) di header kolom Actions tabel surface itu
22. Verifikasi daftar overlay berurutan sesuai kolom Kolom surface itu
23. Verifikasi setiap kolom pada daftar memiliki checkbox tercentang (enabled)
24. Verifikasi setiap kolom pada daftar memiliki handle drag
25. Verifikasi kolom yang tertulis pada "Kolom yang tidak ada di overlay" tidak ada di daftar
26. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
27. Klik item `Setup Column...`
28. Verifikasi Header: judul "Setup Column"
29. Verifikasi Header: teks "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
30. Verifikasi Header: ikon close (X)
31. Verifikasi Body: daftar kolom berurutan sesuai kolom Kolom surface itu
32. Verifikasi setiap kolom di Body memiliki checkbox tercentang
33. Verifikasi setiap kolom di Body memiliki handle drag
34. Verifikasi setiap kolom di Body memiliki ikon Pin
35. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
36. Verifikasi tidak ada tombol `[Cancel]`
37. Klik ikon close (X) popup, lalu klik ikon close (X) modal surface

### TC-GS-FILEMGR-186: Menutup popup Setup Column tanpa Save membuang perubahan pada tiga surface

38. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 39 sampai 45
39. Buka surface sesuai kolom Pembuka
40. Buka popup Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`
41. Hapus centang kolom pada "Kolom di-uncheck"
42. Tutup popup sesuai "Cara tutup popup"
43. Verifikasi popup tertutup tanpa dialog konfirmasi
44. Verifikasi kolom pada "Kolom di-uncheck" tetap tampil di tabel surface itu
45. Tutup modal surface bila surface berupa modal

### TC-GS-FILEMGR-187: Kolom terakhir yang tersisa tidak bisa disembunyikan pada tiga surface

46. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 47 sampai 52
47. Buka surface sesuai kolom Pembuka
48. Buka overlay Column Visibility dan hapus centang semua kolom kecuali kolom pada "Kolom tersisa"
49. Arahkan kursor ke checkbox kolom tersisa
50. Verifikasi checkbox kolom tersisa disabled dan tidak bisa di-uncheck
51. Verifikasi tooltip "At least one column must remain visible."
52. Centang kembali semua kolom lewat overlay Column Visibility, lalu tutup modal surface bila surface berupa modal

## Notes

- Mode: mock. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 175, 178 (tabel utama), 176, 177, 179, 180 (Recycle Bin dan Changelog), 186, 187. Screening di awal, aksi yang mengubah konfigurasi kolom (187) di akhir.
- Panjang spec: 52 langkah tertulis (sekitar 93 langkah setelah ekspansi tiga surface), di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok berkelas sama (komponen Setup Column yang identik di tiga surface, Mode mock), langkah berulang per surface memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7), dan kegagalan satu surface tidak membuat blok surface lain kehilangan makna. Langkah yang diulang: 20 sampai 37 (dua iterasi), 39 sampai 45 dan 47 sampai 52 (tiga iterasi).
- `Verifikasi` yang diulang tetap satu per klausa (S-01). Pratinjau tabel di balik popup (langkah 15) hanya diasersi untuk tabel utama karena hanya TC-GS-FILEMGR-178 yang menyebutnya; TC-GS-FILEMGR-179 dan 180 tidak menyebutnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18 dan 37 (menutup popup dan modal setelah screening), langkah 45 (menutup modal), langkah 52 (memulihkan kolom yang disembunyikan; hook `after` sebagai cadangan).
- Pembagian lintas spec: TC Setup Column hide dan reorder serta persistensi ada di spec `TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi`; pin dan Reset to Default ada di spec `TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset`.
- Temuan untuk QA:
  - Endpoint baca Changelog tidak ada di `openapi.yaml` maupun `low-level-design.md` modul (Changelog ditulis lintas-service oleh Analytics Reporting); owner: API/LLD. Sampai dilengkapi, endpoint dan skemanya disediakan tim FE (S-13).
  - TC-GS-FILEMGR-186 langkah 2 menutup popup Recycle Bin dengan Esc sedangkan dua surface lain dengan ikon close (X); spec mengikuti TC (kolom "Cara tutup popup").
  - Expected a TC-GS-FILEMGR-187 ("tidak bisa di-uncheck") diasersi sebagai checkbox disabled; TC tidak menjelaskan cara membuktikan "tidak bisa" selain tooltip dan state disabled.
