---
id: TC-GS-USER-E2E-166-pencatatan-switch-active-tab-role-di-changelog-modal-system-log-dan-activity-log
title: "Pencatatan Log: Switch Active OFF dan ON di Tab Role Tercatat sebagai Remove dan Assign di Changelog Role, Modal Changelog User, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1101
coverage:
  web: automated
---

# Pencatatan Log: Switch Active OFF dan ON di Tab Role Tercatat sebagai Remove dan Assign di Changelog Role, Modal Changelog User, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`: `Ahmad Fauzi {runId}-166` (padanan Ahmad Fauzi, Tabel Pre-setup No. 13), email `ahmadfauzi+{runId}-166@qwertysystem.net`, Activated, baris `Manage TAG` Active.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan assignment role lewat API; membaca jumlah entri audit trail lewat BE tepat sebelum aksi pemicu (8b butir 10, S-12) pada empat surface: Changelog Role `Ahmad Fauzi {runId}-166` (J1), Modal Changelog User untuk User Name `Ahmad Fauzi {runId}-166` (J2), System Log Siti Nurhaliza (J3), dan Activity Log (J4); jam server dan jam browser tidak digeser.
- State global yang diubah: tidak ada; audit trail permanen bertambah. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus user seed.

## Test Steps

1. Catat baseline jumlah entri lewat kemampuan baca BE sebelum aksi pemicu: J1 (Changelog Role `Ahmad Fauzi {runId}-166`), J2 (Modal Changelog User untuk `Ahmad Fauzi {runId}-166`), J3 (System Log Siti Nurhaliza), J4 (Activity Log)
2. Klik icon Search, ketik `Ahmad Fauzi {runId}-166`, tekan Enter
3. Klik Name `Ahmad Fauzi {runId}-166` di User List
4. Klik Tab `Role`
5. Matikan switch Active baris `Manage TAG`
6. Tunggu aksi selesai (switch Active baris `Manage TAG` berubah OFF)
7. Nyalakan switch Active baris `Manage TAG`
8. Tunggu aksi selesai (switch Active baris `Manage TAG` berubah ON)

### Changelog Role (Tab Role)

9. Klik icon Changelog di Tab Role
10. Verifikasi jumlah entri Changelog Role bertambah tepat 2 dari J1 (1 baris per toggle)
11. Verifikasi baris `Remove | Manage TAG | Access | Assigned | — | Siti N`
12. Verifikasi baris `Assign | Manage TAG | Access | — | Assigned | Siti N`
13. Verifikasi tidak ada baris Action `Activate`, `Deactivate`, atau `Edit` di antara dua entri baru
14. Tutup Changelog lewat `✕`

### Modal Changelog User

15. Klik menu User di sidebar Global Settings
16. Klik icon Changelog pada Table Tools
17. Klik icon Search pada Modal Changelog, ketik `Ahmad Fauzi {runId}-166`, tekan Enter
18. Verifikasi jumlah entri hasil Search bertambah tepat 2 dari J2 (1 baris per toggle)
19. Verifikasi baris `Remove | Ahmad Fauzi {runId}-166 | Manage TAG | Assigned | — | Siti N`
20. Verifikasi baris `Assign | Ahmad Fauzi {runId}-166 | Manage TAG | — | Assigned | Siti N`
21. Verifikasi tidak ada baris Action `Activate`, `Deactivate`, atau `Edit` di antara dua entri baru
22. Tutup Modal Changelog lewat `✕`

### System Log Siti Nurhaliza

23. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
24. Klik Name `Siti Nurhaliza` di User List
25. Klik Tab `System Log`
26. Verifikasi jumlah entri System Log bertambah tepat 2 dari J3 (1 baris per toggle)
27. Verifikasi baris `Remove | System Role | Ahmad Fauzi {runId}-166 | Manage TAG | Assigned | —`
28. Verifikasi baris `Assign | System Role | Ahmad Fauzi {runId}-166 | Manage TAG | — | Assigned`
29. Verifikasi tidak ada baris Action `Activate`, `Deactivate`, atau `Edit` di antara dua entri baru

### Activity Log

30. Buka Global Settings > Activity Log
31. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari J4 (1 baris per toggle)
32. Verifikasi baris `Remove | Manage TAG | Access | Assigned | — | Siti N`
33. Verifikasi baris `Assign | Manage TAG | Access | — | Assigned | Siti N`
34. Verifikasi tidak ada baris Action `Activate`, `Deactivate`, atau `Edit` di antara dua entri baru

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke surface log. Spec ini kelas pencatatan (fungsional) dan memuat satu TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline), 2 dan 23 (Search nama target sebelum Klik Name, R-16), 6 dan 8 (Tunggu aksi selesai sebelum membuka log), 14 dan 22 (menutup modal sebelum pindah surface), 15 (kembali ke User List), 17 (Search di Modal Changelog), 30 (membuka Activity Log).
- Cara baca (S-12, S-14): entri baru dibaca setelah selisih jumlah dari baseline dibuktikan; kedua entri baru dibuat pada menit yang sama, sehingga spec mengasersi himpunan dua baris teratas tanpa mengandalkan urutan `Remove` lalu `Assign`.
- P-1: TC-GS-USER-1101 butir e ("tidak ada Action `Activate`/`Deactivate` dan tidak ada baris `Edit`") diasersi di spec ini lewat selisih jumlah entri terhadap baseline dan isi dua entri baru (langkah 13, 21, 29, 34), bukan lewat spec absence, karena spec absence 147 tidak memuat aksi switch Active Tab Role dan dua entri itu dibangun dalam alur ini (S-05).
- Temuan untuk QA:
  - TC-GS-USER-1101 butir d tidak menyebut kolom Activity Log selain Modified By; spec mengasersi baris dengan format yang sama dengan Changelog Role dan Modified By `Siti N` (R-14).
  - TC-GS-USER-1101 butir b menyebut kolom User Name `Ahmad Fauzi` tanpa urutan kolom Modal Changelog User; spec memakai format baris TC-GS-USER-1052 (`Action | User Name | Role | Old | New | Modified By`).
  - TC-GS-USER-1101 butir a, c, dan d tidak menyebut cara memilih baris di Activity Log yang besar; spec mengandalkan baris teratas sesudah selisih jumlah dibuktikan.
  - TC-GS-USER-1101 memakai user Pre-setup (Ahmad Fauzi); spec memakai seed milik spec (S-06) dan nama bersuffix pada kolom log (R-06).
