---
id: TC-FA-CAT-E2E-114-modal-changelog-search-vs-visibilitas-kolom-dan-kombinasi-search-filter
title: "Modal Changelog: Search Terikat Visibilitas Kolom, Filter Independen, dan Kombinasi Search dengan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-585
  - TC-FA-CAT-405
coverage:
  web: automated
---

# Modal Changelog: Search Terikat Visibilitas Kolom, Filter Independen, dan Kombinasi Search dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`).

## Test Steps

### TC-FA-CAT-585: Search terikat visibilitas kolom, Filter independen dari visibilitas kolom

1. Klik icon Changelog di Table Tools
2. Klik header Actions (⋯) > `Setup Column...`
3. Hilangkan centang kolom `Field` lalu klik `[Save]`
4. Klik icon Search, ketik `Description`, lalu tekan `Enter`
5. Verifikasi empty state `No results found` dengan `Try adjusting your search or filter.` tampil
6. Klik header Actions (⋯) > `Setup Column...`
7. Centang kolom `Field` lalu klik `[Save]`
8. Klik icon Search, ketik `Description`, lalu tekan `Enter`
9. Verifikasi keyword `Description` mencocokkan baris Edit Description `Furniture`
10. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong
11. Klik header Actions (⋯) > `Setup Column...`
12. Hilangkan centang kolom `Field` lalu klik `[Save]`
13. Klik icon Filter, pilih Field `Description`, lalu klik `[Apply]`
14. Klik icon Filter
15. Verifikasi field Filter `Field` tetap ada di Filter Panel walau kolom `Field` disembunyikan
16. Verifikasi nilai Filter Field `Description` tetap ter-Apply
17. Verifikasi tabel hanya memuat baris dengan Field `Description` walau kolom `Field` disembunyikan
18. Klik `[Clear Field]` lalu `[Apply]`, kemudian klik icon Close (✕) pada modal Changelog

### TC-FA-CAT-405: Kombinasi Search dan Filter Changelog serta pelepasan kontrol

19. Klik icon Changelog di Table Tools
20. Klik icon Search, ketik `Electronics`, lalu tekan `Enter`
21. Klik icon Filter, pilih Action `Create`, lalu klik `[Apply]`
22. Verifikasi tabel memuat hasil irisan Search `Electronics` dan Filter Action `Create`
23. Klik Clear Filter
24. Verifikasi Search `Electronics` tetap berlaku setelah Clear Filter
25. Klik icon Filter, pilih Action `Create`, lalu klik `[Apply]`
26. Klik Clear Search
27. Verifikasi Filter Action `Create` tetap berlaku setelah Clear Search
28. Klik Clear Filter lalu klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-586 ada di spec 193.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): langkah 6 dan 7 membuka kembali Setup Column untuk memunculkan kolom `Field`, langkah 10 mengosongkan Search sebelum langkah berikutnya mengandalkan state bersih, langkah 18 membersihkan Filter dan menutup modal, langkah 25 menerapkan ulang Filter Action `Create`, langkah 28 membersihkan Filter dan menutup modal.
- Search hanya menyaring saat `Enter` (8b butir 9); langkah Search ditulis atomik.
- Temuan untuk QA:
  - TC-FA-CAT-405 langkah 3 membersihkan Filter lalu Search berurutan, sehingga klaim "Clear Search mempertahankan Filter" tidak dapat diamati dalam urutan itu; spec menerapkan ulang Filter Action `Create` (langkah 25) sebelum Clear Search agar retensi Filter dapat diasersi.
  - TC-FA-CAT-405 tidak menyebut kontrol yang dimaksud "Clear Filter" dan "Clear Search"; spec memakai `[Clear Field]` untuk Filter pada TC-FA-CAT-585 dan nama kontrol sebagaimana tertulis di TC-FA-CAT-405.
  - Fixture `fixtures/settings-categories.json` belum ada; identitas data Pre-setup #23 ditulis literal di Prerequisites sampai tim FE menetapkan kunci fixture.
