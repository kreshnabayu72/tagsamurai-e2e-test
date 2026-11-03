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
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable dengan Group Role Manage group C/R/U/D pada kedua grup), akun `FA_GM_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan baca notifikasi in-app per pengguna (disediakan tim FE/BE): jumlah notifikasi Auto-Revert Oscar Pranata dibaca sebelum aksi.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Oscar Pranata (Home Group dan status Group Manager IT Infrastructure serta Accounts Payable) di hook `after`. Efek pada Pre-setup: Home Group dan status Group Manager Oscar Pranata berubah (Last Updated, Modified By), entri log permanen `Edit Home Group` dan `Auto-Revert` bertambah, dan Oscar Pranata menerima notifikasi in-app. Spec berakhir pada akun Oscar Pranata; hook `after` memulihkan sesi ke akun default suite.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log, jumlah notifikasi Auto-Revert Oscar Pranata, serta Home Group Oscar Pranata sebagai baseline

### TC-FA-SU-294: Dialog gabungan D-05c

2. Klik ⋯ pada baris Oscar Pranata lalu klik `Edit Home Group`
3. Klik node Accounts Payable lalu klik `[Select]`
4. Verifikasi dialog Title `Remove Group Manager` memuat bagian konfirmasi constraint (daftar Group Role yang akan dicabut) lebih dulu, diikuti `This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited.` dan `Are you sure you want to remove it?`
5. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` tampil

### TC-FA-SU-296: Cancel dialog gabungan

6. Klik `[Cancel]` pada dialog
7. Verifikasi tidak ada toast
8. Buka Detail Oscar Pranata > Tab Role
9. Verifikasi banner Group Manager Oscar Pranata tetap memuat IT Infrastructure dan Accounts Payable
10. Verifikasi Home Group Oscar Pranata sama dengan baseline
11. Baca jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
12. Verifikasi jumlah entri sama dengan baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-295: Konfirmasi dialog gabungan

13. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata dan klik `Edit Home Group`
14. Klik node Accounts Payable lalu klik `[Select]`
15. Klik `[Remove]`
16. Verifikasi toast "Success, home group has been updated." tampil (bukan toast T-06)
17. Verifikasi Home Group Oscar Pranata berubah menjadi Accounts Payable
18. Buka Detail Oscar Pranata > Tab Role
19. Verifikasi banner Group Manager Oscar Pranata hanya memuat grup yang masih dikelola
20. Buka Tab Changelog Oscar Pranata
21. Verifikasi entri `Edit Home Group` tercatat
22. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — IT Infrastructure` / Old Value `Assigned` / New Value `—` tercatat
23. Baca jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
24. Verifikasi jumlah entri `Edit Home Group` dan `Auto-Revert` bertambah masing-masing 1 dibanding baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
25. Ganti akun: Logout lalu login sebagai Oscar Pranata
26. Buka panel notifikasi
27. Verifikasi Oscar Pranata menerima notifikasi in-app view-only (jumlah notifikasi Auto-Revert bertambah 1 dibanding baseline)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-296 (Cancel) diletakkan sebelum TC-FA-SU-295 (Remove) karena TC-FA-SU-296 mensyaratkan Oscar Pranata belum berubah; TC-FA-SU-295 menulis ulang "Ulangi perubahan hingga dialog tampil" (S-04).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan membuka Tab Changelog atau panel notifikasi. Satu entri yang diamati pada tiga surface ditulis satu `Verifikasi` selisih jumlah (S-01). TC-FA-SU-296 "tidak ada entri log" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan kelas g.
- Temuan untuk QA (S-15): (1) Home Group awal Oscar Pranata tidak tertulis di Pre-setup TC; spec membandingkan dengan nilai yang dicatat pada baseline. (2) Expected b TC-FA-SU-294 ("satu klik `[Remove]` menyimpan keduanya") diamati pada TC-FA-SU-295. (3) Post Condition TC-FA-SU-295 butir a dan b diamati pada Expected; Post Condition TC-FA-SU-296 butir lain tanpa observasi tidak diasersi.
