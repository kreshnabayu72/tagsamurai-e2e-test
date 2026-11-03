---
id: TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7
title: "Defense-in-depth: penolakan server atas permintaan langsung (7/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-951
  - TC-FA-RP-952
  - TC-FA-RP-953
  - TC-FA-RP-954
  - TC-FA-RP-955
  - TC-FA-RP-956
  - TC-FA-RP-958
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (7/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Akun ganti (TC-FA-RP-958): Total Control pada `Client Addon Off` (Pre-setup #31: lisensi Addon Audit, Maintenance, dan Tracking tidak aktif). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ADDON_OFF_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso), #3 (Rina Wulandari, Total Control kedua), #12 (Maya Anggraeni: Read Only), #16 (Eka Saputra: Active, Pending Activation), #17 (Gunawan Halim: Home Group `Data Center`; Hesti Rahma: Home Group `Logistics Warehouse`), #18 (pohon group Company Alpha), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`).
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_ADDON_OFF_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-951: Assign Group Manager ke user Total Control atau Read Only ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Rina Wulandari (Total Control) dan Maya Anggraeni (Read Only) sebagai Group Manager di `Data Center` (dua request)
2. Verifikasi respons status `422` pada kedua request dengan pesan `Rina Wulandari is no longer eligible. Please select another.` pada request Rina Wulandari dan `Maya Anggraeni is no longer eligible. Please select another.` pada request Maya Anggraeni
3. Verifikasi lewat fixture BE tidak ada penugasan Group Manager baru

### TC-FA-RP-952: Assign Group Role di luar Home Group constraint ditolak server

4. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Gunawan Halim (Home Group `Data Center`) ke `Manage files` di `Helpdesk`
5. Verifikasi respons status `422` dengan pesan `Gunawan Halim is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus Home Group constraint)
6. Verifikasi lewat fixture BE tidak ada baris baru untuk Gunawan Halim pada `Manage files` di `Helpdesk`

### TC-FA-RP-953: Assign Approver untuk user di luar afiliasi group ditolak server

7. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Hesti Rahma (Home Group `Logistics Warehouse`) sebagai Approver pada `IT Infrastructure` sub-tab Disposal
8. Verifikasi respons status `422` dengan pesan `Hesti Rahma is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus afiliasi group)
9. Verifikasi lewat fixture BE tidak ada penugasan baru

### TC-FA-RP-954: Assign Asset Admin, Monitoring & Report, atau Staff untuk user di luar afiliasi ditolak server

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Hesti Rahma sebagai Asset Admin, Monitoring & Report, dan Staff pada `IT Infrastructure` sub-tab Disposal (tiga request)
11. Verifikasi respons status `422` pada ketiga request dengan pesan `Hesti Rahma is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus afiliasi group)
12. Verifikasi lewat fixture BE tidak ada penugasan baru

### TC-FA-RP-955: Assign Approver untuk user Read Only ditolak server

13. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Maya Anggraeni (Read Only) sebagai Approver
14. Verifikasi respons status `422` dengan pesan `Maya Anggraeni is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus Read Only)
15. Verifikasi lewat fixture BE tidak ada penugasan baru

### TC-FA-RP-956: Assign Approver untuk user bukan Active dan Activated ditolak server

16. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Eka Saputra (Pending Activation) sebagai Approver
17. Verifikasi respons status `422` dengan pesan `Eka Saputra is no longer eligible. Please select another.`
18. Verifikasi lewat fixture BE tidak ada penugasan baru
19. Ganti akun: sesi API aktor beralih ke Total Control `Client Addon Off` (Pre-setup #31; akun disediakan tim FE, password `Spectra.env.FA_ADDON_OFF_TC_PASSWORD`)

### TC-FA-RP-958: Menulis ke sub-tab Addon yang lisensinya nonaktif ditolak server

20. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Asset Admin pada sub-tab `Audit` ketika lisensi Addon Audit nonaktif
21. Verifikasi respons status `403` dengan pesan `This feature requires an active add-on license.`
22. Verifikasi lewat fixture BE tidak ada penugasan baru

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- TC-FA-RP-958 diletakkan terakhir karena membutuhkan ganti akun ke tenant `Client Addon Off` (Step eksplisit, S-07); hook `after` mengembalikan sesi ke akun default suite.
- Copy `(copy usulan, PRD 12 #1)` pada TC-FA-RP-952 sampai 955 (keputusan NC-02) diasersi literal sesuai TC; asersi bergantung pada persetujuan PM atas copy itu, dan bila PM mengubahnya TC dan spec terkait diperbarui.
- Temuan untuk QA:
  - Akun Total Control `Client Addon Off` tidak tertulis di Pre-setup TC (#31 hanya menyebut tenant). Precondition TC-FA-RP-958 merujuk #15 dan #18 tetapi aksinya terjadi di tenant `Client Addon Off` (#31); spec memakai akun tenant itu.
  - TC-FA-RP-952 sampai 955 menulis klausa parentetik copy `V-09` yang tidak diasersi sebagai klausa terpisah. Post Condition kosong pada seluruh TC.
