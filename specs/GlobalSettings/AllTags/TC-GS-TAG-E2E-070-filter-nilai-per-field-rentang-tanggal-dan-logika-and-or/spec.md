---
id: TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or
title: "Filter Registri: Nilai per Field, Rentang Last Scanned/Activated At Inklusif, dan Logika OR/AND"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-203
  - TC-GS-TAG-204
  - TC-GS-TAG-205
  - TC-GS-TAG-212
coverage:
  web: automated
---

# Filter Registri: Nilai per Field, Rentang Last Scanned/Activated At Inklusif, dan Logika OR/AND

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): filter registri dikosongkan dan visibilitas kolom dikembalikan ke default lewat `[Reset to Default]` Setup Column (Activated At tersembunyi).
- Tabel "Filter per field" (parameter langkah 3 sampai 6; jumlah baris dibaca dari teks pagination `Showing ... of N TAGs`):

| Field | Opsi yang dipilih | Hasil yang diharapkan |
|---|---|---|
| `TAG Type` | NFC | 3 baris |
| `Device Name` | `Alien H3 Tag` | 2 baris (DD-02, DD-08) |
| `Brand` | `Zebra` | 3 baris |
| `Model/Type` | `H3` | 3 baris |
| `Source` | Official | 24 baris |
| `Type` | User TAG | 1 baris (DD-02) |
| `Status` | Reserved | 1 baris (DD-06) |
| `Last Scanned In` | Fixed Asset | 3 baris |
| `Last User` | `Siti A` | 5 baris |

## Test Steps

### TC-GS-TAG-203: Filter per field multi-select searchable

1. Klik ikon Filter
2. Untuk setiap baris tabel "Filter per field" pada Prerequisites, lakukan langkah 3 sampai 6
3. Pilih opsi pada kolom "Opsi yang dipilih" untuk field pada baris itu
4. Klik `Apply`
5. Verifikasi tabel menampilkan jumlah baris sesuai kolom "Hasil yang diharapkan"
6. Klik `Clear Field`, lalu klik `Apply`

### TC-GS-TAG-204: Filter Last Scanned dengan rentang tanggal inklusif

7. Pilih rentang `12/09/26` s.d. `15/09/26` pada `Last Scanned`
8. Klik `Apply`
9. Verifikasi baris DD-04 (`12/09/26 09:05`, batas awal), DD-07 (`13/09/26 10:10`), DD-06 (`14/09/26 15:00`), dan DD-02 (`15/09/26 11:20`, batas akhir) tampil dan rentang inklusif
10. Pilih satu hari `16/09/26` s.d. `16/09/26` pada `Last Scanned`
11. Klik `Apply`
12. Verifikasi hanya baris DD-01 yang tampil
13. Verifikasi input tanggal terformat mengikuti Date Format General Settings (`16/09/26`)
14. Klik `Clear Field`, lalu klik `Apply`

### TC-GS-TAG-205: Multi-select dalam satu field memakai OR; antar field berbeda memakai AND

15. Pilih `TAG Type` = NFC dan GPS
16. Klik `Apply`
17. Verifikasi tabel menampilkan 4 baris (NFC atau GPS)
18. Tambahkan `Source` = Official
19. Klik `Apply`
20. Verifikasi tabel menampilkan 2 baris (NFC atau GPS, dan Official)
21. Klik `Clear Field`, lalu klik `Apply`

### TC-GS-TAG-212: Filter Activated At dengan rentang tanggal inklusif

22. Klik ikon Filter untuk menutup panel
23. Tampilkan kolom `Activated At` lewat overlay Column Visibility (⋯)
24. Klik ikon Filter untuk membuka panel
25. Verifikasi field `Activated At` berupa date range picker dengan placeholder `Select date`
26. Pilih rentang `09/09/26` s.d. `10/09/26` pada `Activated At`
27. Klik `Apply`
28. Verifikasi baris DD-01 (`10/09/26 08:00`, batas akhir) dan DD-02 (`09/09/26 09:15`, batas awal) tampil dan rentang inklusif
29. Klik `Clear Field`, lalu klik `Apply`
30. Klik ikon Filter untuk menutup panel
31. Sembunyikan kembali kolom `Activated At` lewat overlay Column Visibility (⋯)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (203, 204, 205, 212). TC-GS-TAG-201, 202, 206 sampai 211 (screening dan perilaku Filter Panel) ada di spec `TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply`. Spec ini tidak menghapus data.
- Panjang spec: 31 langkah tertulis (sekitar 63 langkah setelah ekspansi sembilan field pada langkah 3 sampai 6), di atas sekitar 35 langkah setelah ekspansi. Alasan dipertahankan: seluruh blok satu topik (nilai Filter) pada satu dataset (Seed Registri A) dan satu kelas harness biasa; langkah berulang memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7); tiap iterasi diakhiri `Clear Field` + `Apply` sehingga berdiri sendiri. `Verifikasi` yang diulang tetap satu per klausa. Langkah yang diulang: 3 sampai 6 (9 iterasi).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (mengosongkan filter setelah tiap field), langkah 14, 21, 29 (mengosongkan filter), langkah 22 sampai 24 (menampilkan kolom `Activated At`, precondition TC-GS-TAG-212 butir 3, lewat overlay Column Visibility), langkah 30 dan 31 (menutup panel dan memulihkan kolom).
- Pemisahan dari spec Filter Panel, Search, Sort, dan Pagination registri: kelas harness tidak sama dan tidak semua memakai data yang sama; ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Jumlah baris per field pada langkah 5 dan 17 sampai 20 diturunkan dari Seed Registri A dan teks pagination TC-GS-TAG-245; nilai hasilnya mengikuti Expected TC.
- Temuan untuk QA:
  - TC-GS-TAG-203 langkah 1 menulis "klik `Apply`, amati tabel, lalu `Clear Field` + `Apply`" untuk sembilan field dalam satu langkah tanpa menyebut apakah `Clear Field` mengosongkan seluruh panel; spec mengosongkan panel setelah tiap field (langkah 6).
  - TC-GS-TAG-204 butir a menyebut empat baris "tampil" tanpa menyatakan apakah hasil hanya empat baris; spec mengasersi keempat baris tampil dan batas inklusif, tanpa mengasersi jumlah total.
  - TC-GS-TAG-212 langkah 3 mensyaratkan kolom `Activated At` ditampilkan lewat Setup Column tanpa menyebut waktunya; spec menampilkannya sebelum membuka panel (langkah 23).
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
