---
id: TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1
title: "Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-858
  - TC-FA-RP-859
  - TC-FA-RP-860
  - TC-FA-RP-862
coverage:
  web: automated
---

# Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (1/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard; target: Ahmad Fauzi, tanpa tingkat akses; memegang Global Role `Manage accounting` dengan Create nonaktif untuk TC-FA-RP-862) dan #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi; Ahmad Fauzi hanya memegang Group Role `Manage files` Read di `Data Center`). Siti Rahmawati (#2) adalah aktor, sehingga Modified By diasersi `Siti R`.
- Baseline audit trail (S-12): jumlah entri Changelog, System Log, dan Activity Log dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (UI atau fixture BE); asersi memakai selisih terhadap baseline, bukan angka absolut dan bukan posisi teratas.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-858, TC-FA-RP-859, dan TC-FA-RP-860: aksi Assign Total Control ke Ahmad Fauzi (precondition dan aksi sama)

1. Catat baseline (aksi tanpa `Verifikasi`; buka tiap surface, catat, lalu lanjut):
   - Settings > User > Detail Ahmad Fauzi > Changelog: User: jumlah entri (baseline aggregate)
   - Changelog: User > Global Role: jumlah entri Action `Assign (via Total Control)` (baseline Global Role)
   - Changelog: User > Group Role: jumlah entri, dan jumlah entri Action `Edit` untuk `Manage files — Data Center` (baseline Group Role)
   - Settings > User > Detail Siti Rahmawati > Tab System Log: jumlah entri Action `Assign (via Total Control)` (baseline System Log)
   - Activity Log FAMS (menu Activity Log): jumlah entri Action `Assign (via Total Control)` (baseline Activity Log)
2. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control
3. Klik `[+ Assign]` di Tab Total Control
4. Centang Ahmad Fauzi lalu klik `[Assign]`
5. Tunggu aksi selesai: popup tertutup

### TC-FA-RP-858: Assign Total Control menulis satu entri Access Level ke Changelog: User, aggregate tetap satu baris

6. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User
7. Verifikasi selisih jumlah entri terhadap baseline aggregate adalah tepat satu entri baru dengan Field `Access Level` `—` ke `Total Control`
8. Verifikasi aggregate tidak menampilkan baris cascade per role (tidak ada entri baru Action `Assign (via Total Control)`)

### TC-FA-RP-859: Cascade Assign Total Control tampil di Changelog: User > Global Role per role yang berubah

9. Buka Changelog: User > Global Role
10. Verifikasi entri baru `Assign (via Total Control)` dengan Field `Access` `—` ke `Assigned` tampil untuk tiap Global Role yang baru diaktifkan (selisih terhadap baseline Global Role)
11. Verifikasi kolom Modified By entri cascade tersebut `Siti R`
12. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
13. Verifikasi entri System Log aktor tampil (sedikitnya satu entri)
14. Verifikasi jumlah entri Action `Assign (via Total Control)` pada System Log sama dengan baseline System Log (entri cascade tidak muncul)
15. Buka Activity Log FAMS (menu Activity Log)
16. Verifikasi entri Activity Log tampil (sedikitnya satu entri)
17. Verifikasi jumlah entri Action `Assign (via Total Control)` pada Activity Log sama dengan baseline Activity Log (entri cascade tidak muncul)

### TC-FA-RP-860: Cascade Assign Total Control menulis baris pola Group Role semua group: entri Assign (via Total Control) untuk baris baru dan Edit per kolom yang berubah untuk baris aktif

18. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User > Group Role
19. Verifikasi modal Changelog: User > Group Role tampil
20. Verifikasi entri Action `Assign (via Total Control)` tampil per baris baru (Role × Group yang sebelumnya tidak dimiliki) dengan Field `[Role Name] — [Group Name]`, Old Value `—`, New Value `Assigned`, Modified By `Siti R`
21. Verifikasi entri baru Action `Edit` Field `Delete` Old Value `Inactive` New Value `Active` tampil untuk `Manage files — Data Center`, dan jumlah entri Action `Edit` untuk `Manage files — Data Center` bertambah tepat 1 dari baseline Group Role sehingga kolom Read yang sudah aktif tidak mendapat entri `Edit`
22. Buka Tab System > Detail Role Group Role `Manage files`, klik `All Groups`, lalu klik ikon Changelog di toolbar Detail Role
23. Verifikasi entri yang sama tampil per Group (satu entri per baris, bukan satu entri ringkasan)

### TC-FA-RP-862: Edit CRUD menulis ke Changelog Detail Role dan Changelog: User > Global Role

24. Pulihkan Ahmad Fauzi ke state Precondition (tanpa tingkat akses; baris `Manage accounting` dengan Create nonaktif) lewat seeding API hingga tersimpan
25. Catat baseline (aksi tanpa `Verifikasi`):
   - Detail Role `Manage accounting` > ikon Changelog di toolbar Detail Role: jumlah entri Action `Edit` Field `Create` untuk Ahmad Fauzi
   - Settings > User > Detail Ahmad Fauzi > Changelog: User > Global Role: jumlah entri Action `Edit` Field `Create` untuk `Manage accounting`
26. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting`
27. Centang Create pada baris Ahmad Fauzi
28. Tunggu aksi selesai: perubahan Create tersimpan
29. Klik ikon Changelog di toolbar Detail Role
30. Verifikasi entri baru Action `Edit` Field `Create` `Inactive` ke `Active` untuk `Manage accounting` tercatat di Changelog Detail Role (selisih terhadap baseline)
31. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User > Global Role
32. Verifikasi entri baru Action `Edit` Field `Create` `Inactive` ke `Active` untuk `Manage accounting` tercatat di Changelog: User > Global Role (selisih terhadap baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah.
- TC-FA-RP-858, 859, dan 860 punya precondition dan aksi yang sama (Assign Total Control ke Ahmad Fauzi); aksi dijalankan satu kali pada langkah 4 dan tiap TC mengasersi surface masing-masing tanpa state yang berubah di antaranya. Urutan TC mengikuti TC sumber.
- Langkah penghubung (S-03): pencatatan baseline (langkah 1), pembukaan Tab Total Control, dan "Tunggu aksi selesai". Akun aktor pertama sudah login di hook `before` (S-07).
- Asersi "entri cascade tidak muncul" pada System Log dan Activity Log (TC-FA-RP-859) ditulis sebagai kesamaan jumlah terhadap baseline pada aksi Assign yang sukses; entri Group Role (TC-FA-RP-860) diasersi sebagai entri yang tampil, dengan selisih tepat 1 untuk `Edit` baris aktif, dengan Verifikasi entri tampil sebagai anchor (bagian 3 prinsip 13 butir g: asersi jumlah dengan baseline boleh berada di spec fungsional); bukan kelas absence.
- TC-FA-RP-862 mengasersi entri pada dua surface (Changelog Detail Role dan Changelog: User > Global Role) karena judul TC menyebut keduanya; Expected hanya satu kalimat.
- Temuan untuk QA:
  - TC-FA-RP-859 Expected menyebut "tiap Global Role yang baru diaktifkan" tanpa daftar role; Pre-setup #15 tidak merinci Global Role Ahmad Fauzi. Spec tidak menghitung jumlah entri cascade dan hanya mengasersi bentuk entri.
  - Precondition TC-FA-RP-858 sampai 860 hanya menyebut Pre-setup #15 (TC-FA-RP-860 juga #39); kondisi "Ahmad Fauzi belum memiliki tingkat akses" diambil dari definisi #15 (tanpa tingkat akses).
  - Post Condition TC-FA-RP-858 sampai 860 kosong; tidak ada yang diasersi.
  - TC-FA-RP-862 Expected hanya menyebut "entri Edit ... tercatat" tanpa menyebut surface; spec mengikuti judul TC (dua surface). Baris Ahmad Fauzi pada `Manage accounting` dengan Create nonaktif (Pre-setup #39) di-seed lewat seeding API. TC-FA-RP-862 tanpa Post Condition.
