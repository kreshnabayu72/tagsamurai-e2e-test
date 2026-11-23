---
id: TC-FA-SU-E2E-260-tab-transaction-admin-log-setup-column
title: "Tab Transaction Admin Log: Setup Column (Drag Reorder)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-786
coverage:
  web: automated
---

# Tab Transaction Admin Log: Setup Column (Drag Reorder)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Kemampuan teknis (disediakan tim FE): seret-dan-lepas (drag and drop) baris pada daftar Setup Column.
- Tabel "Kolom Setup Column Hideable" (urutan semula, posisi 1 = paling atas pada daftar Setup Column dan paling kiri pada tabel): `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`.
- Tabel "Urutan Drag Setup Column" (parameter langkah berulang; dijalankan berurutan dari baris pertama, tiap baris drag satu posisi tanpa `[Save]` di antaranya sehingga efeknya kumulatif; posisi akhir dihitung dari urutan semula): (1) `Activity` ke atas, posisi akhir 2; (2) `Date` ke bawah, posisi akhir 3; (3) `Group` ke atas, posisi akhir 4; (4) `Name` ke bawah, posisi akhir 6; (5) `Borrower` ke atas, posisi akhir 5; (6) `Transaction ID` ke atas, posisi akhir 1. Urutan akhir: `Transaction ID`, `Activity`, `Date`, `Group`, `Borrower`, `Name`.

## Test Steps

### TC-FA-SU-786: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Untuk setiap baris pada tabel "Urutan Drag Setup Column" secara berurutan (langkah 4 sampai 5):
4. Drag kolom pada baris tersebut satu posisi ke arah (atas atau bawah) yang tertulis pada tabel
5. Verifikasi urutan Live Preview berubah
6. Klik `[Save]`
7. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 8):
8. Verifikasi kolom pada baris tersebut menempati posisi akhirnya pada tabel
9. Klik `F5`
10. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 11):
11. Verifikasi kolom pada baris tersebut tetap menempati posisi akhirnya pada tabel setelah refresh (`F5`)
12. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan langkah 12 (penghapusan preferensi kolom di browser sesudah geser dan simpan, bagian 8b butir 14, S-09).
- Langkah berulang (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 6 kali, langkah 8 dijalankan 6 kali, langkah 11 dijalankan 6 kali (satu iterasi per baris tabel "Urutan Drag Setup Column"); jumlah langkah dengan ekspansi 32.
- Pembagian TC lintas spec: TC-FA-SU-785 ada di spec 439; TC-FA-SU-782 sampai TC-FA-SU-784 ada di spec 259; TC-FA-SU-787 ada di spec 275; TC-FA-SU-788 ada di spec 448.
- Temuan untuk QA (S-15): (1) TC-FA-SU-786 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (Pre-setup #1) dari hook suite. (2) TC-FA-SU-786 tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan menetapkan arah serta posisi akhir tiap kolom pada tabel "Urutan Drag Setup Column" (turunan spec, bukan dari TC) supaya `Verifikasi` posisi punya nilai pasti.
