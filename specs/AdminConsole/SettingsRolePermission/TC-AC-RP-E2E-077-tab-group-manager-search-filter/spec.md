---
id: TC-AC-RP-E2E-077-tab-group-manager-search-filter
title: "Tab Group Manager: Search, Filter Panel, Filter Status dengan node sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-264
  - TC-AC-RP-265
  - TC-AC-RP-266
coverage:
  web: automated
---

# Tab Group Manager: Search, Filter Panel, Filter Status dengan node sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Data Pre-setup Tab Group Manager (Pre-setup #14), tiga baris: `Fajar Nugroho` — `Region Jawa` ("Bambang H" 11 Jun 2026, 10:30), `Fajar Nugroho` — `Sumatera` ("Siti N" 16 Jun 2026, 09:05), `Jane Smith` — `Region Jawa` (Inactive; "Siti N" 07 Jun 2026, 09:30). Tree group Principal (Pre-setup #11) dipakai oleh Sidebar Group Tree.

## Test Steps

### TC-AC-RP-264: Search Tab Group Manager mencakup kolom Group

1. Klik tab `Group Manager`
2. Ketik Search `sumatera`, tekan Enter
3. Verifikasi baris `Fajar Nugroho` — `Sumatera` tampil
4. Verifikasi tidak ada baris selain `Fajar Nugroho` — `Sumatera`

### TC-AC-RP-265: Filter Panel Tab Group Manager tanpa field Group

5. Klik `(←)` pada kotak Search
6. Klik ikon Filter
7. Verifikasi Filter Panel memuat field Position, Division, Status, Modified By, dan Last Updated
8. Verifikasi Filter Panel tidak memuat field Group

### TC-AC-RP-266: Filter Status Tab Group Manager dikombinasikan dengan node sidebar

9. Klik node `Region Jawa`
10. Pilih Status `Inactive`
11. Klik `[Apply]`
12. Verifikasi baris `Jane Smith` — `Region Jawa` tampil
13. Verifikasi baris `Fajar Nugroho` — `Region Jawa` (Active) tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 5 mengosongkan Search sebelum TC-AC-RP-265 (S-09). Filter Panel dibuka di TC-AC-RP-265 dan dipakai langsung pada TC-AC-RP-266.
- Klausa "(dan field curated bila kolomnya aktif)" pada Expected TC-AC-RP-265 tidak diasersi karena kolom curated tidak diaktifkan di spec ini.
- Temuan untuk QA: TC tidak menyatakan apakah Filter Panel tetap terbuka setelah mengklik node Sidebar Group Tree atau setelah `[Apply]`; spec memakai Filter Panel yang dibuka di TC-AC-RP-265.
