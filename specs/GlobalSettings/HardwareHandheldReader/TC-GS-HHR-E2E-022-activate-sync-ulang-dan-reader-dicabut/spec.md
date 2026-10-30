---
id: TC-GS-HHR-E2E-022-activate-sync-ulang-dan-reader-dicabut
title: "Activate Reader: Sync Ulang dengan Reader yang Sama atau Berbeda dan Reader Dicabut setelah Sync"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-82
  - TC-GS-HHR-83
  - TC-GS-HHR-84
coverage:
  web: automated
---

# Activate Reader: Sync Ulang dengan Reader yang Sama atau Berbeda dan Reader Dicabut setelah Sync

## Prerequisites

- Mode: FE+BE. Backend nyata dengan fixture backend; reader hasil aktivasi di akhir spec dipulihkan oleh hook `after`.
- Suite serial (`parallel: false`). State global yang diubah spec ini: satu reader baru `Zebra RFID Reader - 2` (unit `SN-HHR-00201`) pada langkah 26, dan kartu `Long Range` menjadi `6 of 6`. Hook `after` memulihkannya (hapus reader `Zebra RFID Reader - 2` hasil aktivasi dan pulihkan Seed Reader A lewat fixture backend).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, `Long Range` terpakai 5 dari 6, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. Katalog Device Name DN-01 sampai DN-07 (Admin Console, dibaca read-only oleh Client A). HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal; `SN-HHR-00302` di luar stok. Fixture baru `Fixture.hardwareHandheldReader.syncUlang022`.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-022` (TC-GS-HHR-82 dan TC-GS-HHR-83, hanya diisi dan tidak disimpan); tidak ada data bernama lain yang dibuat spec; nama baris hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit HS-01 (HHR-LOGIC-02g) dan dipakai apa adanya karena Expected TC menyebutnya.
- Kemampuan teknis: simulator reader USB (sambung dan cabut reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); pemulihan fixture backend Seed Reader A.

## Test Steps

### TC-GS-HHR-82: Sync ulang dengan reader yang sama mempertahankan input yang sudah diisi

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` lewat simulator USB
4. Klik `[Sync]`
5. Pilih `Chainway C72` pada `Device Name`
6. Isi `Brand` dengan `Chainway`
7. Isi `Model/Type` dengan `C72`
8. Isi `Alias Name` dengan `Reader Dock 01-{runId}-022`
9. Klik `[Sync]` lagi pada reader yang sama
10. Verifikasi `Device Name` tetap `Chainway C72`
11. Verifikasi `Brand` tetap `Chainway`
12. Verifikasi `Model/Type` tetap `C72`
13. Verifikasi `Alias Name` tetap `Reader Dock 01-{runId}-022`
14. Verifikasi `Serial Number` tetap `SN-HHR-00302`
15. Verifikasi `[Sync]` tetap aktif

### TC-GS-HHR-83: Sync ulang dengan reader berbeda mereset input dan menghitung ulang jalur

16. Cabut reader `SN-HHR-00302`, lalu sambungkan reader USB dengan Serial Number `SN-HHR-00201` (stok Principal) lewat simulator USB
17. Klik `[Sync]`
18. Verifikasi `Serial Number` berganti `SN-HHR-00201`
19. Verifikasi label `Official` tampil
20. Verifikasi `Alias Name` kosong
21. Verifikasi pemilih `Device Name` dan `SKU` Jalur B tidak tampil (isian `Chainway C72` tidak ada)
22. Verifikasi `Brand` terisi `Zebra` dan `Model/Type` terisi `RFD40` dari stok (bukan `Chainway` dan `C72`)
23. Verifikasi `Brand` dan `Model/Type` terkunci
24. Verifikasi slider `Reader Power` terisi `22 dBm`

### TC-GS-HHR-84: Reader dicabut setelah Sync berhasil tidak membatalkan hasil

25. Cabut kabel USB reader `SN-HHR-00201` lewat simulator USB
26. Klik `[Submit]`
27. Tunggu aksi selesai (Popup Activate tertutup)
28. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
29. Verifikasi baris `Zebra RFID Reader - 2` dengan `Status` `Available`
30. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Satu Popup Activate dipakai berurutan untuk TC-GS-HHR-82, 83, dan 84: popup yang sudah berisi hasil Sync reader `SN-HHR-00302` dari TC-GS-HHR-82 diteruskan ke TC-GS-HHR-83 (mengganti reader dan `[Sync]`), lalu ke TC-GS-HHR-84 (mencabut reader dan `[Submit]`). State pada awal TC-GS-HHR-83 dan 84 sama dengan yang dibangun precondition TC masing-masing. Jumlah buka form 1 dan jumlah kejadian menutup form 1 (popup ditutup oleh submit sukses di langkah 26); aksi yang menciptakan data (Submit) ditaruh paling akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): penyambungan dan pencabutan reader di simulator USB, pengisian field di langkah 5 sampai 8 (state pembentuk TC-GS-HHR-82), langkah 27 (Tunggu aksi selesai: hasil Submit tidak diasersi sebelum Search), Search untuk menemukan baris `Zebra RFID Reader - 2` dan `(←)` untuk mengosongkan Search (S-09).
- Spec singkat (30 langkah), di bawah ambang sekitar 35 langkah.
- Pembagian TC lintas spec: TC-GS-HHR-75 dan 76 (Sync pada Jalur B saat toggle BYO nonaktif, termasuk Sync reader lain sesudah penolakan) ada di spec 020; TC-GS-HHR-81 ada di spec 075.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-82 dan TC-GS-HHR-83 ditulis bersuffix per run (`Reader Dock 01-{runId}-022`) mengikuti S-12.
- Temuan untuk QA:
  - Ketiga TC berlabel `Manual Only` (b) di TC sumber (reader USB fisik) tetapi tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-84 mengharapkan "aktivasi berhasil memakai SN-HHR-00201" tetapi hanya menyebut baris `Zebra RFID Reader - 2` ber-`Status` `Available`; spec mengasersi baris itu (nama bawaan dari nomor urut unit HS-01), tidak membaca `Serial Number` baris.
  - TC-GS-HHR-84 tidak menyebut toast sukses; spec tidak mengasersi toast.
