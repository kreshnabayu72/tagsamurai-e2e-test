---
id: TC-FA-SU-E2E-087-penugasan-grup-ganda-dan-grup-dihapus-sebelum-save-popup-assign-group-role
title: "Penugasan Grup Ganda dan Grup Dihapus Sebelum Save pada Popup Assign Group Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-209
  - TC-FA-SU-210
coverage:
  web: automated
---

# Penugasan Grup Ganda dan Grup Dihapus Sebelum Save pada Popup Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Pelaku kedua (Admin B, Pre-setup #13): sesi API yang memicu perubahan state tanpa konteks UI kedua (R-20); akun disediakan tim FE. Admin B menambahkan penugasan (TC-FA-SU-209) dan menghapus grup (TC-FA-SU-210) hingga tersimpan.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya.
- Data uji: grup General Affairs (TC-FA-SU-209) dan grup Logistics Warehouse yang dihapus Admin B di Settings > Groups (TC-FA-SU-210).
- Kemampuan teknis: seed API untuk memulihkan penugasan Group Role Wawan Setiawan serta grup Logistics Warehouse beserta penugasannya (Pre-setup #21 dan #23) sesudah dihapus (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10).
- State global yang diubah: penugasan `Manage files` Wawan Setiawan (General Affairs ditambahkan oleh Admin B) dan grup Logistics Warehouse (dihapus); keduanya dipulihkan lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Wawan Setiawan (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node General Affairs (langkah 2 dan penugasan Admin B langkah 3) dan Logistics Warehouse (langkah 13) tidak Disabled oleh gate Home Group constraint dan penugasan Admin B lewat sesi API tidak ditolak `422`; Home Group Wawan Setiawan dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-209: Penugasan grup ganda ke role yang sama dipaksa: toast duplikat dan popup tetap terbuka

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
2. Klik `[+ Assign Group]`, centang General Affairs, klik `[Select]`
3. Admin B menambahkan General Affairs ke Manage files Wawan Setiawan lewat sesi API hingga penugasan tersimpan
4. Catat jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline (sesudah penugasan Admin B)
5. Klik `[Save]`
6. Verifikasi toast "Error, failed to save group role. This group is already assigned to this role."
7. Verifikasi popup tetap terbuka dengan isi utuh
8. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter
9. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sama dengan baseline
10. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role, buka popup Assign Group Role Manage files, klik `[✕]`, verifikasi dialog `Unsaved Changes`, klik `[Leave]`
11. Pulihkan penugasan Manage files Wawan Setiawan ke Pre-setup #23 lewat seed API

### TC-FA-SU-210: Grup dihapus sebelum Save: toast stale, baris stale dibersihkan, dan popup tetap terbuka

12. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
13. Klik `[+ Assign Group]`, centang Logistics Warehouse, klik `[Select]`
14. Admin B menghapus grup Logistics Warehouse di Settings > Groups lewat sesi API hingga grup terhapus
15. Catat jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
16. Klik `[Save]`
17. Verifikasi toast "Error, failed to save group role. One or more selected groups no longer exist. Please select another."
18. Verifikasi baris stale Logistics Warehouse dibersihkan dari tabel popup
19. Verifikasi popup tetap terbuka
20. Klik `[✕]`
21. Verifikasi kolom Group baris Manage files tidak berubah (tidak ada perubahan tersimpan)
22. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter
23. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sama dengan baseline
24. Pulihkan grup Logistics Warehouse beserta penugasannya lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 4, 10, 11, 15 dan 24. Baseline log dicatat sesudah aksi Admin B karena aksi itu sendiri menambah entri log (S-12); penutupan popup dirty mengikuti S-08; pemulihan lewat seed API memulihkan Pre-setup #21 dan #23 (S-09).
- Langkah pola baca-log: langkah 8, 9, 22 dan 23. Search `Wawan Setiawan` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Pelaku kedua dipicu lewat sesi API dan bukan konteks UI kedua, sehingga tidak memakai `P-2` (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`).
- Klausa "tidak ada entri log" pada TC-FA-SU-209 dan 210 adalah aksi yang gagal sehingga ditulis sebagai asersi jumlah dengan baseline di spec fungsional (bagian 3 prinsip 13 butir g, S-12); toast error menjadi anchor positif.
- TC-FA-SU-207 dan 208 (popup yang sama tanpa pelaku kedua) ada di spec 063.
- Pre-setup #50 diterapkan hanya pada Wawan Setiawan (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih General Affairs (langkah 2 dan penugasan Admin B langkah 3) dan Logistics Warehouse (langkah 13); Home Group Wawan Setiawan dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - TC-FA-SU-209 langkah 1 menyebut "Dua sesi admin menambahkan General Affairs secara berurutan hingga sesi kedua menimpa" tanpa menyebut sesi mana yang memiliki popup yang terbuka; spec memakai aktor UI sebagai sesi kedua yang menekan `[Save]` sesudah Admin B menyimpan.
  - TC-FA-SU-210 butir c ("tidak ada perubahan tersimpan") tidak menyebut cara observasi; spec mengasersi kolom Group baris Manage files setelah popup ditutup dan mengasumsikan popup tidak dirty setelah baris stale dibersihkan (TC-FA-SU-207 butir c).
  - Post Condition TC-FA-SU-209 dan 210 (tidak ada perubahan tersimpan dan tidak ada entri baru) sudah tercakup oleh Expected b dan c; tidak ada Post Condition tambahan yang diasersi.
