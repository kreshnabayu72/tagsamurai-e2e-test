---
id: TC-AC-DN-E2E-182-konkurensi-edit-bagian-2
title: "Konkurensi Edit: Measurement atau Category Dihapus Admin Lain saat Form Edit Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-155
  - TC-AC-DN-156
coverage:
  web: automated
---

# Konkurensi Edit: Measurement atau Category Dihapus Admin Lain saat Form Edit Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement `Unit`, node pohon Category. Nama dinamis dibentuk `<nama dasar> {runId}-182` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `TAG` > `GPS`).
- Data Dinamis (milik spec; dibuat fixture BE di hook `before`, dihapus di hook `after`; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Data | Detail | Dipakai oleh |
  |---|---|---|---|
  | R1 | Device Name `Edit Measurement {runId}-182` | Measurement `Unit`, Category `Antenna`, tanpa SKU | TC-AC-DN-155 |
  | M1 | Measurement `Satuan Sementara {runId}-182` | tanpa pemakai; dihapus Maya lewat sesi API | TC-AC-DN-155 |
  | R2 | Device Name `Edit Category {runId}-182` | Measurement `Unit`, Category `Antenna`, tanpa SKU | TC-AC-DN-156 |
  | C1 | Node Category `Kategori Sementara {runId}-182` | leaf di bawah `TAG` > `GPS`, tanpa Device Name; dihapus Maya lewat sesi API | TC-AC-DN-156 |

- Kemampuan teknis (disediakan tim FE/BE): sesi API Maya Putri untuk menghapus Measurement master dan node Category (tanpa endpoint karangan, S-13).
- State global (S-06, pengecualian 2026-10-30): master Measurement Pre-setup #13 dan pohon Category Pre-setup #14 menerima M1 dan C1 lalu kehilangannya lagi; fixture backend memastikan keduanya tidak tersisa di hook `before` dan `after`. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

### TC-AC-DN-155: Measurement dihapus admin lain

1. Ketik Search `Edit Measurement {runId}-182`, tekan Enter
2. Buka menu aksi pada baris `Edit Measurement {runId}-182`, klik `Edit`
3. Klik field Measurement lalu pilih `Satuan Sementara {runId}-182`
4. Maya Putri (sesi API) menghapus Measurement `Satuan Sementara {runId}-182` di master hingga terhapus
5. Klik `[Save]`
6. Verifikasi error inline di bawah field Measurement: "This measurement no longer exists. Please select another."
7. Verifikasi field Measurement dikosongkan
8. Klik field Measurement
9. Verifikasi daftar opsi Measurement memuat "Unit", "Meter", dan "Box"
10. Verifikasi daftar opsi Measurement tidak memuat `Satuan Sementara {runId}-182`
11. Verifikasi field Device Name berisi `Edit Measurement {runId}-182` dan field Category berisi `Antenna`
12. Verifikasi popup form tetap terbuka
13. Klik icon `(✕)` pada form
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-AC-DN-156: Category dihapus admin lain

16. Ketik Search `Edit Category {runId}-182`, tekan Enter
17. Buka menu aksi pada baris `Edit Category {runId}-182`, klik `Edit`
18. Klik field Category, expand `TAG` lalu `GPS`, pilih leaf `Kategori Sementara {runId}-182`
19. Maya Putri (sesi API) menghapus Category `Kategori Sementara {runId}-182` hingga terhapus
20. Klik `[Save]`
21. Verifikasi error inline di bawah field Category: "This category no longer exists. Please select another."
22. Verifikasi field Category dikosongkan
23. Klik field Category, expand `TAG` lalu `GPS`
24. Verifikasi pohon Category memuat node `GPS`
25. Verifikasi pohon Category tidak memuat `Kategori Sementara {runId}-182`
26. Verifikasi field Device Name berisi `Edit Category {runId}-182` dan field Measurement berisi `Unit`
27. Verifikasi popup form tetap terbuka
28. Klik icon `(✕)` pada form
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah 4 dan 19 ditulis "... hingga terhapus" (R-20). Penghapusan Measurement dan Category lewat sesi API adalah kemampuan yang disediakan tim FE/BE; TC menyebut jalur UI.
- Langkah penghubung (S-03, R-16): langkah 1, 16 (Search) menemukan baris record milik spec; langkah 8 sampai 10 dan 23 sampai 25 membuka dropdown agar "daftar opsi dimuat ulang" teramati (S-14), dengan langkah 9 dan 24 sebagai anchor absence (8b butir 2); langkah 13 sampai 15 dan 28 sampai 30 menutup form dirty (S-08, S-09).
- Record milik spec (S-06, S-12): R1 dan R2 menggantikan `Door Antenna` Pre-setup #16 TC sumber; Pre-setup #16 tidak diubah, sehingga "Record `Door Antenna` tidak berubah" (Post Condition) tidak memerlukan pemulihan.
- Urutan: mengikuti sourceTc. Spec lain: TC-AC-DN-160 dan TC-AC-DN-571 (dua sesi Edit record yang sama) ada di spec 187.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-155 dan TC-AC-DN-156.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-182` (S-12).
