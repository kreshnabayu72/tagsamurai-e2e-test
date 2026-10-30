---
id: TC-GS-TAG-E2E-059-sinkronisasi-fams-receive-manual-dan-pair-tag-to-be-returned
title: "Sinkronisasi FAMS: Receive Manually Menjadi Damaged/Missing dan Pair TAG ke Tag To be Returned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-366
  - TC-GS-TAG-367
coverage:
  web: automated
---

# Sinkronisasi FAMS: Receive Manually Menjadi Damaged/Missing dan Pair TAG ke Tag To be Returned

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah status satu tag (DD-15) lewat aksi FAMS; tidak ada penghapusan data.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Pemicu (sesi API aktor, tidak diasersi): akun FAMS Client A pemegang Update di tab To Be Returned (`Receive Manually`, `Pair TAG`). TC tidak menyebut email akun ini; spec memakai Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`, dan kesesuaiannya perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-15 `E28011606000020F00000001` (disetel To be Returned dengan Return Group `Gudang Pusat` lewat fixture BE sebelum tiap TC), DD-02 (Available). Aset `Not Paired Yet` di FAMS untuk TC-GS-TAG-367 (Return Group DD-15 dalam scope Group user FAMS). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum tiap TC.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): akun FAMS menjalankan `Receive Manually` dan `Pair TAG`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk `Receive Manually` (dengan Note) dan `Pair TAG` dengan pemindaian tag (simulasi reader; D-4); penanda event selesai diproses (Eventual/SSE); pembacaan relasi aset dan user sebuah tag; seed dan reset idempotent Seed Registri A dan keadaan To be Returned DD-15.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan DD-15 dan aset FAMS yang dibuat lewat fixture BE, dan kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-366: Receive Manually menjadi Damaged/Missing

1. Atur DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) lewat fixture BE, muat ulang halaman
2. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
3. Verifikasi DD-15 berstatus `To be Returned`
4. Jalankan `Receive Manually` pada tag DD-15 di FAMS tab To Be Returned lewat sesi API, isi Note `Tag patah saat diterima`, lalu konfirmasi
5. Verifikasi status DD-15 `Damaged/Missing` (badge danger) di Tab All tanpa muat ulang
6. Klik Tab Not Paired
7. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
8. Verifikasi baris DD-15 tampil di Tab Not Paired
9. Verifikasi DD-15 tidak tertaut ke aset maupun user
10. Buka menu baris DD-15, lalu klik `TAG Log`
11. Verifikasi entri `TAG Marked Damaged/Missing by [pelaku penerima di FAMS]` dengan `Previous Status: To be Returned` dan `Note: Tag patah saat diterima`
12. Verifikasi tidak ada entri `TAG Received by ...` maupun `Unpaired`
13. Tutup popup TAG Log

### TC-GS-TAG-367: Pair TAG di FAMS dengan tag To be Returned

14. Atur DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) dan sediakan aset `Not Paired Yet` di FAMS lewat fixture BE, muat ulang halaman, lalu klik Tab All
15. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
16. Verifikasi DD-15 berstatus `To be Returned`
17. Jalankan `Pair TAG` pada aset `Not Paired Yet` di FAMS lewat sesi API, pindai tag DD-15, lalu Submit
18. Verifikasi status DD-15 `Paired` (badge info) di Tab All tanpa muat ulang
19. Klik Tab Paired
20. Verifikasi baris DD-15 tampil di Tab Paired
21. Buka menu baris DD-15, lalu klik `TAG Log`
22. Verifikasi entri `TAG Paired by [pelaku user yang melakukan pair]` dengan `Type: Asset`, `Asset`, `Asset Code`, `Module`, dan `Previous Status: To be Returned`
23. Verifikasi tidak ada entri `TAG Received by ...`
24. Tutup popup TAG Log
25. Klik Tab Not Paired
26. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
27. Verifikasi DD-02 tampil di Tab Not Paired
28. Verifikasi baris DD-15 tidak ada di Tab Not Paired

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 14 (memulihkan DD-15 ke To be Returned), 6, 19, dan 25 (pindah tab), 13 dan 24 (menutup popup TAG Log), 7 dan 26 (mengubah Rows per page menjadi 50 setelah pindah tab supaya DD-15 di halaman 2 tampil; ukuran halaman tidak diasumsikan terbawa antar tab). Rows per page 50 pada langkah 2 dan 15 adalah langkah TC sumber; ukuran halaman dikembalikan ke 10 di hook `after`.
- Asersi tambahan di luar Expected TC (S-03): langkah 3 dan 16 (keadaan awal `To be Returned` agar "berubah dari" bermakna); langkah 27 (data pembanding sebagai anchor absence, bagian 8b butir 2).
- Temuan untuk QA:
  - Q-9: langkah dan selektor FAMS (`Receive Manually`, `Pair TAG`) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - Q-15: `[pelaku penerima di FAMS]` dan `[pelaku user yang melakukan pair]` pada TAG Log tidak diberi nilai dan format penulisan nama; akun FAMS "pemegang Update di tab To Be Returned" tidak diberi email di TC (Pre-setup TC memuat Admin FAMS dan Manage asset & TAG (Update) FAMS).
  - Expected a kedua TC menyatakan "status tidak pernah `Available` pada alur ini"; riwayat status tidak teramati lewat UI, sehingga spec hanya mengasersi status akhir dan tidak adanya entri `TAG Received by ...` serta `Unpaired` pada TAG Log.
  - Q-4: identifier tetap; kondisi DD-15 To be Returned bergantung pada fixture BE (Return Group `Gudang Pusat`).
  - Post Condition TC-GS-TAG-366 dan 367 identik dengan Expected a dan b.
