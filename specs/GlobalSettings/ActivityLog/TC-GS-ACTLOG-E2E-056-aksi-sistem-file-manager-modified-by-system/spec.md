---
id: TC-GS-ACTLOG-E2E-056-aksi-sistem-file-manager-modified-by-system
title: "Aksi Sistem File Manager: Modified By System"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-211
coverage:
  web: automated
---

# Aksi Sistem File Manager: Modified By System

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup: tidak ada data tetap yang diubah atau dipakai sebagai target aksi.
- Data Dinamis: berkas `Auto Purge {runId}-056.png` di Recycle Bin File Manager Client A yang melewati batas auto-purge. Berkas dibuat lewat seed BE di hook `before`. Hook `after` menghapus permanen berkas itu bila masih ada di Recycle Bin (tanpa berasumsi job auto-purge berhasil).
- Kemampuan teknis (disediakan tim FE/BE; kelas harness eksternal: background job): seed BE berkas di Recycle Bin yang melewati batas auto-purge dan pemicu job auto-purge sehingga sistem menghapusnya, tanpa mengarang endpoint dan tanpa menggeser jam server (TC menyebut pemajuan jam server atau seed BE; spec memilih seed BE).
- Spec hanya menambah baris log. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-211: Aksi sistem File Manager menampilkan Modified By System

1. Picu auto-purge sehingga sistem menghapus permanen berkas `Auto Purge {runId}-056.png` dari Recycle Bin dan tunggu job selesai
2. Buka Global Settings > Activity Log > User Action
3. Ketik Search `Auto Purge {runId}-056.png`, tekan Enter
4. Verifikasi entri auto-purge berkas `Auto Purge {runId}-056.png` tampil
5. Verifikasi sel Modified By entri bernilai `System` utuh (tanpa singkatan)
6. Arahkan kursor ke sel Modified By entri
7. Verifikasi tooltip `System` tampil
8. Klik icon Filter, buka daftar opsi field Modified By
9. Verifikasi daftar opsi Modified By memuat `System`

### Pemulihan state akhir spec

10. Tutup Filter Panel tanpa menerapkan filter, lalu klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 (menutup Filter Panel dan membersihkan Search). Menunggu job selesai pada langkah 1 mendahului pembukaan Activity Log (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline entri adalah nol karena nama berkas bersuffix unik per run (S-12).
- Pembagian TC lintas spec: TC-GS-ACTLOG-204 dan 210 (aksi File Manager oleh admin) ada di spec 053.
- Temuan untuk QA:
  - TC-GS-ACTLOG-211 menyebut dua cara memicu auto-purge (jam server dimajukan atau seed BE) tanpa memilih; spec memilih seed BE dan mekanisme pemicunya disediakan tim FE/BE.
  - TC-GS-ACTLOG-211 tidak menyebut Action, Object, dan Name entri auto-purge; spec mencari entri lewat Search dengan nama berkas seed.
  - Kolom Automation TC-GS-ACTLOG-211 `Manual Only`; spec tetap ditulis dengan kebutuhan teknis di Prerequisites.
  - TC-GS-ACTLOG-211 tidak menyebut nama berkas; spec memakai berkas gambar `.png` karena File Manager hanya menerima PNG, JPG, dan JPEG.
