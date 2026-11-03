---
id: TC-FA-CAT-E2E-015-role-matrix-positif-delete-dan-bulk-delete-delete-only
title: "Role Matrix Positif: Delete dan Bulk Delete oleh Delete-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-46
  - TC-FA-CAT-47
coverage:
  web: automated
---

# Role Matrix Positif: Delete dan Bulk Delete oleh Delete-Only

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Role yang diuji (bagian 3a; TC sumber hanya memuat satu role berhak aksi Delete):

| Role | Pre-setup | Akun | Password | Client |
|---|---|---|---|---|
| Delete-Only (Manage Asset Master Data: D) | #6 | `Fixture.settingsCategories.deleteOnly` (`deleteOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_DO_PASSWORD` | CatMain (Pre-setup #20) |

- Login di hook `before` spec ini sebagai Delete-Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_DO_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20, plan Enterprise) sebagai konteks; baris seed Pre-setup tidak dihapus.
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE tanpa endpoint karangan; semua leaf Total Asset 0, tanpa Asset Name yang menunjuk): `Vehicle {runId}-015` (target TC-FA-CAT-46), `Vehicle Bulk {runId}-015` (target TC-FA-CAT-47), dan `Accessory {runId}-015` dengan anak `Cable {runId}-015` (target TC-FA-CAT-47). Hook `after` menghapus sisa kategori bersuffix `{runId}-015` bila masih ada.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-46: Delete-Only menghapus kategori leaf bersih sampai sukses

1. Ketik Search `Vehicle {runId}-015`, tekan Enter
2. Klik elipsis (⋯) baris `Vehicle {runId}-015`
3. Klik `Delete`
4. Verifikasi dialog `Delete Category` D-09 tampil
5. Klik `[Delete]` pada dialog
6. Verifikasi toast sukses `Success, category has been deleted.`
7. Verifikasi baris `Vehicle {runId}-015` hilang dari tabel
8. Verifikasi node `Vehicle {runId}-015` hilang dari sidebar
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-47: Delete-Only menjalankan Bulk Delete sampai sukses

10. Ketik Search `{runId}-015`, tekan Enter
11. Centang baris `Vehicle Bulk {runId}-015`
12. Centang baris `Accessory {runId}-015`
13. Klik `[Delete]` pada Bulk Action Bar
14. Verifikasi dialog `Delete Categories` D-11 tampil
15. Klik `[Delete]` pada dialog
16. Verifikasi toast sukses `Success, category has been deleted.`
17. Verifikasi baris `Vehicle Bulk {runId}-015` terhapus
18. Verifikasi baris `Accessory {runId}-015` terhapus
19. Verifikasi anak `Cable {runId}-015` terhapus dan tidak ada di sidebar
20. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix positif per aksi (bagian 3a): aksi Delete dan Bulk Delete berhasil untuk role berhak. TC sumber tidak memuat kombinasi Total Control atau role lain untuk dua aksi ini; kombinasi itu bukan bagian spec ini.
- Penyimpangan data (S-06, S-12): TC sumber menghapus baris seed `Vehicle`, `Accessory`, dan `Cable` dari Pre-setup #20. Spec menghapus kategori seed milik spec dengan struktur sama (leaf bersih; induk berisi satu anak) agar pohon Pre-setup tidak berubah. Nama pada langkah dan asersi memakai nilai bersuffix.
- Langkah penghubung (S-03, R-16): langkah 1 dan 10 (Search untuk menemukan baris target), langkah 9 dan 20 (mengosongkan Search sebelum langkah berikutnya).
- Temuan untuk QA:
  - TC-FA-CAT-47 Expected c menyebut anak `Cable` terhapus tetapi tidak memberi langkah observasinya; spec mengasersi lewat sidebar dengan toast sukses sebagai anchor (8b butir 2).
  - TC-FA-CAT-46 dan TC-FA-CAT-47 memakai baris seed Pre-setup #20 sebagai target hapus (bertentangan dengan S-06); spec memakai kategori milik spec (lihat butir penyimpangan data).
