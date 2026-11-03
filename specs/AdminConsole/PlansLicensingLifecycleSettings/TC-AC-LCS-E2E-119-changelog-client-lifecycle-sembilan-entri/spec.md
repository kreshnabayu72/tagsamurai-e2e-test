---
id: TC-AC-LCS-E2E-119-changelog-client-lifecycle-sembilan-entri
title: "Isi Entri Changelog Client Lifecycle: Save Sembilan Field Mencatat Sembilan Entri"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-469
coverage:
  web: automated
---

# Isi Entri Changelog Client Lifecycle: Save Sembilan Field Mencatat Sembilan Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Data uji: Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-469: Save 9 field sekaligus pada tab Client Lifecycle mencatat tepat 9 entri

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Catat total entri pada footer modal sebagai baseline N0 (tab Client Lifecycle)
4. Tutup modal dengan `[✕]`
5. Ubah Notify Plan Owner Before Event menjadi `60`
6. Ubah First Reminder Before Event menjadi `45`
7. Ubah Second Reminder Before Event menjadi `14`
8. Ubah Final Reminder Before Event menjadi `3`
9. Ubah Grace Period Duration menjadi `20`
10. Ubah Archive Period Duration menjadi `25`
11. Ubah Purge Warning Email menjadi `12`
12. Ubah Purge Urgent Warning Email menjadi `4`
13. Ubah Post-Purge Retention menjadi `1000`
14. Klik `[Save]` dan tunggu toast sukses
15. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
16. Verifikasi footer menunjukkan total entri baseline N0 ditambah 9 (tepat 9 entri baru)
17. Verifikasi seluruh 9 entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
18. Verifikasi entri baru tampil: Field `Notify Plan Owner Before Event`, Old Value `45`, New Value `60`
19. Verifikasi entri baru tampil: Field `First Reminder Before Event`, Old Value `30`, New Value `45`
20. Verifikasi entri baru tampil: Field `Second Reminder Before Event`, Old Value `7`, New Value `14`
21. Verifikasi entri baru tampil: Field `Final Reminder Before Event`, Old Value `1`, New Value `3`
22. Verifikasi entri baru tampil: Field `Grace Period Duration`, Old Value `30`, New Value `20`
23. Verifikasi entri baru tampil: Field `Archive Period Duration`, Old Value `30`, New Value `25`
24. Verifikasi entri baru tampil: Field `Purge Warning Email`, Old Value `10`, New Value `12`
25. Verifikasi entri baru tampil: Field `Purge Urgent Warning Email`, Old Value `2`, New Value `4`
26. Verifikasi entri baru tampil: Field `Post-Purge Retention`, Old Value `730`, New Value `1000`
27. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
28. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 2 sampai 4 (membaca baseline N0 lalu menutup modal, S-12).
- Entri baru dicari di antara baris teratas urutan Newest First; urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- TC-AC-LCS-438 (entri terbaru di atas setelah Save baru, Dataset L) ada di spec 192 (`TC-AC-LCS-E2E-192-changelog-client-lifecycle-entri-terbaru-di-atas`).
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.
