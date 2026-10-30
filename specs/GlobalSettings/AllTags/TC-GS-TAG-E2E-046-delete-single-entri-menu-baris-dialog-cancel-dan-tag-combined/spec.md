---
id: TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined
title: "Delete Single: Visibilitas Entri Delete per Status, Dialog dan Varian Peringatan, Cancel, dan Tag Combined"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-138
  - TC-GS-TAG-139
  - TC-GS-TAG-140
  - TC-GS-TAG-141
  - TC-GS-TAG-172
  - TC-GS-TAG-363
coverage:
  web: automated
---

# Delete Single: Visibilitas Entri Delete per Status, Dialog dan Varian Peringatan, Cancel, dan Tag Combined

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini hanya membuka menu baris dan dialog lalu `Cancel`; satu-satunya penghapusan adalah DD-15 lewat Delete by Scan sebagai langkah pembuka TC-GS-TAG-363.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; 30 baris, Paired 4, Not Paired 26). Identifier (EPC/NFC/BLE/QR) bersifat tetap dan tidak bisa bersufiks `{runId}` (S-12, Q-4); seeding idempotent lewat fixture BE di hook `before` memulihkan kondisi awal. Baris yang dipakai: DD-01 (Paired), DD-02 (Available), DD-03 (Waiting for Approval), DD-04 (Damaged/Missing), DD-06 (Reserved), DD-07 (To be Returned), DD-08 (Retired), DD-11 dan DD-13 (combined), DD-15..DD-18 (Available).
- Tabel "Menu tanpa Delete" (TC-GS-TAG-138 butir a): DD-01 `E2801160600002054D8A0001` (Paired), DD-06 `E2801160600002054D8A0006` (Reserved).
- Tabel "Menu dengan Delete" (TC-GS-TAG-138 butir b): DD-02 (Available), DD-07 (To be Returned), DD-04 (Damaged/Missing), DD-08 (Retired), DD-03 (Waiting for Approval).
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A; simulasi reader RFID untuk satu sesi Delete by Scan (D-4, Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-15 dipulihkan) lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri di atas dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-138: Visibilitas entri Delete di menu baris per status

1. Untuk setiap baris pada tabel "Menu tanpa Delete" (langkah 2 sampai 5):
2. Buka menu baris tersebut
3. Verifikasi menu hanya berisi `TAG Log`
4. Verifikasi entri `Delete` Hidden (bukan Disabled)
5. Tutup menu
6. Untuk setiap baris pada tabel "Menu dengan Delete" (langkah 7 sampai 10):
7. Buka menu baris tersebut
8. Verifikasi menu berisi `TAG Log` dan `Delete`
9. Verifikasi entri `Delete` enabled
10. Tutup menu

### TC-GS-TAG-139: Dialog Delete TAG

11. Buka menu baris DD-02 `E2801160600002054D8A0002`, lalu klik `Delete`
12. Verifikasi judul dialog `Delete TAG`
13. Verifikasi body memuat bullet `E2801160600002054D8A0002`
14. Verifikasi body memuat baris `This will free up license quota.`
15. Verifikasi body memuat baris `For more accurate results, use Delete by Scan.`
16. Verifikasi body memuat kalimat `Are you sure you want to delete it? This action cannot be undone.`
17. Verifikasi footer memuat tombol `Cancel` dan `Delete` (danger)
18. Klik `Cancel`
19. Verifikasi baris DD-02 tetap tampil di registri
20. Verifikasi tidak ada toast

### TC-GS-TAG-140: Varian peringatan Waiting for Approval

21. Buka menu baris DD-03 (Waiting for Approval), lalu klik `Delete`
22. Verifikasi dialog memuat baris peringatan `This will free up license quota and pending approval will be canceled.`
23. Klik `Cancel`

### TC-GS-TAG-141: Dialog Delete tag Retired

24. Buka menu baris DD-08 (Retired), lalu klik `Delete`
25. Verifikasi baris petunjuk `For more accurate results, use Delete by Scan.` tetap tampil
26. Verifikasi dialog tidak memuat baris peringatan
27. Klik `Cancel`

### TC-GS-TAG-172: Tag combined

28. Klik Tab Not Paired
29. Buka menu baris DD-11
30. Verifikasi menu hanya berisi `TAG Log` (entri `Delete` Hidden)
31. Tutup menu
32. Buka menu baris DD-13
33. Verifikasi menu hanya berisi `TAG Log` (entri `Delete` Hidden)
34. Tutup menu
35. Verifikasi checkbox baris DD-11 dan DD-13 Hidden

### TC-GS-TAG-363: Baris petunjuk Delete by Scan di dialog Delete manual dan Bulk Delete

36. Klik Tab All
37. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
38. Pindai DD-15 `E28011606000020F00000001`
39. Klik `Stop` pada widget
40. Buka menu baris DD-16, lalu klik `Delete`
41. Verifikasi dialog `Delete TAG` untuk DD-16 memuat baris `This will free up license quota.`
42. Verifikasi dialog `Delete TAG` untuk DD-16 memuat baris `For more accurate results, use Delete by Scan.`
43. Klik `Cancel`
44. Klik Tab Not Paired
45. Centang baris DD-17 dan DD-18
46. Pilih `Bulk Action` > `Delete`
47. Verifikasi dialog `Delete TAGs` untuk DD-17 dan DD-18 memuat baris `This will free up license quota.`
48. Verifikasi dialog `Delete TAGs` untuk DD-17 dan DD-18 memuat baris `For more accurate results, use Delete by Scan.`
49. Klik `Cancel`
50. Verifikasi DD-16, DD-17, dan DD-18 tetap tampil di registri (tidak ada baris yang terhapus)
51. Klik `(✕)` pada Bulk Action Bar untuk membatalkan seleksi

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tidak punya asersi absence log.
- Spec melewati sekitar 35 langkah (51 langkah nominal, sekitar 69 setelah ekspansi dua blok ulang: langkah 2 sampai 5 untuk 2 baris dan langkah 7 sampai 10 untuk 5 baris). Alasan: seluruh blok memakai satu dataset (Seed Registri A), satu kelas (FE+BE, hanya buka menu dan dialog lalu `Cancel`), dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang memakai idiom tabel di Prerequisites (langkah 1 dan 6).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 5 dan 10 (menutup menu), 23, 27, 43, dan 49 (`Cancel` pada dialog yang hanya diamati), 28 dan 36 (pindah tab sesuai precondition TC), 31 dan 34 (menutup menu), 51 (membersihkan seleksi).
- Perubahan urutan (S-05 butir terakhir): TC-GS-TAG-172 (screening menu) ditaruh sebelum TC-GS-TAG-363 karena langkah pembuka TC-GS-TAG-363 menghapus DD-15 lewat scan, sehingga bagian tanpa penghapusan lebih dulu.
- TC-GS-TAG-363 Langkah 37 sampai 39 memakai simulasi reader (D-4, Q-1) hanya sebagai pembuka; objek asersinya dialog Delete manual dan Bulk Delete. TC ini ditempatkan di spec fungsional sesuai rencana, padahal membutuhkan harness scan (kelas d).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - Q-4: identifier Seed Registri A tetap; hitungan dan baris yang dipakai valid hanya bila Seed Registri A dipulihkan sebelum spec.
  - TC-GS-TAG-172 Expected b menyebut checkbox DD-11 dan DD-13 "dilewati Select All" tetapi langkah TC tidak menjalankan Select All; spec hanya mengasersi checkbox Hidden. Perilaku dilewati Select All diasersi di spec 047 (TC-GS-TAG-150).
  - TC-GS-TAG-363 tidak memberi Expected untuk toast hasil pindai DD-15 (langkah 2), sehingga langkah 38 tidak punya `Verifikasi`.
  - Post Condition TC-GS-TAG-363 menyebut DD-16, DD-17, DD-18 tetap di registri; ini sama dengan Expected c (langkah 50). DD-15 yang terhapus oleh scan tidak disebut Post Condition.
  - Q-1: TC-GS-TAG-363 berlabel `Manual Only — (b)` untuk scan; kemampuan simulasi reader dicatat di Prerequisites sebagai kebutuhan resmi.
