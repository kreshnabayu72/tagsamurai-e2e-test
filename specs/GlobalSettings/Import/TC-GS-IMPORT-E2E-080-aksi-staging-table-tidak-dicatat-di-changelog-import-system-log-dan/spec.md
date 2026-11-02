---
id: TC-GS-IMPORT-E2E-080-aksi-staging-table-tidak-dicatat-di-changelog-import-system-log-dan
title: "Aksi Staging Table Sebelum Commit Tidak Dicatat di Changelog Import, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-669
coverage:
  web: automated
---

# Aksi Staging Table Sebelum Commit Tidak Dicatat di Changelog Import, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan oleh langkah 1 di awal tiap varian lewat skrip fixture): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter) dengan D-76 varian 1 (`created_at` dimundurkan 25 jam lewat fixture timestamp, bukan jam server, sehingga log tidak bercap waktu masa depan; Unsaved Banner tampil).
- Tabel varian aksi (aksi varian dilakukan pada langkah 9; langkah 1 sampai 17 diulang untuk tiap varian):

| Varian | Aksi |
|---|---|
| 1 Save sesi Edit | baris #1 diubah menjadi `Acme Corporation` lalu `[Save]` |
| 2 Save sesi Duplicate | Duplicate baris #2 lalu `[Save]` |
| 3 Save tanpa perubahan | Edit baris #1 lalu `[Save]` (toast "No changes to save.") |
| 4 Remove | Remove baris #3 |
| 5 Bulk Delete | centang baris #2 dan #5 lalu Bulk Action > Delete |
| 6 Delete All Rows | `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters" |
| 7 Discard Draft | `[Discard]` lalu `[Discard Draft]` |

- Baseline asersi jumlah total: angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) dibaca sebelum aksi dan sesudah aksi pada tiga surface: Changelog Import, System Log pada halaman Detail User pelaku (Sari Dewi), dan Activity Log (Global Settings > Activity Log) tab User Action. Total tidak diasersi sebagai angka absolut (S-12).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client A dipulihkan ke D-09 oleh langkah 1 di awal tiap varian (Kontrak Fixture R2); draft D-09 yang tersisa sesudah varian terakhir ditimpa oleh reset `beforeEach` spec berikutnya.

## Test Steps

Untuk setiap varian pada tabel varian aksi (langkah 1 sampai 17):

1. Pulihkan draft Client A ke D-09 dengan D-76 varian 1 lewat skrip fixture; buka halaman Import > Brand lewat sidebar, lalu muat ulang halaman Import > Brand
2. Buka Changelog Import lewat `[Changelog]` di header
3. Catat angka total pada teks Pagination Changelog Import (baseline Changelog)
4. Tutup modal Changelog
5. Buka System Log pada halaman Detail User pelaku (Sari Dewi)
6. Catat angka total pada teks Pagination System Log (baseline System Log)
7. Buka Activity Log (Global Settings > Activity Log) pada tab User Action
8. Catat angka total pada teks Pagination Activity Log (baseline Activity Log)
9. Buka kembali Import > Brand dan lakukan aksi varian pada tabel varian sampai toast tampil
10. Buka kembali Changelog Import lewat `[Changelog]` di header
11. Verifikasi modal Changelog Import terbuka
12. Verifikasi total pada Pagination Changelog Import sama dengan baseline Changelog pada langkah 3
13. Tutup modal Changelog
14. Buka kembali System Log pada halaman Detail User pelaku (Sari Dewi)
15. Verifikasi total pada Pagination System Log Detail User pelaku sama dengan baseline System Log pada langkah 6
16. Buka kembali Activity Log (Global Settings > Activity Log) pada tab User Action
17. Verifikasi total pada Pagination Activity Log tab User Action sama dengan baseline Activity Log pada langkah 8

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (kelas g, prinsip 13g); objek uji ialah tidak adanya entri log untuk aksi Staging Table dengan baseline jumlah di tiga surface (S-12). Aksi dilakukan di spec ini (bukan hanya dirujuk).
- Langkah 1 sampai 17 diulang tujuh kali (ekspansi 17 × 7 = 119 langkah), di atas smell 35 langkah. Alasan: langkah identik antar-varian dengan parameter aksi pada tabel varian, tiap varian berdiri sendiri dengan baseline dan draft D-09 sendiri, dan blok baca-log berpola (buka surface, baca total) tidak dihitung sebagai smell. Draft dipulihkan ke D-09 pada langkah 1 tiap varian.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pemulihan draft D-09, membuka halaman Import > Brand dari halaman mana pun posisinya, dan muat ulang halaman), langkah 2 sampai 10, 13, 14, 16 (membuka surface dan mencatat baseline). Skrip fixture langkah 1 sinkron (`suite.md`).
- Anchor asersi absence: pembacaan baseline pada langkah 3, 6, dan 8 sebelum aksi pertama; Verifikasi judul modal Changelog Import pada langkah 11 menjadi anchor pembacaan ulang Changelog; toast aksi pada langkah 9 membuktikan aksi selesai sebelum total dibaca ulang.
- Pembagian TC lintas spec: TC-GS-IMPORT-669 hanya memuat aksi pra-commit; pencatatan log commit dan aksi lain ada di spec Changelog dan log lain pada suite ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-669 mencampur tujuh varian aksi dalam satu TC dengan langkah baseline yang sama; spec mengulang langkah 1 sampai 17 per varian.
  - Surface ketiga (Activity Log tab User Action) dan System Log Detail User pelaku tidak menyebut filter Date; spec membaca total tanpa filter dan membandingkan terhadap baseline.
