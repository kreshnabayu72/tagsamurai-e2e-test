---
id: TC-AC-ACC-E2E-061-edit-peran-active-update-only-sukses-dan-tree-exact-match
title: "Active-Update-Only: Edit Client Sampai Sukses dan Tree Select Group Exact-Match"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-586
  - TC-AC-ACC-588
coverage:
  web: automated
---

# Active-Update-Only: Edit Client Sampai Sukses dan Tree Select Group Exact-Match

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Update-Only (A-06) `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_PASSWORD`. Login akun Active-Update-Only di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Assignment A-06 hanya pada node Area Jakarta (exact-match).
- Dataset seed: Client `PT Ubah Mitra 02 {runId}-061` (setara C-ROL-8, Fax kosong) dan `PT Direct Jakarta {runId}-061` (setara C-ROL-13, Direct, Group Area Jakarta). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-586: Edit Client Active sampai sukses

1. Ketik Search `PT Ubah Mitra 02 {runId}-061`, tekan Enter
2. Buka `⋯` baris `PT Ubah Mitra 02 {runId}-061` lalu klik `Edit`
3. Verifikasi popup dengan Title "Edit Client" terbuka
4. Isi Fax dengan `0215550142`
5. Klik `[Save]`
6. Verifikasi popup tertutup
7. Verifikasi toast sukses "Success, client has been updated."
8. Klik Company Name `PT Ubah Mitra 02 {runId}-061` untuk membuka Detail
9. Verifikasi Detail menampilkan Fax "0215550142"
10. Klik breadcrumb "Client" untuk kembali ke List

### TC-588: Tree Select Group Client Direct exact-match

11. Ketik Search `PT Direct Jakarta {runId}-061`, tekan Enter
12. Buka `⋯` baris `PT Direct Jakarta {runId}-061` lalu klik `Edit`
13. Verifikasi field Select Group tampil terisi "Area Jakarta"
14. Buka tree Select Group
15. Verifikasi "Area Jakarta" dapat dipilih
16. Verifikasi "Regional Barat" greyed out
17. Verifikasi "Cabang Menteng" tidak muncul (descendant hidden)
18. Klik node "Regional Barat"
19. Verifikasi field Select Group tetap "Area Jakarta"
20. Klik `[✕]` di header popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Detail dan breadcrumb "Client"; penutup popup Edit TC-588 memakai `[✕]` karena Group tidak berubah (form tidak dirty).
- Temuan untuk QA:
  - Post Condition TC-586 butir b (Changelog `Edit` Field `Fax` tercatat) tidak punya langkah observasi di TC; tidak diasersi.
