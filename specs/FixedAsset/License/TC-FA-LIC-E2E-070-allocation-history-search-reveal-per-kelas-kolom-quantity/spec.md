---
id: TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity
title: "Allocation History: Search (Reveal, Per Kelas Kolom, Quantity Numerik, dan Format Angka)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-230
  - TC-FA-LIC-231
  - TC-FA-LIC-232
  - TC-FA-LIC-261
coverage:
  web: automated
---
# Allocation History: Search (Reveal, Per Kelas Kolom, Quantity Numerik, dan Format Angka)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Anggota pencarian per kelas kolom (parameter langkah 23 sampai 25):

  | TC | Kolom | Kata kunci | Hasil tabel |
  |---|---|---|---|
  | TC-FA-LIC-231 | Allocation ID | `20250210` | LALC-20250210-00001 |
  | TC-FA-LIC-231 | Subscription ID | `SUBS-20250101` | LALC-20250210-00001 |
  | TC-FA-LIC-231 | License Type | `Addon (IT` | LALC-20260801-00004 |
  | TC-FA-LIC-231 | Status | `Expired` | LALC-20250210-00001 |
  | TC-FA-LIC-231 | Plan Owner | `Maju` | LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 |
  | TC-FA-LIC-232 | Quantity | `3000` | LALC-20260101-00001 |
  | TC-FA-LIC-232 | Quantity (format dengan pemisah) | `3,000` | tidak ada baris (empty state `No results found`) |
  | TC-FA-LIC-261 | Quantity | `1500` | LALC-20260312-00002 (Quantity tampil `+1500`) |
  | TC-FA-LIC-261 | Quantity (dengan tanda +) | `+1500` | tidak ada baris (empty state `No results found`) |
  | TC-FA-LIC-261 | Quantity (format dengan pemisah) | `1,500` | tidak ada baris (empty state `No results found`) |

- Kemampuan teknis: hover ikon Search untuk mengamati tooltip dan pengamatan fokus kursor serta isi kotak Search (disediakan tim FE).
- State yang diubah dan dipulihkan: kotak Search tabel Allocation History (ditutup pada langkah 26).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-230: Siklus Search (reveal, auto-focus, placeholder, tooltip, Enter, clear, collapse)

2. Arahkan kursor ke ikon Search pada toolbar
3. Verifikasi tooltip `Search` tampil
4. Klik ikon Search
5. Verifikasi search bar melebar
6. Verifikasi kursor fokus di input
7. Verifikasi placeholder `Search allocation ID, license type...`
8. Ketik `2` (1 karakter) pada kotak Search tanpa menekan Enter
9. Verifikasi icon `(×)` muncul di dalam kotak
10. Verifikasi tabel belum tersaring (enam baris: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001)
11. Ganti isi kotak search dengan `20250210`, tekan Enter
12. Verifikasi tabel tersaring: LALC-20250210-00001
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak Search tetap terbuka dan fokus
16. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: LALC-20250210-00001
17. Tekan Enter pada kotak kosong
18. Verifikasi tabel menampilkan semua baris (enam baris)
19. Ketik `2025` pada kotak Search tanpa menekan Enter, lalu klik icon panah `(←)` di kiri toolbar
20. Verifikasi kotak Search tertutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung kembali ke semua baris (enam baris)

### TC-FA-LIC-231, TC-FA-LIC-232, dan TC-FA-LIC-261: Search per kelas kolom dan format angka

Untuk setiap baris tabel "Anggota pencarian per kelas kolom" (langkah 23 sampai 25):

23. Ketik Search kata kunci baris tabel, tekan Enter
24. Verifikasi tabel menampilkan hasil baris tabel
25. Kosongkan isi kotak search, tekan Enter

26. Klik icon panah `(←)` di kiri toolbar

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (26 langkah nominal; 53 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Search tabel Allocation History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 23 sampai 25 diulang per anggota (sepuluh iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per iterasi (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 25 (mengosongkan Search antar anggota; Enter pada kotak kosong mengembalikan semua baris), dan langkah 26 (menutup kotak Search).
- Asersi di luar Expected TC (S-03): kata kunci langkah 8 (`2`) dan `2025` dipilih spec karena TC-FA-LIC-230 menulis "1 karakter" dan "kata kunci lagi"; hasil enam baris diturunkan dari Pre-setup #13. Baris tabel hasil "tidak ada baris" diasersi sebagai empty state `No results found` (anchor positif bahwa tabel sudah memproses Search; bagian 8b butir 2) padahal Expected TC-FA-LIC-232 dan 261 menulis "tidak ada baris".
- Temuan untuk QA:
  - TC-FA-LIC-230 (langkah TC 3) menulis "Ketik 1 karakter" tanpa menyebut karakternya; spec memakai `2`.
  - TC-FA-LIC-232 dan 261 mengasersi pencarian angka dengan pemisah `3,000` dan `1,500`; hasil "tidak ada baris" tidak menyebut teks empty state.
  - TC-FA-LIC-230, 231, 232, dan 261 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
  - Pre-setup #13 memuat satu nilai Plan Owner (`PT Maju Bersama (Distributor)`) untuk keenam alokasi, sedangkan asersi Search per kolom memerlukan sedikitnya dua nilai distinct pada kolom yang dicari (S-11): Search kolom Plan Owner `Maju` mengembalikan seluruh baris sehingga tidak membuktikan penyaringan. TC tidak diubah dan spec tidak menambah baris milik spec ber-Plan Owner lain, karena Expected TC menyebut enam baris Pre-setup #13.
