---
id: TC-FA-FAAC-E2E-132-search-kolom-tersembunyi-dan-ditampilkan-kembali
title: "Search Tabel Asset Class: Kolom yang Disembunyikan Tidak Dicari dan Kembali Dicari Setelah Ditampilkan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-362
coverage:
  web: automated
---

# Search Tabel Asset Class: Kolom yang Disembunyikan Tidak Dicari dan Kembali Dicari Setelah Ditampilkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Class Name `Heavy Equipment`), VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: konfigurasi kolom tabel (kolom Class Name disembunyikan lalu ditampilkan kembali oleh langkah 9). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-362: Search tidak mencari kolom yang disembunyikan dan kembali mencari setelah ditampilkan

1. Sembunyikan kolom Class Name lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Class Name)
2. Klik `[Save]`
3. Ketik Search `avy equ`, tekan Enter
4. Verifikasi empty state `No results found` tampil
5. Ganti isi kotak search dengan `ffice-n`, tekan Enter
6. Verifikasi kolom Class Code yang masih tampil tetap dicari: baris OFFICE-NEW tampil
7. Tampilkan kembali kolom Class Name lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Class Name)
8. Klik `[Save]`
9. Ganti isi kotak search dengan `avy equ`, tekan Enter
10. Verifikasi baris HEAVY-EQ tampil
11. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 11 (menutup input Search dan mereset tabel, S-09; R-16). Langkah 7 sampai 8 mengembalikan konfigurasi kolom sebelum asersi akhir TC; bukan sekadar pemulihan.
- Spec ini berisi satu TC karena asersinya bergantung pada konfigurasi kolom yang diubah lewat Setup Column dan tidak boleh digabung ke spec Search lain tanpa melampaui sekitar 35 langkah (spec 114).
- Nama literal Pre-setup (HEAVY-EQ, OFFICE-NEW, dan sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
