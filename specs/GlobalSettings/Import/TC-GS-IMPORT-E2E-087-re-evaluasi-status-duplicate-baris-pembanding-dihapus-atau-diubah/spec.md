---
id: TC-GS-IMPORT-E2E-087-re-evaluasi-status-duplicate-baris-pembanding-dihapus-atau-diubah
title: "Re-evaluasi status duplicate: baris pembanding dihapus atau diubah, rekaman sistem dihapus atau dibuat setelah staging, Save tanpa perubahan pada baris duplicate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-188
  - TC-GS-IMPORT-567
  - TC-GS-IMPORT-568
  - TC-GS-IMPORT-647
  - TC-GS-IMPORT-870@L1020
coverage:
  web: automated
---

# Re-evaluasi status duplicate: baris pembanding dihapus atau diubah, rekaman sistem dihapus atau dibuat setelah staging, Save tanpa perubahan pada baris duplicate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan spec ini mengubah master data Brand Client C (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua (hanya memicu perubahan, tanpa asersi UI di sesinya, P-2): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup), memakai sesi API, password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (nama env baru, didaftarkan pada tahap script). Klien HTTP untuk sesi API disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (berkas fixture uji, D-07; nilai bersuffix per run bila membuat atau menghapus master data):
  - D-22 (draft Brand 3 baris Client C, dibuat lewat skrip fixture sebelum TC-647 dan sebelum TC-188): #1 `Pioneer` berstatus `duplicate`, #2 `Nexus` berstatus `pending`, #3 `Pioneer` berstatus `pending`.
  - Brand milik spec `Nova Duplicate {runId}-087`, dibuat lewat API oleh langkah 1; berkas `brand-nova.csv`: header `Brand Name`; 1 baris `Nova Duplicate {runId}-087` (TC-567).
  - Berkas `brand-late.csv`: header `Brand Name`; 1 baris `Late Brand {runId}-087`; Brand `Late Brand {runId}-087` dibuat oleh Admin kedua Client C lewat sesi API pada langkah 23 (TC-568).
  - Berkas `brand-pair.csv`: header `Brand Name`; 2 baris `Acme Corp {runId}-087` dan `Acme Corp {runId}-087` (baris 1 `duplicate`, baris 2 `pending` setelah Confirm Mapping; TC-870@L1020).
  - Nilai ubahan TC-647: Brand Name baris #3 menjadi `Pioneer Plus`.
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft dan seeding draft D-22 (disediakan tim FE/BE), sesi API Admin kedua untuk membuat Brand.
- State global: master data Brand Client C diubah (Brand `Nova Duplicate {runId}-087` dihapus di langkah 16; Brand `Late Brand {runId}-087` dibuat di langkah 23). Hook `after` memulihkan state (menghapus `Late Brand {runId}-087` dan `Nova Duplicate {runId}-087` bila masih ada) dan membuang draft Brand Client C walau spec gagal di tengah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `Nova Duplicate {runId}-087` dan `Late Brand {runId}-087` bila masih ada; buang draft Brand Client C lewat skrip reset.

## Test Steps

### TC-GS-IMPORT-647: Baris pembanding diubah lewat Save

1. Buat Brand `Nova Duplicate {runId}-087` di master data Client C lewat API (aksi tanpa `Verifikasi`; klien HTTP disediakan tim FE/BE)
2. Seed draft D-22 di Client C lewat skrip fixture (aksi tanpa `Verifikasi`), lalu muat ulang halaman Import > Brand
3. Klik `⋯` pada baris #3 `Pioneer`, pilih `Edit`
4. Ubah Brand Name baris #3 menjadi `Pioneer Plus`
5. Klik `[Save]`
6. Verifikasi muncul toast: "Success, row has been updated."
7. Verifikasi badge Status baris #1 `Pioneer` bertuliskan `pending`
8. Verifikasi badge Status baris #3 `Pioneer Plus` bertuliskan `pending`
9. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)

### TC-GS-IMPORT-567: Rekaman sistem dihapus setelah staging

10. Tunggu toast lama hilang otomatis; reset draft Brand Client C lewat skrip reset, lalu muat ulang halaman
11. Klik `[Upload File]`
12. Pilih berkas `brand-nova.csv` pada file picker
13. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
14. Verifikasi badge Status baris 1 bertuliskan `duplicate`
15. Buka Global Settings > Master Reference > Brand
16. Ketik Search `Nova Duplicate {runId}-087`, tekan Enter; klik row action `Delete` pada Brand `Nova Duplicate {runId}-087`; konfirmasi dialog hapus Brand
17. Tunggu aksi selesai (permintaan mendapat respons)
18. Buka Import > Brand, lalu muat ulang halaman
19. Verifikasi badge Status baris 1 bertuliskan `pending`
20. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 0 (Disabled)

### TC-GS-IMPORT-568: Rekaman bentrok dibuat setelah staging

21. Reset draft Brand Client C lewat skrip reset, lalu muat ulang halaman; klik `[Upload File]`, pilih berkas `brand-late.csv` pada file picker, klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
22. Verifikasi badge Status baris 1 bertuliskan `pending`
23. Admin kedua Client C membuat Brand `Late Brand {runId}-087` lewat sesi API hingga tersimpan
24. Muat ulang halaman Import > Brand
25. Verifikasi badge Status baris 1 bertuliskan `duplicate`
26. Arahkan kursor ke badge Status baris 1
27. Verifikasi tooltip pada badge Status baris 1: "Brand name already exists. This row will be skipped automatically."
28. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0 (Disabled), Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-870@L1020: Save tanpa perubahan pada sesi yang memuat baris duplicate

29. Tunggu toast lama hilang otomatis; reset draft Brand Client C lewat skrip reset, lalu muat ulang halaman
30. Klik `[Upload File]`, pilih berkas `brand-pair.csv` pada file picker, klik `[Confirm Mapping]`
31. Aktifkan Switch `Edit this page`
32. Klik `[Save]` tanpa mengubah nilai apa pun
33. Verifikasi muncul toast netral: "No changes to save."
34. Verifikasi sesi edit ditutup (Switch `Edit this page` kembali OFF)
35. Verifikasi badge Status baris 1 bertuliskan `duplicate`
36. Verifikasi badge Status baris 2 bertuliskan `pending`

### TC-GS-IMPORT-188: Baris pembanding dihapus (dijalankan paling akhir karena menghapus baris)

37. Tunggu toast lama hilang otomatis; seed draft D-22 di Client C lewat skrip fixture, lalu muat ulang halaman Import > Brand
38. Klik `⋯` pada baris 3 `Pioneer`, pilih `Remove`
39. Klik `[Delete]` pada dialog Delete Row
40. Verifikasi muncul toast: "Success, row has been deleted."
41. Verifikasi draft berisi 2 baris
42. Muat ulang halaman Import > Brand
43. Verifikasi badge Status baris 1 `Pioneer` bertuliskan `pending`
44. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 0 (Disabled)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-188 dijalankan paling akhir (menghapus baris), TC-647 dijalankan pertama karena memakai D-22 yang sama sebelum penghapusan (prinsip 5 bagian 3).
- P-2: Admin kedua Client C (langkah 23) hanya memicu pembuatan Brand lewat sesi API, bukan objek asersi; tidak ada sesi UI kedua.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 2, 10, 21, 29, dan 37 (pembuatan Brand lewat API, menunggu toast, seed atau reset draft, muat ulang) menjalankan Precondition draft; langkah 15, 16, 17, 18 menjalankan langkah 5 sampai 9 TC-567 (Search pada langkah 16 untuk menemukan baris target); langkah 24 menjalankan langkah 6 TC-568.
- Langkah penghubung "Tunggu aksi selesai" (aksi tanpa `Verifikasi`): langkah 17 menunggu penghapusan Brand pada langkah 16 selesai (permintaan mendapat respons) sebelum langkah 18 berpindah ke Import > Brand dan memuat ulang halaman.
- Spec berisi 44 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dengan satu topik re-evaluasi status duplicate, tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - ID ganda: `TC-GS-IMPORT-870` dipakai dua kali di `tc-import.md` (baris 1020 Save no-op, baris 1079 Cancel dialog konflik kunci); spec ini memakai `870@L1020`. TC tidak diubah.
  - TC-GS-IMPORT-567 dan 568 memakai Brand `Nova Duplicate` dan `Late Brand` yang dihapus atau dibuat; spec memakai nama bersuffix milik spec (S-06) agar Pre-setup Client C tidak diubah.
  - TC-GS-IMPORT-870@L1020 Post Condition ("Draft tidak berubah"; "Tidak ada entri log", dengan awalan ganda `a. a.` dan `b. b.` pada kolom) tidak punya langkah observasi sendiri; Draft tidak berubah sudah diasersi pada Expected b, "Tidak ada entri log" tidak diasersi (S-01, S-05).
  - TC-GS-IMPORT-870@L1020 Expected b "kunci dilepas" tidak punya cara amat di UI untuk aktor ini; spec hanya mengasersi sesi edit ditutup (Switch `Edit this page` kembali OFF), dan pelepasan kunci tidak diasersi.
  - TC-GS-IMPORT-188 Precondition menyebut baris #1 sebagai `duplicate` dari D-22 yang disiapkan fixture; skrip seeding D-22 tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE (S-13).
  - Penanda selesai untuk langkah 17 (konfirmasi dialog hapus Brand) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - Mekanisme skrip reset draft Brand (Kontrak Fixture R1) disediakan tim FE/BE (S-13).
