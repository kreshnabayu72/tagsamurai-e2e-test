---
id: TC-GS-TAG-E2E-099-delete-by-scan-tooltip-dan-tag-to-be-returned-retired-lintas-fams
title: "Delete by Scan: Tooltip dan Scan Tag To be Returned/Retired dengan Efek di FAMS"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-160
  - TC-GS-TAG-358
coverage:
  web: automated
---

# Delete by Scan: Tooltip dan Scan Tag To be Returned/Retired dengan Efek di FAMS

## Prerequisites

- Mode: FE+BE (backend nyata; kelas d, harness scan hardware). Spec ini menghapus data registri; penghapusan dilakukan sesudah tooltip (screening) di awal.
- Akun aktor (ganti akun eksplisit hanya pada TC-GS-TAG-358):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun ini sebagai default suite.
  - Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`, untuk Fixed Asset > TAG > To Be Returned (TC-GS-TAG-358).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`). Baris yang dipakai: DD-07 `E2801160600002054D8A0007` (To be Returned, tampil di Fixed Asset > TAG > To Be Returned) dan DD-08 `E2801160600002054D8A0008` (Retired). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): simulasi reader RFID untuk sesi Delete by Scan (mulai sesi, pindai kode, `Stop`; D-4, Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD); seed dan reset idempotent Seed Registri A; pembacaan jumlah entri Event Log To Be Returned sebelum aksi (N tidak diturunkan dari seeding); pembacaan status dan Tagging aset terakhir DD-07. Langkah dan selektor Fixed Asset tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A lewat fixture BE; sesi dikembalikan ke Total Control Client A.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-160: Tooltip tombol Delete by Scan

1. Arahkan kursor ke tombol `Delete by Scan`
2. Verifikasi tombol enabled
3. Verifikasi tooltip informatif `This will remove the TAG and delete its activation. Scanned TAGs are deleted immediately.` muncul saat kursor diarahkan ke tombol
4. Pindahkan kursor keluar dari tombol
5. Fokus tombol `Delete by Scan` lewat keyboard
6. Verifikasi tooltip informatif yang sama muncul saat keyboard focus

### TC-GS-TAG-358: Scan tag To be Returned dan Retired

7. Ganti akun ke Admin FAMS, buka Fixed Asset > TAG > To Be Returned
8. Catat badge tab To Be Returned
9. Verifikasi DD-07 tampil di tab To Be Returned
10. Klik `Event Log`, catat jumlah entri, lalu tutup modal
11. Buka aset terakhir DD-07 di Fixed Asset, catat status dan Tagging aset
12. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All, catat nilai kartu RFID – Object TAG (`21 of 50`)
13. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
14. Pindai DD-07 `E2801160600002054D8A0007`
15. Verifikasi tidak ada dialog
16. Verifikasi toast sukses `Success, E2801160600002054D8A0007 has been deleted.`
17. Tutup toast
18. Pindai DD-08 `E2801160600002054D8A0008`
19. Verifikasi toast sukses `Success, E2801160600002054D8A0008 has been deleted.`
20. Klik `Stop` pada widget
21. Verifikasi kartu RFID – Object TAG `20 of 50`
22. Ganti akun ke Admin FAMS, buka Fixed Asset > TAG > To Be Returned
23. Ketik Search `E2801160600002054D8A0007`, tekan Enter
24. Verifikasi pencarian menampilkan `No results found` (DD-07 tidak ada lagi di tab To Be Returned)
25. Verifikasi badge tab berkurang 1 dari nilai yang dicatat
26. Klik `Event Log`
27. Verifikasi Event Log To Be Returned tidak memuat entri untuk DD-07 dan jumlah entri sama dengan yang dicatat
28. Tutup modal Event Log, lalu buka aset terakhir DD-07 di Fixed Asset
29. Verifikasi aset terakhir DD-07 tidak terpengaruh (status dan Tagging aset sama dengan yang dicatat)

## Notes

- Mode: FE+BE. Kelas d (hardware scan). Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 29 langkah, di bawah ambang sekitar 35. Dua TC satu topik Delete by Scan dengan satu kelas harness (simulasi reader) dan satu dataset Seed Registri A; tooltip (screening) di awal, lalu blok TC-GS-TAG-358 yang mengasersi modul konsumen (FAMS) lewat ganti akun yang bagian sesudahnya tetap bermakna.
- TC-GS-TAG-161, 164, 165, 181, dan 359 (Delete by Scan di Global Settings, satu akun) ada di spec 054; spec ini memuat blok lintas FAMS dengan ganti akun, sehingga kegagalan ganti akun atau FAMS tidak memengaruhi hasil spec 054.
- Langkah ganti akun eksplisit: 7, 12, 22.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 4 (memindahkan kursor), 8, 10, 11, dan 12 (mencatat baseline), 17 (menutup toast sebelum asersi toast berikutnya, S-09), 23 (Search agar baris DD-07 yang diasersi absen tampil terarah), 7, 22, dan 28 (ganti akun dan navigasi). Hook `after` mengembalikan sesi ke Total Control Client A sesudah langkah 29.
- Asersi tambahan di luar Expected TC (S-03): langkah 9, 24, dan 27 (anchor positif dan absence dengan baseline).
- Pengecualian P-1 (state berat): asersi bahwa Event Log To Be Returned tidak memuat entri DD-07 dan jumlah entri tetap (langkah 27) memakai baseline jumlah entri yang dicatat sebelum sesi scan (langkah 10; S-05, S-12) dan didahului toast sukses (langkah 16), penurunan kartu (langkah 21), dan badge tab berkurang (langkah 25) sebagai anchor positif (bagian 8b butir 2); state berat (sesi scan hardware yang menghapus DD-07) dibangun di spec ini.
- Rujukan lintas spec: TC-GS-TAG-162, 163, 173, 357, dan 362 (penolakan Delete by Scan) ada di spec 055; TC-GS-TAG-360 dan 361 (kegagalan server dan race) ada di spec 056; TC-GS-TAG-161, 164, 165, 181, dan 359 ada di spec 054.
- Temuan untuk QA:
  - Q-1: TC-GS-TAG-358 berlabel `Manual Only — (b)` (scan hardware); kemampuan simulasi reader dicatat di Prerequisites (D-4).
  - Q-4: identifier tetap dan kartu `21 of 50` valid hanya bila Seed Registri A dipulihkan.
  - Q-9: langkah dan selektor Fixed Asset tidak didefinisikan; verifikasi di FAMS hanya sejauh Expected TC.
  - Post Condition TC-GS-TAG-358 butir b (satu baris Event Log Delete di Global Settings, Success 2) tidak punya langkah observasi di TC dan tidak diasersi.
