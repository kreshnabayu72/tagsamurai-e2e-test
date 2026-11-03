---
id: TC-FA-CF-E2E-140-asset-list-search-filter-teks-dropdown-dan-tanggal
title: "Asset List: Search dan Filter Custom Field Teks, Dropdown, dan Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-648
  - TC-FA-CF-649
  - TC-FA-CF-650
coverage:
  web: automated
---

# Asset List: Search dan Filter Custom Field Teks, Dropdown, dan Tanggal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha dengan custom field `AL Text`, `AL Text Area`, `AL Dropdown` (opsi `Gold`, `Silver`), `AL Multi-Dropdown` (opsi `Charger`, `Cable`), `AL Date`, `AL DateTime`, `AL Currency`, `AL Numeric` (1 Decimal Place), `AL Phone`, `AL Percentage`, `AL Email`, `AL URL`, `AL Document`, dan `AL Formula` (`Purchase Price + 10`) bernilai pada aset A1 dan A2 (Pre-setup #38; nilai pada Data Uji TC); dirujuk lewat fixture `Fixture.faCustomFields.assetListFields` (fixture baru, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): preferensi kolom Asset List yang tersimpan di browser (kolom custom field yang ditampilkan lewat Column Visibility) dihapus hook `after`.
- Tabel "Pencarian TC-FA-CF-648" (parameter langkah 2 sampai 3; nilai pada A1):

| Kata cari | Kolom | Nilai A1 |
|---|---|---|
| `STATION` | `AL Text` | `Pump Station Alpha` |
| `inspection` | `AL Text Area` | `Annual inspection notes` |
| `3456` | `AL Phone` | `+62 812 3456 7890` |
| `OPS@EXAMPLE` | `AL Email` | `ops@example.com` |
| `example.com/pump` | `AL URL` | `https://example.com/pump` |

- Nilai data aset: `AL Dropdown` A1 = `Gold`, A2 = `Silver`; `AL Multi-Dropdown` A1 = `Charger` dan `Cable`, A2 = `Cable`; `AL Date` A1 = `15/10/26`, A2 = `20/11/26`; `AL DateTime` A1 = `15/10/26 23:30`, A2 = `20/11/26 08:00`.
- Data Dinamis: tidak ada.
- State global: tidak ada.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-648: Asset List Search mencocokkan nilai Text, Text Area, Phone, Email, dan URL secara substring tidak peka huruf

1. Buka Asset List dan tampilkan kolom `AL Text`, `AL Text Area`, `AL Phone`, `AL Email`, dan `AL URL` lewat Column Visibility
2. Untuk setiap baris tabel "Pencarian TC-FA-CF-648" pada Prerequisites (langkah 2 sampai 3; 5 iterasi): ketik Search kata cari baris tabel, tekan Enter (kotak yang sudah berisi diganti isinya)
3. Verifikasi aset A1 ditemukan pada kolom custom field baris tabel oleh kata cari baris tabel
4. Klik `(←)` pada kotak Search

### TC-FA-CF-649: Filter Dropdown dan Multi-Dropdown menyaring berdasarkan opsi terpilih

5. Buka Filter Panel
6. Pilih opsi `Gold` pada filter `AL Dropdown` lalu klik `[Apply]`
7. Verifikasi aset A1 tampil pada tabel
8. Verifikasi aset A2 tidak tampil pada tabel (hanya A1 tampil)
9. Bersihkan filter `AL Dropdown`, pilih opsi `Charger` pada filter `AL Multi-Dropdown`, lalu klik `[Apply]`
10. Verifikasi aset A1 tampil pada tabel
11. Verifikasi aset A2 tidak tampil pada tabel (elemen array A1 memuat `Charger`)

### TC-FA-CF-650: Filter Date dan DateTime memakai rentang tanggal dengan pembulatan hari penuh

12. Bersihkan filter `AL Multi-Dropdown`, pilih rentang `15/10/26` sampai `15/10/26` pada filter `AL Date`, lalu klik `[Apply]`
13. Verifikasi aset A1 tampil pada tabel
14. Verifikasi aset A2 tidak tampil pada tabel (hanya A1 tampil)
15. Bersihkan filter `AL Date`, pilih rentang `15/10/26` sampai `15/10/26` pada filter `AL DateTime`, lalu klik `[Apply]`
16. Verifikasi aset A1 tampil pada tabel (`23:30` termasuk karena rentang dibulatkan ke hari penuh)
17. Verifikasi aset A2 tidak tampil pada tabel
18. Bersihkan filter `AL DateTime`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): Asset List dan Filter Panel tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC. Spec ini menyimpan konfigurasi kolom Asset List di browser (Column Visibility); pemulihan oleh hook `after` (lihat Prerequisites).
- Iterasi berparameter (8b butir 7): langkah 2 sampai 3 diulang 5 kali dengan parameter pada tabel Prerequisites.
- Urutan TC di spec: 648, 649, 650. Search dibersihkan (langkah penghubung `(←)`) sebelum filter dipakai; tiap filter dibersihkan sebelum filter berikutnya diterapkan (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (menampilkan kolom), `(←)` pada kotak Search, pembukaan Filter Panel, dan pembersihan filter.
- Temuan untuk QA:
  - TC-FA-CF-648 sampai 650 menyebut aset A1 dan A2 tanpa kolom identitas baris pada Asset List; spec menyebut "aset A1" dan "aset A2" seperti TC.
  - TC-FA-CF-649 tidak menyebut urutan pembersihan `AL Dropdown` sebelum `AL Multi-Dropdown`; spec mengikuti "Bersihkan lalu pilih" TC.
  - Email akun Total Control Company Alpha mengikuti pola Pre-setup #1; env var `FA_TC_PASSWORD` disediakan tim FE.
