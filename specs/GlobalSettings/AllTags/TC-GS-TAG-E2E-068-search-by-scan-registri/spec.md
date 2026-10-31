---
id: TC-GS-TAG-E2E-068-search-by-scan-registri
title: "Search by Scan Registri: Tag Dikenali di Tab Aktif, Tidak di Tab Aktif, Tak Dikenal T-09, dan Last Scanned Tidak Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-197
  - TC-GS-TAG-198
  - TC-GS-TAG-199
  - TC-GS-TAG-200
coverage:
  web: automated
---

# Search by Scan Registri: Tag Dikenali di Tab Aktif, Tidak di Tab Aktif, Tak Dikenal T-09, dan Last Scanned Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; Last Scanned DD-02 (`15/09/26 11:20`) dan Last Scanned In DD-02 (`Global Settings`) tidak boleh berubah selama spec.
- Data uji: DD-02 `E2801160600002054D8A0002` (Available, Not Paired; bukan Paired); DD-01 `E2801160600002054D8A0001`; kode acak berformat bukan TAG Samurai (nilai tidak ditetapkan TC; ditentukan penulis script dan tidak ada di registri mana pun; lihat Temuan untuk QA).
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): sesi scan dihentikan, preferensi kolom registri dihapus di browser sehingga visibilitas kembali ke default; kemampuan menghapus preferensi kolom di browser disediakan tim FE.
- Kemampuan teknis (disediakan tim FE; kelas d, D-4 dan Q-1): simulasi reader RFID yang mengirim pindaian (tanpa pemindai fisik; label TC `Manual Only — (b)` tidak menjadi alasan mengeluarkan TC); kontrol penghentian sesi scan (selektor dan mekanismenya tidak didefinisikan di TC). Spec tidak mengarang endpoint atau selektor.

## Test Steps

### Persiapan kolom (TC-GS-TAG-200 butir d)

1. Buka overlay Column Visibility lewat header kolom Actions (⋯), centang `Last Scanned In`, lalu tutup overlay

### TC-GS-TAG-197: Tag dikenali dan ada di tab aktif

2. Klik `Search by Scan`
3. Pilih teknologi `RFID` pada overlay
4. Pindai `E2801160600002054D8A0002`
5. Verifikasi search bar terisi `E2801160600002054D8A0002`
6. Verifikasi daftar menyempit ke baris `E2801160600002054D8A0002` pada Tab All
7. Akhiri sesi scan
8. Klik `(←)` pada kotak Search

### TC-GS-TAG-198: Tag dikenali tetapi tidak ada di tab aktif

9. Klik Tab Paired
10. Klik `Search by Scan`
11. Pilih teknologi `RFID` pada overlay
12. Pindai `E2801160600002054D8A0002` (Available, bukan Paired)
13. Verifikasi tidak ada toast error
14. Verifikasi empty state generik `No results found` tampil
15. Akhiri sesi scan
16. Klik `(←)` pada kotak Search
17. Klik Tab All

### TC-GS-TAG-199: Tag tidak dikenali menampilkan Toast T-09 dan sesi tidak berhenti

18. Klik `Search by Scan`
19. Pilih teknologi `RFID` pada overlay
20. Pindai kode acak berformat bukan TAG Samurai
21. Verifikasi toast error `Error, can't recognize TAG.`
22. Pindai `E2801160600002054D8A0001`
23. Verifikasi sesi scan tetap berjalan setelah toast error (pindaian berikutnya diproses)
24. Verifikasi daftar menyempit ke baris `E2801160600002054D8A0001` (DD-01)
25. Akhiri sesi scan
26. Klik `(←)` pada kotak Search

### TC-GS-TAG-200: Search by Scan tidak memperbarui Last Scanned dan Last Scanned In

27. Catat Last Scanned (`15/09/26 11:20`) dan Last Scanned In (`Global Settings`) baris DD-02
28. Klik `Search by Scan`
29. Pilih teknologi `RFID` pada overlay
30. Pindai `E2801160600002054D8A0002`
31. Akhiri sesi scan
32. Klik `(←)` pada kotak Search (menghapus keyword)
33. Verifikasi Last Scanned baris DD-02 tetap `15/09/26 11:20`
34. Verifikasi Last Scanned In baris DD-02 tetap `Global Settings`
35. Buka overlay Column Visibility, hapus centang `Last Scanned In`, lalu tutup overlay

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas harness: d (scan hardware tersimulasi). Seluruh TC di spec ini bertanda `Manual Only — (b) pemindaian scanner hardware` di kolom Automation TC; keputusan D-4 menahan TC di E2E dengan simulasi reader yang tertulis di Prerequisites ("disediakan tim FE"), karena hambatan teknis bukan alasan mengeluarkan TC (konvensi bagian 2).
- Urutan TC sumber dipertahankan (197 sampai 200). Tidak ada aksi destruktif; TC-GS-TAG-200 di akhir karena menjadi pembanding state yang tidak boleh berubah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (menampilkan Last Scanned In, precondition TC-GS-TAG-200 butir d), langkah 7, 15, 25, 31 (mengakhiri sesi scan supaya pembukaan Search by Scan berikutnya tidak bertabrakan dengan sesi sebelumnya), langkah 8, 16, 26, 32 (mengosongkan Search), langkah 17 (kembali ke Tab All), langkah 35 (memulihkan visibilitas kolom). Langkah 27 adalah langkah TC (mencatat baseline), bukan penghubung.
- Absence toast error (langkah 13) diletakkan segera setelah pemicu pindaian dan sebelum asersi empty state; pindaian itu sendiri menjadi anchor positif dan empty state `No results found` menyusul sebagai buktinya (bagian 8b butir 11).
- Temuan untuk QA:
  - Penghentian sesi scan Search by Scan tidak didefinisikan di TC maupun PRD yang dibaca (apakah sesi berhenti sendiri setelah satu pindaian atau tetap aktif). Expected TC-GS-TAG-199 butir b menyatakan sesi "berlanjut" setelah toast error, sehingga spec menulis "Akhiri sesi scan" sebagai langkah penghubung yang kontrolnya disediakan tim FE.
  - TC-GS-TAG-199 menyebut data uji "Kode acak" tanpa nilai; spec memakai kode berformat bukan TAG Samurai yang ditentukan di tahap script.
  - TC-GS-TAG-197 sampai 200 mensyaratkan "Pemindai fisik tersambung"; spec menggantinya dengan simulasi reader (D-4, Q-1) dan tidak menguji pemindai fisik.
  - TC-GS-TAG-200 langkah 3 ("Hapus keyword") tidak menyebut cara menghapus keyword; spec memakai klik `(←)` pada kotak Search (bagian 8b butir 9).
  - Hitungan dan nilai Seed Registri A bergantung pada dataset utuh dan suite serial (Q-4).
