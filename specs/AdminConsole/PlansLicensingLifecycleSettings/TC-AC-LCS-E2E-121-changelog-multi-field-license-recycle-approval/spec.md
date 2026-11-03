---
id: TC-AC-LCS-E2E-121-changelog-multi-field-license-recycle-approval
title: "Isi Entri Changelog: Save Tiga Field License Timing, Satu Field Recycle Bin, dan Satu Field Approval Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-468
  - TC-AC-LCS-470
  - TC-AC-LCS-471
coverage:
  web: automated
---

# Isi Entri Changelog: Save Tiga Field License Timing, Satu Field Recycle Bin, dan Satu Field Approval Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Data uji License Timing: Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`.
- Parameter tab satu field (diulang di langkah 19 sampai 30):
  | Tab | Field | Old Value | New Value |
  |---|---|---|---|
  | Recycle Bin | Permanently Delete Recycle Bin | 30 | 45 |
  | Approval Settings | Approval Timeout | 3 | 7 |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-468: Save 3 field sekaligus pada tab License Timing mencatat tepat 3 entri

1. Klik tab License Timing
2. Klik icon Changelog di pojok kanan atas panel tab License Timing
3. Catat total entri pada footer modal sebagai baseline N0 (tab License Timing)
4. Tutup modal dengan `[✕]`
5. Ubah Managed Transition Time menjadi `48`
6. Ubah Managed Action Retry Delay menjadi `5`
7. Ubah Addon Reactivation Delay menjadi `7`
8. Klik `[Save]` dan tunggu toast sukses
9. Klik icon Changelog di pojok kanan atas panel tab License Timing
10. Verifikasi footer menunjukkan total entri baseline N0 ditambah 3 (tepat 3 entri baru)
11. Verifikasi seluruh 3 entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
12. Verifikasi entri baru tampil: Field `Managed Transition Time`, Old Value `24`, New Value `48`
13. Verifikasi entri baru tampil: Field `Managed Action Retry Delay`, Old Value `2`, New Value `5`
14. Verifikasi entri baru tampil: Field `Addon Reactivation Delay`, Old Value `2`, New Value `7`
15. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
16. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan
17. Tutup modal dengan `[✕]`

### TC-AC-LCS-470 dan TC-AC-LCS-471: Save 1 field sekaligus pada tab Recycle Bin dan tab Approval Settings mencatat tepat 1 entri

18. Untuk setiap baris tabel "Parameter tab satu field" pada Prerequisites, lakukan langkah 19 sampai 30
19. Klik tab sesuai kolom `Tab`
20. Klik icon Changelog di pojok kanan atas panel tab tersebut
21. Catat total entri pada footer modal sebagai baseline N0 (tab tersebut)
22. Tutup modal dengan `[✕]`
23. Ubah field sesuai kolom `Field` menjadi nilai kolom `New Value`
24. Klik `[Save]` dan tunggu toast sukses
25. Klik icon Changelog di pojok kanan atas panel tab tersebut
26. Verifikasi footer menunjukkan total entri baseline N0 ditambah 1 (tepat 1 entri baru)
27. Verifikasi entri baru (sedikitnya satu baris tampil) bernilai Action `Edit` dan Modified By `Andi W`
28. Verifikasi entri baru: Field sesuai kolom `Field`, Old Value sesuai kolom `Old Value`, New Value sesuai kolom `New Value`
29. Verifikasi tidak ada baris ganda untuk field yang sama di antara entri baru
30. Verifikasi tidak ada entri baru untuk field yang nilainya sama dengan nilai tersimpan

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah yang diulang per tab satu field: langkah 19 sampai 30 (2 tab: Recycle Bin, Approval Settings); parameter tiap iterasi ada di tabel "Parameter tab satu field" pada Prerequisites.
- Langkah penghubung: membaca baseline N0 lalu menutup modal (S-12) dan menutup modal sebelum pindah tab.
- Entri baru dicari di antara baris teratas urutan Newest First; urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- Setelah ekspansi blok ulang spec ini melewati sekitar 35 langkah (di atas smell): blok TC-AC-LCS-468 (17 langkah) ditambah blok satu field yang diulang dua kali (12 langkah x 2). Alasan mempertahankan satu spec: seluruh blok satu kelas (isi entri Changelog hasil Save), identik dalam bentuk, dan berdiri sendiri; tiap blok membaca baseline N0 tab-nya sendiri.
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.
