---
id: TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian
title: "Sinkronisasi FAMS Replace TAG: Hasil Pemindaian Tag Lama, Pengganti To be Returned, Tag Reported, dan Tidak Pernah Retired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-299
  - TC-GS-TAG-300
  - TC-GS-TAG-368
  - TC-GS-TAG-376
coverage:
  web: automated
---

# Sinkronisasi FAMS Replace TAG: Hasil Pemindaian Tag Lama, Pengganti To be Returned, Tag Reported, dan Tidak Pernah Retired

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah status tag lewat aksi FAMS; tidak ada penghapusan data.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Pemicu (sesi API aktor, tidak diasersi): Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`: menandai tag Reported, menjalankan `Replace TAG` di FAMS Asset Detail dengan pemindaian tag lama dan/atau tag pengganti (simulasi reader; D-4). Pada TC-GS-TAG-368 akun FAMS adalah pemegang Update dengan Return Group DD-15 dalam scope Group user; kesesuaian akun perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Jendela SSE: langkah 3 menunggu jendela propagasi event tanpa memuat ulang halaman sebelum asersi "tetap Paired" dan "tetap di Tab Paired" (absence propagasi SSE); durasi mengikuti NC-54 (status Belum, disediakan tim FE); nilai sementara 5 detik dipakai sampai NC-54 dijawab.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`, NFC `3 of 30`). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (RFID Paired ke aset), DD-13 `04A224B2C15E83` (NFC; disetel Paired ke aset FAMS kedua lewat fixture BE dengan relasi combined ke DD-11 dilepas), DD-15 `E28011606000020F00000001` (pengganti; Available, atau To be Returned dengan Return Group `Gudang Pusat` pada TC-GS-TAG-368), DD-16 `E28011606000020F00000002` (pengganti Available), DD-08 `E2801160600002054D8A0008` (Retired, tetap dari seed). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum tiap TC.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Admin FAMS menandai tag Reported dan menjalankan `Replace TAG`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk Tag Reported dan Replace TAG (dengan pilihan memindai atau tidak memindai tag lama); penanda event selesai diproses (Eventual/SSE); pembacaan relasi aset sebuah tag; seed dan reset idempotent Seed Registri A dan keadaan DD-15 To be Returned.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-01, DD-13, DD-15, DD-16) dan aset FAMS lewat fixture BE; kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-300: Tag Reported tidak mengubah status Paired

1. Klik Tab Paired
2. Laporkan tag DD-01 rusak lewat menu TAG Reported di FAMS lewat sesi API Admin FAMS hingga tersimpan
3. Tunggu jendela propagasi event FAMS (durasi: NC-54, disediakan tim FE) tanpa memuat ulang halaman
4. Verifikasi status DD-01 tetap `Paired`
5. Verifikasi baris DD-01 tetap di Tab Paired

### TC-GS-TAG-299: Replace TAG, tag lama tidak dipindai

6. Klik Tab All
7. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
8. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
9. Ganti tag aset dari DD-01 di FAMS Asset Detail (`Replace TAG`) lewat sesi API Admin FAMS dengan memindai hanya tag baru DD-15 (DD-01 tidak dipindai), lalu Submit
10. Verifikasi status DD-01 `Damaged/Missing`
11. Verifikasi DD-01 tidak tertaut ke aset
12. Buka menu baris DD-01, lalu klik `TAG Log`
13. Verifikasi tepat satu entri baru `Unpaired` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
14. Verifikasi entri itu memuat baris `Status` `Paired` → `Damaged/Missing`
15. Verifikasi tidak ada entri `Marked Damaged/Missing` atau `Retired` terpisah
16. Tutup popup TAG Log
17. Verifikasi DD-15 berstatus `Paired`

### TC-GS-TAG-368: Replace TAG dengan pengganti To be Returned

18. Atur DD-01 menjadi Paired ke aset dan DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) lewat fixture BE, muat ulang halaman, lalu klik Tab All
19. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
20. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
21. Jalankan `Replace TAG` di FAMS Asset Detail aset bertag DD-01 lewat sesi API Admin FAMS: pindai tag lama DD-01, lalu pindai tag pengganti DD-15, dan Submit
22. Verifikasi status DD-01 `Available`
23. Verifikasi status DD-15 `Paired` tanpa muat ulang
24. Buka menu baris DD-01, lalu klik `TAG Log`
25. Verifikasi satu entri baru `Unpaired` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
26. Verifikasi entri itu memuat baris `Status` `Paired` → `Available`
27. Tutup popup TAG Log
28. Buka menu baris DD-15, lalu klik `TAG Log`
29. Verifikasi entri `TAG Paired by [pelaku user yang melakukan pair]` dengan `Previous Status: To be Returned`
30. Verifikasi tidak ada entri `TAG Received by ...`
31. Tutup popup TAG Log
32. Klik Tab Paired
33. Verifikasi baris DD-15 tampil di Tab Paired

### TC-GS-TAG-376: Replace TAG pada tag lama RFID dan NFC

34. Atur DD-01 Paired ke aset pertama, DD-13 Paired ke aset kedua (relasi combined dengan DD-11 dilepas), serta DD-15 dan DD-16 Available lewat fixture BE, muat ulang halaman, lalu klik Tab All
35. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
36. Buka menu baris DD-13, klik `TAG Log`, catat jumlah entri, lalu tutup popup
37. Jalankan `Replace TAG` di FAMS Asset Detail aset pertama lewat sesi API Admin FAMS: pindai hanya tag pengganti DD-15 (DD-01 tidak dipindai), lalu Submit
38. Jalankan `Replace TAG` di FAMS Asset Detail aset kedua lewat sesi API Admin FAMS: pindai tag lama DD-13, lalu tag pengganti DD-16, dan Submit
39. Verifikasi status DD-01 `Damaged/Missing` tanpa muat ulang
40. Verifikasi status DD-13 `Available`
41. Verifikasi DD-01 dan DD-13 tidak tertaut ke aset
42. Verifikasi DD-01 dan DD-13 tidak berstatus `Retired`
43. Pasang filter `Status` = `Retired`
44. Verifikasi DD-08 tampil pada hasil filter
45. Verifikasi hasil filter hanya memuat DD-08 (DD-01 dan DD-13 tidak tampil)
46. Hapus filter `Status`
47. Buka menu baris DD-01, lalu klik `TAG Log`
48. Verifikasi satu entri baru `TAG Unpaired by [pelaku user FAMS]` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
49. Verifikasi entri itu memuat baris `Status` `Paired` → `Damaged/Missing`
50. Verifikasi tidak ada entri `TAG Retired by ...` maupun `TAG Marked Damaged/Missing by ...`
51. Tutup popup TAG Log
52. Buka menu baris DD-13, lalu klik `TAG Log`
53. Verifikasi satu entri baru `TAG Unpaired by [pelaku user FAMS]` dengan Reason `Replaced by E28011606000020F00000002` (jumlah entri bertambah satu dari nilai yang dicatat)
54. Verifikasi entri itu memuat baris `Status` `Paired` → `Available`
55. Verifikasi tidak ada entri `TAG Retired by ...` maupun `TAG Marked Damaged/Missing by ...`
56. Tutup popup TAG Log
57. Verifikasi kartu RFID – Object TAG tetap `21 of 50`
58. Verifikasi kartu NFC tetap `3 of 30`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (58 langkah nominal). Alasan: empat TC satu topik (hasil `Replace TAG` di FAMS pada status tag lama dan pengganti) dengan satu dataset Seed Registri A dan satu kelas harness; pemicu FAMS lewat sesi API aktor dan tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di langkah 18 dan 34.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (299, 300, 368, 376) disusun ulang menjadi 300, 299, 368, 376; TC-GS-TAG-300 tidak mengubah status sehingga dijalankan lebih dulu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 6, dan 32 (pindah tab), 8, 20, 35, dan 36 (baseline jumlah entri TAG Log), 16, 27, 31, 51, dan 56 (menutup popup TAG Log), 18 dan 34 (memulihkan data lewat fixture BE), 43 dan 46 (memasang dan menghapus filter), 7 dan 19 (mengubah Rows per page menjadi 50 supaya DD-15 di halaman 2 Tab All tampil; ukuran halaman tidak diasumsikan terbawa antar tab atau muat ulang, dan dikembalikan ke 10 di hook `after`).
- Asersi tambahan di luar Expected TC (S-03): langkah 44 (DD-08 sebagai pembanding hasil filter Retired, bagian 8b butir 2).
- Temuan untuk QA:
  - Q-9: langkah dan selektor FAMS (TAG Reported, Replace TAG) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - TC-GS-TAG-299 Expected a1 menyatakan varian bersyarat (tag lama RFID/NFC dipindai menjadi `Available`; tag lama QR keluar dari registri), tetapi langkah TC hanya menjalankan Replace tanpa memindai tag lama; varian dipindai dicakup TC-GS-TAG-368 dan 376 (langkah 21 dan 38), varian QR tidak punya langkah di TC mana pun pada spec ini.
  - TC-GS-TAG-300 tidak menyebut cara mengamati "TAG Reported" selain Expected status; TC-GS-TAG-300 tidak punya Post Condition.
  - TC-GS-TAG-376 Post Condition butir a (DD-01 Damaged/Missing dan DD-13 Available di Tab Not Paired) dan butir b (DD-15 dan DD-16 `Paired`) tidak punya langkah observasi di TC dan tidak diasersi; butir a identik dengan Expected a kecuali penyebutan tab.
  - Q-15: `[pelaku user yang melakukan pair]` dan `[pelaku user FAMS]` pada TAG Log tidak diberi nilai dan format penulisan nama; TC-GS-TAG-299 dan 368 menulis entri `Unpaired` tanpa awalan `TAG ... by`, sedangkan TC-GS-TAG-376 menulis `TAG Unpaired by [pelaku user FAMS]`; spec mengikuti teks tiap TC.
  - Expected a TC-GS-TAG-368 dan 376 menyebut "tanpa singgah `Available`" (TC-GS-TAG-368) tanpa cara mengamati riwayat status; spec mengasersi status akhir dan tidak adanya entri `TAG Received by ...`.
  - Q-4: identifier tetap; kartu `21 of 50` dan `3 of 30` valid hanya bila Seed Registri A dipulihkan.
  - Post Condition TC-GS-TAG-299 dan 368 tidak ada.
  - NC-54 (status Belum): durasi jendela propagasi event pada langkah 3 (TC-GS-TAG-300) belum ditetapkan; nilai disediakan tim FE.
