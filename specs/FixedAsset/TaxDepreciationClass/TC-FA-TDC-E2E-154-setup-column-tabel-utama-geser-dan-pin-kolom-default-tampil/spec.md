---
id: TC-FA-TDC-E2E-154-setup-column-tabel-utama-geser-dan-pin-kolom-default-tampil
title: "Setup Column Tabel Utama: Geser dan Pin Kolom yang Tampil Secara Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-542
  - TC-FA-TDC-543
coverage:
  web: automated
---

# Setup Column Tabel Utama: Geser dan Pin Kolom yang Tampil Secara Default

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Konfigurasi kolom awal adalah default: 10 kolom tampil berurutan seperti pada tabel parameter, tiga kolom (`Regulation Reference`, `Modified By`, `Last Updated`) tersembunyi.
- Tabel parameter perulangan TC-FA-TDC-542 dan TC-FA-TDC-543 (kolom tampil secara default), literal TC:

  | Kolom | Posisi semula |
  |---|---|
  | `Active` | 1 |
  | `Class Code` | 2 |
  | `Class Name` | 3 |
  | `Asset Type` | 4 |
  | `Useful Life (years)` | 5 |
  | `Straight Line Rate` | 6 |
  | `Declining Balance Rate` | 7 |
  | `Allowed Methods` | 8 |
  | `Used By` | 9 |
  | `Effective From` | 10 |

- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Popup Setup Column dengan seret kolom (drag) dan icon Pin; viewport yang membuat tabel dapat di-scroll horizontal; muat ulang halaman (F5); preferensi kolom tersimpan di browser dan dihapus di hook `after` (`suite.md`); pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel utama (urutan dan Pin; dipulihkan di tiap iterasi dengan menggeser kembali dan Unpin). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Geser urutan kolom di Popup Setup Column (TC-FA-TDC-542)

Untuk setiap baris tabel parameter pada Prerequisites, lakukan langkah 1 sampai 12.

1. Klik icon `⋯` pada header kolom Actions
2. Klik `Setup Column...`
3. Seret kolom pada baris tabel ke posisi paling atas daftar
4. Verifikasi Live Preview menempatkan kolom sebagai kolom pertama
5. Klik `[Save]`
6. Verifikasi urutan tabel sama dengan Live Preview (kolom sebagai kolom pertama)
7. Refresh halaman (F5)
8. Verifikasi urutan tabel tetap sama setelah F5
9. Klik icon `⋯` pada header kolom Actions
10. Klik `Setup Column...`
11. Seret kolom kembali ke posisi semula pada baris tabel
12. Klik `[Save]`

### Pin dan unpin kolom di Popup Setup Column (TC-FA-TDC-543)

Untuk setiap baris tabel parameter pada Prerequisites, lakukan langkah 13 sampai 27.

13. Klik icon `⋯` pada header kolom Actions
14. Klik `Setup Column...`
15. Klik icon Pin pada baris kolom
16. Klik `[Save]`
17. Scroll tabel horizontal
18. Verifikasi kolom membeku (sticky) saat tabel di-scroll horizontal
19. Refresh halaman (F5)
20. Scroll tabel horizontal
21. Verifikasi kolom tetap membeku setelah F5
22. Klik icon `⋯` pada header kolom Actions
23. Klik `Setup Column...`
24. Klik icon Pin kolom yang sama (Unpin)
25. Klik `[Save]`
26. Scroll tabel horizontal
27. Verifikasi kolom ikut bergeser saat scroll

## Notes

- Langkah penghubung (S-03): langkah 9 sampai 12 pada tiap iterasi (menggeser kolom kembali ke posisi semula dan `[Save]`; pemulihan Setup Column, 8b.14, R-24), langkah 17, 20, dan 26 ("Scroll tabel horizontal" adalah aksi TC-FA-TDC-543 yang diulang sesudah F5 dan Unpin supaya asersi sticky bermakna; S-14). Hook `after` hanya cadangan.
- Perulangan langkah 1 sampai 12 dan 13 sampai 27 memakai idiom "Untuk setiap baris tabel ... (langkah X sampai Y)" (8b.7); `Verifikasi` yang diulang tetap satu per klausa. Untuk kolom `Active` (posisi 1), seret ke posisi paling atas tidak mengubah urutan; TC tetap memintanya sehingga langkah 3 sampai 8 diasersi apa adanya.
- Spec ini 27 langkah nominal dan sekitar 270 langkah setelah ekspansi perulangan (10 kolom kali 27 langkah), di atas ~35 langkah. Alasan: satu topik (Setup Column tabel utama, geser dan Pin kolom yang tampil secara default) pada dataset Example Data yang sama, tiap iterasi kolom berdiri sendiri (kegagalan satu kolom tidak membuat kolom lain kehilangan makna), dan perulangan per kolom mengikuti idiom 8b.7 dengan parameter di Prerequisites; S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - TC-FA-TDC-543 Expected "tetap membeku setelah F5" tidak menyebut scroll sesudah F5; spec menambah langkah scroll (langkah 20).
  - TC-FA-TDC-542 dan 543 tidak menyebut viewport atau lebar tabel yang memungkinkan scroll horizontal; spec menuliskannya sebagai kemampuan teknis.
  - TC-FA-TDC-542 langkah 3 menyebut "drag kolom ke posisi paling atas" tanpa mengecualikan kolom yang sudah di posisi pertama (`Active`).
  - TC-FA-TDC-542 dan 543 tidak menyebut apakah Popup Setup Column menutup sesudah `[Save]`; spec mengasumsikan menutup.
  - Email akun Total Control tidak tertulis di TC.
