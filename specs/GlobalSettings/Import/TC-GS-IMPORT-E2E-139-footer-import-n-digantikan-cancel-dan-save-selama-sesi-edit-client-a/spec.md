---
id: TC-GS-IMPORT-E2E-139-footer-import-n-digantikan-cancel-dan-save-selama-sesi-edit-client-a
title: "Footer Import (N) digantikan Cancel dan Save selama sesi edit (Client A)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-367
coverage:
  web: automated
---

# Footer Import (N) digantikan Cancel dan Save selama sesi edit (Client A)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client A).
- Data Dinamis: D-01 (draft Brand 12 baris `pending` dari brand-12.csv, Population Client A, nama literal Apex Tools sampai Linear Dynamics, pengecualian S-12 Population D-01) dipulihkan ke kondisi Population sebelum TC (Kontrak Fixture R2) lewat `Fixture.import.draftBrand12` (fixture baru, seeding idempotent; dilewati bila draft sudah sesuai). TC ini bertanda dependensi pada TC-GS-IMPORT-1, yaitu D-01.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan draft D-01 lewat fixture.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Spec tidak memutasi draft (sesi edit dibatalkan tanpa perubahan). Suite Import berjalan serial.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft D-01 ke Population bila sesi edit masih terbuka.

## Test Steps

### TC-GS-IMPORT-367: Footer [Import (N)] digantikan [Cancel] dan [Save] selama sesi edit

1. Pulihkan draft Brand Client A ke D-01 lewat fixture bila belum sesuai, lalu muat ulang halaman Import > Brand
2. Buka menu `⋯` baris #1
3. Pilih Edit
4. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
5. Verifikasi `[Import (12)]` tidak tampil
6. Klik `[Cancel]` tanpa mengubah nilai apa pun
7. Verifikasi sesi edit berakhir tanpa dialog
8. Verifikasi footer kembali menampilkan `[Import (12)]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pemulihan draft D-01 sesuai Precondition c dan Kontrak Fixture R2).
- Pembagian TC lintas spec: TC-GS-IMPORT-367 berada di section commit (3l) pada TC sumber, tetapi memakai Client A dan tidak ada commit; satu-satunya TC Client A pada irisan commit, ditaruh di spec sendiri karena akun dan client berbeda dari spec commit Client E.
- Temuan untuk QA:
  - TC-GS-IMPORT-367: berada di section commit (3l) namun memakai Client A (draft Population D-01) sementara aturan Kontrak Fixture R3 menyatakan TC commit memakai Client E; tidak ada commit di TC ini, hanya salah letak section.
  - TC-GS-IMPORT-367: Dependensi TC-GS-IMPORT-1 hanya menyatakan draft D-01; spec menyalin kebutuhan itu sebagai pemulihan draft (S-04), bukan merujuk TC.
  - TC-GS-IMPORT-367: Post Condition (draft Brand Client A tetap berisi 12 baris `pending` tanpa perubahan) diamati hanya lewat langkah 8 (`[Import (12)]`).
