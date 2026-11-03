---
id: TC-FA-CF-E2E-109-setup-column-reorder-dan-isolasi-konfigurasi-changelog
title: "Setup Column: Reorder Tiap Kolom dan Isolasi dari Modal Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-410
  - TC-FA-CF-416
coverage:
  web: automated
---

# Setup Column: Reorder Tiap Kolom dan Isolasi dari Modal Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Riwayat Changelog (Precondition TC-FA-CF-416 butir b): Company Alpha memiliki sedikitnya satu entri Changelog tab General (riwayat dari seed, disediakan tim FE/BE); dibutuhkan agar Modal Changelog pada langkah 15 menampilkan ketujuh kolomnya (langkah 16) dan bukan empty state.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: drag-and-drop kolom pada Popup Setup Column, pembacaan urutan Live Preview dan header tabel, dan muat ulang halaman (F5).
- State global: konfigurasi kolom tabel utama disimpan di browser lewat `[Save]`. Spec menyimpan konfigurasi pada langkah 7 dan langkah 13 serta memulihkannya ke default pada langkah 10 dan langkah 18. Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Parameter iterasi langkah 3 sampai 5 (tabel Kolom Dapat Diurutkan, sepuluh kolom TC-FA-CF-410):

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

### TC-FA-CF-410: Reorder tiap kolom di Popup Setup Column tersimpan setelah Save

1. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Verifikasi Live Preview menampilkan sepuluh kolom data dalam urutan default `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Scope`, `Value Type`, `Required`, `Modified By`, `Last Updated`

Untuk setiap baris tabel Kolom Dapat Diurutkan pada `## Prerequisites` (langkah 3 sampai 5):

3. Seret kolom ke posisi pertama pada Popup Setup Column
4. Verifikasi kolom dapat dipindah ke posisi pertama pada Live Preview
5. Seret kolom kembali ke posisi semula pada Popup Setup Column

6. Seret `Last Updated` ke posisi pertama
7. Klik `[Save]`
8. Muat ulang halaman (F5)
9. Verifikasi tabel menampilkan `Last Updated` sebagai kolom data pertama
10. Pulihkan konfigurasi kolom: buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-CF-416: Konfigurasi kolom tabel utama tidak memengaruhi konfigurasi kolom Modal Changelog

11. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
12. Hapus centang `Placeholder`
13. Klik `[Save]`
14. Verifikasi tabel utama tidak menampilkan kolom `Placeholder`
15. Klik icon Changelog
16. Verifikasi Modal Changelog tetap menampilkan ketujuh kolomnya: `Date`, `Action`, `Field Name`, `Field`, `Old Value`, `New Value`, `Modified By`
17. Tutup Modal Changelog dengan icon `[✕]`
18. Pulihkan konfigurasi kolom: buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Spec memuat 18 langkah nominal dan sekitar 45 langkah setelah ekspansi blok berparameter (langkah 3 sampai 5 diulang sepuluh kali), di atas smell 35 langkah. Alasan: satu topik (Setup Column tabel utama), satu popup, satu akun, satu dataset (Company Alpha baseline); kesepuluh iterasi identik tanpa langkah bersyarat dan parameternya ada di tabel `## Prerequisites` (bagian 8b butir 7), sehingga memecah per kolom hanya menambah login dan hook tanpa menambah makna.
- Langkah yang diulang: langkah 3 sampai 5 untuk tiap baris tabel Kolom Dapat Diurutkan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (mengembalikan kolom ke posisi semula, sesuai "lalu kembalikan" di TC-FA-CF-410), langkah 10 dan 18 (memulihkan konfigurasi kolom ke default, S-09), langkah 12 sampai 13 (menyembunyikan `Placeholder` lalu menyimpan sebagai langkah 1 TC-FA-CF-416), langkah 17 (menutup modal).
- Langkah 2 adalah asersi tambahan di luar Expected TC-FA-CF-410 (S-03): memastikan urutan default kolom pada Live Preview sebelum penyeretan, sehingga perubahan urutan pada langkah 3 sampai 5 dan 6 sampai 9 dibandingkan dengan keadaan awal yang diketahui.
- Langkah 14 adalah asersi tambahan di luar Expected TC-FA-CF-416 (S-03): memastikan perubahan konfigurasi tabel utama benar-benar berlaku sebelum Modal Changelog dibuka, sehingga langkah 16 menguji isolasi dan bukan sekadar Save yang tidak berlaku.
- Temuan untuk QA:
  - TC-FA-CF-410 untuk kolom `Active` yang sudah berada di posisi pertama pada urutan default: "seret ke posisi pertama" tidak mengubah urutan; Expected a ("dapat dipindah ke posisi pertama") tidak membedakan kasus ini.
  - TC-FA-CF-416 Precondition b mensyaratkan sedikitnya satu entri Changelog tab General pada Company Alpha (riwayat dari seed); Pre-setup #19 (Company Changelog) tetap satu-satunya Company yang dijamin memiliki riwayat di tabel Pre-setup, sehingga seed riwayat Company Alpha disediakan tim FE/BE (lihat Prerequisites).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
