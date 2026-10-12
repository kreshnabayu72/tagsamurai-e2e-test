---
id: TC-GS-BRAND-E2E-063-sync-fams-form-dan-agregasi-used-by
title: "Sinkronisasi Brand ke Fixed Asset: Opsi Form Asset Name, Rename, dan Agregasi Used By (Items)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-216
  - TC-GS-BRAND-217
  - TC-GS-BRAND-218
  - TC-GS-BRAND-205
coverage:
  web: automated
---

# Sinkronisasi Brand ke Fixed Asset: Opsi Form Asset Name, Rename, dan Agregasi Used By (Items)

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Admin FAMS (hanya lewat API, tanpa login UI) | Admin FAMS Client A (Tari Wulandari) | `famsAdmin_automated_qaTeam1@qwertysystem.net` | `FA_ADMIN_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand. Akun Admin FAMS adalah fixture baru (Tabel Data Uji Pre-setup) yang disediakan tim FE; ia berhak Create dan Delete Asset Name FAMS.
- Environment variable: `GS_TC_PASSWORD`, `FA_ADMIN_PASSWORD` (`FA_ADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Tidak ada data Pre-setup bersama yang dipakai atau diubah; seluruh objek aksi tulis milik spec ini (suffix `{runId}-063`, bagian 5 konvensi).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Tidal Co {runId}-063` (D-11): dibuat spec lewat UI pada TC-GS-BRAND-216 (setara dependensi TC-GS-BRAND-56).
  - `Xenon Bebas {runId}-063` (D-17): brand bebas relasi, di-seed lewat API di hook `before`, dihapus lewat UI pada TC-GS-BRAND-218 (setara dependensi TC-GS-BRAND-95).
  - `Rename Fams Co {runId}-063` (D-47): brand yang dipakai Asset Name FAMS `Rename Item {runId}-063`, keduanya di-seed lewat API di hook `before`. Pada TC-GS-BRAND-217 di-rename menjadi `Rename Fams Baru {runId}-063`, lalu dikembalikan ke `Rename Fams Co {runId}-063`.
  - `Aggregate Co {runId}-063` (D-49): brand yang dipakai 1 Asset Name FAMS `Agg Item {runId}-063`, keduanya di-seed lewat API di hook `before`.
  - Asset Name FAMS `Pallet Jack {runId}-063` dengan Brand `Aggregate Co {runId}-063`: dibuat dan dihapus oleh Admin FAMS lewat API pada TC-GS-BRAND-205.
- Nilai field wajib lain untuk Asset Name FAMS yang dibuat lewat API (`Rename Item`, `Agg Item`, dan `Pallet Jack`; PRD `fixed-asset/settings-asset-name` §4.3.1: Category daun, TAG Type minimal 1, UoM). Fixture `fixtures/brand.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `assetName.category` | Category (kategori daun) | disediakan tim FE |
  | `assetName.tagType` | TAG Type (minimal 1 opsi) | disediakan tim FE |
  | `assetName.uom` | UoM | disediakan tim FE |

- Kemampuan teknis: Admin FAMS sebagai sesi API (login lewat API dengan `Spectra.env.FA_ADMIN_PASSWORD`) untuk menambah dan menghapus Asset Name FAMS tanpa melewati sesi UI Global Settings.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Tidal Co`, `Xenon Bebas`, `Aggregate Co`, dan `Rename Fams Co` atau `Rename Fams Baru` (nama yang masih ada) bersuffix `{runId}-063`; hapus Asset Name FAMS `Rename Item`, `Agg Item`, dan `Pallet Jack` bersuffix `{runId}-063` bila masih ada (Asset Name dihapus sebelum brand-nya).
- Tidak ada state global lain yang diubah.
- TC-GS-BRAND-216, 217, 218, 205: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-216: Brand baru muncul di opsi Brand form Create Asset Name FAMS (pembuatan Brand)

1. Klik [+ Brand], isi Brand Name `Tidal Co {runId}-063`, klik [Submit]
2. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-217: Rename Brand tercermin di Asset Name FAMS yang memakainya

3. Search `Rename Fams Co {runId}-063` pada tabel Brand, klik `⋯` pada baris tersebut > Edit, ubah Brand Name menjadi `Rename Fams Baru {runId}-063`, klik [Save]
4. Buka Asset Name `Rename Item {runId}-063` di FAMS
5. Verifikasi Rename Item menampilkan Brand `Rename Fams Baru {runId}-063` tanpa reload
6. Edit Rename Item, klik [Save] tanpa mengubah Brand
7. Verifikasi Save di FAMS sukses
8. Verifikasi Brand Rename Item tetap `Rename Fams Baru {runId}-063`
9. Buka Global Settings > Master Reference > Brand, Search `Rename Fams Baru {runId}-063`, rename kembali menjadi `Rename Fams Co {runId}-063`, klik [Save]

### TC-GS-BRAND-205: Agregasi Item Type mencerminkan perubahan FAMS tanpa disimpan di Brand

10. Search `Aggregate Co {runId}-063` pada tabel Brand, klik `⋯` pada baris Aggregate Co > Detail → modal Brand Detail tampil
11. Admin FAMS (akun `famsAdmin_automated_qaTeam1@qwertysystem.net`, lewat API) menambah Asset Name `Pallet Jack {runId}-063` dengan Brand `Aggregate Co {runId}-063`
12. Tutup lalu buka lagi Detail Aggregate Co
13. Verifikasi Detail menampilkan `Agg Item {runId}-063`
14. Verifikasi Detail menampilkan `Pallet Jack {runId}-063`
15. Verifikasi Detail menampilkan `Total Item: 2`
16. Tutup Detail, perhatikan sel Used By (Items) baris Aggregate Co di tabel
17. Verifikasi sel Used By (Items) baris Aggregate Co di tabel menampilkan `2`
18. Admin FAMS menghapus Asset Name `Pallet Jack {runId}-063`
19. Search ulang `Aggregate Co {runId}-063` pada tabel Brand
20. Verifikasi Used By (Items) baris Aggregate Co kembali `1` (Post Condition: Aggregate Co kembali 1 item)

### TC-GS-BRAND-218: Brand terhapus hilang dari opsi Brand FAMS (sekaligus opsi TC-GS-BRAND-216)

21. Search `Xenon Bebas {runId}-063` pada tabel Brand, klik `⋯` pada baris tersebut > Delete → dialog `Delete Brand` tampil, klik [Delete]
22. Verifikasi toast sukses: "Success, brand has been deleted."
23. Buka form Create Asset Name FAMS (Fixed Asset > Settings > Asset Master > Create Asset Name)
24. Buka field Brand
25. Verifikasi opsi `Tidal Co {runId}-063` tersedia tanpa reload (TC-GS-BRAND-216 Expected Result a)
26. Verifikasi `Xenon Bebas {runId}-063` tidak ada di opsi Brand (TC-GS-BRAND-218 Expected Result a)
27. Tutup form Create Asset Name lewat `✕` (form tidak berisi perubahan, tanpa dialog Unsaved Changes)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: 216 (hanya pembuatan Brand), 217, lalu 205 sesudah rename 217 dikembalikan; Delete (218) paling akhir (prinsip 5). Form Create Asset Name FAMS dibuka satu kali di akhir untuk memverifikasi opsi TC-GS-BRAND-216 (Tidal Co ada) dan TC-GS-BRAND-218 (Xenon Bebas tidak ada), sehingga jumlah buka form tidak melebihi jumlah kejadian menutup (prinsip 6).
- Dependensi (TC-GS-BRAND-56, 95) dijalankan sebagai langkah di spec ini, bukan menumpang spec lain. `Xenon Bebas` di-seed lewat API karena pembuatannya bukan objek uji.
- Langkah 20 (Used By (Items) kembali `1`) berasal dari Post Condition TC-GS-BRAND-205, bukan dari Expected Result.
- Langkah penghubung: langkah 3, 9, 10, 19, dan 21 (Search baris target pada tabel Brand), langkah 12 dan 16 (menutup lalu membuka Detail, dan menutup Detail, sesuai Langkah Uji TC-GS-BRAND-205), dan langkah 27 (menutup form bersih).
- Kebutuhan akun Admin FAMS (`FA_ADMIN_PASSWORD`), fixture nilai field wajib Asset Name FAMS (`fixtures/brand.json`), dan seeding Asset Name `Rename Item` dan `Agg Item` sudah dicatat sebagai kebutuhan di Prerequisites; fixture belum ada.
