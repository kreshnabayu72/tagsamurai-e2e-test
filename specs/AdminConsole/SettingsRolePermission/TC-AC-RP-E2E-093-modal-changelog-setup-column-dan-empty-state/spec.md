---
id: TC-AC-RP-E2E-093-modal-changelog-setup-column-dan-empty-state
title: "Modal Changelog: Setup Column, Pagination, dan Empty State"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-312
  - TC-AC-RP-313
coverage:
  web: automated
---

# Modal Changelog: Setup Column, Pagination, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec: Wulan Sari, Default User entitas Partner `Partner Mandiri` (`defaultUserPartRP_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RP_PART_DU_PASSWORD`) untuk TC-AC-RP-313. Entitas `Partner Mandiri` tanpa entri Changelog Read Only (Pre-setup #19).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed). Pre-setup #19 (`Partner Mandiri`, pohon group `Default Group`).
- Pemulihan Setup Column: preferensi kolom Changelog yang disimpan TC-AC-RP-312 dihapus di hook `after` (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD`, `AC_RP_PART_DU_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-312: Setup Column dan Pagination Changelog

1. Klik ikon Changelog
2. Buka Column Visibility dan sembunyikan Old Value
3. Verifikasi kolom Old Value tersembunyi
4. Buka pilihan baris per halaman
5. Verifikasi pilihan baris per halaman 10, 25, 50, dan 100 tersedia
6. Pilih 25 baris per halaman
7. Verifikasi Pagination mengikuti pilihan 25
8. Tutup modal Changelog

### TC-AC-RP-313: Empty state Changelog

9. Ganti akun: Logout, lalu login sebagai `Wulan Sari` (`defaultUserPartRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_PART_DU_PASSWORD`)
10. Klik menu `Settings > Role & Permission` di sidebar
11. Klik tab `Read Only`
12. Klik ikon Changelog
13. Verifikasi empty state dengan Title "No changelog yet" dan Description "Activities and changes will appear here."
14. Tutup modal Changelog
15. Klik tab `Total Control`
16. Klik ikon Changelog
17. Ketik Search "zzz", tekan Enter
18. Verifikasi empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
19. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 8, 10, 14, 19.
- Ganti akun eksplisit pada langkah 9: TC-AC-RP-313 mensyaratkan Default User entitas Partner; login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun (S-07).
- Empty state Title dan Description disebut utuh dalam satu butir Expected TC sehingga ditulis satu Verifikasi (S-01); Expected b TC-AC-RP-313 memakai empty state hasil Search sebagai anchor positif.
- Daftar pilihan baris per halaman (10/25/50/100) diverifikasi sebelum memilih 25 karena Expected menyebut keduanya.
- Temuan untuk QA:
  - TC-AC-RP-313 langkah 4 "Search 'zzz' lalu Enter pada varian Total Control" tidak konsisten dengan langkah 2 dan 3 yang membuka varian Read Only dan tidak menyatakan entri Changelog Total Control `Partner Mandiri`; spec membuka varian Total Control sebagai Wulan Sari. Bila Changelog Total Control entitas ini kosong, hasilnya "No changelog yet", bukan "No results found".
  - Email akun Wulan Sari tertulis di Pre-setup #9; password env `AC_RP_PART_DU_PASSWORD` adalah nama baru.
