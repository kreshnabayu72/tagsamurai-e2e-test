---
id: TC-GS-BRAND-E2E-065-sync-all-tags-pemilih-dan-snapshot
title: "Sinkronisasi Brand ke All Tags: Pemilih Brand Activate TAG BYO dan Snapshot Nama Brand pada TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-221
  - TC-GS-BRAND-247
  - TC-GS-BRAND-277
  - TC-GS-BRAND-275
  - TC-GS-BRAND-276
coverage:
  web: automated
---

# Sinkronisasi Brand ke All Tags: Pemilih Brand Activate TAG BYO dan Snapshot Nama Brand pada TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak ada. Spec tidak memakai atau mengubah brand Pre-setup Client A.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before` oleh akun Total Control:
  - `Tidal Co {runId}-065` (D-11): brand yang harus tersedia di pemilih Brand all-tags (setara dependensi TC-GS-BRAND-56).
  - `Pine Co {runId}-065` dan `Quartz Co {runId}-065` (D-05): dibuat lalu dihapus lewat API di hook `before` (setara dependensi TC-GS-BRAND-39), sehingga pada TC-GS-BRAND-247 keduanya sudah terhapus.
  - `Rename Tag Co {runId}-065` (D-48): brand yang dipakai 2 TAG BYO di all-tags (snapshot nama; kolom Brand kedua TAG `Rename Tag Co {runId}-065`). Pada TC-GS-BRAND-277 dan TC-GS-BRAND-221 di-rename menjadi `Rename Tag Group {runId}-065`, lalu dikembalikan ke `Rename Tag Co {runId}-065`.
  - `Snap Tag Co {runId}-065` (D-38): brand yang hanya dipakai 1 TAG BYO di all-tags (snapshot nama), tidak dipakai FAMS, Supply, maupun Device SKU. Dihapus lewat UI pada TC-GS-BRAND-275.
  - Tiga TAG BYO hasil Activate lewat API di hook `before` (dua dengan Brand `Rename Tag Co {runId}-065`, satu dengan Brand `Snap Tag Co {runId}-065`). Identitas (kode) ketiga TAG dicatat hook `before` dan dipakai untuk Search di All Tags.
- Kebutuhan fixture/FE untuk TAG BYO (tim FE menyediakan; fixture `fixtures/brand.json` belum ada). Nilai field Activate TAG BYO yang lain (`global-settings/all-tags` §6.2: Device Name wajib dari katalog perangkat aktif, SKU dikosongkan sehingga Brand wajib diisi, Model/Type opsional):

  | Kunci fixture | Isi | Nilai |
  |---|---|---|
  | `tagByo.pool` | Minimal 3 identitas TAG BYO yang belum pernah di-activate untuk setiap run (pool diganti per run, atau TAG hasil seeding dihapus sehingga identitasnya bisa dipakai ulang) | disediakan tim FE |
  | `tagByo.deviceName` | Device Name dari katalog perangkat aktif | disediakan tim FE |

- Kemampuan teknis: Activate TAG BYO lewat API dengan opsi BYO aktif untuk Client A; Delete TAG (hanya TAG unpaired, `global-settings/all-tags` §4.1) lewat API untuk cleanup TAG hasil seeding, wajib tersedia agar run berikutnya bisa memakai ulang identitas TAG.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga TAG BYO hasil seeding, lalu hapus brand `Tidal Co`, `Rename Tag Co` atau `Rename Tag Group` (nama yang masih ada), dan `Snap Tag Co` bersuffix `{runId}-065` bila masih ada.
- Tidak ada state global lain yang diubah.
- TC-GS-BRAND-221, 247, 277, 275, 276: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-277: Rename Brand tidak mengubah Brand pada TAG all-tags yang sudah tersimpan

1. Search `Rename Tag Co {runId}-065` pada tabel Brand, klik `⋯` pada baris tersebut > Edit, ubah Brand Name menjadi `Rename Tag Group {runId}-065`, klik [Save]
2. Buka Global Settings > All Tags, Search kode kedua TAG pemakai `Rename Tag Co {runId}-065`, lihat kolom Brand keduanya
3. Verifikasi kolom Brand kedua TAG tetap `Rename Tag Co {runId}-065` (tidak berubah menjadi `Rename Tag Group {runId}-065`)

### TC-GS-BRAND-221: Brand baru dan rename tercermin di pemilih Brand all-tags (sekaligus Expected Result b TC-GS-BRAND-277)

4. Buka Global Settings > All Tags > Activate TAG BYO, buka pemilih Brand
5. Verifikasi `Tidal Co {runId}-065` tersedia di pemilih Brand (TC-GS-BRAND-221 Expected Result a)
6. Verifikasi pemilih Brand menampilkan `Rename Tag Group {runId}-065` sebagai opsi selama rename berlaku (TC-GS-BRAND-221 Expected Result b dan TC-GS-BRAND-277 Expected Result b)

### TC-GS-BRAND-247: Brand terhapus hilang dari pemilih Brand all-tags

7. Verifikasi `Pine Co {runId}-065` tidak ada di opsi pemilih Brand (TC-GS-BRAND-247)
8. Verifikasi `Quartz Co {runId}-065` tidak ada di opsi pemilih Brand (TC-GS-BRAND-247)
9. Tutup pemilih Brand dan form Activate TAG BYO (form tidak berisi perubahan)
10. Buka Global Settings > Master Reference > Brand, Search `Rename Tag Group {runId}-065`, rename kembali menjadi `Rename Tag Co {runId}-065`, klik [Save]
11. Search `Rename Tag Co {runId}-065` pada tabel Brand
12. Verifikasi `Rename Tag Co {runId}-065` kembali pada tabel Brand (Post Condition TC-GS-BRAND-277)

### TC-GS-BRAND-275: Brand yang hanya dipakai data tag all-tags berhasil dihapus

13. Search `Snap Tag Co {runId}-065` pada tabel Brand, klik `⋯` pada baris tersebut > Delete
14. Verifikasi dialog `Delete Brand` tampil (bukan `Cannot Delete Brand`)
15. Klik [Delete] pada dialog
16. Verifikasi toast sukses: "Success, brand has been deleted."
17. Verifikasi `Snap Tag Co {runId}-065` hilang dari tabel Brand

### TC-GS-BRAND-276: Data tag all-tags tetap menampilkan nama Brand snapshot setelah Brand dihapus

18. Buka Global Settings > All Tags
19. Cari TAG yang tersimpan dengan Brand `Snap Tag Co {runId}-065` (Search kode TAG hasil seeding)
20. Verifikasi kolom Brand TAG tersebut tetap menampilkan `Snap Tag Co {runId}-065`
21. Buka Activate TAG BYO, buka pemilih Brand
22. Verifikasi `Snap Tag Co {runId}-065` tidak ada di opsi pemilih Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: rename 277 dan 221 dijalankan sekali (langkah 1 dan 10) untuk kedua TC; pemilih Brand dibuka satu kali sesudah rename untuk Expected Result 221 a dan b, 247, dan 277 b (langkah 4 sampai 8), lalu 275 (Delete), dan 276 (membutuhkan 275) paling akhir; aksi menghapus data (275) ditaruh di akhir (prinsip 5). Pemilih dibuka dua kali (langkah 4 dan 21), masing-masing ditutup atau berakhir tanpa Submit.
- TC-GS-BRAND-221 dipecah dua: Expected Result a (Tidal Co tersedia) di langkah 5, Expected Result b (opsi `Rename Tag Group`; TAG tetap `Rename Tag Co`) di langkah 6 dan 3 bersama TC-GS-BRAND-277.
- Pine Co dan Quartz Co dihapus lewat API di hook `before` (dependensi TC-GS-BRAND-39), bukan lewat UI di spec ini, karena penghapusan itu bukan objek uji TC-GS-BRAND-247.
- Langkah penghubung: langkah 1, 10, 11, 13 (Search baris Brand target), langkah 2, 18, 19 (membuka All Tags dan mencari TAG hasil seeding), dan langkah 9 (menutup form bersih).
- Kebutuhan pool TAG BYO, Delete TAG untuk cleanup, dan fixture `fixtures/brand.json` sudah dicatat sebagai kebutuhan di Prerequisites; fixture belum ada.
