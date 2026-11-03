---
id: TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5
title: "Defense-in-depth: penolakan server atas permintaan langsung (5/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-932
  - TC-FA-RP-933
  - TC-FA-RP-934
  - TC-FA-RP-935
  - TC-FA-RP-937
  - TC-FA-RP-939
  - TC-FA-RP-940
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (5/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Budi Santoso memegang `Manage Open API`; Siti Rahmawati aktor memegang `Manage accounting`), #1 (Admin Utama, Default User; memegang `Manage Open API`), dan #18 (pohon group Company Alpha: `Data Center`; Group Role `Manage files`) serta #19 (Approver pada `IT Infrastructure` sub-tab `Disposal`) untuk TC-FA-RP-937.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini). Pada TC-FA-RP-934 dan 939 baris Budi Santoso terhapus oleh request itu sendiri dan dipulihkan antar TC lewat seeding API.
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-932: Meng-Assign Read Only ke Default User ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Read Only ke Admin Utama
2. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
3. Verifikasi lewat fixture BE Admin Utama tidak berstatus Read Only

### TC-FA-RP-933: Meng-Assign Group Manager ke Default User ditolak server

4. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Admin Utama sebagai Group Manager di `Data Center`
5. Verifikasi respons status `403` dengan pesan `Default User cannot be modified.`
6. Verifikasi lewat fixture BE tidak ada penugasan Group Manager untuk Admin Utama

### TC-FA-RP-934: Bulk Remove yang memuat baris Default User ditolak per baris

7. Kirim request langsung ke server (bukan lewat UI) untuk Bulk Remove baris Admin Utama dan Budi Santoso pada `Manage Open API`
8. Verifikasi respons status `403` untuk baris Admin Utama dan sukses untuk baris Budi Santoso dengan pesan `Default User cannot be modified.`
9. Verifikasi lewat fixture BE baris Admin Utama tetap ada pada `Manage Open API`
10. Verifikasi lewat fixture BE baris Budi Santoso terhapus dari `Manage Open API` (partial success)

### TC-FA-RP-935: Mengedit CRUD baris diri sendiri ditolak server

11. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Siti Rahmawati pada `Manage accounting`
12. Verifikasi respons status `403` dengan pesan `You can't manage your own account from here.`
13. Verifikasi lewat fixture BE nilai Create baris Siti Rahmawati pada `Manage accounting` tidak berubah

### TC-FA-RP-937: Meng-Assign diri sendiri di tiap popup ditolak server

14. Kirim enam request terpisah langsung ke server (bukan lewat UI) untuk meng-Assign Siti Rahmawati sebagai:
   - Total Control
   - Read Only
   - Group Manager
   - Global Role `Manage Open API`
   - Group Role `Manage files`
   - Approver
15. Verifikasi respons status `403` pada keenam request dengan pesan `You can't manage your own account from here.`
16. Verifikasi lewat fixture BE tidak ada penugasan baru untuk Siti Rahmawati

### TC-FA-RP-939: Bulk Remove yang memuat baris diri sendiri ditolak per baris

17. Pulihkan Budi Santoso memegang `Manage Open API` lewat seeding API, hingga tersimpan
18. Kirim request langsung ke server (bukan lewat UI) untuk Bulk Remove baris Siti Rahmawati dan Budi Santoso pada `Manage Open API`
19. Verifikasi respons status `403` untuk baris Siti Rahmawati dan sukses untuk Budi Santoso dengan pesan `You can't manage your own account from here.`
20. Verifikasi lewat fixture BE baris Siti Rahmawati tetap ada pada `Manage Open API`

### TC-FA-RP-940: Assign tanpa user ditolak server dengan pesan V-07

21. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control dengan daftar user kosong
22. Verifikasi respons status `422` dengan pesan `You must pick a user`
23. Verifikasi lewat fixture BE tidak ada penugasan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 23 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 17; tidak ada `Verifikasi`.
- TC-FA-RP-934 dan 939 mencampur status per baris (403 dan sukses) dalam satu request Bulk Remove; baris Budi Santoso dipulihkan memegang `Manage Open API` lewat seeding API pada langkah 17 sebelum TC-FA-RP-939 yang membutuhkannya (S-09; langkah seeding tanpa `Verifikasi`). Urutan TC dalam spec: 932, 933, 934, 935, 937, 939, 940.
- Temuan untuk QA:
  - TC-FA-RP-934 dan 939 menulis Expected a sebagai satu status respons campuran ("403 untuk baris X dan sukses untuk baris Y") dengan satu pesan; spec mengasersinya apa adanya dan tidak menafsirkan bentuk status per baris. TC-FA-RP-937 menyebut enam request tanpa daftar urutan baku; spec memakai urutan yang tertulis.
  - TC-FA-RP-940 menulis pesan `You must pick a user` tanpa tanda baca akhir sesuai TC. Post Condition kosong pada seluruh TC.
