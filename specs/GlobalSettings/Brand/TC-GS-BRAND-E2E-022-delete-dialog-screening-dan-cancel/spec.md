---
id: TC-GS-BRAND-E2E-022-delete-dialog-screening-dan-cancel
title: "Screening Row Action dan Dialog Delete Brand serta Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-92
  - TC-GS-BRAND-93
  - TC-GS-BRAND-94
  - TC-GS-BRAND-98
coverage:
  web: automated
---

# Screening Row Action dan Dialog Delete Brand serta Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data pre-setup (data environment tetap, tidak diubah atau dihapus spec ini): brand Client A `Orion Tech` (bebas relasi) dan `Tagline Co` (hanya dipakai 2 TAG di all-tags sebagai snapshot nama, tidak menghalangi hapus). Fixture belum ada; tim FE menyiapkan `fixtures/brand.json` dengan kunci `orionTech` dan `taglineCo`.
- Data dinamis: tidak ada. Semua kasus berakhir dengan Cancel, sehingga tidak ada data tercipta atau terhapus dan tidak ada cleanup. Hook `beforeEach`: tutup dialog atau overlay yang terbuka lalu kembali ke Global Settings > Master Reference > Brand.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-BRAND-92: Screening overlay row action

1. Buka Global Settings > Master Reference > Brand, lalu cari baris Orion Tech (lewat pagination atau Search)
2. Klik `⋯` baris Orion Tech → overlay row action tampil
3. Verifikasi overlay berisi tiga opsi `Detail`, `Edit`, `Delete` dengan icon sesuai `prd-conventions.md` §23.2
4. Verifikasi opsi `Delete` berseverity danger
5. Verifikasi tidak ada opsi yang disabled

### TC-GS-BRAND-93: Screening dialog Delete Brand bebas relasi

6. Klik `Delete` pada overlay baris Orion Tech → dialog Delete Brand tampil
7. Verifikasi Title dialog `Delete Brand` (danger)
8. Verifikasi Body: bullet `• Orion Tech`, lalu teks `Are you sure you want to delete it? This action cannot be undone.`
9. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Delete]` (filled, danger)

### TC-GS-BRAND-94: Cancel dialog Delete tidak menghapus

10. Klik [Cancel]
11. Verifikasi dialog tertutup tanpa toast
12. Verifikasi Orion Tech tetap di tabel

### TC-GS-BRAND-98: Delete Brand yang hanya dipakai tag all-tags menampilkan dialog konfirmasi biasa

13. Cari baris Tagline Co (lewat pagination atau Search), lalu klik `⋯` > Delete
14. Verifikasi dialog `Delete Brand` (danger) tampil dengan `• Tagline Co` dan `Are you sure you want to delete it? This action cannot be undone.`
15. Verifikasi dialog `Cannot Delete Brand` tidak tampil
16. Verifikasi tidak ada breakdown Global Settings (TAG)
17. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil
18. Klik [Cancel]
19. Verifikasi dialog tertutup tanpa perubahan
20. Verifikasi Tagline Co tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul memetakan langkah ke id TC; TC-92 dan TC-93 berbagi satu pembukaan overlay (TC-93 melanjutkan dari opsi `Delete` yang sama), sehingga langkah "Klik `⋯` > Delete" TC-93 sumber digabung ke langkah 6.
- Sesuai bagian 3, tidak ada aksi yang menghapus data di spec ini; Delete sungguhan (konfirmasi `[Delete]`) diuji di spec Delete lain.
- Brand pre-setup tidak diberi suffix `{runId}` (tidak dibuat atau diubah). Pencarian baris lewat Search atau pagination mengikuti Catatan TC sumber.
