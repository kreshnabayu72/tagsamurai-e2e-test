---
id: TC-FA-SU-E2E-093-dialog-gabungan-group-manager-pada-edit-home-group-konfirmasi-cancel-dan-satu-grup
title: "Dialog Gabungan Group Manager pada Edit Home Group: Konfirmasi, Cancel, dan Satu Grup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-294
  - TC-FA-SU-295
  - TC-FA-SU-296
coverage:
  web: automated
---

# Dialog Gabungan Group Manager pada Edit Home Group: Konfirmasi, Cancel, dan Satu Grup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable; memegang baris pola Group Manager pada kedua grup: Group Role katalog selain Manage user & role dengan CRUD penuh sesuai kolom yang berlaku dan Transaction Role Asset Admin serta Approver pada setiap Jenis Transaksi), akun `FA_GM_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, serta entri `Remove (via Group Manager)` pada modal Changelog User > Group Role, modal Changelog User > Transaction Role, Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan baca notifikasi in-app per pengguna (disediakan tim FE/BE): jumlah notifikasi Auto-Revert Oscar Pranata dibaca sebelum aksi.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Oscar Pranata (Home Group dan status Group Manager IT Infrastructure serta Accounts Payable) di hook `after`. Efek pada Pre-setup: Home Group, status Group Manager, dan baris pola Group Manager IT Infrastructure Oscar Pranata berubah (Last Updated, Modified By), entri log permanen `Edit Home Group` dan `Auto-Revert` bertambah, entri `Remove (via Group Manager)` bertambah di kedua modal Changelog User, dan Oscar Pranata menerima notifikasi in-app. Spec berakhir pada akun Oscar Pranata; hook `after` memulihkan sesi ke akun default suite.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role, modal Changelog User > Transaction Role, Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, jumlah notifikasi Auto-Revert Oscar Pranata, serta Home Group Oscar Pranata sebagai baseline

### TC-FA-SU-294: Dialog D-10 memuat bullet Group Role dan Group Manager

2. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
3. Klik node Accounts Payable lalu klik `[Select]`
4. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` memuat bullet `• Manage group — IT Infrastructure` dan `• Group Manager — IT Infrastructure`, kalimat `Setting the Home Group constraint to Accounts Payable for Oscar Pranata will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
5. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` tampil

### TC-FA-SU-296: Cancel dialog D-10

6. Klik `[Cancel]` pada dialog
7. Verifikasi tidak ada toast
8. Buka Detail Oscar Pranata > Tab Role
9. Verifikasi banner Group Manager Oscar Pranata tetap memuat IT Infrastructure dan Accounts Payable
10. Verifikasi Home Group Oscar Pranata sama dengan baseline
11. Baca jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
12. Verifikasi jumlah entri sama dengan baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-295: Konfirmasi dialog D-10

13. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata dan klik `Edit Home Group`
14. Klik node Accounts Payable lalu klik `[Select]`
15. Klik `[Revoke]`
16. Verifikasi toast "Success, home group has been updated." tampil (bukan toast T-06)
17. Verifikasi Home Group Oscar Pranata berubah menjadi Accounts Payable
18. Buka Detail Oscar Pranata > Tab Role
19. Verifikasi banner Group Manager Oscar Pranata hanya memuat grup yang masih dikelola
20. Buka Tab Changelog Oscar Pranata
21. Verifikasi entri `Edit Home Group` tercatat
22. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — IT Infrastructure` / Old Value `Assigned` / New Value `—` tercatat
23. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role, buka modal Changelog User > Group Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
24. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role bertambah dibanding baseline, satu entri untuk tiap baris pola Group Role Group Manager IT Infrastructure (pada node itu dan turunannya) yang dicabut (tidak silent)
25. Tutup modal dengan `[✕]`, klik Sub-tab Transaction Role, buka modal Changelog User > Transaction Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
26. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Transaction Role bertambah dibanding baseline, satu entri untuk tiap baris pola Transaction Role Group Manager IT Infrastructure (pada node itu dan turunannya) yang dicabut (tidak silent)
27. Tutup modal dengan `[✕]`
28. Baca jumlah entri `Edit Home Group`, `Auto-Revert`, dan `Remove (via Group Manager)` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
29. Verifikasi jumlah entri `Edit Home Group` dan `Auto-Revert` bertambah masing-masing 1 dibanding baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
30. Verifikasi jumlah entri `Remove (via Group Manager)` sama dengan baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log (entri itu hanya tampil di kedua modal Changelog User)
31. Ganti akun: Logout lalu login sebagai Oscar Pranata
32. Buka panel notifikasi
33. Verifikasi Oscar Pranata menerima notifikasi in-app view-only (jumlah notifikasi Auto-Revert bertambah 1 dibanding baseline)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-296 (Cancel) diletakkan sebelum TC-FA-SU-295 (Revoke) karena TC-FA-SU-296 mensyaratkan Oscar Pranata belum berubah; TC-FA-SU-295 menulis ulang "Ulangi perubahan hingga dialog tampil" (S-04).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan membuka Tab Changelog atau panel notifikasi. Satu entri yang diamati pada tiga surface ditulis satu `Verifikasi` selisih jumlah (S-01). TC-FA-SU-296 "tidak ada entri log" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan kelas g.
- Langkah penghubung tambahan (S-03): langkah 23, 25, dan 27 (membuka dan menutup modal Changelog User per Sub-tab); langkah 23 dan 25 sekaligus membaca jumlah entri `Remove (via Group Manager)` lewat kemampuan baca tim FE/BE. Expected e TC-FA-SU-295 ("hanya di Modal Changelog User > Group Role dan > Transaction Role") ditulis sebagai selisih positif pada kedua modal (langkah 24 dan 26) dan selisih nol pada tiga surface lain (langkah 30), dengan Verifikasi entri `Auto-Revert` (langkah 29) sebagai anchor positif (bagian 8b butir 2); tidak ada spec absence yang memuat aksi nyata TC ini sehingga Verifikasi berbaseline ada di spec ini (S-05, S-12).
- Temuan untuk QA (S-15): (1) Home Group awal Oscar Pranata tidak tertulis di Pre-setup TC; spec membandingkan dengan nilai yang dicatat pada baseline. (2) Expected b TC-FA-SU-294 ("satu klik `[Revoke]` menyimpan keduanya") diamati pada TC-FA-SU-295. (3) Post Condition TC-FA-SU-295 butir a dan b diamati pada Expected; Post Condition TC-FA-SU-296 butir lain tanpa observasi tidak diasersi. (4) Expected e TC-FA-SU-295 menyebut baris pola "pada node itu dan turunannya" tanpa daftar baris dan jumlah; spec mengasersi selisih jumlah entri tanpa angka absolut.
