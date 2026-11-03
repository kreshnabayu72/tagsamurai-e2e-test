---
id: TC-FA-CAT-E2E-180-new-category-description-bebas-dan-nama-tersimpan-ter-trim
title: "New Category: Description Karakter Bebas dan Category Name Tersimpan Ter-trim"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-107
  - TC-FA-CAT-86
coverage:
  web: automated
---

# New Category: Description Karakter Bebas dan Category Name Tersimpan Ter-trim

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca.
- Data milik spec: kategori level 1 `Desc Free {runId}-180` (TC-FA-CAT-107) dan kategori `Trim  Cat {runId}-180` dengan dua spasi di tengah (TC-FA-CAT-86), keduanya dibuat lewat UI. Hook `after` menghapus keduanya lewat API.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-107: Description menerima karakter bebas tanpa batasan karakter

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Desc Free {runId}-180`
3. Isi Description `Catatan @#%& (uji) / 100% <ok>`
4. Klik `[Submit]`
5. Verifikasi toast `Success, category has been created.` tampil
6. Ketik Search `Desc Free {runId}-180`, tekan Enter
7. Klik elipsis (⋯) pada baris `Desc Free {runId}-180`
8. Klik `Detail`
9. Verifikasi Popup Detail menampilkan Description persis `Catatan @#%& (uji) / 100% <ok>`
10. Tutup Popup Detail

### TC-FA-CAT-86: Category Name disimpan dalam bentuk ter-trim dan spasi tengah tidak berubah

11. Klik `[+] Category` pada sidebar
12. Isi Category Name dua spasi + `Trim` + dua spasi + `Cat {runId}-180` + dua spasi (spasi ganda di tengah, spasi di awal dan akhir)
13. Klik `[Submit]`
14. Verifikasi toast `Success, category has been created.` tampil
15. Ketik Search `Trim`, tekan Enter
16. Perhatikan baris hasil di tabel
17. Verifikasi kategori tersimpan sebagai `Trim  Cat {runId}-180` (spasi awal dan akhir dibuang, dua spasi di tengah dipertahankan)
18. Verifikasi tidak ada pesan atau indikator trim

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 6 dan 15 (Search untuk menemukan baris target), langkah 7 sampai 8 (membuka Popup Detail), langkah 10 (menutup Popup Detail), langkah 16 (mengamati baris hasil).
- Asersi nama pada langkah 17 membaca teks nilai sel (bukan render HTML) agar dua spasi tengah terbedakan.
- Temuan untuk QA:
  - TC-FA-CAT-107 menyebut "Popup Detail" tanpa langkah membukanya; spec menambah langkah membuka Detail (langkah 7 sampai 8) agar Expected punya langkah Verifikasi (S-01).
  - TC-FA-CAT-86 memberi Category Name tanpa suffix; spec menambah suffix `{runId}-180` (S-12).
