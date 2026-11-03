---
id: TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3
title: "Defense-in-depth: penolakan server atas permintaan langsung (3/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-917
  - TC-FA-RP-922
  - TC-FA-RP-925
  - TC-FA-RP-926
  - TC-FA-RP-928
  - TC-FA-RP-965
  - TC-FA-RP-966
  - TC-FA-RP-970
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (3/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager (Pre-setup #5), email `groupManager_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.groupManager.email`), password `Spectra.env.FA_GM_PASSWORD`. Pengguna: Fajar Nugroho; Group Manager di `IT Infrastructure`.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso), #12 (Maya Anggraeni: Read Only; baris Group Role `Manage files` Read di `Data Center`), #13 (Kevin Susanto: Group Manager di `Data Center`), #17 (Home Group pengguna Company Alpha), #18 (pohon group Company Alpha: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`), dan #38 (Tab Group Manager terisi enam baris termasuk baris `Head Office`).
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_GM_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-917: Group Manager meng-Assign Read Only ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Read Only ke Ahmad Fauzi
2. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
3. Verifikasi lewat fixture BE Ahmad Fauzi tidak berstatus Read Only

### TC-FA-RP-922: Group Manager menghapus baris target Read Only ditolak server

4. Kirim request langsung ke server (bukan lewat UI) untuk menghapus baris Maya Anggraeni (Read Only) pada `Manage files` di `Data Center`
5. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
6. Verifikasi lewat fixture BE baris Maya Anggraeni pada `Manage files` di `Data Center` tetap ada

### TC-FA-RP-925: Group Manager menugaskan Group Manager lain pada descendant group-nya ditolak server

7. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso sebagai Group Manager di `Rack A1` (descendant dari `IT Infrastructure`)
8. Verifikasi respons status `403` dengan pesan `Only Default User or Total Control can assign Group Manager.`
9. Verifikasi lewat fixture BE tidak ada penugasan Group Manager baru untuk Budi Santoso

### TC-FA-RP-926: Group Manager menugaskan Group Manager pada group yang dikelolanya sendiri ditolak server

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Budi Santoso sebagai Group Manager di `IT Infrastructure`
11. Verifikasi respons status `403` dengan pesan `Only Default User or Total Control can assign Group Manager.`
12. Verifikasi lewat fixture BE tidak ada penugasan Group Manager baru untuk Budi Santoso

### TC-FA-RP-928: Group Manager melepas Group Manager lain ditolak server

13. Kirim request langsung ke server (bukan lewat UI) untuk meng-Remove Group Manager Kevin Susanto di `Data Center`
14. Verifikasi respons status `403` dengan pesan `Only Default User or Total Control can assign Group Manager.`
15. Verifikasi lewat fixture BE penugasan Group Manager Kevin Susanto di `Data Center` tetap ada

### TC-FA-RP-965: Penyaringan row scope Group Manager diterapkan di server, bukan hanya di klien

16. Kirim request langsung ke server (bukan lewat UI) untuk membaca seluruh penugasan Group Manager tanpa parameter group
17. Verifikasi hasil memuat sedikitnya satu penugasan dalam cakupan `IT Infrastructure` beserta descendant
18. Verifikasi hasil hanya memuat penugasan dalam cakupan `IT Infrastructure` beserta descendant dan baris `Head Office` tidak dikembalikan

### TC-FA-RP-966: Penyaringan Tab Total Control berdasarkan Home Group dilakukan di server

19. Kirim request langsung ke server (bukan lewat UI) untuk membaca daftar Total Control tanpa filter
20. Verifikasi hasil memuat sedikitnya satu pengguna ber-Home Group dalam cakupan aktor
21. Verifikasi hasil hanya memuat user ber-Home Group dalam cakupan aktor

### TC-FA-RP-970: Urutan penolakan server: pesan diri sendiri mendahului pesan baris target Group Manager

22. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create pada baris Fajar Nugroho sendiri di `Manage files` pada node `IT Infrastructure` (baris milik aktor dan sekaligus baris Group Manager di node-nya)
23. Verifikasi respons status `403` dengan pesan `You can't manage your own account from here.`
24. Verifikasi pesan `You don't have permission to edit.` tidak dipakai pada respons tersebut

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 24 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- TC-FA-RP-965 dan 966 adalah request baca langsung; Expected berupa isi hasil (tidak ada status respons yang disebut TC), sehingga yang diasersi hanya isi hasil. Anchor positif (hasil memuat penugasan atau pengguna dalam cakupan) mendahului asersi "hanya/tidak dikembalikan" (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-965 dan 966 tidak menyebut status respons (hanya isi hasil); spec tidak menambahkan asersi status. TC-FA-RP-966 tidak merinci user mana yang berada di luar cakupan aktor (Home Group #17); spec tidak menyebut nama.
  - TC-FA-RP-970 Expected b (pesan `You don't have permission to edit.` tidak dipakai) diasersi sebagai pesan yang tidak muncul pada respons itu; TC tidak menyebut cara membuktikannya selain isi pesan respons. Akun aktor Group Manager (Pre-setup #5) tidak tertulis rujukan #5 pada Precondition tetapi disebut Catatan TC sebagai akun login default.
  - Post Condition kosong pada seluruh TC spec ini.
