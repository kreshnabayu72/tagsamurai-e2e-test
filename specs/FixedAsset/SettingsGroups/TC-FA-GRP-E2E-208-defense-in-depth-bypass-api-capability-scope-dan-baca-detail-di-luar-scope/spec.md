---
id: TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope
title: "Defense-in-Depth: Request Langsung ke API oleh Aktor Tanpa Capability atau di Luar Scope (Create, Add Subgroup, Edit, Delete, Baca Detail)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-917
  - TC-FA-GRP-918
  - TC-FA-GRP-919
  - TC-FA-GRP-920
  - TC-FA-GRP-921
  - TC-FA-GRP-922
  - TC-FA-GRP-923
  - TC-FA-GRP-924
  - TC-FA-GRP-925
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung ke API oleh Aktor Tanpa Capability atau di Luar Scope (Create, Add Subgroup, Edit, Delete, Baca Detail)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Spec ini tidak membuka UI untuk aksi uji; seluruh request dikirim lewat klien HTTP dengan token sesi API aktor pada tabel (login API password, tidak dihitung sebagai sesi web). Env password aktor di bawah adalah nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (dibaca; request ditolak sehingga tidak ada perubahan): pohon group Tabel A: Region West, Branch West 1, Region East, Global HQ. Aktor Manage Group R+U dan R+C berscope Region West tidak tertulis lengkap di Pre-setup No 6 (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP untuk request langsung ke server dengan token sesi aktor; fixture BE untuk membaca state data group sebelum dan sesudah request.

  | Aktor (Pre-setup) | Env password | Request langsung ke API | Hasil yang diharapkan |
  |---|---|---|---|
  | Group Manager scope Region West (No 4) `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `FA_GM_PASSWORD` | create level 1 (tanpa parent) | ditolak server; tidak ada group dibuat (FAGRP-LOGIC-06) |
  | Manage Group CRUD scope Region West (No 5) `manageGroupCrud_automated_{namaCompany}@qwertysystem.net` | `FA_MGCRUD_PASSWORD` | create level 1 | ditolak server (Manage Group C tidak berlaku untuk level 1) |
  | Read Only (No 3) `readOnlyGroups_automated_{namaCompany}@qwertysystem.net` | `FA_RO_PASSWORD` | create subgroup | ditolak server |
  | Manage Group R+U scope Region West (No 6) `manageGroupUpdate_automated_{namaCompany}@qwertysystem.net` | `FA_MGRU_PASSWORD` | Add Subgroup di Region West | ditolak server (tanpa C) |
  | Manage Group R+C scope Region West (No 6) `manageGroupCreate_automated_{namaCompany}@qwertysystem.net` | `FA_MGRC_PASSWORD` | Edit Branch West 1 | ditolak server (tanpa U) |
  | Manage Group R+U scope Region West (No 6) `manageGroupUpdate_automated_{namaCompany}@qwertysystem.net` | `FA_MGRU_PASSWORD` | Delete Branch West 1 | ditolak server (tanpa D) |
  | Group Manager scope Region West (No 4) | `FA_GM_PASSWORD` | Edit Region East (di luar scope) | ditolak server |
  | Group Manager scope Region West (No 4) | `FA_GM_PASSWORD` | Delete Global HQ (ancestor context) | ditolak server |
  | Group Manager scope Region West (No 4) | `FA_GM_PASSWORD` | baca detail/popup Region East | ditolak server; data tidak dikembalikan |

## Test Steps

1. Untuk setiap baris tabel Prerequisites (langkah 1 sampai 4): Catat state data target request lewat fixture BE
2. Kirim request pada kolom Request langsung ke API dengan token sesi API aktor pada baris tabel
3. Verifikasi respons ditolak server sesuai kolom Hasil yang diharapkan
4. Verifikasi state data target tidak berubah dibanding yang dicatat lewat fixture BE

## Notes

- K-1: seluruh TC di spec ini kelas a (defense-in-depth) dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec (BE mencatatnya pada tingkat endpoint). Asersi hanya status respons dan state data lewat fixture BE (8b butir 1).
- Langkah 1 sampai 4 berulang untuk setiap baris tabel Prerequisites (9 baris, satu per TC: TC-917 sampai 925 berurutan); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7). Kode status tidak disebut TC selain "ditolak server", sehingga asersi memakai penolakan tanpa kode tertentu.
- Spec memiliki 4 langkah nominal dan 36 langkah setelah ekspansi (9 iterasi x 4 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) dengan langkah identik tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - Pre-setup No 6 menyebut `manageGroupUpdate_automated_…` (R+U) dan `manageGroupCreate_automated_…` (R+C) tanpa scope; TC-920 sampai 922 menyebut scope Region West. Scope dan email penuh disediakan tim FE.
  - Kode status respons tidak ditulis TC-917 sampai 925 (hanya "ditolak server"); spec tidak mengarang kode.
