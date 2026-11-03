---
id: TC-AC-RP-E2E-130-role-detail-reset-paginasi-dan-pilihan-pagination
title: "Role Detail: Search atau Apply Filter mereset paginasi ke halaman 1 dan pilihan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-262
  - TC-AC-RP-263
coverage:
  web: automated
---

# Role Detail: Search atau Apply Filter mereset paginasi ke halaman 1 dan pilihan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Role Detail `Manage distributor` (Group Role) memuat 12 user (kolom Users Tab System, TC-AC-RP-272), sehingga halaman 2 tersedia pada ukuran halaman bawaan 10 tanpa Search atau Filter (Pre-setup #15).

## Test Steps

### TC-AC-RP-262: Search atau Apply Filter mereset paginasi ke halaman 1

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
3. Pindah ke halaman 2
4. Ketik Search `o`, tekan Enter
5. Verifikasi halaman aktif kembali ke halaman 1 setelah Search
6. Pindah ke halaman 2
7. Klik ikon Filter
8. Pilih Division `Operations`
9. Klik `[Apply]`
10. Verifikasi halaman aktif kembali ke halaman 1 setelah Apply
11. Klik segmen "System" pada Breadcrumb

### TC-AC-RP-263: Pagination pilihan 10, 25, 50, 100

12. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
13. Verifikasi Pagination default 10 baris per halaman
14. Verifikasi pilihan Pagination hanya 10, 25, 50, dan 100 tanpa opsi "All"
15. Pilih 25 baris per halaman
16. Verifikasi indikator ukuran halaman menampilkan 25
17. Pilih 50 baris per halaman
18. Verifikasi indikator ukuran halaman menampilkan 50
19. Pilih 100 baris per halaman
20. Verifikasi indikator ukuran halaman menampilkan 100

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 11 kembali ke Tab System sehingga TC-AC-RP-263 membuka Role Detail dari keadaan default (Search `o` dan Filter TC-AC-RP-262 tidak terbawa).
- Pembagian TC lintas spec: TC-AC-RP-259, 260, dan 261 (retensi state tab dan F5) ada di spec 076.
- Temuan untuk QA:
  - TC-AC-RP-263 Expected "jumlah baris mengikuti pilihan 25/50/100": Role Detail `Manage distributor` memuat 12 user sehingga jumlah baris tampil tidak membedakan pilihan 25, 50, dan 100; spec hanya mengasersi indikator ukuran halaman terpilih (langkah 16, 18, 20). Pengujian jumlah baris per opsi membutuhkan spec kelas e dengan data lebih dari 100 user.
  - TC-AC-RP-262 memindahkan halaman 2 sesudah Search `o`; jumlah baris hasil Search belum tentu melebihi 10 sehingga halaman 2 belum tentu tersedia.
  - TC tidak menyatakan apakah state Search dan Filter Role Detail terbawa setelah halaman ditinggalkan lewat Breadcrumb; spec berasumsi default.
