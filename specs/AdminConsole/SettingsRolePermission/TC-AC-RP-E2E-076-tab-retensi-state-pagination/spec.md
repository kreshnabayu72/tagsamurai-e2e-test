---
id: TC-AC-RP-E2E-076-tab-retensi-state-pagination
title: "Retensi state tab: pindah tab, F5, Back, reset paginasi, Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-259
  - TC-AC-RP-260
  - TC-AC-RP-261
coverage:
  web: automated
---

# Retensi state tab: pindah tab, F5, Back, reset paginasi, Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Role Detail `Manage distributor` (Group Role) dipakai pada TC-AC-RP-260; Tab Group Manager dan Role Detail `Manage language` (Global Role) pada TC-AC-RP-261. Data Pre-setup #11, #14, #15.

## Test Steps

### TC-AC-RP-259: Pindah tab membuka tab tujuan dengan state default

1. Ketik Search `finance`, tekan Enter
2. Klik header Name dua kali (sort Name Z-A)
3. Klik tab `Read Only`
4. Verifikasi Tab Read Only terbuka dengan Search, Filter, Sort, dan Pagination default
5. Klik tab `Total Control`
6. Verifikasi Tab Total Control menampilkan Search, Filter, Sort, dan Pagination default

### TC-AC-RP-261: Tab aktif dan node sidebar setelah F5 atau Back dari Role Detail

7. Klik tab `Group Manager`
8. Klik node `Sumatera`
9. Tekan F5
10. Verifikasi Tab Group Manager tetap aktif
11. Verifikasi node `Sumatera` tetap terpilih
12. Klik tab `System`
13. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
14. Klik segmen "System" pada Breadcrumb
15. Verifikasi Tab System tetap aktif

### TC-AC-RP-260: Search, Filter, Sort, Pagination dipertahankan setelah F5

16. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
17. Ketik Search `a`, tekan Enter
18. Klik ikon Filter
19. Pilih Division `Operations`
20. Klik `[Apply]`
21. Klik header Name dua kali (sort Name Z-A)
22. Pindah ke halaman 2
23. Tekan F5
24. Verifikasi Search `a` tetap seperti sebelum refresh
25. Verifikasi Filter Division `Operations` tetap seperti sebelum refresh
26. Verifikasi Sort Name Z-A tetap seperti sebelum refresh
27. Verifikasi halaman 2 tetap aktif seperti sebelum refresh

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Penyimpangan urutan: TC-AC-RP-261 dijalankan sebelum TC-AC-RP-260 karena langkah terakhir TC-AC-RP-261 (Breadcrumb ke Tab System, langkah 14) menyisakan Tab System aktif sebagai awal TC-AC-RP-260; langkah "Klik tab `System`" TC-AC-RP-260 tidak diulang karena tab sudah aktif.
- Pembagian TC lintas spec: TC-AC-RP-262 dan TC-AC-RP-263 (reset paginasi dan pilihan Pagination Role Detail) ada di spec 130.
- Temuan untuk QA:
  - TC-AC-RP-260 memilih halaman 2 sesudah Search `a` dan Filter Division `Operations` pada Role Detail `Manage distributor`; jumlah baris hasil gabungan Search dan Filter belum tentu melebihi 10 sehingga halaman 2 belum tentu tersedia. Spec mengikuti urutan TC; QA perlu memastikan data uji yang menjamin halaman 2.
  - TC-AC-RP-259 Expected tidak menyebut state Filter yang diisi sebelum pindah tab (langkah TC hanya mengisi Search dan Sort).
