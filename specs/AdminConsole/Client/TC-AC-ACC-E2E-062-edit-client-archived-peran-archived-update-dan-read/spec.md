---
id: TC-AC-ACC-E2E-062-edit-client-archived-peran-archived-update-dan-read
title: "Edit Client Archived: Pemegang Update Boleh Edit, Pemegang Read Tanpa Tombol Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-157
  - TC-AC-ACC-546
  - TC-AC-ACC-547
coverage:
  web: automated
---

# Edit Client Archived: Pemegang Update Boleh Edit, Pemegang Read Tanpa Tombol Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Archived-Update-Only (A-09) `archivedUpdateJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ARCHIVED_UPDATE_PASSWORD`; Archived-Read (A-08) `archivedReadJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ARCHIVED_READ_PASSWORD`. Login akun Archived-Update-Only di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed: Client `PT Karya Abadi {runId}-062` (setara C-04: Archived, Group Area Jakarta, dalam assignment exact-match Area Jakarta, PIC Name awal bebas). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-157: Edit Client Archived oleh pemegang Update

1. Klik sub-tab Archived
2. Ketik Search `PT Karya Abadi {runId}-062`, tekan Enter
3. Buka `⋯` baris `PT Karya Abadi {runId}-062` lalu klik `Edit`
4. Verifikasi popup Edit terbuka
5. Ubah PIC Name menjadi "Dewi Lestari"
6. Klik `[Save]`
7. Verifikasi popup tertutup
8. Verifikasi toast sukses "Success, client has been updated."
9. Verifikasi baris "PT Karya Abadi {runId}-062" tetap berada di sub-tab Archived

### TC-546: Header [Edit] di Detail tampil bagi pemegang Update

10. Klik Company Name `PT Karya Abadi {runId}-062` untuk membuka Detail
11. Verifikasi header menampilkan Company Name "PT Karya Abadi {runId}-062" dan badge `Archived`
12. Verifikasi tombol `[Edit]` tampil di pojok kanan atas header
13. Klik `[Edit]`
14. Verifikasi popup Edit Client terbuka dengan Title "Edit Client" dan Company Name "PT Karya Abadi {runId}-062"
15. Klik `[✕]` di header popup

### TC-547: Header [Edit] Hidden bagi pemegang Read

16. `Logout`, lalu login sebagai Archived-Read (A-08)
17. Klik sub-tab Archived
18. Ketik Search `PT Karya Abadi {runId}-062`, tekan Enter
19. Klik Company Name `PT Karya Abadi {runId}-062` untuk membuka Detail
20. Verifikasi header menampilkan Company Name "PT Karya Abadi {runId}-062" dan badge `Archived`
21. Verifikasi tombol `[Edit]` di pojok kanan atas header Hidden

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Ganti akun eksplisit pada TC-547 (Archived-Update-Only ke Archived-Read); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (prinsip 3, beda akun dengan Step ganti akun). Hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (S-03): sub-tab Archived dan Search nama unik; `✕` menutup popup Edit pristine.
- Temuan untuk QA:
  - Post Condition TC-157 ("Kembalikan PIC Name ke nilai semula") adalah pemulihan; cleanup menghapus Client seed lewat hook `after`.
