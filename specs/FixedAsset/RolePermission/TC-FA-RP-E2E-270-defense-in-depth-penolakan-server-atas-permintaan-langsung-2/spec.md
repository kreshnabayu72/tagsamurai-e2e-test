---
id: TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2
title: "Defense-in-depth: penolakan server atas permintaan langsung (2/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-921
  - TC-FA-RP-923
  - TC-FA-RP-924
  - TC-FA-RP-927
  - TC-FA-RP-936
  - TC-FA-RP-967
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (2/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role dengan Update (Pre-setup #6), email `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`), password `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi memegang `Manage accounting` dengan Create nonaktif; Budi Santoso), #3 (Rina Wulandari, Total Control kedua; memegang Role Transaksi Asset Admin pada `IT Infrastructure` sub-tab `Disposal` lewat seed API untuk TC-FA-RP-924), #13 dan #18 (Kevin Susanto Group Manager di `Data Center`, pohon group Company Alpha), dan #6 (Hendra Wijaya sebagai aktor dan target TC-FA-RP-936 dan 967).
- Kemampuan teknis: sesi API aktor Total Control (Sesi 2 pada TC-FA-RP-967) memakai password `Spectra.env.FA_TC_PASSWORD`; membaca status respons request simpan yang dikirim UI (TC-FA-RP-967) disediakan tim FE (pemantauan jaringan). TC-FA-RP-967 berlabel `Manual Only — (d) dua sesi paralel`; pelaku kedua (Sesi 2) memakai sesi API.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini). Pencabutan Global Role `Manage global user & role` milik Hendra Wijaya pada TC-FA-RP-967 dipulihkan di hook `after`.
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-921: Manage user & role mengedit CRUD target Total Control ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Rina Wulandari (Total Control) pada `Manage accounting`
2. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
3. Verifikasi lewat fixture BE nilai Create baris Rina Wulandari pada `Manage accounting` tidak berubah

### TC-FA-RP-923: Manage user & role menghapus baris Group Role target Group Manager di node GM-nya ditolak server

4. Kirim request langsung ke server (bukan lewat UI) untuk menghapus baris Kevin Susanto pada `Manage files` di `Data Center`
5. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
6. Verifikasi lewat fixture BE baris Kevin Susanto pada `Manage files` di `Data Center` tetap ada

### TC-FA-RP-924: Manage user & role menghapus Role Transaksi milik target Total Control ditolak server

7. Kirim request langsung ke server (bukan lewat UI) untuk menghapus penugasan Role Transaksi milik Rina Wulandari sebagai Asset Admin pada `IT Infrastructure` sub-tab `Disposal`
8. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
9. Verifikasi lewat fixture BE penugasan Rina Wulandari sebagai Asset Admin pada `IT Infrastructure` sub-tab `Disposal` tetap ada

### TC-FA-RP-927: Manage user & role menugaskan Group Manager ditolak server

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso sebagai Group Manager di `Data Center`
11. Verifikasi respons status `403` dengan pesan `Only Default User or Total Control can assign Group Manager.`
12. Verifikasi lewat fixture BE tidak ada penugasan Group Manager baru untuk Budi Santoso

### TC-FA-RP-936: Menghapus baris diri sendiri ditolak server

13. Kirim request langsung ke server (bukan lewat UI) untuk menghapus baris Hendra Wijaya pada `Manage global user & role`
14. Verifikasi respons status `403` dengan pesan `You can't manage your own account from here.`
15. Verifikasi lewat fixture BE baris Hendra Wijaya pada `Manage global user & role` tetap ada

### TC-FA-RP-967: Permission dibaca ulang pada setiap request: pencabutan wewenang berlaku pada request berikutnya

16. Sesi 1 (Hendra Wijaya, UI) membuka Tab System lalu Detail Role `Manage accounting`
17. Sesi 2 (Total Control, sesi API aktor) mencabut Global Role `Manage global user & role` milik Hendra Wijaya hingga tersimpan
18. Sesi 1 mencentang Create pada baris Ahmad Fauzi tanpa login ulang
19. Verifikasi request Sesi 1 ditolak dengan status respons `403` dan pesan `You don't have permission to do this.`
20. Verifikasi lewat fixture BE nilai Create baris Ahmad Fauzi pada `Manage accounting` tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 20 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- TC-FA-RP-967 diletakkan terakhir karena mencabut wewenang aktor (S-10); hook `after` memulihkan Global Role Hendra Wijaya. Sesi 2 memakai sesi API aktor sehingga bukan konteks kedua kelas c (`P-2` tidak diperlukan).
- TC-FA-RP-967 memakai klik UI Sesi 1 sebagai pemicu request; status respons dibaca lewat pemantauan jaringan, bukan request langsung.
- Temuan untuk QA:
  - TC-FA-RP-967 tidak menyebut jalur UI untuk membaca status `403`; spec membaca status respons request simpan Sesi 1 lewat pemantauan jaringan (kemampuan disediakan tim FE). Post Condition kosong pada seluruh TC spec ini.
  - Precondition TC-FA-RP-921, 923, 927, 936, dan 967 tidak merujuk Pre-setup #13 dan #18 secara konsisten; spec memakainya dari data target yang disebut langkah (Kevin Susanto di `Data Center`).
