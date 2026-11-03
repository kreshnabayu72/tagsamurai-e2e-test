---
id: TC-GS-HHR-E2E-025-activate-saving-state-dan-klik-ganda-submit
title: "Activate Reader: Saving State Tombol Submit dan Klik Ganda Cepat pada Submit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-95
  - TC-GS-HHR-98
coverage:
  web: automated
---

# Activate Reader: Saving State Tombol Submit dan Klik Ganda Cepat pada Submit

## Prerequisites

- Mode: FE+BE. Backend nyata dengan fixture backend; reader hasil aktivasi dipulihkan oleh spec sendiri dan hook `after`.
- Suite serial (`parallel: false`). State global yang diubah spec ini: dua aktivasi sukses unit `SN-HHR-00201` menjadi reader `Zebra RFID Reader - 2` (langkah 6 dan 26) dan kartu `Long Range` menjadi `6 of 6`. Reader dari TC-GS-HHR-95 dihapus oleh spec lewat `Delete` agar kuota `Long Range` pulih (NC-06: Delete reader Jalur A mengembalikan unit ke `Available` di Hardware Stock). Hook `after` melepas penundaan respons yang tersisa, menghapus reader sisa, dan memulihkan Seed Reader A lewat fixture backend.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, `Long Range` terpakai 5 dari 6. HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal. Fixture baru `Fixture.hardwareHandheldReader.savingState025`.
- Data Dinamis: nama baris hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit HS-01 (HHR-LOGIC-02g) dan dipakai apa adanya karena Expected TC menyebutnya.
- Kemampuan teknis: simulator reader USB (sambung reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); `Spectra.intercept()` untuk menahan respons request aktivasi (`POST /v2/hardware-tagging/handheld-readers`, kontrak `global-settings/hardware-handheld-reader/API/openapi.yaml`) lalu melepasnya (penahanan hanya untuk mengamati state, bukan kegagalan yang dipaksa); klik ganda cepat pada `[Submit]`; membaca jumlah toast yang tampil.

## Test Steps

### TC-GS-HHR-95: Tombol Submit masuk saving state dan kontrol dibekukan selama request

1. Pasang penundaan respons pada request aktivasi (respons ditahan hingga dilepas)
2. Klik `[+ Activate Reader]`
3. Klik `Long Range` pada Overlay `Select Range Type`
4. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
5. Klik `[Sync]`
6. Klik `[Submit]`
7. Verifikasi `[Submit]` menampilkan spinner
8. Verifikasi `[Submit]` disabled
9. Verifikasi `[Clear Field]` disabled
10. Verifikasi `[Sync]` disabled
11. Verifikasi `[✕]` disabled
12. Verifikasi input `Alias Name` dinonaktifkan
13. Verifikasi slider `Reader Power` dinonaktifkan
14. Lepas penundaan respons pada request aktivasi
15. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
16. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
17. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
18. Klik `[Delete]` pada dialog
19. Tunggu aksi selesai
20. Klik `(←)` pada kotak Search

### TC-GS-HHR-98: Klik ganda cepat pada Submit hanya membuat satu reader

21. Tunggu toast lama hilang otomatis
22. Klik `[+ Activate Reader]`
23. Klik `Long Range` pada Overlay `Select Range Type`
24. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
25. Klik `[Sync]`
26. Klik ganda cepat `[Submit]`
27. Verifikasi hanya satu toast sukses tampil
28. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
29. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
30. Verifikasi kartu `Long Range` menjadi `6 of 6`
31. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec singkat (31 langkah), di bawah ambang sekitar 35 langkah. Popup Activate dibuka 2 kali dan ditutup 2 kali (keduanya lewat Submit sukses).
- Urutan TC-GS-HHR-95 dulu lalu 98 mengikuti nomor TC. TC-GS-HHR-95 menahan respons hanya untuk mengamati state UI (kelas fungsional, bukan kelas b); setelah penahanan dilepas, Submit berhasil dan membuat reader `Zebra RFID Reader - 2`. Reader itu dihapus lewat `Delete` (langkah penghubung, tanpa `Verifikasi`) agar TC-GS-HHR-98 memulai dari kuota `Long Range` `5 of 6` dan serial `SN-HHR-00201` kembali tersedia di stok; TC-GS-HHR-98 membuat reader itu lagi. Reader dari TC-GS-HHR-98 dipulihkan oleh hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan penundaan respons, "Tunggu aksi selesai" (langkah 15; hasil Submit TC-GS-HHR-95 tidak diasersi sebelum Search), penyambungan reader di simulator USB, `[Sync]`, Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search, `Delete` reader hasil TC-GS-HHR-95 diikuti "Tunggu aksi selesai" (langkah 19; aktivasi TC-GS-HHR-98 bergantung pada kuota dan stok yang pulih, bagian 8b butir 8), serta "Tunggu toast lama hilang otomatis" sebelum penghitungan toast pada TC-GS-HHR-98 (toast sukses dari aktivasi dan Delete sebelumnya harus hilang agar hitungan "hanya satu toast" tidak terpengaruh).
- Verifikasi toast pada TC-GS-HHR-98 diletakkan segera sesudah klik ganda karena toast sukses hilang otomatis setelah 4 detik (`foundation/functions/toast-copy.md`).
- Pembagian TC lintas spec: TC-GS-HHR-96 dan 97 (kegagalan 5xx dan timeout saat Submit) ada di spec 026; TC-GS-HHR-99 sampai 101 dan 446 sampai 447 ada di spec 024.
- Temuan untuk QA:
  - Kedua TC berlabel `Manual Only` (b) di TC sumber (reader USB fisik) tetapi tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - Expected TC-GS-HHR-95 b menyebut "input dinonaktifkan" tanpa daftar; spec mengasersi `Alias Name` dan slider `Reader Power` (field input pada popup setelah Sync).
  - TC-GS-HHR-95 langkah 1 menyebut "Aktifkan penundaan respons" tanpa menyebut cara dan kapan dilepas; spec menahan respons lalu melepasnya setelah state diamati. Hasil aktivasi sesudah dilepas tidak ada di Expected TC dan tidak diasersi.
  - Pemulihan antar-TC (`Delete` reader) bergantung pada asumsi bahwa Delete reader Jalur A mengembalikan unit ke `Available` (NC-06) dan nama bawaan aktivasi ulang tetap `Zebra RFID Reader - 2` (nomor urut unit HS-01). TC tidak menyatakan ini; bila nama berbeda, Expected TC-GS-HHR-98 a (nama `Zebra RFID Reader - 2`) perlu disesuaikan.
  - Expected TC-GS-HHR-98 a menyatakan kuota `6 of 6`; nilai ini hanya benar bila kuota `Long Range` awal `5 of 6` pulih sebelum TC (sebagaimana fixture backend yang dipulihkan antar TC pada Catatan TC).
