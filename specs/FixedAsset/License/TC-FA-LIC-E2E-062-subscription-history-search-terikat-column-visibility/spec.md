---
id: TC-FA-LIC-E2E-062-subscription-history-search-terikat-column-visibility
title: "Subscription History: Sort Default, Search Terikat Visibilitas Kolom, dan Berpindah Kolom Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-194
  - TC-FA-LIC-197
  - TC-FA-LIC-198
coverage:
  web: automated
---
# Subscription History: Sort Default, Search Terikat Visibilitas Kolom, dan Berpindah Kolom Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- State yang diubah dan dipulihkan: visibilitas kolom `Plan` (dipulihkan pada langkah 9), Search (ditutup pada langkah 12 dan 20), dan Sort kolom `Plan Owner` (dinetralkan pada langkah 21).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-197: Sort default

2. Verifikasi urutan baris awal: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001
3. Verifikasi indikator sort aktif pada kolom `Start Date`

### TC-FA-LIC-194: Search terikat visibilitas kolom

4. Ketik Search `Enterprise`, tekan Enter
5. Verifikasi hasil awal: SUBS-20241201-00001
6. Klik header kolom Actions `⋯`, hilangkan centang kolom `Plan`, lalu tutup overlay Column Visibility
7. Ulangi pencarian: ganti isi kotak search dengan `Enterprise`, tekan Enter
8. Verifikasi tabel menampilkan empty state `No results found` (pencarian tidak mencocokkan baris melalui kolom `Plan` yang disembunyikan; tidak ada kolom lain yang memuat `Enterprise`)
9. Klik header kolom Actions `⋯`, centang kembali kolom `Plan`, lalu tutup overlay Column Visibility
10. Ulangi pencarian: ganti isi kotak search dengan `Enterprise`, tekan Enter
11. Verifikasi hasil kembali seperti awal: SUBS-20241201-00001
12. Klik `(←)` pada kotak Search

### TC-FA-LIC-198: Berpindah kolom sort

13. Klik header `Subscription ID` sekali
14. Klik header `Plan Owner` sekali
15. Verifikasi kolom `Subscription ID` kembali netral (tanpa indikator sort)
16. Verifikasi kolom `Plan Owner` memulai dari Ascending
17. Ketik Search `Active`, tekan Enter
18. Klik header `Plan Owner` sekali lagi (mengubah arah sort)
19. Verifikasi kata kunci Search `Active` tetap aktif dan tabel tetap menampilkan SUBS-20260101-00001
20. Klik `(←)` pada kotak Search
21. Klik header `Plan Owner` sekali lagi hingga netral

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- TC-FA-LIC-195 dan TC-FA-LIC-196 (siklus sort tiga status per kelas kolom) ada di spec 138. Urutan TC dalam spec: 197, 194, 198 (sort default diamati sebelum state diubah; kasus yang mengubah sort di akhir).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 9 (memulihkan kolom `Plan`; S-09), langkah 12 dan 20 (mengosongkan Search; S-09), langkah 21 (menetralkan sort; S-09).
- Asersi di luar Expected TC (S-03): TC-FA-LIC-198 menulis "Terapkan Search `Active`; ubah arah sort"; hasil tabel SUBS-20260101-00001 pada asersi "Search tidak direset" diturunkan dari Pre-setup #13 (hanya term Active).
- Temuan untuk QA:
  - TC-FA-LIC-194 menulis hasil `Plan` disembunyikan "empty state `No results found` bila tidak ada kolom lain yang cocok"; pada Pre-setup #13 tidak ada kolom lain yang memuat `Enterprise`, sehingga spec mengasersi empty state.
  - TC-FA-LIC-198 menulis "Terapkan Search `Active`; ubah arah sort pada kolom `Plan Owner`" tanpa menyebut arah akhir; spec mengklik header sekali lagi (Descending) dan tidak mengasersi arah akhir karena tidak ada di Expected.
  - TC-FA-LIC-194, 197, dan 198 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
