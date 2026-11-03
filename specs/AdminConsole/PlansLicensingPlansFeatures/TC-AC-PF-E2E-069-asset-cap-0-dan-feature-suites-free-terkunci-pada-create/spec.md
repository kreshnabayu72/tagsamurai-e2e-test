---
id: TC-AC-PF-E2E-069-asset-cap-0-dan-feature-suites-free-terkunci-pada-create
title: "Asset Cap 0 dan Feature Suites Free Terkunci pada Create Default Plan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-182
  - TC-AC-PF-183
coverage:
  web: automated
---

# Asset Cap 0 dan Feature Suites Free Terkunci pada Create Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan V2 (Default FAMS dengan 2 Paid aktif `Growth` dan `Professional`; Free `Starter` sudah di-archive) untuk blok TC-AC-PF-183 dan Dataset Plan V (Default FAMS dengan 3 Paid aktif `Growth`, `Professional`, `Enterprise`; Free `Starter` sudah di-archive) untuk blok TC-AC-PF-182. `before` menyemai Dataset Plan V2; langkah penghubung (langkah 10) memulihkan FAMS ke Dataset Plan V.
- Data Dinamis: `Paket Cap Nol {runId}-069` (default plan Free FAMS dengan Asset cap `0`, dibuat pada TC-AC-PF-182; dihapus fixture BE di hook `after`).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-069`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-183: Feature Suites plan Free pada Create Default Plan tampil tetapi Disabled dan terkunci ke None

1. Klik `+ Default Plan`
2. Pilih Product `FAMS` dan Pricing Type `Free`
3. Amati SectionCard Feature Suites dan coba buka dropdown Borrowing
4. Verifikasi untuk Free: SectionCard Feature Suites tetap tampil (visible)
5. Verifikasi untuk Free: semua field Feature Suites Disabled
6. Verifikasi untuk Free: semua field Feature Suites bernilai `None`
7. Ganti Pricing Type ke `Paid`
8. Verifikasi untuk Paid: field Feature Suites aktif dan dapat dipilih
9. Klik `[Clear Field]`
10. Pulihkan Product FAMS ke Dataset Plan V lewat fixture BE, lalu klik segmen `Plans & Features` pada breadcrumb

### TC-AC-PF-182: Asset cap bernilai 0 sah untuk plan Free dan tersimpan sebagai tanpa kuota

11. Klik `+ Default Plan`
12. Pilih Product `FAMS`, Pricing Type `Free`, isi Plan Name `Paket Cap Nol {runId}-069`
13. Isi Asset cap dengan `0` lalu klik `[Submit]`
14. Verifikasi toast sukses: "Success, default plan has been created."
15. Verifikasi tidak ada pesan error inline `Value must be a whole number of 0 or more`
16. Buka Tab Overview
17. Verifikasi Tab Overview baris Asset cap bernilai `0`

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` pada langkah 9 mengembalikan form ke keadaan bersih; langkah 10 memulihkan data FAMS lewat fixture BE (A-6) dan membuka ulang halaman lewat breadcrumb pada form bersih. Blok TC-AC-PF-183 (tanpa penulisan data) ditempatkan sebelum blok TC-AC-PF-182 yang membuat plan (S-10).
- Asersi `tidak ada pesan error` pada TC-AC-PF-182 ditulis sesudah toast sukses sebagai anchor bahwa respons server sudah diproses (bagian 8b butir 2).
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-183 Langkah 2 meminta "coba buka dropdown Borrowing" tanpa Expected tersendiri bagi hasil percobaan itu selain field Disabled; spec menulis percobaan sebagai aksi dan mengasersi Disabled dan nilai `None`.
