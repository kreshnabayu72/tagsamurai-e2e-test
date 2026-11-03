---
id: TC-AC-ACTS-E2E-226-modal-event-log-tab-add-stock-sort-bagian-2-siklus-search
title: "Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-100
  - TC-AC-ACTS-485
  - TC-AC-ACTS-486
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Dua sesi seed (TC-AC-ACTS-100) bertimestamp sama, dibedakan nilai kolom Success; sesi yang ditulis lebih akhir diketahui dari fixture BE.
- Tabel "Kolom sort kelas angka Tab Add Stock":

  | Kolom | Urutan Ascending |
  |---|---|
  | `Success` | kecil ke besar |
  | `Waiting for Approval` | kecil ke besar |
  | `Failed` | kecil ke besar |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-485: Sort 3-state kelas angka di modal Event Log (Tab Add Stock): Success, Waiting for Approval, Failed

4. Verifikasi tabel memuat sedikitnya satu baris

Langkah 5 sampai 10 diulang untuk setiap baris tabel "Kolom sort kelas angka Tab Add Stock" pada Prerequisites (3 iterasi).

5. Klik header kolom `<Kolom>` sekali
6. Verifikasi urutan kolom `<Kolom>` Ascending (↑) (<Urutan Ascending>)
7. Klik header kolom `<Kolom>` kedua kali
8. Verifikasi urutan kolom `<Kolom>` Descending (↓), terbalik dari urutan Ascending
9. Klik header kolom `<Kolom>` ketiga kali
10. Verifikasi indikator sort kolom `<Kolom>` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-100: Sort: sesi Event Log dengan timestamp sama, yang ditulis lebih akhir tampil lebih atas

11. Verifikasi dua sesi seed bertimestamp sama (dibedakan lewat nilai kolom Success) tampil pada tabel dengan sort Date Newest First
12. Verifikasi sesi yang ditulis lebih akhir berada lebih atas daripada sesi yang ditulis lebih awal

### TC-AC-ACTS-486: Siklus Search toolbar modal Event Log (Tab Add Stock): reveal, Enter, clear, collapse

13. Verifikasi sedikitnya satu baris Activity `Add Stock` dan satu baris Activity `Delete Stock` tampil pada tabel
14. Hover icon Search
15. Verifikasi tooltip `Search` tampil
16. Klik icon Search
17. Verifikasi input Search terbuka dengan fokus otomatis
18. Verifikasi input Search memiliki placeholder `Search by activity, hardware, or modified by...`
19. Ketik `delete stock` tanpa menekan Enter
20. Verifikasi tabel belum tersaring (baris Activity `Add Stock` masih tampil)
21. Verifikasi icon (✕) muncul di dalam input
22. Tekan Enter
23. Verifikasi tabel tersaring sesuai keyword `delete stock`
24. Klik icon (✕) pada input
25. Verifikasi input Search kosong
26. Verifikasi kursor tetap fokus di input Search
27. Verifikasi tabel masih menampilkan hasil search terakhir
28. Tekan Enter pada input kosong
29. Verifikasi tabel kembali menampilkan semua data
30. Ketik Search `delete stock`, tekan Enter
31. Klik icon panah (←)
32. Verifikasi kotak pencarian tertutup
33. Verifikasi keyword dikosongkan
34. Verifikasi tabel langsung kembali menampilkan semua data

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`.
- Pembanding (8b butir 2): langkah 4 memastikan tabel memuat sedikitnya satu baris sebelum asersi urutan sort pertama.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 5 sampai 10 diulang untuk setiap baris tabel "Kolom sort kelas angka Tab Add Stock" (3 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Alasan di atas sekitar 35 langkah: spec ini 46 langkah dihitung dengan ekspansi; seluruh blok memakai satu kelas harness dan satu dataset seed, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang diulang per baris tabel sah menurut bagian 8b butir 7.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-100 tidak menyebut cara mengetahui sesi mana yang ditulis lebih akhir; spec memakai penanda dari fixture BE.
