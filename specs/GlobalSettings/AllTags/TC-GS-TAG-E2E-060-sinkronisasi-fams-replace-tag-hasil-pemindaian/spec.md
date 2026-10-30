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
- Pemicu (P-2, sesi API, tidak diasersi): Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`: menandai tag Reported, menjalankan `Replace TAG` di FAMS Asset Detail dengan pemindaian tag lama dan/atau tag pengganti (simulasi reader; D-4). Pada TC-GS-TAG-368 akun FAMS adalah pemegang Update dengan Return Group DD-15 dalam scope Group user; kesesuaian akun perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`, NFC `3 of 30`). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (RFID Paired ke aset), DD-13 `04A224B2C15E83` (NFC; disetel Paired ke aset FAMS kedua lewat fixture BE dengan relasi combined ke DD-11 dilepas), DD-15 `E28011606000020F00000001` (pengganti; Available, atau To be Returned dengan Return Group `Gudang Pusat` pada TC-GS-TAG-368), DD-16 `E28011606000020F00000002` (pengganti Available), DD-08 `E2801160600002054D8A0008` (Retired, tetap dari seed). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum tiap TC.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk Tag Reported dan Replace TAG (dengan pilihan memindai atau tidak memindai tag lama); penanda event selesai diproses (Eventual/SSE); pembacaan relasi aset sebuah tag; seed dan reset idempotent Seed Registri A dan keadaan DD-15 To be Returned.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-01, DD-13, DD-15, DD-16) dan aset FAMS lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-300: Tag Reported tidak mengubah status Paired

1. Klik Tab Paired
2. Laporkan tag DD-01 rusak lewat menu TAG Reported di FAMS lewat sesi API Admin FAMS hingga tersimpan
3. Verifikasi status DD-01 tetap `Paired`
4. Verifikasi baris DD-01 tetap di Tab Paired

### TC-GS-TAG-299: Replace TAG, tag lama tidak dipindai

5. Klik Tab All
6. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
7. Ganti tag aset dari DD-01 di FAMS Asset Detail (`Replace TAG`) lewat sesi API Admin FAMS dengan memindai hanya tag baru DD-15 (DD-01 tidak dipindai), lalu Submit
8. Verifikasi status DD-01 `Damaged/Missing`
9. Verifikasi DD-01 tidak tertaut ke aset
10. Buka menu baris DD-01, lalu klik `TAG Log`
11. Verifikasi tepat satu entri baru `Unpaired` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
12. Verifikasi entri itu memuat baris `Status` `Paired` → `Damaged/Missing`
13. Verifikasi tidak ada entri `Marked Damaged/Missing` atau `Retired` terpisah
14. Tutup popup TAG Log
15. Verifikasi DD-15 berstatus `Paired`

### TC-GS-TAG-368: Replace TAG dengan pengganti To be Returned

16. Atur DD-01 menjadi Paired ke aset dan DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) lewat fixture BE, muat ulang halaman, lalu klik Tab All
17. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
18. Jalankan `Replace TAG` di FAMS Asset Detail aset bertag DD-01 lewat sesi API Admin FAMS: pindai tag lama DD-01, lalu pindai tag pengganti DD-15, dan Submit
19. Verifikasi status DD-01 `Available`
20. Verifikasi status DD-15 `Paired` tanpa muat ulang
21. Buka menu baris DD-01, lalu klik `TAG Log`
22. Verifikasi satu entri baru `Unpaired` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
23. Verifikasi entri itu memuat baris `Status` `Paired` → `Available`
24. Tutup popup TAG Log
25. Buka menu baris DD-15, lalu klik `TAG Log`
26. Verifikasi entri `TAG Paired by [pelaku user yang melakukan pair]` dengan `Previous Status: To be Returned`
27. Verifikasi tidak ada entri `TAG Received by ...`
28. Tutup popup TAG Log
29. Klik Tab Paired
30. Verifikasi baris DD-15 tampil di Tab Paired

### TC-GS-TAG-376: Replace TAG pada tag lama RFID dan NFC

31. Atur DD-01 Paired ke aset pertama, DD-13 Paired ke aset kedua (relasi combined dengan DD-11 dilepas), serta DD-15 dan DD-16 Available lewat fixture BE, muat ulang halaman, lalu klik Tab All
32. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
33. Buka menu baris DD-13, klik `TAG Log`, catat jumlah entri, lalu tutup popup
34. Jalankan `Replace TAG` di FAMS Asset Detail aset pertama lewat sesi API Admin FAMS: pindai hanya tag pengganti DD-15 (DD-01 tidak dipindai), lalu Submit
35. Jalankan `Replace TAG` di FAMS Asset Detail aset kedua lewat sesi API Admin FAMS: pindai tag lama DD-13, lalu tag pengganti DD-16, dan Submit
36. Verifikasi status DD-01 `Damaged/Missing` tanpa muat ulang
37. Verifikasi status DD-13 `Available`
38. Verifikasi DD-01 dan DD-13 tidak tertaut ke aset
39. Verifikasi DD-01 dan DD-13 tidak berstatus `Retired`
40. Pasang filter `Status` = `Retired`
41. Verifikasi DD-08 tampil pada hasil filter
42. Verifikasi hasil filter hanya memuat DD-08 (DD-01 dan DD-13 tidak tampil)
43. Hapus filter `Status`
44. Buka menu baris DD-01, lalu klik `TAG Log`
45. Verifikasi satu entri baru `TAG Unpaired by [pelaku user FAMS]` dengan Reason `Replaced by E28011606000020F00000001` (jumlah entri bertambah satu dari nilai yang dicatat)
46. Verifikasi entri itu memuat baris `Status` `Paired` → `Damaged/Missing`
47. Verifikasi tidak ada entri `TAG Retired by ...` maupun `TAG Marked Damaged/Missing by ...`
48. Tutup popup TAG Log
49. Buka menu baris DD-13, lalu klik `TAG Log`
50. Verifikasi satu entri baru `TAG Unpaired by [pelaku user FAMS]` dengan Reason `Replaced by E28011606000020F00000002` (jumlah entri bertambah satu dari nilai yang dicatat)
51. Verifikasi entri itu memuat baris `Status` `Paired` → `Available`
52. Verifikasi tidak ada entri `TAG Retired by ...` maupun `TAG Marked Damaged/Missing by ...`
53. Tutup popup TAG Log
54. Verifikasi kartu RFID – Object TAG tetap `21 of 50`
55. Verifikasi kartu NFC tetap `3 of 30`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (55 langkah nominal). Alasan: empat TC satu topik (hasil `Replace TAG` di FAMS pada status tag lama dan pengganti) dengan satu dataset Seed Registri A dan satu kelas harness; pemicu FAMS lewat sesi API (P-2) dan tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di langkah 16 dan 31.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (299, 300, 368, 376) disusun ulang menjadi 300, 299, 368, 376; TC-GS-TAG-300 tidak mengubah status sehingga dijalankan lebih dulu.
- Pengecualian P-2: tandai Reported dan `Replace TAG` oleh Admin FAMS hanyalah pemicu state lewat sesi API; objek asersi adalah status, baris, kartu, dan TAG Log di registri Global Settings.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 5, 29 (pindah tab), 6, 17, 32, dan 33 (baseline jumlah entri TAG Log), 14, 24, 28, 48, dan 53 (menutup popup TAG Log), 16 dan 31 (memulihkan data lewat fixture BE), 40 dan 43 (memasang dan menghapus filter).
- Asersi tambahan di luar Expected TC (S-03): langkah 41 (DD-08 sebagai pembanding hasil filter Retired, bagian 8b butir 2).
- Temuan untuk QA:
  - Q-9: langkah dan selektor FAMS (TAG Reported, Replace TAG) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - TC-GS-TAG-299 Expected a1 menyatakan varian bersyarat (tag lama RFID/NFC dipindai menjadi `Available`; tag lama QR keluar dari registri), tetapi langkah TC hanya menjalankan Replace tanpa memindai tag lama; varian dipindai dicakup TC-GS-TAG-368 dan 376 (langkah 18 dan 35), varian QR tidak punya langkah di TC mana pun pada spec ini.
  - TC-GS-TAG-300 tidak menyebut cara mengamati "TAG Reported" selain Expected status; TC-GS-TAG-300 tidak punya Post Condition.
  - TC-GS-TAG-376 Post Condition butir a (DD-01 Damaged/Missing dan DD-13 Available di Tab Not Paired) dan butir b (DD-15 dan DD-16 `Paired`) tidak punya langkah observasi di TC dan tidak diasersi; butir a identik dengan Expected a kecuali penyebutan tab.
  - Q-15: `[pelaku user yang melakukan pair]` dan `[pelaku user FAMS]` pada TAG Log tidak diberi nilai dan format penulisan nama; TC-GS-TAG-299 dan 368 menulis entri `Unpaired` tanpa awalan `TAG ... by`, sedangkan TC-GS-TAG-376 menulis `TAG Unpaired by [pelaku user FAMS]`; spec mengikuti teks tiap TC.
  - Expected a TC-GS-TAG-368 dan 376 menyebut "tanpa singgah `Available`" (TC-GS-TAG-368) tanpa cara mengamati riwayat status; spec mengasersi status akhir dan tidak adanya entri `TAG Received by ...`.
  - Q-4: identifier tetap; kartu `21 of 50` dan `3 of 30` valid hanya bila Seed Registri A dipulihkan.
  - Post Condition TC-GS-TAG-299 dan 368 tidak ada.
