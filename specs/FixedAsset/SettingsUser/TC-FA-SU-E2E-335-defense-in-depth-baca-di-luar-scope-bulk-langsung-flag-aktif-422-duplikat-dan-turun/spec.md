---
id: TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun
title: "Defense-in-depth Baca Di Luar Scope, Bulk Langsung, Flag Aktif, 422 Duplikat, dan Turun Tangga Tanpa Konfirmasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-999
  - TC-FA-SU-1000
  - TC-FA-SU-1001
  - TC-FA-SU-1002
  - TC-FA-SU-1003
coverage:
  web: automated
---

# Defense-in-depth Baca Di Luar Scope, Bulk Langsung, Flag Aktif, 422 Duplikat, dan Turun Tangga Tanpa Konfirmasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 15 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`); langkah 22 Total Control Lina Marlina (Pre-setup #1; `totalControl_automated_{namaCompany}@qwertysystem.net`; `Spectra.env.FA_TC_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), System Log (#28), Transaction Admin Log (#29), Transaction Role (#39). Target: Indra Wijaya (di luar scope Finance & Accounting), Ahmad Dahlan, Lina Marlina, Citra Lestari, Gita Permata, Wawan Setiawan (Manage files; Manage asset & TAG tanpa grup), dan Mira Anggraini (Disposal × Staff pada Finance & Accounting). Data Dinamis: grup stale `Grup Uji {runId}-335` dibuat dan dihapus seed API di hook `before`.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE. Jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum dan sesudah permintaan (baseline, S-12).
- Pengguna tenant B (TC-FA-SU-999): disediakan tim FE (Pre-setup TC tidak mendefinisikan tenant B). Ganti akun pada spec ini hanya mengambil token sesi API aktor untuk klien HTTP (sesi UI tetap akun pertama).
- State global dan pemulihan: status Gita Permata dipulihkan pada langkah penghubung; penugasan lain tidak berubah karena permintaan ditolak server. Grup stale dibersihkan seed API di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-999: Permintaan langsung membaca data pengguna di luar scope atau tenant lain

1. Kirim permintaan langsung ke API baca daftar User memakai klien HTTP dengan token sesi Sinta Dewi
2. Verifikasi permintaan baca daftar User untuk aktor scope Finance & Accounting hanya mengembalikan pengguna dalam row scope
3. Kirim permintaan langsung ke API baca Detail Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
4. Verifikasi permintaan baca Detail Indra Wijaya ditolak dengan status 403 tanpa data
5. Kirim permintaan langsung ke API baca Tab System Log Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
6. Verifikasi permintaan baca Tab System Log Indra Wijaya ditolak dengan status 403 tanpa data
7. Kirim permintaan langsung ke API baca Tab Transaction Admin Log Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
8. Verifikasi permintaan baca Tab Transaction Admin Log Indra Wijaya ditolak dengan status 403 tanpa data
9. Kirim permintaan langsung ke API baca Changelog Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
10. Verifikasi permintaan baca Changelog Indra Wijaya ditolak dengan status 403 tanpa data
11. Kirim permintaan langsung ke API baca Download Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
12. Verifikasi permintaan baca Download Indra Wijaya ditolak dengan status 403 tanpa data
13. Kirim permintaan langsung ke API baca pengguna tenant B memakai klien HTTP dengan token sesi Sinta Dewi
14. Verifikasi permintaan baca pengguna tenant lain tidak mengembalikan data pengguna apa pun

### TC-FA-SU-1000: Permintaan bulk langsung dengan Default User, akun sendiri, dan target tier

15. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
16. Catat jumlah entri `Deactivate` pada Tab Changelog Ahmad Dahlan, Qori Akbar, Lina Marlina, Citra Lestari, dan Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
17. Kirim permintaan langsung ke API bulk Deactivate berisi Ahmad Dahlan, akun sendiri, Lina Marlina, Citra Lestari, dan Gita Permata memakai klien HTTP dengan token sesi Qori Akbar
18. Verifikasi item Default User (Ahmad Dahlan) dan akun sendiri (Qori Akbar) ditolak tanpa mengubah status (dibaca lewat API)
19. Verifikasi item Lina Marlina (Total Control) dan Citra Lestari (Read Only) dilewati, sedangkan item eligible Gita Permata diproses (partial-success) dan berstatus Inactive
20. Verifikasi jumlah entri `Deactivate` bertambah satu hanya untuk Gita Permata dan sama dengan baseline untuk Ahmad Dahlan, Qori Akbar, Lina Marlina, dan Citra Lestari pada Tab Changelog target, Tab System Log aktor, dan Activity Log
21. Pulihkan status Gita Permata menjadi Active lewat seed API

### TC-FA-SU-1001: Flag aktif per Group Role dari klien diabaikan server

22. Ganti akun: login API sebagai Lina Marlina (Total Control, `Spectra.env.FA_TC_PASSWORD`) untuk klien HTTP
23. Kirim permintaan langsung ke API simpan Group Role Manage asset & TAG milik Wawan Setiawan tanpa grup dan dengan flag aktif benar memakai klien HTTP dengan token sesi Lina Marlina
24. Verifikasi server menurunkan status aktif Group Role hanya dari jumlah grup tersimpan (dibaca lewat API)
25. Verifikasi Group Role Manage asset & TAG Wawan Setiawan tanpa grup tetap tidak aktif walau payload membawa flag aktif (dibaca lewat API)

### TC-FA-SU-1002: Penambahan grup Group Role ganda atau stale ditolak dengan status 422

26. Buat grup `Grup Uji {runId}-335` lewat seed API lalu hapus grup itu sebagai grup stale
27. Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
28. Kirim permintaan langsung ke API tambah Branch Surabaya (sudah ter-assign) ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
29. Verifikasi penambahan grup yang sudah ter-assign ke role yang sama ditolak dengan status 422
30. Verifikasi penugasan Manage files Wawan Setiawan tidak berubah (dibaca lewat API)
31. Kirim permintaan langsung ke API tambah grup stale `Grup Uji {runId}-335` ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Lina Marlina
32. Verifikasi penambahan grup yang sudah dihapus ditolak dengan status 422
33. Verifikasi jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sama dengan baseline

### TC-FA-SU-1003: Assign Transaction Role dengan grup stale atau tanpa konfirmasi turun tangga

34. Kirim permintaan langsung ke API assign Disposal × Monitoring & Report pada Finance & Accounting untuk Mira Anggraini (saat ini Staff) tanpa penanda konfirmasi downgrade memakai klien HTTP dengan token sesi Lina Marlina
35. Verifikasi Save yang menurunkan tangga pada node yang sama (Finance & Accounting) tanpa membawa konfirmasi downgrade ditolak dengan status 409
36. Verifikasi seluruh Save dibatalkan: Transaction Role Mira Anggraini pada Disposal × Finance & Accounting tetap Staff (dibaca lewat API)
37. Kirim permintaan langsung ke API assign Transaction Role dengan grup stale `Grup Uji {runId}-335` untuk Mira Anggraini memakai klien HTTP dengan token sesi Lina Marlina
38. Verifikasi permintaan dengan grup yang sudah dihapus ditolak dengan status 422

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-999 sampai 1003 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tanpa perubahan atau entri log" pada Expected b TC-FA-SU-1002 diasersi di spec ini sebagai jumlah entri dengan baseline (S-12), bukan di spec absence, karena TC-FA-SU-1002 tidak punya pasangan spec kelas g. Hal serupa untuk klausa log TC-FA-SU-1000 (asersi jumlah hanya item eligible).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 16, 21, 26, 27.
- Ganti akun eksplisit (S-07): langkah 15, 22.
- Spec ini 38 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (defense-in-depth, kelas a) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Ekspansi berasal dari TC-FA-SU-999 yang menuntut lima endpoint baca ditambah satu tenant lain.
- Temuan untuk QA:
  - TC-FA-SU-999 menyebut "pengguna tenant B" tanpa mendefinisikan tenant B di Pre-setup; kemampuan membuat atau mengakses tenant B disediakan tim FE.
  - TC-FA-SU-1002 dan 1003 tidak menyebut cara menyiapkan grup yang sudah dihapus; spec memakai grup uji yang dibuat lalu dihapus lewat seed API.
  - TC-FA-SU-1002 Expected b memuat klausa "tanpa entri log" tetapi TC ini tidak punya spec absence (kelas g); asersi jumlah dengan baseline dipakai di spec ini. Pemilik proses dapat meminta spec absence tambahan bila ingin kelas g murni.
  - Email dan password Sinta Dewi (#6) dan Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - TC-FA-SU-1003 butir b diperbarui: guard 409 hanya berlaku bagi penurunan tangga pada node yang sama; Mira Anggraini (Pre-setup #39) hanya memegang Disposal pada Finance & Accounting, sehingga kasus penugasan di ancestor atau descendant (tidak memicu 409) tidak diasersi di sini dan ada di TC-FA-SU-1109 (E2E-422).
  - TC-FA-SU-999 sampai 1003 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
