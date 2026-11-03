---
id: TC-AC-DN-E2E-179-konkurensi-create-duplikat-dan-referensi
title: "Konkurensi Create: Duplikat setelah Pengecekan Lolos dan Measurement Dihapus Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-96
  - TC-AC-DN-104
coverage:
  web: automated
---

# Konkurensi Create: Duplikat setelah Pengecekan Lolos dan Measurement Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement master `Unit`, node pohon Category `Antenna`. Nama dinamis dibentuk `<nama dasar> {runId}-179` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`).
- Data Dinamis (milik spec; dihapus fixture BE di hook `after`):

  | Kode | Data | Detail | Dipakai oleh |
  |---|---|---|---|
  | D1 | Nama `Race Gateway {runId}-179` | diketik sesi Budi; Maya membuat Device Name bernama sama (Unit, Antenna) lewat sesi API | TC-AC-DN-96 |
  | M1 | Measurement `Satuan Sementara {runId}-179` | tanpa pemakai, di-seed fixture BE di hook `before`, dihapus Maya lewat sesi API | TC-AC-DN-104 |
  | D2 | Nama `Stale Meas Gateway {runId}-179` | diketik sesi Budi; Submit ditolak | TC-AC-DN-104 |

- Kemampuan teknis (disediakan tim FE/BE): sesi API Maya Putri untuk membuat Device Name dan menghapus Measurement master (tanpa endpoint karangan, S-13); jeda debounce 500 ms (di bawah 30 detik, R-10) sesuai TC.
- State global (S-06, pengecualian 2026-10-30): master Measurement Pre-setup #13 menerima M1 dan kehilangannya lagi; fixture backend memastikan M1 tidak tersisa di hook `before` dan `after`. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

### TC-AC-DN-96: Submit Create ditolak sebagai duplikat setelah pengecekan lolos

1. Klik `+ Device Name`
2. Ketik "Race Gateway {runId}-179" pada field Device Name
3. Tunggu 500 ms
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Maya Putri (sesi API) membuat Device Name `Race Gateway {runId}-179` dengan Measurement `Unit` dan Category `Antenna` hingga tersimpan
7. Klik `[Submit]`
8. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name
9. Verifikasi popup form tetap terbuka
10. Verifikasi input Device Name, Measurement, dan Category dipertahankan
11. Klik icon `(✕)` pada form
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-AC-DN-104: Submit Create dengan Measurement yang dihapus admin lain

14. Klik `+ Device Name`
15. Ketik "Stale Meas Gateway {runId}-179" pada field Device Name
16. Klik field Measurement lalu pilih `Satuan Sementara {runId}-179`
17. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
18. Maya Putri (sesi API) menghapus Measurement `Satuan Sementara {runId}-179` di master hingga terhapus
19. Klik `[Submit]`
20. Verifikasi error inline di bawah field Measurement: "This measurement no longer exists. Please select another."
21. Verifikasi field Measurement dikosongkan
22. Klik field Measurement
23. Verifikasi daftar opsi Measurement memuat "Unit", "Meter", dan "Box"
24. Verifikasi daftar opsi Measurement tidak memuat `Satuan Sementara {runId}-179`
25. Verifikasi field Device Name berisi "Stale Meas Gateway {runId}-179" dan field Category berisi `Antenna`
26. Verifikasi popup form tetap terbuka
27. Klik icon `(✕)` pada form
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah 6 dan 18 ditulis "... hingga ... tersimpan/terhapus" (R-20). Penghapusan Measurement master dan pembuatan Device Name lewat sesi API adalah kemampuan yang disediakan tim FE/BE; TC menyebut jalur UI untuk langkah tersebut.
- Langkah penghubung (S-03): langkah 3 (jeda debounce 500 ms) mengikuti TC; langkah 11 sampai 13 dan 27 sampai 29 menutup form dirty secara deterministik (S-08, S-09); langkah 22 sampai 24 membuka dropdown Measurement agar "daftar opsi dimuat ulang" teramati (S-14), dengan langkah 23 sebagai anchor langkah 24 (8b butir 2).
- Urutan: mengikuti sourceTc; tidak ada aksi menghapus data Device Name oleh spec (Device Name hasil Maya dihapus fixture di hook `after`).
- Ukuran spec: 29 langkah.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-96 (hanya satu record `Race Gateway` tersimpan) dan TC-AC-DN-104 (tidak ada record baru).
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-179` (S-12). Measurement `Satuan Sementara` tidak ada di Pre-setup #13; di-seed fixture sesuai Precondition TC-AC-DN-104.
