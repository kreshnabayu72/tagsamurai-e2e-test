---
id: TC-GS-USER-E2E-165-remove-access-global-settings-role-active-dan-inactive-retained
title: "Remove Access Global Settings: Role Active dan Inactive-Retained Dihapus Tanpa Pemulihan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1099
coverage:
  web: automated
---

# Remove Access Global Settings: Role Active dan Inactive-Retained Dihapus Tanpa Pemulihan

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`: `Dewi Lestari {runId}-165` (padanan Dewi Lestari, Tabel Pre-setup No. 12), email `dewilestari+{runId}-165@qwertysystem.net`, Activated, Access `Global Settings`, dengan baris `Manage files` Active (Read saja) dan baris `Manage hardware` inactive-retained (Create, Read, Update tersimpan).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan assignment role Active dan inactive-retained beserta nilai CRUD tersimpan lewat API.
- State global yang diubah: tidak ada; yang berubah hanya assignment role user seed milik spec. Spec ini menghapus data sehingga dijalankan sesudah spec lain (suite serial). Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus user seed.

## Test Steps

1. Klik icon Search, ketik `Dewi Lestari {runId}-165`, tekan Enter
2. Klik (⋯) baris `Dewi Lestari {runId}-165` → `Edit`
3. Hapus pilihan Access `Global Settings`
4. Klik `[Save]`
5. Verifikasi dialog Title `Remove Access`
6. Klik `[Remove]`
7. Tunggu aksi selesai (Popup Edit tertutup)
8. Klik (⋯) baris `Dewi Lestari {runId}-165` → `Edit`
9. Pilih Access `Global Settings`
10. Klik `[Save]`
11. Tunggu aksi selesai (Popup Edit tertutup)
12. Klik Name `Dewi Lestari {runId}-165` di User List
13. Klik Tab `Role`
14. Verifikasi switch Active keenam baris OFF
15. Verifikasi seluruh checkbox Tab Role disabled
16. Verifikasi User Type di General Information `Basic`
17. Nyalakan switch Active baris `Manage hardware`
18. Verifikasi checkbox Read baris `Manage hardware` tercentang dan disabled
19. Verifikasi checkbox Create dan Update baris `Manage hardware` tidak tercentang

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama target; nilainya bertahan di kotak Search sampai langkah 12, R-16), 7 dan 11 (Tunggu aksi selesai: Popup Edit tertutup sebelum langkah berikutnya), 6 (`[Remove]` dikonfirmasi tanpa asersi hasil karena TC tidak memberi Expected).
- Langkah 17 sampai 19 mengikuti TC-GS-USER-1099 langkah 5; "baris `Manage hardware` dibuat baru" diasersi lewat nilai CRUD yang tidak dipulihkan (langkah 18 dan 19).
- Temuan untuk QA:
  - TC-GS-USER-1099 Expected a ("Dewi Lestari masih punya 1 role Active, yaitu Manage files") tidak menyebut teks isi dialog Remove Access untuk produk Global Settings; spec hanya mengasersi Title `Remove Access`, dan alasan dialog (masih ada 1 role Active) menjadi precondition seed.
  - TC-GS-USER-1099 langkah 1 "hapus pilihan Global Settings" dan langkah 3 "pilih Global Settings" tidak menyebut kontrol Access; spec memakai field Access pada Popup Edit seperti TC Remove Access lain.
  - TC-GS-USER-1099 Post Condition ("Dewi Lestari punya baris Manage hardware Active (Read saja); tidak ada baris role lain") tanpa langkah observasi tersendiri; diverifikasi sebagian lewat langkah 17 sampai 19.
  - TC-GS-USER-1099 memakai user Pre-setup (Dewi Lestari); spec memakai seed milik spec (S-06).
