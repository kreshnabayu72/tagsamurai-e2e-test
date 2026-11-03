---
id: TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9
title: "Defense-in-depth: penolakan server atas permintaan langsung (9/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-938
  - TC-FA-RP-957
  - TC-FA-RP-961
  - TC-FA-RP-963
  - TC-FA-RP-964
  - TC-FA-RP-1126
  - TC-FA-RP-1143
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (9/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Akun ganti (TC-FA-RP-938): Default User (Pre-setup #1, Admin Utama), email `defaultUser_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.defaultUser.email`), password `Spectra.env.FA_DU_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard), #1 (Admin Utama, Default User; memegang `Manage accounting`), #11 (Lina Marlina: Group Manager di `Head Office`, tanpa baris Group Role eksplisit; TC-FA-RP-1143), #18 (pohon group Company Alpha: `Head Office`, `Helpdesk`, `IT Infrastructure`), #19 (seed Role Transaksi Disposal pada `IT Infrastructure`; `Helpdesk` tanpa Approver dan Group Manager), dan #28 (`Company Beta`: Total Control dan penugasan `Beta Only` atas nama pengguna Zahra Beta pemegang `Manage group`; TC-FA-RP-963 dan 964). Spec tidak login ke `Company Beta`; state `Company Beta` diperiksa lewat fixture BE.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_DU_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-957: Mengaktifkan Require Approval tanpa prasyarat ditolak server dan nilai tetap OFF

1. Kirim request langsung ke server (bukan lewat UI) untuk mengaktifkan Require Approval `Disposal` pada node `Helpdesk` tanpa Approver dan Group Manager
2. Verifikasi respons status `422`
3. Verifikasi lewat fixture BE nilai Require Approval `Disposal` pada node `Helpdesk` tetap Off

### TC-FA-RP-961: Radio aturan persetujuan di luar enum ditolak validasi skema

4. Kirim request langsung ke server (bukan lewat UI) untuk menyimpan aturan persetujuan `Disposal` dengan nilai `majority`
5. Verifikasi respons status `422`
6. Verifikasi lewat fixture BE aturan persetujuan `Disposal` tidak berubah

### TC-FA-RP-1126: Assign Role Transaksi untuk Default User ditolak server

7. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Admin Utama sebagai Asset Admin, Monitoring & Report, Staff, dan Approver pada `IT Infrastructure` sub-tab Disposal (empat request)
8. Verifikasi respons status `403` pada keempat request dengan pesan `Default User cannot be modified.`
9. Verifikasi lewat fixture BE tidak ada penugasan Role Transaksi untuk Admin Utama

### TC-FA-RP-1143: Assign Group Role ke target Group Manager pada node GM-nya lewat request langsung ditolak server

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Lina Marlina ke Group Role `Manage files` di `Head Office`
11. Verifikasi respons status `422` dengan pesan `Lina Marlina is no longer eligible. Please select another.`
12. Verifikasi lewat fixture BE tidak ada baris Group Role baru untuk Lina Marlina pada Detail Role `Manage files` di `Head Office`

### TC-FA-RP-963: Isolasi tenant: data Company Beta tidak terbaca dari Company Alpha

13. Kirim request langsung ke server (bukan lewat UI) untuk membaca penugasan milik `Company Beta` (Zahra Beta) memakai sesi Company Alpha
14. Verifikasi hasil memuat data Company Alpha (sedikitnya satu penugasan Company Alpha)
15. Verifikasi hasil tidak memuat data Company Beta
16. Verifikasi hasil tidak memuat data `Beta Only`

### TC-FA-RP-964: Isolasi tenant: penulisan ke data Company Beta ditolak

17. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control pada pengguna milik `Company Beta` memakai sesi Company Alpha
18. Verifikasi respons status `403`
19. Verifikasi lewat fixture BE tidak ada perubahan pada Company Beta (Total Control Company Beta dan penugasan `Beta Only` tidak berubah)
20. Ganti akun: sesi API aktor beralih ke Default User (Pre-setup #1, Admin Utama)

### TC-FA-RP-938: Default User yang menarget dirinya sendiri: pesan Default User mendahului pesan diri sendiri

21. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Admin Utama (milik aktor sendiri)
22. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
23. Verifikasi lewat fixture BE nilai Create baris Admin Utama tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 23 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- TC-FA-RP-938 diletakkan terakhir karena membutuhkan ganti akun ke Default User (Step eksplisit, S-07); hook `after` mengembalikan sesi ke akun default suite. TC-FA-RP-963 dan 964 memakai sesi Company Alpha (Total Control) sesuai Precondition.
- TC-FA-RP-957 dan 961 Expected b menyebut juga "tidak ada entri log"; asersi itu ada di spec 292 (Absence log: permintaan langsung yang ditolak; aksi nyata dengan baseline sendiri, S-05); spec ini hanya mengasersi status respons dan state data. TC-FA-RP-963 dan 964 tidak memuat langkah periksa state di TC; spec mengasersi isi hasil dan state `Company Beta` lewat fixture BE.
- Temuan untuk QA:
  - TC-FA-RP-963 dan 964 merujuk Pre-setup #28 tetapi tidak menyebut pengguna `Company Beta` mana yang menjadi target TC-FA-RP-964 ("pengguna milik `Company Beta`"); spec memakai Zahra Beta (`Beta Only`) sebagai target dan tidak menyebut akun login Total Control `Company Beta` (`FA_BETA_TC_PASSWORD` tidak dipakai). TC-FA-RP-963 tidak menyebut status respons.
  - TC-FA-RP-957 Expected a hanya `422` tanpa pesan. Post Condition kosong pada seluruh TC.
