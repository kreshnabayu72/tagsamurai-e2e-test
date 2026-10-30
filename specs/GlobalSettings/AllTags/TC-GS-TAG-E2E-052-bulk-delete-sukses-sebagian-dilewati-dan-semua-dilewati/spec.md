---
id: TC-GS-TAG-E2E-052-bulk-delete-sukses-sebagian-dilewati-dan-semua-dilewati
title: "Bulk Delete: Sukses (Toast T-22, Seleksi Reset, Kuota, Event Log), Sebagian Dilewati T-31 dengan Delete Detail, dan Semua Dilewati T-24"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-153
  - TC-GS-TAG-155
  - TC-GS-TAG-177
coverage:
  web: automated
---

# Bulk Delete: Sukses (Toast T-22, Seleksi Reset, Kuota, Event Log), Sebagian Dilewati T-31 dengan Delete Detail, dan Semua Dilewati T-24

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini menghapus data registri; Bulk Delete sukses penuh (TC-GS-TAG-153) dijalankan terakhir.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`). Baris yang dipakai: DD-15 `E28011606000020F00000001`, DD-16 `E28011606000020F00000002`, DD-17 `E28011606000020F00000003`, DD-18 `E28011606000020F00000004` (RFID Object Available, filler). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum TC-GS-TAG-155 dan 153.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): pemicu "Dari FAMS, pair tag" memakai sesi API Admin FAMS (kemampuan "disediakan tim FE"; mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD; Q-5, Q-9) yang hanya memicu perubahan state dan tidak menjadi objek asersi.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A; sesi API pair tag DD-16 dan DD-17 ke aset tepat saat dialog Bulk Delete terbuka dan sebelum `Delete` diklik; pembacaan jumlah baris Event Log Tab Activate TAG (baseline).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): unpair DD-16 dan DD-17, kembalikan Seed Registri A lewat fixture BE, dan kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-177: Bulk Delete dengan seluruh baris dilewati saat commit

1. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
2. Centang DD-16 dan DD-17
3. Pilih `Bulk Action` > `Delete` dan biarkan dialog terbuka
4. Pair tag DD-16 dan DD-17 ke aset lewat sesi API Admin FAMS hingga tersimpan
5. Klik `Delete` pada dialog
6. Verifikasi toast error `Error, failed to delete TAGs.`
7. Verifikasi tidak ada toast sukses
8. Verifikasi daftar di-refresh
9. Klik Tab Paired
10. Verifikasi DD-16 dan DD-17 tetap berstatus `Paired`

### TC-GS-TAG-155: Sebagian baris tidak lagi eligible saat commit

11. Pulihkan DD-15, DD-16, dan DD-17 menjadi Available lewat fixture BE, muat ulang halaman, lalu klik Tab Not Paired
12. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
13. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
14. Centang DD-16 dan DD-15
15. Pilih `Bulk Action` > `Delete` dan biarkan dialog terbuka
16. Pair tag DD-16 ke aset lewat sesi API Admin FAMS hingga tersimpan
17. Klik `Delete` pada dialog
18. Verifikasi toast sukses `Success, TAG has been deleted. Some TAGs were skipped because they are no longer eligible.`
19. Klik Tab All
20. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
21. Verifikasi DD-15 terhapus (tidak ada di registri)
22. Verifikasi DD-16 tetap tampil di registri
23. Buka Event Log > Tab Activate TAG
24. Verifikasi satu baris baru Activity `Delete` dengan Success `1` dan Failed `1` (baris bertambah satu dari jumlah yang dicatat)
25. Klik `Detail` pada baris Delete baru
26. Verifikasi section `Deleted` memuat DD-15
27. Verifikasi section `Failed` memuat DD-16 dengan kolom Status Sebelum Dihapus terisi
28. Tutup popup Detail dan modal Event Log

### TC-GS-TAG-153: Bulk Delete sukses

29. Pulihkan DD-15, DD-16, DD-17, dan DD-18 menjadi Available lewat fixture BE, muat ulang halaman, lalu klik Tab All
30. Catat nilai kartu RFID – Object TAG
31. Klik Tab Not Paired
32. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
33. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
34. Centang DD-15 sampai DD-18
35. Pilih `Bulk Action` > `Delete`
36. Klik `Delete` pada dialog
37. Verifikasi toast sukses `Success, TAG has been deleted.`
38. Verifikasi empat baris DD-15 sampai DD-18 hilang dari registri
39. Verifikasi Bulk Action Bar tertutup
40. Verifikasi seleksi 0
41. Klik Tab All
42. Verifikasi kartu RFID – Object TAG terpakai berkurang 4 dari nilai yang dicatat
43. Buka Event Log > Tab Activate TAG
44. Verifikasi satu baris baru Activity `Delete` dengan Success `4` (baris bertambah satu dari jumlah yang dicatat)

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (44 langkah nominal). Alasan: tiga TC satu topik (Bulk Delete atas Tab Not Paired) dengan satu dataset Seed Registri A dan satu kelas harness; tiap blok memulihkan data lewat fixture BE sehingga berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (153, 155, 177) dibalik menjadi 177, 155, 153 supaya Bulk Delete yang menghapus baris sungguhan (153, lalu 155) berada di akhir; pemicu pair pada 177 dan 155 memakai DD-16 yang dipulihkan di langkah 11 dan 29.
- P-1 tidak dipakai.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 9 (pindah tab untuk mengamati DD-16 dan DD-17 yang Paired), 11 dan 29 (memulihkan data), 13, 30, 33 (mencatat baseline), 31 (kembali ke Tab Not Paired setelah membaca kartu di Tab All), 19 (pindah ke Tab All untuk mengamati DD-16), 41 (pindah ke Tab All, tempat License Counter Card tampil), 23 dan 43 (membuka Event Log), 28 (menutup popup), 1, 12, 20, dan 32 (mengubah Rows per page menjadi 50 supaya DD-15 sampai DD-18 di halaman 2 tampil; ukuran halaman tidak diasumsikan terbawa antar tab atau muat ulang, dan dikembalikan ke 10 di hook `after`).
- Asersi tambahan di luar Expected TC (S-03): langkah 10 (DD-16 dan DD-17 tetap `Paired`) mengikuti Expected b TC-GS-TAG-177; langkah 24 mengikuti Post Condition b TC-GS-TAG-155 (TC memberi langkah observasi Event Log pada langkah 4 TC).
- Temuan untuk QA:
  - Q-4: identifier Seed Registri A tetap dan kartu `21 of 50` valid hanya bila Seed Registri A dipulihkan.
  - Q-5: pemicu "dari FAMS, pair tag" tepat saat dialog terbuka tidak deterministik dan mekanismenya tidak didefinisikan.
  - TC-GS-TAG-155 Expected c menyebut kolom "Status Sebelum Dihapus" untuk DD-16 di section `Failed` tanpa nilai (Available saat dialog dibuka, atau Paired saat commit); spec hanya mengasersi kolom terisi.
  - TC-GS-TAG-153 Expected c "terpakai berkurang 4" tidak menyebut nilai absolut; spec memakai selisih dari baseline yang dicatat.
  - TC-GS-TAG-177 Expected b "daftar di-refresh" tidak menyebut cara mengamati; spec mengasersinya lewat pemuatan ulang data tabel yang dapat diamati harness (disediakan tim FE).
  - Post Condition TC-GS-TAG-153 butir a, b, c identik dengan Expected b, c, d. Post Condition TC-GS-TAG-155 butir a identik dengan Expected b; butir b diasersi di langkah 24.
