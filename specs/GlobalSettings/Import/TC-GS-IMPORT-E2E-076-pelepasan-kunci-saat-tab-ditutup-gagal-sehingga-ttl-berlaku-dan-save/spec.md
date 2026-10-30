---
id: TC-GS-IMPORT-E2E-076-pelepasan-kunci-saat-tab-ditutup-gagal-sehingga-ttl-berlaku-dan-save
title: "Pelepasan Kunci saat Tab Ditutup Gagal sehingga TTL Berlaku, dan Save Ditolak setelah Capability Dicabut lalu Kunci Lepas setelah TTL"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-207
  - TC-GS-IMPORT-668
coverage:
  web: automated
---

# Pelepasan Kunci saat Tab Ditutup Gagal sehingga TTL Berlaku, dan Save Ditolak setelah Capability Dicabut lalu Kunci Lepas setelah TTL

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah jam server dan capability role; lihat `suite.md`.
- Dua sesi browser (kelas harness eksternal; sesi kedua menjadi objek asersi), konteks terpisah dengan sesi login sendiri:
  - TC-GS-IMPORT-207: Sesi TC Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`, dan Sesi Admin kedua Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`; keduanya login di hook `before`.
  - TC-GS-IMPORT-668: Sesi Import data (Create) Client A (Rina Marlina) `importCreate_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_IMPORTCREATE_PASSWORD`, dan Sesi Admin kedua yang sama dengan blok pertama (login lewat langkah ganti akun untuk Sesi Import data (Create)).
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks kedua, memulihkan capability dan jam server, dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`).
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi):
  - Fixture kegagalan pelepasan kunci saat tab ditutup (TC-GS-IMPORT-207; mekanisme paksa gagal tidak didefinisikan di TC, kemungkinan intercept atau blokir jaringan) dan penanganan dialog native browser `beforeunload` pada penutupan tab.
  - Fixture jam server: dimajukan 10 menit (TC-GS-IMPORT-207) atau 12 menit (TC-GS-IMPORT-668); hanya jam server karena TTL kunci dihitung murni di server dan tidak diamati lewat countdown UI. Dipulihkan lewat langkah eksplisit.
  - Margin jam (8b.3): usia kunci hanya bertambah oleh waktu nyata (arah aman ke kedaluwarsa). TC-GS-IMPORT-207 (langkah 12): jam dimajukan tepat 10 menit sehingga usia kunci 10 menit ditambah waktu nyata sejak sesi edit dimulai (margin 0 menit terhadap TTL 10 menit, hitung: 10 menit dikurangi 10 menit); dialog langkah 10 dibaca sebelum jam dimajukan dengan usia kunci hanya selama waktu nyata beberapa detik. TC-GS-IMPORT-668 (langkah 28): jam dimajukan 12 menit, margin 2 menit di atas TTL (12 menit dikurangi 10 menit).
  - TC-GS-IMPORT-668: perubahan capability Import data pada role akun Import data (Create) dari Create menjadi Read saja lewat Role & Permission (UI atau fixture yang disediakan tim FE/BE), dipulihkan ke Create sesudah TC.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk semua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: capability role, jam server, dan draft D-01 dipulihkan di akhir tiap blok dan di hook `after`.

## Test Steps

### TC-GS-IMPORT-207: Pelepasan kunci saat tab ditutup gagal

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
4. [Sesi TC] Tutup tab browser
5. [Sesi TC] Verifikasi dialog native browser konfirmasi tutup tab tampil
6. [Sesi TC] Konfirmasi dialog native browser
7. [Sesi TC] Tunggu aksi selesai (tab tertutup)
8. [Sesi Admin kedua] Klik `⋯` pada baris #2
9. [Sesi Admin kedua] Pilih Edit
10. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
11. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
12. Majukan jam server 10 menit (fixture jam server)
13. [Sesi Admin kedua] Klik `⋯` pada baris #2
14. [Sesi Admin kedua] Pilih Edit
15. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
16. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]` tanpa dialog
17. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan jam server ke waktu nyata dan draft D-01

### TC-GS-IMPORT-668: Save ditolak bila capability dicabut dan kunci terlepas setelah TTL

18. Ganti akun: Sesi Import data (Create) login sebagai Import data (Create) Client A dan membuka Import > Brand
19. [Sesi Import data (Create)] Klik `⋯` pada baris #1
20. [Sesi Import data (Create)] Pilih Edit
21. [Sesi Import data (Create)] Ubah Brand Name baris #1 menjadi `Acme Corporation`
22. [Sesi Admin kedua] Ubah capability Import data pada role akun Import data (Create) dari Create menjadi Read saja lewat Role & Permission
23. [Sesi Admin kedua] Tunggu aksi selesai (permintaan mendapat respons)
24. [Sesi Import data (Create)] Klik `[Save]`
25. [Sesi Import data (Create)] Verifikasi toast error "You don't have permission to do this."
26. [Sesi Import data (Create)] Muat ulang halaman Import > Brand
27. [Sesi Import data (Create)] Verifikasi baris #1 menampilkan `Acme Corp` (perubahan tidak tersimpan)
28. Majukan jam server 12 menit (fixture jam server)
29. [Sesi Admin kedua] Buka Import > Brand
30. [Sesi Admin kedua] Klik `⋯` pada baris #2
31. [Sesi Admin kedua] Pilih Edit
32. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif untuk Admin kedua
33. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]` tanpa dialog
34. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan capability Import data (Create) ke Create, jam server ke waktu nyata, dan draft D-01

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji TTL kunci setelah pelepasan gagal dan setelah capability dicabut).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 6 (menutup tab dan mengonfirmasi dialog), langkah 7 dan 23 (menunggu aksi selesai sebelum aktor atau sesi lain bertindak), langkah 12 dan 28 (jam server), langkah 17 dan 34 (pemulihan), langkah 18 (ganti akun), langkah 26 (muat ulang), langkah 29 (membuka Import).
- Langkah 22 diperlakukan sebagai pemicu perubahan capability oleh Admin kedua; hasilnya dibaca di Sesi Import data (Create) (langkah 24 sampai 27) dan Sesi Admin kedua (langkah 29 sampai 33).
- Konteks kedua beraksi: belum ada id pengecualian untuk Sesi Admin kedua yang beraksi (Edit dan ubah capability) dan diasersi di spec kelas d (TC-GS-IMPORT-207 dan 668), dengan TC-GS-IMPORT-668 mencampur kelas c dan d; `P-2` hanya untuk konteks yang bukan objek asersi dan `P-6` hanya untuk pengamat read-only tanpa interaksi. Spec tidak dipecah (satu TC satu blok, TC mencampur c dan d); usulan aturan baru menunggu batch konvensi.
- Pembagian TC lintas spec: pelepasan kunci saat tab ditutup berhasil (best-effort, TC-GS-IMPORT-871@L1080) ada di spec 072.
- Temuan untuk QA:
  - Penanda "tab tertutup" (langkah 7) dan "permintaan mendapat respons" (langkah 23) tidak disebut di TC-GS-IMPORT-207 dan 668; keduanya dipakai sebagai penanda aman sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-207 Precondition d memakai fixture "pelepasan kunci dibuat gagal" yang tidak ada di Kontrak Fixture R1-R7 maupun Data Dinamis; mekanisme paksa gagal tidak terdefinisi (kemungkinan intercept atau blokir jaringan). Langkah 5 bergantung pada dukungan runner terhadap `beforeunload`.
  - TC-GS-IMPORT-668 memuat dua objek uji berbeda kelas dalam satu TC (capability dicabut di tengah sesi: ditolak server; lalu TTL 12 menit melepas kunci untuk Admin kedua); judul memuat keduanya.
  - Nilai waktu 12 menit pada TC-GS-IMPORT-668 ditandai `PRD?` (tidak tertulis di PRD); PRD hanya menetapkan TTL 10 menit.
  - TC-GS-IMPORT-668 menyebut kedua akun login di sesi browser terpisah tetapi tidak menyebut apakah perubahan capability oleh Admin kedua lewat UI atau fixture.
