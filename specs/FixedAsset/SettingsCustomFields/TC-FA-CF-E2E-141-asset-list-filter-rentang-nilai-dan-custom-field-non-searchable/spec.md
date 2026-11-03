---
id: TC-FA-CF-E2E-141-asset-list-filter-rentang-nilai-dan-custom-field-non-searchable
title: "Asset List: Filter Rentang Nilai dan Custom Field Non-Searchable atau Non-Filterable"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-651
  - TC-FA-CF-652
  - TC-FA-CF-653
coverage:
  web: automated
---

# Asset List: Filter Rentang Nilai dan Custom Field Non-Searchable atau Non-Filterable

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha dengan custom field `AL Text`, `AL Text Area`, `AL Dropdown` (opsi `Gold`, `Silver`), `AL Multi-Dropdown` (opsi `Charger`, `Cable`), `AL Date`, `AL DateTime`, `AL Currency`, `AL Numeric` (1 Decimal Place), `AL Phone`, `AL Percentage`, `AL Email`, `AL URL`, `AL Document`, dan `AL Formula` (`Purchase Price + 10`) bernilai pada aset A1 dan A2 (Pre-setup #38; nilai pada Data Uji TC); dirujuk lewat fixture `Fixture.faCustomFields.assetListFields` (fixture baru, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): preferensi kolom Asset List yang tersimpan di browser (kolom custom field yang ditampilkan lewat Column Visibility) dihapus hook `after`.
- Tabel "Filter rentang TC-FA-CF-651" (parameter langkah 2 sampai 4):

| Kolom filter | Rentang | Aset yang tampil | Nilai A1 / A2 |
|---|---|---|---|
| `AL Numeric` | `10` sampai `20` | A1 | `12.5` / `40` |
| `AL Percentage` | `0` sampai `50` | A1 | `25` / `90` |
| `AL Currency` | `500` sampai `2000` | A1 | `1000` / `5000` |
| `AL Formula` | `100` sampai `200` | A1 | `110` / `11` (Purchase Price A1 = `100`, A2 = `1`) |

- Tabel "Search non-searchable TC-FA-CF-652" (parameter langkah 7 sampai 8; nilai pada A1):

| Kata cari | Kolom |
|---|---|
| `Gold` | `AL Dropdown` |
| `Charger` | `AL Multi-Dropdown` |
| `15/10/26` | `AL Date` |
| `12.5` | `AL Numeric` |
| `25` | `AL Percentage` |
| `1000` | `AL Currency` |
| `110` | `AL Formula` |
| `contract.pdf` | `AL Document` |

- Data Dinamis: tidak ada.
- State global: tidak ada.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-651: Filter Numeric, Percentage, Currency, dan Formula memakai rentang nilai

1. Buka Asset List dan buka Filter Panel
2. Untuk setiap baris tabel "Filter rentang TC-FA-CF-651" pada Prerequisites (langkah 2 sampai 4; 4 iterasi): bersihkan filter iterasi sebelumnya, isi rentang baris tabel pada filter kolom baris tabel, lalu klik `[Apply]`
3. Verifikasi aset A1 tampil pada tabel
4. Verifikasi aset A2 tidak tampil pada tabel (hanya A1 tampil)
5. Bersihkan filter terakhir

### TC-FA-CF-652: Search tidak mencocokkan custom field bertipe non-searchable

6. Tampilkan kolom `AL Dropdown`, `AL Multi-Dropdown`, `AL Date`, `AL DateTime`, `AL Numeric`, `AL Percentage`, `AL Currency`, `AL Formula`, dan `AL Document` lewat Column Visibility
7. Untuk setiap baris tabel "Search non-searchable TC-FA-CF-652" pada Prerequisites (langkah 7 sampai 8; 8 iterasi): ketik Search kata cari baris tabel, tekan Enter (kotak yang sudah berisi diganti isinya)
8. Verifikasi empty state `No results found` tampil (aset A1 tidak ditemukan oleh nilai kolom baris tabel)
9. Klik `(←)` pada kotak Search

### TC-FA-CF-653: Filter Panel tidak memuat field untuk custom field non-filterable

10. Buka Filter Panel
11. Verifikasi Filter Panel memuat field filter `AL Dropdown`
12. Verifikasi Filter Panel tidak memuat field filter untuk `AL Text`, `AL Text Area`, `AL Phone`, `AL Email`, `AL URL`, maupun `AL Document`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): Asset List dan Filter Panel tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC. Spec ini menyimpan konfigurasi kolom Asset List di browser (Column Visibility); pemulihan oleh hook `after`.
- Iterasi berparameter (8b butir 7): langkah 2 sampai 4 diulang 4 kali dan langkah 7 sampai 8 diulang 8 kali dengan parameter pada tabel Prerequisites.
- Urutan TC di spec: 651, 652, 653. Filter dibersihkan sebelum Search dipakai dan Search dibersihkan sebelum Filter Panel dibuka (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Filter Panel, pembersihan filter, langkah 6, dan `(←)` pada kotak Search.
- Temuan untuk QA:
  - TC-FA-CF-652 Expected menyebut `AL DateTime`, tetapi Data Uji TC tidak memberi kata cari untuk `AL DateTime`; spec mencari delapan nilai yang diberikan Data Uji.
  - TC-FA-CF-651 menyebut A2 tidak ditampilkan hanya secara implisit ("hanya A1 tampil"); spec mengasersi A1 tampil lalu A2 tidak tampil.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
