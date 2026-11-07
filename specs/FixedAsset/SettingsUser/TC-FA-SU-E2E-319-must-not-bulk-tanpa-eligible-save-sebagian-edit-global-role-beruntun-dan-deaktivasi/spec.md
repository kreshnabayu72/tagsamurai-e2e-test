---
id: TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi
title: "Must NOT: Bulk Tanpa Eligible, Save Sebagian, Edit Global Role Beruntun, dan Deaktivasi Tanpa Hard-block"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1027
  - TC-FA-SU-1028
  - TC-FA-SU-1029
  - TC-FA-SU-1030
coverage:
  web: automated
---

# Must NOT: Bulk Tanpa Eligible, Save Sebagian, Edit Global Role Beruntun, dan Deaktivasi Tanpa Hard-block

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Admin B (#13), Global Settings (#38: Rudi Hartono nonaktif di Global Settings; Vina Maharani Active), Responsibilities (#24, #25). Target: Rudi Hartono, Vina Maharani, Budi Santoso (aset aktif dan approval tertunda), Gita Permata (Manage accounting: Create dan Read tercentang), dan Wawan Setiawan (Manage files). Data Dinamis: grup `Gudang Uji {runId}-319` dibuat dan dihapus dalam spec ini (pengganti grup Logistics Warehouse Pre-setup #21 agar pohon grup bersama tidak berubah).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Sesi API Principal Automation (Pre-setup #12) dan Admin B (Pre-setup #13, Total Control) untuk memicu perubahan state (R-20), disediakan tim FE/BE; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Pencatat request jaringan halaman (disediakan tim FE/BE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan status aktif, penugasan peran, dan Home Group pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC; dijalankan sebagai langkah penghubung dan di hook `after` (cadangan).
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Wawan Setiawan (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node General Affairs dan grup uji `Gudang Uji {runId}-319` (langkah 30) tidak Disabled oleh gate Home Group constraint; Home Group Wawan Setiawan dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- State global dan pemulihan: Vina Maharani, Budi Santoso, dan nilai CRUD Gita Permata dipulihkan lewat seed API pada langkah penghubung dan di hook `after`; grup `Gudang Uji {runId}-319` dibersihkan di hook `after` bila masih ada. Efek pada Pre-setup: Last Updated dan Modified By Budi Santoso dan Gita Permata berubah dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1029: Bulk Deactivate tanpa baris eligible tidak mengirim request ke server

1. Principal Automation menonaktifkan Vina Maharani di Global Settings lewat sesi API hingga status nonaktif tersimpan (Rudi Hartono sudah nonaktif di Global Settings, Pre-setup #38)
2. Muat ulang halaman User List
3. Ketik Search `Rudi Hartono`, tekan Enter, lalu centang Rudi Hartono
4. Ganti isi kotak search dengan `Vina Maharani`, tekan Enter, lalu centang Vina Maharani
5. Aktifkan pencatat request jaringan halaman, lalu klik Bulk Action > `[Deactivate]`
6. Verifikasi Dialog Blok tampil
7. Verifikasi jaringan tidak memuat request bulk saat Dialog Blok tampil
8. Klik `[OK]`
9. Verifikasi seleksi dua baris tidak di-reset
10. Verifikasi Bulk Actions Bar tidak di-reset
11. Pulihkan Vina Maharani menjadi aktif di Global Settings lewat seed API dan kosongkan seleksi (Unselect All)

### TC-FA-SU-1027: Deaktivasi tidak pernah di-hard-block oleh aset aktif atau approval tertunda

12. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu klik sakelar Active baris Budi Santoso (memegang aset aktif dan ditunggu sebagai approver)
13. Verifikasi tombol `[Deactivate]` pada dialog Enabled walau Budi Santoso memegang aset aktif dan ditunggu sebagai approver
14. Klik `[Deactivate]`
15. Verifikasi deaktivasi berhasil: sakelar Active baris Budi Santoso OFF
16. Klik nama Budi Santoso lalu buka Tab Responsibilities
17. Verifikasi aset yang dipegang Budi Santoso tetap tercatat pada Sub-tab Borrowed Assets dan Assigned Assets
18. Pulihkan Budi Santoso menjadi Active lewat seed API

### TC-FA-SU-1030: Edit Global Role oleh aktor yang sama pada dua checkbox beruntun cepat

19. Kembali ke User List, ganti isi kotak search dengan `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
20. Catat jumlah entri `Edit` Object `Global Role` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
21. Centang Update lalu segera centang Delete pada Manage accounting (keduanya awalnya tidak tercentang)
22. Verifikasi Update dan Delete Manage accounting keduanya tercentang dan tersimpan
23. Buka Tab Changelog
24. Verifikasi dua entri `Edit` dengan Field `Manage accounting — Update` dan `Manage accounting — Delete` tercatat
25. Verifikasi jumlah entri `Edit` Object `Global Role` bertambah dua pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
26. Pulihkan nilai CRUD Manage accounting Gita Permata (Update dan Delete tidak tercentang) lewat seed API

### TC-FA-SU-1028: Save sebagian saat ada referensi grup stale tidak pernah terjadi

27. Buat grup `Gudang Uji {runId}-319` lewat seed API
28. Kembali ke User List, ganti isi kotak search dengan `Wawan`, tekan Enter, klik nama Wawan Setiawan, lalu buka Tab Role > Sub-tab Group Role
29. Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
30. Buka popup Assign Group Role Manage files dan tambah General Affairs serta `Gudang Uji {runId}-319`
31. Admin B menghapus grup `Gudang Uji {runId}-319` di Settings > Groups lewat sesi API hingga penghapusan tersimpan
32. Klik `[Save]`
33. Verifikasi popup Assign Group Role tetap terbuka
34. Verifikasi jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sama dengan baseline
35. Klik `✕` pada popup Assign Group Role
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Verifikasi Sub-tab Group Role Wawan Setiawan menampilkan Manage files (anchor penugasan yang ada)
39. Verifikasi Save yang memuat satu grup stale ditolak seluruhnya: General Affairs tidak tersimpan pada Sub-tab Group Role Manage files

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1029, 1027, 1030, 1028): blok yang hanya mengubah state ringan lebih dulu, dan blok yang membuat dan menghapus grup terakhir.
- TC-FA-SU-1028 memakai grup uji milik spec sebagai pengganti Logistics Warehouse (S-06) karena TC menghapus grup itu di Settings > Groups; TC-FA-SU-1028 berlabel `Manual Only (d) dua sesi paralel` dan pelaku kedua memakai sesi API (R-20).
- TC-FA-SU-1028 Expected b "tidak ada entri log" pada Save yang ditolak ditulis sebagai asersi jumlah dengan baseline (bagian 3, asersi jumlah bukan kelas g).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 2, 11, 18, 19, 20, 26, 27, 28, 29. Langkah 3 dan 4 (Search per pengguna lalu centang), 5 (aktifkan pencatat request, dipisah dari pemicu), dan 12 (Search lalu klik sakelar) adalah langkah aksi tanpa asersi; langkah 3, 4, 12, 19, dan 28 juga Search untuk menemukan baris target di luar halaman 1 (R-16). Langkah 6 (Dialog Blok tampil) adalah anchor positif untuk asersi absence request bulk pada langkah 7, dan langkah 38 adalah anchor positif untuk asersi absence pada langkah 39 (8b.2).
- Spec ini 39 langkah (di atas smell 35 langkah). Alasan: seluruh blok satu topik (aksi yang tidak boleh terjadi: Must NOT) dan tiap blok berdiri sendiri; tambahan empat langkah berasal dari Search per baris target dan anchor absence.
- Pre-setup #50 diterapkan hanya pada Wawan Setiawan (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih General Affairs dan grup uji `Gudang Uji {runId}-319` (langkah 30); Home Group Wawan Setiawan dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - Teks Dialog Blok TC-FA-SU-1029 tidak disebut TC; spec hanya mengasersi bahwa request bulk tidak terkirim dan seleksi tidak di-reset.
  - TC-FA-SU-1028 menyebut Logistics Warehouse sebagai grup yang dihapus; spec memakai grup uji milik spec (S-06).
  - Expected b TC-FA-SU-1030 menulis Field `Manage accounting — Update` dan `Manage accounting — Delete`; spec mengutipnya persis.
  - TC-FA-SU-1029 tidak menyebut apakah seleksi dipertahankan saat Search diganti; spec memilih satu pengguna per Search (langkah 3-4) dan mengasumsikan seleksi pertama tetap tercentang sampai Bulk Action; bila tidak, tim QA perlu menetapkan cara memilih dua baris di halaman berbeda.
  - TC-FA-SU-1027 tidak menyebut teks toast sukses Deactivate; spec mengasersi status sakelar OFF.
