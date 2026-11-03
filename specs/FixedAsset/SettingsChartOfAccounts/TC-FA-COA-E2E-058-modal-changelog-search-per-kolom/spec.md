---
id: TC-FA-COA-E2E-058-modal-changelog-search-per-kolom
title: "Modal Changelog: Search per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-200
  - TC-FA-COA-201
  - TC-FA-COA-230
  - TC-FA-COA-321
coverage:
  web: automated
---

# Modal Changelog: Search per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat Changelog P41 (asumsi pre-setup, bukan data PRD): empat baris Example Data Modal Changelog (PRD §4.1.1; tanggal contoh 20 sampai 23 Oct 2026; kode 5-6001, 6-2001, 1-1002, 5-6000; Modified By Rina P) ditambah satu baris Create, satu baris Delete, satu baris Activate (Status Inactive menjadi Active), dan satu entri oleh user B; baris tambahan memakai kode akun selain 1-1002 dan tidak memuat teks `Depr Expense`, `Aug 2026`, atau `Rina` di kolom selain Modified By. Changelog adalah audit trail permanen yang tumbuh; asersi memakai baris seed P41 yang dikenali lewat tanggal contoh dan Modified By pada ukuran halaman 100 (langkah 2).
- Parameter langkah berulang 3 sampai 6 (kolom yang dicari tercantum pada kolom "Kolom"):

  | Query | Kolom | Baris tampil | Baris tidak tampil |
  |---|---|---|---|
  | `Delete` | Action | baris Action Delete | baris Edit kode 5-6001 |
  | `1-1002` | Account Code | baris Status kode 1-1002 | baris kode 6-2001 |
  | `Last Used` | Field | baris Field Last Used in Journal | baris Field Status |
  | `Depr Expense` | Old Value | baris Account Name kode 5-6000 | baris Field Status |
  | `Aug 2026` | New Value | baris Last Used in Journal kode 6-2001 | baris Field Account Code |
  | `Rina` | Modified By | baris dengan Modified By Rina P | baris user B |

- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-200: Search per kolom

1. Klik ikon Changelog di toolbar
2. Pilih ukuran halaman 100
3. Ketik Search `Delete`, tekan Enter
4. Verifikasi baris yang tercantum pada kolom "Baris tampil" tabel Prerequisites tampil (baris Action Delete)
5. Verifikasi baris yang tercantum pada kolom "Baris tidak tampil" tabel Prerequisites tidak tampil (baris Edit kode 5-6001)
6. Klik `(←)` pada kotak Search
7. Ulangi langkah 3 sampai 6 untuk setiap baris lain pada tabel Prerequisites (`1-1002`, `Last Used`, `Depr Expense`, `Aug 2026`, `Rina`)

### TC-FA-COA-201: Kolom Date tidak ikut dicari

8. Catat teks sel Date baris kode 5-6001 (disalin dari layar)
9. Ketik Search teks sel Date yang dicatat, tekan Enter
10. Verifikasi empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
11. Klik `(←)` pada kotak Search

### TC-FA-COA-230: Spasi awal dan akhir dibuang

12. Ketik Search ` Rina ` (dengan spasi di awal dan akhir), tekan Enter
13. Verifikasi hasil sama dengan query `Rina` (baris Rina P tampil dan baris user B tidak tampil)
14. Verifikasi isi kotak Search tidak berubah (tetap ` Rina `)
15. Verifikasi tidak ada pesan atau indikator
16. Klik `(←)` pada kotak Search

### TC-FA-COA-321: Siklus reveal, hapus teks, Enter pada input kosong, dan collapse

17. Klik ikon Search di modal
18. Verifikasi kotak Search terbuka dengan fokus pada input
19. Ketik `Aug 2026`, tekan Enter
20. Verifikasi hanya baris yang cocok tampil (baris Last Used in Journal kode 6-2001 tampil dan baris user B tidak tampil)
21. Klik `(✕)`
22. Verifikasi teks terhapus tanpa mereset tabel (hasil `Aug 2026` masih tampil)
23. Tekan Enter pada input kosong
24. Verifikasi tabel direset (baris user B tampil kembali)
25. Ketik `Aug 2026`, tekan Enter
26. Klik `(←)`
27. Verifikasi kotak Search menutup
28. Verifikasi tabel langsung mereset (baris user B tampil kembali)
29. Pilih ukuran halaman 10
30. Tutup modal dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (30 langkah nominal, sekitar 54 dengan ekspansi langkah 7): langkah 3 sampai 6 diulang untuk enam query kolom (idiom 8b.7, parameter pada tabel Prerequisites, `Verifikasi` tetap satu per klausa); seluruh blok memakai satu modal Changelog dan satu kelas harness (fungsional) dan tiap query berdiri sendiri.
- Langkah 7 mengulang langkah 3 sampai 6 untuk lima query lain.
- Langkah penghubung (S-03): langkah 2 dan 29 (ukuran halaman 100 sementara agar baris seed teramati dalam satu halaman, S-14, dan pemulihannya), langkah 6, 11, 16 (menutup kotak Search dan mereset tabel, S-09), langkah 8 (mencatat teks sel Date), langkah 30 (menutup modal).
- Langkah 17 membuka kotak Search dengan klik ikon karena TC-321 menguji siklus input (8b.9).
- Temuan untuk QA:
  - TC-200 butir d memakai query `Depr Expense` pada kolom Old Value, tetapi baris sasaran (Account Name kode 5-6000) hanya dijamin ada pada riwayat seed P41 yang merupakan asumsi pre-setup.
  - TC-201 meminta teks sel Date "disalin dari layar"; spec mencatat teks itu sebagai langkah penghubung sebelum Search.
  - TC-230 butir a ("isi kotak Search tidak berubah") tidak menyebut apakah spasi dipertahankan dalam kotak; spec mengasersi isi tetap ` Rina `.
  - Audit trail tumbuh oleh spec lain; baris pembanding "tidak tampil" hanya memakai baris seed P41.
