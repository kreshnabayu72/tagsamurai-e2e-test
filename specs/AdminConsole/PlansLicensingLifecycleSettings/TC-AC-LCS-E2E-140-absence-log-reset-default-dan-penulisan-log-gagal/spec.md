---
id: TC-AC-LCS-E2E-140-absence-log-reset-default-dan-penulisan-log-gagal
title: "Absence Log: Reset to Default Saat Seluruh Field Default dan Kegagalan Penulisan Log Tidak Menulis Entri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-477
  - TC-AC-LCS-686
coverage:
  web: automated
---

# Absence Log: Reset to Default Saat Seluruh Field Default dan Kegagalan Penulisan Log Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: pada TC-AC-LCS-477 Changelog tab `Free Plan Settings` kosong (dikosongkan lewat Fixture BE di hook `before` spec ini); pada TC-AC-LCS-686 Changelog tab `Trial Settings` diseed tepat 1 entri Edit Max Trial Duration 31 menjadi 30 (dipakai sebagai precondition TC, tidak diasersi selain lewat footer).
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser tidak digeser.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memaksa penulisan log gagal (pemicu, bukan objek uji, `P-5` butir a), mengosongkan Changelog satu tab, menyeed satu entri Changelog, dan memulihkan ketujuh tab (mengosongkan dan menyeed riwayat Changelog menimpa riwayat tab itu, idempotent; Lampiran A-15, dinyatakan di `suite.md`); kemampuan membaca entri teratas System Log aktor dan Activity Log Admin Console sebagai baseline.
- Pemulihan: penulisan log dikembalikan normal di langkah akhir TC-AC-LCS-477 dan di hook `after` suite; ketujuh tab dipulihkan ke nilai default dan dataset Changelog ke keadaan awal oleh hook `after` suite.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Nilai Pre-setup dan state Changelog dirujuk lewat `Fixture.lifecycleSettings.<kunci>` dari `fixtures/lifecycle-settings.json`.

## Test Steps

### TC-AC-LCS-477: Penulisan log gagal membatalkan Save sehingga data tidak berubah

1. Klik tab `Free Plan Settings`
2. Ubah Free Plan Duration dari `365` menjadi `400`
3. Paksa penulisan log gagal lewat Fixture BE
4. Klik `[Save]`
5. Verifikasi toast error "Error, failed to save free plan settings." tampil
6. Verifikasi `[Save]` tetap enabled
7. Muat ulang halaman Lifecycle Settings
8. Klik tab `Free Plan Settings`
9. Verifikasi Free Plan Duration tetap `365`
10. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
11. Verifikasi Changelog menampilkan empty state (tidak ada entri)
12. Pulihkan penulisan log ke keadaan normal lewat Fixture BE

### TC-AC-LCS-686: Reset to Default tab Trial Settings saat seluruh field sudah bernilai default tidak menulis entri pada tiga surface log

13. Atur lewat Fixture BE: tab `Trial Settings` tersimpan dengan nilai default (Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`, Require Approval for Trial Activation `OFF`, First Notification `7`, Second Notification `1`) dan Changelog tab `Trial Settings` berisi tepat 1 entri (Edit Max Trial Duration 31 menjadi 30), lalu muat ulang halaman Lifecycle Settings
14. Catat entri teratas System Log `Andi Wijaya` dan entri teratas Activity Log Admin Console sebagai baseline
15. Klik `[Reset to Default]`
16. Verifikasi toast sukses "Success, trial settings have been reset to default." tampil
17. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
18. Verifikasi Changelog tetap `1–1 of 1` dan tidak ada baris baru
19. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
20. Verifikasi entri teratas System Log sama dengan baseline (tidak ada entri Reset karena tidak ada field yang berubah)
21. Buka Activity Log (Admin Console)
22. Verifikasi entri teratas Activity Log sama dengan baseline (tidak ada entri Reset karena tidak ada field yang berubah)

## Notes

- `P-5` butir a: kegagalan penulisan log yang dipaksa lewat Fixture BE pada TC-AC-LCS-477 hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai state dan baseline sendiri (S-05).
- Anchor positif asersi absence: toast error pada TC-AC-LCS-477 dan toast sukses Reset pada TC-AC-LCS-686 (respons server sudah diproses), ditambah nilai field dan halaman Changelog yang tampil (bagian 8b butir 2).
- Pengecualian A-15: empty state (langkah 11) dan footer `1-1 of 1` (langkah 18) diasersi sebagai angka absolut karena riwayat tab dikosongkan lewat Fixture BE di hook `before` spec (TC-AC-LCS-477) dan di-seed tepat 1 entri pada langkah penghubung 13 (TC-AC-LCS-686) sebelum modal dibuka; hook `after` suite mengembalikan dataset Changelog.
- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC), langkah 3 "Paksa penulisan log gagal lewat Fixture BE" (membentuk Precondition TC-AC-LCS-477 sebelum Save, S-04), "Muat ulang halaman", "Catat entri teratas ... sebagai baseline" (S-12), dan langkah 12 "Pulihkan penulisan log" (S-03, S-09).
- Temuan untuk QA: Post Condition TC-AC-LCS-477 menyebut "Tidak ada entri log pada ketiga surface", tetapi langkah TC hanya mengamati Changelog; System Log dan Activity Log tidak diasersi karena TC tidak memberi langkah observasinya (S-01, S-05).
- Temuan untuk QA: Expected TC-AC-LCS-686 butir c dan d ("entri teratas tidak berubah") bergantung pada entri teratas yang tidak berubah oleh aktivitas lain; spec mencatat entri teratas sebagai baseline sebelum aksi. Mekanisme memaksa penulisan log gagal tidak didefinisikan di TC, PRD, atau LLD sehingga langkah 3 memakai kemampuan Fixture BE yang disediakan tim FE/BE (S-13).
