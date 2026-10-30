---
id: TC-GS-FILEMGR-E2E-061-plan-tier-tidak-digate
title: "File Manager Identik pada Seluruh Tier Plan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-243
coverage:
  web: automated
---

# File Manager Identik pada Seluruh Tier Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah state global tier plan Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE; TC dan PRD tidak menyebut cara pindah tier, lihat Temuan untuk QA): memindah tier plan Client uji ke Starter, Growth, Professional, dan Enterprise, dan memuat ulang halaman sesudahnya.
- State global yang diubah: tier plan Client uji. Hook `before` mencatat tier awal; hook `after` memulihkan tier awal walau spec gagal di tengah.
- Tabel "Tier yang diuji" (langkah 1 sampai 9 diulang per baris; file yang dihapus berbeda per tier):

  | Tier | File aktif milik spec yang dihapus |
  |---|---|
  | Starter | `tier-starter-{runId}-061.jpg` |
  | Growth | `tier-growth-{runId}-061.jpg` |
  | Professional | `tier-professional-{runId}-061.jpg` |
  | Enterprise | `tier-enterprise-{runId}-061.jpg` |

- Data milik spec (suffix `{runId}-061`, seeding lewat fixture BE di hook `before`; mekanisme seeding disediakan tim FE/BE): empat file aktif pada tabel di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-061` yang masih ada dan pulihkan tier awal.

## Test Steps

### TC-GS-FILEMGR-243: File Manager tanpa gating tier

Untuk setiap baris pada tabel "Tier yang diuji", lakukan langkah 1 sampai 9:

1. Pindahkan tier plan Client uji ke tier pada baris tabel, lalu buka Global Settings > File Manager
2. Verifikasi halaman File Manager terbuka dan toolbar `Search | Filter | Download | Changelog | Recycle Bin` tampil
3. Verifikasi tidak ada tampilan upsell pada File Manager
4. Verifikasi tidak ada batas jumlah pada File Manager
5. Ketik Search nama file pada baris tabel, tekan Enter, klik ikon (⋯) baris file tersebut, klik `Delete`, lalu klik [Delete]
6. Verifikasi toast sukses: "Success, [File Name] has been deleted." dengan File Name file pada baris tabel
7. Klik tombol Recycle Bin di toolbar
8. Verifikasi modal Recycle Bin terbuka
9. Tutup modal Recycle Bin lewat `✕`

Sesudah keempat iterasi:

10. Verifikasi perilaku File Manager identik pada Starter, Growth, Professional, dan Enterprise (hasil langkah 2, 6, dan 8 sama pada keempat tier)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas state tenant (plan tier).
- Langkah 1 sampai 9 diulang untuk empat baris tabel "Tier yang diuji" (36 langkah setelah ekspansi, ditambah langkah 10). Idiom ulang per baris tabel (bagian 8b butir 7): tanpa langkah bersyarat dan `Verifikasi` tetap satu per klausa. Satu kelas (state tenant), tiap iterasi berdiri sendiri.
- Nama file Pre-setup tidak dipakai; TC menyebut "hapus satu file", sehingga spec men-seed satu file bersuffix per tier (S-06, S-11 seeding minimal).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (pindah tier dan buka halaman), langkah 9 (menutup modal Recycle Bin sebelum pindah tier berikutnya).
- Temuan untuk QA:
  - Cara memindah tier dan daftar tier "Starter, Growth, Professional, Enterprise" tidak didefinisikan di TC (Q-10); ditulis sebagai kemampuan yang disediakan tim FE.
  - Expected b ("tidak ada tampilan upsell, batas jumlah, atau perbedaan perilaku") bersifat universal tanpa langkah observasi spesifik di TC; spec mengasersi upsell dan batas jumlah pada tiap iterasi (langkah 3 dan 4) dan perbandingan lintas tier pada langkah 10.
