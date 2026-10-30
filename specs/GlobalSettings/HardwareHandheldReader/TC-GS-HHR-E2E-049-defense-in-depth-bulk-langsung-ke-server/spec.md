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
  - Read Only (Maya Putri) Client A `readOnly_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk TC-GS-HHR-229: login lewat langkah ganti akun eksplisit (langkah 33 sampai 35) dengan `Spectra.env.GS_RO_PASSWORD`; kredensial akun yang sama dipakai klien HTTP.
  - Hook `after` mengembalikan sesi ke akun Total Control default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SKU-HHR-01, Available), DD-03 (`Zebra Mobile Reader - 1`, Damaged), DD-05 (`Chainway C72 - 1`, Waiting for Approval), dan DD-07 (`Honeywell CK65 - 1`, Available). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR).
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya sebelum TC-GS-HHR-466 (DD-01 sudah Damaged oleh TC-GS-HHR-228) lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" yang disediakan tim FE/BE tanpa endpoint yang dikarang, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log: Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action). Baseline jumlah entri dicatat per surface sebelum request langsung pada TC-GS-HHR-228 (TC-GS-HHR-229 dan TC-GS-HHR-474 tidak membaca log di spec ini; jumlah entri log atas keduanya diasersi di spec `TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak`).
- Kemampuan teknis: klien HTTP yang mengirim request bulk Mark as Damaged dan bulk Delete langsung ke server dengan kredensial akun aktor (endpoint sesuai kontrak API modul; tidak diulang di spec) dan membaca status serta isi respons per reader; pembacaan Badge `Status` dan tiga surface log; pemulihan Seed Reader A lewat fixture backend; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain status Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite); Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor (Total Control dan Read Only) dan hook `after` memulihkannya; lihat `suite.md`.

## Test Steps

### TC-GS-HHR-474: Request bulk seluruhnya dilewati dengan alasan campuran dijawab 409

1. Kirim langsung request bulk Mark as Damaged berisi DD-03 (Damaged) dan DD-05 (Waiting for Approval) lewat klien HTTP
2. Verifikasi respons server 409 Conflict (prioritas alasan 409 di atas 422)
3. Verifikasi tidak ada reader yang diproses
4. Buka Global Settings > Hardware > Handheld Reader
5. Verifikasi Badge `Status` DD-03 tetap `Damaged`
6. Verifikasi Badge `Status` DD-05 tetap `Waiting for Approval`

### TC-GS-HHR-228: Request bulk memuat reader Waiting for Approval dan status tidak sah dilewati per reader

7. Buka Global Settings > Hardware > Handheld Reader
8. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
9. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
10. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
11. Kirim langsung request bulk Mark as Damaged berisi DD-01 (Available), DD-03 (Damaged), dan DD-05 (Waiting for Approval) lewat klien HTTP
12. Verifikasi hasil per reader pada respons: DD-01 diproses
13. Verifikasi hasil per reader pada respons: DD-03 dilewati dengan 409 Conflict (status sudah Damaged)
14. Verifikasi hasil per reader pada respons: DD-05 ditolak 422 dengan pesan `This device is waiting for approval and cannot be changed.`
15. Buka Global Settings > Hardware > Handheld Reader
16. Verifikasi Badge `Status` DD-01 menjadi `Damaged`
17. Verifikasi Badge `Status` DD-05 tetap `Waiting for Approval`
18. Buka ikon Changelog
19. Verifikasi jumlah entri Changelog bertambah tepat 1 dibanding baseline langkah 8, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
20. Tutup Modal Changelog dengan `✕`
21. Buka Global Settings > User > Detail akun aktor > tab System Log
22. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dibanding baseline langkah 9, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
23. Buka Global Settings > Activity Log > tab User Action
24. Verifikasi jumlah entri Activity Log bertambah tepat 1 dibanding baseline langkah 10, yaitu untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`

### TC-GS-HHR-466: Request bulk campuran diproses dan dilewati dijawab 200 dengan hasil per reader

25. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
26. Kirim langsung request bulk Mark as Damaged berisi DD-01 (Available) dan DD-03 (Damaged) lewat klien HTTP
27. Verifikasi respons server 200 OK
28. Verifikasi hasil per reader pada respons: DD-01 diproses
29. Verifikasi hasil per reader pada respons: DD-03 dilewati dengan alasan 409 Conflict
30. Buka Global Settings > Hardware > Handheld Reader
31. Verifikasi Badge `Status` DD-01 menjadi `Damaged`
32. Verifikasi Badge `Status` DD-03 tetap `Damaged`

### Ganti akun ke Read Only

33. Ganti akun: logout dari akun Total Control
34. Login sebagai Read Only (Maya Putri) Client A dengan `Spectra.env.GS_RO_PASSWORD`
35. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-229: Request bulk oleh Read Only ditolak server

36. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
37. Kirim langsung request bulk Delete berisi DD-01 dan DD-07 lewat klien HTTP dengan kredensial akun Read Only
38. Verifikasi respons server 403 Forbidden
39. Buka Global Settings > Hardware > Handheld Reader
40. Verifikasi reader DD-01 dan DD-07 tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k). Kelas a (defense-in-depth) satu spec per kelas per modul; `K-1`: TC kelas a yang Expected-nya respons API (status respons dan state data) tumpang tindih dengan `tc-hardware-handheld-reader-backend.md`; TC-GS-HHR-466 dan 474 tetap di spec FE+BE ini karena tiap TC granular tepat satu spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix reader Pre-setup DD-01, DD-03, DD-05, dan DD-07 Client A karena asersi bergantung pada nama dan status persis; pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok (langkah 25 dan 36), dinyatakan di `suite.md` dan Prerequisites; suite serial.
- Urutan TC di spec: 474 (ditolak, tidak mengubah data), 228 (mengubah DD-01), 466 (memulihkan lalu mengubah DD-01), lalu ganti akun ke Read Only dan 229 paling akhir. Menyimpang dari urutan nomor TC sumber (228, 229, 466, 474). TC-GS-HHR-229 diletakkan sesudah ganti akun eksplisit (langkah 33 sampai 35) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (konvensi bagian 3, kasus b). Bila server ternyata memproses Delete oleh Read Only, TC-GS-HHR-229 berada di akhir spec sehingga kegagalannya tidak mengubah data yang dipakai TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 sampai 10 (baseline jumlah entri sebelum request langsung; S-12), langkah 4, 7, 15, 30, 35, dan 39 (membuka atau kembali ke halaman Handheld Reader), langkah 18, 21, dan 23 (membuka surface log untuk dibaca), langkah 20 (menutup Modal Changelog), langkah 25 dan 36 (pemulihan dan muat ulang), dan ganti akun 33 sampai 34.
- Request langsung ke server (8b butir 1): hanya respons server dan state data yang diasersi. Perilaku UI untuk respons yang sama tidak diasersi di spec ini (lihat Temuan untuk QA).
- Asersi jumlah entri memakai selisih terhadap baseline; pada TC-GS-HHR-228 selisih tepat 1 tiap surface membuktikan tidak ada entri untuk DD-03 dan DD-05.
- Pembagian TC lintas spec (S-05): TC-GS-HHR-474 dan TC-GS-HHR-229 juga ada di spec `TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak`, yang mengasersi jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log tidak bertambah dengan baseline, sesi, dan request langsung sendiri (rujukan sebaliknya ada di Notes spec 079). Spec ini hanya mengasersi respons server (409 untuk TC-GS-HHR-474, 403 untuk TC-GS-HHR-229) dan state data (Badge `Status` tetap, reader tetap ada) (8b butir 1).
- Spec memuat 40 langkah (di atas sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (request bulk langsung ke server lewat klien HTTP), tiap blok mengasersi respons dan state data sendiri, dan Seed Reader A dipulihkan fixture backend sebelum blok yang mengubahnya (langkah 25 dan 36), sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-HHR-228 Expected tidak menyebut kode status keseluruhan respons dan tidak menyebut apakah DD-01 diproses meski ada reader lain yang ditolak; spec mengasersi hasil per reader (DD-01 diproses, DD-03 409, DD-05 422) dan state akhir.
  - TC-GS-HHR-228 Expected b ("DD-03 ... tanpa entri") dan c ("DD-05 ... tanpa entri") diasersi sebagai selisih tepat 1 per surface (hanya DD-01), bukan sebagai asersi absence kelas g.
  - TC-GS-HHR-466 Expected a menyebut respons 200 OK "memuat hasil per reader" tanpa bentuk payload; spec mengasersi hasil per reader tanpa mengasersi struktur payload.
  - TC-GS-HHR-474 Expected a ("tidak ada reader yang diproses") tidak punya cara observasi selain state akhir; spec mengasersi respons 409 dan Badge `Status` tetap.
  - TC-GS-HHR-228, 229, 466, dan 474 tidak mencantumkan Post Condition.
  - TC-GS-HHR-229 Expected b memuat dua klausa yang diasersi di dua spec: kedua reader tetap ada (spec ini, langkah 40) dan jumlah entri tiga surface log tidak bertambah (spec 079, S-05).
