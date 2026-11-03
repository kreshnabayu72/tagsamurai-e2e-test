---
id: TC-FA-CF-E2E-110-setup-column-pin-dan-unpin
title: "Setup Column: Pin dan Unpin Tiap Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-411
  - TC-FA-CF-412
coverage:
  web: automated
---

# Setup Column: Pin dan Unpin Tiap Kolom

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: klik icon Pin pada Popup Setup Column, hover tooltip, pengaturan ukuran viewport browser, dan scroll horizontal tabel.
- State global: konfigurasi kolom (pin) tabel utama disimpan di browser lewat `[Save]`. Spec menyimpan konfigurasi pada langkah 10 dan memulihkannya ke default pada langkah 15; ukuran viewport dikecilkan pada langkah 11 dan dipulihkan pada langkah 14. Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Parameter iterasi langkah 3 sampai 6 (tabel Kolom Dapat Di-pin, sepuluh kolom TC-FA-CF-411):

| No | Kolom |
|---|---|
| 1 | `Active` |
| 2 | `Field Name` |
| 3 | `Data Type` |
| 4 | `Value Setting` |
| 5 | `Placeholder` |
| 6 | `Scope` |
| 7 | `Value Type` |
| 8 | `Required` |
| 9 | `Modified By` |
| 10 | `Last Updated` |

## Test Steps

### TC-FA-CF-411: Pin tiap kolom membekukan kolom saat scroll horizontal dan maksimum tiga kolom

1. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Verifikasi icon Pin tampil pada kesepuluh kolom di Popup Setup Column

Untuk setiap baris tabel Kolom Dapat Di-pin pada `## Prerequisites` (langkah 3 sampai 6):

3. Klik icon Pin kolom
4. Verifikasi kolom dapat di-pin (icon Pin kolom aktif)
5. Klik icon Pin kolom sekali lagi untuk unpin
6. Verifikasi kolom dapat di-unpin (icon Pin kolom tidak aktif)

7. Klik icon Pin pada `Field Name`, `Data Type`, dan `Scope`
8. Arahkan kursor ke icon Pin kolom `Value Type`
9. Verifikasi icon Pin kolom `Value Type` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
10. Klik `[Save]`
11. Persempit viewport browser sampai tabel dapat di-scroll horizontal
12. Scroll tabel horizontal
13. Verifikasi kolom `Field Name`, `Data Type`, dan `Scope` tetap terlihat saat tabel di-scroll horizontal
14. Pulihkan ukuran viewport browser ke ukuran semula

### TC-FA-CF-412: Unpin kolom mengembalikan icon Pin kolom lain menjadi aktif

15. Pulihkan konfigurasi kolom: buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`
16. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
17. Klik icon Pin pada `Field Name`, `Data Type`, dan `Scope`
18. Klik icon Pin pada `Scope` untuk unpin
19. Verifikasi icon Pin kolom lain (`Value Type`) kembali aktif
20. Klik icon `[✕]` untuk menutup popup tanpa menyimpan

## Notes

- Spec memuat 20 langkah nominal dan sekitar 54 langkah setelah ekspansi blok berparameter (langkah 3 sampai 6 diulang sepuluh kali), di atas smell 35 langkah. Alasan: satu topik (Pin di Popup Setup Column), satu popup, satu akun, satu dataset (Company Alpha baseline); kesepuluh iterasi identik tanpa langkah bersyarat dan parameternya ada di tabel `## Prerequisites` (bagian 8b butir 7), sehingga memecah per kolom hanya menambah login dan hook tanpa menambah makna.
- Langkah yang diulang: langkah 3 sampai 6 untuk tiap baris tabel Kolom Dapat Di-pin. `Verifikasi` tetap satu per klausa (di-pin, lalu di-unpin).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 dan 14 (mengecilkan viewport supaya tabel dapat di-scroll horizontal, lalu memulihkannya; S-03 dan S-14), langkah 15 (memulihkan konfigurasi kolom ke default; S-09), langkah 20 (menutup popup tanpa menyimpan).
- Langkah 2 adalah anchor positif sebelum iterasi (icon Pin tampil pada kesepuluh kolom).
- Temuan untuk QA:
  - TC-FA-CF-411 langkah 5 ("scroll tabel horizontal") dan Expected l ("ketiga kolom tetap terlihat saat tabel di-scroll horizontal") mengandaikan tabel melebihi lebar viewport; Precondition TC tidak menyebut lebar viewport. Spec mengecilkan viewport (langkah 11).
  - TC-FA-CF-411 Expected a sampai j ("dapat di-pin dan di-unpin") dipecah menjadi dua `Verifikasi` per kolom; cara mengamati status pin (icon aktif) tidak disebut TC.
  - TC-FA-CF-412 langkah 2 ("Pin tiga kolom lalu unpin satu") tidak menyebut kolomnya; spec memakai `Field Name`, `Data Type`, `Scope` (sama dengan TC-FA-CF-411) dan unpin `Scope`.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
