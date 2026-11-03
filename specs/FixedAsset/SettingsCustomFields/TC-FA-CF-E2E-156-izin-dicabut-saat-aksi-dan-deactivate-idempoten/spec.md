---
id: TC-FA-CF-E2E-156-izin-dicabut-saat-aksi-dan-deactivate-idempoten
title: "Izin Dicabut Saat Modal atau Dialog Terbuka dan Deactivate Idempoten"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-597
  - TC-FA-CF-599
  - TC-FA-CF-600
coverage:
  web: automated
---

# Izin Dicabut Saat Modal atau Dialog Terbuka dan Deactivate Idempoten

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite.
- Pelaku kedua TC-FA-CF-597: Total Control sesi 2 Company Alpha (Pre-setup #10) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Rina Putri) lewat sesi API (login API dengan `Spectra.env.FA_TC2_PASSWORD`, token tidak dihitung sebagai sesi web; lihat `suite.md`).
- Tabel "Role yang diuji" (ganti akun eksplisit pada langkah 12, 13, 23, dan 24; Company Alpha, pola email `<role>_automated_{namaCompany}@qwertysystem.net`):

| Role | Pre-setup | Email | Env password |
|---|---|---|---|
| Master-Update | #6 | `masterUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MU_PASSWORD` |
| Master-Delete | #7 | `masterDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MD_PASSWORD` |

  Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup Company Alpha (Pre-setup #11 dan #12; Master-Crud #8 dipakai mekanisme pencabutan capability): field `Asset Serial Tag`, `Storage Capacity`, dan `Legacy Tag`. Aksi TC-FA-CF-599 dan 600 ditolak sehingga data tidak berubah; `Asset Serial Tag` dinonaktifkan sesi API pada TC-FA-CF-597 dan dipulihkan hook `after` lewat seed reset Company Alpha (S-06). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis: Field Name hasil Edit yang ditolak `Storage Capacity Edit {runId}-156`.
- Kemampuan teknis: seed pencabutan capability Manage asset master data dari pemegang Update dan pemegang Delete lewat Pre-setup (disediakan tim FE/BE); sesi API aktor; kemampuan baca Modal Changelog dengan Search nama field; baseline jumlah entri dicatat sebelum aksi (S-12).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor (Total Control, pemegang Update, pemegang Delete) dan hook `after` memulihkannya (lihat `suite.md`).
- State global: capability pemegang Update dan pemegang Delete dicabut pada langkah 15 dan 26; hook `after` memulihkannya lewat seed reset Company Alpha dan mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-597: Deactivate field yang sudah Inactive karena aksi aktor lain

1. Catat jumlah entri Modal Changelog untuk Search `Asset Serial Tag` sebagai baseline
2. Geser switch Active baris `Asset Serial Tag` ke OFF sampai dialog Deactivate tampil
3. Sesi API (Rina Putri) menonaktifkan `Asset Serial Tag` hingga penonaktifan tersimpan
4. Klik `[Deactivate]` pada dialog
5. Verifikasi aksi berhasil tanpa error 500
6. Verifikasi status `Asset Serial Tag` tetap Inactive
7. Verifikasi tabel di-refresh ke status terkini
8. Buka Modal Changelog, ketik Search `Asset Serial Tag`, tekan Enter
9. Verifikasi Modal Changelog memuat entri Deactivate `Asset Serial Tag` dari sesi 2
10. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline (tidak ada entri log ganda)
11. Tutup Modal Changelog

### TC-FA-CF-599: capability dicabut saat modal Edit terbuka

12. Ganti akun: `Logout` dari Total Control Company Alpha (Sarah Johnson)
13. Login sebagai pemegang Update (Pre-setup #6) dengan `Spectra.env.FA_MU_PASSWORD`
14. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
15. Cabut capability Manage asset master data dari pemegang Update lewat Pre-setup
16. Ubah Field Name menjadi `Storage Capacity Edit {runId}-156`
17. Klik `[Save]`
18. Verifikasi toast error `You don't have permission to do this.` tampil
19. Verifikasi modal Edit tertutup otomatis
20. Verifikasi tabel di-refresh
21. Verifikasi elemen tulis tersembunyi
22. Verifikasi tidak ada perubahan data (baris `Storage Capacity` tetap)

### TC-FA-CF-600: capability dicabut saat dialog konfirmasi terbuka

23. Ganti akun: `Logout` dari pemegang Update
24. Login sebagai pemegang Delete (Pre-setup #7) dengan `Spectra.env.FA_MD_PASSWORD`
25. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil
26. Cabut capability Manage asset master data dari pemegang Delete lewat Pre-setup
27. Klik `[Delete]` pada dialog
28. Verifikasi dialog Delete tertutup
29. Verifikasi tabel di-refresh
30. Verifikasi toast `You don't have permission to do this.` tampil
31. Verifikasi field `Legacy Tag` tidak terhapus

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua pada TC-FA-CF-597 memicu state lewat sesi API (bukan konteks kedua kelas c), ditulis "... hingga ... tersimpan" (R-20); `P-2` tidak dipakai (keputusan 2026-10-30). Pencabutan capability pada TC-FA-CF-599 dan 600 adalah pemicu state lewat seed, bukan sesi kedua.
- P-1: klausa "tidak ada entri log ganda" TC-FA-CF-597 menempel pada state idempoten yang dibangun alur ini (sesi 2 menonaktifkan field saat dialog sesi 1 terbuka) dan diasersi dengan baseline (S-12, langkah 10); tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); bagian 3a, keputusan 2026-10-30.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline), langkah 8 dan 11 (membuka dan menutup Modal Changelog, Search, R-16), langkah 12, 13, 23, dan 24 (ganti akun eksplisit); hook `after` mengembalikan sesi ke akun default suite.
- Temuan untuk QA:
  - TC-FA-CF-597, 599, dan 600 bertanda Manual Only (dua sesi paralel) padahal pelaku kedua atau pencabut capability hanya memicu state; TC-FA-CF-599 dan 600 menyebut "lewat Pre-setup" tanpa menyebut mekanisme pencabutan capability.
  - Expected b TC-FA-CF-599 ("elemen tulis tersembunyi") tidak menyebut elemen yang diamati; spec mengasersinya sebagai satu `Verifikasi` umum.
  - Expected b TC-FA-CF-597 meminta "tidak ada entri log ganda" tanpa angka absolut; spec memakai selisih satu terhadap baseline.
