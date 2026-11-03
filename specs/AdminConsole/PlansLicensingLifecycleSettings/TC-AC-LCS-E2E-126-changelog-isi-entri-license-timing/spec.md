---
id: TC-AC-LCS-E2E-126-changelog-isi-entri-license-timing
title: "Isi Entri Changelog per Field Tab License Timing"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-445
  - TC-AC-LCS-446
  - TC-AC-LCS-447
coverage:
  web: automated
---

# Isi Entri Changelog per Field Tab License Timing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Changelog tab `License Timing` kosong saat tiap TC dimulai: dikosongkan lewat Fixture BE di hook `before` spec ini dan di langkah penghubung antar TC. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser sinkron; waktu aksi dicatat sesudah klik `[Save]` dan kolom Date dibandingkan dengan waktu itu dengan toleransi satu menit (kolom Date berketelitian menit).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan ketujuh tab ke nilai default dan mengosongkan Changelog satu tab.
- Pemulihan: ketujuh tab dikembalikan ke nilai default dan dataset Changelog ke keadaan awal oleh hook `after` suite; nilai yang diubah tiap TC dipulihkan oleh langkah penghubung antar TC.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-445: Save perubahan Managed Transition Time mencatat satu entri Edit pada Changelog License Timing

1. Klik tab `License Timing`
2. Ubah Managed Transition Time dari `24` menjadi `25`
3. Klik `[Save]`
4. Verifikasi toast sukses "Success, license timing settings have been saved." tampil
5. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
6. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
7. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Managed Transition Time`, Old Value `24`, New Value `25`, Modified By `Andi W`
8. Verifikasi tidak ada baris untuk field lain
9. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `License Timing` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-446: Save perubahan Managed Action Retry Delay mencatat satu entri Edit pada Changelog License Timing

10. Klik tab `License Timing`
11. Ubah Managed Action Retry Delay dari `2` menjadi `3`
12. Klik `[Save]`
13. Verifikasi toast sukses "Success, license timing settings have been saved." tampil
14. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
15. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
16. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Managed Action Retry Delay`, Old Value `2`, New Value `3`, Modified By `Andi W`
17. Verifikasi tidak ada baris untuk field lain
18. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `License Timing` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-447: Save perubahan Addon Reactivation Delay mencatat satu entri Edit pada Changelog License Timing

19. Klik tab `License Timing`
20. Ubah Addon Reactivation Delay dari `2` menjadi `3`
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, license timing settings have been saved." tampil
23. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
24. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
25. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Addon Reactivation Delay`, Old Value `2`, New Value `3`, Modified By `Andi W`
26. Verifikasi tidak ada baris untuk field lain

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Pulihkan ketujuh tab ... lalu muat ulang halaman Lifecycle Settings" antar TC (memulihkan nilai default dan Changelog kosong sebagai precondition TC berikutnya, S-03, S-09) dan "Klik tab" (precondition TC: user berada di tab terkait).
- Expected "Tidak ada baris untuk field lain" adalah asersi jumlah dan state (footer `1–1 of 1` dengan Changelog kosong sebelum aksi), bukan asersi absence kelas g.
- Satu `Verifikasi` baris Changelog memuat seluruh kolom satu entri (Date, Action, Field, Old Value, New Value, Modified By) karena diamati dari satu baris (S-01).
- Temuan untuk QA: TC mensyaratkan "Changelog tab kosong" sedangkan Changelog permanen; cara mengosongkan hanya lewat Fixture BE yang tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC (nilai tersimpan dan satu entri tercatat) tidak punya langkah observasi sendiri; nilai tersimpan teramati lewat kolom New Value baris Changelog dan Post Condition tidak diasersi terpisah (S-01).
