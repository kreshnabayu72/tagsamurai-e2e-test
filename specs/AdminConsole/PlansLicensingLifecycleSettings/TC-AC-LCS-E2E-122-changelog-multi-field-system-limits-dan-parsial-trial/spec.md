---
id: TC-AC-LCS-E2E-122-changelog-multi-field-system-limits-dan-parsial-trial
title: "Isi Entri Changelog: Save Enam Field System Limits dan Dua dari Enam Field Trial Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-472
  - TC-AC-LCS-473
coverage:
  web: automated
---

# Isi Entri Changelog: Save Enam Field System Limits dan Dua dari Enam Field Trial Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Data uji System Limits: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`. Data uji Trial Settings: Max Trial Asset Quota `75`, First Notification `10`.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-472: Save 6 field sekaligus pada tab System Limits mencatat tepat 6 entri

1. Klik tab System Limits
2. Klik icon Changelog di pojok kanan atas panel tab System Limits
3. Catat total entri pada footer modal sebagai baseline N0 (tab System Limits)
4. Tutup modal dengan `[✕]`
5. Ubah Bulk Transaction Row Limit menjadi `2000`
6. Ubah Selection Limit menjadi `1500`
7. Ubah Register Asset Bulk Limit menjadi `2500`
8. Ubah Hierarchy Depth Limit menjadi `60`
9. Ubah Master Data Count Limit menjadi `20000`
10. Ubah Max Visible Columns menjadi `25`
11. Klik `[Save]` dan tunggu toast sukses
12. Klik icon Changelog di pojok kanan atas panel tab System Limits
13. Verifikasi footer menunjukkan total entri baseline N0 ditambah 6 (tepat 6 entri baru)
14. Verifikasi seluruh 6 entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
15. Verifikasi entri baru tampil: Field `Bulk Transaction Row Limit`, Old Value `1000`, New Value `2000`
16. Verifikasi entri baru tampil: Field `Selection Limit`, Old Value `1000`, New Value `1500`
17. Verifikasi entri baru tampil: Field `Register Asset Bulk Limit`, Old Value `1000`, New Value `2500`
18. Verifikasi entri baru tampil: Field `Hierarchy Depth Limit`, Old Value `50`, New Value `60`
19. Verifikasi entri baru tampil: Field `Master Data Count Limit`, Old Value `10000`, New Value `20000`
20. Verifikasi entri baru tampil: Field `Max Visible Columns`, Old Value `20`, New Value `25`
21. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
22. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan
23. Tutup modal dengan `[✕]`

### TC-AC-LCS-473: Save dua dari enam field tab Trial Settings hanya mencatat dua entri

24. Klik tab Trial Settings
25. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
26. Catat total entri pada footer modal sebagai baseline N0 (tab Trial Settings)
27. Tutup modal dengan `[✕]`
28. Ubah Max Trial Asset Quota dari `50` menjadi `75`
29. Ubah First Notification dari `7` menjadi `10`
30. Klik `[Save]` dan tunggu toast sukses
31. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
32. Verifikasi footer menunjukkan total entri baseline N0 ditambah 2 (tepat 2 entri baru)
33. Verifikasi entri baru tampil: Field `Max Trial Asset Quota`, Old Value `50`, New Value `75`
34. Verifikasi entri baru tampil: Field `First Notification`, Old Value `7`, New Value `10`
35. Verifikasi tidak ada entri baru untuk Max Trial Duration, Max Trial Concurrent User Quota, Require Approval for Trial Activation, dan Second Notification

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: membaca baseline N0 lalu menutup modal (S-12) dan menutup modal sebelum pindah tab.
- Entri baru dicari di antara baris teratas urutan Newest First; urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.
