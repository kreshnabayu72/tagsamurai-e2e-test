---
id: TC-FA-SU-E2E-089-popup-select-home-group-singular-screening-tombol-select-dan-cancel
title: "Popup Select Home Group Singular: Screening, Tombol Select, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-281
  - TC-FA-SU-287
  - TC-FA-SU-289
coverage:
  web: automated
---

# Popup Select Home Group Singular: Screening, Tombol Select, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan pohon grup (#21). Pengguna target: Gita Permata (Home Group Finance & Accounting) dan Hana Kusuma (Home Group General Affairs). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Spec ini mengosongkan Home Group Hana Kusuma (langkah 29); pemulihan ke General Affairs lewat seed API pada langkah 33 dan di hook `after`. Efek pada Pre-setup: Last Updated dan Modified By Hana Kusuma berubah dan satu entri log permanen `Edit Home Group` bertambah; Home Group Gita Permata tidak diubah.

## Test Steps

### TC-FA-SU-281: Screening popup Select Home Group singular

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
2. Ketik Search `Gita Permata`, tekan Enter
3. Klik ⋯ pada baris Gita Permata
4. Klik `Edit Home Group`
5. Verifikasi header `Select Home Group` dengan close `[✕]` tampil
6. Verifikasi kolom pencarian dengan placeholder `Search groups...` tampil
7. Verifikasi pohon grup berbentuk single-select tanpa radio atau checkbox per node
8. Verifikasi Home Group saat ini (Finance & Accounting) ter-highlight (background dan teks bold/primary)
9. Verifikasi footer menampilkan `[Cancel]` (Text, Contrast) dan `[Select]`
10. Verifikasi popup tidak memuat field lain
11. Verifikasi popup tidak memuat daftar nama pengguna terdampak

### TC-FA-SU-287: Tombol Select singular Disabled sampai pilihan berbeda

12. Verifikasi `[Select]` Disabled saat popup dibuka dengan Home Group saat ini ter-highlight
13. Klik node IT Infrastructure
14. Verifikasi `[Select]` Enabled
15. Klik node Finance & Accounting
16. Verifikasi `[Select]` Disabled

### TC-FA-SU-289: Cancel popup Select Home Group

17. Klik node IT Infrastructure
18. Klik `[Cancel]`
19. Verifikasi popup tertutup
20. Verifikasi tidak ada toast
21. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
22. Klik `[✕]`
23. Verifikasi popup tertutup
24. Verifikasi tidak ada toast
25. Verifikasi kolom Home Group baris Gita Permata tetap Finance & Accounting
26. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
27. Verifikasi jumlah entri `Edit Home Group` sama dengan baseline pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-287: Pengguna tanpa Home Group

28. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
29. Klik ⋯ pada baris Hana Kusuma, klik `Edit Home Group`, klik ulang node General Affairs yang ter-highlight, lalu klik `[Select]`
30. Klik ⋯ pada baris Hana Kusuma lalu klik `Edit Home Group`
31. Verifikasi `[Select]` Disabled pada pengguna tanpa Home Group sampai node dipilih
32. Klik `[Cancel]`
33. Pulihkan Home Group Hana Kusuma ke General Affairs lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-287 langkah 1 sampai 3 memakai popup yang masih terbuka dari TC-FA-SU-281 (tanpa pembukaan ulang), lalu TC-FA-SU-289, dan bagian pengguna tanpa Home Group TC-FA-SU-287 (langkah 4) diletakkan terakhir karena mengubah data.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline) dan langkah 33 (pemulihan).
- Langkah penghubung Search (R-16, bagian 8b butir 9 dan 13): langkah 2 mencari Gita Permata dan langkah 28 mengganti isi kotak search dengan Hana Kusuma sebelum membuka menu ⋯ baris target, karena User List memuat 3 halaman.
- TC-FA-SU-289 mensyaratkan "tidak ada entri log": ditulis sebagai asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g.
- Temuan untuk QA (S-15): (1) TC-FA-SU-287 langkah 4 menyebut "Edit Home Group tanpa memilih node" untuk mengosongkan Home Group, sedangkan cara mengosongkan pada TC-FA-SU-288 adalah klik ulang node terpilih lalu `[Select]`; spec mengikuti cara TC-FA-SU-288. (2) Post Condition TC-FA-SU-289 "penugasan target tidak berubah" tidak punya langkah observasi dan tidak diasersi.
