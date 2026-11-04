---
id: TC-FA-RP-E2E-316-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-5
title: "Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-872
  - TC-FA-RP-1140
coverage:
  web: automated
---

# Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (5/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, tanpa tingkat akses; TC-FA-RP-872), #12 (Maya Anggraeni: Read Only, seluruh Global Role hanya Read, baris pola Group Role Read saja pada setiap group termasuk `Manage files` di `Data Center`; TC-FA-RP-1140), dan #24 (Company Changelog; tidak dibutuhkan karena asersi memakai selisih baseline).
- Baseline audit trail (S-12): jumlah entri Changelog, System Log, dan Activity Log dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (UI atau fixture BE); asersi memakai selisih terhadap baseline, bukan angka absolut dan bukan posisi teratas.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Pemulihan di hook `after`: nama Ahmad Fauzi dikembalikan dari `Ahmad Fauzi Rahman` dan Maya Anggraeni dikembalikan sebagai Read Only (aturan pemulihan fixture destruktif pada Catatan TC).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-872: Entri log lama tetap memakai nama saat itu setelah user di-rename

1. Catat baseline (aksi tanpa `Verifikasi`): Detail Role `Manage Open API` > ikon Changelog di toolbar Detail Role, jumlah entri Action `Assign` untuk Ahmad Fauzi
2. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
3. Klik `[+ Assign]`, centang Ahmad Fauzi, klik `[Assign]` (entri log Assign dibuat)
4. Tunggu aksi selesai: popup tertutup
5. Ubah nama Ahmad Fauzi menjadi Ahmad Fauzi Rahman di Settings > User
6. Tunggu aksi selesai: perubahan nama tersimpan
7. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
8. Klik ikon Changelog di toolbar Detail Role
9. Verifikasi entri lama (Assign Ahmad Fauzi) tetap menampilkan `Manage Open API — Ahmad Fauzi` (snapshot)
10. Verifikasi entri lama tidak berubah menjadi nama baru (tidak menampilkan `Ahmad Fauzi Rahman`)

### TC-FA-RP-1140: Changelog upgrade Read Only ke Total Control: entri Edit per kolom C/U/D yang berubah (Global Role dan Group Role), tanpa Remove (via Read Only)

11. Catat baseline (aksi tanpa `Verifikasi`):
   - Detail Role `Manage Open API` > ikon Changelog: jumlah entri untuk Maya Anggraeni dengan Action `Edit` Field `Update`, Action `Remove (via Read Only)`, dan Action `Assign (via Total Control)`
   - Detail Role `Import data` > ikon Changelog: jumlah entri untuk Maya Anggraeni dengan Action `Edit` Field `Create`, Field `Read`, dan Action `Remove (via Read Only)`
   - Settings > User > Detail Maya Anggraeni > Tab Role sub-tab Global Role > ikon Changelog: jumlah entri Action `Edit` dan `Remove (via Read Only)`
   - Sub-tab Group Role > ikon Changelog: jumlah entri Action `Edit` (termasuk Field `Read`), Action `Remove (via Read Only)`, dan Action `Assign (via Total Control)`
12. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control
13. Klik `[+ Assign]` di Tab Total Control
14. Centang Maya Anggraeni lalu klik `[Assign]`
15. Tunggu aksi selesai: popup tertutup
16. Buka Tab System, lalu Detail Role `Manage Open API`
17. Klik ikon Changelog di toolbar Detail Role
18. Verifikasi entri baru Action `Edit`, Role Name — User `Manage Open API — Maya Anggraeni`, Field `Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti R` tampil
19. Verifikasi tidak ada entri baru Action `Remove (via Read Only)` maupun `Assign (via Total Control)` untuk Maya Anggraeni (jumlah sama dengan baseline)
20. Tutup modal, lalu buka Detail Role `Import data`
21. Klik ikon Changelog di toolbar Detail Role
22. Verifikasi entri baru Action `Edit`, Role Name — User `Import data — Maya Anggraeni`, Field `Create`, Old Value `Inactive`, New Value `Active`, Modified By `Siti R` tampil
23. Verifikasi kolom Read tidak mendapat entri `Edit` baru (jumlah entri Field `Read` sama dengan baseline)
24. Verifikasi tidak ada entri baru Action `Remove (via Read Only)` (jumlah sama dengan baseline)
25. Buka Settings > User > Detail Maya Anggraeni > Tab Role sub-tab Global Role, lalu klik ikon Changelog
26. Verifikasi modal Changelog: User > Global Role memuat entri `Edit` baru yang sama
27. Verifikasi modal Changelog: User > Global Role tidak memuat entri baru `Remove (via Read Only)` (jumlah sama dengan baseline)
28. Buka sub-tab Group Role, lalu klik ikon Changelog
29. Verifikasi modal Changelog: User > Group Role memuat entri baru Action `Edit` per kolom yang berubah pada tiap baris pola (mis. Field `Delete`, Old Value `Inactive`, New Value `Active` untuk `Manage files — Data Center`), Modified By `Siti R`
30. Verifikasi modal Changelog: User > Group Role: kolom yang sudah sama tidak mendapat entri `Edit` baru (jumlah entri Field `Read` sama dengan baseline)
31. Verifikasi modal Changelog: User > Group Role tidak memuat entri baru `Remove (via Read Only)` maupun `Assign (via Total Control)` (jumlah sama dengan baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab dan Detail Role, "Tunggu aksi selesai", dan pemulihan Maya Anggraeni lewat seeding API. Akun aktor pertama sudah login di hook `before` (S-07).
- Asersi "tidak ada entri `Remove (via Read Only)`" dan "tidak ada entri `Assign (via Total Control)`" ditulis sebagai kesamaan jumlah terhadap baseline pada aksi Assign yang sukses, dengan Verifikasi entri baru sebagai anchor (bagian 3 prinsip 13 butir g: asersi jumlah dengan baseline boleh berada di spec fungsional); bukan kelas absence.
- Temuan untuk QA:
  - TC-FA-RP-872 tidak merinci langkah UI rename Ahmad Fauzi di Settings > User; spec memakai langkah TC apa adanya. Nama Pre-setup #15 bersifat literal (nama pengguna Pre-setup tidak bersuffix; pada surface admin dan log pengguna diidentifikasi lewat nama karena asersi snapshot nama adalah objek uji). TC-FA-RP-872 merujuk Pre-setup #24 di Precondition; spec berjalan di Company Alpha dengan baseline selisih.
  - TC-FA-RP-1140 Expected d menyebut entri `Edit` per kolom yang berubah "pada tiap baris pola" hanya dengan contoh `Manage files — Data Center` (Field `Delete`); daftar Role × Group dan kolom lain tidak disebut, sehingga spec mengasersi entri `Edit` bentuk contoh itu dan tidak mengasersi jumlah entri.
  - TC-FA-RP-1140 Expected a menyebut Role Name — User untuk `Manage Open API` dan `Import data`; jumlah baris yang berubah pada role lain tidak disebut dan tidak diasersi. Post Condition TC-FA-RP-872 dan 1140 kosong; tidak ada yang diasersi.
