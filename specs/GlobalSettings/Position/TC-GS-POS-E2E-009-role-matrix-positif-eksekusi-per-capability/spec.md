---
id: TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Create, Edit, Delete, dan Bulk Delete Position oleh Aktor Capability Spesifik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-32
  - TC-GS-POS-33
  - TC-GS-POS-34
  - TC-GS-POS-35
coverage:
  web: automated
---

# Role Matrix Positif: Create, Edit, Delete, dan Bulk Delete Position oleh Aktor Capability Spesifik

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec Role Matrix positif (bagian 3a konvensi): aksi berhasil oleh role yang berhak. Tiap TC memakai role berbeda sehingga ada langkah ganti akun eksplisit. Password tidak ditulis di spec atau fixture.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Aksi | Role | Email | Env var password |
|---|---|---|---|---|
| TC-GS-POS-32 | Create | Manage user and role: Create-Only (Sari Dewi) | `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5) | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-POS-33 | Edit | Manage user and role: Update-Only | `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 6) | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-POS-34 | Delete single | Manage user and role: Delete-Only | `manageUserRoleDelete_automated_{namaCompany}@qwertysystem.net` (Pre-setup 7) | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-POS-35 | Bulk Delete | Manage user and role: Delete-Only | `manageUserRoleDelete_automated_{namaCompany}@qwertysystem.net` (Pre-setup 7) | `Spectra.env.GS_DELETE_PASSWORD` |

- Akun aktor pertama (Create-Only) login di hook `before`; akun berikutnya login lewat langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Layar awal Global Settings > User > Position dibuka hook `beforeEach` untuk akun pertama; sesudah ganti akun, layar dibuka lagi lewat langkah eksplisit.
- Data Dinamis (nama bersuffix per run; milik spec ini, tidak menumpang spec lain):
  - `Procurement Analyst {runId}-009`: dibuat lewat UI oleh Create-Only pada TC-GS-POS-32 (record ini tidak dipakai TC berikutnya).
  - `Procurement Analyst Edit {runId}-009`: di-seed lewat API di hook `before`, diubah menjadi `Procurement Lead Edit {runId}-009` pada TC-GS-POS-33.
  - `Procurement Lead {runId}-009`: di-seed lewat API di hook `before`, dihapus pada TC-GS-POS-34.
  - `Office Administrator {runId}-009` dan `Security Officer {runId}-009`: di-seed lewat API di hook `before` (setara TC dependensi TC-GS-POS-53), bebas relasi, dihapus pada TC-GS-POS-35.
  - Seeding memakai Fixture baru `Fixture.position.roleMatrixSeed009`; seeding dipakai sebagai precondition TC, tidak diasersi.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Procurement Analyst {runId}-009`, `Procurement Analyst Edit {runId}-009`, `Procurement Lead Edit {runId}-009`, `Procurement Lead {runId}-009`, `Office Administrator {runId}-009`, dan `Security Officer {runId}-009` bila masih ada; kembalikan sesi ke akun default suite.
- Kemampuan teknis: ganti akun (logout lalu login); pencarian di tabel dengan Search.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-POS-32: Create Position oleh aktor capability Create saja

1. Klik `[+ Position]`
2. Ketik Position Name `Procurement Analyst {runId}-009`
3. Klik `[Submit]`
4. Verifikasi muncul toast sukses: "Success, position has been created."
5. Verifikasi popup tertutup
6. Ketik Search `{runId}-009`, tekan Enter
7. Verifikasi baris `Procurement Analyst {runId}-009` tampil di tabel

### TC-GS-POS-33: Edit Position oleh aktor capability Update saja

8. Ganti akun: logout, lalu login sebagai Manage user and role: Update-Only
9. Buka Global Settings > User > Position
10. Ketik Search `{runId}-009`, tekan Enter
11. Klik `⋯` pada baris `Procurement Analyst Edit {runId}-009`, pilih `Edit`
12. Ubah Position Name menjadi `Procurement Lead Edit {runId}-009`
13. Klik `[Save]`
14. Verifikasi muncul toast sukses: "Success, position has been updated."
15. Verifikasi popup tertutup
16. Verifikasi baris tampil sebagai `Procurement Lead Edit {runId}-009`

### TC-GS-POS-34: Delete single Position oleh aktor capability Delete saja

17. Ganti akun: logout, lalu login sebagai Manage user and role: Delete-Only
18. Buka Global Settings > User > Position
19. Ketik Search `{runId}-009`, tekan Enter
20. Klik `⋯` pada baris `Procurement Lead {runId}-009`, pilih `Delete`
21. Pada Dialog Delete Position klik `[Delete]`
22. Verifikasi muncul toast sukses: "Success, position has been deleted."
23. Verifikasi baris `Procurement Lead {runId}-009` hilang dari tabel

### TC-GS-POS-35: Bulk Delete Position oleh aktor capability Delete saja

24. Centang baris `Office Administrator {runId}-009` dan `Security Officer {runId}-009`
25. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
26. Pada Dialog Delete Position klik `[Delete]`
27. Verifikasi muncul toast sukses: "Success, position has been deleted."
28. Verifikasi baris `Office Administrator {runId}-009` hilang dari tabel
29. Verifikasi baris `Security Officer {runId}-009` hilang dari tabel
30. Verifikasi Bulk Action Bar hilang

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti TC sumber (32, 33, 34, 35). Rantai dependensi TC-GS-POS-32 ke 33 ke 34 tidak dijalankan sebagai rantai: record yang dibutuhkan TC-GS-POS-33 (`Procurement Analyst Edit {runId}-009`) dan TC-GS-POS-34 (`Procurement Lead {runId}-009`) di-seed lewat API di hook `before` (S-04) supaya tiap TC berdiri sendiri dan bernama berbeda dari record hasil TC-GS-POS-32. Aksi yang menghapus data (TC-GS-POS-34 dan 35) berada di akhir.
- Tabel difilter dengan Search `{runId}-009` supaya baris spec ini mudah ditemukan; Search dimulai dari state bersih pada tiap akun karena ganti akun membuka sesi baru. Kolom Position Name berisi nama bersuffix yang unik per spec. Baris dipilih lewat nama lengkap karena beberapa baris spec ini tampil bersamaan pada hasil Search.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): ganti akun (langkah 8 dan 17), buka Position sesudah login akun baru (langkah 9 dan 18), Search (langkah 6, 10, 19) untuk menemukan baris.
- Langkah 24 sampai 25 mengikuti TC-GS-POS-35 (`Bulk Action` pada Bulk Action Bar, lalu `Delete`).
- Temuan untuk QA:
  - Post Condition TC-GS-POS-32, 33, 34, dan 35 ("Changelog: Position mencatat entri ... dengan Modified By = aktor") tidak punya langkah observasi di TC, sehingga tidak diasersi (S-01). Pencatatan entri Changelog dan Modified By diuji di spec 044.
  - TC-GS-POS-33 mensyaratkan record `Procurement Analyst` ada dari TC-GS-POS-32 tanpa menyebut aktor yang membuatnya; spec membuat record TC-GS-POS-32 oleh aktor Create-Only di blok TC-GS-POS-32 dan men-seed record TC-GS-POS-33 secara terpisah.
  - Nama seed `Procurement Analyst Edit {runId}-009` dan `Procurement Lead {runId}-009` adalah pilihan editor spec untuk memisahkan record TC-GS-POS-33 dan 34 dari record hasil TC-GS-POS-32; rantai TC-GS-POS-32 ke 33 ke 34 di TC tidak dijalankan sebagai rantai.
  - TC-GS-POS-35 dependensi TC-GS-POS-53 membuat sepuluh Position; spec hanya menyiapkan dua Position (`Office Administrator` dan `Security Officer`) yang dipakai TC.
