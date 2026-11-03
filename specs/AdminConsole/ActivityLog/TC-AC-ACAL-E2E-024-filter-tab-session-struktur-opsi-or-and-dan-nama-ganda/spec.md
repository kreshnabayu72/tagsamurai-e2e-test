---
id: TC-AC-ACAL-E2E-024-filter-tab-session-struktur-opsi-or-and-dan-nama-ganda
title: "Filter Tab Session: Struktur, Opsi, OR/AND, dan Nama Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-55
  - TC-AC-ACAL-56
  - TC-AC-ACAL-57
  - TC-AC-ACAL-58
  - TC-AC-ACAL-172
  - TC-AC-ACAL-173
coverage:
  web: automated
---

# Filter Tab Session: Struktur, Opsi, OR/AND, dan Nama Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 9 dan 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): `John Doe` (EMP001, Staff, Marketing) dan `Jane Smith` (EMP002, tanpa Position, Finance), masing-masing dengan entri Session; `John Doe` kedua (EMP010) dengan entri Session untuk TC-AC-ACAL-173.
- Data Dinamis (sufiks `{runId}-024`, `{runId}` hanya digit; dibuat lewat API di hook `before`; password subjek dinamis `Spectra.env.AC_DYN_PASSWORD`, password uji ditetapkan tim FE, nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`):

  | Subjek | Keadaan | Peran di spec |
  |---|---|---|
  | `Dewi Lestari {runId}-024` | Terdaftar di Global Settings > User, tidak pernah membuka Admin Console | Tidak boleh muncul di opsi User (TC-AC-ACAL-56) |
  | `Bayu {runId}-024` | Membuka Admin Console lalu dihapus dari Global Settings > User | Tetap muncul di opsi User (TC-AC-ACAL-56) |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session untuk `John Doe` (EMP001 dan EMP010) dan `Jane Smith`; sesi API subjek yang membuka Admin Console (untuk `Bayu {runId}-024`) sebelum subjek dihapus (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); membaca seluruh daftar opsi dropdown (menggulir) untuk asersi absence.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Dewi Lestari {runId}-024` lewat API. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACAL-55: Screening Filter Panel

1. Klik icon Filter
2. Verifikasi panel Filter tampil di bawah toolbar
3. Verifikasi icon Filter berubah gelap
4. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
5. Verifikasi field `User` berupa multi-select searchable dengan placeholder `All users`
6. Verifikasi field `Position` berupa multi-select searchable dengan placeholder `All positions`
7. Verifikasi field `Division` berupa multi-select searchable dengan placeholder `All divisions`
8. Verifikasi tidak ada nilai pre-selected pada keempat field
9. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) tampil
10. Verifikasi tidak ada field Activity, Status, Note, Employee ID, IP Address, maupun Device / Browser di panel

### TC-AC-ACAL-56: Isi opsi dropdown User, Position, Division dari data log

11. Buka dropdown User
12. Verifikasi opsi `John Doe` tampil (pembanding)
13. Verifikasi opsi `Bayu {runId}-024` tetap muncul
14. Verifikasi opsi `Dewi Lestari {runId}-024` tidak muncul
15. Verifikasi tidak ada opsi `None` atau kosong di dropdown User
16. Tutup dropdown User
17. Buka dropdown Position
18. Verifikasi opsi `Staff` (nilai yang tercatat) tampil
19. Verifikasi tidak ada opsi kosong di dropdown Position walau ada baris Position `—`
20. Tutup dropdown Position
21. Buka dropdown Division
22. Verifikasi opsi `Marketing` dan `Finance` (nilai yang tercatat) tampil
23. Tutup dropdown Division

### TC-AC-ACAL-57: Filter per field dropdown

24. Buka dropdown User, centang `John Doe`, klik `[Apply]`
25. Verifikasi hanya baris `John D` yang tampil (baris `John D` tampil dan baris `Jane S` tidak tampil)
26. Klik `[Clear Field]`, pilih Position `Staff`, klik `[Apply]`
27. Verifikasi hanya baris Position `Staff` yang tampil (baris `John D` tampil dan baris `Jane S` dengan Position `—` tidak tampil)
28. Klik `[Clear Field]`, pilih Division `Finance`, klik `[Apply]`
29. Verifikasi hanya baris Division `Finance` yang tampil (baris `Jane S` tampil dan baris `John D` dengan Division `Marketing` tidak tampil)

### TC-AC-ACAL-58: OR di dalam satu field, AND antar field

30. Klik `[Clear Field]`, pilih User `John Doe` dan `Jane Smith`, klik `[Apply]`
31. Verifikasi baris `John D` dan baris `Jane S` tampil
32. Tambah Division `Marketing`, klik `[Apply]`
33. Verifikasi hanya baris `John D` (Division `Marketing`) yang tampil dan baris `Jane S` tidak tampil

### TC-AC-ACAL-172: Opsi dropdown tidak menyempit mengikuti Search dan Filter lain

34. Klik `[Clear Field]`, pilih User `John Doe`, klik `[Apply]`
35. Verifikasi tabel hanya berisi baris `John D` (baris `Jane S` tidak tampil)
36. Buka dropdown Division
37. Verifikasi opsi Division tetap memuat `Finance` dan `Marketing`
38. Tutup dropdown Division
39. Ketik Search `Jane`, tekan Enter
40. Buka dropdown Division
41. Verifikasi opsi Division tetap memuat `Finance` dan `Marketing`
42. Tutup dropdown Division

### TC-AC-ACAL-173: Dua pengguna bernama sama tampil sebagai satu opsi User

43. Klik `←` pada kotak Search, lalu klik `[Clear Field]`
44. Buka dropdown User
45. Verifikasi hanya ada satu opsi berlabel `John Doe` (nama lengkap)
46. Centang opsi `John Doe`, klik `[Apply]`
47. Verifikasi tabel memuat baris `John Doe` dengan Employee ID `EMP001` dan baris `John Doe` dengan Employee ID `EMP010`
48. Klik `[Clear Field]`, klik `[Apply]` untuk mengosongkan saringan User

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan dropdown (langkah 16, 20, 23, 38, 42), pengosongan saringan (langkah 26, 28, 30, 34, 43, 48), dan penutupan Search (langkah 43). State Filter dan Search direset oleh hook `beforeEach` suite pada spec berikutnya (klik sidebar mereset Search, Sort, dan Filter).
- Langkah 48 (pemulihan, tanpa `Verifikasi`, S-03 dan S-09): mengosongkan saringan User yang tersisa dari langkah 46 agar state akhir tidak terbawa; hasil tabel tidak diasersi karena tidak ada Expected TC.
- Spec memiliki 48 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Tab Session pada akun dan dataset yang sama) dan tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; seluruh blok hanya membuka dropdown dan menerapkan saringan tanpa langkah bersyarat.
- Asersi tambahan (S-03): "baris tidak tampil" pada langkah 25, 27, 29, 33, dan 35 membuktikan kata "hanya" pada Expected TC; baris `Jane S` atau `John D` dipakai sebagai pembanding.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri Session tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC tidak menyatakan apakah Filter Panel menutup sesudah `[Apply]`; TC-AC-ACAL-57, 58, 172, dan 173 menekan `[Clear Field]` atau membuka dropdown tanpa membuka ulang panel. Spec mengikuti urutan langkah TC apa adanya.
  - TC-AC-ACAL-56 Expected b dan c ("hanya nilai yang tercatat") tidak menyebut nilai pembanding yang tidak tercatat; spec mengasersi nilai tercatat tampil dan opsi kosong tidak ada.
  - TC-AC-ACAL-56 menamai `Dewi Lestari` dan `Bayu` secara literal; spec memakai nama bersuffix milik spec karena asersi tidak bergantung pada singkatan nama (S-12), sehingga `Bayu` tidak bentrok dengan penghapusan `Bayu` di spec lain.
  - TC-AC-ACAL-173 tidak menyebut Position dan Division `John Doe` kedua (EMP010); nilai itu ditetapkan tim FE dan tidak diasersi.
  - TC-AC-ACAL-172 langkah 3 mengetik Search `Jane` saat filter User `John Doe` aktif; TC tidak memberi Expected tabel, sehingga hasil tabel tidak diasersi.
