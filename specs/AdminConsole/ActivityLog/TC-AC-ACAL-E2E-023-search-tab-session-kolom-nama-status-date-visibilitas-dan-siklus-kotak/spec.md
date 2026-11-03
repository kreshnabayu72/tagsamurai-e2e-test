---
id: TC-AC-ACAL-E2E-023-search-tab-session-kolom-nama-status-date-visibilitas-dan-siklus-kotak
title: "Search Tab Session: Kolom, Nama Lengkap, Status, Date, Visibilitas Kolom, dan Siklus Kotak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-49
  - TC-AC-ACAL-50
  - TC-AC-ACAL-51
  - TC-AC-ACAL-52
  - TC-AC-ACAL-53
  - TC-AC-ACAL-54
coverage:
  web: automated
---

# Search Tab Session: Kolom, Nama Lengkap, Status, Date, Visibilitas Kolom, dan Siklus Kotak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 9 dan 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): `John Doe` (EMP001, Staff, Marketing) dan `Jane Smith` (EMP002, tanpa Position, Finance). Tidak ada Data Dinamis.
- Data log (entri Session contoh PRD; seed BE). Baris diidentifikasi lewat User, Note, dan IP Address:

  | Kode | User | Employee ID | Position | Division | Note | IP Address | Device / Browser | Date |
  |---|---|---|---|---|---|---|---|---|
  | e1 | `John Doe` (`John D`) | `EMP001` | `Staff` | `Marketing` | `Session started` | `192.0.2.10` | `Chrome on Windows` | terbaru |
  | e2 | `John Doe` (`John D`) | `EMP001` | `Staff` | `Marketing` | `Session ended` | `192.0.2.10` | `Chrome on Windows` | terbaru |
  | e3 | `Jane Smith` (`Jane S`) | `EMP002` | `—` | `Finance` | `Session ended` | `2001:db8::1a` | `Safari on macOS` | terbaru |
  | e4 | `John Doe` (`John D`) | `EMP001` | `Staff` | `Marketing` | `Session started` | `192.0.2.10` | `Chrome on Windows` | `18 Jun 2026` (zona waktu tampilan General Settings) |

- Data uji TC-AC-ACAL-50 (kata kunci per kolom; baris "tidak tampil" bertanda `-` dilewati):

  | Kolom | Kata kunci | Baris yang tampil | Baris yang tidak tampil |
  |---|---|---|---|
  | Employee ID | `emp00` | baris e1 (`EMP001`) dan e3 (`EMP002`) | - |
  | Position | `staff` | baris e1 (Position `Staff`) | baris e3 (Position `—`) |
  | Division | `FINANCE` | baris e3 (Division `Finance`) | baris e1 (Division `Marketing`) |
  | Activity | `session` | baris e1, e2, dan e3 (Activity selalu `Session`) | - |
  | Note | `ended` | baris e2 dan e3 (`Session ended`) | baris e1 (`Session started`) |
  | IP Address | `2001:db8` | baris e3 (`2001:db8::1a`) | baris e1 (`192.0.2.10`) |
  | Device / Browser | `safari` | baris e3 (`Safari on macOS`) | baris e1 (`Chrome on Windows`) |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dengan Date `18 Jun 2026` dan nilai IP Address serta Device / Browser pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); menelusuri halaman bila baris tidak berada di halaman pertama.
- State global yang diubah: visibilitas kolom Division (langkah 39 sampai 48) dipulihkan di langkah 46; preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE, didaftarkan di `suite.md`). Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACAL-49: Siklus kotak Search

1. Verifikasi tabel menampilkan sedikitnya satu baris
2. Klik icon Search
3. Verifikasi input Search terbuka
4. Verifikasi kursor fokus di input Search
5. Verifikasi placeholder input Search `Search session log...`
6. Ketik `John` di kotak Search tanpa menekan Enter
7. Verifikasi icon `✕` muncul di kotak Search
8. Verifikasi tabel belum tersaring (baris `Jane S` masih tampil)
9. Tekan Enter
10. Verifikasi tabel tersaring keyword `John` (baris `John D` tampil dan baris `Jane S` tidak tampil)
11. Klik `✕` pada kotak Search
12. Verifikasi input Search kosong
13. Verifikasi input Search tetap terbuka
14. Verifikasi tabel masih hasil `John` (baris `Jane S` tidak tampil)
15. Tekan Enter pada input kosong
16. Verifikasi tabel kembali ke semua data (baris `John D` dan `Jane S` tampil)
17. Ketik Search `  John  ` (spasi di awal dan akhir), tekan Enter
18. Verifikasi hasil sama dengan kata kunci `John` (baris `John D` tampil dan baris `Jane S` tidak tampil)
19. Klik `←` pada kotak Search
20. Verifikasi input Search tertutup
21. Verifikasi tabel langsung kembali ke semua data (baris `John D` dan `Jane S` tampil; keyword kosong)

### TC-AC-ACAL-50: Search substring dan tidak membedakan huruf besar kecil per kolom

22. Untuk setiap baris tabel Data uji TC-AC-ACAL-50 (langkah 22 sampai 25): ketik Search kata kunci kolom, tekan Enter
23. Verifikasi baris pada kolom "Baris yang tampil" tampil
24. Verifikasi baris pada kolom "Baris yang tidak tampil" tidak tampil (kolom bertanda `-` dilewati)
25. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-51: Search kolom User mencocokkan nama lengkap

26. Ketik Search `doe`, tekan Enter
27. Verifikasi baris `John D` ditemukan
28. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-52: Search kolom Status memakai nilai tampil

29. Ketik Search `Success`, tekan Enter
30. Verifikasi tampil `No results found`
31. Ganti isi kotak search dengan `Failed`, tekan Enter
32. Verifikasi tampil `No results found`
33. Ganti isi kotak search dengan `—`, tekan Enter
34. Verifikasi semua baris tampil (baris `John D` dan `Jane S` tampil, bukan `No results found`)
35. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-53: Kolom Date tidak dapat dicari

36. Ketik Search `18 Jun 2026`, tekan Enter
37. Verifikasi tampil `No results found`
38. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-54: Kolom yang di-hide tidak ikut dicari

39. Klik header `⋯`
40. Hilangkan centang kolom `Division` di Overlay Column Visibility
41. Verifikasi kolom `Division` hilang dari tabel
42. Tutup Overlay Column Visibility
43. Verifikasi baris `Jane S` tampil di tabel
44. Ganti isi kotak search dengan `Finance`, tekan Enter
45. Verifikasi baris yang hanya cocok di Division (baris `Jane S`) tidak tampil
46. Klik header `⋯`, ceklis kembali kolom `Division` di Overlay Column Visibility, lalu tutup Overlay Column Visibility
47. Tekan Enter pada kotak Search berisi `Finance`
48. Verifikasi baris Division `Finance` (baris `Jane S`) kembali ditemukan

### Pemulihan state

49. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search (langkah 25, 28, 35, 38), penutupan Overlay Column Visibility (langkah 42 dan 46), pemulihan visibilitas kolom (langkah 46), dan penutupan Search di langkah 49 (hook `after` sebagai cadangan). "Ketik Search" membuka kotak Search bila tertutup (bagian 8b butir 9); kotak tetap terbuka setelah `✕`. Langkah 1 adalah pembanding generik sebelum asersi tersaring dan langkah 43 adalah anchor positif (baris pembanding pada tabel yang sama) sebelum asersi absence di langkah 45.
- Langkah 22 sampai 25 berulang untuk setiap baris tabel Data uji TC-AC-ACAL-50 (tujuh iterasi, bagian 8b butir 7). Baris amatan diidentifikasi lewat User, Note, dan IP Address karena tabel audit trail memuat entri dari run dan spec lain.
- Spec memiliki 49 langkah nominal dan 73 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Search Tab Session pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan per kolom data tanpa langkah bersyarat.
- Asersi tambahan (S-03): "baris tidak tampil" pada kolom ketiga Data uji TC-AC-ACAL-50 membuktikan kecocokan terbatas pada kolom yang dicari; TC hanya menulis "saja" pada kolom Note. Langkah 8, 14, dan 18 memakai baris `Jane S` sebagai pembanding hasil tersaring.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri Session (stempel `18 Jun 2026`, IP Address, Device / Browser) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-53 mensyaratkan entri bertanggal `18 Jun 2026`, tanggal yang sama dengan data Filter Date TC-AC-ACAL-59/99 (spec 034); entri seed spec ini dapat muncul pada hasil Filter Date `18 Jun 2026` spec lain dan tidak dapat dihapus. Asersi "hanya" di spec Filter Date sebaiknya dibatasi User atau Name.
  - TC-AC-ACAL-54 Expected b memuat syarat bersyarat ("`No results found` bila tidak ada kolom lain cocok"); spec hanya mengasersi baris yang hanya cocok di Division tidak tampil, tanpa asersi `No results found`.
  - TC-AC-ACAL-49 Expected g ("keyword kosong") tidak punya observasi terpisah; spec menyimpulkannya dari tabel yang kembali ke semua data (langkah 21).
  - TC-AC-ACAL-50 Expected a menyebut baris `EMP001`, `EMP002` tanpa menyebut User; spec memakai `John Doe` dan `Jane Smith` dari Data Uji Pre-setup No 12.
