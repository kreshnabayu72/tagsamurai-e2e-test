---
id: TC-FA-SU-E2E-445-tab-transaction-admin-log-borrow-baris-per-aset-dan-aksi-draft
title: "Tab Transaction Admin Log Sub-tab Borrow: Baris per Aset dan Aksi Draft"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1134
  - TC-FA-SU-1135
  - TC-FA-SU-1136
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Borrow: Baris per Aset dan Aksi Draft

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Nama pengguna dan Group dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before`, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan): `Gita Permata {runId}-445`, email `gita.permata+{runId}-445@qwertysystem.net`, Active, ber-Transaction Role Borrowing & Assignment sebagai PIC (Approver) pada Group asal aset di bawah. Sub-tab Transaction Admin Log Borrow pengguna ini kosong sebelum spec berjalan sehingga baseline awal nol. Jumlah baris sub-tab Borrow pengguna ini tidak melewati 9 baris sehingga tabel satu halaman (ukuran halaman 10).
- Seed transaksi dan aset milik spec (kemampuan disediakan tim FE/BE, tanpa endpoint karangan): transaksi Borrow T1 yang memuat dua aset (aset 1 dan aset 2, Group asal `General Affairs`) dengan Borrower `Rina Wijaya`; dua aset lain untuk Draft (aset 3 dan aset 4, Group asal `Finance & Accounting`). Nama aset tampil `[Asset Name] - [Increment]` (increment dihasilkan sistem; pada TC `Laptop Dell Latitude - 6` dan `Monitor LG 24 - 2`). Transaction ID T1 dihasilkan sistem (pada TC `BRW-2026-0316`).
- Kemampuan pelaku lewat sesi API (disediakan tim FE/BE, bukan konteks UI kedua; langkah ditulis "... hingga ... tersimpan", R-20): login API `Gita Permata {runId}-445` (kredensial disediakan tim FE/BE, tanpa nama env baru) untuk Approve T1, membuat, mengedit, menyimpan, dan menghapus Borrow Draft. Jalur aksi (UI Borrow atau API) tidak ditetapkan TC (lihat Temuan untuk QA).
- Log muncul eventual; sesudah aksi, halaman dimuat ulang tiap 5 detik sampai baris baru tampil (batas 2 menit, idiom polling bagian 6).

## Test Steps

1. Ketik Search `Gita Permata {runId}-445`, tekan Enter, klik Name Gita Permata {runId}-445, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow

### TC-FA-SU-1134: Aksi bulk atas beberapa aset menghasilkan satu baris per aset

2. Catat baseline jumlah baris sub-tab Borrow
3. Approve transaksi T1 (dua aset) dalam satu aksi sebagai `Gita Permata {runId}-445` lewat sesi API hingga transaksi tersimpan
4. Tunggu aksi selesai
5. Muat ulang halaman tiap 5 detik sampai baris baru tampil (batas 2 menit), lalu klik Tab Transaction Admin Log dan Sub-tab Borrow
6. Verifikasi jumlah baris bertambah 2 dari baseline dan kedua baris baru bertransaksi T1 (satu baris per aset, bukan satu baris gabungan)
7. Verifikasi kedua baris baru Activity `Approved` dengan Name aset 1 dan Name aset 2
8. Verifikasi kedua baris memuat Transaction ID T1, Borrower `Rina Wijaya`, dan Group `General Affairs`

### TC-FA-SU-1135: Aksi Draft menulis satu baris per aset

9. Catat baseline jumlah baris sub-tab Borrow
10. Buat Borrow Draft berisi aset 3 dan aset 4 tanpa Borrower sebagai `Gita Permata {runId}-445` lewat sesi API hingga Draft tersimpan
11. Edit Draft: tetapkan Borrower `Andi Pratama` lalu simpan lewat sesi API hingga perubahan tersimpan
12. Simpan Draft lagi tanpa mengubah isi lewat sesi API hingga tersimpan
13. Hapus Draft lewat sesi API hingga terhapus
14. Tunggu aksi selesai
15. Muat ulang halaman tiap 5 detik sampai baris Draft terbaru tampil (batas 2 menit), lalu klik Tab Transaction Admin Log dan Sub-tab Borrow
16. Verifikasi `Draft created`: dua baris (satu per aset dalam Draft) dengan Transaction ID `—` dan Borrower `—`
17. Verifikasi `Draft edited`: dua baris dengan Transaction ID `—` dan Borrower `Andi Pratama`
18. Verifikasi `Draft deleted`: dua baris dengan Transaction ID `—`
19. Verifikasi jumlah baris bertambah tepat 6 dari baseline (Simpan Draft tanpa perubahan isi tidak menambah baris)
20. Verifikasi Activity setiap baris Draft tampil sebagai teks biasa tanpa badge berwarna
21. Verifikasi Name setiap baris Draft berformat `[Asset Name] - [Increment]`
22. Verifikasi Group setiap baris Draft `Finance & Accounting`

### TC-FA-SU-1136: Aksi atas Draft tanpa aset menulis satu baris

23. Catat baseline jumlah baris sub-tab Borrow
24. Buat Borrow Draft tanpa aset dan tanpa Borrower sebagai `Gita Permata {runId}-445` lewat sesi API hingga Draft tersimpan
25. Tunggu aksi selesai
26. Muat ulang halaman tiap 5 detik sampai baris Draft baru tampil (batas 2 menit), lalu klik Tab Transaction Admin Log dan Sub-tab Borrow
27. Verifikasi tersedia satu baris baru Activity `Draft created` dengan Transaction ID `—`, Name `—`, Borrower `—`, dan Group `—`
28. Verifikasi jumlah baris bertambah tepat 1 dari baseline (tidak ada baris tambahan untuk aset)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna lewat Search di User List, R-16, lalu membuka tab dan sub-tab), langkah 2, 9, dan 23 (mencatat baseline sebelum pemicu tiap TC, S-12), langkah 4, 14, dan 25 (Tunggu aksi selesai, 8b.8), dan langkah 5, 15, dan 26 (memuat ulang sampai log eventual tampil lalu membuka kembali sub-tab). Aksi pada langkah 3, 10 sampai 13, dan 24 dilakukan lewat sesi API sebagai pelaku kedua dan bukan objek asersi (R-20).
- Baris baru dibaca sebagai himpunan baris sesuai selisih jumlah dari baseline; urutan di antara baris dalam menit yang sama tidak diasersi (S-14). Tabel satu halaman sehingga baris dikenali lewat Activity, Name, dan Transaction ID tanpa Search (R-23).
- Temuan untuk QA (S-15): TC-FA-SU-1134 sampai 1136 menulis "Sebagai Gita Permata" (Approver, pembuat Draft) tetapi ACC hanya #1 dan #29; akun Gita Permata, jalur aksi (UI Borrow atau sesi API), dan ID literal `BRW-2026-0316` tidak ditetapkan. Spec memakai Gita Permata milik spec bersuffix dengan aksi lewat sesi API dan merujuk Transaction ID sebagai T1 hasil seed. TC-FA-SU-1135 Expected c ("tidak menambah baris") dan TC-FA-SU-1136 Expected b ("tidak ada baris tambahan") adalah asersi jumlah; ditulis di spec fungsional ini dengan selisih terhadap baseline (langkah 19 dan 28). TC-FA-SU-1135 tidak menyatakan urutan Activity pada baris Draft maupun Group aset Draft selain `Finance & Accounting`. Post Condition tidak ada.
