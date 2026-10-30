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
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap varian): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter) dengan D-76 varian 1 (`created_at` dimundurkan 25 jam lewat fixture timestamp, bukan jam server, sehingga log tidak bercap waktu masa depan; Unsaved Banner tampil).
- Tabel varian aksi (langkah 8 sampai 14 diulang untuk tiap varian):

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
- Pemulihan: draft Client A dipulihkan ke D-09 sesudah tiap varian (Kontrak Fixture R2).

## Test Steps

Untuk setiap varian pada tabel varian aksi (langkah 1 sampai 15):

1. Buka Changelog Import lewat `[Changelog]` di header
2. Catat angka total pada teks Pagination Changelog Import (baseline Changelog)
3. Tutup modal Changelog
4. Buka System Log pada halaman Detail User pelaku (Sari Dewi)
5. Catat angka total pada teks Pagination System Log (baseline System Log)
6. Buka Activity Log (Global Settings > Activity Log) pada tab User Action
7. Catat angka total pada teks Pagination Activity Log (baseline Activity Log)
8. Buka kembali Import > Brand dan lakukan aksi varian pada tabel varian sampai toast tampil
9. Buka kembali Changelog Import lewat `[Changelog]` di header
10. Verifikasi total pada Pagination Changelog Import sama dengan baseline Changelog pada langkah 2
11. Tutup modal Changelog
12. Buka kembali System Log pada halaman Detail User pelaku (Sari Dewi)
13. Verifikasi total pada Pagination System Log Detail User pelaku sama dengan baseline System Log pada langkah 5
14. Buka kembali Activity Log (Global Settings > Activity Log) pada tab User Action
15. Verifikasi total pada Pagination Activity Log tab User Action sama dengan baseline Activity Log pada langkah 7

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (kelas g, prinsip 13g); objek uji ialah tidak adanya entri log untuk aksi Staging Table dengan baseline jumlah di tiga surface (S-12). Aksi dilakukan di spec ini (bukan hanya dirujuk).
- Langkah 1 sampai 15 diulang tujuh kali (ekspansi sekitar 105 langkah), di atas smell 35 langkah. Alasan: langkah identik antar-varian dengan parameter aksi pada tabel varian, tiap varian berdiri sendiri dengan baseline dan draft D-09 sendiri, dan blok baca-log berpola (buka surface, baca total) tidak dihitung sebagai smell. Draft dipulihkan ke D-09 antar varian.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 9, 11, 12, 14 (membuka surface dan mencatat baseline), pemulihan draft D-09 setelah langkah 15 pada tiap varian.
- Anchor asersi absence: pembacaan baseline pada langkah 2, 5, dan 7 sebelum aksi pertama; toast aksi pada langkah 8 membuktikan aksi selesai sebelum total dibaca ulang.
- Pembagian TC lintas spec: TC-GS-IMPORT-669 hanya memuat aksi pra-commit; pencatatan log commit dan aksi lain ada di spec Changelog dan log lain pada suite ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-669 mencampur tujuh varian aksi dalam satu TC dengan langkah baseline yang sama; spec mengulang langkah 1 sampai 15 per varian.
  - Surface ketiga (Activity Log tab User Action) dan System Log Detail User pelaku tidak menyebut filter Date; spec membaca total tanpa filter dan membandingkan terhadap baseline.
