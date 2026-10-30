---
id: TC-GS-TAG-E2E-061-sinkronisasi-retire-un-retire-combine-dan-separate
title: "Sinkronisasi: Pemensiunan Tag (SSE), Un-Retire dari Supply Asset, serta Combine dan Separate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-301
  - TC-GS-TAG-302
  - TC-GS-TAG-303
coverage:
  web: automated
---

# Sinkronisasi: Pemensiunan Tag (SSE), Un-Retire dari Supply Asset, serta Combine dan Separate

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah status tag lewat aksi FAMS/Supply Asset dan memisahkan lalu menggabungkan kembali tag combined; tidak ada penghapusan data.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Akses Global Settings > TAG Combine & Separate dipakai oleh akun ini.
- Pemicu (P-2, sesi API, tidak diasersi): pemensiunan tag oleh FAMS/Supply Asset (TC-GS-TAG-301) dan Un-retire oleh akun Supply Asset yang berwenang (TC-GS-TAG-302). Akun Supply Asset tidak ada di Pre-setup TC dan disediakan tim FE (S-13); pemensiunan oleh FAMS memakai Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.FA_ADMIN_PASSWORD`. Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`). Baris yang dipakai: DD-12 `E2801160600002054D8A0012` (RFID Object Available, dipensiunkan), DD-08 `E2801160600002054D8A0008` (RFID Retired, di-Un-retire), DD-11 `E2801160600002054D8A0011` (RFID) dan DD-13 `04A224B2C15E83` (NFC) yang combined. Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum tiap TC.
- Kemampuan teknis (disediakan tim FE/BE): sesi API pemensiunan dan Un-retire; penanda event selesai diproses (Eventual/SSE); simulasi reader RFID dan NFC untuk wizard Combine (D-4, Q-1); langkah rinci halaman Combine & Separate (selektor dan alur pemisahan) tidak didefinisikan di TC, PRD, atau LLD ("disediakan tim FE"); seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-08, DD-11, DD-12, DD-13) lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.
- Tabel "Pasangan combined": DD-11 `E2801160600002054D8A0011` (pasangan DD-13) dan DD-13 `04A224B2C15E83` (pasangan DD-11).

## Test Steps

### TC-GS-TAG-301: Pemensiunan tag oleh FAMS/Supply Asset

1. Catat nilai kartu RFID – Object TAG (`21 of 50`)
2. Pensiunkan tag DD-12 di FAMS/Supply Asset lewat sesi API hingga tersimpan
3. Tunggu event diproses (Eventual)
4. Verifikasi status DD-12 `Retired` tanpa muat ulang
5. Verifikasi kartu RFID – Object TAG terpakai berkurang 1 dari nilai yang dicatat (`20 of 50`)
6. Buka menu baris DD-12, lalu klik `TAG Log`
7. Verifikasi entri `Retired` dengan `Previous Status`
8. Tutup popup TAG Log

### TC-GS-TAG-302: Un-retire dari Supply Asset

9. Pulihkan Seed Registri A lewat fixture BE (DD-08 Retired, DD-12 Available), lalu muat ulang halaman
10. Buka menu baris DD-08 (Retired)
11. Verifikasi menu hanya berisi `TAG Log` dan `Delete` (tidak ada aksi ubah status Retired atau Un-retire dari registri)
12. Tutup menu
13. Lakukan Un-retire pada tag DD-08 di Supply Asset lewat sesi API hingga tersimpan
14. Tunggu event diproses (Eventual)
15. Verifikasi status DD-08 `Available` tanpa muat ulang
16. Klik Tab Not Paired
17. Verifikasi DD-08 tampil di Tab Not Paired
18. Buka menu baris DD-08, lalu klik `TAG Log`
19. Verifikasi entri baru `Recovered` dengan `Previous Status: Retired`
20. Tutup popup TAG Log
21. Verifikasi kartu RFID – Object TAG terpakai bertambah 1 (`22 of 50`)

### TC-GS-TAG-303: Combine dan Separate

22. Pulihkan Seed Registri A lewat fixture BE (DD-11 dan DD-13 combined), muat ulang halaman, lalu klik Tab All
23. Buka Global Settings > TAG Combine & Separate
24. Pisahkan DD-11 dan DD-13
25. Kembali ke Global Settings > TAG Tab All
26. Untuk setiap baris pada tabel "Pasangan combined" (langkah 27 sampai 30):
27. Verifikasi baris tag tidak menampilkan ikon 🔗
28. Buka menu baris tag, lalu klik `TAG Log`
29. Verifikasi TAG Log tag memuat `Separated`
30. Tutup popup TAG Log
31. Buka Global Settings > TAG Combine & Separate
32. Gabungkan kembali dengan memindai DD-11 lalu DD-13 di wizard Combine, lalu Submit
33. Kembali ke Global Settings > TAG Tab All
34. Untuk setiap baris pada tabel "Pasangan combined" (langkah 35 sampai 41):
35. Verifikasi baris tag menampilkan ikon 🔗
36. Klik ikon 🔗 pada baris tag
37. Verifikasi popup Combined TAG memuat pasangannya
38. Tutup popup Combined TAG
39. Buka menu baris tag, lalu klik `TAG Log`
40. Verifikasi TAG Log tag memuat `Combined`
41. Tutup popup TAG Log

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (41 langkah nominal, sekitar 54 setelah ekspansi dua blok ulang: langkah 27 sampai 30 untuk 2 tag dan langkah 35 sampai 41 untuk 2 tag). Alasan: tiga TC satu topik (sinkronisasi perubahan status tag dan relasi combined ke registri) dengan satu dataset Seed Registri A dan satu kelas harness; tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di langkah 9 dan 22. Langkah berulang memakai idiom tabel di Prerequisites (langkah 26 dan 34).
- Perubahan urutan di dalam TC-GS-TAG-302 (S-05 butir terakhir): Expected d (modul GS tidak menyediakan kontrol Un-retire) hanya bermakna selagi DD-08 masih Retired, sehingga diamati di langkah 10 sampai 12 sebelum pemicu Un-retire (langkah 13); TC sumber menaruhnya di Expected sesudah Un-retire.
- Pengecualian P-2: pemensiunan dan Un-retire hanyalah pemicu state lewat sesi API; objek asersi adalah status, kartu, dan TAG Log di registri Global Settings. Aksi Separate dan Combine (TC-GS-TAG-303) dijalankan langsung oleh Total Control Client A pada Global Settings.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 (baseline kartu), 8, 20, 30, 38, dan 41 (menutup popup), 9 dan 22 (memulihkan data lewat fixture BE), 12 (menutup menu), 16 (pindah tab), 25 dan 33 (kembali ke registri).
- Asersi tambahan di luar Expected TC (S-03): langkah 10 sampai 12 menjalankan Expected d TC-GS-TAG-302 dengan langkah buka menu yang tidak ada di TC; tidak ada asersi lain.
- Temuan untuk QA:
  - Q-9: langkah dan selektor FAMS, Supply Asset, dan halaman Combine & Separate tidak didefinisikan; langkah 24 dan 32 ditulis sebagai kemampuan "disediakan tim FE".
  - Q-1: TC-GS-TAG-303 berlabel `Manual Only — (b)` (pemindaian DD-11 lalu DD-13 di wizard Combine); kemampuan simulasi reader dicatat di Prerequisites (D-4).
  - TC-GS-TAG-301 Expected b menyebut entri `Retired` "dengan Previous Status" tanpa nilai; spec mengasersi kehadiran field (nilai Available mengikuti Seed Registri A dan tidak diasersi). Post Condition tidak ada.
  - TC-GS-TAG-302 Expected a menyebut DD-08 menjadi `Available` dan tampil di Tab Not Paired; Expected c menyebut kartu `22 of 50` (naik 1 dari `21 of 50`). Post Condition tidak ada.
  - TC-GS-TAG-303 Expected a menyebut "ikon 🔗 hilang pada kedua baris" dan Expected b "popup Combined TAG memuat pasangannya" tanpa memerinci isi popup; spec mengasersi pasangan tampil.
  - Q-4: identifier tetap; kartu `21 of 50` valid hanya bila Seed Registri A dipulihkan.
