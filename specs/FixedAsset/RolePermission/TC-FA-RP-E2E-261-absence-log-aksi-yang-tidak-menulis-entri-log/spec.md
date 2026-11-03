---
id: TC-FA-RP-E2E-261-absence-log-aksi-yang-tidak-menulis-entri-log
title: "Absence log: aksi yang tidak menulis entri log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-867
  - TC-FA-RP-868
  - TC-FA-RP-873
coverage:
  web: automated
---

# Absence log: aksi yang tidak menulis entri log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso sebagai Standard tanpa tingkat akses; Ahmad Fauzi dan Budi Santoso memegang Global Role `Manage accounting` dengan Create nonaktif untuk TC-FA-RP-868 dan 873), #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi), dan #24 (Company Changelog; tidak dibutuhkan karena asersi memakai baseline jumlah entri).
- Kemampuan teknis: sesi API aktor (`suite.md`) sebagai pelaku kedua yang hanya memicu perubahan state (menghapus identitas Budi Santoso pada TC-FA-RP-867 dan mencentang Create pada TC-FA-RP-868, masing-masing hingga tersimpan); intercept parsial atas request simpan perubahan CRUD untuk memaksa respons 5xx pada TC-FA-RP-873 (endpoint tidak disebut karena tidak ada di TC; intercept dilepas segera sesudah pemicu); kemampuan membaca jumlah entri audit trail sebelum aksi (baseline, S-12) disediakan tim FE/BE.
- State global: tidak ada yang diubah selain data pengguna Pre-setup #15, dipulihkan lewat seeding API di hook `after`.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-867: Submit Assign atomik yang ditolak tidak menulis entri log apa pun

1. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri pada Changelog Tab Total Control, pada System Log aktor (Settings > User > Detail Siti Rahmawati > Tab System Log), dan pada Activity Log FAMS (menu Activity Log)
2. Klik `[+ Assign]` di Tab Total Control
3. Centang Ahmad Fauzi dan Budi Santoso
4. Hapus identitas Budi Santoso lewat sesi API aktor hingga terhapus tersimpan
5. Klik `[Assign]` sehingga submit ditolak `V-08`
6. Tunggu aksi selesai: respons penolakan diterima
7. Tutup popup lewat `✕`
8. Klik ikon Changelog di toolbar Tab Total Control
9. Verifikasi modal Changelog Tab Total Control tampil dengan jumlah entri yang terbaca
10. Verifikasi jumlah entri Changelog Tab Total Control sama dengan baseline (tidak ada entri baru)
11. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
12. Verifikasi System Log aktor tampil dengan jumlah entri yang terbaca
13. Verifikasi jumlah entri System Log sama dengan baseline (tidak ada entri baru)
14. Buka Activity Log FAMS (menu Activity Log)
15. Verifikasi Activity Log tampil dengan jumlah entri yang terbaca
16. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-RP-868: Edit No-Op tidak menulis entri di surface mana pun

17. Pulihkan Budi Santoso lewat seeding API (identitas dan penugasan `Manage accounting`), lalu catat baseline (aksi tanpa `Verifikasi`): jumlah entri Action `Edit` Field `Create` untuk Ahmad Fauzi pada Changelog Detail Role `Manage accounting`, pada System Log aktor, dan pada Activity Log FAMS
18. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting` (halaman Sesi 2 dimuat sebelum Sesi 1 mengubah data)
19. Sesi 1 (sesi API aktor) mencentang Create pada baris Ahmad Fauzi hingga tersimpan
20. Sesi 2 (halaman yang belum disegarkan) mencentang Create pada baris Ahmad Fauzi yang sama dan menerima toast netral
21. Tunggu aksi selesai: respons Sesi 2 diterima
22. Klik ikon Changelog di toolbar Detail Role
23. Verifikasi Changelog Detail Role memuat tepat satu entri baru Action `Edit` Field `Create` untuk Ahmad Fauzi (dari Sesi 1; selisih satu terhadap baseline)
24. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
25. Verifikasi System Log aktor tampil dengan jumlah entri yang terbaca
26. Verifikasi selisih jumlah entri Action `Edit` pada System Log terhadap baseline tepat satu (tidak ada entri tambahan dari Sesi 2)
27. Buka Activity Log FAMS (menu Activity Log)
28. Verifikasi Activity Log tampil dengan jumlah entri yang terbaca
29. Verifikasi selisih jumlah entri Action `Edit` pada Activity Log terhadap baseline tepat satu (tidak ada entri tambahan dari Sesi 2)

### TC-FA-RP-873: Aksi yang gagal 5xx tidak menulis entri log

30. Pulihkan baris Ahmad Fauzi pada `Manage accounting` ke Create nonaktif lewat seeding API hingga tersimpan, lalu buka Tab System dan Detail Role `Manage accounting`
31. Catat baseline (aksi tanpa `Verifikasi`): klik ikon Changelog di toolbar Detail Role, catat jumlah entri Action `Edit` Field `Create` untuk Ahmad Fauzi, lalu tutup modal
32. Blokir respons simpan perubahan CRUD dengan status 5xx (intercept parsial)
33. Centang Create pada baris Ahmad Fauzi
34. Tunggu aksi selesai: respons 5xx diterima
35. Lepas intercept 5xx
36. Klik ikon Changelog di toolbar Detail Role
37. Verifikasi modal Changelog Detail Role tampil dengan jumlah entri yang terbaca
38. Verifikasi jumlah entri Action `Edit` Field `Create` untuk Ahmad Fauzi sama dengan baseline (tidak ada entri baru untuk aksi yang gagal)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 38 langkah.
- Spec absence (kelas g): tiap blok punya aksi nyata dan baseline sendiri (S-12). Pemicu kelas lain (dua sesi pada TC-FA-RP-867 dan 868, kegagalan 5xx pada TC-FA-RP-873) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a). Pelaku kedua memakai sesi API aktor sehingga bukan konteks kedua kelas c.
- Anchor positif absence (bagian 8b butir 2): pada tiap surface, Verifikasi surface tampil dengan jumlah entri yang terbaca (jumlah awal yang dicatat) mendahului kesamaan jumlah; untuk TC-FA-RP-868 anchor tambahan adalah entri baru dari Sesi 1.
- Langkah penghubung (S-03): pencatatan baseline, pemulihan lewat seeding API, pembukaan halaman, penutupan popup (`✕`), dan "Tunggu aksi selesai". Akun aktor pertama sudah login di hook `before` (S-07).
- Urutan TC dan baris Pre-setup: TC-FA-RP-867 pertama karena memakai Tab Total Control yang dibuka hook `beforeEach`; TC-FA-RP-868 lalu 873 memakai baris yang sama sehingga 873 didahului pemulihan baris Ahmad Fauzi.
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama, tiap blok punya baseline dan pemicu sendiri dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - TC-FA-RP-867 tidak menyebut copy penolakan `V-08` maupun perilaku popup sesudah penolakan (tetap terbuka atau tertutup); spec tidak mengasersi keduanya dan menutup popup lewat `✕` sebagai langkah penghubung. TC-FA-RP-867 dan 868 berlabel `Manual Only — (d) dua sesi paralel`; spec memerankan Sesi 1 TC-FA-RP-868 lewat sesi API aktor dan Sesi 2 lewat UI yang belum disegarkan.
  - TC-FA-RP-868 menyebut "toast netral" tanpa teksnya; spec tidak mengasersi toast itu. Baris Ahmad Fauzi pada `Manage accounting` (Pre-setup #39) di-seed lewat seeding API.
  - Precondition TC-FA-RP-867, 868, dan 873 merujuk Pre-setup #24 (Company Changelog); spec berjalan di Company Alpha dengan baseline sehingga #24 tidak dibutuhkan. Post Condition ketiga TC kosong.
