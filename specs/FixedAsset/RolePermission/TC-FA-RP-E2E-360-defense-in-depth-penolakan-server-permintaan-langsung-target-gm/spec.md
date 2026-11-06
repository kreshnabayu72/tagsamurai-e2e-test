---
id: TC-FA-RP-E2E-360-defense-in-depth-penolakan-server-permintaan-langsung-target-gm
title: "Defense-in-depth: penolakan server atas permintaan langsung yang menyasar target Group Manager"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1197
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung yang menyasar target Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi API aktor, bukan sesi UI): Group Manager Fajar Nugroho (Pre-setup #5; `groupManager_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_GM_PASSWORD`; lalu Manage user & role (Group, Update) Gita Maharani (Pre-setup #7; `murGroup_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_MUR_GROUP_PASSWORD`. Sesi API Fajar Nugroho dibuka di hook `before` spec ini; halaman dibuka hook `beforeEach` suite dan tidak dipakai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #5, #7, #13 (Kevin Susanto, Group Manager hanya di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`: Group Role katalog selain `Manage user & role` dengan CRUD penuh dan Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi), #18 (pohon group Company Alpha), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`). Baris yang diasersi tetap ada: Group Role `Manage files` Kevin Susanto di `Rack A1` dan Approver Kevin Susanto di `Rack A1` sub-tab `Disposal`. Seed Group Manager yang menulis baris pola disediakan tim FE/BE (tanpa endpoint karangan).
- Kemampuan teknis: request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`, Hook suite); endpoint tidak disebut karena tidak ada di TC. State data dibaca lewat fixture BE (disediakan tim FE/BE). Asersi hanya status respons, pesan respons, dan state data (bagian 8b butir 1).
- Baseline (S-12): jumlah penugasan Monitoring & Report pada `Data Center` sub-tab `Disposal` dicatat lewat fixture BE sebelum request pertama.
- State global yang diubah: tidak ada (seluruh request diharapkan ditolak). Tanpa data Dinamis. Pemulihan bila ada request yang ternyata lolos: baris Kevin Susanto dan penugasan Monitoring & Report dipulihkan ke Tabel Data Uji Pre-setup TC (#13, #19) di hook `after` lewat fixture BE. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`, `FA_MUR_GROUP_PASSWORD`, dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password dan token tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1197: permintaan langsung ke target Group Manager ditolak server

1. Catat baseline (aksi tanpa `Verifikasi`): jumlah penugasan Monitoring & Report pada `Data Center` sub-tab `Disposal` lewat fixture BE
2. Kirim request langsung ke server (bukan lewat UI) sebagai Fajar Nugroho untuk meng-Assign Kevin Susanto sebagai Monitoring & Report pada `Data Center` sub-tab `Disposal`
3. Verifikasi respons status `422` dengan pesan `Kevin Susanto is no longer eligible. Please select another.`
4. Kirim request langsung ke server (bukan lewat UI) sebagai Fajar Nugroho untuk menghapus baris Kevin Susanto pada `Manage files` di `Rack A1`
5. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
6. Kirim request langsung ke server (bukan lewat UI) sebagai Fajar Nugroho untuk Remove baris Approver Kevin Susanto di `Rack A1` sub-tab `Disposal`
7. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
8. Ganti akun: sesi API aktor beralih ke Manage user & role (Group, Update) Gita Maharani
9. Kirim request langsung ke server (bukan lewat UI) sebagai Gita Maharani untuk menghapus baris Kevin Susanto pada `Manage files` di `Rack A1`
10. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
11. Kirim request langsung ke server (bukan lewat UI) sebagai Gita Maharani untuk Remove baris Approver Kevin Susanto di `Rack A1` sub-tab `Disposal`
12. Verifikasi respons status `403` dengan pesan `You don't have permission to edit.`
13. Verifikasi lewat fixture BE jumlah penugasan Monitoring & Report pada `Data Center` sub-tab `Disposal` sama dengan baseline langkah 1 (tidak ada penugasan baru)
14. Verifikasi lewat fixture BE baris Kevin Susanto pada `Manage files` di `Rack A1` tetap ada
15. Verifikasi lewat fixture BE baris Approver Kevin Susanto di `Rack A1` sub-tab `Disposal` tetap ada
16. Verifikasi lewat fixture BE Kevin Susanto tetap Group Manager

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 16 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Bagian 8b butir 1: seluruh langkah "Kirim request langsung" tidak melewati browser; pengalihan halaman, toast, atau tampilan tidak diasersi di spec ini. Perilaku FE untuk respons yang sama tidak ditulis.
- Langkah penghubung (S-03): pencatatan baseline (langkah 1) dan ganti akun sesi API aktor (langkah 8, S-07). Status respons dan pesan respons satu request diasersi dalam satu `Verifikasi` (satu respons); tiap request punya `Verifikasi` sendiri tepat sesudahnya.
- Pembagian TC lintas spec: TC-FA-RP-1197 hanya ada di spec ini. Asersi "tidak ada baris atau entri log baru" atas penolakan ini tidak diasersi di spec ini (S-05; TC tidak memuatnya).
- Temuan untuk QA:
  - TC-FA-RP-1197 tidak menyebut endpoint dan body request; spec tidak mengarangnya (klien HTTP dan fixture BE disediakan tim FE/BE).
  - TC-FA-RP-1197 Expected a menyebut pesan `Kevin Susanto is no longer eligible. Please select another.` sebagai "copy `V-09`" tanpa penanda copy usulan; spec menyalin teks persis.
  - TC-FA-RP-1197 Expected c ("tidak ada penugasan baru") tidak menyebut pembanding; spec memakai baseline jumlah penugasan Monitoring & Report pada `Data Center` sub-tab `Disposal` (langkah 1 dan 13).
  - Seed Kevin Susanto: Pre-setup #13 dan #43 menyebut Group Manager hanya di `Data Center`, sedangkan Pre-setup #38 menyebut Group Manager di `Data Center` dan `Helpdesk`; spec memakai #13 dan #43. Post Condition TC kosong.
