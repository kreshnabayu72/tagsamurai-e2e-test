---
id: TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server
title: "Defense-in-Depth: Request Bulk Langsung ke Server dengan Status Tidak Sah, Hasil Campuran, dan oleh Read Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-228
  - TC-GS-HHR-229
  - TC-GS-HHR-466
  - TC-GS-HHR-474
coverage:
  web: automated
---

# Defense-in-Depth: Request Bulk Langsung ke Server dengan Status Tidak Sah, Hasil Campuran, dan oleh Read Only

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas a (defense-in-depth): request bulk dikirim langsung ke server lewat klien HTTP tanpa melalui UI; asersi hanya respons server dan state data (Badge `Status` di daftar dan jumlah entri tiga surface log).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini mengubah status reader Seed Reader A dan memulihkannya (lihat butir pemulihan).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman) atau pembacaan log (kembali ke halaman).
- Akun aktor:
  - Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; kredensial akun yang sama dipakai klien HTTP untuk TC-GS-HHR-474, 228, dan 466.
  - Read Only (Maya Putri) Client A `readOnly_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk TC-GS-HHR-229: login lewat langkah ganti akun eksplisit (langkah 43 sampai 45) dengan `Spectra.env.GS_RO_PASSWORD`; kredensial akun yang sama dipakai klien HTTP.
  - Hook `after` mengembalikan sesi ke akun Total Control default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SKU-HHR-01, Available), DD-03 (`Zebra Mobile Reader - 1`, Damaged), DD-05 (`Chainway C72 - 1`, Waiting for Approval), dan DD-07 (`Honeywell CK65 - 1`, Available). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya sebelum TC-GS-HHR-466 (DD-01 sudah Damaged oleh TC-GS-HHR-228) lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" yang disediakan tim FE/BE tanpa endpoint yang dikarang, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log: Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action). Baseline jumlah entri dicatat per surface sebelum request langsung pertama pada tiap TC yang mengasersi log.
- Kemampuan teknis: klien HTTP yang mengirim request bulk Mark as Damaged dan bulk Delete langsung ke server dengan kredensial akun aktor (endpoint sesuai kontrak API modul; tidak diulang di spec) dan membaca status serta isi respons per reader; pembacaan Badge `Status` dan tiga surface log; pemulihan Seed Reader A lewat fixture backend; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain status Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite); Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor (Total Control dan Read Only) dan hook `after` memulihkannya; lihat `suite.md`.

## Test Steps

### TC-GS-HHR-474: Request bulk seluruhnya dilewati dengan alasan campuran dijawab 409

1. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
2. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
3. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
4. Kirim langsung request bulk Mark as Damaged berisi DD-03 (Damaged) dan DD-05 (Waiting for Approval) lewat klien HTTP
5. Verifikasi respons server 409 Conflict (prioritas alasan 409 di atas 422)
6. Verifikasi tidak ada reader yang diproses
7. Buka Global Settings > Hardware > Handheld Reader
8. Verifikasi Badge `Status` DD-03 tetap `Damaged`
9. Verifikasi Badge `Status` DD-05 tetap `Waiting for Approval`
10. Buka ikon Changelog
11. Verifikasi jumlah entri Changelog sama dengan baseline langkah 1
12. Tutup Modal Changelog dengan `✕`
13. Buka Global Settings > User > Detail akun aktor > tab System Log
14. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 2
15. Buka Global Settings > Activity Log > tab User Action
16. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 3

### TC-GS-HHR-228: Request bulk memuat reader Waiting for Approval dan status tidak sah dilewati per reader

17. Buka Global Settings > Hardware > Handheld Reader
18. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
19. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
20. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
21. Kirim langsung request bulk Mark as Damaged berisi DD-01 (Available), DD-03 (Damaged), dan DD-05 (Waiting for Approval) lewat klien HTTP
22. Verifikasi hasil per reader pada respons: DD-01 diproses
23. Verifikasi hasil per reader pada respons: DD-03 dilewati dengan 409 Conflict (status sudah Damaged)
24. Verifikasi hasil per reader pada respons: DD-05 ditolak 422 dengan pesan `This device is waiting for approval and cannot be changed.`
25. Buka Global Settings > Hardware > Handheld Reader
26. Verifikasi Badge `Status` DD-01 menjadi `Damaged`
27. Verifikasi Badge `Status` DD-05 tetap `Waiting for Approval`
28. Buka ikon Changelog
29. Verifikasi jumlah entri Changelog bertambah tepat 1 dibanding baseline langkah 18, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
30. Tutup Modal Changelog dengan `✕`
31. Buka Global Settings > User > Detail akun aktor > tab System Log
32. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dibanding baseline langkah 19, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
33. Buka Global Settings > Activity Log > tab User Action
34. Verifikasi jumlah entri Activity Log bertambah tepat 1 dibanding baseline langkah 20, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`

### TC-GS-HHR-466: Request bulk campuran diproses dan dilewati dijawab 200 dengan hasil per reader

35. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
36. Kirim langsung request bulk Mark as Damaged berisi DD-01 (Available) dan DD-03 (Damaged) lewat klien HTTP
37. Verifikasi respons server 200 OK
38. Verifikasi hasil per reader pada respons: DD-01 diproses
39. Verifikasi hasil per reader pada respons: DD-03 dilewati dengan alasan 409 Conflict
40. Buka Global Settings > Hardware > Handheld Reader
41. Verifikasi Badge `Status` DD-01 menjadi `Damaged`
42. Verifikasi Badge `Status` DD-03 tetap `Damaged`

### Ganti akun ke Read Only

43. Ganti akun: logout dari akun Total Control
44. Login sebagai Read Only (Maya Putri) Client A dengan `Spectra.env.GS_RO_PASSWORD`
45. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-229: Request bulk oleh Read Only ditolak server

46. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
47. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
48. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
49. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
50. Kirim langsung request bulk Delete berisi DD-01 dan DD-07 lewat klien HTTP dengan kredensial akun Read Only
51. Verifikasi server menolak request
52. Buka Global Settings > Hardware > Handheld Reader
53. Verifikasi baris DD-01 dan DD-07 tetap ada di tabel
54. Buka ikon Changelog
55. Verifikasi jumlah entri Changelog sama dengan baseline langkah 47
56. Tutup Modal Changelog dengan `✕`
57. Buka Global Settings > User > Detail akun aktor > tab System Log
58. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 48
59. Buka Global Settings > Activity Log > tab User Action
60. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 49

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k). Kelas a (defense-in-depth) satu spec per kelas per modul; TC-GS-HHR-466 dan 474 tetap sebagai spec FE+BE (keputusan P-4).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 474 (ditolak, tidak mengubah data), 228 (mengubah DD-01), 466 (memulihkan lalu mengubah DD-01), lalu ganti akun ke Read Only dan 229 paling akhir. Menyimpang dari urutan nomor TC sumber (228, 229, 466, 474). TC-GS-HHR-229 diletakkan sesudah ganti akun eksplisit (langkah 43 sampai 45) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (konvensi bagian 3, kasus b). Bila server ternyata memproses Delete oleh Read Only, TC-GS-HHR-229 berada di akhir spec sehingga kegagalannya tidak mengubah data yang dipakai TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3, 18 sampai 20, dan 47 sampai 49 (baseline jumlah entri sebelum request langsung pertama; S-12), langkah 7, 17, 25, 40, 45, dan 52 (membuka atau kembali ke halaman Handheld Reader), langkah 10, 13, 15, 28, 31, 33, 54, 57, dan 59 (membuka surface log untuk dibaca), langkah 12, 30, dan 56 (menutup Modal Changelog), langkah 35 dan 46 (pemulihan dan muat ulang), dan ganti akun 43 sampai 44.
- Request langsung ke server (8b butir 1): hanya respons server dan state data yang diasersi. Perilaku UI untuk respons yang sama tidak diasersi di spec ini (lihat Temuan untuk QA).
- Asersi jumlah entri memakai selisih terhadap baseline; pada TC-GS-HHR-228 selisih tepat 1 tiap surface membuktikan tidak ada entri untuk DD-03 dan DD-05. Asersi sama-dengan-baseline pada TC-GS-HHR-474 dan 229 adalah asersi jumlah (bukan kelas g) dan memakai baseline dari langkah sebelum request.
- Spec memuat 60 langkah (di atas sekitar 35 langkah). Alasan: seluruh blok satu kelas (request bulk langsung ke server), tiap blok mengasersi respons dan state data sendiri, dan blok baca-log (tiga surface) adalah blok baca-log berpola yang diulang per TC.
- Temuan untuk QA:
  - TC-GS-HHR-229 Expected a menulis "UI menampilkan toast error: `You don't have permission to do this.`" untuk request yang dikirim langsung tanpa melalui UI; perilaku FE atas request langsung tidak disalin ke spec ini (8b butir 1). Perilaku FE untuk penolakan izin dicakup spec Role Matrix dan defense-in-depth izin (spec 008 sampai 012 menurut plan).
  - TC-GS-HHR-229 Expected a menyebut "Server menolak" tanpa kode status; spec mengasersi penolakan tanpa kode.
  - TC-GS-HHR-228 Expected tidak menyebut kode status keseluruhan respons dan tidak menyebut apakah DD-01 diproses meski ada reader lain yang ditolak; spec mengasersi hasil per reader (DD-01 diproses, DD-03 409, DD-05 422) dan state akhir.
  - TC-GS-HHR-228 Expected b ("DD-03 ... tanpa entri") dan c ("DD-05 ... tanpa entri") diasersi sebagai selisih tepat 1 per surface (hanya DD-01), bukan sebagai asersi absence kelas g.
  - TC-GS-HHR-466 Expected a menyebut respons 200 OK "memuat hasil per reader" tanpa bentuk payload; spec mengasersi hasil per reader tanpa mengasersi struktur payload.
  - TC-GS-HHR-474 Expected a ("tidak ada reader yang diproses") tidak punya cara observasi selain state akhir; spec mengasersi respons 409 dan Badge `Status` tetap.
  - TC-GS-HHR-229 membaca tiga surface log sebagai akun Read Only; TC tidak menyebut apakah Read Only dapat membuka Changelog, System Log akun sendiri, dan Activity Log. Bila tidak, pembacaan state dilakukan lewat fixture BE yang disediakan tim FE/BE.
  - TC-GS-HHR-228, 229, 466, dan 474 tidak mencantumkan Post Condition.
  - Seed Reader A tidak diberi suffix per run (nama literal) dan mekanisme pemulihannya hanya disebut "fixture backend" di Catatan TC; pengecualian Population S-12 untuk HHR belum ada di konvensi.
