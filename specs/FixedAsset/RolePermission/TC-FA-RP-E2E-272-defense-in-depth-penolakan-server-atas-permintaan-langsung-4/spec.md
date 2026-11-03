---
id: TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4
title: "Defense-in-depth: penolakan server atas permintaan langsung (4/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-918
  - TC-FA-RP-919
  - TC-FA-RP-920
  - TC-FA-RP-929
  - TC-FA-RP-930
  - TC-FA-RP-931
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (4/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user & role (Group, Update) (Pre-setup #7), email `murGroup_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroup.email`), password `Spectra.env.FA_MUR_GROUP_PASSWORD`.
- Akun ganti (urut): Tanpa Akses (Pre-setup #10, Tono Wibowo), email `noAccess_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.noAccess.email`), password `Spectra.env.FA_NOACCESS_PASSWORD`; lalu Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Manage user & role (Group, Update) (akun aktor pertama); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Budi Santoso; Ahmad Fauzi), #18 (pohon group Company Alpha: `IT Infrastructure`, `Dock 1`), #1 (Default User Admin Utama; memegang `Manage accounting` dan `Manage Open API` untuk TC-FA-RP-929 dan 930), dan #7, #10, #2 sebagai aktor. Cakupan aktor Group (#7): `IT Infrastructure`.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_MUR_GROUP_PASSWORD`, `FA_NOACCESS_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-918: Aktor Group meng-Assign Group Role ke group di luar cakupan ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso ke `Manage files` di group `Dock 1` (di luar cakupan `IT Infrastructure`)
2. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
3. Verifikasi lewat fixture BE tidak ada baris baru di `Dock 1` untuk `Manage files`
4. Ganti akun: sesi API aktor beralih ke Tanpa Akses (Pre-setup #10, Tono Wibowo)

### TC-FA-RP-919: Peran tanpa akses modul meminta daftar penugasan ditolak server

5. Kirim request langsung ke server (bukan lewat UI) untuk membaca daftar Tab Total Control
6. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
7. Verifikasi lewat fixture BE tidak ada data yang dikembalikan

### TC-FA-RP-920: Peran tanpa akses modul membuka rute Detail Role langsung ditolak server

8. Kirim request langsung ke server (bukan lewat UI) untuk membaca Detail Role `Manage Open API`
9. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
10. Verifikasi lewat fixture BE tidak ada data penugasan yang dikembalikan
11. Ganti akun: sesi API aktor beralih ke Total Control (Pre-setup #2, Siti Rahmawati)

### TC-FA-RP-929: Mengedit CRUD baris Default User ditolak server

12. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Admin Utama pada `Manage accounting`
13. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
14. Verifikasi lewat fixture BE nilai Create baris Admin Utama pada `Manage accounting` tidak berubah

### TC-FA-RP-930: Menghapus baris Default User ditolak server

15. Kirim request langsung ke server (bukan lewat UI) untuk menghapus baris Admin Utama pada `Manage Open API`
16. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
17. Verifikasi lewat fixture BE baris Admin Utama pada `Manage Open API` tetap ada

### TC-FA-RP-931: Meng-Remove tingkat akses Default User ditolak server

18. Kirim request langsung ke server (bukan lewat UI) untuk meng-Remove Total Control milik Admin Utama
19. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
20. Verifikasi lewat fixture BE Admin Utama tetap Total Control

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 20 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Urutan TC: TC-FA-RP-918 (Gita Maharani), 919 dan 920 (Tono Wibowo), lalu TC-FA-RP-929, 930, 931 (Total Control); ganti akun dua kali memakai Step eksplisit (S-07).
- Temuan untuk QA:
  - TC-FA-RP-929 sampai 931 menyebut Pre-setup #15 dan #1 pada Precondition, tetapi baris Admin Utama pada `Manage accounting` dan `Manage Open API` hanya tersirat dari Default User (Total Control permanen); spec men-seed baris itu bila belum ada. Post Condition kosong pada seluruh TC.
  - TC-FA-RP-919 dan 920 menyebut "Tidak ada data yang dikembalikan" tanpa bentuk respons; spec mengasersi hanya yang disebut TC.
