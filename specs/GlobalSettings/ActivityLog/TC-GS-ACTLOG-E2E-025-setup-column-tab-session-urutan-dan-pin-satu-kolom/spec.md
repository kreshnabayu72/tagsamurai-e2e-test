---
id: TC-GS-ACTLOG-E2E-025-setup-column-tab-session-urutan-dan-pin-satu-kolom
title: "Setup Column Tab Session: Urutan dan Pin Satu Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-97
  - TC-GS-ACTLOG-98
coverage:
  web: automated
---

# Setup Column Tab Session: Urutan dan Pin Satu Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Data Pre-setup dan Data Dinamis: tidak ada seeding. Tabel Tab Session memuat baris Login akun aktor dari hook `before` dan log lain entitas.
- Preferensi kolom tab Session (visibilitas, urutan, pin) tersimpan di cache browser (TC-GS-ACTLOG-95 butir b), bukan lewat API, sehingga tidak ada endpoint yang dipakai untuknya. "Muat ulang halaman (F5)" dilakukan pada konteks browser yang sama supaya cache tetap ada.
- Data uji TC-GS-ACTLOG-97 dan 98 (sepuluh kolom, satu per iterasi):

  | No | Kolom |
  |---|---|
  | 1 | `Date` |
  | 2 | `User` |
  | 3 | `Employee ID` |
  | 4 | `Position` |
  | 5 | `Division` |
  | 6 | `Activity` |
  | 7 | `Status` |
  | 8 | `Note` |
  | 9 | `IP Address` |
  | 10 | `Device / Browser` |

- Lebar viewport untuk TC-GS-ACTLOG-98: tabel dapat digulir horizontal. Nilai lebar ditetapkan tim FE (contoh 1024 px) dan diatur di langkah 12; viewport dipulihkan di langkah 25.
- Kemampuan teknis: drag and drop baris kolom di Popup Setup Column; mengatur viewport; menggulir tabel secara horizontal dan membaca kolom yang membeku; memuat ulang halaman pada konteks browser yang sama.
- State global yang dipulihkan (di langkah 11, 25, dan hook `after` yang tetap jalan walau spec gagal di tengah): konfigurasi kolom tab Session dikembalikan ke default (sepuluh kolom tampil berurutan seperti pada Data uji, tanpa pin) lewat `[Reset to Default]` atau penghapusan key cache tab Session; viewport dikembalikan ke ukuran awal. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-97: Geser urutan kolom lewat Popup Setup Column

2. Untuk setiap baris tabel Data uji (langkah 2 sampai 11): buka Popup Setup Column (klik header `Column Visibility (⋯)`, klik `Setup Column...`), lalu seret baris kolom ke posisi paling atas
3. Verifikasi kolom menjadi kolom pertama di tabel di balik popup
4. Klik `[Save]`
5. Verifikasi kolom menjadi kolom pertama di tabel setelah `[Save]`
6. Muat ulang halaman (F5)
7. Verifikasi kolom tetap menjadi kolom pertama di tabel setelah F5
8. Buka Popup Setup Column
9. Klik `[Reset to Default]`
10. Klik `[Save]`
11. Verifikasi urutan kolom kembali ke default

### TC-GS-ACTLOG-98: Pin dan Unpin satu kolom lewat Popup Setup Column

12. Atur lebar viewport sehingga tabel dapat digulir horizontal
13. Untuk setiap baris tabel Data uji (langkah 13 sampai 24): buka Popup Setup Column, lalu klik icon Pin pada baris kolom
14. Klik `[Save]`
15. Gulir tabel ke kanan
16. Verifikasi kolom membeku di sisi kiri saat tabel digulir horizontal
17. Muat ulang halaman (F5)
18. Gulir tabel ke kanan
19. Verifikasi kolom tetap membeku di sisi kiri setelah F5
20. Buka Popup Setup Column
21. Klik icon Pin pada baris kolom lagi
22. Klik `[Save]`
23. Gulir tabel ke kanan
24. Verifikasi kolom ikut tergulir setelah Unpin

### Pemulihan state akhir

25. Kembalikan lebar viewport ke ukuran awal

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Setup Column Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-94 (prasyarat kedua TC) ada di spec 024 dan TC-GS-ACTLOG-99 (bergantung pada TC-GS-ACTLOG-98) ada di spec 026.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (mengatur viewport untuk precondition TC-GS-ACTLOG-98), langkah 18 (menggulir ulang tabel setelah F5 karena muat ulang mengembalikan posisi gulir; S-14), dan langkah 25 (memulihkan viewport; hook `after` sebagai cadangan). Langkah 2 dan 13 membuka popup di tiap iterasi karena `[Save]` menutup popup; TC hanya menulis pembukaan popup sekali. Langkah sesudah `[Save]` pertama pada TC-GS-ACTLOG-97 memisahkan asersi "setelah [Save]" dari "setelah F5" pada Expected TC-GS-ACTLOG-97 (S-01).
- Langkah 2 sampai 11 dan 13 sampai 24 berulang untuk setiap baris tabel Data uji di Prerequisites.
- Spec memiliki 25 langkah nominal dan 223 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: kedua TC satu kelas harness (Setup Column Tab Session pada akun dan tabel yang sama), ekspansi berasal dari dua perulangan per kolom tanpa langkah bersyarat, dan sebagian besar langkah adalah `Verifikasi` hasil pemecahan klausa Expected (S-01).
- Temuan untuk QA:
  - TC-GS-ACTLOG-97 menyuruh menyeret tiap kolom ke posisi paling atas, termasuk `Date` yang sudah berada di posisi pertama pada urutan default; untuk `Date` langkah seret tidak mengubah urutan dan asersi "menjadi kolom pertama" sudah benar sebelum seret.
  - TC-GS-ACTLOG-98 tidak menyebut lebar viewport yang membuat tabel dapat digulir horizontal; nilai ditetapkan tim FE di Prerequisites.
