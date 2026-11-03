---
id: TC-FA-LBL-E2E-177-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role-bagian-2-2
title: "Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-36
  - TC-FA-LBL-37
  - TC-FA-LBL-42
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Delete-Only login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; Full-CRUD lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` | TC-FA-LBL-36, TC-FA-LBL-37 | 1 sampai 13 |
| Full-CRUD | #7 | `Fixture.assetLabeling.akun.fullCrud` | `Spectra.env.FA_FULLCRUD_PASSWORD` | TC-FA-LBL-42 | 14 sampai 28 |

- Environment variable: `FA_DELETEONLY_PASSWORD`, `FA_FULLCRUD_PASSWORD`, `FA_LBL_TC_PASSWORD` (dipakai hanya oleh hook `after`). Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (Company Alpha, di-seed lewat sesi API di hook `before`, bersuffix `{runId}-177`; label yang dibuat spec lewat UI dan yang tersisa dibersihkan di hook `after`):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Delete Target 36 {runId}-177` | TC-FA-LBL-36 | bersih (Total Asset 0, bukan Default Label), dihapus |
| `Bulk Target A 37 {runId}-177` | TC-FA-LBL-37 | bersih, dihapus |
| `Bulk Target B 37 {runId}-177` | TC-FA-LBL-37 | bersih, dihapus |
| `Full Target 42 {runId}-177` | TC-FA-LBL-42 | bersih; dipakai sebagai precondition TC, tidak diasersi |
| `Full Create 42 {runId}-177` | TC-FA-LBL-42 | dibuat spec lewat UI, diubah namanya menjadi `Full Edited 42 {runId}-177`, dihapus |

- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan pembersihan (lihat `suite.md`).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Delete-Only: TC-FA-LBL-36 dan TC-FA-LBL-37

1. Ketik Search `Delete Target 36`, tekan Enter
2. Klik `⋯` pada baris `Delete Target 36 {runId}-177` lalu `Delete`
3. Verifikasi dialog `Delete Label` tampil dengan bullet `Delete Target 36 {runId}-177`
4. Klik `[Delete]` pada dialog
5. Verifikasi toast `Success, label has been deleted.`
6. Verifikasi baris `Delete Target 36 {runId}-177` hilang dari tabel
7. Ganti isi kotak search dengan `Bulk Target`, tekan Enter
8. Centang baris `Bulk Target A 37 {runId}-177` dan `Bulk Target B 37 {runId}-177`
9. Klik `Bulk Action` lalu `Delete`
10. Verifikasi dialog `Delete Labels` tampil dengan bullet `Bulk Target A 37 {runId}-177` dan `Bulk Target B 37 {runId}-177`
11. Klik `[Delete]` pada dialog
12. Verifikasi toast `Success, label has been deleted.`
13. Verifikasi baris `Bulk Target A 37 {runId}-177` dan `Bulk Target B 37 {runId}-177` hilang dari tabel

### Full-CRUD: TC-FA-LBL-42

14. Ganti akun: Logout, login sebagai Full-CRUD `Fixture.assetLabeling.akun.fullCrud` (`Spectra.env.FA_FULLCRUD_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
15. Klik `[+ Label]`
16. Isi Label Name dengan `Full Create 42 {runId}-177`
17. Klik `[Submit]`
18. Verifikasi toast `Success, label has been created.`
19. Ketik Search `Full Create 42`, tekan Enter
20. Klik `⋯` pada baris `Full Create 42 {runId}-177` lalu `Edit`
21. Ubah Label Name menjadi `Full Edited 42 {runId}-177`
22. Klik `[Save]`
23. Verifikasi toast `Success, label has been updated.`
24. Ganti isi kotak search dengan `Full Edited 42`, tekan Enter
25. Klik `⋯` pada baris `Full Edited 42 {runId}-177` lalu `Delete`
26. Klik `[Delete]` pada dialog
27. Verifikasi toast `Success, label has been deleted.`
28. Verifikasi baris `Full Edited 42 {runId}-177` hilang dari tabel

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 14) karena akun pertama login di hook `before` dan ganti akun menuntut Step eksplisit (bagian 3a, varian A, 2026-10-30).
- Langkah penghubung (S-03): langkah 1, 7, 19, dan 24 (Search untuk menemukan baris target, R-16).
- Urutan TC: langkah tiap TC mengikuti urutan TC (S-10); blok per role: Delete-Only lalu Full-CRUD, sehingga tiap akun hanya login sekali.
- Absence "hilang dari tabel" (langkah 6, 13, 28): toast sukses hapus (langkah 5, 12, 27) menjadi anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi tidak diasersi: TC-FA-LBL-36 dan 37 ("tidak ada lagi di katalog"), TC-FA-LBL-42 ("`Full Edited 42` tidak ada lagi").
  - TC-FA-LBL-42 Precondition menyebut label bersih `Full Target 42`, tetapi langkahnya hanya memakai label baru `Full Create 42` dan tidak menyentuh `Full Target 42`; label itu di-seed sebagai precondition dan tidak diasersi.
  - TC-FA-LBL-36, 37, dan 42 tidak menyebut halaman tempat baris target berada di tabel; Search dipakai sebagai langkah penghubung.
