---
id: TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes
title: "Edit Position: Tutup Tanpa Perubahan, Dialog Unsaved Changes, Nilai Dikembalikan Tidak Dirty, Clear Field, Backdrop, Reload, dan Pindah Menu"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-93
  - TC-GS-POS-94
  - TC-GS-POS-95
  - TC-GS-POS-96
  - TC-GS-POS-97
  - TC-GS-POS-98
  - TC-GS-POS-99
  - TC-GS-POS-100
  - TC-GS-POS-101
  - TC-GS-POS-102
  - TC-GS-POS-103
coverage:
  web: automated
---

# Edit Position: Tutup Tanpa Perubahan, Dialog Unsaved Changes, Nilai Dikembalikan Tidak Dirty, Clear Field, Backdrop, Reload, dan Pindah Menu

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`.
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.editSeed018`): satu Position `Legal Counsel {runId}-018` (milik spec ini; tidak pernah disimpan ulang, nama tidak berubah). Nilai uji yang diketik namun tidak tersimpan: `Legal Manager`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Position `Legal Counsel {runId}-018` bila masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: input keyboard (Esc, F5); klik pada area backdrop; menangani dialog `beforeunload` bawaan browser (membaca bahwa dialog muncul lalu membatalkan reload tanpa meninggalkan halaman); navigasi sidebar in-app.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `Legal Counsel {runId}-018`, tekan Enter

### TC-GS-POS-93: Tutup via `[✕]` tanpa perubahan

2. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
3. Verifikasi Popup Edit Position terbuka
4. Klik `✕` pada Popup Edit
5. Verifikasi Popup Edit langsung tertutup
6. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-94: Tutup via Esc tanpa perubahan

7. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
8. Verifikasi Popup Edit Position terbuka
9. Tekan Esc
10. Verifikasi Popup Edit langsung tertutup
11. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-95: Tutup via `[✕]` setelah nilai diubah memunculkan Dialog Unsaved Changes

12. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
13. Verifikasi Popup Edit Position terbuka
14. Ganti nilai Position Name menjadi `Legal Manager`
15. Klik `✕` pada Popup Edit
16. Verifikasi dialog Header menampilkan Title "Unsaved Changes"
17. Verifikasi dialog Header berseverity warning
18. Verifikasi dialog Body menampilkan "You have unsaved changes. Are you sure you want to leave?"
19. Verifikasi dialog Footer memiliki tombol `[Cancel]` (text, contrast)
20. Verifikasi dialog Footer memiliki tombol `[Leave]` (filled, warning)

### TC-GS-POS-97: Cancel pada Dialog Unsaved Changes

21. Klik `[Cancel]`
22. Verifikasi dialog tertutup
23. Verifikasi Popup Edit tetap terbuka
24. Verifikasi field Position Name tetap berisi `Legal Manager`

### TC-GS-POS-96: Esc setelah nilai diubah memunculkan Dialog Unsaved Changes

25. Tekan Esc
26. Verifikasi dialog Unsaved Changes muncul
27. Verifikasi Popup Edit tidak langsung tertutup
28. Klik `[Cancel]`

### TC-GS-POS-101: Klik backdrop saat nilai diubah

29. Klik area backdrop
30. Verifikasi Popup Edit tetap terbuka
31. Verifikasi field Position Name tetap berisi `Legal Manager`
32. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-98: Leave pada Dialog Unsaved Changes

33. Klik `✕` pada Popup Edit
34. Verifikasi dialog Unsaved Changes muncul
35. Klik `[Leave]`
36. Verifikasi tidak ada toast
37. Verifikasi dialog tertutup
38. Verifikasi Popup Edit tertutup
39. Verifikasi baris tetap `Legal Counsel {runId}-018`

### TC-GS-POS-99: Nilai diubah lalu dikembalikan identik tidak dianggap dirty

40. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
41. Verifikasi Popup Edit Position terbuka
42. Ganti nilai Position Name menjadi `Legal Manager`
43. Ketik ulang hingga nilai kembali `Legal Counsel {runId}-018`
44. Klik `✕` pada Popup Edit
45. Verifikasi Popup Edit langsung tertutup
46. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-100: Tutup setelah Clear Field memunculkan Dialog Unsaved Changes

47. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
48. Verifikasi Popup Edit Position terbuka
49. Klik `[Clear Field]`
50. Klik `✕` pada Popup Edit
51. Verifikasi dialog Unsaved Changes muncul
52. Klik `[Leave]`

### TC-GS-POS-102: Reload tab saat nilai diubah memunculkan konfirmasi browser

53. Klik `⋯` pada baris `Legal Counsel {runId}-018`, pilih `Edit`
54. Verifikasi Popup Edit Position terbuka
55. Ganti nilai Position Name menjadi `Legal Manager`
56. Tekan F5
57. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
58. Batalkan reload pada konfirmasi browser (tetap di halaman)

### TC-GS-POS-103: Pindah menu in-app saat nilai diubah

59. Klik menu sidebar Global Settings > General Settings
60. Verifikasi dialog Unsaved Changes muncul dengan body "You have unsaved changes. Are you sure you want to leave?"
61. Klik `[Leave]`
62. Verifikasi halaman berpindah ke General Settings

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 93, 94, 95, 97, 96, 101, 98, 99, 100, 102, 103. Urutan ini menyimpang dari urutan TC sumber dan mengikuti kondisi form: TC-GS-POS-95, 97, 96, 101, dan 98 memakai satu pembukaan form dirty (`Legal Manager`); TC-GS-POS-102 dan 103 memakai satu pembukaan form dirty dan ditaruh terakhir karena TC-GS-POS-103 meninggalkan halaman. Penutupan bersih (TC-GS-POS-93, 94, 99) memakai form baru masing-masing.
- Jumlah pembukaan Popup Edit: 6 (langkah 2, 7, 12, 40, 47, 53); jumlah kejadian menutup: 6 (langkah 4, 9, 33 sampai 35, 44, 50 sampai 52, dan `[Leave]` di langkah 61).
- Langkah 21 (`[Cancel]`) adalah langkah TC-GS-POS-97; dialog yang dibuka langkah 15 dipakai bersama TC-GS-POS-95 dan 97. Pada TC-GS-POS-98, `✕` lalu `[Leave]` (langkah 33 dan 35) memakai dialog baru; `Verifikasi` dialog pada langkah 34 ditambahkan agar penutupan form dirty deterministik (S-08).
- Langkah 3, 8, 13, 41, 48, dan 54 adalah `Verifikasi` dari anotasi "→ Popup Edit Position terbuka" pada Langkah 1 TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search agar baris target tampil pada halaman aktif), langkah 28 (menutup dialog agar TC-GS-POS-101 berjalan pada form yang masih terbuka), langkah 52 (menutup form dirty), dan langkah 58 (membatalkan reload agar form tetap terbuka untuk TC-GS-POS-103).
- Seluruh langkah penutupan memakai `✕`, `Esc`, atau `[Leave]` (tanpa `[Cancel]` pada modal Edit). `[Cancel]` hanya pada dialog Unsaved Changes.
- Spec melewati sekitar 35 langkah (62 langkah). Seluruhnya satu kelas (penutupan form Edit), satu akun, satu record milik spec, dan tidak ada aksi yang mengubah data. Tiap kelompok (penutupan bersih, form dirty, reload dan pindah menu) membuka form baru dan memulai dari nilai tersimpan, sehingga kelompok sesudahnya tetap bermakna bila kelompok sebelumnya gagal, kecuali kegagalan keras pada pembukaan popup.
- Temuan untuk QA:
  - Post Condition "Record tetap `Legal Counsel`" (TC-GS-POS-97, 98, 103) dan "tidak ada entri Changelog" (TC-GS-POS-98) tanpa langkah observasi di TC; hanya "baris tetap `Legal Counsel`" pada Expected TC-GS-POS-98 yang diasersi (langkah 39).
  - TC-GS-POS-102 menyebut "Konfirmasi bawaan browser muncul" tanpa menyebut tindak lanjut; spec membatalkan reload (tetap di halaman) agar form tetap terbuka. Kemampuan menangani dialog `beforeunload` ada di Prerequisites.
