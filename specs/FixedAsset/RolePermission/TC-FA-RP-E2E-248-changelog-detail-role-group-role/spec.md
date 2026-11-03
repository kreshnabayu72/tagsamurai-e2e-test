---
id: TC-FA-RP-E2E-248-changelog-detail-role-group-role
title: "Changelog Detail Role Group Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-815
  - TC-FA-RP-816
  - TC-FA-RP-817
  - TC-FA-RP-818
  - TC-FA-RP-819
coverage:
  web: automated
---

# Changelog Detail Role Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager (Fajar Nugroho, Pre-setup #5) `groupManager_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_GM_PASSWORD`. Akun aktor kedua: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Pergantian ke Total Control memakai langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #5 (Group Manager Fajar Nugroho di `IT Infrastructure`), #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group), #24 (`Company Changelog`), #39 (Detail Role Group Role `Manage files` terisi: Budi Santoso di `Helpdesk`, Ahmad Fauzi dan Dimas Pranata di `Data Center`). Precondition TC-FA-RP-817: Ahmad Fauzi memegang Group Role `Manage group` di `Data Center` dengan Read aktif, Create dan Update tidak aktif (dipakai sebagai precondition TC, disiapkan lewat seeding API di hook `before`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: Subgroup `Server Room {runId}-248` (dibuat TC-FA-RP-819 oleh Fajar Nugroho; suffix memuat nomor spec; tetap ada sampai akhir sesi pengujian, Tabel Data Uji Dinamis #1).
- Kemampuan teknis: Membaca modal Changelog Detail Role lewat UI; waktu aksi dicatat sesudah aksi pemicu. Penghapusan group `Helpdesk` lewat UI Settings > Groups dan pemulihannya lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Penugasan Group Role Budi Santoso (dicabut di `Helpdesk` pada TC-FA-RP-816 dan dipulihkan lewat seeding API sebelum TC-FA-RP-818 menghapus group itu), Create dan Update baris Ahmad Fauzi pada `Manage group`, group `Helpdesk`, dan Subgroup `Server Room {runId}-248` diubah atau dibuat spec ini; Pre-setup dipulihkan ke keadaan awal di hook `after`, Subgroup dibersihkan di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-819: Changelog Detail Role Group Role: Creator Auto-Assign satu entri Assign tanpa Edit CRUD

1. Buka Settings > Groups
2. Buat Subgroup `Server Room {runId}-248` di bawah `IT Infrastructure` di Settings > Groups, catat waktu sesudah pembuatan, lalu tunggu aksi selesai
3. Ganti akun: logout lalu login sebagai Total Control (Siti Rahmawati, `Spectra.env.FA_TC_PASSWORD`)
4. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage group`
5. Klik ikon Changelog di toolbar Detail Role
6. Verifikasi Modal memuat tepat satu entri terbaru untuk Subgroup `Server Room {runId}-248`: Action `Assign`; Object `Manage group — Fajar Nugroho — Server Room {runId}-248`; Field `Access`; Old Value `—`; New Value `Assigned`; Modified By `Fajar N`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Verifikasi Modal tidak memuat entri Edit CRUD terpisah untuk Subgroup `Server Room {runId}-248`

### TC-FA-RP-815: Changelog Detail Role Group Role: Assign dengan segmen group pada Object

8. Tutup modal Changelog lalu klik segmen `System` pada Breadcrumb
9. Buka Detail Role `Manage files`
10. Pilih node `Data Center`
11. Klik `[+ Assign]`
12. Centang Budi Santoso lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
13. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
14. Klik ikon Changelog di toolbar Detail Role
15. Verifikasi Modal memuat entri terbaru: Action `Assign`; Role Name — User — Group Name `Manage files — Budi Santoso — Data Center`; Field `Access`; Old Value `—`; New Value `Assigned`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)

### TC-FA-RP-816: Changelog Detail Role Group Role: Remove

16. Tutup modal Changelog
17. Klik `All Groups`
18. Klik `[⋯]` baris Budi Santoso di `Helpdesk` lalu `Remove`
19. Klik `[Remove]`, catat waktu sesudah `[Remove]`
20. Tunggu aksi selesai: dialog Remove tertutup dan baris pengguna tidak lagi tampil di tabel
21. Klik ikon Changelog di toolbar Detail Role
22. Verifikasi Modal memuat entri terbaru: Action `Remove`; Role Name — User — Group Name `Manage files — Budi Santoso — Helpdesk`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)

### TC-FA-RP-817: Changelog Detail Role Group Role: Edit CRUD satu entri per bidang

23. Tutup modal Changelog lalu klik segmen `System` pada Breadcrumb
24. Buka Detail Role `Manage group`
25. Klik `All Groups`
26. Centang Create pada baris Ahmad Fauzi di `Data Center`, catat waktu sesudahnya
27. Centang Update pada baris Ahmad Fauzi di `Data Center`, catat waktu sesudahnya
28. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
29. Klik ikon Changelog di toolbar Detail Role
30. Verifikasi Modal memuat entri teratas (terbaru, Date Newest First default): Action `Edit`; Role Name — User — Group Name `Manage group — Ahmad Fauzi — Data Center`; Field `Update`; Old Value `Inactive`; New Value `Active`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
31. Verifikasi entri di bawahnya (lebih lama): Action `Edit`; Role Name — User — Group Name `Manage group — Ahmad Fauzi — Data Center`; Field `Create`; Old Value `Inactive`; New Value `Active`; Modified By `Siti R`

### TC-FA-RP-818: Changelog Detail Role Group Role: Remove (Group Deleted)

32. Pulihkan penugasan Budi Santoso di `Helpdesk` lewat seeding API, hingga tersimpan
33. Tutup modal Changelog lalu buka Settings > Groups
34. Hapus group `Helpdesk` (konfirmasi dialog `Delete Group`), catat waktu sesudah konfirmasi, lalu tunggu aksi selesai
35. Buka Fixed Asset > Settings > Role & Permission, klik Tab `System`, lalu buka Detail Role `Manage files`
36. Klik ikon Changelog di toolbar Detail Role
37. Verifikasi Modal memuat entri terbaru: Action `Remove (Group Deleted)`; Role Name — User — Group Name `Manage files — Budi Santoso — Helpdesk`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
38. Pulihkan group `Helpdesk` lewat seeding API, hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 38 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 8, 13, 16, 20, 23, 28, 33, 35. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 32, 38; tidak ada `Verifikasi`.
- Langkah 32 (pemulihan penugasan Budi Santoso di `Helpdesk`, S-09) adalah langkah penghubung antar blok TC: TC-FA-RP-816 mencabut baris itu dan TC-FA-RP-818 mengharapkan entri `Remove (Group Deleted)` untuk baris yang sama, sehingga baris harus ada sebelum group dihapus (opsi memindahkan blok TC-FA-RP-818 ke depan tidak dipilih agar urutan TC tetap).
- Urutan TC: TC-FA-RP-819, 815, 816, 817, 818 (TC-FA-RP-819 lebih dulu) supaya akun pertama di hook `before` adalah Group Manager (pembuat Subgroup) dan hanya satu langkah ganti akun yang dibutuhkan: TC-FA-RP-819 membutuhkan Group Manager untuk membuat Subgroup lalu Total Control untuk membaca Changelog, sedangkan TC lain memakai Total Control.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Subgroup `Server Room {runId}-248` memakai suffix bernomor spec (bagian 5); `Server Room {n}` pada TC adalah Data Dinamis Pre-setup (Tabel Dinamis #1) yang Lifecycle-nya tetap ada sampai akhir sesi.
- TC-FA-RP-815: modal `Changelog` dibuka dari Detail Role `Manage files` pada node `Data Center`; TC-FA-RP-816 melanjutkan Detail Role yang sama setelah klik `All Groups`.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Spec ini memuat lebih dari 35 langkah (di atas smell): kelima blok satu kelas (Changelog Detail Role Group Role), memakai Detail Role dan dataset Pre-setup yang sama, dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan prasyarat); langkah tambahan hanya langkah penghubung "Tunggu aksi selesai" sebelum pembukaan Modal Changelog (butir 8b.8).
- Temuan untuk QA:
  - TC-FA-RP-819 langkah 2 menyebut "Login sbg Role: Total Control" tanpa menyebut logout; spec menulis langkah ganti akun eksplisit (S-07).
  - TC-FA-RP-819 Expected memuat kata "entri terbaru" dan "tepat satu entri" yang bertentangan dalam satu kalimat; spec mengasersi satu entri Assign dan tidak adanya entri Edit CRUD terpisah untuk Subgroup itu.
  - TC-FA-RP-817 precondition d meminta Create dan Update belum aktif lewat seed API; Pre-setup #39 tidak memuat `Manage group` untuk Ahmad Fauzi.
