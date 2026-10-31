---
id: TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user
title: "Sort Registri: Kolom Badge Alfabetis, Kolom Tanggal Oldest/Newest First, dan Last User Berdasarkan Nama Lengkap"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-223
  - TC-GS-TAG-224
  - TC-GS-TAG-225
coverage:
  web: automated
---

# Sort Registri: Kolom Badge Alfabetis, Kolom Tanggal Oldest/Newest First, dan Last User Berdasarkan Nama Lengkap

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data. Tiap kolom yang diuji punya sedikitnya dua nilai distinct (S-11): Status (tujuh nilai), Brand, Model/Type, Last Scanned In (`Fixed Asset`, `Global Settings`, `Supply Asset`), Last Scanned (sepuluh timestamp), Activated At, dan Last User (`Budi S` = Budi Santoso dan `Siti A` = Siti Amalia).
- Nilai batas untuk langkah tanggal (dari Seed Registri A, tanpa kembar pada ujung urutan):

| Kolom | Oldest First: baris pertama | Newest First: baris pertama |
|---|---|---|
| `Last Scanned` | DD-08 (`01/09/26 12:00`); baris tanpa tanggal (`—`) di akhir | DD-01 (`16/09/26 14:30`); baris tanpa tanggal (`—`) di akhir |
| `Activated At` | DD-15 (`01/08/26 08:00`) | DD-03 (`15/09/26 13:00`) |

- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): Sort dikembalikan netral, Rows per page dikembalikan ke 10, visibilitas kolom dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; Last Scanned In, Activated At, Last User tersembunyi).
- Kemampuan teknis: membaca indikator sort pada header kolom dan urutan baris tabel; Rows per page 50 dipakai supaya seluruh 30 baris tampil pada satu halaman (langkah 1).

## Test Steps

### Persiapan (precondition TC-GS-TAG-223 butir d, 224 butir d, dan 225 butir d)

1. Ubah Rows per page menjadi 50 (seluruh 30 baris tampil pada satu halaman)
2. Buka overlay Column Visibility lewat header kolom Actions (⋯), centang `Last Scanned In`, `Activated At`, dan `Last User`, lalu tutup overlay

### TC-GS-TAG-223: Sort kolom badge alfabetis

3. Klik header `Status` sekali
4. Verifikasi `Status` ascending alfabetis berurutan `Available`, `Damaged/Missing`, `Paired`, `Reserved`, `Retired`, `To be Returned`, `Waiting for Approval` (bukan urutan lifecycle)
5. Klik header `Brand` sekali
6. Verifikasi `Brand` ascending alfabetis
7. Klik header `Model/Type` sekali
8. Verifikasi `Model/Type` ascending alfabetis
9. Klik header `Last Scanned In` sekali
10. Verifikasi `Last Scanned In` ascending alfabetis
11. Klik header `Last Scanned In` dua kali lagi (kembali netral)

### TC-GS-TAG-224: Sort kolom tanggal Oldest First dan Newest First

12. Klik header `Last Scanned` sekali
13. Verifikasi urutan `Oldest First` pada `Last Scanned` (baris pertama DD-08 `01/09/26 12:00`, baris terakhir yang bertanggal DD-01 `16/09/26 14:30`)
14. Verifikasi baris dengan Last Scanned `—` berada di akhir daftar pada arah `Oldest First`
15. Klik header `Last Scanned` (klik #2)
16. Verifikasi urutan `Newest First` pada `Last Scanned` (baris pertama DD-01 `16/09/26 14:30`, baris terakhir yang bertanggal DD-08 `01/09/26 12:00`)
17. Verifikasi baris dengan Last Scanned `—` tetap berada di akhir daftar pada arah `Newest First`
18. Klik header `Last Scanned` (klik #3, kembali netral)
19. Klik header `Activated At` sekali
20. Verifikasi urutan `Oldest First` pada `Activated At` (baris pertama DD-15 `01/08/26 08:00`, baris terakhir DD-03 `15/09/26 13:00`)
21. Klik header `Activated At` (klik #2)
22. Verifikasi urutan `Newest First` pada `Activated At` (baris pertama DD-03 `15/09/26 13:00`, baris terakhir DD-15 `01/08/26 08:00`)
23. Verifikasi setiap baris `Activated At` berisi tanggal (tidak ada nilai kosong, sehingga tidak ada penempatan khusus)
24. Klik header `Activated At` (klik #3, kembali netral)

### TC-GS-TAG-225: Sort kolom Last User berdasarkan nama lengkap

25. Klik header `Last User` sekali
26. Verifikasi `Last User` ascending berdasarkan nama lengkap A-Z: baris `Budi S` (Budi Santoso) berada sebelum baris `Siti A` (Siti Amalia)
27. Klik header `Last User` dua kali lagi (kembali netral)
28. Buka overlay Column Visibility, hapus centang `Last Scanned In`, `Activated At`, dan `Last User`, lalu tutup overlay
29. Ubah Rows per page kembali menjadi 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (223, 224, 225). TC-GS-TAG-221, 222, 226 (kolom teks, ikon TAG Type, kolom Actions) ada di spec `TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions`. Spec tidak mengubah data dan tidak menghapus apa pun.
- Panjang spec: 29 langkah, di bawah sekitar 35 langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 29 (Rows per page 50 supaya seluruh baris terlihat, lalu dipulihkan), langkah 2 dan 28 (menampilkan dan menyembunyikan kolom curated, precondition TC butir d), langkah 11, 18, 24, 27 (mengembalikan sort ke netral).
- Nilai batas urutan tanggal (DD-08, DD-01, DD-15, DD-03) diturunkan dari Seed Registri A; Expected TC hanya menyebut `Oldest First`, `Newest First`, dan penempatan nilai kosong.
- Pemisahan dari spec topik registri lain (Search, Filter, Sort, Pagination, Setup Column): ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Temuan untuk QA:
  - TC-GS-TAG-224 butir a menyebut `Oldest First` dan `Newest First` tanpa menyatakan apakah itu label yang tampil (tooltip atau caption sort) atau hanya nama arah; spec mengasersi arah urutan berdasarkan nilai timestamp.
  - Seed Registri A memuat dua baris dengan Last Scanned dan Activated At sama persis (DD-11 dan DD-13: `09/09/26 13:30` dan `02/09/26 10:00`); TC tidak menetapkan urutan sekunder, sehingga spec tidak mengasersi urutan relatif kedua baris itu.
  - TC-GS-TAG-223 tidak menyebut penempatan nilai kosong untuk `Brand`, `Model/Type`, dan `Last Scanned In` (baris QR tanpa nilai); NC-03 hanya membahas Last Scanned, SKU, dan Type. Spec tidak mengasersi penempatan kosong pada ketiga kolom itu.
  - TC-GS-TAG-225 data ujinya (`Budi S` sebelum `Siti A`) konsisten dengan urutan nama lengkap dan urutan singkatan, sehingga asersi tidak membedakan sort berdasarkan nama lengkap dari sort berdasarkan teks tampil; perlu data uji yang urutannya berbeda di kedua bentuk.
  - TC-GS-TAG-223 sampai 225 tidak menyebut ukuran halaman; spec menaikkan Rows per page menjadi 50 (langkah 1).
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
