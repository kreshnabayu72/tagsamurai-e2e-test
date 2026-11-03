---
id: TC-FA-FAAL-E2E-021-search-tab-session-date-tanpa-hasil-tersembunyi-dan-trim
title: "Search Tab Session: Date, Tanpa Hasil, dan Kolom Tersembunyi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-65
  - TC-FA-FAAL-66
  - TC-FA-FAAL-67
coverage:
  web: automated
---

# Search Tab Session: Date, Tanpa Hasil, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah. Spec hanya membaca dan tidak mengubah data.
- Visibilitas kolom Note diubah lewat overlay Column Visibility pada langkah 16 dan dipulihkan pada langkah 22; bila spec gagal di tengah, hook `after` menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`).
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

| Baris | User (nama lengkap) | Employee ID | Position | Division | Note | Tanggal (Asia/Jakarta) |
|---|---|---|---|---|---|---|
| SS-01 | John Doe | EMP001 | Staff | Marketing | Session started | 14/07/26 08:05 |
| SS-02 | John Doe | EMP001 | Staff | Marketing | Session ended | 14/07/26 09:30 |
| SS-03 | Siti Nurbaya (tampil `Siti N`) | EMP002 | Manager | Finance | Concurrent limit reached | 14/07/26 10:00 |
| SS-04 | Mike Tan | EMP003 | Staff | Operations | Logged out by admin | 14/07/26 14:00 |
| SS-05 | Jane Smith | kosong | kosong | Finance | Session started | 15/07/26 08:00 |
| SS-06 | Budi Santoso (tampil `Budi S`) | EMP004 | Supervisor | Operations | Session started | 15/07/26 09:00 |
| SS-07 | Dewi Lestari | EMP005 | Staff | Marketing | Session started | 15/07/26 10:00 |
| SS-08 | Hendra Pratama (pengguna pertama) | EMP006 | Staff | Marketing | Session started | 15/07/26 11:00 |
| SS-09 | Hendra Pratama (pengguna kedua) | EMP007 | Manager | Finance | Session started | 15/07/26 12:00 |
| SS-10 | John Dalton | EMP008 | Staff | Operations | Session started | 16/07/26 08:00 |
| SS-11 | John Davis | EMP009 | Supervisor | Finance | Session ended | 16/07/26 09:00 |

## Test Steps

### TC-FA-FAAL-65: Search tidak mencocokkan kolom Date Tab Session

1. Ketik Search `14/07/26`, tekan Enter
2. Verifikasi state `No results found` tampil (kolom Date tidak Searchable)
3. Kosongkan isi kotak search, tekan Enter
4. Ketik Search `Jul`, tekan Enter
5. Verifikasi state `No results found` tampil (kolom Date tidak Searchable)
6. Klik `(←)` pada kotak Search
7. Klik icon Filter
8. Verifikasi penyaringan tanggal tersedia lewat field Date di Filter Panel
9. Klik icon Filter untuk menutup Filter Panel

### TC-FA-FAAL-66: Search tanpa hasil di Tab Session menampilkan state kosong terfilter

10. Ketik Search `zzzz`, tekan Enter
11. Verifikasi tampil Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
12. Verifikasi tidak ada baris tabel dan tidak ada pesan error
13. Verifikasi pagination tidak menampilkan baris data
14. Klik `(←)` pada kotak Search

### TC-FA-FAAL-67: Search tidak mencari kolom Note yang disembunyikan

15. Klik header Actions (⋯)
16. Hilangkan centang kolom Note di overlay Column Visibility
17. Tutup overlay Column Visibility
18. Ketik Search `limit`, tekan Enter
19. Verifikasi state `No results found` tampil (keyword `limit` tidak mencocokkan baris mana pun saat Note disembunyikan)
20. Kosongkan isi kotak search, tekan Enter
21. Klik header Actions (⋯)
22. Centang kembali kolom Note di overlay Column Visibility
23. Tutup overlay Column Visibility
24. Ketik Search `limit`, tekan Enter
25. Verifikasi SS-03 tampil
26. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 3, 6, 9, 14, 17, 20, 23, dan 26 (mengosongkan atau menutup kotak Search, menutup overlay Column Visibility, dan menutup Filter Panel).
- Langkah 7 (klik icon Filter) dan 8 (`Verifikasi` field Date) menjadi pengamatan untuk Expected b TC-FA-FAAL-65 ("penyaringan tanggal hanya melalui field Date di Filter Panel"), karena TC tidak memberi langkah pengamatannya (S-14).
- TC-FA-FAAL-68 (trim spasi kedua tab) ada di spec 080.
- Temuan untuk QA:
  - Pre-setup #11 menyebut tepat 11 baris Tab Session (dan #12 tepat 15 baris Tab User Action) tanpa menyatakan bahwa login aktor (dan spec lain pada client yang sama) menambah baris `Session started` pada log permanen. Asersi hitungan (`Showing 1–10 of 11 entries`, 15 baris) hanya benar bila data Pre-setup berada di client yang terisolasi dari login lain; spec mengikuti TC.
  - TC-FA-FAAL-65 Expected b ("penyaringan tanggal hanya melalui field Date di Filter Panel") berupa pernyataan aturan tanpa langkah uji; spec mengamati keberadaan field Date (langkah 8).
