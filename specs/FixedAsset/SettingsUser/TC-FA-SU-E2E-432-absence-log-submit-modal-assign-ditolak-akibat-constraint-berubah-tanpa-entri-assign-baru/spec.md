---
id: TC-FA-SU-E2E-432-absence-log-submit-modal-assign-ditolak-akibat-constraint-berubah-tanpa-entri-assign-baru
title: "Absence Log: Submit Modal Assign Transaction Role yang Ditolak karena Constraint Berubah Tidak Menulis Entri Assign Baru di Tab Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1123
coverage:
  web: automated
---

# Absence Log: Submit Modal Assign Transaction Role yang Ditolak karena Constraint Berubah Tidak Menulis Entri Assign Baru di Tab Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Sesi A): Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dan sesi API aktor dinyatakan di `suite.md`.
- Pelaku kedua (Sesi B): Admin B (Pre-setup #13, Total Control lain) lewat sesi API untuk Edit Home Group; hanya memicu perubahan state dan tidak ada sesi UI kedua. Kemampuan sesi API Admin B dan kredensialnya disediakan tim FE/BE; Pre-setup TC dan `suite.md` tidak memuat email maupun nama env password akun ini (lihat Temuan untuk QA).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Pre-setup #50 (`FaUserNoHG`). Target: Gita Permata tanpa Home Group pada awal skenario (Home Group dikosongkan lewat seed API di hook `before`; pengguna lain tidak diubah), dengan seluruh penugasan Gita Permata berada di Finance & Accounting. Seed #50 belum tersedia dan disediakan tim FE/BE.
- Data uji: Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report; Home Group baru Gita Permata dari Sesi B: Finance & Accounting.
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): sesi API Admin B untuk Edit Home Group Gita Permata; pembacaan jumlah entri `Assign` pada Tab Changelog Gita Permata sebelum aksi sebagai baseline (audit trail permanen: N tidak diturunkan dari seeding, bagian 8b butir 10). Entri log muncul eventual: Tab Changelog dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global dan pemulihan: Home Group Gita Permata berubah dari kosong menjadi Finance & Accounting oleh langkah 6 (beserta Last Updated dan entri `Edit Home Group`). Dipulihkan ke Pre-setup #50 (Gita Permata tanpa Home Group) lalu ke Pre-setup #20 lewat seed API pada langkah 15 dan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1123 (butir c, log): Submit yang ditolak karena constraint berubah tidak menulis entri Assign baru

1. Catat baseline: jumlah entri `Assign` pada Tab Changelog Gita Permata
2. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik `[+ Assign]`
5. Pilih Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report tanpa klik `[Submit]`
6. Sesi API Admin B: Edit Home Group Gita Permata ke Finance & Accounting hingga tersimpan
7. Sesi A: klik `[Submit]`
8. Verifikasi modal Assign tetap terbuka
9. Klik `[×]` pada modal Assign
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Klik Tab Changelog, lalu muat ulang sampai entri `Edit Home Group` tampil
13. Verifikasi Tab Changelog Gita Permata memuat entri `Edit Home Group` untuk aksi Admin B
14. Verifikasi jumlah entri `Assign` pada Tab Changelog Gita Permata sama dengan baseline langkah 1
15. Pulihkan Gita Permata ke Pre-setup #50 lalu ke Pre-setup #20 lewat seed API

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan prinsip 13g: TC-FA-SU-1123 terbelah antara asersi fungsional dan absence. Butir a (Edit Home Group Sesi B tersimpan tanpa dialog) dan butir b (penolakan 422 `V-09`, pilihan stale dibersihkan, modal tetap terbuka) serta klausa "tidak ada baris Transfer × Monitoring & Report pada Sub-tab Transaction Role" butir c ada di spec 426. Spec ini memuat aksi nyata yang sama (Sesi A membuka modal, Sesi B mengubah Home Group, Sesi A Submit) dengan baseline sendiri dan hanya mengasersi "tidak ada entri `Assign` baru" pada Tab Changelog (Langkah Uji 4 TC). Rujukan yang sama ada di `## Notes` spec 426.
- Sesi B lewat sesi API (R-20): Admin B hanya memicu perubahan state (Edit Home Group), sehingga tidak ada konteks UI kedua dan tidak memakai `P-2`. TC-FA-SU-1123 berlabel Manual Only (dua sesi paralel); label itu bukan alasan mengeluarkan TC, sehingga spec ditulis dengan `coverage.web: automated`.
- Anchor positif (bagian 8b butir 2): `Verifikasi` modal Assign tetap terbuka (langkah 8, klausa Expected b yang tidak bergantung bentuk tampilan pesan) membuktikan Submit diproses server dan ditolak. Pada Tab Changelog, entri `Edit Home Group` dari Admin B (langkah 13) adalah anchor pada surface yang sama sesudah muat ulang (R-21); jumlah entri `Assign` dibandingkan dengan baseline langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (baseline, S-12), langkah 2 (Search untuk menemukan baris target, R-16, R-23), langkah 3 (membuka Sub-tab), langkah 9 dan 11 (menutup modal dirty deterministik, S-08; `Verifikasi` dialog langkah 10 diwajibkan S-08), langkah 12 (membuka Tab Changelog dan memuat ulang), dan langkah 15 (pemulihan, S-09). Langkah 7 adalah pemicu Submit.
- Sisa pilihan stale di modal sesudah penolakan (Transaction Transfer dan Role Monitoring & Report tetap terpilih) membuat form tetap berbeda dari keadaan awal, sehingga langkah 9 memicu dialog `Unsaved Changes`; langkah 10 mengasersinya.
- Temuan untuk QA:
  - TC-FA-SU-1123 berlabel Manual Only (d) dua sesi; direncanakan otomatis dengan Admin B lewat sesi API. Mohon dikonfirmasi bila TC dimaksudkan tetap manual (maka dicatat `coverage.web: unsupported`).
  - Pre-setup #50 didefinisikan global (seluruh 25 pengguna tanpa Home Group), sedangkan TC ini hanya membutuhkan Gita Permata tanpa Home Group; spec mengosongkan Home Group Gita Permata saja lewat seed API dan memulihkannya. Mohon dikonfirmasi bila #50 harus diterapkan penuh (state global berat, suite serial).
  - NC-27: bentuk tampilan penolakan 422 `V-09` (toast atau inline) belum ditetapkan; Expected b TC tidak meng-assert bentuknya dan spec ini tidak mengasersi pesan maupun bentuknya.
  - TC tidak menyebut kredensial Admin B (Pre-setup #13); spec tidak membuat nama env baru dan menuliskan kebutuhan itu di Prerequisites. Mohon didaftarkan.
  - Expected butir c menyebut "entri `Assign` baru" tanpa surface; spec membaca Tab Changelog Gita Permata mengikuti Langkah Uji 4 TC dan tidak membaca modal Changelog per sub-tab.
  - Precondition TC tidak menyebut bahwa seluruh penugasan Gita Permata berada di Finance & Accounting, padahal Expected a mengandalkannya; spec menulis syarat itu di Prerequisites dan tidak mengasersi butir a.
  - TC menyebut pilihan stale "dibersihkan" tanpa menyebut bagian yang tetap terpilih; spec mengandalkan form tetap dirty untuk langkah 9 dan 10. Bila form tidak dirty, dialog `Unsaved Changes` tidak tampil dan langkah 10 gagal.
  - Seed Pre-setup #50 (`FaUserNoHG`) untuk Gita Permata, kunci fixture, dan kemampuan baca jumlah entri `Assign` disediakan tim FE/BE.
