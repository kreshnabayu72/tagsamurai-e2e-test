---
id: TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit
title: "Batas Plafon Total Master Data Count Limit pada Create dan Delete"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-188
  - TC-FA-CF-190
  - TC-FA-CF-324
  - TC-FA-CF-627
coverage:
  web: automated
---

# Batas Plafon Total Master Data Count Limit pada Create dan Delete

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas volume data (1000 sampai 1005 field per Company Plafon). Suite serial (`parallel: false`): spec mengubah state global Master Data Count Limit dan volume field Company Plafon.
- Akun aktor: Total Control Company Plafon `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Plafon (Pre-setup #17). Akun ini tidak tertulis sebagai baris sendiri di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PLAFON_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup Company Plafon (Pre-setup #17; seed fixture backend yang disediakan tim FE/BE, tidak ada endpoint yang dikarang). Varian per blok diatur lewat langkah "Atur backend" (pengaturan limit dan volume):
  - TC-FA-CF-190: Master Data Count Limit diturunkan ke 1000 saat 1005 field tersimpan.
  - TC-FA-CF-188, 324, dan 627: Master Data Count Limit 1000 dan tepat 1000 field; semua Scope `General` Inactive kecuali `Plafon Pump` (Active, Scope `Pump`). Varian ini dipakai berurutan oleh TC-FA-CF-188, 324, lalu 627 tanpa pengaturan ulang (TC-FA-CF-324 menonaktifkan `Plafon Pump`; TC-FA-CF-627 menghapusnya).
- Data Dinamis: tidak ada field baru yang dibuat oleh spec ini; `Plafon Pump` (data seed) menjadi target Deactivate dan Delete (S-06 pengecualian 2026-10-30: kuota total tidak dapat dimiliki spec; pemulihan ke keadaan awal dijamin seed Company Plafon yang disediakan tim FE/BE).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): kembalikan Company Plafon ke baseline (Master Data Count Limit 1000, volume dan `Plafon Pump` dipulihkan) lewat seed reset Company.
- Kemampuan teknis: pengaturan Master Data Count Limit dan volume field Company Plafon oleh backend (disediakan tim FE/BE; TC menyebut kebutuhan seed tetapi tidak mendefinisikan mekanismenya); pembacaan total record tabel (disediakan tim FE/BE).
- State global yang diubah: Master Data Count Limit dan volume field Company Plafon, status Active `Plafon Pump` dan keberadaan `Plafon Pump`; dipulihkan di hook `after`.

## Test Steps

### TC-FA-CF-190: Plafon diturunkan di bawah jumlah field yang ada tidak menghapus field dan hanya Create baru diblokir

1. Atur backend: Master Data Count Limit diturunkan ke 1000 saat tepat 1005 field tersimpan
2. Muat ulang halaman (F5)
3. Klik [+ Custom Field]
4. Verifikasi dialog `Limit Reached` tampil dengan `[Limit]` 1000: "You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit."
5. Verifikasi seluruh 1005 field yang ada tetap tersimpan dan tampil: total record tabel 1005
6. Klik `[OK]`

### TC-FA-CF-188: Klik tombol Create saat total custom field mencapai Master Data Count Limit menampilkan dialog blok

7. Atur backend: Master Data Count Limit 1000 dan tepat 1000 field tersimpan
8. Muat ulang halaman (F5)
9. Klik [+ Custom Field]
10. Verifikasi dialog blok 🔒 `Limit Reached` dengan teks "You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit." dan tombol `[OK]` tampil
11. Verifikasi modal Create tidak terbuka
12. Klik `[OK]`
13. Verifikasi dialog tertutup
14. Verifikasi tidak ada field baru: total record tabel tetap 1000

### TC-FA-CF-324: Deactivate tidak membebaskan plafon total

15. Ketik Search `Plafon Pump`, tekan Enter
16. Geser switch Active baris `Plafon Pump` ke OFF
17. Klik `[Deactivate]`
18. Klik `(←)` pada kotak Search
19. Klik [+ Custom Field]
20. Verifikasi dialog `Limit Reached` tampil karena Deactivate tidak mengurangi total field
21. Klik `[OK]`

### TC-FA-CF-627: Delete membebaskan plafon total sehingga tombol Create kembali membuka modal

22. Ketik Search `Plafon Pump`, tekan Enter
23. Klik row action `⋯` > `Delete` pada baris `Plafon Pump`, lalu klik `[Delete]`
24. Verifikasi field `Plafon Pump` terhapus: empty state "No results found" tampil
25. Klik `(←)` pada kotak Search
26. Verifikasi total record tabel menjadi 999
27. Klik [+ Custom Field]
28. Verifikasi modal Create terbuka
29. Verifikasi dialog `Limit Reached` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Kelas: volume data (kelas e, bagian 3 prinsip 13e; ambang 100 baris). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 190, 188, 324, 627 (urutan sumber 188, 190, 324, 627). Varian 1005 field lebih dulu karena tiap blok mengatur limit dan volume sendiri di awal blok ("Atur backend"); TC-FA-CF-188 dan TC-FA-CF-324 tidak mengurangi total field sehingga berbagi varian 1000 field; TC-FA-CF-627 menghapus data dan ditaruh paling akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 6, 7, 8, 12, 15, 18, 21, 22, 25 ("Atur backend" adalah pengaturan seed oleh tim FE/BE, F5 memuat ulang halaman, Search `Plafon Pump` menemukan baris target (R-16), `(←)` menutup Search, `[OK]` menutup dialog). Klik `[OK]` pada langkah 6 dan 21 tidak ada di Langkah Uji TC-FA-CF-190 dan TC-FA-CF-324; langkah itu menutup dialog sebelum blok berikutnya.
- Langkah 24 memakai empty state hasil Search sebagai anchor positif absence baris sesudah Delete (bagian 8b butir 2); langkah 26 membaca total record dan membutuhkan kemampuan baca total (Prerequisites).
- Pembagian TC lintas spec: TC-FA-CF-189 dan TC-FA-CF-617 (varian 999 field) ada di spec 168.
- Temuan untuk QA:
  - Akun Total Control Company Plafon tidak tertulis sebagai baris sendiri di Pre-setup TC (Pre-setup #1 hanya Company Alpha); ditulis "disediakan tim FE" (S-11).
  - TC-FA-CF-190: Expected b ("seluruh 1005 field tetap tersimpan dan tampil") membutuhkan pembacaan total record; kemampuan ini tidak didefinisikan di TC, PRD, atau LLD dan ditulis "disediakan tim FE/BE" (S-13).
  - TC-FA-CF-190 dan TC-FA-CF-324: Langkah Uji tidak menyebut klik `[OK]` pada dialog sesudah asersi; spec menambahkannya sebagai langkah penghubung (langkah 6 dan 21).
  - TC-FA-CF-188: Expected b menyebut "tidak ada field baru"; spec mengasersinya lewat total record tetap 1000.
  - TC-FA-CF-324: baris `Plafon Pump` ditemukan lewat Search karena TC tidak menyebut cara menemukan baris di antara 1000 baris.
