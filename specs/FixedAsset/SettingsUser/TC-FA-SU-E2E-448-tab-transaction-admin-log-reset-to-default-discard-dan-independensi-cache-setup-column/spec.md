---
id: TC-FA-SU-E2E-448-tab-transaction-admin-log-reset-to-default-discard-dan-independensi-cache-setup-column
title: "Tab Transaction Admin Log: Reset to Default, Discard, dan Independensi Cache Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-788
coverage:
  web: automated
---

# Tab Transaction Admin Log: Reset to Default, Discard, dan Independensi Cache Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) sesuai Pre-setup #29 TC. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc` dan seret-dan-lepas (drag and drop) baris pada daftar Setup Column.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Hilangkan centang kolom `Group`
4. Drag kolom `Activity` satu posisi
5. Klik icon Pin pada kolom `Transaction ID`
6. Klik `[Reset to Default]`
7. Verifikasi Live Preview mengembalikan visibility, urutan, dan pin ke default modul
8. Klik `[Save]`
9. Verifikasi tabel menampilkan visibility, urutan, dan pin default
10. Klik header kolom `⋯`, lalu klik item `Setup Column...`
11. Hilangkan centang kolom `Group`
12. Klik `✕` pada popup Setup Column
13. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Group` tampil)
14. Klik header kolom `⋯`, lalu klik item `Setup Column...`
15. Hilangkan centang kolom `Group`
16. Tekan `Esc`
17. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Group` tampil)
18. Klik Back breadcrumb ke User List
19. Verifikasi konfigurasi kolom tabel User List tidak berubah

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16). Pembukaan popup Setup Column, perubahan pengaturan, dan penutupan popup adalah langkah TC.
- Pemulihan Setup Column: konfigurasi tabel sudah default sesudah `[Reset to Default]` dan `[Save]` di langkah 6 sampai 8, dan dua perubahan sesudahnya dibuang lewat `✕` dan `Esc`, sehingga tidak ada perubahan yang perlu dipulihkan selain cadangan hook `after` (bagian 8b butir 14).
- Pembagian TC lintas spec: TC-FA-SU-786 ada di spec 260, TC-FA-SU-787 ada di spec 275, TC-FA-SU-785 ada di spec 439.
- Temuan untuk QA (S-15): (1) TC-FA-SU-788 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (Pre-setup #1) dari hook suite. (2) Langkah Uji nomor 6 ("Buka tabel lain yang punya Setup Column dan bandingkan") tidak menyebut tabelnya; spec memakai tabel User List. Karena konfigurasi tabel ini sudah default sesudah `[Reset to Default]` dan `[Save]`, perbandingan itu tidak membuktikan independensi cache sepenuhnya. (3) Langkah Uji nomor 2 ("Ubah beberapa pengaturan") tidak menyebut pengaturannya; spec memilih hilangkan centang `Group`, drag `Activity`, dan Pin `Transaction ID`. (4) Post Condition tidak punya langkah observasi dan tidak diasersi.
