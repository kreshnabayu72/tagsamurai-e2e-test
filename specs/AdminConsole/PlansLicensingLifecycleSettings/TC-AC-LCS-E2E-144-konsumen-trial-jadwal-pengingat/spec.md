---
id: TC-AC-LCS-E2E-144-konsumen-trial-jadwal-pengingat
title: "Konsumen Trial: Perubahan First Notification dan Second Notification Mengubah Jadwal Pengingat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-506
  - TC-AC-LCS-507
coverage:
  web: automated
---

# Konsumen Trial: Perubahan First Notification dan Second Notification Mengubah Jadwal Pengingat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Client PT Bintang Timur (`Fixture.lifecycleSettings.clientBintangTimur`) dengan trial aktif; tanggal berakhir trial diatur per TC lewat Fixture BE (10 hari lagi pada TC-AC-LCS-506, 2 hari lagi pada TC-AC-LCS-507). Penerima pengingat trial: inisiator trial dan kontak klien (sesuai `plans-licensing-trial.md` F-ACTR-05); akun keduanya disediakan tim FE (alamat tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE): mail-catcher atau inbox riil yang dapat dibaca penguji beserta pembacaan Overlay Notifikasi kedua penerima; baseline jumlah email per alamat dan jumlah notifikasi In-App dicatat sebelum aksi (R-11); Fixture BE untuk mengatur tanggal data uji dan memicu job pengingat trial; jam server tidak digeser.
- Pemulihan: ketujuh tab dan data trial uji dipulihkan lewat Fixture BE di langkah penghubung antar TC dan hook `after`; suite berjalan serial (`parallel: false`).
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-506: Perubahan First Notification mengubah jadwal pengingat trial aktif (dibaca ulang)

1. Atur lewat Fixture BE: trial aktif PT Bintang Timur berakhir 10 hari lagi dan belum menerima pengingat pertama (dipakai sebagai precondition TC, tidak diasersi)
2. Catat baseline jumlah email per alamat inisiator trial dan kontak klien PT Bintang Timur serta jumlah notifikasi In-App keduanya
3. Ubah First Notification dari `7` menjadi `14`
4. Klik `[Save]` dan tunggu toast sukses
5. Picu eksekusi job pengingat trial lewat Fixture BE
6. Baca inbox dan Overlay Notifikasi inisiator trial PT Bintang Timur
7. Verifikasi inisiator trial menerima satu pengingat pertama trial melalui In-App
8. Verifikasi inisiator trial menerima satu pengingat pertama trial melalui Email
9. Baca inbox dan Overlay Notifikasi kontak klien PT Bintang Timur
10. Verifikasi kontak klien menerima satu pengingat pertama trial melalui In-App
11. Verifikasi kontak klien menerima satu pengingat pertama trial melalui Email

### TC-AC-LCS-507: Perubahan Second Notification mengubah jadwal pengingat trial aktif (dibaca ulang)

12. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: trial aktif PT Bintang Timur berakhir 2 hari lagi dan pengingat pertama sudah terkirim (dipakai sebagai precondition TC, tidak diasersi)
13. Catat baseline jumlah email per alamat inisiator trial dan kontak klien PT Bintang Timur serta jumlah notifikasi In-App keduanya
14. Ubah Second Notification dari `1` menjadi `3`
15. Klik `[Save]` dan tunggu toast sukses
16. Picu eksekusi job pengingat trial lewat Fixture BE
17. Baca inbox dan Overlay Notifikasi inisiator trial PT Bintang Timur
18. Verifikasi inisiator trial menerima satu pengingat kedua trial melalui In-App
19. Verifikasi inisiator trial menerima satu pengingat kedua trial melalui Email
20. Baca inbox dan Overlay Notifikasi kontak klien PT Bintang Timur
21. Verifikasi kontak klien menerima satu pengingat kedua trial melalui In-App
22. Verifikasi kontak klien menerima satu pengingat kedua trial melalui Email

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (R-11, S-12), "Picu eksekusi job ...", "Baca inbox dan Overlay Notifikasi ...", dan "Pulihkan ..." antar TC (S-03, S-09).
- Temuan untuk QA: Expected TC memuat klausa pembanding "padahal dengan nilai `7` (atau `1`) belum terkirim" tanpa langkah observasi sebelum perubahan nilai; klausa itu tidak diasersi (S-01).
- Temuan untuk QA: TC tidak menyebut akun inisiator trial dan kontak klien serta cara membaca Overlay Notifikasi keduanya; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE (S-11, S-13). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
