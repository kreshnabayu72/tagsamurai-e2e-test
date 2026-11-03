---
id: TC-FA-CF-E2E-108-setup-column-ceklis-kolom-dan-reset-to-default
title: "Setup Column: Ceklis Tiap Kolom dan Reset to Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-409
  - TC-FA-CF-413
coverage:
  web: automated
---

# Setup Column: Ceklis Tiap Kolom dan Reset to Default

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: hapus centang dan centang checkbox kolom pada Popup Setup Column, pembacaan Live Preview, dan muat ulang halaman (F5).
- State global: konfigurasi kolom tabel utama disimpan di browser lewat `[Save]`. Spec menyimpan konfigurasi pada langkah 8 dan langkah 15 serta memulihkannya ke default pada langkah 19. Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Parameter iterasi langkah 3 sampai 6 (tabel Kolom Hideable, sepuluh kolom TC-FA-CF-409):

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

### TC-FA-CF-409: Ceklis dan unceklis tiap kolom di Popup Setup Column tersimpan setelah Save

1. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Verifikasi Live Preview menampilkan sepuluh kolom data dari `Active` sampai `Last Updated`

Untuk setiap baris tabel Kolom Hideable pada `## Prerequisites` (langkah 3 sampai 6):

3. Hapus centang kolom pada Popup Setup Column dan perhatikan Live Preview
4. Verifikasi kolom hilang dari Live Preview saat tidak dicentang
5. Centang kembali kolom pada Popup Setup Column
6. Verifikasi kolom kembali tampil pada Live Preview saat dicentang

7. Hapus centang `Placeholder` dan `Required`
8. Klik `[Save]`
9. Muat ulang halaman (F5)
10. Verifikasi header kolom `Field Name` tampil pada tabel
11. Verifikasi tabel tidak menampilkan kolom `Placeholder` dan `Required` setelah Save dan reload

### TC-FA-CF-413: Reset to Default mengembalikan susunan kolom ke default setelah Save

12. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
13. Hapus centang `Scope`
14. Seret `Last Updated` ke posisi pertama
15. Klik `[Save]`
16. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
17. Klik `[Reset to Default]`
18. Verifikasi Live Preview kembali ke sepuluh kolom default berurutan `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`
19. Klik `[Save]`
20. Muat ulang halaman (F5)
21. Verifikasi tabel menampilkan susunan default: sepuluh kolom data berurutan `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`

## Notes

- Spec memuat 21 langkah nominal dan sekitar 57 langkah setelah ekspansi blok berparameter (langkah 3 sampai 6 diulang sepuluh kali), di atas smell 35 langkah. Alasan: satu topik (Setup Column tabel utama), satu popup, satu akun, satu dataset (Company Alpha baseline) tanpa membuat atau mengubah data; kesepuluh iterasi identik tanpa langkah bersyarat dan parameternya ada di tabel `## Prerequisites` (bagian 8b butir 7), sehingga memecah per kolom hanya menambah login dan hook tanpa menambah makna.
- Langkah yang diulang: langkah 3 sampai 6 untuk tiap baris tabel Kolom Hideable. `Verifikasi` tetap satu per klausa (hilang, lalu kembali).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 sampai 15 (mengubah susunan dan visibilitas kolom lalu menyimpan, sebagai langkah 1 TC-FA-CF-413: menyembunyikan `Scope` dan memindah `Last Updated`, di atas konfigurasi `Placeholder` dan `Required` tersembunyi dari TC-FA-CF-409), langkah 16 (membuka popup untuk reset). Langkah 10 adalah anchor positif untuk absence langkah 11 (bagian 8b butir 2).
- Urutan TC di spec: 409 lalu 413. Konfigurasi yang disimpan TC-FA-CF-409 dipakai sebagai keadaan awal TC-FA-CF-413 dan dikembalikan ke default oleh langkah 19 (S-09).
- Temuan untuk QA:
  - TC-FA-CF-409 Expected a sampai j memakai kalimat identik per kolom ("hilang dari Live Preview saat tidak dicentang dan kembali saat dicentang"); spec memecahnya menjadi dua `Verifikasi` per kolom (hilang, kembali).
  - TC-FA-CF-413 langkah 1 ("Ubah susunan dan visibilitas kolom") tidak menyebut kolom yang diubah; spec memilih `Scope` (disembunyikan) dan `Last Updated` (dipindah ke posisi pertama).
  - TC-FA-CF-413 Expected tidak menyatakan state pin; spec tidak mengasersinya.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
