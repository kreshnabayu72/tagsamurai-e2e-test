---
id: TC-FA-TAG-E2E-017-screening-tab-to-be-returned-header-kolom-dan-format-sel-bagian-2
title: "Tab To Be Returned: Hover Return Group dan Current Holder, Nilai Kosong, Reason, Breadcrumb Antar Tab, Tag QR, dan Popup TAG Log"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-81
  - TC-FA-TAG-82
  - TC-FA-TAG-83
  - TC-FA-TAG-84
  - TC-FA-TAG-88
  - TC-FA-TAG-89
  - TC-FA-TAG-90
coverage:
  web: automated
---

# Tab To Be Returned: Hover Return Group dan Current Holder, Nilai Kosong, Reason, Breadcrumb Antar Tab, Tag QR, dan Popup TAG Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab To Be Returned (hanya dibaca, tidak diubah):

  | TAG Code | Tipe | Last Asset | Reason | Return Group | Current Holder |
  |---|---|---|---|---|---|
  | `RF-00071` | RFID | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. |
  | `RF-00088` | RFID | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. |
  | `NF-00092` | NFC | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. |

- Data tambahan (di-seed lewat fixture BE yang disediakan tim FE/BE; kode Tag tidak disebut di TC, lihat Temuan untuk QA):
  - TC-FA-TAG-81: Return Group `Disposal Center` berada di bawah group induk (hierarki `[Parent] > [Child]`).
  - TC-FA-TAG-82: pengguna `Dedi K.` tersimpan dengan nama lengkap di data user.
  - TC-FA-TAG-83: satu Tag To Be Returned yang saat dilepas tidak punya pemegang terakhir aset maupun pelaku disposal (snapshot Current Holder kosong).
  - TC-FA-TAG-84: satu Tag lama hasil Replace RFID/NFC pada Global berstatus Available atau Damaged/Missing, yang tidak berada di tabel To Be Returned.
  - TC-FA-TAG-89: aset bertag QR (`QR-00232`) yang disposal-nya selesai, dan Tag RFID `RF-00071` dari disposal yang sama.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-81: Hover badge Return Group menampilkan hierarki group penuh

1. Klik Tab `To Be Returned`
2. Arahkan kursor ke badge Return Group baris `RF-00071`
3. Verifikasi tooltip menampilkan hierarki group penuh dengan format `[Parent] > [Child]` untuk `Disposal Center`

### TC-FA-TAG-82: Hover Current Holder menampilkan nama lengkap

4. Arahkan kursor ke teks `Dedi K.` pada baris `RF-00071`
5. Verifikasi tooltip menampilkan nama lengkap pengguna `Dedi K.`

### TC-FA-TAG-83: Current Holder kosong tampil dengan tanda "—"

6. Periksa kolom `Current Holder` pada baris Tag yang snapshot Current Holder-nya kosong
7. Verifikasi sel `Current Holder` menampilkan `—`

### TC-FA-TAG-84: Kolom Reason hanya bernilai "Disposal"

8. Periksa seluruh nilai kolom `Reason`
9. Verifikasi sedikitnya satu baris Tag tampil pada tabel
10. Verifikasi semua baris menampilkan Reason `Disposal`
11. Ketik Search kode Tag lama hasil Replace, tekan Enter
12. Verifikasi empty state `No results found` tampil
13. Verifikasi Tag lama hasil Replace tidak muncul di tabel To Be Returned
14. Klik `(←)` pada kotak Search

### TC-FA-TAG-88: Breadcrumb mengikuti tab aktif saat berpindah antar tab

15. Buka menu Fixed Asset > TAG lewat sidebar
16. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired`
17. Klik Tab `To Be Returned`
18. Verifikasi Breadcrumb `Fixed Asset > TAG > To Be Returned`
19. Klik Tab `Paired`
20. Verifikasi Breadcrumb kembali `Fixed Asset > TAG > Paired`

### TC-FA-TAG-89: Tag QR tidak muncul di tabel To Be Returned

21. Klik Tab `To Be Returned`
22. Verifikasi baris `RF-00071` ada pada tabel
23. Verifikasi tabel hanya memuat Tag RFID atau NFC
24. Ketik Search `QR-00232`, tekan Enter
25. Verifikasi empty state `No results found` dan `Try adjusting your search or filter.` tampil
26. Klik `(←)` pada kotak Search

### TC-FA-TAG-90: Klik TAG Code di tab To Be Returned membuka Popup TAG Log read-only

27. Klik TAG Code `RF-00071` pada baris pertama
28. Verifikasi Popup TAG Log Tag `RF-00071` terbuka dan hanya memiliki ikon close
29. Verifikasi popup memuat riwayat status Tag dari Global Settings (read-only)
30. Verifikasi tidak ada aksi tulis pada popup
31. Klik ikon close pada Popup TAG Log

## Notes

- Langkah 6, 8, 14, 26, dan 31 adalah langkah penghubung atau pengamatan tanpa asersi (S-03, R-16). Langkah 11 dan 24 adalah Search yang menjadi bagian aksi TC-FA-TAG-84 dan TC-FA-TAG-89; kotak Search dikosongkan pada langkah 14 dan 26 (S-09).
- Langkah 15 membuka menu dari sidebar karena TC-FA-TAG-88 memulai dari tab Paired yang aktif.
- Langkah 13, 23, dan 30 adalah asersi absence; anchor positif adalah Verifikasi `No results found` (langkah 12), Verifikasi baris `RF-00071` ada (langkah 22), dan Verifikasi popup memuat riwayat status (langkah 29) pada surface yang sama (bagian 8b butir 2). Langkah 10 dan 23 yang memakai kuantor universal didahului Verifikasi sedikitnya satu baris tampil (langkah 9 dan 22) (bagian 8b butir 2).
- TC-FA-TAG-76 sampai 80 ada di spec 016. TC-FA-TAG-85 ada di spec 004, TC-FA-TAG-86 di spec 003, dan TC-FA-TAG-87 di spec resilience kelas b.
- Temuan untuk QA:
  - TC-FA-TAG-81 dan 82 tidak menyebut nama group induk `Disposal Center` maupun nama lengkap `Dedi K.`; spec mengasersi tooltip sesuai format TC dan menyerahkan nilai persis ke data seeding.
  - TC-FA-TAG-83 dan 84 tidak menyebut kode Tag yang dipakai (Tag tanpa Current Holder, Tag lama hasil Replace); spec memakai referensi fixture BE yang disediakan tim FE/BE.
  - TC-FA-TAG-84 Precondition c menyebut Tag lama berstatus Available atau Damaged/Missing sekaligus; spec memakai satu Tag lama saja dan tidak menguji kedua status.
  - TC-FA-TAG-84 Langkah 3 ("Cari Tag lama hasil Replace pada tabel") tidak menyebut cara mencari; spec memakai Search dengan kode Tag itu.
  - TC-FA-TAG-90 Expected b ("riwayat status Tag dari Global Settings") tidak menyebut isi riwayat; spec hanya mengasersi keberadaannya.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi kode, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
