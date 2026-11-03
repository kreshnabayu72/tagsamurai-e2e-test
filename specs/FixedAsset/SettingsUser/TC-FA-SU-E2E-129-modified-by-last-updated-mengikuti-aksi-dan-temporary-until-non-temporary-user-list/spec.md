---
id: TC-FA-SU-E2E-129-modified-by-last-updated-mengikuti-aksi-dan-temporary-until-non-temporary-user-list
title: "Modified By dan Last Updated Mengikuti Aksi Terakhir, dan Temporary Until Pengguna Non-temporary"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-371
  - TC-FA-SU-372
coverage:
  web: automated
---

# Modified By dan Last Updated Mengikuti Aksi Terakhir, dan Temporary Until Pengguna Non-temporary

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Data Pre-setup tambahan: layanan terkendali pemeriksaan aset dan approval (#37). Pengguna Pre-setup yang dibaca tanpa diubah: Fajar Nugroho (Temporary User, Temporary Until `31/12/26`).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; S-06): `Gita Permata {runId}-129`, email `gita.permata+{runId}-129@qwertysystem.net`, Active, non-temporary, tanpa aset aktif dan bukan approver tertunggu. Pengguna baru untuk App Access: `Pengguna Baru {runId}-129`, email `pengguna.baru+{runId}-129@qwertysystem.net`.
- Kemampuan Principal Automation (Pre-setup #12, disediakan tim FE): memberi App Access FAMS pada pengguna baru di Global Settings hingga tersimpan; App Access dicabut di hook `after`.
- `Pengguna Baru {runId}-129` dibuat lewat seed API tanpa App Access FAMS di hook `before`.
- Waktu aksi dibaca setelah aksi selesai; jam server dan jam browser sinkron; Last Updated dibandingkan dengan waktu aksi dengan toleransi satu menit (S-12).
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-371: Modified By dan Last Updated mengikuti aksi terakhir

1. Ketik Search `Gita Permata {runId}-129`, tekan Enter
2. Klik sakelar Active pada baris `Gita Permata {runId}-129`
3. Klik `[Deactivate]` pada dialog konfirmasi
4. Tunggu aksi selesai (sakelar Active baris berpindah ke OFF)
5. Verifikasi kolom Modified By baris `Gita Permata {runId}-129` berformat `Lina M`
6. Hover kolom Modified By baris `Gita Permata {runId}-129`
7. Verifikasi hover menampilkan nama lengkap `Lina Marlina`
8. Verifikasi Last Updated baris `Gita Permata {runId}-129` berformat tanggal waktu sesuai General Settings
9. Beri App Access FAMS pada `Pengguna Baru {runId}-129` di Global Settings lewat Principal Automation hingga tersimpan, lalu catat waktu aksi
10. Muat ulang halaman User List
11. Ganti isi kotak search dengan `Pengguna Baru {runId}-129`, tekan Enter
12. Verifikasi Modified By baris `Pengguna Baru {runId}-129` adalah `System`
13. Verifikasi Last Updated baris `Pengguna Baru {runId}-129` sama dengan waktu pemberian App Access (toleransi satu menit)

### TC-FA-SU-372: Temporary Until pengguna non-temporary

14. Klik `(←)` pada kotak Search
15. Klik header kolom Actions (⋯), klik `Setup Column...`
16. Centang `Temporary Until`, klik `[Save]`
17. Ketik Search `Fajar Nugroho`, tekan Enter
18. Verifikasi Temporary Until baris Fajar Nugroho `31/12/26`
19. Ganti isi kotak search dengan `Gita Permata {runId}-129`, tekan Enter
20. Verifikasi Temporary Until baris `Gita Permata {runId}-129` `—`
21. Klik ⋯ pada baris `Gita Permata {runId}-129`, klik `Detail`
22. Verifikasi field Temporary Until di General Information Hidden tanpa menyisakan sel kosong
23. Klik breadcrumb `User`
24. Klik menu Settings > User pada sidebar
25. Ketik Search `Fajar Nugroho`, tekan Enter
26. Klik ⋯ pada baris Fajar Nugroho, klik `Detail`
27. Verifikasi field Temporary Until di General Information menampilkan `Temporary until 31/12/26`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 17, 19, 25 (Search untuk menemukan baris target, R-16), 4 (tunggu aksi selesai, 8b butir 8), 10, 14, 24 (memuat ulang atau mereset Search), serta 15 dan 16 (menampilkan kolom curated lewat Setup Column).
- TC-FA-SU-369 dan TC-FA-SU-370 ada di spec 108.
- Temuan untuk QA (S-15): (1) Post Condition TC-FA-SU-371 (Gita Permata Inactive dengan Modified By aktor dan Last Updated terbaru; pengguna baru Modified By `System`) tidak punya langkah observasi tersendiri selain Expected a sampai c, sehingga tidak diasersi terpisah. (2) TC-FA-SU-371 memakai Gita Permata Pre-setup; spec memakai pengguna milik spec bernama sama dengan suffix (S-06), dan teks dialog Deactivate diasersi di spec 029. (3) TC-FA-SU-372 menyebut pengguna non-temporary Gita Permata; spec memakai pengguna milik spec yang non-temporary.
