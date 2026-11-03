---
id: TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup
title: "Konkurensi: Akses Dicabut Saat Popup Terbuka, Item Bulk Berubah, Dua Admin, dan Grup Dihapus Saat Tree Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1020
  - TC-FA-SU-1022
  - TC-FA-SU-1023
  - TC-FA-SU-1031
coverage:
  web: automated
---

# Konkurensi: Akses Dicabut Saat Popup Terbuka, Item Bulk Berubah, Dua Admin, dan Grup Dihapus Saat Tree Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Admin B (#13), Global Settings (#38). Target: Gita Permata, Hana Kusuma (Pending Activation), dan Wawan Setiawan. Data Dinamis: grup `Gudang Uji {runId}-320` dibuat dan dihapus dalam spec ini (pengganti grup Logistics Warehouse Pre-setup #21 agar pohon grup bersama tidak berubah).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Sesi API Principal Automation (Pre-setup #12) dan Admin B (Pre-setup #13, Total Control) untuk memicu perubahan state (R-20), disediakan tim FE/BE; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan status aktif, penugasan peran, dan Home Group pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC; dijalankan sebagai langkah penghubung dan di hook `after` (cadangan).
- State global dan pemulihan: Gita Permata, Hana Kusuma, dan App Access FAMS Wawan Setiawan dipulihkan lewat seed API pada langkah penghubung dan di hook `after`; grup `Gudang Uji {runId}-320` dibersihkan di hook `after` bila masih ada. Efek pada Pre-setup: Last Updated dan Modified By Gita Permata, Hana Kusuma, dan Wawan Setiawan berubah dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1022: Item bulk berubah status di antara seleksi dan commit

1. Catat jumlah entri `Deactivate` pada Tab Changelog Gita Permata dan Hana Kusuma, Tab System Log aktor, dan Activity Log sebagai baseline
2. Centang Gita Permata dan Hana Kusuma (keduanya Active) di sesi A
3. Admin B (Total Control, sesi API) mendeaktivasi Hana Kusuma hingga status Inactive tersimpan (tanpa memuat ulang User List sesi A)
4. Klik Bulk Action > `[Deactivate]`, lalu klik `[Deactivate]` pada dialog
5. Verifikasi Hana Kusuma (sudah berubah status oleh Admin B) dilewati dan tercantum pada hasil sebagian
6. Verifikasi Gita Permata diproses dan berstatus Inactive
7. Verifikasi toast "Success, user has been deactivated. Some items were skipped."
8. Verifikasi jumlah entri `Deactivate` bertambah satu untuk Gita Permata dan satu untuk Hana Kusuma (dari Admin B), tanpa entri kedua untuk Hana Kusuma, pada Tab Changelog target, Tab System Log aktor, dan Activity Log
9. Pulihkan Gita Permata dan Hana Kusuma menjadi Active lewat seed API dan kosongkan seleksi (Unselect All)

### TC-FA-SU-1023: Dua admin mengedit peran dan status pengguna yang sama pada waktu berdekatan

10. Ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
11. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
12. Admin A mencentang Update pada Manage accounting
13. Admin B (Total Control, sesi API) mendeaktivasi Gita Permata hingga status Inactive tersimpan
14. Verifikasi perubahan peran oleh Admin A tersimpan: Update Manage accounting tercentang
15. Verifikasi Deactivate oleh Admin B tersimpan: Gita Permata berstatus Inactive
16. Verifikasi tidak ada dialog konflik versi dan tidak ada status 409
17. Verifikasi kedua perubahan memiliki entri log sendiri: jumlah entri `Edit` Object `Global Role` bertambah satu dan `Deactivate` bertambah satu pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
18. Pulihkan Gita Permata (Active, Update Manage accounting tidak tercentang) lewat seed API

### TC-FA-SU-1031: Hapus grup saat Select Group atau tree Group terbuka

19. Buat grup `Gudang Uji {runId}-320` lewat seed API
20. Kembali ke User List, ketik Search `Wawan`, tekan Enter, klik nama Wawan Setiawan, lalu buka Tab Role > Sub-tab Group Role
21. Buka popup Assign Group Role Manage files, buka popup Select Group, dan centang `Gudang Uji {runId}-320`
22. Admin B menghapus grup `Gudang Uji {runId}-320` di Settings > Groups lewat sesi API hingga penghapusan tersimpan
23. Klik `[Select]` lalu klik `[Save]` pada popup Assign Group Role
24. Verifikasi Sub-tab Group Role Wawan Setiawan menampilkan Manage files (anchor penugasan yang ada)
25. Verifikasi penolakan stale: grup yang sudah dihapus tidak ditugaskan pada Group Role Manage files Wawan Setiawan
26. Verifikasi tree grup di-refresh setelah penolakan
27. Klik `✕` pada popup Assign Group Role
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

### TC-FA-SU-1020: Akses FAMS pengguna target dicabut saat popup terbuka

30. Buka popup Assign Group Role Manage files Wawan Setiawan
31. Principal Automation mencabut App Access FAMS Wawan Setiawan di Global Settings lewat sesi API hingga pencabutan tersimpan
32. Klik `[Save]`
33. Verifikasi toast netral "This user is no longer available."
34. Verifikasi popup yang terbuka ditutup
35. Verifikasi daftar User List di-refresh
36. Verifikasi Wawan Setiawan tidak ada pada User List
37. Berikan kembali App Access FAMS Wawan Setiawan lewat seed API

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1022, 1023, 1031, 1020): pencabutan App Access Wawan Setiawan (TC-FA-SU-1020) di akhir karena menghapus akses data bersama (S-10).
- TC-FA-SU-1020, 1022, 1023, dan 1031 berlabel `Manual Only (d) dua sesi paralel`; pelaku kedua (Admin B dan Principal Automation) memakai sesi API (R-20), sehingga TC tetap masuk spec ini tanpa butir `P-2`.
- TC-FA-SU-1031 memakai grup uji milik spec sebagai pengganti Logistics Warehouse (S-06) karena TC menghapus grup itu.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 9, 10, 11, 18, 19, 20, 37. Langkah 24 adalah anchor positif untuk asersi absence pada langkah 25 (8b.2), dan langkah 35 untuk langkah 36.
- Spec ini 37 langkah (di atas smell 35 langkah). Alasan: seluruh blok satu topik (konkurensi) dan tiap blok berdiri sendiri dengan pengguna dan grup uji sendiri; tambahan dua langkah berasal dari anchor asersi absence.
- Temuan untuk QA:
  - Teks toast sebagian TC-FA-SU-1022 tidak disebut TC ("toast sebagian skip tampil"); spec memakai teks yang sama dengan toast bulk Deactivate sebagian pada TC-FA-SU-1063 ("Success, user has been deactivated. Some items were skipped.").
  - Kondisi popup Assign Group Role sesudah penolakan stale TC-FA-SU-1031 (tetap terbuka atau tertutup) tidak disebut TC; spec menutup popup lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]`.
  - Expected TC-FA-SU-1031 "penolakan stale" tidak menyebut teks toast atau pesan; spec mengasersi hasilnya (grup tidak ditugaskan).
  - TC-FA-SU-1020 berstatus P1 tetapi mencabut App Access pengguna bersama; spec memakai Wawan Setiawan dan memulihkan lewat seed API.
