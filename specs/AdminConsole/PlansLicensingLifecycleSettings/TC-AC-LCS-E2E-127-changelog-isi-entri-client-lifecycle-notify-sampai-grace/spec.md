---
id: TC-AC-LCS-E2E-127-changelog-isi-entri-client-lifecycle-notify-sampai-grace
title: "Isi Entri Changelog per Field Tab Client Lifecycle: Notify Plan Owner sampai Final Reminder"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-448
  - TC-AC-LCS-449
  - TC-AC-LCS-450
  - TC-AC-LCS-451
coverage:
  web: automated
---

# Isi Entri Changelog per Field Tab Client Lifecycle: Notify Plan Owner sampai Final Reminder

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Changelog tab `Client Lifecycle` kosong saat tiap TC dimulai: dikosongkan lewat Fixture BE di hook `before` spec ini dan di langkah penghubung antar TC. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser sinkron; waktu aksi dicatat sesudah klik `[Save]` dan kolom Date dibandingkan dengan waktu itu dengan toleransi satu menit (kolom Date berketelitian menit).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan ketujuh tab ke nilai default dan mengosongkan Changelog satu tab.
- Pemulihan: ketujuh tab dikembalikan ke nilai default dan dataset Changelog ke keadaan awal oleh hook `after` suite; nilai yang diubah tiap TC dipulihkan oleh langkah penghubung antar TC.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-448: Save perubahan Notify Plan Owner Before Event mencatat satu entri Edit pada Changelog Client Lifecycle

1. Klik tab `Client Lifecycle`
2. Ubah Notify Plan Owner Before Event dari `45` menjadi `46`
3. Klik `[Save]`
4. Verifikasi toast sukses "Success, client lifecycle settings have been saved." tampil
5. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
6. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
7. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Notify Plan Owner Before Event`, Old Value `45`, New Value `46`, Modified By `Andi W`
8. Verifikasi tidak ada baris untuk field lain
9. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `Client Lifecycle` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-449: Save perubahan First Reminder Before Event mencatat satu entri Edit pada Changelog Client Lifecycle

10. Klik tab `Client Lifecycle`
11. Ubah First Reminder Before Event dari `30` menjadi `31`
12. Klik `[Save]`
13. Verifikasi toast sukses "Success, client lifecycle settings have been saved." tampil
14. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
15. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
16. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `First Reminder Before Event`, Old Value `30`, New Value `31`, Modified By `Andi W`
17. Verifikasi tidak ada baris untuk field lain
18. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `Client Lifecycle` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-450: Save perubahan Second Reminder Before Event mencatat satu entri Edit pada Changelog Client Lifecycle

19. Klik tab `Client Lifecycle`
20. Ubah Second Reminder Before Event dari `7` menjadi `8`
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, client lifecycle settings have been saved." tampil
23. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
24. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
25. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Second Reminder Before Event`, Old Value `7`, New Value `8`, Modified By `Andi W`
26. Verifikasi tidak ada baris untuk field lain
27. Pulihkan ketujuh tab ke nilai default dan kosongkan Changelog tab `Client Lifecycle` lewat Fixture BE, lalu muat ulang halaman Lifecycle Settings

### TC-AC-LCS-451: Save perubahan Final Reminder Before Event mencatat satu entri Edit pada Changelog Client Lifecycle

28. Klik tab `Client Lifecycle`
29. Ubah Final Reminder Before Event dari `1` menjadi `2`
30. Klik `[Save]`
31. Verifikasi toast sukses "Success, client lifecycle settings have been saved." tampil
32. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
33. Verifikasi footer modal Changelog menampilkan `1–1 of 1`
34. Verifikasi baris 1: Date tanggal dan jam saat Save sesuai General Settings, Action `Edit`, Field `Final Reminder Before Event`, Old Value `1`, New Value `2`, Modified By `Andi W`
35. Verifikasi tidak ada baris untuk field lain

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Pulihkan ketujuh tab ... lalu muat ulang halaman Lifecycle Settings" antar TC (memulihkan nilai default dan Changelog kosong sebagai precondition TC berikutnya, S-03, S-09) dan "Klik tab" (precondition TC: user berada di tab terkait).
- Expected "Tidak ada baris untuk field lain" adalah asersi jumlah dan state (footer `1–1 of 1` dengan Changelog kosong sebelum aksi), bukan asersi absence kelas g.
- Satu `Verifikasi` baris Changelog memuat seluruh kolom satu entri (Date, Action, Field, Old Value, New Value, Modified By) karena diamati dari satu baris (S-01).
- Temuan untuk QA: TC mensyaratkan "Changelog tab kosong" sedangkan Changelog permanen; cara mengosongkan hanya lewat Fixture BE yang tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC (nilai tersimpan dan satu entri tercatat) tidak punya langkah observasi sendiri; nilai tersimpan teramati lewat kolom New Value baris Changelog dan Post Condition tidak diasersi terpisah (S-01).
