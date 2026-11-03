---
id: TC-FA-RP-E2E-245-changelog-detail-role-global-role-1
title: "Changelog Detail Role Global Role (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-806
  - TC-FA-RP-807
  - TC-FA-RP-808
  - TC-FA-RP-809
  - TC-FA-RP-810
coverage:
  web: automated
---

# Changelog Detail Role Global Role (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #24 (`Company Changelog`), #39 (Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi, termasuk baris Ahmad Fauzi). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog Detail Role lewat UI; waktu aksi dicatat sesudah aksi pemicu. Precondition TC-FA-RP-807 (Budi Santoso memegang `Manage Open API`) dipenuhi oleh hasil TC-FA-RP-806; Delete aktif pada baris Ahmad Fauzi di `Manage accounting` (TC-FA-RP-810) dan Create, Update tidak aktif (TC-FA-RP-808, 809) disiapkan lewat seeding API.
- State yang diubah dan pemulihannya: Penugasan Budi Santoso pada `Manage Open API` serta Create, Update, dan Delete baris Ahmad Fauzi diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-806: Changelog Detail Role Global Role: Assign

1. Klik Tab `System` lalu buka Detail Role `Manage Open API`
2. Klik `[+ Assign]`
3. Centang Budi Santoso lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
4. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
5. Klik ikon Changelog di toolbar Detail Role
6. Verifikasi Modal `Changelog: Role & Permission > Manage Open API` memuat entri terbaru: Action `Assign`; Role Name — User `Manage Open API — Budi Santoso`; Field `Access`; Old Value `—`; New Value `Assigned`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog

### TC-FA-RP-807: Changelog Detail Role Global Role: Remove

8. Klik `[⋯]` baris Budi Santoso lalu `Remove`
9. Klik `[Remove]`, catat waktu sesudah `[Remove]`
10. Tunggu aksi selesai: dialog Remove tertutup dan baris pengguna tidak lagi tampil di tabel
11. Klik ikon Changelog di toolbar Detail Role
12. Verifikasi Modal memuat entri terbaru: Action `Remove`; Role Name — User `Manage Open API — Budi Santoso`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
13. Tutup modal Changelog

### TC-FA-RP-808: Changelog Detail Role Global Role: Edit Create

14. Klik segmen `System` pada Breadcrumb lalu buka Detail Role `Manage accounting`
15. Centang Create pada baris Ahmad Fauzi, catat waktu sesudahnya
16. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
17. Klik ikon Changelog di toolbar Detail Role
18. Verifikasi Modal memuat entri terbaru: Action `Edit`; Role Name — User `Manage accounting — Ahmad Fauzi`; Field `Create`; Old Value `Inactive`; New Value `Active`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
19. Tutup modal Changelog

### TC-FA-RP-809: Changelog Detail Role Global Role: Edit Update

20. Klik segmen `System` pada Breadcrumb lalu buka Detail Role `Manage Open API`
21. Centang Update pada baris Ahmad Fauzi, catat waktu sesudahnya
22. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
23. Klik ikon Changelog di toolbar Detail Role
24. Verifikasi Modal memuat entri terbaru: Action `Edit`; Role Name — User `Manage Open API — Ahmad Fauzi`; Field `Update`; Old Value `Inactive`; New Value `Active`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
25. Tutup modal Changelog

### TC-FA-RP-810: Changelog Detail Role Global Role: Edit Delete

26. Klik segmen `System` pada Breadcrumb lalu buka Detail Role `Manage accounting`
27. Hapus centang Delete pada baris Ahmad Fauzi, catat waktu sesudahnya
28. Tunggu aksi selesai: kotak centang tetap pada kondisi baru dan indikator memuat pada baris hilang
29. Klik ikon Changelog di toolbar Detail Role
30. Verifikasi Modal memuat entri terbaru: Action `Edit`; Role Name — User `Manage accounting — Ahmad Fauzi`; Field `Delete`; Old Value `Active`; New Value `Inactive`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
31. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 7, 10, 13, 14, 16, 19, 20, 22, 25, 26, 28, 31. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Modal `Changelog: Role & Permission > Manage Open API` pada TC-FA-RP-806 dibuka dari Detail Role yang sama untuk TC-FA-RP-807; judul modal untuk blok `Manage accounting` tidak disebut TC sehingga tidak diasersi.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-806 menyebut judul modal `Changelog: Role & Permission > Manage Open API`, sedangkan TC-FA-RP-807 sampai 810 tidak menyebut judul modal.
