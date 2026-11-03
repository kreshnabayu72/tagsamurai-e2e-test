---
id: TC-AC-SG-E2E-050-search-tabel-utama-kolom-di-hide-trim-dan-lokal-terhadap-node-terpilih
title: "Search Tabel Utama: Kolom Di-hide, Trim Query, dan Lokal terhadap Node Terpilih"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-180
  - TC-AC-SG-181
  - TC-AC-SG-182
coverage:
  web: automated
---

# Search Tabel Utama: Kolom Di-hide, Trim Query, dan Lokal terhadap Node Terpilih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #19, #20), node `All Groups` terpilih, 14 group, page size bawaan 10 baris. Nilai yang dipakai: `Branch 1` dan `Branch 2` Modified By `Admin B`; `Region A` memiliki descendant `Branch 1`, `Branch 2`, `Floor 1`, dan `Room 301`; `Branch 3` dan `Branch 4` berada di bawah `Region B`.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih. Spec ini menyembunyikan kolom Modified By lewat Overlay Column Visibility lalu menampilkannya kembali di dalam spec; hook `after` (dan `before`) spec ini menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-180: Search tidak mencari kolom yang sedang di-hide

1. Klik header kolom Actions `⋯` untuk membuka Overlay Column Visibility
2. Hapus centang kolom Modified By
3. Tutup Overlay Column Visibility
4. Ketik Search `Admin B`, tekan Enter
5. Verifikasi empty state `No results found` (pencarian tidak menemukan baris selama kolom Modified By di-hide)
6. Klik header kolom Actions `⋯` untuk membuka Overlay Column Visibility
7. Centang kembali kolom Modified By
8. Tutup Overlay Column Visibility
9. Ganti isi kotak search dengan `Admin B`, tekan Enter
10. Verifikasi tabel menampilkan `Branch 1` dan `Branch 2`

### TC-AC-SG-181: Query Search di-trim, query spasi saja diperlakukan kosong

11. Ganti isi kotak search dengan `  Region A  ` (dua spasi di awal dan di akhir), tekan Enter
12. Verifikasi tabel menampilkan `Region A`
13. Verifikasi teks di input search tetap persis `  Region A  ` seperti diketik
14. Ganti isi kotak search dengan tiga spasi, tekan Enter
15. Verifikasi seluruh data tampil (info pagination menunjukkan total 14 baris)

### TC-AC-SG-182: Search lokal terhadap node yang dipilih di sidebar

16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
17. Klik node `Region A` di sidebar
18. Ketik Search `Branch`, tekan Enter
19. Verifikasi tabel menampilkan `Branch 1` dan `Branch 2` (descendant `Region A`)
20. Verifikasi `Branch 3` dan `Branch 4` tidak tampil di tabel
21. Ganti isi kotak search dengan `Region B`, tekan Enter
22. Verifikasi empty state `No results found` (`Region B` berada di luar node terpilih)
23. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
24. Klik node `All Groups` di sidebar

## Notes

- Langkah penghubung (S-03): langkah 6 sampai 8 membalik langkah 1 sampai 3 sebagai bagian dari "Unhide kolom Modified By" TC-180; langkah 16 (mereset tabel dari hasil kosong/spasi), langkah 23 dan 24 (menutup Search dan mengembalikan node `All Groups`, S-09).
- Langkah "Pastikan" TC-180 dan TC-181 dipenuhi Prerequisites; tidak ada langkah terpisah. Langkah 20 (absence) diawali Verifikasi langkah 19 yang membuktikan baris `Branch 1` dan `Branch 2` tampil pada surface yang sama (8b butir 2).
- Temuan untuk QA:
  - TC-AC-SG-180: Expected a memakai "(empty state)" tanpa Title; spec mengasersi `No results found` sesuai TC lain di kelompok Search.
  - TC-AC-SG-182: Expected b "tidak menemukan baris (empty state)" tidak menyebut teks empty state; spec memakai Title `No results found`.
