---
id: TC-GS-ROLE-E2E-083-absence-log-assign-total-control-tidak-menulis-changelog-user-role
title: "Absence Log: Assign Total Control Tidak Menulis Entry ke Changelog: User > Role"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-224
coverage:
  web: automated
---

# Absence Log: Assign Total Control Tidak Menulis Entry ke Changelog: User > Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`): Sari Wulandari (#11 kandidat, Active), tanpa access level dan tanpa baris role (Given di hook `before`).
- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). Sari Wulandari bernama literal, sehingga entri log run sebelumnya tetap ada. Baseline dicatat pada langkah 1 dan 2 (sebelum aksi pemicu pada langkah 3) sebagai total entri tab Changelog: User > Role (`B-ROLE`) dan tab Changelog: User (`B-USER`) milik Sari Wulandari (seluruh halaman). Kemampuan membaca total entri pada kedua tab disediakan tim FE.
- Kemampuan teknis: aksi pemicu Assign Total Control dijalankan lewat sesi API atas nama Ahmad Fauzi; aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Sari Wulandari dikembalikan ke tanpa access level dan tanpa baris role (Remove Total Control). Efek pada Pre-setup: Modified By dan Last Updated Sari Wulandari berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### TC-GS-ROLE-224: Assign Total Control tidak menulis entry ke Changelog: User > Role

1. Buka Global Settings > User > Sari Wulandari > Changelog: User > Role, catat total entri sebagai `B-ROLE`
2. Buka Global Settings > User > Sari Wulandari > Changelog: User, catat total entri sebagai `B-USER`
3. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Sari Wulandari (setara TC-GS-ROLE-58 langkah 1 sampai 3)
4. Buka Global Settings > User > Sari Wulandari > Changelog: User
5. Verifikasi total entri sama dengan `B-USER` + 1 (aksi Assign tercatat pada surface Changelog: User)
6. Verifikasi entry baru (teratas): Action `Assign`, Field `Access Level`
7. Buka Global Settings > User > Sari Wulandari > Changelog: User > Role
8. Verifikasi total entri sama dengan `B-ROLE` (tidak ada entry per-role akibat Assign Total Control)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Spec absence (kelas g, bagian 3 konvensi); satu TC sumber, TC-GS-ROLE-224. Pencatatan Assign Total Control di Changelog Tab Total Control diasersi di spec `TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert` (TC-GS-ROLE-207); spec ini tidak mengulangnya.
- Aksi nyata dan baseline sendiri: Assign Total Control dijalankan pada langkah 3 dengan baseline yang dicatat pada langkah 1 dan 2 (S-05, S-12). Anchor positif langkah 8 adalah langkah 5 dan 6 (entry Assign pada Changelog: User milik user yang sama membuktikan aksi sudah selesai dan log sudah dimuat ulang), sebelum langkah 8 membaca Changelog: User > Role.
- Dependensi TC-GS-ROLE-58 dijalankan lewat aksi pemicu sesi API (langkah 3); Given Sari Wulandari tanpa access level dan tanpa baris role terjadi di hook `before` sebelum baseline.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka tab Changelog: User atau Changelog: User > Role (langkah 1, 2, 4, 7); aksi pemicu API (langkah 3).
- Temuan untuk QA:
  - TC-GS-ROLE-224 Expected menyatakan dua hasil sah ("No changelog yet" atau entry lain yang tidak terkait). Spec memakai jumlah entri sama dengan baseline (langkah 8), tidak memverifikasi teks "No changelog yet" karena langkah bersyarat tidak dipakai (S-08) dan baseline Sari Wulandari tidak dijamin nol.
  - TC-GS-ROLE-224 Langkah Uji hanya membuka Changelog: User > Role dan tidak memuat aksi Assign; spec menambahkan aksi pemicu Assign Total Control dari dependensi TC-GS-ROLE-58 supaya asersi absence punya aksi nyata dan baseline.
  - Langkah 5 dan 6 (entry Assign pada Changelog: User) adalah anchor positif tambahan di luar Expected TC-GS-ROLE-224; didasarkan pada TC-GS-ROLE-223 Expected a (Changelog: User memuat entry Assign Access Level).
  - TC-GS-ROLE-224 tidak mendefinisikan cara menghitung entri pada tab Changelog: User > Role dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total entri dengan baseline sebagai kemampuan yang disediakan tim FE.
