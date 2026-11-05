---
id: TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima
title: "Defense-in-depth: request langsung Assign Role Transaksi ke ancestor atau sibling constraint ditolak 422, ke node dalam constraint atau user tanpa constraint diterima"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1238
  - TC-FA-RP-1239
coverage:
  web: automated
---

# Defense-in-depth: request langsung Assign Role Transaksi ke ancestor atau sibling constraint ditolak 422, ke node dalam constraint atau user tanpa constraint diterima

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi API aktor, bukan sesi UI): Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite dan tidak dipakai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor): lihat `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (kolam pengguna Standard, tercantum di Precondition TC), #17 (Gunawan Halim: Home Group `Data Center`; Indra Kusuma: tanpa Home Group; keduanya Active, Activated), #18 (pohon Group: `IT Infrastructure` ancestor `Data Center`, `Helpdesk` sibling `Data Center` di bawah `IT Infrastructure`, `Rack A1` di bawah `Data Center`, `Dock 1` di bawah `Logistics Warehouse`), dan #19 (seed Role Transaksi `IT Infrastructure` sub-tab `Disposal`). Spec tidak membuat data Dinamis.
- Seeding precondition (hook `before`, lewat fixture BE yang disediakan tim FE/BE, tanpa endpoint karangan): Gunawan Halim tanpa penugasan Role Transaksi pada `IT Infrastructure`, `Helpdesk`, dan `Rack A1` sub-tab `Disposal`; Indra Kusuma tanpa penugasan Role Transaksi pada `Dock 1` sub-tab `Disposal` (sisa penugasan dicabut).
- Kemampuan teknis: request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`, Hook suite); endpoint dan body request tidak disebut karena tidak ada di TC. State data dibaca dan dipulihkan lewat fixture BE (disediakan tim FE/BE). Asersi hanya status respons, pesan respons, dan state data (bagian 8b butir 1).
- Baseline (S-12): penugasan Role Transaksi Gunawan Halim pada `IT Infrastructure`, `Helpdesk`, dan `Rack A1` serta Indra Kusuma pada `Dock 1` (sub-tab `Disposal`) dicatat lewat fixture BE sebelum request pertama.
- State yang diubah dan pemulihannya: request sukses langkah 10 dan 13 menambah penugasan Asset Admin Gunawan Halim pada `Rack A1` dan Indra Kusuma pada `Dock 1` sub-tab `Disposal` (data Pre-setup bersama #18). Keduanya dicabut pada langkah terakhir spec dan di hook `after` sebagai cadangan, lewat fixture BE, sehingga kedua node kembali tanpa penugasan manual keduanya (Pre-setup #19 dan #17). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password dan token tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1238: Request langsung Assign Role Transaksi ke ancestor atau sibling constraint ditolak server

1. Catat baseline (aksi tanpa `Verifikasi`): penugasan Role Transaksi Gunawan Halim pada `IT Infrastructure`, `Helpdesk`, dan `Rack A1` serta Indra Kusuma pada `Dock 1` (sub-tab `Disposal`) lewat fixture BE
2. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Gunawan Halim (Home Group `Data Center`) sebagai Asset Admin pada `IT Infrastructure` sub-tab Disposal (ancestor constraint)
3. Verifikasi respons langkah 2 berstatus `422`
4. Verifikasi pesan respons langkah 2 memuat `Gunawan Halim is no longer eligible.` (copy `V-09`, tanpa copy khusus Home Group constraint)
5. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Gunawan Halim sebagai Approver pada `Helpdesk` sub-tab Disposal (sibling di luar constraint)
6. Verifikasi respons langkah 5 berstatus `422`
7. Verifikasi pesan respons langkah 5 memuat `Gunawan Halim is no longer eligible.` (copy `V-09`, tanpa copy khusus Home Group constraint)
8. Verifikasi lewat fixture BE tidak ada penugasan Role Transaksi baru untuk Gunawan Halim pada `IT Infrastructure` sub-tab Disposal (sama dengan baseline langkah 1)
9. Verifikasi lewat fixture BE tidak ada penugasan Role Transaksi baru untuk Gunawan Halim pada `Helpdesk` sub-tab Disposal (sama dengan baseline langkah 1)

### TC-FA-RP-1239: Request langsung Assign Role Transaksi diterima server untuk node dalam constraint dan user tanpa constraint

10. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Gunawan Halim (Home Group `Data Center`) sebagai Asset Admin pada `Rack A1` sub-tab Disposal
11. Verifikasi respons langkah 10 sukses (bukan `422`)
12. Verifikasi lewat fixture BE Gunawan Halim tercatat sebagai Asset Admin `Rack A1` sub-tab Disposal
13. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Indra Kusuma (tanpa Home Group) sebagai Asset Admin pada `Dock 1` sub-tab Disposal
14. Verifikasi respons langkah 13 sukses (bukan `422`)
15. Verifikasi lewat fixture BE Indra Kusuma tercatat sebagai Asset Admin `Dock 1` sub-tab Disposal
16. Pulihkan lewat fixture BE (aksi tanpa `Verifikasi`): cabut baris Asset Admin Gunawan Halim pada `Rack A1` dan Indra Kusuma pada `Dock 1` sub-tab Disposal

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 16 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons, pesan respons, dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint). Spec berdiri sendiri (kelas a) dan tidak digabung dengan spec defense-in-depth lain.
- Bagian 8b butir 1: seluruh langkah "Kirim request langsung" tidak melewati browser; pengalihan halaman, toast, atau tampilan tidak diasersi di spec ini. Perilaku FE untuk respons yang sama tidak ditulis.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline, S-12) dan langkah 16 (pemulihan, S-09). Urutan: TC penolakan (TC-FA-RP-1238) lebih dulu, TC penerimaan (TC-FA-RP-1239) sesudahnya, karena request yang diterima mengubah state (S-10).
- Pembagian klausa Expected (S-01): TC-FA-RP-1238 a dipecah per request menjadi status (langkah 3 dan 6) dan pesan (langkah 4 dan 7); b dipecah per node (langkah 8 dan 9). TC-FA-RP-1239 a dan b masing-masing: respons sukses (langkah 11 dan 14) dan penyimpanan state (langkah 12 dan 15). Frasa "tanpa copy khusus Home Group constraint" di TC-FA-RP-1238 a adalah penjelasan sumber copy dan tidak diasersi sebagai klausa terpisah.
- Asersi pesan respons dibuat longgar (memuat `<nama> is no longer eligible.`, tanpa kalimat penutup `Please select another.`) karena TC menandai copy sebagai `(copy usulan, PRD 12 #1)` dan arah gate belum dikonfirmasi (lihat Temuan untuk QA). Asersi status `422` dan state tetap ketat.
- Asersi "tidak ada baris atau entri log baru" atas penolakan langkah 3 dan 6 tidak diasersi di spec ini (S-05; TC tidak memuatnya).
- Temuan untuk QA:
  - NC-20 (PRD Open Item #9) menunggu PM: arah gate Home Group constraint pada Role Transaksi, tanpa migrasi, dan copy usulan belum dikonfirmasi. Penolakan ancestor dan sibling (TC-FA-RP-1238) dan penerimaan node dalam constraint (TC-FA-RP-1239) bergantung pada arah gate itu; bila PM mengubahnya, TC dan spec ini diperbarui.
  - Email Gunawan Halim dan Indra Kusuma tidak tertulis di Pre-setup #17 (hanya nama dan Home Group). Spec ini tidak login sebagai keduanya (hanya sebagai target request) sehingga tidak membutuhkan email atau password; user dirujuk lewat nama.
  - TC-FA-RP-1238 dan 1239 tidak menyebut endpoint, body request, atau bentuk keluaran fixture BE; spec tidak mengarang. Dibutuhkan klien HTTP sesi API aktor dan fixture BE pembaca state penugasan Role Transaksi (serta pencabut penugasan untuk pemulihan), disediakan tim FE/BE.
  - TC-FA-RP-1239 Expected menyebut "respons sukses" tanpa kode status; spec tidak mengarang kode (hanya "bukan `422`").
  - Precondition TC-FA-RP-1238 dan 1239 tidak menyebut bahwa Gunawan Halim dan Indra Kusuma belum punya penugasan Role Transaksi pada node-node itu; spec menetapkannya lewat seeding hook `before`.
  - TC-FA-RP-1239 menulis ke `Rack A1` dan `Dock 1` (Pre-setup #18 bersama), bukan data milik spec (S-06). Spec memulihkan baris hasil request lewat fixture BE (langkah 16 dan hook `after`) dan Prerequisites menyatakan efeknya; bila auditor menilai target harus data milik spec, pindahkan ke Group sementara bersuffix `{runId}-396`.
  - Post Condition TC-FA-RP-1238 dan 1239 kosong ("-").
