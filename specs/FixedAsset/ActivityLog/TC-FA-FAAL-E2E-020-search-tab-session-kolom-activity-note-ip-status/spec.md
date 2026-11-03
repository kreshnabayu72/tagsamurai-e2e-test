---
id: TC-FA-FAAL-E2E-020-search-tab-session-kolom-activity-note-ip-status
title: "Search Tab Session: Activity, Note, IP Address, Device/Browser, dan Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-61
  - TC-FA-FAAL-62
  - TC-FA-FAAL-63
  - TC-FA-FAAL-64
coverage:
  web: automated
---

# Search Tab Session: Activity, Note, IP Address, Device/Browser, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah; Activity bernilai `Session` dan Status tampil `—` pada setiap baris. IP Address dan Device/Browser dipakai lewat keyword dan baris hasil yang disebut TC (`192.168.1` cocok SS-01, SS-02, SS-08, SS-09; `chrome` cocok SS-01, SS-02, SS-04, SS-10; `SAFARI` cocok SS-03 dan SS-11). Spec hanya membaca dan tidak mengubah data.
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

### TC-FA-FAAL-61: Search kolom Activity Tab Session mencocokkan seluruh baris

1. Klik icon Filter
2. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
3. Klik `[Apply]`
4. Ketik Search `session`, tekan Enter
5. Verifikasi seluruh 11 baris (SS-01 sampai SS-11) tetap tampil
6. Verifikasi teks pagination `Showing 1–10 of 11 entries`
7. Klik `(←)` pada kotak Search

### TC-FA-FAAL-62: Search kolom Note Tab Session

8. Ketik Search `limit`, tekan Enter
9. Verifikasi hanya SS-03 (Concurrent limit reached) tampil
10. Kosongkan isi kotak search, tekan Enter
11. Ketik Search `LOGGED OUT`, tekan Enter
12. Verifikasi hanya SS-04 (Logged out by admin) tampil
13. Kosongkan isi kotak search, tekan Enter
14. Ketik Search `ended`, tekan Enter
15. Verifikasi SS-02 dan SS-11 (Session ended) tampil
16. Klik `(←)` pada kotak Search

### TC-FA-FAAL-63: Search kolom IP Address dan Device/Browser Tab Session

17. Ketik Search `192.168.1`, tekan Enter
18. Verifikasi SS-01, SS-02, SS-08, dan SS-09 tampil
19. Kosongkan isi kotak search, tekan Enter
20. Ketik Search `chrome`, tekan Enter
21. Verifikasi SS-01, SS-02, SS-04, dan SS-10 tampil
22. Kosongkan isi kotak search, tekan Enter
23. Ketik Search `SAFARI`, tekan Enter
24. Verifikasi SS-03 dan SS-11 tampil
25. Klik `(←)` pada kotak Search

### TC-FA-FAAL-64: Search kolom Status Tab Session memakai nilai tampil

26. Ketik Search `Success`, tekan Enter
27. Verifikasi tampil Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
28. Verifikasi tidak ada baris tabel yang tampil (keyword `Success` tidak mencocokkan baris mana pun karena Status tampil `—`)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `Failed`, tekan Enter
31. Verifikasi tampil Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
32. Verifikasi tidak ada baris tabel yang tampil (keyword `Failed` tidak mencocokkan baris mana pun karena Status tampil `—`)
33. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1 sampai 3 (menerapkan Filter Date Jendela Seed Tab Session sesuai precondition d TC-FA-FAAL-61; filter tetap aktif untuk TC-FA-FAAL-62 sampai 64), langkah 7, 10, 13, 16, 19, 22, 25, 29, 33 (mengosongkan atau menutup kotak Search sebelum keyword atau kasus berikutnya).
- Expected b TC-FA-FAAL-64 (empty state) ditulis sebelum Expected a (tidak ada baris) karena empty state `No results found` hasil Search menjadi anchor positif untuk asersi absence baris (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAL-61 butir a ("seluruh 11 baris tetap tampil") tidak dapat diamati utuh pada halaman 1 (ukuran halaman 10); baris ke-11 berada di halaman 2. Spec mengasersi butir a dan memakai pagination (butir b) sebagai bukti jumlah.
  - Pre-setup #11 menyebut tepat 11 baris Tab Session (dan #12 tepat 15 baris Tab User Action) tanpa menyatakan bahwa login aktor (dan spec lain pada client yang sama) menambah baris `Session started` pada log permanen. Asersi hitungan (`Showing 1–10 of 11 entries`, 15 baris) hanya benar bila data Pre-setup berada di client yang terisolasi dari login lain; spec mengikuti TC.
  - Pre-setup #11 tidak menyebut IP Address dan Device/Browser SS-02, SS-04, dan SS-10; spec hanya mengasersi baris hasil yang disebut Expected TC-FA-FAAL-63.
