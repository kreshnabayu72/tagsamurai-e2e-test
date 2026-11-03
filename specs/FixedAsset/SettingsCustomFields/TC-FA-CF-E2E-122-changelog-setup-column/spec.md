---
id: TC-FA-CF-E2E-122-changelog-setup-column
title: "Modal Changelog: Setup Column dan Isolasi dari Tabel Utama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-474
  - TC-FA-CF-475
  - TC-FA-CF-644
coverage:
  web: automated
---

# Modal Changelog: Setup Column dan Isolasi dari Tabel Utama

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Tabel utama tab General Company Changelog menampilkan kesepuluh kolom data dengan konfigurasi default.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: drag-and-drop kolom, klik icon Pin, pembacaan Live Preview, pengaturan ukuran viewport browser, dan scroll horizontal tabel modal.
- State global: konfigurasi kolom Modal Changelog dan tabel utama disimpan di browser lewat `[Save]`. Spec menyimpan konfigurasi Modal Changelog pada langkah 19 dan langkah 34, dan memulihkannya ke default pada langkah 31 dan langkah 38; viewport dikecilkan pada langkah 20 dan dipulihkan pada langkah 25. Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Parameter iterasi langkah 7 sampai 15 (tabel Kolom Modal Changelog, tujuh kolom TC-FA-CF-475):

| No | Kolom |
|---|---|
| 1 | `Date` |
| 2 | `Action` |
| 3 | `Field Name` |
| 4 | `Field` |
| 5 | `Old Value` |
| 6 | `New Value` |
| 7 | `Modified By` |

## Test Steps

1. Klik icon Changelog di toolbar

### TC-FA-CF-474: Screening Overlay Column Visibility Modal Changelog memuat tujuh kolom

2. Klik header kolom Actions `(⋯)` di modal
3. Verifikasi overlay memuat tujuh kolom ber-checkbox tercentang: `Date`, `Action`, `Field Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi overlay memuat item `Setup Column...`

### TC-FA-CF-475: Popup Setup Column Modal Changelog: ceklis, geser, pin tiap kolom, reset, dan discard

5. Klik `Setup Column...`
6. Verifikasi Live Preview menampilkan tujuh kolom `Date`, `Action`, `Field Name`, `Field`, `Old Value`, `New Value`, `Modified By`

Untuk setiap baris tabel Kolom Modal Changelog pada `## Prerequisites` (langkah 7 sampai 15):

7. Hapus centang kolom pada Popup Setup Column
8. Verifikasi kolom dapat di-ceklis: kolom hilang dari Live Preview saat tidak dicentang
9. Centang kembali kolom
10. Verifikasi kolom kembali tampil pada Live Preview saat dicentang
11. Seret kolom ke posisi pertama
12. Verifikasi kolom dapat digeser ke posisi pertama pada Live Preview
13. Klik icon Pin kolom
14. Verifikasi kolom dapat di-pin
15. Klik icon Pin kolom sekali lagi untuk unpin

16. Hapus centang `Old Value`
17. Seret `Modified By` ke posisi pertama
18. Klik icon Pin `Date`
19. Klik `[Save]`
20. Persempit viewport browser sampai tabel Modal Changelog dapat di-scroll horizontal
21. Scroll tabel Modal Changelog horizontal
22. Verifikasi kolom `Old Value` hilang dari Modal Changelog
23. Verifikasi kolom `Modified By` berada di depan (kolom data pertama)
24. Verifikasi kolom `Date` beku saat tabel di-scroll horizontal
25. Pulihkan ukuran viewport browser ke ukuran semula
26. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
27. Klik `[Reset to Default]`
28. Verifikasi Live Preview menampilkan tujuh kolom dalam susunan default
29. Klik icon `[✕]`
30. Verifikasi tabel Modal Changelog tetap memakai konfigurasi tersimpan (kolom `Old Value` tetap hilang dan `Modified By` tetap kolom data pertama)
31. Pulihkan konfigurasi kolom Modal Changelog: buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-CF-644: Konfigurasi kolom Modal Changelog tidak memengaruhi konfigurasi kolom tabel utama

32. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
33. Hapus centang `Old Value`
34. Klik `[Save]`
35. Verifikasi Modal Changelog menyembunyikan kolom `Old Value`
36. Klik icon `[✕]` untuk menutup modal
37. Verifikasi tabel utama tetap menampilkan kesepuluh kolom data: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`
38. Pulihkan konfigurasi kolom Modal Changelog: klik icon Changelog, buka Popup Setup Column, klik `[Reset to Default]`, klik `[Save]`, lalu tutup modal

## Notes

- Spec memuat 38 langkah nominal dan sekitar 92 langkah setelah ekspansi blok berparameter (langkah 7 sampai 15 diulang tujuh kali), di atas smell 35 langkah. Alasan: satu topik (Setup Column Modal Changelog dan isolasinya dari tabel utama), satu popup, satu akun, satu dataset (Company Changelog) tanpa mengubah data; tujuh iterasi identik tanpa langkah bersyarat dengan parameter di tabel `## Prerequisites` (bagian 8b butir 7), dan tiga blok TC saling terkait pada konfigurasi kolom yang sama, sehingga memecahnya hanya menambah login dan hook.
- Langkah yang diulang: langkah 7 sampai 15 untuk tiap baris tabel Kolom Modal Changelog. `Verifikasi` tetap satu per klausa (di-ceklis dengan dua keadaan, digeser, di-pin; S-01).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal sesuai langkah uji TC), langkah 5 (membuka popup dari overlay sesuai langkah 2 TC-FA-CF-475), langkah 15 (unpin supaya batas tiga kolom tidak tercapai pada iterasi berikut), langkah 20 dan 25 (mengecilkan lalu memulihkan viewport supaya tabel dapat di-scroll horizontal; S-14), langkah 31 dan 38 (memulihkan konfigurasi Modal Changelog ke default; S-09), langkah 32 sampai 34 (menyimpan konfigurasi sesuai langkah uji TC-FA-CF-644).
- Anchor absence: langkah 6 (tujuh kolom tampil) mendahului absence kolom hilang di langkah 8; langkah 22 sampai 24 didahului kolom lain pada tabel modal yang tampil (langkah 23).
- Langkah 26 sampai 30 menjalankan klausa Expected i ("Reset hanya berlaku setelah Save; menutup dengan `[✕]` membuang perubahan"): Reset hanya mengubah Live Preview (langkah 28) dan penutupan dengan `[✕]` membuang perubahan itu (langkah 30).
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-475 Expected a sampai g ("dapat di-ceklis, digeser, dan di-pin") bermajemuk per kolom; spec memecahnya menjadi `Verifikasi` hilang, kembali, digeser, dan di-pin per kolom.
  - TC-FA-CF-475 Expected h ("`Date` beku saat scroll") mengandaikan tabel modal melebihi lebar viewport; Precondition TC tidak menyebut lebar viewport. Spec mengecilkan viewport (langkah 20).
  - TC-FA-CF-475 langkah 3 ("seret ke posisi pertama") untuk kolom `Date` yang sudah berada di posisi pertama tidak mengubah urutan; Expected tidak membedakan kasus ini.
  - TC-FA-CF-644 langkah 1 menyebut membuka Popup Setup Column "lalu" tanpa menyebut `Setup Column...` di overlay; spec memakai alur yang sama dengan TC-FA-CF-475.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
