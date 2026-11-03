---
id: TC-AC-LCS-E2E-120-changelog-multi-field-trial-dan-free
title: "Isi Entri Changelog: Save Enam Field Trial Settings dan Satu Field Free Plan Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-466
  - TC-AC-LCS-467
coverage:
  web: automated
---

# Isi Entri Changelog: Save Enam Field Trial Settings dan Satu Field Free Plan Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Data uji Trial Settings: Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`. Data uji Free Plan Settings: Free Plan Duration `400`.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-466: Save 6 field sekaligus pada tab Trial Settings mencatat tepat 6 entri

1. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
2. Catat total entri pada footer modal sebagai baseline N0 (tab Trial Settings)
3. Tutup modal dengan `[✕]`
4. Ubah Max Trial Duration menjadi `45`
5. Ubah Max Trial Asset Quota menjadi `100`
6. Ubah Max Trial Concurrent User Quota menjadi `20`
7. Aktifkan Switch Require Approval for Trial Activation (status `ON`)
8. Ubah First Notification menjadi `14`
9. Ubah Second Notification menjadi `3`
10. Klik `[Save]` dan tunggu toast sukses
11. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
12. Verifikasi footer menunjukkan total entri baseline N0 (tab Trial Settings) ditambah 6 (tepat 6 entri baru)
13. Verifikasi seluruh 6 entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
14. Verifikasi entri baru tampil: Field `Max Trial Duration`, Old Value `30`, New Value `45`
15. Verifikasi entri baru tampil: Field `Max Trial Asset Quota`, Old Value `50`, New Value `100`
16. Verifikasi entri baru tampil: Field `Max Trial Concurrent User Quota`, Old Value `10`, New Value `20`
17. Verifikasi entri baru tampil: Field `Require Approval for Trial Activation`, Old Value `Off`, New Value `On`
18. Verifikasi entri baru tampil: Field `First Notification`, Old Value `7`, New Value `14`
19. Verifikasi entri baru tampil: Field `Second Notification`, Old Value `1`, New Value `3`
20. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
21. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan
22. Tutup modal dengan `[✕]`

### TC-AC-LCS-467: Save 1 field sekaligus pada tab Free Plan Settings mencatat tepat 1 entri

23. Klik tab Free Plan Settings
24. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
25. Catat total entri pada footer modal sebagai baseline N0 (tab Free Plan Settings)
26. Tutup modal dengan `[✕]`
27. Ubah Free Plan Duration menjadi `400`
28. Klik `[Save]` dan tunggu toast sukses
29. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
30. Verifikasi footer menunjukkan total entri baseline N0 (tab Free Plan Settings) ditambah 1 (tepat 1 entri baru)
31. Verifikasi seluruh 1 entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
32. Verifikasi entri baru tampil: Field `Free Plan Duration`, Old Value `365`, New Value `400`
33. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
34. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 sampai 3 dan 24 sampai 26 (membaca baseline N0 lalu menutup modal, S-12); menutup modal sebelum pindah tab.
- Entri baru dicari di antara baris teratas urutan Newest First; urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.
