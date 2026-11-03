---
id: TC-FA-COA-E2E-057-modal-changelog-screening-loading-kosong-dan-sort
title: "Modal Changelog: Screening, Loading, Kosong, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-88
  - TC-FA-COA-89
  - TC-FA-COA-91
  - TC-FA-COA-197
  - TC-FA-COA-198
  - TC-FA-COA-199
  - TC-FA-COA-288
coverage:
  web: automated
---

# Modal Changelog: Screening, Loading, Kosong, dan Sort

## Prerequisites

- Mode: FE+BE (TC-288 memakai `Spectra.intercept()` untuk menahan respons riwayat Changelog di atas backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Satu ganti akun eksplisit di langkah 29 dan 30 (TC-89); hook `after` mengembalikan sesi ke akun default suite.
- Riwayat Changelog P41 (asumsi pre-setup, bukan data PRD): empat baris Example Data Modal Changelog (PRD §4.1.1; tanggal contoh 20 sampai 23 Oct 2026; kode 5-6001, 6-2001, 1-1002, 5-6000; Modified By Rina P) ditambah satu baris Create, satu baris Delete, satu baris Activate (Status Inactive menjadi Active), dan satu entri oleh user B yang nama lengkapnya berurutan setelah nama lengkap Rina P; baris tambahan memakai kode akun selain 1-1002 dan tidak memuat teks `Depr Expense`, `Aug 2026`, atau `Rina` di kolom selain Modified By. Riwayat ini berisi lebih dari satu halaman. Changelog adalah audit trail permanen yang tumbuh; asersi urutan memakai urutan relatif baris seed P41 (dikenali lewat tanggal contoh dan Modified By) pada ukuran halaman 100 (langkah 19).
- Parameter langkah berulang 20 sampai 25 (urutan relatif baris seed P41):

  | Kolom | Klik 1 (indikator ↑) | Klik 2 (indikator ↓) |
  |---|---|---|
  | `Action` | urutan A-Z: Create, Delete, Edit | urutan Z-A: Edit, Delete, Create |
  | `Account Code` | urutan relatif 1-1002, 5-6000, 5-6001, 6-2001 | urutan kebalikannya |
  | `Field` | urutan relatif Account Code, Account Name, Last Used in Journal, Status | urutan kebalikannya |
  | `Modified By` | A-Z menurut nama lengkap user (bukan format tampilan `[First Name] [Last Initial]`); baris Rina P mendahului baris user B | Z-A menurut nama lengkap; baris user B mendahului baris Rina P |
  | `Old Value` | nilai terisi urut A-Z (`Active` mendahului `Inactive`) dan baris `—` di akhir | baris `—` di awal dan nilai terisi urut Z-A |
  | `New Value` | nilai terisi urut A-Z (`Active` mendahului `Inactive`) dan baris `—` (baris Delete) di akhir | baris `—` di awal dan nilai terisi urut Z-A |

- Akun TC-89 (client atau akun tanpa riwayat perubahan; tanpa ID Pre-setup di TC): disediakan tim FE/BE (lihat Seed dan pemulihan di `suite.md`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor dan akun TC-89 (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-88: Screening modal Changelog

1. Klik ikon Changelog di toolbar
2. Verifikasi judul modal "Changelog: Chart of Accounts"
3. Verifikasi kolom Date, Action, Account Code, Field, Old Value, New Value, dan Modified By tampil
4. Verifikasi urutan default Date Newest First
5. Verifikasi Old Value pada baris Action Create ditulis `—`
6. Tutup modal dengan ikon ✕

### TC-FA-COA-288: Loading Shimmer

7. Aktifkan intercept yang menahan respons riwayat Changelog
8. Klik ikon Changelog di toolbar
9. Verifikasi modal Changelog menampilkan Loading (Shimmer) selama data belum diterima
10. Lepas tahanan respons
11. Verifikasi baris riwayat tampil
12. Verifikasi Loading (Shimmer) hilang
13. Tutup modal dengan ikon ✕

### TC-FA-COA-91: Sort Date Oldest First

14. Klik ikon Changelog di toolbar
15. Klik header Date untuk sort Oldest First
16. Verifikasi urutan baris berubah menjadi Oldest First
17. Tutup modal dengan ikon ✕

### TC-FA-COA-197, TC-FA-COA-198, dan TC-FA-COA-199: Sort siklus tiga tahap

18. Klik ikon Changelog di toolbar
19. Pilih ukuran halaman 100
20. Klik header `Action` satu kali
21. Verifikasi kolom `Action` berindikator ↑ dengan urutan pada kolom "Klik 1" tabel Prerequisites
22. Klik header `Action` sekali lagi
23. Verifikasi kolom `Action` berindikator ↓ dengan urutan pada kolom "Klik 2" tabel Prerequisites
24. Klik header `Action` sekali lagi
25. Verifikasi urutan kembali ke default Date Newest First
26. Ulangi langkah 20 sampai 25 untuk setiap baris lain pada tabel Prerequisites (`Account Code`, `Field`, `Modified By`, `Old Value`, `New Value`)
27. Pilih ukuran halaman 10
28. Tutup modal dengan ikon ✕

### TC-FA-COA-89: Modal Changelog kosong

29. Klik Logout dari akun aktor default
30. Login sebagai akun tanpa riwayat perubahan, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
31. Klik ikon Changelog di toolbar
32. Verifikasi ilustrasi dengan judul "No changelog yet"
33. Verifikasi deskripsi "Activities and changes will appear here."
34. Tutup modal dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (34 langkah nominal, sekitar 64 dengan ekspansi langkah 26): langkah 20 sampai 25 diulang untuk enam kolom (idiom 8b.7, parameter pada tabel Prerequisites, tanpa langkah bersyarat, `Verifikasi` tetap satu per klausa); seluruh blok memakai satu modal Changelog dan satu kelas harness (fungsional), dan tiap kolom berdiri sendiri sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah 26 mengulang langkah 20 sampai 25 untuk lima kolom lain; TC-197 mencakup kolom Action, Account Code, dan Field, TC-198 kolom Modified By, TC-199 kolom Old Value dan New Value.
- Langkah penghubung (S-03): langkah 6, 13, 17, 28, dan 34 (menutup modal, sort kembali ke default sesudah modal dibuka ulang), langkah 19 dan 27 (ukuran halaman 100 sementara agar baris seed teramati dalam satu halaman, S-14, dan pemulihannya), langkah 29 dan 30 (ganti akun untuk TC-89).
- Pemicu TC-288 (menahan respons) adalah state sementara yang diamati, bukan kegagalan yang dipaksa (kelas b); intercept dilepas pada langkah 10 dan `Verifikasi` shimmer hilang ditulis sesudah baris riwayat tampil (8b.11).
- Temuan untuk QA:
  - TC-89 ("Belum ada riwayat perubahan") tidak menyebut akun atau client yang dipakai dan tidak punya ID Pre-setup; spec menulis kebutuhan akun tanpa riwayat sebagai "disediakan tim FE/BE". Changelog adalah audit trail permanen sehingga akun dengan riwayat nol harus client terpisah.
  - TC-197 sampai TC-199 mengasumsikan riwayat hanya berisi baris seed P41; audit trail tumbuh oleh spec lain, sehingga spec mengasersi urutan relatif baris seed dan bukan urutan seluruh halaman.
  - TC-91 tidak menyebut data yang diamati selain "urutan berubah"; spec mengasersi hanya urutan Oldest First.
  - P41 adalah asumsi pre-setup, bukan data PRD.
