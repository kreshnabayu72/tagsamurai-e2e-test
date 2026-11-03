---
id: TC-FA-SU-E2E-080-popup-assign-group-tambah-dan-cabut-sekaligus-cabut-semua-dan-cancel-tanpa-unsaved
title: "Popup Assign Group: Tambah dan Cabut Sekaligus, Cabut Semua, dan Cancel Tanpa Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-260
  - TC-FA-SU-261
  - TC-FA-SU-262
coverage:
  web: automated
---

# Popup Assign Group: Tambah dan Cabut Sekaligus, Cabut Semua, dan Cancel Tanpa Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; baris Disposal × Staff pada Finance & Accounting dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: Finance & Accounting dicabut dan IT Infrastructure ditambahkan pada Disposal × Staff (TC-FA-SU-260); seluruh grup dicabut (TC-FA-SU-261); IT Infrastructure dicentang lalu dibatalkan (TC-FA-SU-262).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini; dipulihkan ke Pre-setup #39 lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-260: Assign Group: tambah dan cabut sekaligus menghasilkan toast updated dan satu transaksi

1. Catat jumlah entri `Assign` dan `Remove` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
3. Hapus centang Finance & Accounting dan centang IT Infrastructure
4. Klik `[Save]`
5. Verifikasi dialog Title `Remove Transaction Role` (pencabutan, D-07) tampil
6. Verifikasi dialog `Change Transaction Role` (D-06) tidak tampil karena Role baris tidak berubah
7. Klik `[Remove]` pada dialog
8. Verifikasi toast "Success, Staff has been updated."
9. Verifikasi baris Disposal × Staff memuat IT Infrastructure tanpa Finance & Accounting (penambahan dan pencabutan tersimpan bersamaan)
10. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
11. Verifikasi satu entri `Assign` untuk grup tambahan IT Infrastructure bertambah dibanding baseline pada Tab Changelog
12. Verifikasi satu entri `Remove` untuk grup dicabut Finance & Accounting bertambah dibanding baseline pada Tab Changelog

### TC-FA-SU-261: Assign Group: seluruh grup dicabut tanpa penambahan menghapus baris dari tabel

13. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
14. Hapus centang seluruh grup lalu klik `[Save]`
15. Klik `[Remove]` pada dialog
16. Verifikasi baris Disposal × Staff hilang dari tabel
17. Verifikasi Sub-tab tetap menampilkan baris Borrowing & Assignment × Approver
18. Verifikasi toast "Success, Staff has been removed."

### TC-FA-SU-262: Assign Group: Cancel dan close membuang perubahan tanpa dialog Unsaved Changes

19. Pulihkan Transaction Role Mira Anggraini ke Pre-setup #39 lewat seed API
20. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
21. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
22. Centang IT Infrastructure lalu klik `[Cancel]`
23. Verifikasi popup menutup tanpa perubahan (kolom Group baris Disposal × Staff tetap Finance & Accounting)
24. Verifikasi tidak ada dialog Unsaved Changes
25. Klik `[Assign Group]` lagi pada baris Disposal × Staff, centang IT Infrastructure, lalu klik `[✕]`
26. Verifikasi popup menutup tanpa perubahan (kolom Group baris Disposal × Staff tetap Finance & Accounting)
27. Verifikasi tidak ada dialog Unsaved Changes
28. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
29. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 19 dan 20. Pemulihan lewat seed API memulihkan baris Disposal × Staff yang dihapus TC-FA-SU-261 sebelum TC-FA-SU-262 mengandalkannya (S-09); baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 10 sampai 12, 28 dan 29. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-262: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); popup menutup tanpa perubahan menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-SU-261 langkah 4 menyebut `[Remove]` pada dialog tanpa Expected untuk isi dialog; spec tidak mengasersi isi dialog pada TC-FA-SU-261. Post Condition TC-FA-SU-261 (entri `Remove` per grup, Settings > Role & Permission) dan TC-FA-SU-260 (tiga permukaan log) tidak punya langkah observasi tambahan di TC dan tidak diasersi.
  - TC-FA-SU-261 mencabut "seluruh grup" tanpa menyebut bahwa hasil TC-FA-SU-260 meninggalkan IT Infrastructure sebagai satu-satunya grup; spec memakai urutan TC apa adanya.
