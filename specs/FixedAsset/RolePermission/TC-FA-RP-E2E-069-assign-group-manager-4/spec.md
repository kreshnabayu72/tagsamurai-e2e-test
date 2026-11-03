---
id: TC-FA-RP-E2E-069-assign-group-manager-4
title: "Assign Group Manager (4/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-232
  - TC-FA-RP-233
coverage:
  web: automated
---

# Assign Group Manager (4/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager (`IT Infrastructure`) (Pre-setup #5, Fajar Nugroho), email `groupManager_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Budi Santoso dan kolam pengguna Standard), #18 (pohon group), #33 (Seed Manage user & role Group: Gita Maharani di `IT Infrastructure`), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #39 (Detail Role Group Role `Manage files` terisi, termasuk Ahmad Fauzi dan Dimas Pranata di `Data Center`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-232: Group Manager mengelola Group Role pada descendant empat level (Rack A1) tanpa baris per descendant

1. Klik Tab `System`
2. Buka Detail Role `Manage files`
3. Klik node `Rack A1`
4. Klik `[+ Assign]`
5. Buka field Group
6. Verifikasi node `Rack A1` dapat dipilih pada field Group
7. Centang Budi Santoso lalu klik `[Assign]`
8. Verifikasi muncul toast sukses: `Success, Manage files has been assigned.`
9. Verifikasi baris Budi Santoso tampil pada node `Rack A1`
10. Klik node `Data Center` lalu amati tabel
11. Verifikasi sedikitnya satu baris lain tampil pada node `Data Center`
12. Verifikasi baris Budi Santoso tidak tampil pada node `Data Center` (tidak digandakan ke node lain)

### TC-FA-RP-233: Group Manager tidak dapat menugaskan Group Manager lain, termasuk pada descendant group-nya

13. Klik Tab `Group Manager`
14. Klik node `Data Center` di Sidebar Group Tree
15. Amati toolbar Tab Group Manager dan kolom aksi baris Kevin Susanto
16. Verifikasi `[+ Assign]` Hidden sehingga tidak ada jalur menugaskan Group Manager dari UI
17. Verifikasi aksi `Remove` pada baris Kevin Susanto Hidden

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 17 langkah.
- Langkah penghubung (S-03): langkah 1, 13. Akun aktor pertama sudah login di hook `before` (S-07).
- Penyimpangan kecil TC-FA-RP-232: baris Budi Santoso diverifikasi pada node `Rack A1` sebelum berpindah ke node `Data Center` agar asersi "hanya tampil pada node `Rack A1`" punya pembanding; Expected c TC dipecah menjadi dua `Verifikasi` (tampil di `Rack A1`, tidak tampil di `Data Center`).
- Absence baris pada node `Data Center` didahului `Verifikasi` baris lain pada tabel yang sama (butir 8b.2); asersi `Hidden` pada TC-FA-RP-233 memakai halaman yang sudah termuat sebagai anchor permukaan (butir 8b.2 untuk elemen UI).
- Temuan untuk QA:
  - TC-FA-RP-233 Expected c ("tidak ada jalur menugaskan Group Manager dari UI") adalah kesimpulan dari Expected a dan b dan tidak teramati terpisah; digabung ke satu `Verifikasi` dengan `[+ Assign]` Hidden (S-03).
  - TC-FA-RP-233 Expected b menyebut aksi `Remove` pada baris Hidden tanpa menyebut baris target; spec memakai baris Kevin Susanto (Group Manager di `Data Center`, Pre-setup #43).
  - TC-FA-RP-232 dan 233 memakai Group Manager (Fajar Nugroho) sebagai aktor; TC-FA-RP-232 precondition b menyebut Tab System, TC-FA-RP-233 menyebut Tab Group Manager; langkah klik tab adalah langkah penghubung.
