---
id: TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree
title: "Screening Tab Group Manager dan Sidebar Group Tree: Baris, Hover Path, dan Node"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-18
  - TC-AC-RP-19
  - TC-AC-RP-20
  - TC-AC-RP-21
coverage:
  web: automated
---

# Screening Tab Group Manager dan Sidebar Group Tree: Baris, Hover Path, dan Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`) dan #14 (penugasan GM: `Fajar Nugroho` di `Region Jawa` "Bambang H" 11 Jun 2026, 10:30 dan di `Sumatera` "Siti N" 16 Jun 2026, 09:05; `Jane Smith` di `Region Jawa`, Inactive). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-18: Screening Tab Group Manager

1. Klik tab `Group Manager`
2. Susuri toolbar, tabel, dan panel kanan
3. Verifikasi Toolbar: Search, Filter, Download, Changelog, "+ Assign"
4. Verifikasi kolom default: Name, Group, Position, Division, Status, Modified By, Last Updated, Actions `⋯`
5. Verifikasi 3 baris berurutan Name A-Z: `Fajar Nugroho` — `Region Jawa`, `Fajar Nugroho` — `Sumatera`, `Jane Smith` — `Region Jawa`
6. Verifikasi baris `Jane Smith` — `Region Jawa` berstatus `Inactive`
7. Verifikasi Sidebar Group Tree tampil di kanan dengan node "All Groups" aktif (di-highlight)
8. Verifikasi tidak ada Bulk Action Bar

### TC-AC-RP-19: Satu user GM di dua group tampil sebagai dua baris

9. Verifikasi `Fajar Nugroho` tampil sebagai dua baris terpisah
10. Verifikasi baris `Fajar Nugroho` — `Region Jawa` ber-Modified By "Bambang H" dan Last Updated "11 Jun 2026, 10:30"
11. Verifikasi baris `Fajar Nugroho` — `Sumatera` ber-Modified By "Siti N" dan Last Updated "16 Jun 2026, 09:05"
12. Verifikasi tidak ada baris untuk descendant `Jakarta` atau `Surabaya`

### TC-AC-RP-20: Hover badge Group menampilkan full path

13. Hover badge `Region Jawa` pada kolom Group
14. Verifikasi kolom Group tampil sebagai Badge
15. Verifikasi tooltip menampilkan full path "Region Jawa"

### TC-AC-RP-21: Sidebar Group Tree menampilkan seluruh node entitas tanpa hidden atau greyed out

16. Expand seluruh node di Sidebar Group Tree
17. Verifikasi Tree menampilkan "All Groups" lalu `Default Group`, `Region A` (anak `Branch 1`), `Region Jawa` (anak `Jakarta`, `Surabaya`), `Sumatera`
18. Verifikasi tidak ada node disabled atau greyed out
19. Verifikasi tidak ada badge count per node

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 2 (susur toolbar, tabel, dan panel kanan sebagai prasyarat asersi), langkah 13 (hover badge), dan langkah 16 (expand seluruh node, S-14).
- Asersi absence baris descendant `Jakarta` dan `Surabaya` (langkah 12) memakai tiga baris GM langsung yang diasersi pada langkah sebelumnya sebagai anchor positif (8b butir 2). Asersi tidak ada node disabled dan tidak ada badge count memakai node pohon yang diasersi pada langkah sebelumnya sebagai anchor.
- Temuan untuk QA:
  - TC-AC-RP-20 Expected menyebut tooltip full path "Region Jawa" untuk group tingkat satu; path bertingkat (mis. `Jakarta`) tidak diuji pada TC ini dan tidak ada TC dalam slice ini yang menegaskannya.
  - TC-AC-RP-18 Expected d menyebut "node 'All Groups' aktif (di-highlight)" tanpa kriteria visual; asersi memakai deskripsi TC.
