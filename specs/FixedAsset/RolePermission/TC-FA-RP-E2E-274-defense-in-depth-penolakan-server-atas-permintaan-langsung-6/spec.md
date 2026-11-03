---
id: TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6
title: "Defense-in-depth: penolakan server atas permintaan langsung (6/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-941
  - TC-FA-RP-942
  - TC-FA-RP-945
  - TC-FA-RP-946
  - TC-FA-RP-947
  - TC-FA-RP-949
  - TC-FA-RP-950
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (6/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso sebagai Standard tanpa tingkat akses) dan #3 (Rina Wulandari, Total Control kedua; TC-FA-RP-942, 949, dan 950). Kondisi yang di-seed: satu pengguna uji yang identitasnya sudah dihapus (TC-FA-RP-941), group uji yang sudah dihapus (TC-FA-RP-946), baris Budi Santoso pada `Manage accounting` yang sudah dihapus (TC-FA-RP-947), dan group `Data Center` (TC-FA-RP-945 memakai Budi Santoso tanpa Group).
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-941: Assign memuat user yang sudah dihapus ditolak server seluruhnya

1. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control ke Ahmad Fauzi (valid) dan satu user yang identitasnya sudah dihapus
2. Verifikasi respons status `422` dengan pesan `[User Name] no longer exists. Please select another.`
3. Verifikasi lewat fixture BE tidak ada penugasan dibuat untuk Ahmad Fauzi (atomik)

### TC-FA-RP-942: Assign memuat user yang tidak eligible ditolak server seluruhnya

4. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control ke Rina Wulandari (sudah Total Control) dan Ahmad Fauzi
5. Verifikasi respons status `422` dengan pesan `Rina Wulandari is no longer eligible. Please select another.`
6. Verifikasi lewat fixture BE tidak ada penugasan dibuat (atomik)

### TC-FA-RP-945: Assign Group Manager tanpa group ditolak server

7. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso sebagai Group Manager tanpa Group
8. Verifikasi respons status `422` dengan pesan `You must select a group`
9. Verifikasi lewat fixture BE tidak ada penugasan baru

### TC-FA-RP-946: Assign ke group yang sudah dihapus ditolak server pada field Group

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso ke `Manage files` pada group yang sudah dihapus
11. Verifikasi respons status `422` dengan pesan `This group no longer exists. Please select another.`
12. Verifikasi lewat fixture BE tidak ada penugasan baru

### TC-FA-RP-947: Edit CRUD atas baris yang sudah dihapus bagi aktor berwenang mengembalikan not found

13. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Budi Santoso yang sudah dihapus pada `Manage accounting`
14. Verifikasi respons status `404`
15. Verifikasi lewat fixture BE tidak ada perubahan tersimpan

### TC-FA-RP-949: Assign Total Control ke user yang sudah Total Control ditolak server

16. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control ke Rina Wulandari
17. Verifikasi respons status `422` dengan pesan `Rina Wulandari is no longer eligible. Please select another.`
18. Verifikasi lewat fixture BE Rina Wulandari tetap Total Control

### TC-FA-RP-950: Assign Read Only ke user Total Control ditolak server

19. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Read Only ke Rina Wulandari
20. Verifikasi respons status `422` dengan pesan `Rina Wulandari is no longer eligible. Please select another.`
21. Verifikasi lewat fixture BE Rina Wulandari tetap Total Control

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Pesan 422 TC-FA-RP-941 memuat `[User Name]` ditulis literal sebagai placeholder sesuai TC (copy PRD); nilai nama pengguna yang menggantikan placeholder tidak diasersi karena TC tidak menyebutnya untuk pengguna yang sudah dihapus. Pesan 422 TC-FA-RP-942, 949, dan 950 memuat nama konkret `Rina Wulandari` sesuai TC.
- Temuan untuk QA:
  - TC-FA-RP-941 tidak menyebut nama pengguna pada placeholder `[User Name]` (user yang dihapus); spec tidak mengasersi substitusinya. TC-FA-RP-945 tidak merujuk Pre-setup #18 meski Group Manager membutuhkan group.
  - Precondition TC-FA-RP-941 dan 946 tidak merinci cara menyiapkan user dan group yang sudah dihapus; spec men-seed lewat seeding API. Post Condition kosong pada seluruh TC.
