---
id: TC-FA-LIC-E2E-071-allocation-history-search-non-searchable-trim-terikat
title: "Allocation History: Search Guard Kolom Tanggal, Trim Spasi Tepi, dan Terikat Visibilitas Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-233
  - TC-FA-LIC-234
  - TC-FA-LIC-235
coverage:
  web: automated
---
# Allocation History: Search Guard Kolom Tanggal, Trim Spasi Tepi, dan Terikat Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Anggota guard kolom non-searchable (TC-FA-LIC-233, parameter langkah 2 sampai 4): Date `20/07/26`, End Date `31/12/26`, dan Last Updated `14:10`; hasil ketiganya empty state `No results found`.
- State yang diubah dan dipulihkan: Search tabel Allocation History (dikosongkan pada langkah 8 dan 17) dan visibilitas kolom `License Type` (dipulihkan pada langkah 14).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-233: Guard kolom non-searchable

Untuk setiap anggota guard kolom non-searchable (langkah 2 sampai 4):

2. Ketik Search nilai anggota, tekan Enter
3. Verifikasi tabel menampilkan empty state `No results found` (kolom tidak dicari; penyaringan lewat Filter Panel)
4. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-234: Trim spasi tepi

5. Ketik Search `  20250210  ` (spasi di awal dan akhir, huruf kapital), tekan Enter
6. Verifikasi tabel menampilkan: LALC-20250210-00001
7. Verifikasi isi kotak Search di layar tetap `  20250210  ` (spasi tepi tetap terlihat)
8. Klik `(←)` pada kotak Search

### TC-FA-LIC-235: Search terikat visibilitas kolom

9. Ketik Search `Addon (IT`, tekan Enter
10. Verifikasi hasil awal: LALC-20260801-00004
11. Klik header kolom Actions `⋯`, hilangkan centang kolom `License Type`, lalu tutup overlay Column Visibility
12. Ulangi pencarian: ganti isi kotak search dengan `Addon (IT`, tekan Enter
13. Verifikasi tabel menampilkan empty state `No results found` (pencarian tidak mencocokkan baris melalui kolom `License Type` yang disembunyikan; tidak ada kolom lain yang memuat `Addon (IT`)
14. Klik header kolom Actions `⋯`, centang kembali kolom `License Type`, lalu tutup overlay Column Visibility
15. Ulangi pencarian: ganti isi kotak search dengan `Addon (IT`, tekan Enter
16. Verifikasi hasil kembali seperti awal: LALC-20260801-00004
17. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- TC-FA-LIC-236, 237, dan 238 (siklus sort per kelas kolom) ada di spec 137.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 4 (mengosongkan Search antar anggota), langkah 8 dan 17 (mengosongkan Search; S-09), langkah 14 (memulihkan kolom `License Type`; S-09).
- Asersi di luar Expected TC (S-03): hasil awal TC-FA-LIC-235 diturunkan dari Pre-setup #13 (hanya LALC-20260801-00004 bertipe `Addon (IT Inventory)`).
- Temuan untuk QA:
  - TC-FA-LIC-233 memakai nilai Date `20/07/26`, End Date `31/12/26`, dan Last Updated `14:10` yang tidak diketahui pasti apakah ada pada Pre-setup #13; kolom tanggal non-searchable sehingga hasil tetap kosong. Spec mengikuti TC.
  - TC-FA-LIC-233, 234, dan 235 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
