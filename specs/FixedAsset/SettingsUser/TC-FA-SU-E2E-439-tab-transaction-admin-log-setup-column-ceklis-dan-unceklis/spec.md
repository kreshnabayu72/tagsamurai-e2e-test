---
id: TC-FA-SU-E2E-439-tab-transaction-admin-log-setup-column-ceklis-dan-unceklis
title: "Tab Transaction Admin Log: Ceklis dan Unceklis Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-785
coverage:
  web: automated
---

# Tab Transaction Admin Log: Ceklis dan Unceklis Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec ini mengubah preferensi kolom tabel Sub-tab Borrow (unceklis dan `[Save]`); preferensi disimpan per perangkat dan tidak memengaruhi tabel lain. Pemulihan: langkah ceklis kembali dan `[Save]` di dalam spec ini; hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE, bukan `[Reset to Default]`).
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Tabel "Kolom Putaran 1" (parameter langkah berulang; unceklis bersamaan, kolom `Group` tetap tercentang): `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`.
- Tabel "Kolom Putaran 2": `Group` (unceklis sementara kelima kolom lain tercentang).

## Test Steps

### TC-FA-SU-785: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 4 sampai 5):
4. Hilangkan centang kolom pada baris tersebut
5. Verifikasi kolom pada baris tersebut hilang dari Live Preview
6. Hover checkbox kolom `Group`
7. Verifikasi checkbox kolom `Group` disabled karena menjadi satu-satunya kolom visible
8. Verifikasi tooltip `At least one column must remain visible.` tampil
9. Klik `[Save]`
10. Verifikasi tabel menampilkan kolom `Group`
11. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 12):
12. Verifikasi kolom pada baris tersebut tidak tampil di tabel
13. Klik `F5`
14. Verifikasi tabel menampilkan kolom `Group`
15. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 16):
16. Verifikasi kolom pada baris tersebut tetap tidak tampil di tabel setelah refresh (`F5`)
17. Klik header kolom `⋯`, lalu klik item `Setup Column...`
18. Centang kembali kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `Borrower`
19. Hilangkan centang kolom `Group` (tabel "Kolom Putaran 2")
20. Verifikasi kolom `Group` hilang dari Live Preview
21. Klik `[Save]`
22. Verifikasi tabel menampilkan kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `Borrower`
23. Verifikasi tabel tidak menampilkan kolom `Group`
24. Klik `F5`
25. Verifikasi tabel menampilkan kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `Borrower`
26. Verifikasi tabel tetap tidak menampilkan kolom `Group` setelah refresh (`F5`)
27. Klik header kolom `⋯`, lalu klik item `Setup Column...`
28. Centang kembali kolom `Group`
29. Klik `[Save]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan pemulihan kolom pada dua langkah terakhir (ceklis kembali lalu `[Save]`, bagian 8b butir 14). Langkah pembuka Setup Column kedua (ceklis kembali lima kolom dan unceklis `Group`) adalah langkah penghubung yang memberi kolom `Group` kondisi unceklis dengan kolom lain tampil.
- Langkah berulang (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 5 kali (satu iterasi per baris tabel "Kolom Putaran 1"); langkah 12 dijalankan 5 kali; langkah 16 dijalankan 5 kali. Kolom `Group` diuji terpisah (tabel "Kolom Putaran 2") karena TC-FA-SU-785 butir g menetapkan kolom yang tersisa sebagai satu-satunya kolom visible tidak dapat di-uncheck; lima kolom lain tidak dapat di-uncheck bersama `Group`.
- Absence kolom di tabel (langkah 12, 16, dan langkah sesudah putaran 2) didahului `Verifikasi` kolom lain tampil pada tabel yang sama (bagian 8b butir 2); kolom lain tampil sesudah `F5` diverifikasi ulang karena halaman dimuat ulang.
- Pembagian TC lintas spec: TC-FA-SU-782 sampai TC-FA-SU-784 ada di spec 259; TC-FA-SU-786 dan TC-FA-SU-788 ada di spec 260; TC-FA-SU-787 ada di spec 275.
- Temuan untuk QA (S-15): (1) TC-FA-SU-785 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-785 tidak menyebut bahwa kolom `Group` harus diuji pada putaran terpisah; spec menetapkan dua putaran (turunan spec) supaya aturan satu kolom visible tetap terpenuhi. (3) Post Condition TC-FA-SU-785 (preferensi tersimpan per perangkat) tidak punya langkah observasi di luar `F5` pada tabel ini dan tidak diasersi pada tabel lain.
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01) dan dari langkah berulang per kolom, bukan dari langkah tambahan.
