---
id: TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama
title: "Screening Tab Total Control: Tooltip Toolbar, Breadcrumb per Tab, Tanpa Bulk Action, dan Klik Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-11
  - TC-AC-RP-12
  - TC-AC-RP-13
  - TC-AC-RP-14
coverage:
  web: automated
---

# Screening Tab Total Control: Tooltip Toolbar, Breadcrumb per Tab, Tanpa Bulk Action, dan Klik Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal) dan #13 (pemegang Total Control, termasuk `John Doe`). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-11: Tooltip ikon toolbar Tab Total Control

1. Hover ikon Search
2. Verifikasi tooltip "Search" tampil
3. Hover ikon Filter
4. Verifikasi tooltip "Filter" tampil
5. Hover ikon Download
6. Verifikasi tooltip "Download" tampil
7. Hover ikon Changelog
8. Verifikasi tooltip "Changelog" tampil

### TC-AC-RP-12: Breadcrumb mengikuti tab aktif dan segmen terakhir bukan link

9. Klik tab `Read Only`
10. Verifikasi Breadcrumb menjadi "Settings > Role & Permission > Read Only"
11. Klik tab `Group Manager`
12. Verifikasi Breadcrumb menjadi "Settings > Role & Permission > Group Manager"
13. Klik tab `System`
14. Verifikasi Breadcrumb menjadi "Settings > Role & Permission > System"
15. Verifikasi segmen terakhir Breadcrumb (tab aktif) bukan link
16. Klik segmen terakhir Breadcrumb
17. Verifikasi klik tidak berpindah halaman: Breadcrumb tetap "Settings > Role & Permission > System" dan Tab System tetap aktif
18. Klik tab `Total Control`

### TC-AC-RP-13: Tidak ada bulk action dan checkbox pada Tab Total Control

19. Verifikasi tabel Tab Total Control menampilkan sedikitnya satu baris
20. Verifikasi tabel tidak memiliki kolom Checkbox multi-select
21. Verifikasi Bulk Action Bar tidak tampil

### TC-AC-RP-14: Klik Name pada tabel tidak membuka halaman detail

22. Klik teks Name `John Doe`
23. Verifikasi tidak ada navigasi atau popup: Tab Total Control tetap tampil dengan Breadcrumb "Settings > Role & Permission > Total Control"
24. Verifikasi Name tidak berupa link

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 18 mengembalikan Tab Total Control aktif setelah TC-AC-RP-12 agar TC-AC-RP-13 dan TC-AC-RP-14 mulai dari tab yang sama dengan TC sumber (S-09).
- Verifikasi tabel menampilkan sedikitnya satu baris (langkah 19) adalah anchor positif absence untuk kolom Checkbox dan Bulk Action Bar (8b butir 2); bukan asersi tambahan atas Expected TC.
- Verifikasi segmen terakhir Breadcrumb bukan link ditaruh sebelum klik (8b.5) dan klik segmen terakhir diasersi setelahnya; kedua klausa Expected b TC-AC-RP-12 tetap terpenuhi.
- Verifikasi "Name tidak berupa link" pada TC-AC-RP-14 berasal dari klausa alasan Expected ("Name bukan link"); ditulis sebagai asersi karena TC-AC-RP-3 juga menegaskannya.
- Temuan untuk QA:
  - TC-AC-RP-11 hanya menyebut tooltip tanpa menyatakan keadaan Search sebelum hover; spec mengasumsikan kotak Search tertutup.
  - TC-AC-RP-14 tidak menyatakan cara mengamati "tidak ada navigasi"; spec memakai Breadcrumb dan tab aktif tetap sama.
