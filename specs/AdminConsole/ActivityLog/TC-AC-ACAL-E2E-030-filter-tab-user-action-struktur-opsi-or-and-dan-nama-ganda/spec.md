---
id: TC-AC-ACAL-E2E-030-filter-tab-user-action-struktur-opsi-or-and-dan-nama-ganda
title: "Filter Tab User Action: Struktur, Opsi Dinamis, OR/AND, dan Nama Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-95
  - TC-AC-ACAL-96
  - TC-AC-ACAL-97
  - TC-AC-ACAL-98
  - TC-AC-ACAL-176
coverage:
  web: automated
---

# Filter Tab User Action: Struktur, Opsi Dinamis, OR/AND, dan Nama Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): dua akun admin berbeda bernama `Hendra Pratama` (tampil `Hendra P`) yang masing-masing pernah mengedit Client; pelaku entri r1 dan r2.
- Data Dinamis (sufiks `{runId}-030`, `{runId}` hanya digit; dibuat lewat API di hook `before`; password subjek dinamis `Spectra.env.AC_DYN_PASSWORD`, password uji ditetapkan tim FE, nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`):

  | Subjek | Keadaan | Peran di spec |
  |---|---|---|
  | `Rina {runId}-030` | Admin yang membuat entri log r11 lalu dihapus dari Global Settings > User | Tetap muncul di opsi Modified By (TC-AC-ACAL-96) |
  | `Pasif Uji {runId}-030` | Terdaftar di Global Settings > User, tidak pernah mengubah data | Tidak muncul di opsi Modified By (TC-AC-ACAL-96) |

- Data log Tab User Action (seed BE; Name bersuffix `{runId}-030`):

  | Kode | Action | Object | Name | Field | Modified By | Date |
  |---|---|---|---|---|---|---|
  | r1 | `Create` | `Distributor` | `PT Maju Bersama {runId}-030` | `Company Name` | `Hendra Pratama` (akun pertama) | terbaru |
  | r2 | `Edit` | `Client` | `PT Sejahtera {runId}-030` | `PIC Name` | `Hendra Pratama` (akun kedua) | terbaru |
  | r3 | `Delete` | `Brand` | `Acme {runId}-030` | `Brand Name` | ditetapkan tim FE | terbaru |
  | r4 | `Suspend` | `Partner` | `Partner Suspend {runId}-030` | `Status` | ditetapkan tim FE | `18 Jun 2026` |
  | r5 | `Reassign` | `Partner` | `Partner Reassign {runId}-030` | `Distributor` | ditetapkan tim FE | `18 Jun 2026` |
  | r6 | `Suspend` | `Client` | `Klien Suspend {runId}-030` | `Status` | ditetapkan tim FE | `18 Jun 2026` |
  | r7 | `Suspend` | `Partner` | `Partner Suspend Lain {runId}-030` | `Status` | ditetapkan tim FE | tanggal lain (bukan 17 sampai 20 Jun 2026) |
  | r8 | `Resend Activation Email` | `Distributor` | `Distributor Kirim Ulang {runId}-030` | `Email` | ditetapkan tim FE | terbaru |
  | r9 | `Cancel` | `Subscription` | `Langganan Batal {runId}-030` | `Status` | ditetapkan tim FE | terbaru |
  | r10 | `Create` | `Wallet` | `Dompet Baru {runId}-030` | `Status` | ditetapkan tim FE | terbaru (Object `Wallet` baru tanpa perubahan konfigurasi) |
  | r11 | `Create` | `Distributor` | `PT Rina {runId}-030` | `Company Name` | `Rina {runId}-030` | terbaru |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Date, Modified By, dan nilai kolom pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); pembuatan dan penghapusan akun admin lewat API; membaca seluruh daftar opsi dropdown (menggulir) untuk asersi absence; memilih rentang tanggal pada date range picker.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Pasif Uji {runId}-030` lewat API. Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-95: Screening Filter Panel

2. Klik icon Filter
3. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
4. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
5. Verifikasi field `Object` berupa multi-select searchable dengan placeholder `All objects`
6. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
7. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
8. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
9. Verifikasi icon Filter berubah gelap
10. Verifikasi tidak ada field filter Name, Old Value, maupun New Value di panel

### TC-AC-ACAL-96: Isi opsi dinamis dari data log

11. Buka dropdown Action
12. Verifikasi opsi memuat aksi tercatat `Create`, `Edit`, `Delete`, `Suspend`, `Reassign`, `Resend Activation Email`, dan `Cancel`
13. Verifikasi tidak ada opsi kosong di dropdown Action
14. Tutup dropdown Action
15. Buka dropdown Object
16. Verifikasi opsi memuat `Wallet` tanpa perubahan konfigurasi
17. Verifikasi tidak ada opsi kosong di dropdown Object
18. Tutup dropdown Object
19. Buka dropdown Field
20. Verifikasi opsi memuat nama atribut tercatat `Company Name`, `PIC Name`, dan `Status`
21. Verifikasi tidak ada opsi `None` atau kosong di dropdown Field
22. Tutup dropdown Field
23. Buka dropdown Modified By
24. Verifikasi opsi `Rina {runId}-030` tetap muncul
25. Verifikasi opsi `Pasif Uji {runId}-030` tidak muncul
26. Verifikasi tidak ada opsi `None` atau kosong di dropdown Modified By
27. Tutup dropdown Modified By

### TC-AC-ACAL-97: Filter per field dropdown

28. Buka dropdown Action, centang `Delete`, klik `[Apply]`
29. Verifikasi hanya baris Action `Delete` yang tampil (baris r3 tampil dan baris r1 tidak tampil)
30. Ketik Search `{runId}-030`, tekan Enter
31. Klik `[Clear Field]`, pilih Object `Partner`, klik `[Apply]`
32. Verifikasi hanya baris Object `Partner` yang tampil (baris r4 tampil dan baris r1 tidak tampil)
33. Klik `[Clear Field]`, pilih Field `PIC Name`, klik `[Apply]`
34. Verifikasi hanya baris Field `PIC Name` yang tampil (baris r2 tampil dan baris r1 tidak tampil)
35. Klik `[Clear Field]`, pilih Modified By `Hendra Pratama`, klik `[Apply]`
36. Verifikasi hanya baris `Hendra P` yang tampil (baris r1 dan r2 tampil, baris r3 tidak tampil)

### TC-AC-ACAL-98: OR di dalam satu field, AND antar field

37. Klik `[Clear Field]`, pilih Action `Suspend` dan `Reassign`, klik `[Apply]`
38. Verifikasi baris Suspend atau Reassign tampil (baris r4, r5, r6, dan r7 tampil, baris r1 tidak tampil)
39. Tambah Object `Partner` dan Date `18 Jun 2026` sampai `18 Jun 2026`, klik `[Apply]`
40. Verifikasi hanya baris Suspend atau Reassign dengan Object `Partner` pada `18 Jun 2026` yang tampil (baris r4 dan r5 tampil, baris r6 dan r7 tidak tampil)

### TC-AC-ACAL-176: Dua pengguna bernama sama tampil sebagai satu opsi Modified By

41. Klik `[Clear Field]`, buka dropdown Modified By
42. Verifikasi hanya ada satu opsi berlabel `Hendra Pratama` (nama lengkap)
43. Centang opsi `Hendra Pratama`, klik `[Apply]`
44. Verifikasi tabel memuat entri kedua akun `Hendra Pratama` (baris r1 dan baris r2 tampil)
45. Klik `[Clear Field]`, klik `[Apply]` untuk mengosongkan saringan Modified By
46. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan dropdown (langkah 14, 18, 22, 27), pengisian Search pembatas (langkah 30), pengosongan saringan (langkah 31, 33, 35, 37, 41, 45), penutupan Search (langkah 46). State Filter direset oleh hook `beforeEach` suite pada spec berikutnya (klik sidebar mereset Search, Sort, dan Filter).
- Langkah 45 (pemulihan, tanpa `Verifikasi`, S-03 dan S-09): mengosongkan saringan Modified By yang tersisa dari langkah 43 agar state akhir tidak terbawa; hasil tabel tidak diasersi karena tidak ada Expected TC.
- Spec memiliki 46 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Tab User Action pada akun dan dataset yang sama) dan tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; seluruh blok hanya membuka dropdown dan menerapkan saringan tanpa langkah bersyarat.
- Langkah penghubung pembatas (S-03, R-16): langkah 30 (Search `{runId}-030`, Enter) dan langkah 46 (tutup Search, S-09). Alasan: audit trail append-only, urut Date terbaru, page size default 10; baris r4 sampai r7 ber-Date lama, sehingga pada run berikutnya turun ke halaman 2 oleh baris Partner/Suspend/Reassign baru dari run dan spec lain, dan asersi "tampil" langkah 32, 38, dan 40 gagal bukan karena perilaku Filter. Name r4 sampai r7 bersuffix `{runId}-030`; Search dan Filter digabung AND dan tiap tab menyimpan keduanya (PRD FI-06), sehingga langkah 32 sampai 45 tetap dibatasi ke baris run ini. Langkah 29 (Action `Delete`, r3 terbaru) tidak memerlukan pembatas.
- Asersi tambahan (S-03): "baris tidak tampil" pada langkah 29, 32, 34, 36, 38, dan 40 membuktikan kata "hanya" pada Expected TC; baris r1, r3, r6, dan r7 dipakai sebagai pembanding.
- Baris r10 (Object `Wallet`, Name `Dompet Baru {runId}-030`) berada pada entitas Principal default akun aktor, terpisah dari Principal segar spec 043 (TC-AC-ACAL-166, dan prekondisi c TC-AC-ACAL-96); kedua data tidak saling memengaruhi.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-98 menyaring Date `18 Jun 2026`, tanggal yang sama dengan data Filter Date TC-AC-ACAL-99 (spec 034); entri r4 sampai r6 spec ini dapat muncul pada hasil Filter Date `18 Jun 2026` spec lain dan tidak dapat dihapus. Asersi "hanya" di spec Filter Date sebaiknya dibatasi User atau Name.
  - TC-AC-ACAL-96 tidak menyebut "user yang tidak pernah mengubah data" dan akun `Rina`; spec memakai `Pasif Uji {runId}-030` dan `Rina {runId}-030` bersuffix (pilihan spec).
  - TC-AC-ACAL-97 dan 176 memakai `Hendra Pratama` tanpa menyebut entri yang dikerjakannya; spec memakai entri r1 dan r2 milik spec.
  - TC tidak menyatakan apakah Filter Panel menutup sesudah `[Apply]`; TC-AC-ACAL-97, 98, dan 176 menekan `[Clear Field]` atau membuka dropdown tanpa membuka ulang panel. Spec mengikuti urutan langkah TC apa adanya.
  - TC-AC-ACAL-98 langkah 2 menambah Object `Partner` dan Date `18 Jun 2026` pada filter Action yang aktif; TC tidak menyebut apakah Date dipilih sebagai rentang satu hari, spec memilih `18 Jun 2026` sampai `18 Jun 2026`.
