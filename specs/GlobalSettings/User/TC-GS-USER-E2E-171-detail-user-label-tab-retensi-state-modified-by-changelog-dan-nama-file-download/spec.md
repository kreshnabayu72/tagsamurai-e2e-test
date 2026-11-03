---
id: TC-GS-USER-E2E-171-detail-user-label-tab-retensi-state-modified-by-changelog-dan-nama-file-download
title: "User Detail: Label Tab dan Sub-Tab dengan Angka 0, Retensi State Search Sort Paginasi antar Tab, Modified By Singkat dengan Hover Nama Lengkap, dan Nama File Download Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1126
  - TC-GS-USER-1122
  - TC-GS-USER-1127
  - TC-GS-USER-1132
coverage:
  web: automated
---

# User Detail: Label Tab dan Sub-Tab dengan Angka 0, Retensi State Search Sort Paginasi antar Tab, Modified By Singkat dengan Hover Nama Lengkap, dan Nama File Download Changelog

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target dan tidak diubah (S-06).
- Data Dinamis, di-seed lewat API sebagai Siti Nurhaliza di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD), dihapus di hook `after`. Semua user Activated, Division `Finance`, Access `Fixed Asset`, email `<nama tanpa spasi huruf kecil>+{runId}-171@qwertysystem.net`:
  - `Dewi Lestari {runId}-171`: tanpa data Responsibilities dan tanpa Non-Login User (label `Responsibilities (0)` dan `Non-Login User (0)`; TC-GS-USER-1126).
  - `Joko Susilo {runId}-171`: punya data Responsibilities tetapi tanpa baris Assigned Assets (label sub-tab `Assigned Assets (0)`; TC-GS-USER-1126). Seeding Responsibilities FAMS disediakan tim FE/BE.
  - `Ahmad Fauzi {runId}-171`: Holder role `Manage user and role`; sedikitnya satu baris Changelog yang memuat kata `Manage` dan satu baris yang tidak, sedikitnya satu baris Pending Approvals dengan nomor `REQ` dan satu baris tanpa `REQ`, serta sedikitnya satu baris System Log (TC-GS-USER-1122). Seeding Pending Approvals dan System Log disediakan tim FE/BE.
  - `John Doe {runId}-171`: perubahan datanya dibuat oleh aktor Siti Nurhaliza sehingga Tab Changelog memuat baris ber-Modified By `Siti N` (TC-GS-USER-1127).
  - `Mary Ann  &  O'Neil` (dua spasi sebelum dan sesudah `&`), email `maryannoneil+{runId}-171@qwertysystem.net`: nama literal tanpa suffix karena nama berkas unduhan diturunkan dari nama (TC-GS-USER-1132); seeding idempotent (dilewati bila sudah ada), hook `after` hanya menghapus yang dibuat spec ini, suite serial. Lihat Temuan untuk QA (Need Confirmation: butir Lampiran A).
- Kemampuan teknis, disediakan tim FE/BE: menangkap berkas unduhan browser ke direktori bersih dan membaca nama berkasnya; membaca isi tampilan kotak Search, indikator sort, dan page size Tab Changelog serta sub-tab Pending Approvals; hover pada nilai Modified By.
- State global yang diubah: tidak ada (state Search, Sort, dan paginasi tab Detail bersifat per kunjungan Detail). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus kelima user seed lewat API; berkas unduhan dihapus bersama direktori bersihnya.

## Test Steps

### TC-GS-USER-1126: Label tab dan sub-tab menampilkan angka termasuk (0)

1. Ketik Search `Dewi Lestari {runId}-171`, tekan Enter
2. Klik Name `Dewi Lestari {runId}-171` di User List
3. Verifikasi label tab `Responsibilities (0)`
4. Verifikasi label tab `Non-Login User (0)`
5. Klik menu User di sidebar Global Settings
6. Ketik Search `Joko Susilo {runId}-171`, tekan Enter
7. Klik Name `Joko Susilo {runId}-171` di User List
8. Klik Tab `Responsibilities`
9. Verifikasi label sub-tab `Assigned Assets (0)` tampil dengan angka 0

### TC-GS-USER-1122: State Search, Filter, Sort, dan paginasi tiap tab dan sub-tab Detail dipertahankan saat pindah tab

10. Klik menu User di sidebar Global Settings
11. Ketik Search `Ahmad Fauzi {runId}-171`, tekan Enter
12. Klik Name `Ahmad Fauzi {runId}-171` di User List
13. Klik Tab `Changelog`
14. Ketik Search `Manage`, tekan Enter
15. Urutkan kolom Date menjadi Oldest First
16. Ubah page size ke 25
17. Klik Tab `Responsibilities` lalu sub-tab `Pending Approvals`
18. Ketik Search `REQ`, tekan Enter
19. Klik Tab `System Log`
20. Klik Tab `Changelog`
21. Verifikasi kotak Search Tab Changelog berisi `Manage`
22. Verifikasi sort kolom Date Tab Changelog Oldest First
23. Verifikasi page size Tab Changelog 25
24. Klik Tab `Responsibilities` lalu sub-tab `Pending Approvals`
25. Verifikasi kotak Search sub-tab Pending Approvals berisi `REQ`
26. Verifikasi kotak Search sub-tab Pending Approvals tidak berisi `Manage` (state Tab Changelog tidak memengaruhi tab lain)
27. Klik menu User di sidebar Global Settings
28. Ketik Search `Ahmad Fauzi {runId}-171`, tekan Enter
29. Klik Name `Ahmad Fauzi {runId}-171` di User List
30. Klik Tab `Changelog`
31. Verifikasi kotak Search Tab Changelog kosong (state default)
32. Verifikasi sort kolom Date Tab Changelog Newest First (state default)
33. Verifikasi page size Tab Changelog 10 (state default)
34. Klik Tab `Responsibilities` lalu sub-tab `Pending Approvals`
35. Verifikasi kotak Search sub-tab Pending Approvals kosong (state default)

### TC-GS-USER-1127: Kolom Modified By Tab Changelog berformat singkat dengan hover nama lengkap

36. Klik menu User di sidebar Global Settings
37. Ketik Search `John Doe {runId}-171`, tekan Enter
38. Klik Name `John Doe {runId}-171` di User List
39. Klik Tab `Changelog`
40. Verifikasi kolom Modified By baris teratas `Siti N`
41. Hover nilai Modified By baris teratas
42. Verifikasi hover menampilkan nama lengkap `Siti Nurhaliza`

### TC-GS-USER-1132: Placeholder nama file Download, spasi jadi `-`, simbol dibuang, `-` berurutan diringkas

43. Klik menu User di sidebar Global Settings
44. Ketik Search `Mary Ann  &  O'Neil`, tekan Enter
45. Klik Name `Mary Ann  &  O'Neil` di User List
46. Klik Tab `Changelog`
47. Klik icon Download
48. Klik opsi `Download as CSV`
49. Verifikasi nama file `Changelog-Mary-Ann-ONeil.csv` (spasi menjadi `-`, `&` dan `'` dibuang, `-` berurutan diringkas, huruf besar dan kecil dipertahankan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (49 langkah). Alasan: keempat TC berada di satu kelas harness (fungsional; tiga TC baca saja dan satu TC mengunduh berkas yang hanya diasersi nama berkasnya, bagian 3 prinsip 13f) dan satu layar (User Detail); TC-GS-USER-1122 sendiri 26 langkah karena TC itu menuntut state tiga tab dan satu sub-tab diubah, dipindah, dan diperiksa kembali; tiap blok berdiri sendiri pada user seed sendiri, dan 17 langkah adalah pembukaan Detail berulang (klik menu User, Search, dan klik Name), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber dipertahankan menurut daftar `sourceTc`; TC-GS-USER-1132 di akhir karena mengunduh berkas.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 6, 11, 28, 37, 44 (Search), 5, 10, 27, 36, 43 (kembali ke User List lewat menu User), 8, 13, 17, 19, 20, 24, 30, 34, 39, 46 (berpindah tab dan sub-tab), 14 sampai 16 dan 18 (aksi yang membentuk state tab pada TC-GS-USER-1122), 41 (hover pemicu tooltip, bagian 8b butir 5), 47 dan 48 (membuka overlay Download dan memilih format).
- Langkah 26 menjadi bukti isolasi antar tab: sub-tab Pending Approvals berisi `REQ` meskipun Tab Changelog berisi `Manage`; langkah 21 menjadi bukti sebaliknya (Tab Changelog masih `Manage`, bukan `REQ`, sesudah Search `REQ` dijalankan di langkah 18).
- Langkah 40 membaca baris teratas Tab Changelog `John Doe {runId}-171`; seluruh baris seed dibuat oleh aktor Siti Nurhaliza sehingga tidak bergantung pada urutan baris.
- Pembagian TC lintas spec: Tab Changelog (Search, Filter, Sort, Pagination, Setup Column) ada di spec 092 dan 093; sub-tab Pending Approvals ada di spec 126 sampai 131; isi berkas unduhan Tab Changelog (kelas f) tidak diasersi di spec ini, hanya nama berkas.
- Temuan untuk QA:
  - TC-GS-USER-1132 memakai user bernama literal `Mary Ann  &  O'Neil` yang tidak ada pada Tabel Pre-setup, dan nama berkas `Changelog-Mary-Ann-ONeil.csv` tidak dapat diasersi bila nama diberi suffix `{runId}`. Lampiran A (A-3, A-4) tidak mencakup nama literal ini; spec memakai nama literal dengan email bersuffix dan syarat seeding idempotent seperti pengecualian S-12. Need Confirmation: butir Lampiran A baru untuk nama literal ini.
  - TC-GS-USER-1132 langkah 2 ("Download sebagai CSV") tidak menyebut label opsi; spec memakai `Download as CSV` mengikuti spec 107.
  - TC-GS-USER-1122 Expected c ("semua tab kembali ke state default") tidak merinci nilai default; spec mengasersi Search kosong, sort Date Newest First, dan page size 10 pada Tab Changelog, serta Search kosong pada sub-tab Pending Approvals. Need Confirmation: nilai default sort dan page size Tab Changelog.
  - TC-GS-USER-1122 menyebut "Filter" pada judul tetapi langkah dan Expected hanya memuat Search, Sort, dan page size; Filter tidak diasersi.
  - TC-GS-USER-1127 menyebut `John Doe` tanpa perubahan data yang menghasilkan baris Changelog ber-Modified By `Siti N`; spec men-seed user oleh aktor Siti Nurhaliza (tidak butuh nama literal).
  - TC-GS-USER-1126, 1122, dan 1127 memakai Dewi Lestari, Joko Susilo, Ahmad Fauzi, dan John Doe Pre-setup; spec memakai seed bersuffix milik spec (S-06, S-12).
