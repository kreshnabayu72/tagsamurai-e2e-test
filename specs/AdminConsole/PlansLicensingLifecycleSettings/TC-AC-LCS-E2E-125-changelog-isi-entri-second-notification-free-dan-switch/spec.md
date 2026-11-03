---
id: TC-AC-LCS-E2E-125-changelog-isi-entri-second-notification-free-dan-switch
title: "Isi Entri Changelog: Second Notification, Free Plan Duration, dan Switch Require Approval"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-443
  - TC-AC-LCS-444
  - TC-AC-LCS-465
coverage:
  web: automated
---

# Isi Entri Changelog: Second Notification, Free Plan Duration, dan Switch Require Approval

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Changelog tab `Trial Settings`, `Free Plan Settings` kosong saat tiap TC dimulai: dikosongkan lewat Fixture BE di hook `before` spec ini dan di langkah penghubung antar TC. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser sinkron; waktu aksi dicatat sesudah klik `[Save]` dan kolom Date dibandingkan dengan waktu itu dengan toleransi satu menit (kolom Date berketelitian menit).
- Kemampuan teknis (disediakan tim FE/BE, Lampiran A-15; dinyatakan juga di `suite.md`): Fixture BE untuk memulihkan ketujuh tab ke nilai default dan menimpa atau mengosongkan riwayat Changelog per tab (idempotent).
- Pemulihan: ketujuh tab dikembalikan ke nilai default dan dataset Changelog ke keadaan awal oleh hook `after` suite; nilai yang diubah tiap TC dipulihkan oleh langkah penghubung antar TC.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Nilai Pre-setup dan state Changelog dirujuk lewat `Fixture.lifecycleSettings.<kunci>` dari `fixtures/lifecycle-settings.json`.

## Test Steps

### TC-AC-LCS-443: Save perubahan Second Notification mencatat satu entri Edit pada Changelog Trial Settings

1. Ubah Second Notification dari `1` menjadi `2`
2. Klik `[Save]`
3. Verifikasi toast sukses "Success, trial settings have been saved." tampil
4. Catat waktu sesudah toast sukses sebagai waktu Save
5. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
6. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
7. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Second Notification`, Old Value `1`, New Value `2`, Modified By `Andi W`
8. Verifikasi tidak ada baris untuk field lain
9. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `Trial Settings` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-444: Save perubahan Free Plan Duration mencatat satu entri Edit pada Changelog Free Plan Settings

10. Klik tab `Free Plan Settings`
11. Ubah Free Plan Duration dari `365` menjadi `366`
12. Klik `[Save]`
13. Verifikasi toast sukses "Success, free plan settings have been saved." tampil
14. Catat waktu sesudah toast sukses sebagai waktu Save
15. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
16. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
17. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Free Plan Duration`, Old Value `365`, New Value `366`, Modified By `Andi W`
18. Verifikasi tidak ada baris untuk field lain
19. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `Free Plan Settings` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-465: Save Switch Require Approval for Trial Activation mencatat Old Value `Off` dan New Value `On`

20. Aktifkan Switch `Require Approval for Trial Activation`
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, trial settings have been saved." tampil
23. Catat waktu sesudah toast sukses sebagai waktu Save
24. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
25. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
26. Verifikasi baris 1: Action `Edit`, Field `Require Approval for Trial Activation`, Old Value `Off`, New Value `On`, Modified By `Andi W`

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Pulihkan ketujuh tab ... lalu muat ulang halaman Lifecycle Settings" antar TC (memulihkan nilai default dan Changelog kosong sebagai precondition TC berikutnya, S-03, S-09) dan "Klik tab" (precondition TC: user berada di tab terkait).
- Expected "Tidak ada baris untuk field lain" adalah asersi jumlah dan state (footer `1–1 of 1` dengan Changelog kosong sebelum aksi), bukan asersi absence kelas g.
- Satu `Verifikasi` baris Changelog memuat seluruh kolom satu entri (Date, Action, Field, Old Value, New Value, Modified By) karena diamati dari satu baris (S-01).
- Pengecualian A-15: total entri Changelog (footer `1–1 of 1`) diasersi sebagai angka absolut karena riwayat tab dikosongkan lewat Fixture BE di hook `before` spec dan di langkah penghubung antar TC, lalu dikembalikan di hook `after`; suite berjalan serial.
- Langkah "Catat waktu sesudah toast sukses sebagai waktu Save" adalah langkah penghubung sebagai pembanding kolom Date (S-12).
- Temuan untuk QA: Post Condition TC (nilai tersimpan dan satu entri tercatat) tidak punya langkah observasi sendiri; nilai tersimpan teramati lewat kolom New Value baris Changelog dan Post Condition tidak diasersi terpisah (S-01).
